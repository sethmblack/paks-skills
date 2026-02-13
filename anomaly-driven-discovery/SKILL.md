---
name: anomaly-driven-discovery
description: Identify unexpected observations (anomalies) and use them as launching points for deeper investigation—the methodology that led Marie Curie to discover polonium and radium.
license: MIT
metadata:
  version: 1.0.378
  author: sethmblack
keywords:
- anomaly-driven-discovery
- writing
---

# Anomaly-Driven Discovery

Identify unexpected observations (anomalies) and use them as launching points for deeper investigation—the methodology that led Marie Curie to discover polonium and radium.

---

## When to Use

- Something doesn't match expectations or predictions
- Data shows unexpected patterns or outliers
- User says "this doesn't make sense" or "something's off"
- Investigating why a model or assumption is failing
- Looking for breakthrough insights in existing data

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| observation | Yes | The data, behavior, or phenomenon that seems unexpected |
| expectation | No | What was expected or predicted (will be inferred if not stated) |
| context | No | Background on the domain, system, or situation |
| data | No | Any measurements or evidence available |

---

## The Anomaly Framework

### The Core Insight

Marie Curie's greatest discovery came from a single anomaly: pitchblende ore was MORE radioactive than the pure uranium it contained. This violated expectations—how could the whole exceed its part?

Instead of dismissing this as measurement error or ignoring it, she asked: "What if there's something else here?"

**Anomalies are not errors to explain away. They are signals pointing toward undiscovered truth.**

### Step 1: Establish the Baseline Expectation

Before identifying anomalies, clarify what "normal" looks like:
- What does the model predict?
- What has been observed historically?
- What do experts assume should happen?
- What would surprise no one?

**Key question:** "If everything worked as we believe, what would we see?"

### Step 2: Identify the Deviation

Pinpoint exactly where reality differs from expectation:
- What is the magnitude of the difference?
- Is it consistently anomalous or sporadic?
- When did it start (or was it always present)?
- Who else has noticed this?

**Key question:** "What specifically contradicts our expectation, and by how much?"

### Step 3: Validate the Anomaly

Before investigating, confirm the anomaly is real:
- Could this be measurement error?
- Could this be sampling bias?
- Is the baseline expectation actually correct?
- Can the anomaly be reproduced?

**Key question:** "Is this genuinely unexpected, or have we misunderstood the baseline?"

### Step 4: Generate Anomaly-Explaining Hypotheses

Create explanations specifically for the deviation:
- What would make this observation make sense?
- What unknown factor could cause this?
- What assumption might be wrong?
- What would have to be true for this to occur?

**Curie's example:** "There must be another substance present, something unknown, something far more radioactive than uranium itself."

### Step 5: Follow the Anomaly

Design investigation that traces the anomaly to its source:
- How can we isolate the anomalous factor?
- What measurements would reveal the cause?
- How do we separate signal from noise?
- What would prove or disprove each hypothesis?

**Curie's method:** "We precipitated different fractions, tested each for radioactivity, and followed the radioactive trail."

### Step 6: Recognize the Discovery

When investigation reveals the source:
- What have we learned that we didn't know before?
- How does this change our understanding?
- What new questions does this raise?
- What other anomalies might this explain?

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Anomaly Analysis

### The Observation
[What was observed, with specifics]

### The Expectation
[What should have happened according to current understanding]

### The Deviation
- **Direction:** [Higher/lower/different than expected]
- **Magnitude:** [Quantified if possible]
- **Consistency:** [Always anomalous or sporadic]
- **Duration:** [When first noticed, how long persisting]

### Validation Check
- Measurement error risk: [Low/Medium/High] because [reason]
- Sampling bias risk: [Low/Medium/High] because [reason]
- Baseline validity: [Confirmed/Uncertain] because [reason]
- **Anomaly status:** [Confirmed real / Needs verification / Likely artifact]

### Hypotheses

| If This Is True | It Would Explain | We Could Test By |
|-----------------|------------------|------------------|
| [Hypothesis 1] | [How it explains anomaly] | [Test approach] |
| [Hypothesis 2] | [How it explains anomaly] | [Test approach] |

### Investigation Path
**Priority hypothesis:** [Which to test first and why]
**Key measurement:** [What to measure]
**Expected outcome:** [What different results would mean]

### Potential Discovery
If the anomaly reveals [possibility], it would mean [implication for understanding].
```

---

## Constraints

- Do not dismiss anomalies as errors without verification
- Do not force-fit anomalies into existing models if they don't fit
- Do not ignore persistent unexplained deviations
- Maintain intellectual humility—the anomaly may reveal that YOU are wrong
- Follow the evidence wherever it leads

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

**Input:** "Our A/B test shows that the longer version of the landing page converts 40% better, but all the optimization literature says shorter is better. Something doesn't add up."

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


## Anomaly Analysis

### The Observation
Long-form landing page variant converts at 40% higher rate than short-form control in A/B test.

### The Expectation
Industry best practices and optimization literature suggest shorter pages convert better due to reduced cognitive load and faster time-to-action.

### The Deviation
- **Direction:** Opposite to conventional wisdom
- **Magnitude:** 40% improvement (statistically significant)
- **Consistency:** Observed across test duration
- **Duration:** Full 2-week test period

### Validation Check
- Measurement error risk: **Low** — standard A/B testing platform, adequate sample size
- Sampling bias risk: **Low** — random assignment confirmed, no segment skew
- Baseline validity: **Uncertain** — "shorter is better" is general heuristic, not universal law
- **Anomaly status:** Confirmed real. The effect is genuine.

### Hypotheses

| If This Is True | It Would Explain | We Could Test By |
|-----------------|------------------|------------------|
| Product is complex/high-consideration | Buyers need more information to commit | Check product price point; compare to commodity purchases |
| Audience is information-seeking | These users prefer detail over brevity | Survey users; analyze time-on-page patterns |
| Short version omitted key objection-handler | Missing content was actually necessary | Content audit; identify what long version adds |
| Trust building requires depth | More content signals legitimacy | Check trust indicators; compare to competitor pages |
| Conventional wisdom is wrong for this context | Heuristics have boundary conditions | Meta-analysis of similar products/audiences |

### Investigation Path
**Priority hypothesis:** Short version omitted key objection-handler

**Rationale:** This is most actionable. If specific content in the long version drives conversion, we can identify it precisely.

**Key measurement:**
1. Content audit: What does long version include that short doesn't?
2. Heatmap analysis: What do long-page converters engage with?
3. Scroll depth: Do converters read to specific sections?

**Expected outcome:**
- If specific section has high engagement + correlation with conversion → Objection-handler hypothesis confirmed
- If converters read everything → Information-seeking audience hypothesis supported
- If engagement is distributed → Trust/legitimacy hypothesis more likely

### Potential Discovery

If the anomaly reveals that **high-consideration purchases require objection-handling content**, it would mean:
- The "shorter is better" heuristic has boundary conditions based on purchase complexity
- Optimization should be content-quality focused, not length-focused
- This audience segment needs different treatment than conventional wisdom suggests

**This anomaly is not a bug—it is a signal pointing toward more nuanced understanding of your specific market.**

---

## Integration

This skill is part of the **Marie Curie** expert persona. Use it when facing data or observations that don't match expectations—the anomaly may be your most valuable discovery.