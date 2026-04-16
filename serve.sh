#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# Pixel Vault — Development Server
#
# Starts a local server with no-cache headers. Serves ALL features:
#   http://localhost:8080/                    → Dev gallery (browse & play)
#   http://localhost:8080/tools/qa-dashboard.html → QA testing dashboard
#   http://localhost:8080/public/             → Public gallery (monetization wrapper)
#   http://localhost:8080/compendium.html     → Historical compendium
#   http://localhost:8080/docs/               → Documentation
#
# Usage:
#   bash serve.sh          # Start server on port 8080
#   bash serve.sh 9090     # Start on custom port
# ─────────────────────────────────────────────────────────────────
set -euo pipefail

PORT="${1:-8080}"
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Kill any existing server on this port
lsof -ti:$PORT 2>/dev/null | xargs kill -9 2>/dev/null || true
sleep 0.5

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║           PIXEL VAULT — DEVELOPMENT SERVER           ║"
echo "╠══════════════════════════════════════════════════════╣"
echo "║                                                      ║"
echo "║  🎮  Game Arcade:                                    ║"
echo "║      http://localhost:$PORT/                         ║"
echo "║                                                      ║"
echo "║  🔍  QA Dashboard:                                   ║"
echo "║      http://localhost:$PORT/tools/qa-dashboard.html  ║"
echo "║                                                      ║"
echo "║  🌐  Public Gallery (monetization preview):          ║"
echo "║      http://localhost:$PORT/public/                  ║"
echo "║                                                      ║"
echo "║  📖  Compendium:                                     ║"
echo "║      http://localhost:$PORT/compendium.html          ║"
echo "║                                                      ║"
echo "║  📊  Catalogue:                                      ║"
echo "║      http://localhost:$PORT/CATALOGUE.md             ║"
echo "║                                                      ║"
echo "║  Games: $(find prototypes ai-archaeology ai-evolution -name '*.html' 2>/dev/null | wc -l | tr -d ' ') prototypes                               ║"
echo "║  Press Ctrl+C to stop                                ║"
echo "║                                                      ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Start server with no-cache headers for development
python3 -c "
import http.server, os
os.chdir('$DIR')

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    def log_message(self, format, *args):
        # Only log non-200 requests to keep output clean
        if '200' not in str(args[1] if len(args) > 1 else ''):
            super().log_message(format, *args)

print(f'Serving on http://localhost:$PORT ...')
http.server.HTTPServer(('', $PORT), NoCacheHandler).serve_forever()
"
