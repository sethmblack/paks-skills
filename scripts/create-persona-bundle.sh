#!/bin/bash
# Create a persona bundle that includes the persona + all its skills
# Usage: ./create-persona-bundle.sh <persona-name>

set -e

PERSONA_NAME=$1
EXPERTS_DIR="/Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/experts"
SKILLS_DIR="/Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/skills"
OUTPUT_DIR="/Users/ziggs/Documents/InfiniteBackroom/paks-skills/persona-bundles"

if [ -z "$PERSONA_NAME" ]; then
    echo "Usage: ./create-persona-bundle.sh <persona-name>"
    exit 1
fi

PERSONA_PATH="$EXPERTS_DIR/$PERSONA_NAME/PROMPT.md"
if [ ! -f "$PERSONA_PATH" ]; then
    echo "ERROR: Persona not found: $PERSONA_PATH"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR/$PERSONA_NAME"

# Extract skill names from the persona (from tables with backticks)
SKILL_NAMES=$(grep -oE '\`[a-z][-a-z0-9]+\`' "$PERSONA_PATH" 2>/dev/null | tr -d '`' | sort -u || true)

# Create display name
DISPLAY_NAME=$(echo "$PERSONA_NAME" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')

# Start building the bundle
OUTPUT_FILE="$OUTPUT_DIR/$PERSONA_NAME/SKILL.md"

# Create YAML frontmatter with proper values
cat > "$OUTPUT_FILE" << EOF
---
name: ${PERSONA_NAME}-expert
description: Embody ${DISPLAY_NAME} - AI persona expert with integrated methodology skills
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
  - persona
  - expert
  - ai-persona
  - ${PERSONA_NAME}
---

# ${DISPLAY_NAME} Expert (Bundle)

> This is a bundled persona that includes all referenced methodology skills inline for self-contained use.

---

EOF

# Add persona content (skip any existing YAML frontmatter if present)
if head -1 "$PERSONA_PATH" | grep -q "^---"; then
    # Has frontmatter, skip it
    awk '/^---$/{p++} p==2{found=1; next} found' "$PERSONA_PATH" >> "$OUTPUT_FILE"
else
    cat "$PERSONA_PATH" >> "$OUTPUT_FILE"
fi

# Add skills section
if [ -n "$SKILL_NAMES" ]; then
    echo "" >> "$OUTPUT_FILE"
    echo "---" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "# Bundled Methodology Skills" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "The following methodology skills are integrated into this persona. Use them as described in the Available Skills section above." >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    SKILL_COUNT=0
    SKILLS_FOUND=""
    for skill in $SKILL_NAMES; do
        SKILL_PATH="$SKILLS_DIR/$skill/PROMPT.md"
        if [ -f "$SKILL_PATH" ]; then
            ((SKILL_COUNT++))
            SKILLS_FOUND="$SKILLS_FOUND $skill"
            echo "## Skill: \`$skill\`" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
            # Add skill content (skip frontmatter if present)
            if head -1 "$SKILL_PATH" | grep -q "^---"; then
                awk '/^---$/{p++} p==2{found=1; next} found' "$SKILL_PATH" >> "$OUTPUT_FILE"
            else
                cat "$SKILL_PATH" >> "$OUTPUT_FILE"
            fi
            echo "" >> "$OUTPUT_FILE"
            echo "---" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
        fi
    done

    # Update keywords with skill names
    if [ $SKILL_COUNT -gt 0 ]; then
        for skill in $SKILLS_FOUND; do
            sed -i '' "/^keywords:/a\\
  - $skill" "$OUTPUT_FILE"
        done
    fi

    echo "[$PERSONA_NAME] Bundled $SKILL_COUNT skills" >&2
else
    echo "[$PERSONA_NAME] No skills to bundle (standalone persona)" >&2
fi

echo "$OUTPUT_FILE"
