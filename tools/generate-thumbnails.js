#!/usr/bin/env node
/**
 * generate-thumbnails.js
 *
 * Generates WebP thumbnail screenshots for Pixel Vault game files using
 * Playwright headless Chromium. Each game's canvas renders its first frame
 * (or ~2 seconds of gameplay), which is captured as a thumbnail.
 *
 * Output:
 *   thumbnails/{game-id}.webp       — 400×300 hero thumbnail
 *   thumbnails/{game-id}-sm.webp    — 200×150 card thumbnail
 *
 * Requirements:
 *   npm install playwright
 *   npx playwright install chromium
 *
 * Usage:
 *   node tools/generate-thumbnails.js                           # all allowed tracks
 *   node tools/generate-thumbnails.js --track=archetype         # one track
 *   node tools/generate-thumbnails.js --track=archetype,ai-archaeology
 *   node tools/generate-thumbnails.js --id=maz-001-pacman       # one game
 *   node tools/generate-thumbnails.js --limit=20                # first N games by track order
 *   node tools/generate-thumbnails.js --dry-run                 # show what would run, no output
 *   node tools/generate-thumbnails.js --force                   # regenerate even if thumb exists
 *   node tools/generate-thumbnails.js --serve-port=9000         # custom port for local server
 *
 * Notes:
 * - Runs a local HTTP server on a free port to serve game files (needed because
 *   canvas taints itself on file:// protocol for some games)
 * - ai-evolution track is excluded by default (use --track=ai-evolution to override)
 * - Games with status: broken in manifest.json are skipped automatically
 * - A game that crashes or produces a blank canvas after 3s gets a text placeholder
 *   thumbnail instead (series + name code) — never a broken image
 */

'use strict';

const path = require('path');
const fs = require('fs');
const http = require('http');
const { execSync } = require('child_process');

// ── Playwright (graceful failure if not installed) ──────────────────────────
let playwright;
try {
  playwright = require('playwright');
} catch (_e) {
  console.error('');
  console.error('ERROR: playwright is not installed.');
  console.error('  Run: npm install playwright && npx playwright install chromium');
  console.error('');
  process.exit(1);
}

// ── Sharp for resizing (optional — falls back to Playwright's clip if absent) ──
let sharp;
try {
  sharp = require('sharp');
} catch (_e) {
  sharp = null;
}

// ── Config ───────────────────────────────────────────────────────────────────
const REPO_ROOT = path.resolve(__dirname, '..');
const MANIFEST_PATH = path.join(REPO_ROOT, 'manifest.json');
const THUMBS_DIR = path.join(REPO_ROOT, 'thumbnails');
const GAME_WIDTH = 800;
const GAME_HEIGHT = 600;
const THUMB_HERO_W = 400;
const THUMB_HERO_H = 300;
const THUMB_CARD_W = 200;
const THUMB_CARD_H = 150;
const WAIT_MS = 2500;        // time to let game canvas render before screenshot
const TIMEOUT_MS = 10000;    // max time per game before giving up
const CONCURRENCY = 3;       // parallel browser tabs (increase with caution)

// Default allowed tracks — mirrors pv-deploy-play.sh
const DEFAULT_ALLOWED_TRACKS = new Set(['archetype', 'ai-archaeology']);

// ── Parse args ───────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const getArg = (prefix) => {
  const arg = args.find(a => a.startsWith(prefix));
  return arg ? arg.split('=')[1] : null;
};

const DRY_RUN     = args.includes('--dry-run');
const FORCE       = args.includes('--force');
const TRACK_FILTER = getArg('--track');     // "archetype" or "archetype,ai-archaeology"
const ID_FILTER    = getArg('--id');        // exact game id
const LIMIT        = parseInt(getArg('--limit') || '0', 10);
const SERVE_PORT   = parseInt(getArg('--serve-port') || '0', 10) || null;

const allowedTracks = TRACK_FILTER
  ? new Set(TRACK_FILTER.split(',').map(t => t.trim()))
  : DEFAULT_ALLOWED_TRACKS;

function titleCaseFromSlug(value) {
  return String(value || '')
    .split('-')
    .filter(Boolean)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function escapeXml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

async function primePageForThumbnail(page) {
  const actions = [
    async () => page.keyboard.press('Enter'),
    async () => page.keyboard.press('Space'),
    async () => page.mouse.click(GAME_WIDTH / 2, GAME_HEIGHT / 2),
  ];

  for (const action of actions) {
    try {
      await action();
      await page.waitForTimeout(180);
    } catch (_err) {
      // Ignore input failures and keep priming with the next common start action.
    }
  }
}

async function writeThumbnail(buffer, width, height, outPath, game) {
  const title = titleCaseFromSlug(game.name || game.id || 'pixel-vault');
  const ribbonHeight = width >= THUMB_HERO_W ? 54 : 38;
  const fontSize = width >= THUMB_HERO_W ? 24 : 16;
  const seriesLabel = `${String(game.series || 'pv').toUpperCase()}-${String(game.number || '').padStart(3, '0')}`;
  const svg = `
    <svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="${height - ribbonHeight}" width="${width}" height="${ribbonHeight}" fill="rgba(7,10,16,0.84)"/>
      <rect x="0" y="${height - ribbonHeight}" width="${width}" height="2" fill="rgba(100,200,255,0.72)"/>
      <text x="14" y="${height - ribbonHeight + 18}" fill="rgba(100,200,255,0.95)" font-family="Arial, sans-serif" font-size="${Math.max(11, Math.floor(fontSize * 0.5))}" font-weight="700">${escapeXml(seriesLabel)}</text>
      <text x="14" y="${height - 12}" fill="#f8fafc" font-family="Arial, sans-serif" font-size="${fontSize}" font-weight="700">${escapeXml(title)}</text>
    </svg>`;

  await sharp(buffer)
    .resize(width, height, { fit: 'cover' })
    .composite([{ input: Buffer.from(svg), top: 0, left: 0 }])
    .webp({ quality: width >= THUMB_HERO_W ? 82 : 80 })
    .toFile(outPath);
}

// ── Load manifest ─────────────────────────────────────────────────────────────
if (!fs.existsSync(MANIFEST_PATH)) {
  console.error('ERROR: manifest.json not found. Run: python3 tools/catalogue-generator.py');
  process.exit(1);
}
const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
const allGames = manifest.prototypes || [];

// ── Filter games ──────────────────────────────────────────────────────────────
let games = allGames.filter(g => {
  if (!allowedTracks.has(g.track || 'archetype'))   return false;
  if (g.status === 'broken')                         return false;
  if (!g.file || !fs.existsSync(path.join(REPO_ROOT, g.file))) return false;
  if (ID_FILTER && g.id !== ID_FILTER)               return false;
  return true;
});

if (!FORCE) {
  // Skip games that already have a thumbnail
  games = games.filter(g => {
    const heroPath = path.join(THUMBS_DIR, `${g.id}.webp`);
    return !fs.existsSync(heroPath);
  });
}

if (LIMIT > 0) games = games.slice(0, LIMIT);

console.log('');
console.log('╔══════════════════════════════════════════════════════╗');
console.log('║       PIXEL VAULT — THUMBNAIL GENERATOR             ║');
console.log('╚══════════════════════════════════════════════════════╝');
console.log('');
console.log(`  Tracks     : ${[...allowedTracks].join(', ')}`);
console.log(`  Total in manifest : ${allGames.length}`);
console.log(`  To generate       : ${games.length}${FORCE ? ' (--force: regenerating existing)' : ''}`);
if (DRY_RUN) console.log('  DRY RUN — no files will be written');
console.log('');

if (games.length === 0) {
  console.log('No games to process. All thumbnails may already exist (use --force to regenerate).');
  process.exit(0);
}

if (DRY_RUN) {
  console.log('Games that would be processed:');
  games.forEach(g => console.log(`  ${g.id}  →  thumbnails/${g.id}.webp`));
  console.log('');
  process.exit(0);
}

// ── Create thumbnails directory ───────────────────────────────────────────────
if (!fs.existsSync(THUMBS_DIR)) {
  fs.mkdirSync(THUMBS_DIR, { recursive: true });
}

// ── Start local HTTP server ───────────────────────────────────────────────────
function startServer(root, preferredPort) {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      const safePath = req.url.split('?')[0];
      const filePath = path.join(root, decodeURIComponent(safePath));

      // Path traversal protection
      if (!filePath.startsWith(root)) {
        res.writeHead(403);
        res.end('Forbidden');
        return;
      }

      if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }

      const ext = path.extname(filePath).toLowerCase();
      const mimeTypes = {
        '.html': 'text/html; charset=utf-8',
        '.js':   'application/javascript',
        '.css':  'text/css',
        '.webp': 'image/webp',
        '.png':  'image/png',
        '.jpg':  'image/jpeg',
        '.json': 'application/json',
      };
      const mime = mimeTypes[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': mime });
      fs.createReadStream(filePath).pipe(res);
    });

    server.listen(preferredPort || 0, '127.0.0.1', () => {
      const port = server.address().port;
      resolve({ server, port });
    });
  });
}

// ── Generate placeholder thumbnail (text on canvas) ────────────────────────
async function generatePlaceholder(game) {
  // Use Playwright to render a simple canvas with series + name
  const browser = await playwright.chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: GAME_WIDTH, height: GAME_HEIGHT });

  const series = (game.series || 'UNK').toUpperCase();
  const gameName = (game.name || game.id || 'Unknown').toUpperCase();

  await page.setContent(`<!DOCTYPE html>
<html><body style="margin:0;background:#0a0d14">
<canvas id="c" width="${GAME_WIDTH}" height="${GAME_HEIGHT}"></canvas>
<script>
const ctx = document.getElementById('c').getContext('2d');
ctx.fillStyle = '#0a0d14';
ctx.fillRect(0, 0, ${GAME_WIDTH}, ${GAME_HEIGHT});
// Grid pattern
ctx.strokeStyle = 'rgba(255,255,255,0.05)';
ctx.lineWidth = 1;
for (let x = 0; x <= ${GAME_WIDTH}; x += 40) { ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,${GAME_HEIGHT}); ctx.stroke(); }
for (let y = 0; y <= ${GAME_HEIGHT}; y += 40) { ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(${GAME_WIDTH},y); ctx.stroke(); }
// Border
ctx.strokeStyle = 'rgba(100,200,255,0.3)';
ctx.lineWidth = 2;
ctx.strokeRect(2, 2, ${GAME_WIDTH}-4, ${GAME_HEIGHT}-4);
// Series badge
ctx.fillStyle = 'rgba(100,200,255,0.2)';
ctx.fillRect(${GAME_WIDTH/2 - 60}, ${GAME_HEIGHT/2 - 80}, 120, 50);
ctx.fillStyle = '#64c8ff';
ctx.font = 'bold 28px "Courier New", monospace';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillText('${series}', ${GAME_WIDTH/2}, ${GAME_HEIGHT/2 - 55});
// Name
ctx.fillStyle = '#e2e8f0';
ctx.font = 'bold 20px "Courier New", monospace';
const name = '${gameName.substring(0, 24)}';
ctx.fillText(name, ${GAME_WIDTH/2}, ${GAME_HEIGHT/2 + 10});
// Subtext
ctx.fillStyle = 'rgba(148,163,184,0.6)';
ctx.font = '14px "Courier New", monospace';
ctx.fillText('PIXEL VAULT', ${GAME_WIDTH/2}, ${GAME_HEIGHT/2 + 50});
</script></body></html>`);

  await page.waitForTimeout(500);
  const screenshotBuffer = await page.screenshot({ type: 'png' });
  await browser.close();
  return screenshotBuffer;
}

// ── Process one game ──────────────────────────────────────────────────────────
async function processGame(game, port) {
  const gameUrl = `http://127.0.0.1:${port}/${game.file}`;
  const heroPath  = path.join(THUMBS_DIR, `${game.id}.webp`);
  const cardPath  = path.join(THUMBS_DIR, `${game.id}-sm.webp`);

  let browser;
  let screenshotBuffer;
  let usedPlaceholder = false;

  try {
    browser = await playwright.chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });
    const context = await browser.newContext({
      viewport: { width: GAME_WIDTH, height: GAME_HEIGHT },
    });
    const page = await context.newPage();

    // Suppress console noise from games
    page.on('console', () => {});
    page.on('pageerror', () => {});

    await page.goto(gameUrl, { timeout: TIMEOUT_MS, waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(250);
    await primePageForThumbnail(page);

    // Wait for canvas to render (games start immediately on load)
    await page.waitForTimeout(WAIT_MS);

    // Check if canvas has rendered anything (not all black)
    const canvasIsBlank = await page.evaluate(() => {
      const canvas = document.querySelector('canvas');
      if (!canvas) return true;
      const ctx = canvas.getContext('2d');
      const data = ctx.getImageData(0, 0, Math.min(canvas.width, 100), Math.min(canvas.height, 100)).data;
      const allBlack = data.every((v, i) => i % 4 === 3 || v < 5);
      return allBlack;
    }).catch(() => true);

    if (canvasIsBlank) {
      throw new Error('Canvas appears blank after render wait');
    }

    screenshotBuffer = await page.screenshot({
      type: 'png',
      clip: { x: 0, y: 0, width: GAME_WIDTH, height: GAME_HEIGHT },
    });
  } catch (err) {
    // Game crashed or timed out — generate a placeholder
    usedPlaceholder = true;
    screenshotBuffer = await generatePlaceholder(game);
  } finally {
    if (browser) await browser.close().catch(() => {});
  }

  // Save hero and card thumbnails
  if (sharp) {
    // Use sharp for high-quality resize plus a sanitized title ribbon.
    await writeThumbnail(screenshotBuffer, THUMB_HERO_W, THUMB_HERO_H, heroPath, game);
    await writeThumbnail(screenshotBuffer, THUMB_CARD_W, THUMB_CARD_H, cardPath, game);
  } else {
    // Fall back to Playwright's clip for correct size
    // Note: quality is lower without sharp — install it for better output
    fs.writeFileSync(heroPath, screenshotBuffer);
    fs.writeFileSync(cardPath, screenshotBuffer);
  }

  return { success: true, placeholder: usedPlaceholder };
}

// ── Concurrency pool ──────────────────────────────────────────────────────────
async function runWithConcurrency(tasks, concurrency) {
  const results = [];
  let idx = 0;

  async function worker() {
    while (idx < tasks.length) {
      const i = idx++;
      results[i] = await tasks[i]();
    }
  }

  const workers = Array.from({ length: concurrency }, () => worker());
  await Promise.all(workers);
  return results;
}

// ── Main ──────────────────────────────────────────────────────────────────────
(async () => {
  // Start local server
  const { server, port } = await startServer(REPO_ROOT, SERVE_PORT);
  const actualPort = SERVE_PORT || port;
  console.log(`  HTTP server : http://127.0.0.1:${actualPort}`);
  console.log(`  Output dir  : ${THUMBS_DIR}`);
  console.log(`  Concurrency : ${CONCURRENCY} parallel tabs`);
  if (!sharp) {
    console.log(`  [WARN] sharp not installed — thumbnails will be unresized PNG`);
    console.log(`         Run: npm install sharp  for proper WebP output`);
  }
  console.log('');

  let succeeded = 0;
  let failed = 0;
  let placeholders = 0;

  const tasks = games.map((game, i) => async () => {
    const progress = `[${String(i + 1).padStart(3)}/${games.length}]`;
    process.stdout.write(`  ${progress} ${game.id.padEnd(40)}`);

    try {
      const result = await processGame(game, actualPort);
      if (result.placeholder) {
        placeholders++;
        console.log('  [PLACEHOLDER]');
      } else {
        succeeded++;
        console.log('  ✓');
      }
    } catch (err) {
      failed++;
      console.log(`  ✗ ${err.message}`);
    }
  });

  await runWithConcurrency(tasks, CONCURRENCY);

  server.close();

  // ── Summary ────────────────────────────────────────────────────────────────
  const totalGenerated = fs.readdirSync(THUMBS_DIR).filter(f => f.endsWith('.webp') && !f.endsWith('-sm.webp')).length;

  console.log('');
  console.log('── Summary ──────────────────────────────────────────────');
  console.log(`  Generated   : ${succeeded} real screenshots`);
  console.log(`  Placeholder : ${placeholders} (game crashed or blank canvas)`);
  console.log(`  Failed      : ${failed} (unexpected errors)`);
  console.log(`  Total hero  : ${totalGenerated} WebP files in thumbnails/`);
  console.log('');
  console.log('  Next steps:');
  console.log('    1. Review generated thumbnails/ folder visually');
  console.log('    2. Re-run with --force --id=<id> to regenerate specific games');
  console.log('    3. Deploy to staging with thumbnails:');
  console.log('         bash scripts/pv-deploy-staging.sh --force');
  console.log('    4. Deploy to production:');
  console.log('         bash scripts/pv-deploy-play.sh --include-assets');
  console.log('');
})();
