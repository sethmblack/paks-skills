#!/bin/bash
# Publish persona bundles to GitHub and Paks registry
# Usage: ./publish-persona-bundles.sh [--resume]

set -e

BUNDLES_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/persona-bundles"
GITHUB_USER="sethmblack"
LOG_FILE="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/persona-publish-log.txt"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

publish_persona() {
    local persona_name=$1
    local bundle_path="$BUNDLES_DIR/$persona_name"
    local repo_name="persona-$persona_name"

    if [ ! -f "$bundle_path/SKILL.md" ]; then
        log "${RED}[SKIP] $persona_name - No SKILL.md found${NC}"
        return 1
    fi

    log "${YELLOW}[START] $persona_name${NC}"

    # Check if repo already exists
    if gh repo view "$GITHUB_USER/$repo_name" &>/dev/null; then
        log "${YELLOW}[EXISTS] Repo $repo_name already exists, updating...${NC}"
    else
        # Create new repo
        gh repo create "$GITHUB_USER/$repo_name" --public --description "AI Persona: $persona_name expert bundle with integrated skills" || {
            log "${RED}[ERROR] Failed to create repo $repo_name${NC}"
            return 1
        }
        sleep 1
    fi

    # Clone to temp dir
    local temp_dir=$(mktemp -d)
    cd "$temp_dir"

    # Initialize repo
    git init -q
    git remote add origin "https://github.com/$GITHUB_USER/$repo_name.git"

    # Copy skill file
    cp "$bundle_path/SKILL.md" .

    # Commit and push
    git add SKILL.md
    git commit -q -m "Initial commit: $persona_name persona bundle"
    git branch -M main
    git push -u origin main -f 2>/dev/null || git push -u origin main

    sleep 1

    # Publish to paks
    if paks publish . -y 2>&1 | grep -q -E "(Published|already exists)"; then
        log "${GREEN}[SUCCESS] $persona_name published!${NC}"
        # Copy to paks-ready directory
        mkdir -p "/Users/ziggs/Documents/InfiniteBackroom/paks-skills/paks-ready/$persona_name"
        cp "$bundle_path/SKILL.md" "/Users/ziggs/Documents/InfiniteBackroom/paks-skills/paks-ready/$persona_name/"
    else
        log "${RED}[ERROR] Failed to publish $persona_name to paks${NC}"
    fi

    # Cleanup
    cd "$BUNDLES_DIR"
    rm -rf "$temp_dir"

    return 0
}

# Main
echo "Persona Bundle Publisher" | tee "$LOG_FILE"
echo "========================" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

RESUME_MODE=false
[[ "$1" == "--resume" ]] && RESUME_MODE=true

count=0
success=0
failed=0
skipped=0

for bundle_dir in "$BUNDLES_DIR"/*/; do
    persona_name=$(basename "$bundle_dir")
    repo_name="persona-$persona_name"

    # Skip if not a bundle directory
    [[ ! -f "$bundle_dir/SKILL.md" ]] && continue

    ((count++))

    # In resume mode, skip if repo already exists
    if [ "$RESUME_MODE" = true ] && gh repo view "$GITHUB_USER/$repo_name" &>/dev/null; then
        ((skipped++))
        continue
    fi

    if publish_persona "$persona_name"; then
        ((success++))
    else
        ((failed++))
    fi

    # Rate limiting - 30 second delay (avoid GitHub repo creation limits)
    sleep 30

    # Progress update every 25 personas
    if [ $((count % 25)) -eq 0 ]; then
        log "Progress: $count personas processed ($success success, $failed failed, $skipped skipped)"
    fi
done

log ""
log "========================"
log "COMPLETE"
log "Total: $count | Success: $success | Failed: $failed | Skipped: $skipped"
log "Finished: $(date)"
