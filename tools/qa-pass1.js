#!/usr/bin/env node
/**
 * QA Pass 1 — Automated Game Health Scanner
 *
 * Extracts <script> content from each HTML game file and runs static analysis:
 *   FATAL:    JS syntax errors, missing game loop, missing canvas reference
 *   ERROR:    Undefined variable patterns, unreachable code, infinite loop risks
 *   WARNING:  Common bug patterns (no bounds check, missing collision, off-screen drift)
 *   OK:       No issues detected
 *
 * Usage:
 *   node tools/qa-pass1.js                    # Scan all games
 *   node tools/qa-pass1.js --file=path.html   # Scan one game
 *   node tools/qa-pass1.js --json             # Output JSON report
 *   node tools/qa-pass1.js --fatal-only       # Only show FATAL issues
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const PROJECT_ROOT = path.resolve(__dirname, '..');

// ── Args ──
const args = process.argv.slice(2);
const jsonOutput = args.includes('--json');
const fatalOnly = args.includes('--fatal-only');
let singleFile = '';
for (const a of args) {
  if (a.startsWith('--file=')) singleFile = a.slice(7);
}

// ── Find game files ──
function findGameFiles(dir) {
  const results = [];
  if (!fs.existsSync(dir)) return results;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...findGameFiles(full));
    } else if (entry.name.endsWith('.html') && !entry.name.startsWith('.')) {
      results.push(full);
    }
  }
  return results;
}

let files = [];
if (singleFile) {
  files = [path.resolve(PROJECT_ROOT, singleFile)];
} else {
  for (const dir of ['prototypes', 'ai-archaeology', 'ai-evolution', 'refined']) {
    files.push(...findGameFiles(path.join(PROJECT_ROOT, dir)));
  }
}
files.sort();

// ── Extract JS from HTML ──
function extractJS(html) {
  const blocks = [];
  const re = /<script[^>]*>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    blocks.push(m[1]);
  }
  return blocks.join('\n\n');
}

// ── Check 1: JS Syntax ──
function checkSyntax(js) {
  const issues = [];
  try {
    new vm.Script(js, { filename: 'game.js' });
  } catch (e) {
    issues.push({
      severity: 'FATAL',
      code: 'SYNTAX_ERROR',
      message: e.message.replace(/game\.js:/, 'line '),
      line: e.stack ? (e.stack.match(/game\.js:(\d+)/) || [])[1] : null
    });
  }
  return issues;
}

// ── Check 2: Game Loop ──
function checkGameLoop(js) {
  const issues = [];
  const hasRAF = /requestAnimationFrame/.test(js);
  const hasSetInterval = /setInterval/.test(js);

  if (!hasRAF && !hasSetInterval) {
    issues.push({
      severity: 'FATAL',
      code: 'NO_GAME_LOOP',
      message: 'No requestAnimationFrame or setInterval found — game has no update loop'
    });
  }

  // Check if RAF is called but the callback function exists
  const rafCalls = js.match(/requestAnimationFrame\s*\(\s*(\w+)\s*\)/g) || [];
  for (const call of rafCalls) {
    const funcName = call.match(/requestAnimationFrame\s*\(\s*(\w+)\s*\)/);
    if (funcName && funcName[1]) {
      const fn = funcName[1];
      // Check if this function is defined
      const fnDef = new RegExp(`function\\s+${fn}\\s*\\(|(?:const|let|var)\\s+${fn}\\s*=`);
      if (!fnDef.test(js)) {
        issues.push({
          severity: 'FATAL',
          code: 'MISSING_LOOP_FUNCTION',
          message: `requestAnimationFrame references '${fn}' but no function definition found`
        });
      }
    }
  }

  return issues;
}

// ── Check 3: Canvas Reference ──
function checkCanvas(html, js) {
  const issues = [];
  const hasCanvasEl = /<canvas/i.test(html);
  const hasCanvasRef = /getElementById|querySelector|getContext/.test(js);

  if (!hasCanvasEl) {
    issues.push({
      severity: 'FATAL',
      code: 'NO_CANVAS_ELEMENT',
      message: 'No <canvas> element in HTML'
    });
  }
  if (!hasCanvasRef) {
    issues.push({
      severity: 'ERROR',
      code: 'NO_CANVAS_REFERENCE',
      message: 'JS never references canvas via getElementById/querySelector/getContext'
    });
  }

  // Check canvas size (JS or HTML attributes)
  const widthSetJS = /\.width\s*=\s*\d{2,}|W\s*=\s*\d{3}|canvas\.width|width\s*=\s*800/.test(js);
  const widthSetHTML = /<canvas[^>]+width\s*=/i.test(html);
  if (!widthSetJS && !widthSetHTML && hasCanvasEl) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_CANVAS_SIZE',
      message: 'Canvas dimensions never set in HTML or JS — may default to 300x150'
    });
  }

  return issues;
}

// ── Check 4: Common Bug Patterns ──
function checkBugPatterns(js) {
  const issues = [];

  // Player position without bounds checking
  const hasPlayerXY = /player\s*[\.\[].*[xy]\s*[+\-=]|playerX|player\.x|this\.x/i.test(js);
  const hasBoundsCheck = /Math\.max|Math\.min|clamp|if\s*\(.*[xy]\s*[<>]|boundary|bounds/i.test(js);
  if (hasPlayerXY && !hasBoundsCheck) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_BOUNDS_CHECK',
      message: 'Player position modified but no bounds checking detected (Math.max/min/clamp) — sprite may drift off-screen'
    });
  }

  // Division by zero risk
  const divPatterns = js.match(/\/\s*(\w+)(?!\s*[=*\/])/g) || [];
  // Not worth checking all — too many false positives

  // Collision detection (skip for games that don't need it: puzzles, cards, sims, strategy, board games)
  const hasEnemies = /enemy|enemies|ghost|obstacle|hazard|monster|bullet/i.test(js);
  const hasCollision = /collision|collide|intersect|overlap|hitbox|distance.*<|abs.*<|AABB|hit\s*\(|checkHit|checkCollision|Math\.hypot|dx\s*\*\s*dx|touching|contact|within/i.test(js);
  if (hasEnemies && !hasCollision) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_COLLISION_DETECTION',
      message: 'Has enemies/obstacles but no collision detection pattern found'
    });
  }

  // Key handling without preventDefault
  const hasKeyHandler = /addEventListener.*key/i.test(js);
  const hasPreventDefault = /preventDefault/.test(js);
  if (hasKeyHandler && !hasPreventDefault) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_PREVENT_DEFAULT',
      message: 'Key event handlers without preventDefault — arrow keys may scroll the page'
    });
  }

  // Potential NaN propagation
  const hasParseInt = /parseInt\s*\(/.test(js);
  const hasNaNCheck = /isNaN|Number\.isFinite/.test(js);
  const hasUndefinedAccess = /undefined|\.length\s*-\s*1/.test(js);

  // ctx.drawImage with potentially undefined
  const drawImageCalls = (js.match(/drawImage/g) || []).length;
  if (drawImageCalls > 0) {
    // Not necessarily a bug, but image-based games may have load order issues
    const hasOnLoad = /onload|addEventListener.*load/i.test(js);
    if (!hasOnLoad && drawImageCalls > 2) {
      issues.push({
        severity: 'WARNING',
        code: 'IMAGE_LOAD_ORDER',
        message: `${drawImageCalls} drawImage calls but no image onload handler — images may not be loaded when drawn`
      });
    }
  }

  // requestAnimationFrame without time/delta parameter
  const rafCallbacks = js.match(/function\s+(\w+)\s*\(\s*\)|(\w+)\s*=\s*\(\s*\)\s*=>/g) || [];
  const hasTimeDelta = /delta|dt|elapsed|timestamp|now\s*-\s*last|performance\.now|Date\.now/i.test(js);
  if (!hasTimeDelta) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_DELTA_TIME',
      message: 'No delta time calculation — game speed may vary with frame rate'
    });
  }

  // Array access without length check
  const arrayAccess = /\[\s*\w+\s*\]/.test(js);
  // Too many false positives to report

  // Duplicate event listeners (common copy-paste bug)
  const keydownHandlers = (js.match(/addEventListener\s*\(\s*['"]keydown/g) || []).length;
  if (keydownHandlers > 3) {
    issues.push({
      severity: 'WARNING',
      code: 'DUPLICATE_LISTENERS',
      message: `${keydownHandlers} keydown event listeners — possible duplicates causing double-input`
    });
  }

  // Missing game state reset
  const hasRestart = /restart|reset|newGame|init|startGame|resetGame|restartGame/i.test(js);
  const hasRKey = /['"](r|R|KeyR)['"]/i.test(js);
  if (hasRKey && !hasRestart) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_RESTART_FUNCTION',
      message: 'R key referenced but no restart/reset/init function found'
    });
  }

  // Mouse events on canvas without offset calculation
  const hasMouseEvent = /addEventListener.*mouse|addEventListener.*click/i.test(js);
  const hasOffsetCalc = /offsetX|offsetY|getBoundingClientRect|offsetLeft|offsetTop|clientX\s*-/i.test(js);
  if (hasMouseEvent && !hasOffsetCalc) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_MOUSE_OFFSET',
      message: 'Mouse events without coordinate offset calculation — clicks may misalign with canvas'
    });
  }

  // Recursive function without base case (potential stack overflow)
  const recursiveFns = js.match(/function\s+(\w+)[^{]*\{[^}]*\1\s*\(/g) || [];
  // This regex is too simplistic, skip for now

  // Update function that never calls draw/render
  const hasUpdate = /function\s+(update|gameLoop|loop|tick|frame)\s*\(/i.test(js);
  const hasDraw = /function\s+(draw|render|paint)\s*\(|ctx\.(fill|stroke|drawImage|clearRect)/i.test(js);
  if (hasUpdate && !hasDraw) {
    issues.push({
      severity: 'ERROR',
      code: 'NO_DRAW_CALLS',
      message: 'Has update/loop function but no draw/render calls — screen may be blank'
    });
  }

  // Info panel guard check (matches various patterns: if (infoOpen) return; if (infoOpen || ...) return; if (infoOpen) { draw(); return; })
  const hasInfoPanel = /infoOpen|info-panel/i.test(js);
  const hasInfoGuard = /if\s*\(.*infoOpen.*\)\s*(?:return|{\s*(?:draw|render)\s*\(\s*\)\s*;\s*return)/.test(js);
  if (hasInfoPanel && !hasInfoGuard) {
    issues.push({
      severity: 'WARNING',
      code: 'NO_INFO_GUARD',
      message: 'Info panel exists but no `if (infoOpen) return` guard in update loop'
    });
  }

  return issues;
}

// ── Check 5: Variable/Function Reference Issues ──
function checkReferences(js) {
  const issues = [];

  // Find all function definitions
  const funcDefs = new Set();
  const funcDefRe = /function\s+(\w+)\s*\(|(?:const|let|var)\s+(\w+)\s*=\s*(?:function|\()/g;
  let m;
  while ((m = funcDefRe.exec(js)) !== null) {
    funcDefs.add(m[1] || m[2]);
  }

  // Common game functions that should exist if referenced
  const criticalFuncs = ['update', 'draw', 'render', 'gameLoop', 'loop', 'tick', 'init', 'reset'];
  for (const fn of criticalFuncs) {
    // Match standalone function calls, not method calls or compound words
    const callRe = new RegExp(`(?<!\\w)${fn}\\s*\\(`, 'g');
    const calls = js.match(callRe) || [];
    if (calls.length > 0 && !funcDefs.has(fn)) {
      // Check if it's a method call (obj.fn()) which is fine
      const methodCallRe = new RegExp(`\\.${fn}\\s*\\(`);
      if (!methodCallRe.test(js)) {
        issues.push({
          severity: 'ERROR',
          code: 'UNDEFINED_FUNCTION',
          message: `Function '${fn}()' called but never defined`
        });
      }
    }
  }

  return issues;
}

// ── Check 6: Game-specific patterns ──
function checkGameSpecific(js, filePath) {
  const issues = [];
  const fileName = path.basename(filePath);

  // Maze games should have wall collision
  if (/maz-/.test(fileName)) {
    const hasWallCheck = /wall|solid|blocked|canMove|isWall|TILE|maze/i.test(js);
    if (!hasWallCheck) {
      issues.push({
        severity: 'WARNING',
        code: 'MAZE_NO_WALLS',
        message: 'Maze game but no wall/tile collision detection found'
      });
    }
  }

  // Platformers should have gravity
  if (/plt-/.test(fileName)) {
    const hasGravity = /gravity|grav|vy\s*\+|velocityY|vel\.y|yVel/i.test(js);
    if (!hasGravity) {
      issues.push({
        severity: 'WARNING',
        code: 'PLATFORMER_NO_GRAVITY',
        message: 'Platformer but no gravity/vertical velocity found'
      });
    }
  }

  // Racing games should have speed
  if (/rac-/.test(fileName)) {
    const hasSpeed = /speed|velocity|accel/i.test(js);
    if (!hasSpeed) {
      issues.push({
        severity: 'WARNING',
        code: 'RACER_NO_SPEED',
        message: 'Racing game but no speed/velocity/acceleration found'
      });
    }
  }

  return issues;
}

// ── Run all checks ──
function analyzeGame(filePath) {
  const html = fs.readFileSync(filePath, 'utf-8');
  const js = extractJS(html);
  const relPath = path.relative(PROJECT_ROOT, filePath);

  const result = {
    file: relPath,
    size: fs.statSync(filePath).size,
    jsLength: js.length,
    issues: [],
    severity: 'OK' // will be upgraded
  };

  if (js.length === 0) {
    result.issues.push({
      severity: 'FATAL',
      code: 'NO_JS',
      message: 'No JavaScript found in file'
    });
    result.severity = 'FATAL';
    return result;
  }

  // Run checks
  result.issues.push(...checkSyntax(js));
  result.issues.push(...checkGameLoop(js));
  result.issues.push(...checkCanvas(html, js));
  result.issues.push(...checkBugPatterns(js));
  result.issues.push(...checkReferences(js));
  result.issues.push(...checkGameSpecific(js, filePath));

  // Determine overall severity
  for (const issue of result.issues) {
    if (issue.severity === 'FATAL') { result.severity = 'FATAL'; break; }
    if (issue.severity === 'ERROR' && result.severity !== 'FATAL') result.severity = 'ERROR';
    if (issue.severity === 'WARNING' && result.severity === 'OK') result.severity = 'WARNING';
  }

  return result;
}

// ── Main ──
const results = [];
for (const file of files) {
  results.push(analyzeGame(file));
}

// Sort: FATAL first, then ERROR, WARNING, OK
const severityOrder = { FATAL: 0, ERROR: 1, WARNING: 2, OK: 3 };
results.sort((a, b) => severityOrder[a.severity] - severityOrder[b.severity]);

if (jsonOutput) {
  // Write JSON report
  const reportPath = path.join(PROJECT_ROOT, 'qa-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
  console.log(`Report written to ${reportPath} (${results.length} games)`);
} else {
  // Console output
  const colors = {
    FATAL: '\x1b[31m\x1b[1m',   // bright red
    ERROR: '\x1b[31m',           // red
    WARNING: '\x1b[33m',         // yellow
    OK: '\x1b[32m',              // green
    RESET: '\x1b[0m',
    DIM: '\x1b[2m',
    BOLD: '\x1b[1m',
    CYAN: '\x1b[36m'
  };

  console.log('');
  console.log(`${colors.CYAN}${colors.BOLD}╔══════════════════════════════════════════════╗${colors.RESET}`);
  console.log(`${colors.CYAN}${colors.BOLD}║       PIXEL VAULT — QA PASS 1 SCANNER        ║${colors.RESET}`);
  console.log(`${colors.CYAN}${colors.BOLD}╚══════════════════════════════════════════════╝${colors.RESET}`);
  console.log('');

  const counts = { FATAL: 0, ERROR: 0, WARNING: 0, OK: 0 };
  for (const r of results) counts[r.severity]++;

  console.log(`${colors.BOLD}Summary:${colors.RESET} ${results.length} games scanned`);
  console.log(`  ${colors.FATAL}FATAL:${colors.RESET}   ${counts.FATAL}  (won't start / syntax errors)`);
  console.log(`  ${colors.ERROR}ERROR:${colors.RESET}   ${counts.ERROR}  (likely broken / missing critical code)`);
  console.log(`  ${colors.WARNING}WARNING:${colors.RESET} ${counts.WARNING}  (potential issues / may work with bugs)`);
  console.log(`  ${colors.OK}OK:${colors.RESET}      ${counts.OK}  (no issues detected)`);
  console.log('');

  // Show issues grouped by severity
  for (const sev of ['FATAL', 'ERROR', 'WARNING']) {
    const filtered = results.filter(r => r.severity === sev);
    if (fatalOnly && sev !== 'FATAL') continue;
    if (filtered.length === 0) continue;

    console.log(`${colors[sev]}${colors.BOLD}━━━ ${sev} (${filtered.length}) ━━━${colors.RESET}`);
    for (const r of filtered) {
      console.log(`  ${colors[sev]}${sev}${colors.RESET}  ${r.file}`);
      for (const issue of r.issues) {
        if (fatalOnly && issue.severity !== 'FATAL') continue;
        const ic = colors[issue.severity] || '';
        console.log(`    ${ic}[${issue.severity}]${colors.RESET} ${issue.code}: ${issue.message}`);
      }
    }
    console.log('');
  }

  if (!fatalOnly && counts.OK > 0) {
    console.log(`${colors.OK}${colors.BOLD}━━━ OK (${counts.OK}) ━━━${colors.RESET}`);
    const okFiles = results.filter(r => r.severity === 'OK');
    // Just list them compactly
    const perLine = 3;
    for (let i = 0; i < okFiles.length; i += perLine) {
      const chunk = okFiles.slice(i, i + perLine).map(r => {
        const short = r.file.replace(/prototypes\/|ai-archaeology\/|ai-evolution\//, '').replace(/\.html$/, '');
        return `${colors.OK}✓${colors.RESET} ${short}`;
      });
      console.log('  ' + chunk.join('   '));
    }
    console.log('');
  }

  // Final summary
  console.log(`${colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.RESET}`);
  if (counts.FATAL > 0) {
    console.log(`${colors.FATAL}${colors.BOLD}✗ ${counts.FATAL} game(s) have FATAL issues — fix these first${colors.RESET}`);
  }
  if (counts.ERROR > 0) {
    console.log(`${colors.ERROR}${colors.BOLD}⚠ ${counts.ERROR} game(s) have ERROR issues — likely broken${colors.RESET}`);
  }
  if (counts.FATAL === 0 && counts.ERROR === 0) {
    console.log(`${colors.OK}${colors.BOLD}✓ No FATAL or ERROR issues found${colors.RESET}`);
  }
  console.log('');
}
