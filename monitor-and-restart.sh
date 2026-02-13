#!/bin/bash
cd /Users/ziggs/Documents/InfiniteBackroom/paks-skills

echo "Monitoring publish script..."
echo "Will restart with --resume when current run finishes"

# Wait for the current script to finish
while pgrep -f "publish-to-paks.sh" > /dev/null; do
    sleep 30
    # Show progress
    success=$(grep -c "\[SUCCESS\]" publish-output.log 2>/dev/null || echo 0)
    skip=$(grep -c "\[SKIP\]" publish-output.log 2>/dev/null || echo 0)
    current=$(grep "\[START\]" publish-output.log | tail -1 | sed 's/.*\[START\] //' | tr -d '\033[1;33m')
    echo "$(date '+%H:%M:%S') - Published: $success, Skipped: $skip, Current: $current"
done

echo ""
echo "=== Original run finished at $(date) ==="
echo ""

# Wait a moment then restart for new skills
sleep 5
echo "Restarting to publish new skills..."
./scripts/publish-to-paks.sh --resume >> publish-output.log 2>&1

echo "=== Second run finished at $(date) ==="
echo "Final counts:"
grep -c "\[SUCCESS\]" publish-output.log
