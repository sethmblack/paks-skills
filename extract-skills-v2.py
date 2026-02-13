#!/usr/bin/env python3
"""
Production-grade skill extraction from persona files.
Creates high-quality skills matching prompt engineering standards.
"""

import os
import re
import json
import subprocess
from pathlib import Path

AI_PERSONAS = Path("/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas")
EXPERTS_DIR = AI_PERSONAS / "experts"
SKILLS_DIR = AI_PERSONAS / "skills"

def get_persona_content(persona_name):
    """Get PROMPT.md and expertise.md content for a persona"""
    expertise_path = EXPERTS_DIR / persona_name / "expertise.md"
    prompt_path = EXPERTS_DIR / persona_name / "PROMPT.md"

    content = ""

    if prompt_path.exists():
        content += f"# PERSONA PROMPT\n\n{prompt_path.read_text()}\n\n"

    if expertise_path.exists():
        content += f"# EXPERTISE\n\n{expertise_path.read_text()[:10000]}\n\n"

    return content if content else None

def extract_skills_with_claude(persona_name, content):
    """Use Claude CLI to extract production-quality skills"""

    extraction_prompt = f'''You are a production-grade prompt engineer. Analyze this persona and extract 3-4 reusable methodology skills.

PERSONA: {persona_name}

{content[:18000]}

---

Extract DISTINCTIVE methodology skills - the specific techniques, mental models, and approaches that made this person effective.

For each skill, provide a COMPLETE JSON object with:

1. name: kebab-case (e.g., "forbidden-word-methodology")
2. description: 3-4 sentences on what it does and why it works
3. core_principle: 2-3 sentences capturing the fundamental insight
4. when_to_use: Array of 5-6 specific trigger conditions
5. phases: Array of 3-5 named phases, each with:
   - name: Phase title
   - description: What this phase accomplishes
   - steps: Array of 3-4 step objects with "title" and "content"
6. output_format: Description of the structured output this methodology produces
7. constraints: Array of 5-6 critical limitations and warnings
8. anti_patterns: Array of 4-5 common mistakes with explanations
9. examples: Array of 2-3 complete examples, each with:
   - title: Example name
   - situation: The input scenario
   - application: How the methodology applies
   - output: The result
10. integration: Object with:
    - works_with: Array of complementary skills/approaches
    - when_to_prefer: When to use this over alternatives
    - cautions: Warnings for integration

Return ONLY valid JSON:
{{"skills": [...]}}'''

    try:
        result = subprocess.run(
            ['claude', '-p', extraction_prompt, '--output-format', 'json'],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"  Claude error: {result.stderr[:200]}")
            return None

        response = json.loads(result.stdout)
        if 'result' in response:
            result_text = response['result']
            json_match = re.search(r'\{[\s\S]*\}', result_text)
            if json_match:
                return json.loads(json_match.group())
        return response
    except json.JSONDecodeError as e:
        print(f"  JSON parse error: {e}")
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

def create_skill_prompt(skill, persona_name):
    """Create production-quality PROMPT.md for a skill"""

    name = skill['name']
    title = name.replace('-', ' ').title()
    persona_title = persona_name.replace('-', ' ').title()

    description = skill.get('description', f"A methodology derived from {persona_title}'s approach.")
    core_principle = skill.get('core_principle', '')
    when_to_use = skill.get('when_to_use', [])
    phases = skill.get('phases', [])
    output_format = skill.get('output_format', '')
    constraints = skill.get('constraints', [])
    anti_patterns = skill.get('anti_patterns', [])
    examples = skill.get('examples', [])
    integration = skill.get('integration', {})

    # Build the skill file
    content = f'''---
name: {name}
description: {description[:150]}
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
  source_persona: {persona_name}
keywords:
- {name.split('-')[0]}
- methodology
- {persona_name}
---

# {title}

{description}

## When to Use

'''
    for trigger in when_to_use:
        content += f"- {trigger}\n"

    content += '''
## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The context, problem, or scenario to analyze |
| goal | No | Specific outcome desired (default: apply methodology) |
| constraints | No | Limitations or requirements to honor |

## Core Principle

'''
    if core_principle:
        content += f"{core_principle}\n\n"
    else:
        content += f"This methodology embodies {persona_title}'s distinctive approach—the specific techniques and mental models that made their work effective.\n\n"

    content += "## Methodology\n\n"

    # Add phases
    if phases:
        for i, phase in enumerate(phases, 1):
            phase_name = phase.get('name', f'Phase {i}')
            phase_desc = phase.get('description', '')
            steps = phase.get('steps', [])

            content += f"### Phase {i}: {phase_name}\n\n"
            if phase_desc:
                content += f"{phase_desc}\n\n"

            for j, step in enumerate(steps, 1):
                if isinstance(step, dict):
                    step_title = step.get('title', f'Step {j}')
                    step_content = step.get('content', '')
                else:
                    step_title = f'Step {j}'
                    step_content = step

                content += f"#### Step {j}: {step_title}\n\n{step_content}\n\n"
    else:
        content += "*Methodology phases will be defined based on application.*\n\n"

    content += "## Output Format\n\n"
    if output_format:
        content += f"{output_format}\n\n"
    else:
        content += '''Provide a structured response that includes:
1. **Analysis**: What the methodology reveals about the situation
2. **Application**: Specific recommendations or actions
3. **Rationale**: Why this approach fits the situation

'''

    content += "## Constraints\n\n"
    if constraints:
        for c in constraints:
            content += f"- {c}\n"
    else:
        content += '''- Honor the original context and spirit of the methodology
- Adapt to the specific situation rather than applying mechanically
- Acknowledge limitations and edge cases
- Do not use to harm, deceive, or manipulate
'''

    content += "\n## Anti-Patterns to Avoid\n\n"
    if anti_patterns:
        for ap in anti_patterns:
            if isinstance(ap, dict):
                content += f"- **{ap.get('name', 'Mistake')}**: {ap.get('description', '')}\n"
            else:
                content += f"- {ap}\n"
    else:
        content += "- Applying mechanically without understanding\n- Ignoring context and nuance\n- Missing the underlying principle for surface technique\n"

    content += "\n## Examples\n\n"
    if examples:
        for i, ex in enumerate(examples, 1):
            if isinstance(ex, dict):
                ex_title = ex.get('title', f'Example {i}')
                situation = ex.get('situation', '')
                application = ex.get('application', '')
                output = ex.get('output', '')

                content += f"### Example {i}: {ex_title}\n\n"
                if situation:
                    content += f"**Situation**: {situation}\n\n"
                if application:
                    content += f"**Application**: {application}\n\n"
                if output:
                    content += f"**Output**: {output}\n\n"
            else:
                content += f"### Example {i}\n\n{ex}\n\n"
    else:
        content += f"*See {persona_title}'s work for examples of this methodology in action.*\n\n"

    content += f'''## Integration

This skill derives from **{persona_title}**'s methodology.

'''

    if integration:
        works_with = integration.get('works_with', [])
        when_to_prefer = integration.get('when_to_prefer', '')
        cautions = integration.get('cautions', '')

        if works_with:
            content += "**Works well with:**\n"
            for w in works_with:
                content += f"- {w}\n"
            content += "\n"

        if when_to_prefer:
            content += f"**When to prefer this skill:**\n{when_to_prefer}\n\n"

        if cautions:
            content += f"**Cautions:**\n{cautions}\n"
    else:
        content += f'''**Works well with:**
- Other skills from {persona_title}
- Complementary perspectives from related experts

**When to prefer this skill:**
- The situation matches the trigger conditions above
- You need this specific lens or methodology
'''

    return content

def create_extraction_report(persona_name, skills):
    """Create skill-extraction-report.md"""
    persona_title = persona_name.replace('-', ' ').title()

    content = f'''# Skill Extraction Report: {persona_title}

**Expert:** {persona_name}
**Extraction Date:** 2026-02-12
**Extraction Method:** Production v2

---

## Extracted Skills

'''
    for i, skill in enumerate(skills, 1):
        name = skill.get('name', f'skill-{i}')
        description = skill.get('description', '')

        content += f'''### {i}. {name}

**Description:** {description}

**Priority:** HIGH

---

'''
    return content

def process_persona(persona_name):
    """Process a single persona with production-quality extraction"""
    print(f"\nProcessing {persona_name}...")

    content = get_persona_content(persona_name)
    if not content:
        print(f"  No content found")
        return False

    print(f"  Extracting skills with Claude (production mode)...")
    result = extract_skills_with_claude(persona_name, content)

    if not result or 'skills' not in result:
        print(f"  Failed to extract skills")
        return False

    skills = result['skills']
    if not skills:
        print(f"  No skills extracted")
        return False

    print(f"  Found {len(skills)} skills:")
    for s in skills:
        print(f"    - {s.get('name', 'unnamed')}")

    # Create skill files
    created = 0
    for skill in skills:
        skill_name = skill.get('name', '')
        if not skill_name:
            continue

        skill_dir = SKILLS_DIR / skill_name
        skill_file = skill_dir / "PROMPT.md"

        # Only create if doesn't exist
        if not skill_file.exists():
            skill_dir.mkdir(parents=True, exist_ok=True)
            skill_prompt = create_skill_prompt(skill, persona_name)
            skill_file.write_text(skill_prompt)
            print(f"    Created: {skill_name}")
            created += 1
        else:
            print(f"    Exists: {skill_name}")

    # Create extraction report
    report_path = EXPERTS_DIR / persona_name / "skill-extraction-report.md"
    report_content = create_extraction_report(persona_name, skills)
    report_path.write_text(report_content)
    print(f"  Created skill-extraction-report.md ({created} new skills)")

    return True

def main():
    """Process remaining personas"""
    import sys

    if len(sys.argv) > 1:
        # Process specific personas from command line
        personas = sys.argv[1:]
    else:
        # Find personas without skill-extraction-report.md
        personas = []
        for persona_dir in EXPERTS_DIR.iterdir():
            if persona_dir.is_dir():
                report = persona_dir / "skill-extraction-report.md"
                if not report.exists():
                    personas.append(persona_dir.name)
        personas = sorted(personas)

    print(f"Found {len(personas)} personas to process")

    success = 0
    failed = 0

    for persona in personas:
        try:
            if process_persona(persona):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

    print(f"\n=== Results ===")
    print(f"Success: {success}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
