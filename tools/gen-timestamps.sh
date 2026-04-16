#!/usr/bin/env bash
# Generate file modification timestamps for QA dashboard "updated" detection
# Output: tools/qa-timestamps.json
cd "$(dirname "$0")/.."
echo "{" > tools/qa-timestamps.json
first=1
for f in prototypes/*/*.html ai-archaeology/*/*.html ai-evolution/*/*.html; do
  [[ -f "$f" ]] || continue
  ts=$(git log -1 --format='%aI' -- "$f" 2>/dev/null || echo "unknown")
  [[ $first -eq 0 ]] && echo "," >> tools/qa-timestamps.json
  printf '  "%s": "%s"' "$f" "$ts" >> tools/qa-timestamps.json
  first=0
done
echo "" >> tools/qa-timestamps.json
echo "}" >> tools/qa-timestamps.json
echo "Generated tools/qa-timestamps.json"
