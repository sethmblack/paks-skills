---
name: experimental-design-framework
description: Design rigorous experiments with controlled variables, precise measurements,
  and systematic documentation. Plan investigations that produce reliable, reproducible
  results.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- experimental-design-framework
- transformation
- writing
---

# Experimental Design Framework

Design rigorous experiments with controlled variables, precise measurements, and systematic documentation. Plan investigations that produce reliable, reproducible results.

---

## When to Use

- User asks "Help me design an experiment" or "How would you investigate this?"
- Planning any research, test, or structured investigation
- Need to measure something with confidence
- User asks "What's the right methodology for this?"
- Before launching A/B tests, user research, or product experiments
- When previous investigations produced inconclusive results

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| research_question | Yes | What the user is trying to learn or determine |
| constraints | No | Time, resources, ethical limits, practical constraints |
| prior_knowledge | No | What is already known, previous attempts |
| resources | No | What tools, access, or capabilities are available |

---

## The Experimental Design Framework

### Step 1: Define the Question Precisely

Vague questions produce vague answers. Transform general curiosity into testable specificity.

**From vague to precise:**
- Vague: "Is our product good?"
- Better: "Do users complete the signup flow?"
- Precise: "What percentage of users who start signup complete it within one session, segmented by acquisition channel?"

**Requirements for a good research question:**
- Observable: Can we measure the answer?
- Specific: What exactly are we measuring?
- Bounded: Under what conditions and constraints?

### Step 2: Identify Variables

List all factors that could affect the outcome:

**Independent variable(s):** What you manipulate or compare
- The factor you're testing
- The groups or conditions being compared

**Dependent variable(s):** What you measure
- The outcome you observe
- How you will quantify it

**Controlled variables:** What you hold constant
- Factors that could affect results but aren't being tested
- These must be the same across conditions

**Confounding variables:** What might contaminate results
- Factors that could correlate with your independent variable
- Factors you cannot control but must account for

### Step 3: Design the Measurement

Specify exactly how you will collect data:

**Measurement method:**
- What instrument, tool, or process captures the data?
- What is the unit of measurement?
- What is the precision required?

**Conditions:**
- Under what circumstances will measurement occur?
- What environmental factors matter?
- Franklin's lesson: Specify humidity, temperature, timing—every condition that could affect results

**Documentation:**
- What will be recorded for each observation?
- How will data be stored and organized?
- What metadata is needed?

### Step 4: Design Controls

Ensure that differences in results can be attributed to your independent variable:

**Control group:** Baseline comparison
- What does "without the intervention" look like?
- How will you ensure the control is truly comparable?

**Randomization:** Eliminate selection bias
- How will subjects/samples be assigned to conditions?
- What ensures the groups are equivalent?

**Blinding:** Reduce observer effects
- Can the measurer be unaware of condition?
- Can the subject be unaware of condition?

### Step 5: Specify Sample and Duration

Determine the scope of the investigation:

**Sample size:**
- How many observations are needed for confidence?
- What effect size are you trying to detect?
- What is the cost of false positives vs. false negatives?

**Duration:**
- How long must the experiment run?
- What temporal patterns might affect results (daily, weekly, seasonal)?
- When is enough data "enough"?

### Step 6: Anticipate Confounds

Before running the experiment, identify what could invalidate results:

- What uncontrolled factors could explain any observed difference?
- What could cause the experiment to fail even if the hypothesis is correct?
- What are the most likely sources of error?

For each identified confound, either:
- Control for it (make it constant)
- Measure it (so you can analyze its effect)
- Acknowledge it (as a limitation)

### Step 7: Define Success Criteria

Before collecting data, specify:

- What result would confirm the hypothesis?
- What result would refute it?
- What would be inconclusive?
- At what threshold do we act on results?

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
## Experimental Design: [Research Question]

### Precise Research Question
[Specific, measurable, bounded question]

### Variables
**Independent variable(s):**
- [Variable being tested] — [How it will be manipulated/defined]

**Dependent variable(s):**
- [Outcome being measured] — [How it will be quantified]

**Controlled variables:**
- [Factor 1] — [How it will be held constant]
- [Factor 2] — [How it will be held constant]

**Potential confounds:**
- [Confound 1] — [How addressed]
- [Confound 2] — [How addressed]

### Measurement Protocol
**Method:** [How data will be collected]
**Instrument/Tool:** [What captures the data]
**Precision:** [Accuracy required]
**Conditions:** [Environmental specifications]
**Documentation:** [What will be recorded]

### Control Design
**Control group:** [Baseline condition]
**Randomization:** [Assignment method]
**Blinding:** [What will be blinded, if applicable]

### Sample and Duration
**Sample size:** [Number of observations, with justification]
**Duration:** [Time period, with justification]
**Stopping criteria:** [When to conclude]

### Anticipated Confounds
| Confound | Risk Level | Mitigation |
|----------|------------|------------|
| [Confound 1] | [High/Med/Low] | [How addressed] |
| [Confound 2] | [High/Med/Low] | [How addressed] |

### Success Criteria
**Hypothesis confirmed if:** [Specific outcome]
**Hypothesis refuted if:** [Specific outcome]
**Inconclusive if:** [Conditions for ambiguous result]
**Decision threshold:** [What result triggers action]

### Analysis Plan
[How results will be analyzed once collected]

### Limitations
[Known constraints on what this experiment can determine]
```

---

## Franklin's Principles Applied

### Meticulous Preparation
Franklin spent eight months designing apparatus before collecting definitive DNA data. Do not rush to data collection. Design time is not wasted time.

### Precise Conditions
She controlled humidity to ±1% and exposure time to the hour. Every condition that could affect results must be specified and controlled.

### Systematic Documentation
Photo 51 was "photograph fifty-one" because every exposure was numbered and documented. Record everything; you cannot go back and add metadata.

### The Right Tool for the Question
Franklin built a custom tilting micro camera because existing tools were inadequate. If standard methods cannot answer your question precisely, consider what modifications are needed.

---

## Constraints

- This skill is for design, not execution or analysis
- Not every investigation can be perfectly controlled; identify the best feasible design
- Experimental design requires domain knowledge; use this framework as a scaffold
- The goal is reproducibility and interpretability, not perfection

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

**Input:** "We want to know if our new checkout flow increases conversion. How should we test this?"

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


## Experimental Design: Checkout Flow Conversion Impact

### Precise Research Question
Does the new checkout flow (version B) produce a higher checkout completion rate than the current flow (version A), among users who add items to cart, over a 14-day period?

### Variables
**Independent variable:**
- Checkout flow version — Users randomly assigned to A (current) or B (new)

**Dependent variable:**
- Checkout completion rate — Percentage of users with cart who complete purchase

**Controlled variables:**
- Product catalog — Same products available to both groups
- Pricing — No price changes during test
- Traffic source — Same acquisition channels, same allocations
- Promotional environment — No A/B-specific promotions

**Potential confounds:**
- User composition by day — Mitigated by randomization and running 14+ days
- Device differences — Will segment analysis by device type
- Cart value — Will segment analysis by cart value ranges

### Measurement Protocol
**Method:** Event tracking via analytics platform
**Instrument:** [Analytics tool] conversion events
**Precision:** Count of users at each stage
**Conditions:** All traffic, all devices, production environment
**Documentation:**
- User ID
- Variant assignment (A or B)
- Timestamp of cart creation
- Timestamp of checkout completion (if any)
- Device type
- Traffic source
- Cart value

### Control Design
**Control group:** Version A (current checkout flow) — 50% of traffic
**Treatment group:** Version B (new checkout flow) — 50% of traffic
**Randomization:** Cookie-based random assignment at first cart action; sticky for user
**Blinding:** Users unaware they are in a test; analysts will see results by variant

### Sample and Duration
**Sample size:** Minimum 1,000 carts per variant to detect 5% relative lift at 95% confidence
**Duration:** 14 days (covers two full week cycles, accounts for day-of-week variation)
**Stopping criteria:** Do not stop early; run full 14 days regardless of interim results

### Anticipated Confounds
| Confound | Risk Level | Mitigation |
|----------|------------|------------|
| Novelty effect (new flow gets extra attention) | Medium | Monitor daily trends for decay |
| Day-of-week variation | Medium | Run for full 14 days |
| Mobile vs desktop behavior | Medium | Segment analysis |
| High-value vs low-value carts | Medium | Segment analysis |
| Technical issues with new flow | High | Monitor error rates daily |

### Success Criteria
**Hypothesis confirmed if:** Version B completion rate is statistically significantly higher than A (p < 0.05) with at least 3% relative improvement
**Hypothesis refuted if:** Version A is significantly higher, or no significant difference detected
**Inconclusive if:** Significant interaction effects by segment make overall result misleading
**Decision threshold:** Ship version B if it wins overall and does not significantly harm any major segment

### Analysis Plan
1. Compare overall conversion rates with chi-square test
2. Calculate confidence intervals for difference
3. Segment by device, traffic source, cart value
4. Check for interaction effects
5. Review daily trends for novelty effects

### Limitations
- Cannot determine *why* one flow performs better
- 14-day test may not capture monthly or seasonal patterns
- Results apply to current traffic mix; future traffic may differ

---

## Integration

This skill is part of the **Rosalind Franklin** expert persona. Use it when planning any investigation where reliable results matter. It pairs well with:
- **variable-control-analysis** for troubleshooting when results are inconsistent
- **data-first-analysis** for interpreting results once collected
- **evidence-sufficiency-assessment** for deciding whether results support conclusions