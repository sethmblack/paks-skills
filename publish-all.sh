#!/bin/bash
# Publish all skills to paks.stakpak.dev
# Uses 30-second delay only for NEW repos to avoid rate limits
# Updates (existing repos) have no delay

PAKS_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills"
LOG_FILE="$PAKS_DIR/publish-log.txt"
NEW_DELAY=30  # seconds between NEW repo creations

cd "$PAKS_DIR"

# Get list of skill directories (exclude files and persona-bundles)
SKILLS=$(ls -d */ 2>/dev/null | grep -v "persona-bundles" | sed 's/\///')

TOTAL=$(echo "$SKILLS" | wc -l | tr -d ' ')
CURRENT=0
SUCCESS=0
FAILED=0
NEW_REPOS=0
UPDATES=0

echo "Starting publish of $TOTAL skills at $(date)" | tee "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

for skill in $SKILLS; do
    CURRENT=$((CURRENT + 1))

    # Skip if not a directory with SKILL.md
    if [ ! -f "$skill/SKILL.md" ]; then
        echo "[$CURRENT/$TOTAL] SKIP: $skill (no SKILL.md)" | tee -a "$LOG_FILE"
        continue
    fi

    # Skip skills starting with numbers (invalid paks names)
    if [[ "$skill" =~ ^[0-9] ]]; then
        echo "[$CURRENT/$TOTAL] SKIP: $skill (name starts with number)" | tee -a "$LOG_FILE"
        continue
    fi

    # Check if skill already exists in registry (strip ANSI codes)
    EXISTS=$(paks search "$skill" 2>/dev/null | sed 's/\x1b\[[0-9;]*m//g' | grep -c "sethmblack/$skill")

    echo "[$CURRENT/$TOTAL] Publishing: $skill (exists: $EXISTS)" | tee -a "$LOG_FILE"

    cd "$PAKS_DIR/$skill"

    # Publish with --yes for non-interactive mode
    OUTPUT=$(paks publish --yes 2>&1)
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        SUCCESS=$((SUCCESS + 1))
        echo "  ✓ Success" | tee -a "$LOG_FILE"

        # Only delay for NEW repos (didn't exist before)
        if [ "$EXISTS" -eq 0 ]; then
            NEW_REPOS=$((NEW_REPOS + 1))
            echo "  [NEW REPO] Waiting ${NEW_DELAY}s for rate limit..."
            sleep $NEW_DELAY
        else
            UPDATES=$((UPDATES + 1))
        fi
    else
        FAILED=$((FAILED + 1))
        echo "  ✗ Failed: $OUTPUT" | tee -a "$LOG_FILE"
    fi

    cd "$PAKS_DIR"
done

echo "==========================================" | tee -a "$LOG_FILE"
echo "Completed at $(date)" | tee -a "$LOG_FILE"
echo "Success: $SUCCESS (New: $NEW_REPOS, Updates: $UPDATES)" | tee -a "$LOG_FILE"
echo "Failed: $FAILED / Total: $TOTAL" | tee -a "$LOG_FILE"
