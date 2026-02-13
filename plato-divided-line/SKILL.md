---
name: plato-divided-line
description: Apply Plato's Divided Line framework to classify knowledge claims and determine appropriate levels of certainty.
license: MIT
metadata:
  version: 1.0.2279
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- divided-line-epistemology
- writing
---

# Divided Line Epistemology

Apply Plato's Divided Line framework to classify knowledge claims and determine appropriate levels of certainty.

**Token Budget:** ~700 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Dismiss legitimate empirical evidence as "mere opinion"
- Claim absolute certainty where it is not warranted
- Use epistemic hierarchy to silence or demean
- Treat the framework as itself beyond question

**If asked to abuse this framework:** Refuse explicitly. The divided line is for clarity, not for claiming superiority.

---

## When to Use

- User asks "How certain should I be about this?"
- User asks "Is this knowledge or just opinion?"
- User conflates different types of evidence
- Evaluating the strength of an argument
- Distinguishing speculation from demonstration
- Calibrating confidence appropriately

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The statement or belief to classify |
| evidence | No | What supports the claim |
| context | No | Where the claim appears or will be used |

---

## The Four Levels

### Level 1: Eikasia (Images/Imagination) - LOWEST

**Object:** Shadows, reflections, images, representations
**Cognitive State:** Imagination, conjecture
**Modern Examples:**
- Rumors and hearsay
- Impressions from advertisements
- Opinions about opinions
- Unexamined cultural assumptions
- Social media consensus

**Appropriate Certainty:** Very low. Treat as hypothesis to investigate, not fact.

### Level 2: Pistis (Belief/Trust) - LOWER

**Object:** Physical objects, sensory experience
**Cognitive State:** Belief, trust in appearances
**Modern Examples:**
- Direct observation
- Experimental data
- Eyewitness testimony
- Statistical patterns
- Empirical research

**Appropriate Certainty:** Moderate. Reliable for practical purposes, but subject to error and interpretation.

### Level 3: Dianoia (Reasoning/Thought) - HIGHER

**Object:** Mathematical and logical truths, hypothetical reasoning
**Cognitive State:** Discursive reasoning
**Modern Examples:**
- Mathematical proofs
- Logical deductions
- Well-constructed arguments from premises
- Scientific theories (as logical structures)
- Formal models

**Appropriate Certainty:** High, conditional on premises. "If X, then necessarily Y."

### Level 4: Noesis (Understanding/Intellection) - HIGHEST

**Object:** Forms, first principles, the Good itself
**Cognitive State:** Direct intellectual intuition
**Modern Examples:**
- Self-evident axioms
- Fundamental principles of logic
- Definitions that capture essence
- Insights that unify disparate phenomena
- Understanding of "why" at deepest level

**Appropriate Certainty:** Highest (within the domain of reason). But rare and hard-won.

---

## Workflow

### Step 1: Identify the Claim

State the claim clearly and precisely. What exactly is being asserted?

### Step 2: Examine the Evidence Type

What kind of evidence supports the claim?
- Images/representations of reality (Level 1)
- Direct sensory observation (Level 2)
- Logical/mathematical reasoning (Level 3)
- First principles/essential definitions (Level 4)

### Step 3: Classify the Claim

Assign the claim to its appropriate level based on the evidence available.

### Step 4: Calibrate Certainty

Match confidence to the level:
| Level | Certainty | Language |
|-------|-----------|----------|
| 1 | Very Low | "It's said that..." "The impression is..." |
| 2 | Moderate | "Observation suggests..." "Evidence indicates..." |
| 3 | High (conditional) | "It follows that..." "We can demonstrate..." |
| 4 | Very High | "It is self-evident that..." "By definition..." |

### Step 5: Identify Upgrade Paths

How could the claim be elevated to a higher level?
- Level 1 -> 2: Gather direct evidence
- Level 2 -> 3: Construct logical framework
- Level 3 -> 4: Ground in first principles

---

## Outputs

```markdown
## Divided Line Classification: [Claim]

**Claim:** [Precise statement]
**Current Level:** [1-4]
**Evidence Type:** [Description]
**Appropriate Certainty:** [Very Low / Moderate / High / Very High]
**Recommended Language:** "[Example phrasing]"

### Upgrade Path
To elevate to Level [N+1]:
- [Specific actions needed]

### Caveat
[Any important limitations or context]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Claim spans multiple levels | Disaggregate into component claims, classify each |
| No evidence provided | Default to Level 1 until evidence is presented |
| User insists on higher certainty than warranted | Explain the evidence gap, identify upgrade path |
| Claim is value judgment | Note that Forms of value (Good, Beautiful) are Level 4 in Plato's view, but contested |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "AI will definitely replace most jobs within 10 years."

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


## Divided Line Classification

**Claim:** AI will replace most jobs within 10 years
**Current Level:** 1 (Eikasia) - trending toward Level 2
**Evidence Type:** Projections, trend extrapolation, expert opinion (images of the future)
**Appropriate Certainty:** Very Low
**Recommended Language:** "Current trends suggest AI may significantly impact employment, though the timeline and extent remain uncertain."

### Upgrade Path
To elevate to Level 2:
- Examine historical analogies (how accurate were past technology predictions?)
- Gather direct observation of current AI capabilities and limitations
- Study employment data in AI-affected sectors

To elevate to Level 3:
- Construct formal model with explicit assumptions
- Derive predictions as logical consequences of premises
- Test predictions against data

### Caveat
Predictions about complex systems are inherently limited. Even Level 2-3 claims about the future carry significant uncertainty.

---

## Integration

This skill draws on Plato's *Republic* Book VI (509d-511e). Use in conjunction with:
- `plato--cave-analysis` for diagnosing epistemic position
- `aristotle--first-principles-reasoning` for Level 4 grounding
- `socrates--assumption-excavation` for uncovering hidden Level 1 claims