---
name: values-first-evaluation
description: Evaluate team members or candidates using the principle of "zero tolerance
  for values violations; infinite patience for skill development.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- escalation
- values-first-evaluation
- writing
---

# Values-First Evaluation

Evaluate team members or candidates using the principle of "zero tolerance for values violations; infinite patience for skill development."

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for output generation.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create evaluations that use values as pretense for discrimination
- Design frameworks to justify predetermined termination decisions
- Weaponize values evaluations against whistleblowers or dissenters
- Apply values standards inconsistently based on performance level

**If asked to misuse values evaluation:** Refuse explicitly. Explain that values-first evaluation must be applied consistently and fairly.

---

## When to Use

- Leader asks "Should I keep this team member?"
- High performer exhibits cultural problems
- Candidate evaluation needs character assessment
- Team member struggling but has good attitude
- User asks "How do I evaluate cultural fit?"
- Performance review needs values component

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **person** | Yes | Role and context of person being evaluated |
| **behaviors** | Yes | Expected behaviors or values to evaluate against |
| **incidents** | No | Specific incidents or patterns observed |
| **skills_assessment** | No | Current skill level assessment |
| **context** | No | Relevant context (tenure, recent changes, etc.) |

**Input Validation:**
- `behaviors`: Must have documented expected behaviors to evaluate against
- Cannot evaluate against unstated or unevenly applied standards

---

## Workflow
### 1. Separate Values from Skills

Create two distinct assessments:

**Values Assessment:**
- Observable adherence to expected behaviors
- Character and integrity indicators
- Treatment of others
- Consistency between words and actions

**Skills Assessment:**
- Technical competency
- Domain knowledge
- Productivity and output
- Learning velocity

### 2. Apply the Mulally Principle

**Core Rule:** "Skills can be taught; character cannot."

| Quadrant | Values | Skills | Action |
|----------|--------|--------|--------|
| A | Strong | Strong | Retain, promote, celebrate |
| B | Strong | Weak | Retain, coach, develop |
| C | Weak | Strong | Address immediately, high risk |
| D | Weak | Weak | Exit process |

**Critical insight:** Quadrant C (high performer with values problems) is the most dangerous. Their output makes leaders reluctant to act, but they damage culture disproportionately.

### 3. Evidence-Based Assessment

For values evaluation, document:
- Specific observable behaviors
- Pattern vs. isolated incident
- Impact on others
- Response to feedback

**Avoid:**
- Vague accusations ("bad attitude")
- Hearsay without verification
- Single incidents without pattern
- Inconsistent application of standards

### 4. Determine Action

**For Values Violations:**

### Step 1: Address immediately and directly



### Step 2: State expectation clearly



### Step 3: Document the conversation



### Step 4: Set clear timeline for change



### Step 5: Zero tolerance means consequences if repeated



**For Skill Gaps:**

### Step 1: Assess coachability



### Step 2: Create development plan



### Step 3: Provide resources and support



### Step 4: Set milestones with patience



### Step 5: Celebrate improvement



### 5. Document Decision

Create clear record of:
- Assessment criteria used
- Evidence evaluated
- Decision made
- Rationale
- Follow-up plan

---

## Outputs

### Values-First Evaluation Report

```markdown
# Values-First Evaluation: [Person/Role]

**Evaluation Date:** [Date]
**Evaluator:** [Name/Role]
**Expected Behaviors Reference:** [Document name]

## Values Assessment

| Expected Behavior | Rating | Evidence |
|-------------------|--------|----------|
| [Behavior 1] | [Strong/Adequate/Concern/Violation] | [Specific observations] |
| [Behavior 2] | [Strong/Adequate/Concern/Violation] | [Specific observations] |
| [Behavior 3] | [Strong/Adequate/Concern/Violation] | [Specific observations] |

**Values Summary:** [Overall assessment]

### Specific Incidents (if applicable)

| Date | Incident | Behavior Violated | Impact |
|------|----------|-------------------|--------|
| [Date] | [Description] | [Behavior] | [Impact on team/org] |

## Skills Assessment

| Skill Area | Rating | Notes |
|------------|--------|-------|
| [Skill 1] | [Expert/Proficient/Developing/Novice] | [Notes] |
| [Skill 2] | [Expert/Proficient/Developing/Novice] | [Notes] |
| [Skill 3] | [Expert/Proficient/Developing/Novice] | [Notes] |

**Skills Summary:** [Overall assessment]

## Quadrant Placement

```
Values →  Weak                Strong
         ┌─────────────┬─────────────┐
  Strong │ C: Address  │ A: Retain   │
Skills ↓ │    now      │   promote   │
         ├─────────────┼─────────────┤
    Weak │ D: Exit     │ B: Coach    │
         │             │   develop   │
         └─────────────┴─────────────┘
```

**This person is in Quadrant: [A/B/C/D]**

## Recommendation

**Action:** [Retain/Coach/Address/Exit]

**Rationale:**
[Explanation applying the "skills can be taught; character cannot" principle]

**Specific Next Steps:**
1. [Action with timeline]
2. [Action with timeline]
3. [Action with timeline]

## Follow-Up Plan

| Milestone | Date | Success Criteria |
|-----------|------|------------------|
| [Milestone] | [Date] | [Criteria] |

## Values-First Commitment

- [ ] Assessment applied same standards as for other team members
- [ ] Performance level did not influence values assessment
- [ ] Person was given fair opportunity to demonstrate values
- [ ] Feedback was clear and specific
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No documented expected behaviors | Cannot evaluate; create behaviors first |
| Single incident, no pattern | Note concern, increase observation, don't over-react |
| Leader wants to protect high performer | Emphasize: "Quadrant C is most dangerous to culture" |
| Person claims values weren't communicated | Address communication gap, then reset expectations |
| Values applied inconsistently across team | Acknowledge and correct; cannot enforce selectively |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
person: Senior Engineer, 18 months tenure
behaviors: [List of team expected behaviors]
incidents: "In last 3 retrospectives, blamed others for issues.
           In code reviews, leaves dismissive comments.
           Junior engineers avoid asking them questions."
skills_assessment: "Top 10% technical contributor, ships features fast"
```

**Output:** [Quadrant C assessment. Recommendation to address immediately with clear conversation about "communicate candidly but respectfully" and "never at others' expense" behaviors. Development plan for interpersonal skills. Clear timeline: improvement within 30 days or escalation. Note that technical excellence does not excuse cultural damage.]

---

## Integration

This skill integrates with:
- **expected-behaviors-design** - Provides the criteria for evaluation
- **transparency-culture-launch** - Honest feedback requires psychological safety
- **alignment-check** - Values alignment is part of overall alignment

**Source Expert:** Alan Mulally - Based on his principle that he tolerated skill gaps indefinitely but had zero tolerance for values violations.