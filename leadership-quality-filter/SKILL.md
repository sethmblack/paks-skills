---
name: leadership-quality-filter
description: Evaluate whether a leader possesses the three non-negotiable traits (clarity of thinking, work ethic, effectiveness) and identify "hot mess" warning signs that disqualify leadership.
license: MIT
metadata:
  version: 1.0.4368
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- leadership-quality-filter
- writing
---

# Leadership Quality Filter

Evaluate whether a leader possesses the three non-negotiable traits (clarity of thinking, work ethic, effectiveness) and identify "hot mess" warning signs that disqualify leadership.

**Token Budget:** ~600 tokens. Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Make assessments based on protected characteristics (age, gender, race, etc.)
- Provide assessments intended to harm individuals unfairly
- Fabricate behavioral evidence not provided
- Make clinical diagnoses or psychological evaluations

**If asked to assess without evidence:** Request specific behavioral examples before rendering judgment.

---

## When to Use

- User asks "Is this person leadership material?"
- User asks "Should this person run something?"
- User asks "Evaluate this leader"
- User asks for "Hot mess check"
- Making promotion or hiring decisions for leadership roles
- Diagnosing why an initiative is failing
- Assessing executive team composition

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **behavioral_evidence** | Yes | Specific examples of the person's actions, decisions, and results |
| **track_record** | Yes | History of outcomes in previous roles |
| **context** | No | Role being considered, organizational needs, team dynamics |
| **peer_feedback** | No | Observations from those who work with this person |

**Input Validation:**
- If only vague impressions provided: Request specific examples
- If track record missing: Note limitation in assessment confidence

---

## The Three Non-Negotiables

**"It's not how smart you are, or even your communication skills. It's your clarity of thinking, your work ethic and your effectiveness. Those are management traits that are non-negotiable - if you don't have them you will fail."**

### 1. Clarity of Thinking

**Definition:** Ability to cut through complexity to identify core issues and make sound decisions

| Level | Evidence |
|-------|----------|
| Strong | Identifies root causes; decisions are logical and well-reasoned; can explain complex issues simply; separates signal from noise |
| Adequate | Generally sound reasoning; occasional confusion under complexity; needs some guidance on novel problems |
| Weak | Frequently misdiagnoses problems; decisions lack clear logic; overwhelmed by complexity; conflates symptoms with causes |

**Key questions:**
- When faced with a complex problem, do they find clarity or create confusion?
- Can they explain their reasoning simply?
- Do their decisions follow from their analysis?

### 2. Work Ethic

**Definition:** Consistent, relentless effort applied to the right priorities

| Level | Evidence |
|-------|----------|
| Strong | Consistently high output; works until the job is done; prioritizes effectively; sets example for others; shows up prepared |
| Adequate | Generally reliable; occasional lapses in follow-through; solid but not exemplary effort |
| Weak | Inconsistent effort; cuts corners; leaves work incomplete; relies on others to carry the load; frequently unprepared |

**Key questions:**
- Do they do what they say they will do?
- Is their effort consistent or sporadic?
- Do they work hard on the right things?

### 3. Effectiveness

**Definition:** Actually achieving results, not just activity

| Level | Evidence |
|-------|----------|
| Strong | Track record of delivered outcomes; objectives achieved; measurable impact on organization; problems get solved |
| Adequate | Generally achieves objectives; some misses; results vary by context |
| Weak | Lots of activity, little result; initiatives stall; problems persist despite effort; excuses outweigh outcomes |

**Key questions:**
- What has this person actually accomplished?
- Do their efforts translate into outcomes?
- When they take ownership, do things get better?

---

## The "Hot Mess" Indicators

**"A lot of people who run stuff, they're a hot mess. Don't let them run something because they'll be a disaster."**

| Indicator | Why It Matters |
|-----------|---------------|
| Always late | Cannot manage their own time; will not manage others' time well |
| Disorganized | Chaos follows them; creates more problems than they solve |
| Not doing their jobs | Expects others to cover; erodes team performance |
| Weighs the whole company down | Negative multiplier on everyone they touch |
| Avoids accountability | Problems persist because no one owns them |
| Drama magnet | Creates unnecessary conflict and distraction |

**Two or more hot mess indicators = Do not let them run something.**

---

## Workflow
### Step 1: Gather Behavioral Evidence

Collect specific examples for each non-negotiable:
- Decisions made and their outcomes
- Work patterns and consistency
- Results achieved (or not achieved)

### Step 2: Score Each Non-Negotiable

| Trait | Strong (3) | Adequate (2) | Weak (1) |
|-------|-----------|--------------|----------|
| Clarity of Thinking | | | |
| Work Ethic | | | |
| Effectiveness | | | |

**Minimum for leadership role:** No trait below "Adequate" (2)
**Ideal for leadership role:** All traits "Strong" (3)

### Step 3: Check Hot Mess Indicators

Review evidence for hot mess warning signs. Count indicators present.

### Step 4: Make Determination

| Score | Hot Mess Count | Determination |
|-------|---------------|---------------|
| 7-9 | 0-1 | **Cleared for leadership** - strong candidate |
| 5-6 | 0-1 | **Conditional** - can lead with support/development |
| Any | 2+ | **Not cleared** - hot mess indicators disqualify |
| Any trait = 1 | Any | **Not cleared** - non-negotiable failure |

---

## Output Format

```markdown
## Leadership Quality Filter

**Subject:** {name or role}
**Assessment Date:** {date}
**Determination:** {Cleared / Conditional / Not Cleared}

### Non-Negotiable Assessment

| Trait | Score | Evidence |
|-------|-------|----------|
| Clarity of Thinking | {1-3} | {specific examples} |
| Work Ethic | {1-3} | {specific examples} |
| Effectiveness | {1-3} | {specific examples} |

**Total:** {X}/9

### Hot Mess Indicators

| Indicator | Present? | Evidence |
|-----------|----------|----------|
| Always late | {Yes/No} | {if yes, examples} |
| Disorganized | {Yes/No} | {if yes, examples} |
| Not doing their job | {Yes/No} | {if yes, examples} |
| Weighs company down | {Yes/No} | {if yes, examples} |
| Avoids accountability | {Yes/No} | {if yes, examples} |
| Drama magnet | {Yes/No} | {if yes, examples} |

**Hot Mess Count:** {X}/6

### Determination

{2-3 sentences explaining the determination with specific reasoning}

### Recommendations

{If Conditional: what development is needed}
{If Not Cleared: what role might be appropriate instead}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient evidence | Request specific behavioral examples; note confidence limitations |
| Conflicting evidence | Note conflicting signals; recommend additional observation |
| Strong on two, weak on one | Not cleared - all three are non-negotiable |
| Personal bias suspected | Focus on observable behaviors and outcomes only |
| High performer with hot mess signs | Assess carefully - results may mask dysfunction that affects others |

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

**Input:** Evaluating VP candidate who led successful product launch but team morale dropped significantly during the project, and two key people left.

**Output (summary):**

### Determination: Conditional

The successful product launch demonstrates effectiveness (3/3). Work ethic appears strong given the outcome achieved (3/3). However, the team attrition and morale decline raise concerns about clarity of thinking regarding people leadership (2/3) - they may be solving problems in ways that create new ones.

No hot mess indicators are present, but the pattern of "results at any cost" requires monitoring. Clear this person for leadership only with explicit expectations about team health metrics and a 90-day review of retention and morale in their new scope.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's leadership evaluation framework. When invoked by the Dimon expert, outputs should maintain his direct, no-nonsense voice about leadership standards.

**Related skills:** accountability-mapping, honest-assessment-protocol