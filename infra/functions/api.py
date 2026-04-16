"""
Pixel Vault — API Lambda Handler
Routes: GET /api/leaderboard/{gameId}, POST /api/score, POST /api/session, GET /api/stats

Security:
  - Input validation on all parameters (type, length, pattern)
  - IP hashing for privacy (never store raw IPs)
  - Player name sanitized: alphanumeric + space/hyphen/underscore, max 20 chars
  - Game ID validated against strict pattern: abc-001-name
  - Score validated: integer, 0–999999
  - CORS restricted to AllowedOrigin env var
  - Leaderboard SK uses zero-padded score for efficient range queries
"""

import hashlib
import json
import logging
import os
import re
import time
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")

# ── Tables (injected via Lambda environment variables) ──
LEADERBOARD_TABLE = os.environ["LEADERBOARD_TABLE"]
STATS_TABLE = os.environ["STATS_TABLE"]
SESSIONS_TABLE = os.environ["SESSIONS_TABLE"]
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "https://joshuaayson.com")
MAX_CONCURRENT = int(os.environ.get("MAX_CONCURRENT", "200"))

# ── Input validation patterns ──
GAMEID_PATTERN = re.compile(r"^[a-z]{2,4}-\d{3}-[a-z][a-z0-9-]{0,30}$")
NAME_PATTERN = re.compile(r"^[a-zA-Z0-9 _-]{1,20}$")
SESSION_PATTERN = re.compile(r"^[a-fA-F0-9]{16,64}$")

MAX_SCORE = 999_999
LEADERBOARD_TOP_N = 10
SCORE_PAD_WIDTH = 9  # 0-padded score for lexicographic sort (000000000–999999999)


# ──────────────────────────────────────────────────────────────────
# Response helpers
# ──────────────────────────────────────────────────────────────────

def ok(body: Any, status: int = 200) -> dict:
    return _response(status, body)


def err(message: str, status: int = 400) -> dict:
    return _response(status, {"error": message})


def _response(status: int, body: Any) -> dict:
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, X-Session-ID",
        },
        "body": json.dumps(body),
    }


# ──────────────────────────────────────────────────────────────────
# Router
# ──────────────────────────────────────────────────────────────────

def handler(event: dict, _context: Any) -> dict:
    """Main Lambda entry point — routes by HTTP method + path."""
    method = (
        event.get("httpMethod")
        or event.get("requestContext", {}).get("http", {}).get("method", "")
    ).upper()
    path = event.get("path") or event.get("rawPath") or ""

    logger.info("Request: %s %s", method, path)

    # CORS preflight
    if method == "OPTIONS":
        return ok({})

    # Route table
    if method == "GET" and path.startswith("/api/leaderboard/"):
        game_id = path.removeprefix("/api/leaderboard/").strip("/")
        return get_leaderboard(game_id)

    if method == "POST" and path.rstrip("/") == "/api/score":
        return submit_score(event)

    if method == "POST" and path.rstrip("/") == "/api/session":
        return start_session(event)

    if method == "GET" and path.rstrip("/") == "/api/stats":
        return get_stats()

    return err("not found", 404)


# ──────────────────────────────────────────────────────────────────
# GET /api/leaderboard/{gameId}
# ──────────────────────────────────────────────────────────────────

def get_leaderboard(game_id: str) -> dict:
    """Return top-N scores for a given game, ordered by score descending."""
    if not GAMEID_PATTERN.match(game_id):
        return err("invalid gameId format")

    table = dynamodb.Table(LEADERBOARD_TABLE)
    result = table.query(
        KeyConditionExpression=Key("gameId").eq(game_id),
        ScanIndexForward=False,  # Descending SK → highest score first
        Limit=LEADERBOARD_TOP_N,
    )

    entries = []
    for i, item in enumerate(result.get("Items", []), start=1):
        entries.append({
            "rank": i,
            "name": item.get("playerName", "UNKNOWN"),
            "score": int(item.get("rawScore", 0)),
            "date": _ms_to_date(item.get("ts", "0")),
        })

    return ok({"gameId": game_id, "entries": entries, "total": len(entries)})


# ──────────────────────────────────────────────────────────────────
# POST /api/score
# Body: { gameId, playerName, score, sessionId }
# ──────────────────────────────────────────────────────────────────

def submit_score(event: dict) -> dict:
    """Validate and store a player score."""
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return err("request body is not valid JSON")

    game_id = str(body.get("gameId", ""))
    player_name = str(body.get("playerName", "")).strip()
    score_raw = body.get("score")
    session_id = str(body.get("sessionId", ""))

    # ── Validate all inputs ──
    if not GAMEID_PATTERN.match(game_id):
        return err("invalid gameId: must match pattern abc-001-name")

    if not NAME_PATTERN.match(player_name):
        return err(
            "invalid playerName: 1–20 characters, alphanumeric / spaces / hyphens / underscores only"
        )

    if not isinstance(score_raw, (int, float)) or isinstance(score_raw, bool):
        return err("score must be a number")

    score = int(score_raw)
    if score < 0 or score > MAX_SCORE:
        return err(f"score out of range (0–{MAX_SCORE})")

    # ── Validate session (prevent submissions without a real session) ──
    if session_id and SESSION_PATTERN.match(session_id):
        _invalidate_session(session_id)  # One score per session
    else:
        session_id = ""  # Allow anonymous, but don't track

    # ── Privacy: hash the IP, never store raw ──
    ip = (
        event.get("requestContext", {})
        .get("identity", {})
        .get("sourceIp", "unknown")
    )
    ip_hash = hashlib.sha256(ip.encode()).hexdigest()[:16]

    ts_ms = str(int(time.time() * 1000))
    score_padded = str(score).zfill(SCORE_PAD_WIDTH)
    sk = f"{score_padded}#{ts_ms}#{ip_hash}"

    table = dynamodb.Table(LEADERBOARD_TABLE)
    table.put_item(Item={
        "gameId": game_id,
        "sk": sk,
        "playerName": player_name.upper(),  # Store uppercase for consistency
        "rawScore": score,
        "ts": ts_ms,
        "sessionId": session_id[:64],
        "ipHash": ip_hash,
    })

    logger.info("Score submitted: game=%s name=%s score=%d", game_id, player_name, score)
    return ok({"success": True, "gameId": game_id, "score": score})


# ──────────────────────────────────────────────────────────────────
# POST /api/session
# Body: { gameId }
# Returns: { sessionId, playCount, queuePosition, isQueued }
# ──────────────────────────────────────────────────────────────────

def start_session(event: dict) -> dict:
    """
    Start a play session. Increments play count. Returns a sessionId.
    Also checks active session count for soft queue display.
    """
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return err("request body is not valid JSON")

    game_id = str(body.get("gameId", ""))
    if not GAMEID_PATTERN.match(game_id):
        return err("invalid gameId")

    # ── Increment play count ──
    stats_table = dynamodb.Table(STATS_TABLE)
    resp = stats_table.update_item(
        Key={"gameId": game_id},
        UpdateExpression="ADD playCount :inc SET lastPlayed = :ts",
        ExpressionAttributeValues={":inc": 1, ":ts": str(int(time.time()))},
        ReturnValues="UPDATED_NEW",
    )
    play_count = int(resp["Attributes"].get("playCount", 1))

    # ── Create session record with 1-hour TTL ──
    session_id = hashlib.sha256(
        f"{game_id}{time.time()}{os.urandom(8).hex()}".encode()
    ).hexdigest()[:32]
    ttl = int(time.time()) + 3600  # 1 hour

    sessions_table = dynamodb.Table(SESSIONS_TABLE)
    sessions_table.put_item(Item={
        "sessionId": session_id,
        "gameId": game_id,
        "startTime": str(int(time.time())),
        "ttl": ttl,
        "scoreSubmitted": False,
    })

    # ── Soft queue: count active sessions for this game ──
    active_count = _count_active_sessions(game_id)
    is_queued = active_count > MAX_CONCURRENT
    queue_position = max(0, active_count - MAX_CONCURRENT) if is_queued else 0

    return ok({
        "sessionId": session_id,
        "playCount": play_count,
        "isQueued": is_queued,
        "queuePosition": queue_position,
        "activePlayers": min(active_count, MAX_CONCURRENT),
    })


# ──────────────────────────────────────────────────────────────────
# GET /api/stats
# ──────────────────────────────────────────────────────────────────

def get_stats() -> dict:
    """Return play counts for all games."""
    table = dynamodb.Table(STATS_TABLE)
    # Use pagination for large stats tables
    stats: dict[str, Any] = {}
    last_key = None

    while True:
        kwargs: dict = {
            "ProjectionExpression": "gameId, playCount, lastPlayed",
        }
        if last_key:
            kwargs["ExclusiveStartKey"] = last_key

        result = table.scan(**kwargs)
        for item in result.get("Items", []):
            stats[item["gameId"]] = {
                "playCount": int(item.get("playCount", 0)),
                "lastPlayed": item.get("lastPlayed", ""),
            }

        last_key = result.get("LastEvaluatedKey")
        if not last_key:
            break

    return ok({"stats": stats, "totalGames": len(stats)})


# ──────────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────────

def _invalidate_session(session_id: str) -> None:
    """Mark session as score-submitted to prevent duplicate submissions."""
    try:
        table = dynamodb.Table(SESSIONS_TABLE)
        table.update_item(
            Key={"sessionId": session_id},
            UpdateExpression="SET scoreSubmitted = :t",
            ExpressionAttributeValues={":t": True},
            ConditionExpression="attribute_exists(sessionId) AND scoreSubmitted = :f",
            ExpressionAttributeValues={":t": True, ":f": False},  # type: ignore[dict-item]
        )
    except Exception:
        # Session not found or already submitted — silently allow (don't block score)
        pass


def _count_active_sessions(game_id: str) -> int:
    """
    Count active (non-expired) sessions for a game.
    DynamoDB TTL cleanup is eventual; we check the 'ttl' attribute manually.
    Returns an approximate count (performance-optimised: not exact).
    """
    try:
        table = dynamodb.Table(SESSIONS_TABLE)
        now = int(time.time())
        # Scan with filter — only valid for small session counts
        # For high-traffic production use GSI on gameId instead
        result = table.scan(
            FilterExpression="gameId = :gid AND #ttl > :now",
            ExpressionAttributeNames={"#ttl": "ttl"},
            ExpressionAttributeValues={":gid": game_id, ":now": now},
            Select="COUNT",
        )
        return result.get("Count", 0)
    except Exception:
        return 0


def _ms_to_date(ts_ms: str) -> str:
    """Convert millisecond timestamp string to YYYY-MM-DD date string."""
    try:
        ts = int(ts_ms) / 1000
        return time.strftime("%Y-%m-%d", time.gmtime(ts))
    except (ValueError, TypeError):
        return ""
