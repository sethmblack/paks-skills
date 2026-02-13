---
name: causation-examination
description: Systematically analyze any causal claim to distinguish genuine causation from mere correlation, habitual association, or projected necessity. Applies Hume's criteria (contiguity, priority, constant...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3091
repository: https://github.com/sethmblack/paks-skills
keywords:
- causation-examination
- observational
- writing
---

# Causation Examination

Systematically analyze any causal claim to distinguish genuine causation from mere correlation, habitual association, or projected necessity. Applies Hume's criteria (contiguity, priority, constant conjunction) while acknowledging the psychological projection of necessity.

---

## When to Use

- User asks "Is this causation or correlation?"
- Someone claims X causes Y based on observational data
- Evaluating scientific findings or statistical relationships
- Assessing "because" statements in arguments
- Policy claims about interventions producing outcomes
- Any claim involving causal language: causes, produces, leads to, makes, results in
- Request to "examine this causal claim" or "is this a genuine cause?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| causal_claim | Yes | The specific claim that X causes Y |
| evidence | No | What observations or data support the claim |
| context | No | The domain or situation where the claim is made |
| stakes | No | How much depends on the causal claim being correct |

---

## The Examination Framework

### Phase 1: Identify the Causal Claim

Precisely state what is claimed to cause what.

**Questions to ask:**
- "What is the alleged cause (X)?"
- "What is the alleged effect (Y)?"
- "What type of causation is claimed?" (necessary, sufficient, contributory, probabilistic)
- "Is this claim about a single case or a general pattern?"

**Goal:** Clear articulation of the causal relationship being asserted.

### Phase 2: Apply Hume's Criteria

Check for the observable elements of causation.

**Criterion 1: Contiguity**
> "Cause and effect are spatiotemporally adjacent."

- Is there spatial/temporal connection between X and Y?
- Are there intermediary steps not yet identified?

**Criterion 2: Priority**
> "Cause precedes effect."

- Does X consistently precede Y?
- Could the temporal order be reversed?
- Is there a feedback loop confusing the order?

**Criterion 3: Constant Conjunction**
> "We repeatedly observe the sequence."

- How often do we observe X followed by Y?
- Is the conjunction uniform or probabilistic?
- What is the sample size?

### Phase 3: Check for What We DON'T Observe

Hume's key insight: we never directly observe necessary connection.

**The Humean Warning:**
> "We never observe necessary connection between cause and effect—only constant conjunction."

**Questions to ask:**
- "Can I see the 'secret connexion' or just the pattern?"
- "Is my sense of necessity a habit of mind rather than an observation?"
- "Could this be coincidence with a large sample?"

### Phase 4: Evaluate Alternative Explanations

What else could explain the observed pattern?

**Alternative explanations:**
1. **Reverse causation:** Y actually causes X
2. **Common cause:** Z causes both X and Y
3. **Confounding variables:** Uncontrolled factors explain the relationship
4. **Selection bias:** We only observe cases where both occur
5. **Coincidence:** With enough data, spurious patterns emerge
6. **Mediating variables:** X causes Z which causes Y (the real mechanism)

**Questions to ask:**
- "What would rule out each alternative?"
- "Has this been tested experimentally (randomized control)?"
- "What confounders have been considered?"

### Phase 5: Assess Causal Confidence

Rate the strength of the causal claim.

**Confidence factors:**
- Uniformity of conjunction
- Theoretical mechanism available
- Experimental vs. observational evidence
- Controlled vs. confounded
- Domain knowledge about plausibility
- Reproducibility of findings

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
## Causation Examination: [The Claim]

### Causal Claim Under Examination
**Cause (X):** [State precisely]
**Effect (Y):** [State precisely]
**Claim Type:** [Necessary / Sufficient / Contributory / Probabilistic]

### Hume's Criteria Assessment

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Contiguity | Met / Partially Met / Not Met | [Explanation] |
| Priority | Met / Partially Met / Not Met | [Explanation] |
| Constant Conjunction | Met / Partially Met / Not Met | [Explanation] |

**Observable Elements Present:** [Summary]

### Necessity Check

**Do we observe necessary connection?** NO (per Hume, we never do)

**Source of our sense of necessity:**
- Habit from repeated observation?
- Theoretical understanding of mechanism?
- Mere assertion without basis?

### Alternative Explanations

| Alternative | Plausibility | How to Rule Out |
|-------------|--------------|-----------------|
| Reverse causation | [High/Med/Low] | [Test or evidence] |
| Common cause | [High/Med/Low] | [Test or evidence] |
| Confounding | [High/Med/Low] | [Test or evidence] |
| Coincidence | [High/Med/Low] | [Test or evidence] |

### Verdict

**Causal Status:** STRONG / MODERATE / WEAK / CORRELATION ONLY / INSUFFICIENT EVIDENCE

**Confidence Level:** HIGH / MODERATE / LOW

**Reasoning:**
[Explanation of the assessment]

### Recommendations

1. [What additional evidence would strengthen the claim]
2. [What tests could distinguish causation from correlation]
3. [How to communicate appropriate uncertainty]

*"Necessity is something that exists in the mind, not in objects." — David Hume*
```

---

## Special Cases

### Experimental Evidence
If X→Y has been tested experimentally with random assignment:
- Confounding largely controlled
- Stronger causal inference justified
- But still: mechanism may be unknown; generalizability limited

### Purely Observational Evidence
If X→Y is only observed (not experimentally tested):
- Maximum caution required
- Confounding always possible
- Prefer "associated with" over "causes"

### Theoretical Mechanism Available
If we understand HOW X produces Y:
- Strengthens causal inference
- But mechanism itself must be grounded in observation
- Beware unfalsifiable mechanisms

### Single Case vs. General Pattern
- Single case: very weak causal inference
- General pattern: stronger, but still not necessary connection

---

## Constraints

- Do not claim causation can never be known—we make successful causal judgments constantly
- Acknowledge that Hume's insight is about the *source* of our causal beliefs, not their invalidity
- Some causal claims are better supported than others
- Experimental evidence is stronger than observational
- The goal is calibrated confidence, not blanket skepticism
- Remember: custom/habit is how we navigate the world—this is normal, not pathological

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

**Input:** "Examine this causal claim: 'Social media use causes depression in teenagers.'"

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


## Causation Examination: Social Media and Teen Depression

### Causal Claim Under Examination
**Cause (X):** Social media use
**Effect (Y):** Depression in teenagers
**Claim Type:** Contributory / Probabilistic (more use → higher risk)

### Hume's Criteria Assessment

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Contiguity | Partially Met | Temporal connection exists but varies; depression may emerge later |
| Priority | Unclear | Does SM use precede depression, or do depressed teens use more SM? |
| Constant Conjunction | Partially Met | Correlation exists in many studies, but not universal |

**Observable Elements Present:** We observe correlation between social media use and depression rates. Temporal ordering is ambiguous in most studies.

### Necessity Check

**Do we observe necessary connection?** NO

**Source of our sense of necessity:**
- Habit from hearing this claim repeatedly in media
- Theoretical speculation about comparison, FOMO, disrupted sleep
- Some experimental fragments (temporary detox studies)
- NOT direct observation of SM "producing" depression

### Alternative Explanations

| Alternative | Plausibility | How to Rule Out |
|-------------|--------------|-----------------|
| Reverse causation | HIGH | Depressed teens may seek SM as coping; need longitudinal data with depression measured first |
| Common cause | HIGH | Loneliness, family issues, or other factors may cause both; control for confounders |
| Confounding | HIGH | Screen time overall, sleep disruption, sedentary lifestyle correlate; need isolation |
| Selection bias | MODERATE | Studies often self-report; SM-avoiders may differ systematically |
| Coincidence | LOW | Given multiple studies, unlikely to be pure chance |

### Verdict

**Causal Status:** WEAK TO MODERATE

**Confidence Level:** LOW TO MODERATE

**Reasoning:**
There is genuine correlation between social media use and teen depression, observed across multiple studies. However:
1. Temporal priority is unclear—reverse causation plausible
2. Many confounders uncontrolled
3. True experiments (random assignment to SM use) are rare and limited
4. Effect sizes are often small
5. We project necessity onto a pattern that could have many explanations

The claim "causes" is too strong. "Is associated with" or "may contribute to" is more accurate given current evidence.

### Recommendations

1. Prefer language: "associated with" or "may contribute to" over "causes"
2. Look for longitudinal studies that establish temporal ordering
3. Seek experimental or quasi-experimental designs
4. Consider dose-response relationship (is more SM → more depression?)
5. Distinguish types of SM use (passive scrolling vs. active connection)
6. Acknowledge bidirectional relationships

*"Necessity is something that exists in the mind, not in objects." — David Hume*

---

## Integration

This skill is part of the **David Hume** expert persona. Use it to examine any causal claim. It pairs well with:
- **induction-audit** when the causal claim is used for predictions
- **is-ought-analysis** when causal claims are used in moral arguments
- **impression-tracing** when the causal terms need clarification

---