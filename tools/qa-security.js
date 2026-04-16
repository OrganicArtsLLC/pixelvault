#!/usr/bin/env node
/**
 * QA Security Scanner — Check all game files for security vulnerabilities
 *
 * Scans for: XSS vectors, code injection, data exfiltration, CSP violations,
 * unsafe DOM manipulation, external resource loading, eval/Function usage,
 * localStorage abuse, and postMessage risks.
 *
 * Usage:
 *   node tools/qa-security.js              # Scan all games
 *   node tools/qa-security.js --fix        # Show fix suggestions
 */

const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.resolve(__dirname, '..');
const args = process.argv.slice(2);
const showFixes = args.includes('--fix');

function findGameFiles(dir) {
  const results = [];
  if (!fs.existsSync(dir)) return results;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) results.push(...findGameFiles(full));
    else if (entry.name.endsWith('.html') && !entry.name.startsWith('.')) results.push(full);
  }
  return results;
}

let files = [];
for (const dir of ['prototypes', 'ai-archaeology', 'ai-evolution', 'refined']) {
  files.push(...findGameFiles(path.join(PROJECT_ROOT, dir)));
}
files.sort();

const CHECKS = [
  {
    id: 'EVAL_USAGE',
    severity: 'CRITICAL',
    pattern: /\beval\s*\(|new\s+Function\s*\(/g,
    message: 'eval() or new Function() — code injection vector',
    fix: 'Replace with direct function calls or JSON.parse for data'
  },
  {
    id: 'INNERHTML_VARIABLE',
    severity: 'HIGH',
    pattern: /\.innerHTML\s*=\s*(?!['"`])[^;]*(?:variable|\bvar\b|\+|`\$\{)/gi,
    message: 'innerHTML assigned from variable/expression — XSS risk',
    fix: 'Use textContent for text, or sanitize HTML input'
  },
  {
    id: 'INNERHTML_DYNAMIC',
    severity: 'MEDIUM',
    pattern: /\.innerHTML\s*[+]=|\.innerHTML\s*=\s*[^'"`;]*\+/g,
    message: 'innerHTML concatenation — potential XSS if any input is user-controlled',
    fix: 'Use DOM methods (createElement, textContent) instead of innerHTML concatenation'
  },
  {
    id: 'DOCUMENT_WRITE',
    severity: 'HIGH',
    pattern: /document\.write\s*\(/g,
    message: 'document.write() — can overwrite entire page, XSS-prone',
    fix: 'Use DOM manipulation methods instead'
  },
  {
    id: 'EXTERNAL_SCRIPT',
    severity: 'CRITICAL',
    pattern: /<script[^>]+src\s*=\s*["']https?:\/\//gi,
    message: 'External script loaded — violates zero-dependency contract, supply chain risk',
    fix: 'Remove external script dependencies; inline all code'
  },
  {
    id: 'EXTERNAL_FETCH',
    severity: 'HIGH',
    pattern: /fetch\s*\(\s*['"`]https?:\/\/|XMLHttpRequest|\.open\s*\(\s*['"](?:GET|POST)/gi,
    message: 'External HTTP request — data exfiltration risk, violates zero-dep contract',
    fix: 'Remove all external network requests; games must be fully offline'
  },
  {
    id: 'EXTERNAL_CSS',
    severity: 'MEDIUM',
    pattern: /<link[^>]+href\s*=\s*["']https?:\/\//gi,
    message: 'External CSS loaded — tracking pixel risk via CSS',
    fix: 'Inline all styles'
  },
  {
    id: 'EXTERNAL_IMAGE',
    severity: 'LOW',
    pattern: /(?:src|url)\s*(?:=|:)\s*["']https?:\/\//gi,
    message: 'External resource URL — tracking/fingerprinting vector',
    fix: 'Use inline data URIs or canvas-drawn graphics only'
  },
  {
    id: 'LOCALSTORAGE',
    severity: 'LOW',
    pattern: /localStorage|sessionStorage/g,
    message: 'Web storage usage — may persist user data without consent',
    fix: 'Acceptable for high scores; ensure no PII is stored'
  },
  {
    id: 'POSTMESSAGE',
    severity: 'MEDIUM',
    pattern: /postMessage|addEventListener\s*\(\s*['"]message/g,
    message: 'postMessage API — cross-origin communication risk if no origin check',
    fix: 'Add origin validation: if (event.origin !== expected) return'
  },
  {
    id: 'COOKIE_ACCESS',
    severity: 'HIGH',
    pattern: /document\.cookie/g,
    message: 'Cookie access — tracking/session hijacking risk',
    fix: 'Games should not access cookies; remove this code'
  },
  {
    id: 'GEOLOCATION',
    severity: 'CRITICAL',
    pattern: /navigator\.geolocation|getCurrentPosition/g,
    message: 'Geolocation access — privacy violation, completely unnecessary for games',
    fix: 'Remove geolocation access immediately'
  },
  {
    id: 'CAMERA_MIC',
    severity: 'CRITICAL',
    pattern: /getUserMedia|mediaDevices/g,
    message: 'Camera/microphone access — severe privacy violation',
    fix: 'Remove media device access immediately'
  },
  {
    id: 'WEBSOCKET',
    severity: 'HIGH',
    pattern: /new\s+WebSocket/g,
    message: 'WebSocket connection — violates offline/zero-dep contract',
    fix: 'Remove WebSocket; games must work offline'
  },
  {
    id: 'SERVICE_WORKER',
    severity: 'MEDIUM',
    pattern: /serviceWorker|navigator\.serviceWorker/g,
    message: 'Service worker registration — may cache/intercept requests',
    fix: 'Only acceptable if intentionally used for offline support'
  },
  {
    id: 'CLIPBOARD',
    severity: 'LOW',
    pattern: /navigator\.clipboard|execCommand\s*\(\s*['"]copy/g,
    message: 'Clipboard access — may exfiltrate data',
    fix: 'Only acceptable for explicit user-initiated copy actions'
  },
  {
    id: 'BEACON',
    severity: 'HIGH',
    pattern: /navigator\.sendBeacon/g,
    message: 'Beacon API — data exfiltration that survives page close',
    fix: 'Remove beacon usage; no analytics in game files'
  },
  {
    id: 'IFRAME_INJECT',
    severity: 'HIGH',
    pattern: /createElement\s*\(\s*['"]iframe/g,
    message: 'Dynamic iframe creation — clickjacking/phishing vector',
    fix: 'Remove dynamic iframe creation'
  },
  {
    id: 'BASE64_DECODE',
    severity: 'MEDIUM',
    pattern: /atob\s*\(/g,
    message: 'Base64 decoding — may hide malicious payloads',
    fix: 'Review decoded content; ensure it is not obfuscated code'
  },
  {
    id: 'PROTOTYPE_POLLUTION',
    severity: 'MEDIUM',
    pattern: /__proto__|Object\.assign\s*\(\s*\{\}/g,
    message: 'Potential prototype pollution vector',
    fix: 'Use Object.create(null) for dictionaries; avoid __proto__'
  },
];

// ── Scan ──
const results = [];
let totalIssues = 0;

for (const file of files) {
  const content = fs.readFileSync(file, 'utf-8');
  const relPath = path.relative(PROJECT_ROOT, file);
  const issues = [];

  for (const check of CHECKS) {
    const matches = content.match(check.pattern);
    if (matches) {
      issues.push({
        id: check.id,
        severity: check.severity,
        message: check.message,
        count: matches.length,
        fix: check.fix
      });
    }
  }

  // Additional: check for inline event handlers (onclick in HTML outside info panel)
  const inlineHandlers = content.match(/\bon\w+\s*=\s*["'][^"']*["']/g) || [];
  // Filter out the info panel close button which is expected
  const suspiciousHandlers = inlineHandlers.filter(h => !h.includes('toggleInfo'));
  if (suspiciousHandlers.length > 0) {
    issues.push({
      id: 'INLINE_HANDLERS',
      severity: 'LOW',
      message: `${suspiciousHandlers.length} inline event handler(s) outside info panel`,
      count: suspiciousHandlers.length,
      fix: 'Move event handlers to addEventListener in <script> block'
    });
  }

  if (issues.length > 0) {
    results.push({ file: relPath, issues });
    totalIssues += issues.length;
  }
}

// ── Output ──
const colors = {
  CRITICAL: '\x1b[31m\x1b[1m',
  HIGH: '\x1b[31m',
  MEDIUM: '\x1b[33m',
  LOW: '\x1b[36m',
  RESET: '\x1b[0m',
  BOLD: '\x1b[1m',
  GREEN: '\x1b[32m',
  CYAN: '\x1b[36m\x1b[1m'
};

console.log('');
console.log(`${colors.CYAN}╔══════════════════════════════════════════════╗${colors.RESET}`);
console.log(`${colors.CYAN}║      PIXEL VAULT — SECURITY SCANNER          ║${colors.RESET}`);
console.log(`${colors.CYAN}╚══════════════════════════════════════════════╝${colors.RESET}`);
console.log('');

const sevCounts = { CRITICAL: 0, HIGH: 0, MEDIUM: 0, LOW: 0 };
for (const r of results) {
  for (const i of r.issues) sevCounts[i.severity]++;
}

console.log(`${colors.BOLD}Scanned:${colors.RESET} ${files.length} games`);
console.log(`${colors.BOLD}Files with issues:${colors.RESET} ${results.length}`);
console.log(`${colors.BOLD}Total issues:${colors.RESET} ${totalIssues}`);
console.log(`  ${colors.CRITICAL}CRITICAL:${colors.RESET} ${sevCounts.CRITICAL}`);
console.log(`  ${colors.HIGH}HIGH:${colors.RESET}     ${sevCounts.HIGH}`);
console.log(`  ${colors.MEDIUM}MEDIUM:${colors.RESET}   ${sevCounts.MEDIUM}`);
console.log(`  ${colors.LOW}LOW:${colors.RESET}      ${sevCounts.LOW}`);
console.log('');

// Sort by severity
const sevOrder = { CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3 };
results.sort((a, b) => {
  const aMax = Math.min(...a.issues.map(i => sevOrder[i.severity]));
  const bMax = Math.min(...b.issues.map(i => sevOrder[i.severity]));
  return aMax - bMax;
});

for (const r of results) {
  const maxSev = r.issues.reduce((max, i) => sevOrder[i.severity] < sevOrder[max] ? i.severity : max, 'LOW');
  console.log(`  ${colors[maxSev]}${maxSev}${colors.RESET}  ${r.file}`);
  for (const i of r.issues) {
    console.log(`    ${colors[i.severity]}[${i.severity}]${colors.RESET} ${i.id} (×${i.count}): ${i.message}`);
    if (showFixes) console.log(`      ${colors.GREEN}FIX:${colors.RESET} ${i.fix}`);
  }
}

console.log('');
if (sevCounts.CRITICAL > 0) {
  console.log(`${colors.CRITICAL}✗ ${sevCounts.CRITICAL} CRITICAL issue(s) found — fix immediately${colors.RESET}`);
} else if (sevCounts.HIGH > 0) {
  console.log(`${colors.HIGH}⚠ No CRITICAL issues, but ${sevCounts.HIGH} HIGH severity issue(s) to review${colors.RESET}`);
} else {
  console.log(`${colors.GREEN}${colors.BOLD}✓ No CRITICAL or HIGH security issues found${colors.RESET}`);
}
console.log('');
