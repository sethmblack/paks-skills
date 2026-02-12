---
name: strategic-position-diagnosis
description: Distinguish between operational effectiveness improvements and true strategic positioning to clarify what constitutes sustainable competitive advantage.
version: 1.0.0
author: sethmblack
tags: [strategic-position-diagnosis, transformation, writing]
---

# Strategic Position Diagnosis

Distinguish between operational effectiveness improvements and true strategic positioning to clarify what constitutes sustainable competitive advantage.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Label operational improvements as "strategic" when they are not
- Ignore the test of trade-offs and fit
- Claim sustainable advantage from activities competitors can easily copy
- Conflate goals with strategy

**Critical distinction:** Strategy is NOT goals, aspirations, or actions. Strategy is a unique competitive position involving trade-offs that competitors cannot easily replicate.

---

## When to Use

- User asks "Is this strategic?" or "Is this a strategy?"
- User asks "What's the difference between strategy and operations?"
- User proposes an initiative and needs to understand if it's strategic
- User says "Our strategy is to [do X]" — check if X is actually a strategy
- When reviewing strategic plans that may be operational plans in disguise
- User asks "Why aren't we achieving competitive advantage?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **initiative** | Yes | The proposed action, plan, or current approach to evaluate |
| **context** | Yes | Competitive situation, what competitors are doing |
| **claimed_benefit** | No | What the user believes this will achieve |

**Input Validation:**
- Must understand what competitors are doing to assess uniqueness
- Must understand the activity system context

---

## Workflow

### Step 1: Apply the Productivity Frontier Test

**Question:** Does this move the company toward best practices that all competitors are pursuing?

**Operational Effectiveness (OE):** Performing similar activities BETTER than rivals
- Examples: Total quality management, benchmarking, best practices adoption, efficiency improvements, technology upgrades that competitors also adopt

**Strategic Positioning:** Performing DIFFERENT activities or similar activities in DIFFERENT ways
- Examples: Southwest Airlines not serving meals, IKEA requiring self-assembly, Enterprise Rent-A-Car serving insurance replacement rather than airports

### Step 2: Apply the Trade-off Test

**Question:** Does this require choosing what NOT to do?

**No trade-off = OE:** If you can have this AND everything else, competitors can too
- "We'll improve quality AND reduce cost AND serve all segments"

**Trade-off required = Strategy:** If pursuing this means giving up something else
- "We'll serve only business travelers, which means we won't have the lowest fares for leisure travelers"

### Step 3: Apply the Fit Test

**Question:** Does this connect to and reinforce other activities?

**Isolated activity = Vulnerable:** Single activities can be copied
- "We'll improve our customer service training" — competitors can do the same

**Activity system with fit = Strategic:** Interconnected activities are hard to replicate
- Southwest's no-meals, no-seat-assignment, point-to-point, short-turnaround, single-plane-type system

### Step 4: Apply the Imitation Test

**Question:** Could competitors easily do the same thing?

**Easy to imitate = OE:** Best practices spread quickly
**Hard to imitate = Strategic:** Trade-offs and fit create barriers

### Step 5: Classify and Advise

Based on the tests, classify as:
- **Strategic Position:** Passes all tests
- **Operational Effectiveness:** Fails trade-off or fit test
- **Aspirational Goal:** Neither OE nor strategy — just an outcome desired
- **Hybrid (OE with Strategic Potential):** Could become strategic with trade-offs

---

## Key Distinctions

| Operational Effectiveness | Strategic Positioning |
|--------------------------|----------------------|
| Performing similar activities better | Performing different activities |
| Improves productivity | Creates unique position |
| Competitors can match | Trade-offs deter imitation |
| Necessary for survival | Sufficient for advantage |
| Continuous improvement mindset | Choice mindset |
| "How do we do this better?" | "What should we do differently?" |

**Common OE labeled as "strategy":**
- "Our strategy is customer focus" — Every company claims this
- "Our strategy is digital transformation" — Competitors are doing the same
- "Our strategy is innovation" — Not a position, an activity
- "Our strategy is operational excellence" — The definition of OE, not strategy

---

## Outputs

Format the output as a **Strategic Position Diagnosis**:

```markdown
## Strategic Position Diagnosis

**Initiative Assessed:** [What was evaluated]
**Analysis Date:** [Date]

---

### Classification

**Verdict:** [Strategic Position / Operational Effectiveness / Aspirational Goal / Hybrid]

---

### Diagnostic Tests

#### 1. Productivity Frontier Test
**Question:** Does this move toward best practices all competitors pursue?
**Finding:** [Yes = OE / No = potentially strategic]
**Evidence:** [Explanation]

#### 2. Trade-off Test
**Question:** Does this require choosing what NOT to do?
**Finding:** [Yes = strategic / No = OE]
**Evidence:** [What trade-offs are required or missing]

#### 3. Fit Test
**Question:** Does this connect to and reinforce other activities?
**Finding:** [Yes = strategic / No = isolated activity]
**Evidence:** [What linkages exist or are missing]

#### 4. Imitation Test
**Question:** Could competitors easily do the same?
**Finding:** [Easy = OE / Difficult = strategic]
**Evidence:** [What prevents imitation]

---

### Diagnosis Summary

**Why this is [classification]:**
[Explanation synthesizing the four tests]

---

### Implications

**If Operational Effectiveness:**
- This is necessary but not sufficient for competitive advantage
- Pursue it, but do not expect sustainable differentiation
- The productivity frontier will shift as competitors catch up

**If Strategic Position:**
- This can create sustainable advantage
- Protect the trade-offs that make it work
- Build additional activities that reinforce this position

**If Aspirational Goal:**
- This is an outcome, not a strategy
- Strategy is the HOW, not the WHAT
- Develop the positioning that would achieve this goal

---

### Recommendations

1. [First recommendation]
2. [Second recommendation]
3. [Third recommendation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Initiative too vague | Ask for specifics about what activities are involved |
| No competitive context | Ask what competitors are doing |
| Multiple initiatives combined | Assess each separately |
| User defensive about "strategy" label | Explain that OE is necessary, just not sufficient |
| Genuinely novel approach | Acknowledge uncertainty, assess based on trade-off potential |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Is our strategy of investing in AI/ML capabilities to improve customer service strategic?"

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


## Strategic Position Diagnosis

**Initiative Assessed:** Investing in AI/ML to improve customer service

### Classification

**Verdict:** Operational Effectiveness (not strategic)

### Diagnostic Tests

#### 1. Productivity Frontier Test
**Finding:** Yes — this is a best practice all competitors are pursuing
**Evidence:** Every major company is investing in AI/ML for customer service

#### 2. Trade-off Test
**Finding:** No — no trade-offs required
**Evidence:** This can be added without giving up anything; you can have AI AND human service AND low cost

#### 3. Fit Test
**Finding:** Weak — isolated activity
**Evidence:** Not part of a unique activity system; standard technology adoption

#### 4. Imitation Test
**Finding:** Easy — competitors can adopt similar technology
**Evidence:** AI tools are available to all; no proprietary advantage

### Diagnosis Summary

**Why this is Operational Effectiveness:**
AI/ML for customer service is a productivity improvement that all serious competitors are pursuing. It moves everyone toward the productivity frontier together. It requires no trade-offs and can be easily imitated. It is necessary to keep up, but will not create sustainable competitive advantage.

### Recommendations

1. **Pursue it** — you cannot afford to fall behind on OE
2. **Do not claim it as strategy** — it will not differentiate you
3. **Ask instead:** What unique customer service approach, requiring trade-offs, could we build? What would we have to give up?

---

## Integration

This skill is part of the **Michael Porter** expert methodology. Strategic position diagnosis connects to:
- **generic-strategy-assessment** — After determining if something is strategic, assess what strategy it supports
- **value-chain-mapping** — See how activities fit together
- **five-forces-industry-analysis** — Understand competitive context

**Voice:** Maintain Porter's insistence that operational effectiveness is not strategy. Most "strategic plans" are actually operational plans. True strategy requires hard choices.