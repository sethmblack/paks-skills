#!/bin/bash
echo "Waiting 30 minutes for rate limit reset..."
echo "Started: $(date)"
sleep 1800
echo "Starting publish at: $(date)"
cd /Users/ziggs/Documents/InfiniteBackroom/paks-skills
./scripts/publish-persona-bundles.sh --resume >> persona-publish-output.log 2>&1
