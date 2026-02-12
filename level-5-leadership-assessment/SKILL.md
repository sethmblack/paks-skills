---
name: level-5-leadership-assessment
description: Assess leadership against Jim Collins' research-based five-level hierarchy,
  identifying current level, specific gaps, and development path toward Level 5 leadership.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- level-5-leadership-assessment
- writing
---

# Level 5 Leadership Assessment

Assess leadership against Jim Collins' research-based five-level hierarchy, identifying current level, specific gaps, and development path toward Level 5 leadership.

**Token Budget:** ~900 tokens. Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide assessment without evidence-based questions
- Claim someone is Level 5 without rigorous validation
- Use this assessment to harm, manipulate, or unfairly judge individuals
- Skip the window/mirror diagnostic

**If insufficient information:** Note what cannot be assessed and what additional input is needed.

---

## When to Use

- User asks "Am I a Level 5 leader?" or "How can I improve my leadership?"
- Executive development or succession planning context
- Leadership team evaluation
- Self-assessment for personal development
- User explicitly requests Level 5 assessment

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `leadership_context` | Yes | Role, organization, scope of responsibility | Must have leadership responsibility |
| `behaviors_observed` | Yes | Specific actions and patterns | Concrete examples, not aspirations |
| `attribution_patterns` | No | How they explain success and failure | Critical for Level 5 diagnosis |
| `ambition_orientation` | No | What they are ambitious for | Self vs. organization vs. cause |

---

## Background: The Level 5 Hierarchy

From Jim Collins' *Good to Great* research:

> "Level 5 leaders channel their ego needs away from themselves and into the larger goal of building a great company. It's not that Level 5 leaders have no ego or self-interest. Indeed, they are incredibly ambitious - but their ambition is first and foremost for the institution, not themselves."

### The Five Levels

| Level | Title | Capability |
|-------|-------|------------|
| 5 | Executive | Builds enduring greatness through paradoxical blend of personal humility + professional will |
| 4 | Effective Leader | Catalyzes commitment to and vigorous pursuit of compelling vision; stimulates higher performance |
| 3 | Competent Manager | Organizes people and resources toward effective pursuit of pre-determined objectives |
| 2 | Contributing Team Member | Contributes individual capabilities to achievement of group objectives; works effectively in group |
| 1 | Highly Capable Individual | Makes productive contributions through talent, knowledge, skills, and good work habits |

---

## Workflow
### Phase 1: Establish Baseline Level

Assess against each level in sequence. A leader must exhibit characteristics of lower levels to be assessed at higher levels.

**Level 1 Assessment:**
- Does this person make productive individual contributions?
- Do they have the baseline capabilities for their domain?
- Evidence: work product quality, technical competence

**Level 2 Assessment:**
- Do they work effectively with others toward group goals?
- Do they contribute to team success beyond individual work?
- Evidence: collaboration patterns, team feedback

**Level 3 Assessment:**
- Can they organize people and resources toward objectives?
- Do they achieve planned results through others?
- Evidence: project outcomes, resource allocation, goal achievement

**Level 4 Assessment:**
- Do they catalyze commitment to a compelling vision?
- Do they stimulate higher performance from their team?
- Evidence: team engagement, ambitious goal pursuit, performance lift

### Phase 2: The Level 5 Diagnostic

Level 5 requires BOTH personal humility AND professional will. Assess each:

**Personal Humility Indicators:**

| Indicator | Diagnostic Question | What to Look For |
|-----------|---------------------|------------------|
| Self-effacing | How do they describe personal achievements? | Deflects credit, attributes to team and luck |
| Quiet determination | How do they communicate resolve? | Relies on inspired standards, not inspiring personality |
| Succession focus | Have they developed successors? | Sets up next generation for even greater success |
| Credit distribution | How do they explain good results? | Window: points outside to give credit |

**Professional Will Indicators:**

| Indicator | Diagnostic Question | What to Look For |
|-----------|---------------------|------------------|
| Unwavering resolve | How do they respond to obstacles? | Does whatever it takes to produce results |
| Standard setting | What level of results do they accept? | Settles for nothing less than best results |
| Blame acceptance | How do they explain poor results? | Mirror: looks inward to assign responsibility |
| Institution building | What is their ambition directed toward? | Building something greater than themselves |

### Phase 3: The Window and Mirror Test

**This is the critical Level 5 diagnostic.**

**When things go well** (Window Test):
- Level 5 leaders look OUT THE WINDOW to find factors outside themselves to give credit
- They credit other people, external factors, and good luck
- Red flag: Taking personal credit, "I" language, ego display

**When things go poorly** (Mirror Test):
- Level 5 leaders look IN THE MIRROR to apportion responsibility
- They take responsibility, never blame bad luck or external factors
- Red flag: Blaming circumstances, other people, market conditions

**Assessment questions:**

### Step 1: "Tell me about a major success. What caused it?"



### Step 2: "Tell me about a significant failure. What caused it?"



### Step 3: Listen for window (external attribution for success) and mirror (internal attribution for failure)



### Phase 4: Ambition Audit

**What are they ambitious FOR?**

| Ambition Type | Indicators | Level Implication |
|---------------|------------|-------------------|
| Self | Career advancement, personal recognition, compensation | Caps at Level 4 |
| Organization | Company success, team achievement | Potential Level 5 |
| Cause/Mission | Something larger than any organization | Strong Level 5 indicator |

**Key question:** "If the organization's success required you to step aside, would you?"

### Phase 5: Deliver Assessment

Format the output as a Level 5 Leadership Assessment Report.

---

## Output Format

```markdown
## Level 5 Leadership Assessment: [Name/Role]

### Baseline Assessment

| Level | Status | Evidence |
|-------|--------|----------|
| Level 1: Capable Individual | Achieved/Not Achieved | [Evidence] |
| Level 2: Team Member | Achieved/Not Achieved | [Evidence] |
| Level 3: Competent Manager | Achieved/Not Achieved | [Evidence] |
| Level 4: Effective Leader | Achieved/Not Achieved | [Evidence] |

### Level 5 Component Analysis

**Personal Humility:** [Strong/Developing/Weak]
- Self-effacing nature: [Assessment]
- Credit distribution: [Assessment]
- Succession focus: [Assessment]

**Professional Will:** [Strong/Developing/Weak]
- Unwavering resolve: [Assessment]
- Standard setting: [Assessment]
- Blame acceptance: [Assessment]

### Window and Mirror Diagnostic

**Success Attribution (Window):** [Looks out/Looks in]
- [Specific example and analysis]

**Failure Attribution (Mirror):** [Looks in/Looks out]
- [Specific example and analysis]

**Verdict:** [Passes Window-Mirror Test / Does Not Pass]

### Ambition Orientation

**Primary Ambition:** [Self/Organization/Cause]
- [Evidence and analysis]

### Overall Assessment

**Current Level:** [1-5]

**Level 5 Readiness:** [Ready/Developing/Not Ready]

**Key Gaps:**
1. [Specific gap with evidence]
2. [Specific gap with evidence]

### Development Recommendations

1. [Specific action to address gap]
2. [Specific action to strengthen existing capability]
3. [Practice or experience to build Level 5 qualities]

### Cautionary Notes

- [What might prevent Level 5 development]
- [Patterns to monitor]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Self-assessment only | Note limitations of self-reporting; recommend 360-degree input |
| Insufficient examples | Request specific behavioral examples before assessing |
| Mixed signals | Document the inconsistency; note that Level 5 is rare |
| User wants instant Level 5 label | Explain that Level 5 is validated through years of results, not self-proclamation |
| Assessment for hiring decision | Note that Level 5 qualities often emerge over time; assess potential |

---

## Example (abbreviated)

**Input:**
```
Role: CEO of $50M manufacturing company, 7 years tenure
Behaviors: Turned around struggling division, built strong management team
Success story: "We had the right strategy and our team executed flawlessly"
Failure story: "The market shifted and our competitors got lucky with timing"
```

**Assessment:**

### Window and Mirror Diagnostic

**Success Attribution:** Partial window - credits team but also implies strategic genius ("right strategy")

**Failure Attribution:** Looks OUT - blames market and competitor luck, not internal factors

**Verdict:** Does Not Pass Window-Mirror Test

The attribution patterns suggest Level 4 leadership with ego still central. A Level 5 leader would attribute failure to internal factors ("We didn't anticipate the shift; I should have...") and success more fully to external factors and team.

### Overall Assessment

**Current Level:** 4 - Effective Leader

**Level 5 Readiness:** Developing

---

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill is part of the **Jim Collins** expert persona. When invoked:
- Ground assessment in Collins' research evidence
- Be direct about gaps - Level 5 is rare by definition
- Emphasize that Level 5 is about behavior patterns, not personality
- Note that Level 5 can be developed; it is not innate

---

## Success Criteria

Assessment is complete when:

1. Baseline levels 1-4 have been assessed
2. Both humility and will components are analyzed
3. Window/mirror diagnostic is applied
4. Ambition orientation is identified
5. Current level is declared with evidence
6. Specific development recommendations are provided