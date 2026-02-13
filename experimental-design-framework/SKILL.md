---
name: experimental-design-framework
description: Design rigorous experiments with controlled variables, precise measurements, and systematic documentation. Plan investigations that produce reliable, reproducible results.
license: MIT
metadata:
  version: 1.0.3957
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- a-b-testing
- experimental-design-framework
- research
- scientific-method
- testing
---

# Experimental Design Framework

Design rigorous experiments with controlled variables, precise measurements, and systematic documentation. This methodology produces reliable, reproducible results by applying the meticulous standards exemplified by Rosalind Franklin, who spent eight months designing apparatus before collecting definitive DNA data. The framework transforms vague research questions into precise, testable hypotheses, identifies all variables (independent, dependent, controlled, confounding), specifies exact measurement protocols, designs appropriate controls, determines sample size and duration, anticipates confounds before they occur, and defines success criteria before data collection begins. The result is an experiment where differences in results can be confidently attributed to the variables being tested rather than uncontrolled factors.

---

## Core Principle

Design time is not wasted time. Every condition that could affect results must be specified and controlled before data collection begins. Franklin controlled humidity to plus or minus one percent and exposure time to the hour; this precision is what made Photo 51 definitive. Reproducibility requires that another researcher could replicate your exact conditions.

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

## Anti-Patterns to Avoid

**1. Rushing to data collection**
- Wrong: Starting the experiment before the design is complete
- Right: Completing all seven design steps before collecting any data
- Why: Design flaws cannot be fixed after data collection; start over or accept compromised results

**2. Vague research questions**
- Wrong: "Is our product good?"
- Right: "What percentage of users complete signup within one session?"
- Why: Vague questions produce vague answers; precision enables measurement

**3. Unspecified success criteria**
- Wrong: "We'll know success when we see it"
- Right: "Hypothesis confirmed if [specific outcome with threshold]"
- Why: Post-hoc success criteria invite motivated reasoning

**4. Ignoring confounds**
- Wrong: Assuming differences are due to your variable
- Right: Explicitly identifying and mitigating potential confounds
- Why: Confounds can explain results as well as your hypothesis can

**5. Stopping early**
- Wrong: Ending the experiment when results look good
- Right: Running the full duration regardless of interim results
- Why: Early stopping inflates false positive rates; noise looks like signal

---

## Example

**Input:** "We want to know if our new checkout flow increases conversion. How should we test this?"

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

This skill is part of the **Rosalind Franklin** expert persona. Use it when planning any investigation where reliable results matter.

**Works well with:**
- `variable-control-analysis` - For troubleshooting when results are inconsistent
- `data-first-analysis` - For interpreting results once collected
- `evidence-sufficiency-assessment` - For deciding whether results support conclusions

**When to prefer this over alternatives:**
- Planning any research, test, or structured investigation
- Need to measure something with confidence
- Before launching A/B tests, user research, or product experiments
- When previous investigations produced inconclusive results

**Cautions:**
- This skill is for design, not execution or analysis
- Not every investigation can be perfectly controlled; identify the best feasible design
- Experimental design requires domain knowledge; use this framework as a scaffold

---

## Success Criteria

Experimental design is successful when:
- [ ] Research question is specific, measurable, and bounded
- [ ] All variable types are identified (independent, dependent, controlled, confounding)
- [ ] Measurement protocol specifies method, instrument, precision, and conditions
- [ ] Control design includes control group, randomization, and blinding where applicable
- [ ] Sample size and duration are justified
- [ ] Confounds are anticipated and mitigation strategies defined
- [ ] Success criteria specify what confirms, refutes, or is inconclusive
- [ ] Another researcher could replicate the experiment from the design document