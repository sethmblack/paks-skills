#!/bin/bash
# Publish each skill to its own GitHub repo and paks registry
# Usage: ./publish-to-paks.sh [skill-name] or ./publish-to-paks.sh --all

set -e

SKILLS_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills"
GITHUB_USER="sethmblack"
LOG_FILE="$SKILLS_DIR/publish-log.txt"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

create_and_publish_skill() {
    local skill_name=$1
    local skill_path="$SKILLS_DIR/$skill_name"
    local repo_name="skill-$skill_name"

    if [ ! -f "$skill_path/SKILL.md" ]; then
        log "${RED}[SKIP] $skill_name - No SKILL.md found${NC}"
        return 1
    fi

    log "${YELLOW}[START] $skill_name${NC}"

    # Check if repo already exists
    if gh repo view "$GITHUB_USER/$repo_name" &>/dev/null; then
        log "${YELLOW}[EXISTS] Repo $repo_name already exists, updating...${NC}"
    else
        # Create new repo
        log "  Creating repo $repo_name..."
        gh repo create "$GITHUB_USER/$repo_name" --public --description "Paks skill: $skill_name" || {
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
    cp "$skill_path/SKILL.md" .

    # Reset version to 1.0.0 for fresh publish
    if grep -q "version:" SKILL.md; then
        sed -i '' 's/version: [0-9.]*/version: 1.0.0/' SKILL.md
    fi

    # Commit and push
    git add SKILL.md
    git commit -q -m "Initial commit: $skill_name skill"
    git branch -M main
    git push -u origin main -f 2>/dev/null || git push -u origin main

    sleep 2

    # Publish to paks
    log "  Publishing to paks registry..."
    if paks publish . -y 2>&1 | tee -a "$LOG_FILE"; then
        log "${GREEN}[SUCCESS] $skill_name published!${NC}"
    else
        log "${RED}[ERROR] Failed to publish $skill_name to paks${NC}"
    fi

    # Cleanup
    cd "$SKILLS_DIR"
    rm -rf "$temp_dir"

    return 0
}

# Main
echo "Paks Skill Publisher" | tee "$LOG_FILE"
echo "===================" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

if [ "$1" == "--all" ] || [ "$1" == "--resume" ]; then
    # Publish all skills (--resume skips existing repos)
    RESUME_MODE=false
    [[ "$1" == "--resume" ]] && RESUME_MODE=true

    count=0
    success=0
    failed=0
    skipped=0

    for skill_dir in "$SKILLS_DIR"/*/; do
        skill_name=$(basename "$skill_dir")
        repo_name="skill-$skill_name"

        # Skip non-skill directories
        [[ "$skill_name" == "scripts" ]] && continue
        [[ "$skill_name" == ".git" ]] && continue
        [[ ! -f "$skill_dir/SKILL.md" ]] && continue

        ((count++))

        # In resume mode, skip if repo already exists
        if [ "$RESUME_MODE" = true ] && gh repo view "$GITHUB_USER/$repo_name" &>/dev/null; then
            log "${YELLOW}[SKIP] $skill_name - repo exists (resume mode)${NC}"
            ((skipped++))
            continue
        fi

        if create_and_publish_skill "$skill_name"; then
            ((success++))
        else
            ((failed++))
        fi

        # Rate limiting - 30 second delay to avoid GitHub repo creation limits
        sleep 30

        # Progress update every 10 skills
        if [ $((count % 10)) -eq 0 ]; then
            log "Progress: $count skills processed ($success success, $failed failed, $skipped skipped)"
        fi
    done

    log ""
    log "==================="
    log "COMPLETE"
    log "Total: $count | Success: $success | Failed: $failed | Skipped: $skipped"
    log "Finished: $(date)"

elif [ -n "$1" ]; then
    # Publish single skill
    create_and_publish_skill "$1"
else
    echo "Usage:"
    echo "  ./publish-to-paks.sh skill-name    # Publish single skill"
    echo "  ./publish-to-paks.sh --all         # Publish all skills"
    echo "  ./publish-to-paks.sh --resume      # Resume, skipping existing repos"
fi
