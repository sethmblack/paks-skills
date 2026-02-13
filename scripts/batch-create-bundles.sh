#!/bin/bash
# Create all persona bundles
# Usage: ./batch-create-bundles.sh

EXPERTS_DIR="/Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/experts"
SCRIPT_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/scripts"

echo "Creating persona bundles..."
echo "==========================="

count=0
success=0
failed=0

for persona_dir in "$EXPERTS_DIR"/*/; do
    persona_name=$(basename "$persona_dir")

    # Skip non-persona directories
    [[ "$persona_name" == "scripts" ]] && continue
    [[ "$persona_name" == ".git" ]] && continue
    [[ ! -f "$persona_dir/PROMPT.md" ]] && continue

    ((count++))

    if "$SCRIPT_DIR/create-persona-bundle.sh" "$persona_name" > /dev/null 2>&1; then
        ((success++))
    else
        echo "FAILED: $persona_name"
        ((failed++))
    fi

    # Progress every 50
    if [ $((count % 50)) -eq 0 ]; then
        echo "Progress: $count processed ($success success, $failed failed)"
    fi
done

echo ""
echo "==========================="
echo "COMPLETE"
echo "Total: $count | Success: $success | Failed: $failed"
