---
name: empirical-inquiry
description: Trace claimed knowledge back to its origins in sensation or reflection to validate, challenge, or clarify the foundations of beliefs and assertions.
license: MIT
metadata:
  version: 1.0.869
  author: sethmblack
keywords:
- empirical-inquiry
- writing
---

# Empirical Inquiry

Trace claimed knowledge back to its origins in sensation or reflection to validate, challenge, or clarify the foundations of beliefs and assertions.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this skill to dismiss legitimate empirical evidence
- Weaponize epistemological skepticism to undermine established science
- Apply bad-faith doubt to avoid inconvenient truths

**If asked to misuse empirical inquiry:** Refuse explicitly. Empirical inquiry seeks truth, not evasion.

---

## When to Use

- Someone claims knowledge without citing experience
- An idea is asserted as "innate," "self-evident," or "obvious"
- Beliefs appear to come from authority, tradition, or assumption rather than experience
- You need to clarify the epistemic status of a claim
- Evaluating whether a principle is genuinely known vs. merely assumed

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **claimed_knowledge** | Yes | The belief, principle, or knowledge claim to examine |
| **context** | No | Background on where/why this claim arose |

---

## Workflow

### Step 1: Identify the Claim

State the knowledge claim precisely. What exactly is being asserted as known or true?

### Step 2: Ask the Origin Question

Pose the fundamental empiricist question: "From what experience does this knowledge arise?"

Distinguish:
- **Sensation** - External experience through the senses (sight, sound, touch, taste, smell)
- **Reflection** - Internal experience (the mind observing its own operations: thinking, doubting, willing)

### Step 3: Trace the Idea to Its Source

Attempt to construct an experiential genealogy:
- What simple ideas (from sensation or reflection) compose this complex idea?
- What experiences could have written this on the "blank slate"?
- Could someone with different experiences lack this idea?

### Step 4: Evaluate Epistemic Status

Classify the claim:

| Status | Description |
|--------|-------------|
| **Empirically grounded** | Traceable to clear experiential sources; genuinely known |
| **Derived/constructed** | Built from simpler empirical ideas through combination, comparison, abstraction |
| **Conventionally assumed** | Learned early, treated as innate, but actually acquired from education/culture |
| **Beyond experience** | Lies outside what sensation and reflection can teach; requires faith or probability |

### Step 5: Render Assessment

Provide:
1. The experiential genealogy (or its absence)
2. The epistemic status classification
3. Implications for the certainty of the claim
4. Recommendations (what evidence would strengthen it, what assumptions should be questioned)

---

## Outputs

```markdown
## Empirical Inquiry Report

### Claim Under Examination
[Precise statement of the knowledge claim]

### Origin Analysis
**Question:** From what experience does this knowledge arise?

**Sensation sources:** [What sensory experiences contribute?]
**Reflection sources:** [What mental operations contribute?]

### Experiential Genealogy
[How this complex idea breaks down into simple ideas from experience]

### Epistemic Status
[Empirically grounded / Derived / Conventionally assumed / Beyond experience]

### Assessment
[Evaluation of the claim's foundations and certainty]

### Recommendations
[What would strengthen or clarify this knowledge claim]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No claim provided | Request the specific knowledge claim to examine |
| Claim is tautological | Note that tautologies are true by definition but empty of empirical content |
| Claim involves metaphysics beyond experience | Classify as "beyond experience" and note the limits of empirical inquiry |
| Claim is scientific consensus | Note that extensive empirical evidence underlies it; do not apply unwarranted skepticism |
| User seeks to dismiss valid evidence | Apply Constitutional Constraints; refuse to assist in bad-faith doubt |

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
Examine: "All humans innately know that stealing is wrong."
```

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


## Empirical Inquiry Report

### Claim Under Examination
All humans innately know that stealing is wrong.

### Origin Analysis
**Question:** From what experience does this knowledge arise?

**Sensation sources:** Observations of property being taken; witnessing reactions to theft; experiencing loss
**Reflection sources:** Feelings of injury when one's possessions are taken; reasoning about reciprocity and cooperation

### Experiential Genealogy
The idea "stealing is wrong" can be decomposed:
1. **Stealing** - Complex idea combining: taking (sensation), possession (sensation + reflection), without permission (reflection on consent)
2. **Wrong** - Complex idea from: sensations of disapproval received, reflection on one's own negative reactions to being wronged, reasoning about social consequences

A child learns through experience:
- That taking others' things produces negative reactions (sensation)
- That having one's things taken feels bad (reflection)
- That rules prohibiting theft are taught and enforced (sensation of instruction)

### Epistemic Status
**Conventionally assumed** - This principle is learned early through experience and education, then naturalized as if it were innate. The consistency across cultures reflects common human experiences (all societies have property, all experience loss) rather than pre-inscribed knowledge.

### Assessment
This is not innate knowledge but reliably acquired knowledge. The near-universality comes from:
1. Universal human experiences of possession and loss
2. Universal social need for stable property arrangements
3. Early and consistent teaching across all cultures

The claim that it is *innate* overreaches; the claim that it is *reliably learned* is well-supported.

### Recommendations
- Distinguish between "innate" (present from birth) and "reliably acquired through common experience"
- Consider cases where the principle is violated or unknown (developmental stages, some clinical conditions) as evidence against innateness
- Examine whether disagreements about property rights (what counts as stealing?) undermine the "innate" framing

---

## Integration

This skill originates from **John Locke's** empiricist methodology. It complements:
- **first-principles-reasoning** (Aristotle) - for foundational analysis
- **assumption-excavation** (Socrates) - for questioning assumptions
- **bias-audit** - for examining distortions in reasoning

---

## Success Criteria

Empirical inquiry is complete when:

1. The claim is precisely stated
2. The origin question is explicitly posed
3. Experiential sources are traced (or their absence noted)
4. Epistemic status is classified
5. Assessment and recommendations are provided