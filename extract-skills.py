#!/usr/bin/env python3
"""
Extract methodology skills from persona expertise.md files.
Uses Claude to analyze and create skills.
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path

AI_PERSONAS = Path("/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas")
PAKS_SKILLS = Path("/Users/ziggs/Documents/InfiniteBackroom/paks-skills")
EXPERTS_DIR = AI_PERSONAS / "experts"
SKILLS_DIR = AI_PERSONAS / "skills"

def get_personas_needing_skills():
    """Get list of personas without embedded skills"""
    needs_skills = []
    persona_bundles = PAKS_SKILLS / "persona-bundles"

    for persona_dir in persona_bundles.iterdir():
        if persona_dir.is_dir():
            skill_file = PAKS_SKILLS / persona_dir.name / "SKILL.md"
            if skill_file.exists():
                content = skill_file.read_text()
                if "# Embedded Skills" not in content:
                    needs_skills.append(persona_dir.name)

    return sorted(needs_skills)

def get_persona_content(persona_name):
    """Get expertise.md and PROMPT.md content for a persona"""
    expertise_path = EXPERTS_DIR / persona_name / "expertise.md"
    prompt_path = EXPERTS_DIR / persona_name / "PROMPT.md"

    content = ""

    if expertise_path.exists():
        content += f"# EXPERTISE FILE\n\n{expertise_path.read_text()}\n\n"

    if prompt_path.exists():
        content += f"# PROMPT FILE\n\n{prompt_path.read_text()}\n\n"

    return content if content else None

def extract_skills_with_claude(persona_name, content):
    """Use Claude to extract skills from persona content"""

    extraction_prompt = f'''Analyze this AI persona's expertise and methodology to extract 3-5 reusable skills.

PERSONA: {persona_name}

{content[:15000]}

---

Extract actionable methodology skills - techniques that can be applied independently.
These should capture the DISTINCTIVE methods, mental models, and approaches that made this person effective.

For each skill provide:
1. name: kebab-case identifier (e.g., "absurd-escalation", "reality-tunnel-hacking")
2. description: 2-3 sentences explaining what this methodology does and why it's effective
3. core_principle: 1-2 sentences capturing the underlying philosophy or insight
4. when_to_use: 4-5 specific trigger conditions/situations where this applies
5. workflow: 4-6 concrete steps with descriptive titles (format: "Title: explanation")
6. example_input: A realistic scenario or question this skill would address
7. example_output: Brief demonstration of the methodology applied to that input
8. anti_patterns: 2-3 common mistakes or misapplications to avoid

Return ONLY valid JSON:
{{"skills": [
  {{
    "name": "skill-name",
    "description": "What it does and why it works",
    "core_principle": "The underlying insight",
    "when_to_use": ["trigger1", "trigger2", "trigger3", "trigger4"],
    "workflow": ["Title: step explanation", "Title: step explanation"],
    "example_input": "A realistic scenario",
    "example_output": "Brief demonstration",
    "anti_patterns": ["mistake1", "mistake2"]
  }}
]}}'''

    try:
        result = subprocess.run(
            ['claude', '-p', extraction_prompt, '--output-format', 'json'],
            capture_output=True,
            text=True,
            timeout=180
        )

        if result.returncode != 0:
            return None

        response = json.loads(result.stdout)
        if 'result' in response:
            result_text = response['result']
            json_match = re.search(r'\{[\s\S]*\}', result_text)
            if json_match:
                return json.loads(json_match.group())
        return response
    except Exception as e:
        print(f"  Error: {e}")
        return None

def create_skill_prompt(skill_data, persona_name):
    """Create PROMPT.md content for a skill - production quality template"""
    name = skill_data['name']
    description = skill_data['description']
    when_to_use = skill_data.get('when_to_use', [])
    workflow = skill_data.get('workflow', [])
    core_principle = skill_data.get('core_principle', '')
    example_input = skill_data.get('example_input', '')
    example_output = skill_data.get('example_output', '')
    anti_patterns = skill_data.get('anti_patterns', [])

    title = name.replace('-', ' ').title()
    persona_title = persona_name.replace('-', ' ').title()

    content = f'''# {title}

{description}

## When to Use

'''
    for trigger in when_to_use:
        content += f"- {trigger}\n"

    content += f'''
## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The context, problem, or material to analyze |
| goal | No | Specific outcome desired (default: apply methodology) |
| constraints | No | Limitations or requirements to honor |

## Core Principle

'''
    if core_principle:
        content += f"{core_principle}\n\n"
    else:
        content += f"This methodology embodies {persona_title}'s distinctive approach: the specific techniques, mental models, and perspectives that made their work effective. Apply these not as rigid rules but as a lens for seeing and acting.\n\n"

    content += '''## Methodology

'''
    # Group workflow into phases if possible
    if len(workflow) >= 4:
        # Create phases
        mid = len(workflow) // 2
        content += f"### Phase 1: Analysis\n\n"
        for i, step in enumerate(workflow[:mid], 1):
            step_content = step.split(':', 1)[1].strip() if ':' in step else step
            step_title = step.split(':')[0].strip() if ':' in step else f"Assess the situation"
            content += f"**Step {i}: {step_title}**\n{step_content}\n\n"

        content += f"### Phase 2: Application\n\n"
        for i, step in enumerate(workflow[mid:], mid + 1):
            step_content = step.split(':', 1)[1].strip() if ':' in step else step
            step_title = step.split(':')[0].strip() if ':' in step else f"Apply the insight"
            content += f"**Step {i}: {step_title}**\n{step_content}\n\n"
    else:
        for i, step in enumerate(workflow, 1):
            step_content = step.split(':', 1)[1].strip() if ':' in step else step
            step_title = step.split(':')[0].strip() if ':' in step else f"Step {i}"
            content += f"**Step {i}: {step_title}**\n{step_content}\n\n"

    content += '''## Output Format

Provide a structured response that includes:
1. **Analysis**: What the methodology reveals about the situation
2. **Application**: Specific recommendations or transformations
3. **Rationale**: Why this approach fits the situation

## Constraints

- Honor the original context and spirit of the methodology
- Adapt to the specific situation rather than applying mechanically
- Acknowledge limitations and edge cases
- Do not use this methodology to harm, deceive, or manipulate
- Recognize when a different approach would serve better

'''

    if anti_patterns:
        content += "## Anti-Patterns to Avoid\n\n"
        for ap in anti_patterns:
            content += f"- {ap}\n"
        content += "\n"

    content += f'''## Example

**Input**: {example_input if example_input else f"A situation requiring {persona_title}'s methodology"}

**Output**: {example_output if example_output else f"Application of the methodology showing analysis, specific recommendations, and rationale grounded in {persona_title}'s approach."}

## Integration

This skill derives from **{persona_title}**'s methodology.

**Works well with:**
- Other skills from {persona_title} for comprehensive analysis
- Complementary perspectives from related experts
- Iterative application for complex situations

**When to prefer this skill:**
- The situation matches the trigger conditions above
- You need this specific lens or methodology
- Other approaches haven't yielded satisfactory results
'''
    return content

def create_skill_extraction_report(persona_name, skills):
    """Create skill-extraction-report.md"""
    content = f'''# Skill Extraction Report: {persona_name.replace('-', ' ').title()}

**Expert:** {persona_name}
**Extraction Date:** 2026-02-12

---

## Extracted Skills

'''
    for i, skill in enumerate(skills, 1):
        content += f'''### {i}. {skill['name']}

**Description:** {skill['description']}

**Priority:** HIGH

---

'''
    return content

def process_persona(persona_name):
    """Process a single persona"""
    print(f"Processing {persona_name}...")

    content = get_persona_content(persona_name)
    if not content:
        print(f"  No content found")
        return False

    # Check if already has skill-extraction-report
    report_path = EXPERTS_DIR / persona_name / "skill-extraction-report.md"

    print(f"  Extracting skills with Claude...")
    result = extract_skills_with_claude(persona_name, content)

    if not result or 'skills' not in result:
        print(f"  Failed to extract skills")
        return False

    skills = result['skills']
    if not skills:
        print(f"  No skills extracted")
        return False

    print(f"  Found {len(skills)} skills: {[s['name'] for s in skills]}")

    # Create skill files
    for skill in skills:
        skill_name = skill['name']
        skill_dir = SKILLS_DIR / skill_name

        if not skill_dir.exists():
            skill_dir.mkdir(parents=True)
            skill_prompt = create_skill_prompt(skill, persona_name)
            (skill_dir / "PROMPT.md").write_text(skill_prompt)
            print(f"    Created: {skill_name}")

    # Create/update skill extraction report
    report_content = create_skill_extraction_report(persona_name, skills)
    report_path.write_text(report_content)
    print(f"  Created skill-extraction-report.md")

    return True

def main():
    personas = get_personas_needing_skills()
    print(f"Found {len(personas)} personas needing skill extraction\n")

    success = 0
    failed = 0

    for persona in personas:
        try:
            if process_persona(persona):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  Error: {e}")
            failed += 1

        # Brief pause to avoid rate limits
        time.sleep(1)

        if (success + failed) % 10 == 0:
            print(f"\n--- Progress: {success}/{success+failed} ---\n")

    print(f"\nFinal Results:")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")

if __name__ == "__main__":
    main()
