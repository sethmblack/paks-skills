---
name: okr-creation
description: Transform vague goals and aspirations into properly structured OKRs (Objectives and Key Results) with measurable key results, following John Doerr's methodology from *Measure What Matters*.
license: MIT
metadata:
  version: 1.0.1543
  author: sethmblack
keywords:
- okr-creation
- transformation
- writing
---

# OKR Creation

Transform vague goals and aspirations into properly structured OKRs (Objectives and Key Results) with measurable key results, following John Doerr's methodology from *Measure What Matters*.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create OKRs for harmful, illegal, or unethical objectives
- Set key results that would harm people or organizations
- Fabricate baseline metrics or unrealistic targets

**If asked to create harmful OKRs:** Refuse explicitly and explain why the objective is problematic.

---

## When to Use

- User has a vague goal or aspiration that needs structure
- User says "Create OKRs for...", "Turn this goal into OKRs", "Help me set objectives"
- User has a vision but lacks measurable success criteria
- User needs to translate strategy into executable quarterly goals

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| goal | Yes | The vague goal, aspiration, or vision to transform |
| context | No | Domain, industry, or organizational context |
| timeline | No | Target timeframe (defaults to quarterly) |
| baseline | No | Current state metrics if available |

---

## Workflow

### Step 1: Clarify the Objective

Ask: What is the person or organization actually trying to achieve?

Transform the input into a clear Objective that is:
- **Significant** - Matters to the organization
- **Concrete** - Specific enough to visualize
- **Action-oriented** - Begins with an action verb or implies action
- **Inspirational** - Motivates and energizes

**Test:** Is this objective meaningful, audacious, and inspiring?

### Step 2: Establish Baseline

Identify what can be measured:
- What is the current state?
- What metrics exist?
- What data is available?

If baseline unknown, note as "TBD - establish baseline before finalizing"

### Step 3: Define Key Results

Create 3-5 Key Results that:
- Are **quantitative** (specific numbers)
- Are **time-bound** (by when)
- Are **verifiable** (can objectively determine if achieved)
- Measure **outcomes**, not activities
- Are **ambitious but achievable** (60-70% confidence)

**Test each KR:** "Did I do this or didn't I?" must have a clear yes/no answer.

### Step 4: Assign Ownership and Cadence

Recommend:
- Who should own each Key Result
- What review cadence is appropriate (weekly check-in, quarterly grading)
- Whether these are Committed (must hit) or Aspirational (stretch)

---

## Output Format

```markdown
## OKR: [Title]

**Objective:** [Qualitative, inspirational statement]

**Key Results:**
- KR1: [Specific metric] from [baseline] to [target] by [date]
- KR2: [Specific metric] from [baseline] to [target] by [date]
- KR3: [Specific metric] from [baseline] to [target] by [date]

**Type:** Committed / Aspirational

**Grading Notes:**
- 0.0-0.3: [What failure looks like]
- 0.4-0.6: [What partial progress looks like]
- 0.7-1.0: [What success looks like]

**Owner:** [Recommended owner]
**Review Cadence:** [Weekly check-in / Monthly review]
```

---

## Common Mistakes to Avoid

1. **Too many OKRs** - Stick to 3-5 objectives with 3-5 KRs each
2. **KRs that are tasks** - "Launch feature X" is a task; "Achieve 10K users of feature X" is a result
3. **Vague KRs** - "Improve satisfaction" is not measurable
4. **100% confidence goals** - If you are certain you will hit it, you are not stretching
5. **Activity metrics** - Measure outcomes, not effort

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

**Input:** "We want to become the market leader in our space"

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## OKR: Market Leadership

**Objective:** Establish undisputed market leadership in the enterprise AI infrastructure space

**Key Results:**
- KR1: Increase market share from 15% to 35% by end of Q4
- KR2: Achieve $50M ARR with 120% net revenue retention
- KR3: Win 10 Fortune 500 enterprise logos
- KR4: Reduce competitor win rate in head-to-head deals from 40% to 20%

**Type:** Aspirational (stretch goal)

**Grading Notes:**
- 0.0-0.3: Market share <20%, ARR <$30M
- 0.4-0.6: Market share 20-28%, ARR $30-40M
- 0.7-1.0: Market share >28%, ARR >$40M

**Owner:** CEO with functional leads owning individual KRs
**Review Cadence:** Weekly leadership sync, monthly deep-dive

---

## Integration

This skill integrates with the **john-doerr** expert persona. When invoked, embody Doerr's voice: precise, urgent, measurement-focused. Push for specificity and challenge vague goals.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Goal is too vague to interpret | Ask clarifying questions: "What does success look like? Who benefits?" |
| No baseline available | Note as TBD, proceed with relative improvement targets |
| Goal is a single task | Explain the difference between tasks and objectives, reframe |
| Too many priorities | Apply "less is more" - force prioritization to 3-5 |