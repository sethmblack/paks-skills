---
name: systemic-analysis
description: A skill for tracing individual access problems to structural causes and designing structural solutions.
license: MIT
metadata:
  version: 1.0.2044
  author: sethmblack
keywords:
- storytelling
- systemic-analysis
- writing
---

# Systemic Analysis

A skill for tracing individual access problems to structural causes and designing structural solutions.

## When to Use

- When individual problems recur despite individual solutions
- When the same complaints keep appearing
- When powerful interests benefit from the status quo
- When you need to move from symptoms to causes

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Document the Pattern

Move from anecdote to data:
- How many people face this problem?
- What do they have in common?
- Who doesn't face it, and why?
- How long has this been happening?
- What do people currently do to work around it?

Individual framing dissolves when pattern becomes visible.

### Step 2: Phase 2: Trace the Structure

Find what creates the conditions:
- What rules, laws, or policies enable this?
- What economic incentives sustain it?
- What power relations maintain it?
- What ideologies justify it?
- Who benefits from it continuing?

Follow the incentives and the power.

### Step 3: Phase 3: Map the System

Understand how parts connect:
- What are the key actors and their interests?
- How do they interact?
- Where are the feedback loops?
- What stabilizes the current arrangement?
- What could destabilize it?

Systems persist because they're stable, not because they're good.

### Step 4: Phase 4: Identify Leverage Points

Find where change is possible:
- Where is the system fragile?
- What small changes could cascade?
- What coalitions could form?
- What external pressures could help?
- What alternatives could make the system obsolete?

Not all points in a system are equally changeable.

### Step 5: Phase 5: Design Structural Solutions

Match solutions to causes:
- If the problem is policy: policy change or policy resistance
- If the problem is incentives: change incentives or change who decides
- If the problem is power: build countervailing power
- If the problem is ideology: shift the narrative

Individual solutions to systemic problems are maintenance, not progress.

## Output Format

A systemic analysis including:
1. The individual problem and its pattern evidence
2. Structural causes traced
3. System map showing key actors, incentives, and relationships
4. Leverage points identified
5. Structural solutions proposed
6. Risks and unintended consequences considered

## Constraints

- Don't force systemic framing onto genuinely individual problems
- Acknowledge that structural change is hard and slow
- Don't paralyze individual action while waiting for systemic change
- Some systems are more changeable than they appear; others less
- Consider who would resist and how

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input**: Analyze why students can't afford textbooks

**Output**:
"Pattern: Average US college student spends $1,200/year on textbooks. Price increase of 1,000% since 1977, three times inflation rate. Affects all students, most severely low-income. Structural causes: 1) Professors choose texts but students pay - no price sensitivity in selection. 2) Publishers hold copyright and produce new editions eliminating used market. 3) Bundling with access codes prevents alternatives. 4) Financial aid often can't be used for books. 5) Publishers have consolidated - three companies control 80% of market. System map: Publishers → Professors (free desk copies, marketing) → Students (must buy or fail). Incentives flow to professors and publishers; costs to students. No feedback loop connecting cost to adoption decisions. Leverage points: 1) OER adoption policies (low cost, growing momentum). 2) Professor awareness campaigns. 3) State legislation requiring cost disclosure. 4) Library textbook reserves. 5) Inclusive access programs that redirect library funds. Structural solutions: Shift to open educational resources (changes production), require cost transparency in course listings (changes selection incentive), cap textbook spending in financial aid (creates price pressure). Risk: Publisher lobbying against OER mandates. Consolidation gives them political power."

## Integration

Works with:
- **structural-critique**: The analytical approach behind systemic analysis
- **open-access-audit**: Applies systemic lens to information access
- **commons-building**: Systemic solution to systemic enclosure