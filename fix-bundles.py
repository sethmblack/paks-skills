#!/usr/bin/env python3
"""
Fix bundled personas by embedding their skills from skill-extraction-report.md
"""

import os
import re
import yaml
from pathlib import Path

AI_PERSONAS = Path("/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas")
PAKS_SKILLS = Path("/Users/ziggs/Documents/InfiniteBackroom/paks-skills")
EXPERTS_DIR = AI_PERSONAS / "experts"
SKILLS_DIR = AI_PERSONAS / "skills"

def to_kebab_case(text):
    """Convert title case or mixed case to kebab-case"""
    text = text.replace('`', '')
    if '-' in text and text == text.lower():
        return text
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'([a-z])([A-Z])', r'\1-\2', text)
    return text.lower().strip('-')

def extract_skills_from_report(report_path):
    """Extract skill names from skill-extraction-report.md"""
    if not report_path.exists():
        return []

    content = report_path.read_text()
    skills = []

    # Method 1: "## Skill Candidates" section with "**Priority:** HIGH" inline
    in_skill_candidates = False
    current_skill = None

    for line in content.split('\n'):
        line_lower = line.lower()

        if '## skill candidates' in line_lower:
            in_skill_candidates = True
            continue
        elif line.startswith('## ') and in_skill_candidates:
            in_skill_candidates = False

        if in_skill_candidates:
            match = re.match(r'^###\s*\d+\.\s*(.+)$', line)
            if match:
                current_skill = to_kebab_case(match.group(1).strip())

            if current_skill and '**priority:**' in line_lower and 'high' in line_lower:
                if current_skill not in skills:
                    skills.append(current_skill)
                current_skill = None

    # Method 2: "## Extracted Skills" section (skills listed directly under it)
    in_extracted = False
    for line in content.split('\n'):
        line_lower = line.lower()

        if '## extracted skills' in line_lower:
            in_extracted = True
            continue
        elif line.startswith('## ') and in_extracted:
            in_extracted = False

        if in_extracted:
            match = re.match(r'^###\s*\d+\.\s*(.+)$', line)
            if match:
                skill_name = to_kebab_case(match.group(1).strip())
                if skill_name and skill_name not in skills:
                    skills.append(skill_name)

    # Method 3: "### HIGH PRIORITY" section header
    in_high_priority = False
    for line in content.split('\n'):
        line_lower = line.lower()

        if 'high priority' in line_lower and line.startswith('#'):
            in_high_priority = True
            continue
        elif ('medium priority' in line_lower or 'low priority' in line_lower) and line.startswith('#'):
            in_high_priority = False

        if in_high_priority:
            match = re.match(r'^#{2,4}\s*\d+\.\s*(.+)$', line)
            if match:
                skill_name = to_kebab_case(match.group(1).strip())
                if skill_name and skill_name not in skills:
                    skills.append(skill_name)

    # Method 4: "## Recommended Skill Creation Order" or "## Prioritization Summary" sections
    rec_patterns = [
        (r'## Recommended Skill Creation Order.*?(?=## |\Z)', True),
        (r'### HIGH Priority.*?(?=### MEDIUM|### LOW|\Z)', True),
        (r'## Prioritization Summary.*?(?=## |\Z)', False),
    ]

    for pattern, extract_from_list in rec_patterns:
        rec_section = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if rec_section:
            for line in rec_section.group(0).split('\n'):
                # Match "1. **skill-name**" or "1. skill-name - description"
                match = re.match(r'^\d+\.\s*\*{0,2}([^*\n]+)', line)
                if match:
                    # Extract just the skill name (before any " - " description)
                    skill_part = match.group(1).split(' - ')[0].split(' (')[0].strip()
                    skill_name = to_kebab_case(skill_part)
                    if skill_name and skill_name not in skills and len(skill_name) > 3:
                        skills.append(skill_name)

    return skills[:5]  # Limit to 5 skills max

def get_skill_content(skill_name):
    """Get the full content of a skill from AI-Personas/skills/"""
    skill_path = SKILLS_DIR / skill_name / "PROMPT.md"
    if skill_path.exists():
        return skill_path.read_text()
    return None

def update_bundle(expert_name, skills):
    """Update the bundled persona with embedded skills"""
    bundle_path = PAKS_SKILLS / expert_name / "SKILL.md"
    if not bundle_path.exists():
        return False, "bundle_not_found"

    content = bundle_path.read_text()

    if "# Embedded Skills" in content:
        return False, "already_embedded"

    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            yaml_content = content[3:end_idx].strip()
            rest_content = content[end_idx+3:].strip()

            try:
                frontmatter = yaml.safe_load(yaml_content)
                if frontmatter is None:
                    frontmatter = {}
            except:
                frontmatter = {}
        else:
            frontmatter = {}
            rest_content = content
    else:
        frontmatter = {}
        rest_content = content

    existing_keywords = frontmatter.get('keywords', [])
    if isinstance(existing_keywords, str):
        existing_keywords = [existing_keywords]
    if existing_keywords is None:
        existing_keywords = []

    for skill in skills:
        if skill not in existing_keywords:
            existing_keywords.insert(0, skill)

    frontmatter['keywords'] = existing_keywords

    skills_content = "\n\n---\n\n# Embedded Skills\n\n"
    skills_content += "> The following methodology skills are integrated into this persona for self-contained use.\n\n"

    embedded_count = 0
    for skill in skills:
        skill_text = get_skill_content(skill)
        if skill_text:
            skills_content += f"---\n\n## Skill: {skill}\n\n{skill_text}\n\n"
            embedded_count += 1

    if embedded_count == 0:
        return False, "no_skill_content"

    new_content = "---\n"
    new_content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content += "---\n\n"
    new_content += rest_content
    new_content += skills_content

    bundle_path.write_text(new_content)
    return True, f"embedded_{embedded_count}"

def main():
    experts_with_reports = []
    for expert_dir in EXPERTS_DIR.iterdir():
        if expert_dir.is_dir():
            report_path = expert_dir / "skill-extraction-report.md"
            if report_path.exists():
                experts_with_reports.append(expert_dir.name)

    print(f"Found {len(experts_with_reports)} experts with skill extraction reports")

    results = {
        "updated": 0,
        "already_embedded": 0,
        "bundle_not_found": 0,
        "no_skills_found": 0,
        "no_skill_content": 0,
    }

    for expert in sorted(experts_with_reports):
        report_path = EXPERTS_DIR / expert / "skill-extraction-report.md"
        skills = extract_skills_from_report(report_path)

        if not skills:
            results["no_skills_found"] += 1
            continue

        valid_skills = [s for s in skills if (SKILLS_DIR / s / "PROMPT.md").exists()]

        if not valid_skills:
            results["no_skill_content"] += 1
            continue

        print(f"Processing {expert}: {valid_skills}")

        success, status = update_bundle(expert, valid_skills)
        if success:
            results["updated"] += 1
        else:
            if status in results:
                results[status] += 1

    print(f"\nResults:")
    for key, val in results.items():
        print(f"  {key}: {val}")

if __name__ == "__main__":
    main()
