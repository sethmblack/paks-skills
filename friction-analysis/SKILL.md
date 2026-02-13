---
name: friction-analysis
description: '**Expert Origin:** Carl von Clausewitz **Skill Type:** Diagnostic Framework **Trigger:** "Why isn''t this working as planned?" / "Plans keep failing in execution'
license: MIT
metadata:
  version: 1.0.1021
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- friction-analysis
- writing
---

# Friction Analysis

**Expert Origin:** Carl von Clausewitz
**Skill Type:** Diagnostic Framework
**Trigger:** "Why isn't this working as planned?" / "Plans keep failing in execution"

---

## Purpose

Diagnose why well-conceived plans fail in execution by identifying sources of friction—the countless minor difficulties that accumulate to create a gap between theory and reality.

---

## The Clausewitz Principle

*"Everything is very simple in war, but the simplest thing is difficult. These difficulties accumulate and produce a friction which no man can imagine exactly who has not seen war."*

Friction is not a bug to be eliminated but a fundamental feature of reality. The commander who ignores friction will be perpetually surprised; the commander who accounts for it builds resilience.

---

## Friction Categories

### 1. Physical Friction
- Exhaustion and fatigue
- Equipment failure
- Weather and environmental factors
- Distance and logistics
- Material shortages

### 2. Information Friction
- Delayed communication
- Distorted reports
- Missing data
- Contradictory intelligence
- Misunderstood orders

### 3. Human Friction
- Fear, doubt, confusion
- Conflicting personalities
- Differing interpretations
- Motivation failures
- Skill gaps

### 4. Organizational Friction
- Coordination failures
- Bureaucratic delays
- Competing priorities
- Unclear authority
- Process overhead

### 5. External Friction
- Competitor responses
- Market changes
- Regulatory shifts
- Stakeholder resistance
- Timing misalignments

---

## Workflow
### Step 1: Map the Plan-Reality Gap

| Planned | Actual | Gap |
|---------|--------|-----|
| What was supposed to happen | What actually happened | The difference |

For each significant gap, ask: What friction produced this?

### Step 2: Categorize Friction Sources

For each friction source identified:

| Source | Category | Severity | Reducible? |
|--------|----------|----------|------------|
| [Specific friction] | Physical/Information/Human/Organizational/External | High/Medium/Low | Yes/Partially/No |

### Step 3: Distinguish Reducible from Inherent Friction

**Reducible Friction:** Can be addressed through:
- Better planning
- More resources
- Improved communication
- Training and preparation
- Process changes

**Inherent Friction:** Must be absorbed through:
- Reserves and slack
- Flexible plans
- Empowered decision-making
- Acceptance of uncertainty

### Step 4: Assess Cumulative Impact

Individual frictions may seem minor. Their cumulative effect is decisive.

Questions to ask:
- How many friction sources are operating simultaneously?
- Are they compounding each other?
- At what point does cumulative friction cause systemic failure?
- Where are the cascading effects?

### Step 5: Build Friction Tolerance

For future planning:

| Friction Type | Mitigation Strategy |
|---------------|---------------------|
| Physical | Reserves, redundancy, slack time |
| Information | Multiple channels, verification, direct observation |
| Human | Training, clear intent, trust-building |
| Organizational | Simplified structure, decentralized authority |
| External | Scenario planning, adaptive frameworks |

---

## Outputs
### Friction Analysis Report

**Situation:** [Brief description]

**Plan-Reality Gaps:**
1. [Gap 1]: [Planned vs. Actual]
2. [Gap 2]: [Planned vs. Actual]
3. [Gap 3]: [Planned vs. Actual]

**Friction Sources Identified:**
| Source | Category | Severity | Reducible? |
|--------|----------|----------|------------|
| ... | ... | ... | ... |

**Cumulative Assessment:**
[How are these frictions compounding? What is the total impact?]

**Recommendations:**
- **Reduce:** [Friction that can be addressed]
- **Absorb:** [Friction that must be accepted]
- **Build Tolerance:** [Changes for future resilience]

**Clausewitz Counsel:**
[Perspective on accepting friction as inherent to complex endeavors]

---

## Example Application

**Situation:** Product launch delayed by three months despite detailed planning.

**Plan-Reality Gaps:**
1. Development completion: Planned 8 weeks, Actual 14 weeks
2. QA cycle: Planned 2 weeks, Actual 5 weeks
3. Partner integration: Planned simultaneous, Actual sequential

**Friction Sources Identified:**
| Source | Category | Severity | Reducible? |
|--------|----------|----------|------------|
| Key developer illness | Human | High | No |
| Unclear requirements discovered late | Information | High | Yes |
| Testing environment unavailable | Organizational | Medium | Yes |
| Partner API changed mid-project | External | High | Partially |
| Team stretched across multiple projects | Organizational | Medium | Yes |

**Cumulative Assessment:**
Five significant friction sources compounded. Developer illness triggered cascade: work redistributed to already-stretched team, causing requirement misunderstandings, extending QA. Partner change forced reactive development.

**Recommendations:**
- **Reduce:** Formalize requirements earlier; dedicated testing environment; reduce concurrent project load
- **Absorb:** Accept that external partner changes will occur; build buffer
- **Build Tolerance:** 25% time buffer on all estimates; identify backup resources before crises

**Clausewitz Counsel:**
*"The plan appeared sound because it assumed each element would function as designed. But friction ensures nothing functions exactly as designed. The next plan must not seek to eliminate friction—that is impossible—but to build reserves sufficient to absorb it."*

---

## When to Use
- Post-mortems on failed or delayed initiatives
- Mid-project assessments when things are going wrong
- Pre-launch readiness reviews
- Any situation where "the plan was good but execution failed"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Voice Note

When delivering friction analysis, maintain Clausewitz's philosophical acceptance. Friction is not failure—it is reality. The counsel is not "try harder" but "build tolerance for what cannot be controlled."

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

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems