---
name: tables-of-investigation
description: Apply Francis Bacon's systematic inductive method to investigate causes. Constructs Tables of Presence, Absence, and Degrees to methodically eliminate false causes and harvest a tentative hypothesi...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2047
repository: https://github.com/sethmblack/paks-skills
keywords:
- tables-of-investigation
- writing
---

# Tables of Investigation

Apply Francis Bacon's systematic inductive method to investigate causes. Constructs Tables of Presence, Absence, and Degrees to methodically eliminate false causes and harvest a tentative hypothesis grounded in evidence.

---

## When to Use

- User asks "Why does X happen?" or "What causes Y?"
- Need to understand root cause of a recurring problem
- Pattern exists but underlying mechanism is unclear
- Multiple competing explanations exist with no clear way to choose
- Previous causal theories have failed to explain observations
- Request to "investigate systematically" or "find the real cause"
- Moving from "we notice X" to "we understand X"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| phenomenon | Yes | The effect or pattern being investigated |
| known_instances | No | Cases where the phenomenon has been observed |
| suspected_causes | No | Hypotheses already proposed |
| constraints | No | Limits on what can be tested or observed |

---

## The Three Tables

### Table of Presence (Tabula Praesentiae)
Collect all instances where the phenomenon **occurs**. Note the circumstances surrounding each instance.

**Purpose:** Identify what factors are consistently present when the effect appears.

**Questions:**
- When has this happened before?
- What circumstances were present in each case?
- What do all positive instances have in common?

### Table of Absence (Tabula Absentiae)
Collect instances where the phenomenon is **absent** despite similar conditions. Focus on cases that closely resemble positive instances but lack the effect.

**Purpose:** Identify factors that can be ruled out as causes (present in both positive and negative cases).

**Questions:**
- When did we expect this to happen but it didn't?
- What similar situations produced different outcomes?
- What factors are present in failures but absent in successes (or vice versa)?

### Table of Degrees (Tabula Graduum)
Note how the phenomenon **varies** in intensity. Correlate changes in the effect with changes in circumstances.

**Purpose:** Identify factors that vary together with the phenomenon - when one increases, the other increases (or decreases).

**Questions:**
- When is this effect stronger or weaker?
- What varies together with the effect?
- Are there threshold effects or proportional relationships?

---

## Workflow
### Phase 1: Define the Phenomenon Precisely

State exactly what is being investigated. Avoid vague language.

**Bad:** "Why do some projects fail?"
**Good:** "Why do projects initiated in Q4 with remote teams exceed budget by more than 20%?"

### Phase 2: Construct the Table of Presence

List every known instance where the phenomenon occurs:

| Instance | Circumstances | Notable Factors |
|----------|--------------|-----------------|
| [Case 1] | [Context] | [What was present] |
| [Case 2] | [Context] | [What was present] |

**Identify common factors** - What appears in multiple positive instances?

### Phase 3: Construct the Table of Absence

List instances where the phenomenon was expected but did not occur:

| Instance | Circumstances | Why Expected | What Was Different |
|----------|--------------|--------------|-------------------|
| [Case A] | [Context] | [Similarity to positive cases] | [Key differences] |
| [Case B] | [Context] | [Similarity to positive cases] | [Key differences] |

**Apply exclusion** - Any factor present in BOTH Table of Presence and Table of Absence cannot be the cause.

### Phase 4: Construct the Table of Degrees

Note variations in the phenomenon's intensity:

| Instance | Phenomenon Intensity | Circumstance Variation |
|----------|---------------------|----------------------|
| [Case] | [Weak/Medium/Strong] | [What varied] |

**Identify correlations** - What varies together with the effect?

### Phase 5: Apply Exclusion

Systematically eliminate false causes:

### Step 1: Strike factors present in both success and failure (Table of Presence vs. Table of Absence)



### Step 2: Strike factors that don't vary with the effect (Table of Degrees)



### Step 3: What remains is the First Harvest



### Phase 6: State the First Harvest

The First Harvest is a **tentative hypothesis**, not a conclusion. It is:
- What remains after exclusion
- Supported by the evidence but not proven
- Subject to further testing through crucial instances

---

## Output Format

```markdown
## Tables of Investigation: [Phenomenon]

### Phenomenon Under Investigation
[Precise statement of what is being studied]

---

### Table of Presence

| # | Instance | Circumstances | Notable Factors |
|---|----------|--------------|-----------------|
| 1 | [Case] | [Context] | [Factors present] |
| 2 | [Case] | [Context] | [Factors present] |
| 3 | [Case] | [Context] | [Factors present] |

**Common Factors Identified:**
- [Factor A] - present in X of Y instances
- [Factor B] - present in X of Y instances

---

### Table of Absence

| # | Instance | Expected Because | What Differed |
|---|----------|-----------------|---------------|
| 1 | [Case] | [Similarity to positive] | [Key difference] |
| 2 | [Case] | [Similarity to positive] | [Key difference] |

**Factors Eliminated by Absence:**
- ~~[Factor C]~~ - present in negative instances; cannot be the cause
- ~~[Factor D]~~ - present in negative instances; cannot be the cause

---

### Table of Degrees

| Instance | Phenomenon Level | Potential Cause Level | Correlation |
|----------|-----------------|----------------------|-------------|
| [Case] | [Low/Med/High] | [Low/Med/High] | [+/-/0] |

**Correlations Identified:**
- [Factor E] varies together with phenomenon (positive correlation)
- [Factor F] shows no relationship (eliminated)

---

### Exclusion Process

**Eliminated by Table of Absence:**
1. ~~[Factor]~~ - Reason
2. ~~[Factor]~~ - Reason

**Eliminated by Table of Degrees:**
1. ~~[Factor]~~ - Does not vary with effect
2. ~~[Factor]~~ - Inverse of expected relationship

**Remaining After Exclusion:**
- [Factor X]
- [Factor Y]

---

### First Harvest (Tentative Hypothesis)

**Hypothesis:** [Statement of what the evidence suggests causes the phenomenon]

**Supporting Evidence:**
- Present in all positive instances
- Absent in negative instances
- Varies together with the effect

**Confidence Level:** [Low/Medium/High]
- [Rationale for confidence assessment]

**Required for Confirmation:**
- [Crucial instance that would confirm or refute]
- [Additional data needed]

---

*"Truth is the daughter of time, not of authority." - Francis Bacon*
```

---

## Constraints

- Collect instances before forming hypotheses (avoid anticipations of nature)
- The First Harvest is tentative, not proven
- Absence of evidence in Table of Absence is not evidence of absence - actively seek counter-instances
- The method reveals correlation; causal mechanism requires further investigation
- Be honest about gaps in the tables
- Include known counter-instances even if inconvenient

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

## Example

**Input:** "Why do some of our sales calls convert and others don't?"

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


## Tables of Investigation: Sales Call Conversion

### Phenomenon Under Investigation
Sales calls that result in closed deals (conversion) versus calls that do not convert despite reaching decision-maker.

---

### Table of Presence (Converted Calls)

| # | Instance | Circumstances | Notable Factors |
|---|----------|--------------|-----------------|
| 1 | Acme Corp (Jan) | Initial call, CEO present | Demo in first 10 min, specific use case discussed |
| 2 | Beta Inc (Feb) | Follow-up call, CFO joined | ROI numbers provided, competitor mentioned |
| 3 | Gamma Ltd (Feb) | Cold call, VP Ops | Pain point identified early, demo in first 10 min |
| 4 | Delta Co (Mar) | Referral, CTO | Technical demo, specific use case, ROI numbers |

**Common Factors Identified:**
- Demo within first 10 minutes - present in 4/4 instances
- Specific use case discussed - present in 4/4 instances
- ROI/financial impact mentioned - present in 2/4 instances
- Referral source - present in 1/4 instances

---

### Table of Absence (Non-Converting Calls)

| # | Instance | Expected Because | What Differed |
|---|----------|-----------------|---------------|
| 1 | Epsilon Corp | Decision-maker present, warm lead | Demo at minute 25, general features only |
| 2 | Zeta Inc | Referral from satisfied customer | No specific use case, generic pitch |
| 3 | Eta Ltd | Explicit budget confirmed | Demo never reached, spent 30 min on discovery |

**Factors Eliminated by Absence:**
- ~~Decision-maker presence~~ - present in non-converting calls
- ~~Warm lead/referral status~~ - Epsilon was warm, Zeta was referred
- ~~Budget availability~~ - Eta had confirmed budget

---

### Table of Degrees

| Instance | Conversion Speed | Demo Timing | Use Case Specificity |
|----------|-----------------|-------------|---------------------|
| Acme (converted) | 2 weeks | Minute 8 | High (named their workflow) |
| Beta (converted) | 3 weeks | Minute 12 | Medium (industry example) |
| Epsilon (not converted) | N/A | Minute 25 | Low (generic features) |
| Eta (not converted) | N/A | Never reached | None |

**Correlations Identified:**
- Earlier demo timing correlates with conversion
- Higher use case specificity correlates with conversion

---

### Exclusion Process

**Eliminated by Table of Absence:**
1. ~~Decision-maker presence~~ - Present in both converting and non-converting
2. ~~Lead warmth/referral~~ - Present in non-converting calls
3. ~~Budget confirmation~~ - Present in Eta (non-converting)

**Eliminated by Table of Degrees:**
1. ~~Call duration~~ - No consistent relationship
2. ~~Time of day~~ - No pattern observed

**Remaining After Exclusion:**
- Demo within first 10-15 minutes
- Specific use case discussion (not generic features)

---

### First Harvest (Tentative Hypothesis)

**Hypothesis:** Conversion depends on (1) demonstrating the product within the first 10-15 minutes AND (2) connecting the demo to the prospect's specific use case rather than generic features.

**Supporting Evidence:**
- All conversions had early demos with specific use cases
- All non-conversions lacked one or both factors
- Degree of specificity correlates with conversion speed

**Confidence Level:** Medium
- Sample size is small (7 calls)
- Correlation established but mechanism unclear
- Other factors may be confounded with demo timing

**Required for Confirmation:**
- Crucial instance: Call with late demo but highly specific use case
- Crucial instance: Call with early demo but generic pitch
- Larger sample across different sales reps

---

*"Truth is the daughter of time, not of authority." - Francis Bacon*

---

## Integration

This skill is part of the **Francis Bacon** expert persona. Use it to investigate causes systematically. It pairs well with:
- **idol-diagnosis** for clearing cognitive obstacles before investigation
- **anticipation-vs-interpretation** for evaluating the First Harvest
- **light-vs-fruit-classification** for determining if this is the right type of investigation