#!/bin/bash
# Publish persona bundles in batches to avoid GitHub rate limits
# Publishes 20 at a time, then waits 5 minutes

set -e

BUNDLES_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/persona-bundles"
PAKS_READY_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/paks-ready"
GITHUB_USER="sethmblack"
LOG_FILE="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/persona-batch-log.txt"
BATCH_SIZE=20
BATCH_WAIT=300  # 5 minutes between batches

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

publish_persona() {
    local persona_name=$1
    local bundle_path="$BUNDLES_DIR/$persona_name"
    local repo_name="persona-$persona_name"

    if [ ! -f "$bundle_path/SKILL.md" ]; then
        return 1
    fi

    # Check if repo already exists
    if ! gh repo view "$GITHUB_USER/$repo_name" &>/dev/null; then
        # Create new repo
        if ! gh repo create "$GITHUB_USER/$repo_name" --public --description "AI Persona: $persona_name expert bundle" 2>/dev/null; then
            return 1
        fi
        sleep 2
    fi

    # Clone to temp dir and push
    local temp_dir=$(mktemp -d)
    cd "$temp_dir"
    git init -q
    git remote add origin "https://github.com/$GITHUB_USER/$repo_name.git"
    cp "$bundle_path/SKILL.md" .
    git add SKILL.md
    git commit -q -m "Initial commit: $persona_name persona bundle"
    git branch -M main
    git push -u origin main -f 2>/dev/null || git push -u origin main 2>/dev/null

    sleep 1

    # Publish to paks
    if paks publish . -y 2>&1 | grep -q -E "(Published|already exists)"; then
        # Copy to paks-ready
        mkdir -p "$PAKS_READY_DIR/$persona_name"
        cp "$bundle_path/SKILL.md" "$PAKS_READY_DIR/$persona_name/"
        cd "$BUNDLES_DIR"
        rm -rf "$temp_dir"
        return 0
    else
        cd "$BUNDLES_DIR"
        rm -rf "$temp_dir"
        return 1
    fi
}

# Main
echo "Persona Batch Publisher" | tee "$LOG_FILE"
echo "=======================" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "Batch size: $BATCH_SIZE, Wait between batches: ${BATCH_WAIT}s" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Get list of personas not yet in paks-ready
PENDING=()
for bundle_dir in "$BUNDLES_DIR"/*/; do
    persona_name=$(basename "$bundle_dir")
    [[ ! -f "$bundle_dir/SKILL.md" ]] && continue
    [[ -d "$PAKS_READY_DIR/$persona_name" ]] && continue
    PENDING+=("$persona_name")
done

total=${#PENDING[@]}
log "Found $total personas to publish"
log ""

batch_num=0
processed=0
success=0
failed=0

while [ $processed -lt $total ]; do
    ((batch_num++))
    batch_start=$processed
    batch_end=$((processed + BATCH_SIZE))
    [ $batch_end -gt $total ] && batch_end=$total

    log "${CYAN}=== Batch $batch_num: personas $((batch_start+1))-$batch_end of $total ===${NC}"

    for ((i=batch_start; i<batch_end; i++)); do
        persona_name="${PENDING[$i]}"
        if publish_persona "$persona_name"; then
            log "${GREEN}[OK] $persona_name${NC}"
            ((success++))
        else
            log "${RED}[FAIL] $persona_name${NC}"
            ((failed++))
        fi
        ((processed++))
        sleep 3  # Small delay between each in batch
    done

    log "Batch $batch_num complete: $success success, $failed failed so far"

    if [ $processed -lt $total ]; then
        log "${YELLOW}Waiting ${BATCH_WAIT}s before next batch...${NC}"
        sleep $BATCH_WAIT
    fi
done

log ""
log "======================="
log "COMPLETE"
log "Total: $total | Success: $success | Failed: $failed"
log "Finished: $(date)"
