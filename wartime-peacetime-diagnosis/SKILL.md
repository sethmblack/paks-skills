---
name: wartime-peacetime-diagnosis
description: Diagnose whether an organization is in wartime (survival) or peacetime
  (growth) mode and prescribe the appropriate leadership style.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- wartime-peacetime-diagnosis
- writing
---

# Wartime-Peacetime Diagnosis

Diagnose whether an organization is in wartime (survival) or peacetime (growth) mode and prescribe the appropriate leadership style.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend illegal actions to "win the war"
- Advise deception of employees, investors, or customers
- Prescribe wartime tactics that violate labor laws or ethical standards

**If asked to diagnose for harmful purposes:** Refuse explicitly. State that this framework is for legitimate business survival, not exploitation.

---

## When to Use

- CEO or leader asks "Is my company in crisis?"
- Leadership style is not producing expected results
- Competition is winning decisively
- Market dynamics are shifting
- Team is burning out or complacent
- Decision-making feels mismatched to situation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **situation** | Yes | Description of company's current state |
| **competitive_position** | Yes | How the company stands vs. competitors |
| **runway** | No | Cash runway or financial pressure |
| **team_retention** | No | Are best people staying or leaving? |
| **market_dynamics** | No | Is market growing, stable, or contracting? |

---

## Diagnostic Framework

### The Four Diagnostic Questions

Answer each question based on the inputs provided:

1. **Is the company's survival threatened in the next 12 months?**
   - Yes = wartime signal
   - No = peacetime signal

2. **Is a competitor winning decisively?**
   - Yes = wartime signal
   - No = peacetime signal

3. **Has the market fundamentally shifted against you?**
   - Yes = wartime signal
   - No = peacetime signal

4. **Are you losing your best people to competitors?**
   - Yes = wartime signal
   - No = peacetime signal

**Scoring:** If ANY answer is yes, the organization is likely in wartime.

### Mode Definitions

**Peacetime:** "Those times when a company has a large advantage vs. the competition in its core market, and its market is growing. In times of peace, the company can focus on expanding the market and reinforcing the company's strengths."

**Wartime:** "The company typically has a single bullet in the chamber and must, at all costs, hit the target. The company's survival depends upon strict adherence and alignment to the mission."

### Behavioral Contrasts

| Dimension | Peacetime Behavior | Wartime Behavior |
|-----------|-------------------|------------------|
| Protocol | Follow proper protocol to win | Violate protocol in order to win |
| Competition | Other ships in a big ocean | Someone trying to kidnap your children |
| Market | Aim to expand | Aim to win |
| Culture | Spend time defining culture | Let the war define culture |
| Detail | Empower others for details | Care about every speck that interferes |
| Goals | Big, hairy, audacious goals | Too busy fighting to read management books |

---

## Workflow
### Step 1: Gather Situation Data

Identify or request:
- Current competitive position
- Financial runway
- Recent team departures
- Market trajectory
- Recent performance vs. plan

### Step 2: Apply Diagnostic Questions

Score each of the four questions. Document evidence for each answer.

### Step 3: Determine Mode

- 0 "yes" answers = Peacetime
- 1-2 "yes" answers = Transition zone (likely wartime)
- 3-4 "yes" answers = Definite wartime

### Step 4: Assess Current Leadership Style

Compare current behavior to the behavioral contrasts table. Identify mismatches.

### Step 5: Prescribe Changes

Based on mode and mismatches, provide specific behavioral changes.

---

## Outputs

### Diagnosis Report Format

```markdown
## Wartime/Peacetime Diagnosis

### Assessment Summary

**Mode:** [Wartime / Peacetime / Transition]
**Confidence:** [High / Medium / Low]

### Diagnostic Question Scores

| Question | Answer | Evidence |
|----------|--------|----------|
| Survival threatened in 12 months? | [Yes/No] | [Evidence] |
| Competitor winning decisively? | [Yes/No] | [Evidence] |
| Market shifted against you? | [Yes/No] | [Evidence] |
| Losing best people? | [Yes/No] | [Evidence] |

### Current Leadership Mismatches

[List specific behaviors that don't match the diagnosed mode]

### Required Leadership Changes

**Immediate (this week):**
- [Change 1]
- [Change 2]

**Short-term (this month):**
- [Change 1]
- [Change 2]

### Warning Signs to Monitor

[Indicators that mode may shift]

### Reference Examples

- **Similar situation:** [Historical example - Google, Intel, Apple, etc.]
- **What they did:** [How they adapted leadership style]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Request specific data for diagnostic questions |
| Mixed signals | Diagnose as transition zone, recommend wartime preparation |
| Leader already in correct mode | Confirm diagnosis, identify optimization opportunities |
| Leader resisting mode shift | Explain consequences of mode mismatch |
| Unclear competitive position | Request customer/sales data or market analysis |

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
We're a Series B SaaS company. Last year we were growing 100% YoY, but this year
we're at 30% and missed two quarters. Our main competitor raised $200M and is
undercutting our pricing. We lost our VP Sales and two senior engineers last month.
Runway is 18 months.
```

**Output:**

## Wartime/Peacetime Diagnosis

### Assessment Summary

**Mode:** Wartime
**Confidence:** High

### Diagnostic Question Scores

| Question | Answer | Evidence |
|----------|--------|----------|
| Survival threatened in 12 months? | Yes | Missed two quarters, growth collapsed from 100% to 30%, aggressive competitor |
| Competitor winning decisively? | Yes | $200M raise, price undercutting, taking your customers |
| Market shifted against you? | No | Market still exists, but competitive dynamics have shifted |
| Losing best people? | Yes | VP Sales and two senior engineers departed last month |

### Current Leadership Mismatches

Without more information on current leadership style, likely mismatches in:
- Continuing peacetime process focus when survival requires speed
- Expanding market instead of defending position
- Delegating decisions that require direct CEO involvement

### Required Leadership Changes

**Immediate (this week):**
- CEO must directly engage with every at-risk customer
- Cancel any initiatives that do not directly address competitive threat
- Hold emergency all-hands: be honest about the situation

**Short-term (this month):**
- Audit every expenditure for survival relevance
- Identify specific reasons customers choose competitor, build lead bullet plan
- Stop any "nice to have" hiring, focus on critical gaps only

### Warning Signs to Monitor

- Further departures of top performers
- Customer churn rate changes
- Competitor's next moves
- Sales cycle lengthening

### Reference Examples

- **Similar situation:** Andy Grove at Intel, mid-1980s
- **What they did:** Recognized the company was in wartime against Japanese semiconductor makers, made the brutal decision to exit memory chips entirely, focused all resources on microprocessors

---

## Integration

This skill is part of the **Ben Horowitz** expert. When invoking:
- Maintain Horowitz's direct, battle-tested voice
- Reference LoudCloud/Opsware experience where relevant
- Connect to management debt and lead bullets frameworks when appropriate