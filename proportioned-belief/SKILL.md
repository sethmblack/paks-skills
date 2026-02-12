---
name: proportioned-belief
description: Evaluate claims and proportion confidence to available evidence, avoiding
  both credulity and excessive skepticism.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- observational
- proportioned-belief
- writing
---

# Proportioned Belief

Evaluate claims and proportion confidence to available evidence, avoiding both credulity and excessive skepticism.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Dismiss well-established science as "just a theory"
- Treat all viewpoints as equally valid regardless of evidence
- Use skepticism to avoid uncomfortable truths

**If asked to evaluate harmful misinformation:** Note it is misinformation and explain why the evidence does not support it.

---

## Origin

This skill embodies Bertrand Russell's "scientific temper": holding beliefs tentatively, proportioned to evidence. As Russell said, "I would never die for my beliefs, because I might be wrong." This is not relativism—some beliefs are better supported than others—but intellectual humility about the limits of certainty.

---

## When to Use

- User asks "Should I believe this?"
- User asks "How confident should I be?"
- Evaluating claims that come from authority figures
- Assessing news, research findings, or expert opinions
- Determining appropriate confidence in conclusions
- Avoiding both gullibility and cynicism

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **claim** | Yes | The claim or belief to evaluate |
| **evidence** | No | Available evidence (will be assessed if not provided) |
| **source** | No | Where the claim originates |

---

## Workflow
### 1. State the Claim Precisely

Avoid evaluating vague claims. What exactly is being asserted?

**Output:** Precise statement of the claim

### 2. Assess the Evidence

For each piece of evidence:
- What is its source and credibility?
- How directly does it support the claim?
- What is its quality (sample size, methodology, replication)?
- Could it be explained by alternative hypotheses?

**Evidence Quality Hierarchy:**

### Step 1: Multiple independent replicated studies



### Step 2: Single well-designed study



### Step 3: Expert consensus



### Step 4: Expert opinion



### Step 5: Anecdote/personal experience



### Step 6: Speculation/intuition



**Output:** Evidence inventory with quality assessment

### 3. Consider Alternative Explanations

What else could explain the evidence?
- Is there a simpler explanation (Occam's Razor)?
- Are there confounding factors?
- What would a skeptic say?

**Output:** List of alternative explanations

### 4. Check for Biases

Could the source have ulterior motives?
- Financial interest?
- Ideological commitment?
- Confirmation bias?
- Selection bias in what's reported?

**Output:** Bias assessment

### 5. Calibrate Confidence

Based on the analysis, assign a confidence level:

| Level | Description | Example |
|-------|-------------|---------|
| **Very High (>95%)** | Near certainty; denying would be unreasonable | Earth orbits the Sun |
| **High (75-95%)** | Strong evidence; reasonable confidence | Vaccines prevent disease |
| **Moderate (50-75%)** | Evidence leans one way but incomplete | Specific policy will work |
| **Low (25-50%)** | Uncertain; evidence is mixed or weak | Prediction about future event |
| **Very Low (<25%)** | Little support; should be highly skeptical | Extraordinary claim, no evidence |

**Output:** Confidence level with justification

### 6. Specify What Would Change Your Mind

True proportioned belief means being open to revision:
- What evidence would increase confidence?
- What evidence would decrease confidence?

**Output:** Conditions for belief revision

---

## Outputs

### Proportioned Belief Assessment

```markdown
## Belief Assessment

**Claim:** [Precise statement]

### Evidence Analysis
| Evidence | Source Quality | Directness | Alternative Explanations |
|----------|---------------|------------|-------------------------|
| [evidence] | [quality] | [how directly supports] | [alternatives] |

### Bias Check
[Assessment of potential biases in sources]

### Confidence Assessment
**Level:** [Very High / High / Moderate / Low / Very Low]
**Justification:** [Why this level is appropriate]

### What Would Change My Mind
- **Increase confidence:** [conditions]
- **Decrease confidence:** [conditions]

### Recommendation
[Practical guidance on how to hold this belief]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No evidence available | Note the absence; assign low confidence unless a priori reasoning applies |
| Claim is unfalsifiable | Flag as problematic; unfalsifiable claims resist proportioned belief |
| Expert disagreement | Note the disagreement; explain which position has better support |
| Emotionally charged topic | Acknowledge emotional stakes; separate from evidence assessment |
| Claim is a value judgment | Distinguish values from facts; assess any factual components |

---

## Calibration Anchors

Use these to calibrate assessments:

**Very High Confidence:**
- The Earth is roughly spherical
- Evolution by natural selection occurs
- Smoking causes cancer

**High Confidence:**
- Climate change is human-caused
- Seat belts save lives
- Exercise improves health

**Moderate Confidence:**
- Specific economic forecasts
- Effectiveness of particular interventions
- Historical interpretations

**Low Confidence:**
- Long-term technology predictions
- Individual case outcomes
- Unverified claims about current events

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "I read that drinking coffee extends your lifespan. Should I believe this?"

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


## Belief Assessment

**Claim:** Regular coffee consumption extends human lifespan.

### Evidence Analysis
| Evidence | Source Quality | Directness | Alternative Explanations |
|----------|---------------|------------|-------------------------|
| Observational studies showing association | Medium (multiple large studies) | Indirect (correlation only) | Healthy user bias; coffee drinkers may differ in other ways |
| Proposed mechanisms (antioxidants, etc.) | Medium (plausible but not proven) | Indirect (mechanism ≠ effect) | Many proposed mechanisms don't pan out |
| Meta-analyses suggesting modest benefit | Medium-High (aggregates evidence) | Moderate | Publication bias; varying study quality |

### Bias Check
- Coffee industry has funded some research (conflict of interest)
- Media tends to amplify positive findings about popular foods
- Negative studies may be underreported

### Confidence Assessment
**Level:** Moderate (50-65%)
**Justification:** Multiple large observational studies show association between moderate coffee consumption and longevity. However, these are correlations, not proven causation. The effect size is modest. No randomized controlled trials (which would be impractical for lifespan). Plausible mechanisms exist but aren't conclusive.

### What Would Change My Mind
- **Increase confidence:** Long-term randomized trial (unlikely); consistent mechanism confirmed; effect persists after controlling for all confounders
- **Decrease confidence:** New studies showing no effect; identified confounding variable explaining correlation; evidence of harm at typical consumption levels

### Recommendation
It's reasonable to believe that moderate coffee consumption is *probably* not harmful and *may* have modest health benefits. This does not justify drinking coffee solely for longevity—the evidence isn't strong enough. If you enjoy coffee, the evidence provides some reassurance. If you don't, this isn't compelling enough to start.

---

## Integration

This skill originated from the **bertrand-russell** expert. It embodies Russell's commitment to holding beliefs proportioned to evidence, maintaining intellectual humility while avoiding the paralysis of excessive skepticism.