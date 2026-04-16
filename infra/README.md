# Pixel Vault — Infrastructure

Serverless AWS backend for leaderboards, play stats, and session tracking.

**Stack:** AWS SAM → API Gateway (HTTP) + Lambda (Python 3.11) + DynamoDB + WAF

---

## Architecture

```
CloudFront (joshuaayson.com)
  /pixel-vault/*    → S3 bucket (static games + gallery)
  /pixel-vault/api/* → API Gateway → Lambda → DynamoDB
                                  ↑
                              WAF WebACL
                         (rate limit + OWASP rules)
```

### DynamoDB Tables

| Table | Purpose | Key |
|-------|---------|-----|
| `pixelvault-leaderboard-{env}` | Player scores | PK: gameId, SK: score_padded#timestamp#iphash |
| `pixelvault-stats-{env}` | Play counts | PK: gameId |
| `pixelvault-sessions-{env}` | Active sessions (TTL: 1hr) | PK: sessionId |

### API Routes

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/leaderboard/{gameId}` | Top 10 scores for a game |
| POST | `/api/score` | Submit a player score |
| POST | `/api/session` | Start a play session, get sessionId + play count |
| GET | `/api/stats` | Play counts for all games |

---

## Local Development

```bash
# Prerequisites: AWS SAM CLI, AWS credentials configured

# Install Python deps for local testing
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Build
sam build

# Local API test (requires Docker)
sam local start-api --env-vars env.json

# Invoke single function
sam local invoke ApiFunction --event events/leaderboard-get.json
```

### `env.json` for local testing (gitignored)
```json
{
  "ApiFunction": {
    "LEADERBOARD_TABLE": "pixelvault-leaderboard-development",
    "STATS_TABLE": "pixelvault-stats-development",
    "SESSIONS_TABLE": "pixelvault-sessions-development",
    "ALLOWED_ORIGIN": "http://localhost:8080",
    "MAX_CONCURRENT": "10",
    "ENVIRONMENT": "development"
  }
}
```

---

## Deployment

### First-time setup

```bash
# Deploy to production (interactive — sets up samconfig.toml)
sam build
sam deploy --guided --parameter-overrides \
    Environment=production \
    AllowedOrigin=https://joshuaayson.com \
    RateLimit=100

# Note the output: ApiEndpoint URL
# Add this to your publish-config.json as apiUrl
```

### Subsequent deployments

```bash
sam build && sam deploy
```

### Attach WAF to CloudFront (if using CloudFront instead of API GW directly)

The WAF in `template.yaml` is REGIONAL scope for API Gateway.
To protect the CloudFront distribution itself, create a separate CLOUDFRONT-scope
WAF in us-east-1 and associate it with your CloudFront distribution.

---

## CloudFront Path Routing Setup

To serve API through `joshuaayson.com/pixel-vault/api/*`, add a CloudFront
behavior in your CDK stack:

```typescript
// In your CDK stack
distribution.addBehavior('/pixel-vault/api/*', new origins.HttpOrigin(apiGatewayDomain), {
  allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
  cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
  originRequestPolicy: cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
});
```

This makes the API appear same-origin, satisfying `connect-src 'self'` CSP.

---

## Security Notes

- Raw IPs are never stored — only a 16-char SHA-256 hash for abuse detection
- Player names validated server-side: `^[a-zA-Z0-9 _-]{1,20}$`
- Game IDs validated against strict regex: `^[a-z]{2,4}-\d{3}-[a-z][a-z0-9-]{0,30}$`
- WAF rate limit: 100 requests / 5 minutes per IP
- AWS Managed Rules cover OWASP Top 10, SQL injection, XSS, known bad inputs
- Sessions table uses DynamoDB TTL (1 hour) — auto-purge prevents unbounded growth
- Score submissions require an active sessionId to prevent bare API abuse
