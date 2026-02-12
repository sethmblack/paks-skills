#!/usr/bin/env python3
"""Fix SKILL.md frontmatter to match paks format."""

import os
import re
import sys
import yaml

def fix_frontmatter(content):
    """Convert our format to paks format."""
    # Match frontmatter
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return content, False

    frontmatter_text = match.group(1)
    body = content[match.end():]

    # Parse existing fields with regex (safer than yaml for malformed input)
    name_match = re.search(r'^name:\s*(.+)$', frontmatter_text, re.MULTILINE)
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter_text, re.MULTILINE)
    version_match = re.search(r'^version:\s*(.+)$', frontmatter_text, re.MULTILINE)
    author_match = re.search(r'^author:\s*(.+)$', frontmatter_text, re.MULTILINE)
    tags_match = re.search(r'^tags:\s*\[(.+)\]$', frontmatter_text, re.MULTILINE)

    # Also check for keywords format (from previous fix)
    keywords = []
    keywords_section = re.search(r'^keywords:\n((?:  - .+\n?)+)', frontmatter_text, re.MULTILINE)
    if keywords_section:
        keywords = re.findall(r'  - (.+)', keywords_section.group(1))

    if not name_match:
        return content, False

    name = name_match.group(1).strip()

    # Get description - could be from desc_match or from body first paragraph
    if desc_match:
        description = desc_match.group(1).strip()
    else:
        # Try to get from first paragraph of body
        first_para = re.search(r'^#[^\n]+\n+([^\n#]+)', body)
        if first_para:
            description = first_para.group(1).strip()[:200]
        else:
            description = f"A skill for {name}"

    version = version_match.group(1).strip() if version_match else "1.0.0"
    author = author_match.group(1).strip() if author_match else "sethmblack"

    # Get tags from either format
    if tags_match:
        keywords = [t.strip() for t in tags_match.group(1).split(',')]

    # Truncate description if too long (max 200 chars for safety)
    if len(description) > 200:
        description = description[:197] + "..."

    # Clean description - remove quotes that might be there
    description = description.strip('"\'')

    # Build new frontmatter using yaml for proper escaping
    frontmatter_dict = {
        'name': name,
        'description': description,
        'license': 'MIT',
        'metadata': {
            'version': version,
            'author': author
        }
    }

    if keywords:
        frontmatter_dict['keywords'] = keywords[:10]

    # Use yaml.dump for proper escaping
    new_frontmatter = "---\n" + yaml.dump(frontmatter_dict, default_flow_style=False, allow_unicode=True, sort_keys=False) + "---\n"

    return new_frontmatter + body, True

def process_skill(skill_dir):
    """Process a single skill directory."""
    skill_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_path):
        return False

    with open(skill_path, 'r') as f:
        content = f.read()

    new_content, changed = fix_frontmatter(content)

    if changed:
        with open(skill_path, 'w') as f:
            f.write(new_content)
        return True
    return False

def main():
    base_dir = "/Users/ziggs/Documents/InfiniteBackroom/paks-skills"
    fixed = 0
    skipped = 0
    errors = []

    for item in sorted(os.listdir(base_dir)):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            try:
                if process_skill(item_path):
                    fixed += 1
                    if fixed % 100 == 0:
                        print(f"Progress: {fixed} skills fixed...")
                else:
                    skipped += 1
            except Exception as e:
                errors.append(f"{item}: {e}")
                print(f"✗ Error: {item} - {e}")

    print(f"\nDone! Fixed: {fixed}, Skipped: {skipped}, Errors: {len(errors)}")

if __name__ == "__main__":
    main()
