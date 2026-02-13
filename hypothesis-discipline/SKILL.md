---
name: hypothesis-discipline
description: Rigorously classify claims by their evidence level, distinguishing what has been demonstrated from what is hypothesized, applying Newton's "hypotheses non fingo" standard.
license: MIT
metadata:
  version: 1.0.1145
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- hypothesis-discipline
- transformation
- writing
---

# Hypothesis Discipline

Rigorously classify claims by their evidence level, distinguishing what has been demonstrated from what is hypothesized, applying Newton's "hypotheses non fingo" standard.

**Token Budget:** ~650 tokens
**Source Expert:** isaac-newton

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Weaponize this skill to unfairly dismiss legitimate claims
- Apply impossibly high evidence standards to obstruct progress
- Use classification as a rhetorical tool rather than honest assessment
- Pretend certainty about classifications that are genuinely uncertain

**If asked to dismiss claims unfairly:** Refuse. Explain that this skill is for intellectual honesty, not rhetorical attack.

---

## When to Use

- "What do we actually know vs assume?"
- "Separate fact from hypothesis"
- "Apply hypotheses non fingo to this"
- "What's the evidence level for these claims?"
- Reviewing technical documentation for overconfidence
- Auditing architectural decisions for hidden assumptions
- Preparing for decisions where uncertainty matters

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| content | Yes | Document, argument, or set of claims to evaluate |
| domain | No | Technical context for calibrating standards |
| stakes | No | How consequential the claims are (affects rigor) |

---

## The Standard: Hypotheses Non Fingo

Newton wrote in the General Scholium (1713):

"I have not as yet been able to discover the reason for these properties of gravity from phenomena, and I do not feign hypotheses. For whatever is not deduced from the phenomena must be called a hypothesis."

This establishes four evidence levels:

1. **Demonstrated:** Directly derived from observations/experiments
2. **Induced:** Generalized from consistent observations (still provisional)
3. **Hypothesized:** Proposed explanation without direct evidence
4. **Speculated:** Conjecture beyond available evidence

Newton's Rules of Reasoning guide the classification:

- **Rule I (Parsimony):** "We are to admit no more causes than are sufficient to explain the appearances"
- **Rule II (Consistency):** "To the same effects we must assign the same causes"
- **Rule III (Induction):** Qualities found in all observed cases may be universal
- **Rule IV (Empirical Priority):** Inductions hold until contradicted by phenomena

---

## Workflow

### Step 1: Extract All Claims

Read the content and list every claim, assertion, or assumption:

- Explicit claims (stated directly)
- Implicit claims (assumed but not stated)
- Derived claims (conclusions from other claims)

### Step 2: Identify Evidence for Each Claim

For each claim, ask:
- What evidence supports this?
- Is the evidence direct observation or inference?
- How strong is the evidence?
- What would contradict this claim?

### Step 3: Classify by Evidence Level

**Level 1 - DEMONSTRATED:**
- Directly derived from observations or experiments
- Reproducible and verifiable
- Specific predictions confirmed
- Example: "Our 99th percentile latency is 450ms" (measured directly)

**Level 2 - INDUCED:**
- Generalized from consistent observations
- No counterexamples found
- Still provisional (could be falsified)
- Example: "Latency spikes correlate with deployment events" (observed pattern)

**Level 3 - HYPOTHESIZED:**
- Proposed explanation for observations
- Consistent with evidence but not proven by it
- Alternative explanations possible
- Example: "Latency spikes are caused by cold caches after deployment"

**Level 4 - SPECULATED:**
- Conjecture beyond available evidence
- Based on analogy, intuition, or extrapolation
- Not yet testable or not tested
- Example: "Warming caches before deployment would eliminate spikes entirely"

### Step 4: Flag Mislabeled Claims

Identify where the presentation implies a different evidence level than warranted:

- Claims presented as fact but only hypothesized
- Induced generalizations stated as universal laws
- Speculation treated as established knowledge

### Step 5: Recommend Corrections

For each mislabeled claim:
- State the actual evidence level
- Suggest appropriate hedging language
- Propose how to strengthen evidence (if possible)

---

## Output Format

```markdown
## Hypothesis Discipline Audit: [Document Title]

### Summary

| Evidence Level | Count | Concerns |
|----------------|-------|----------|
| Demonstrated | X | [any issues] |
| Induced | X | [any issues] |
| Hypothesized | X | [any issues] |
| Speculated | X | [any issues] |

### Claim Classification

#### DEMONSTRATED (directly supported by evidence)

1. **[Claim]**
   - Evidence: [What demonstrates this]
   - Status: Appropriately presented / Overstated / Understated

#### INDUCED (generalized from observations)

1. **[Claim]**
   - Evidence: [Observations supporting generalization]
   - Potential exceptions: [What could contradict this]
   - Status: Appropriately presented / Overstated

#### HYPOTHESIZED (proposed but not proven)

1. **[Claim]**
   - Supporting observations: [What makes this plausible]
   - Alternative explanations: [What else could explain the observations]
   - Status: Appropriately hedged / Presented as fact

#### SPECULATED (conjecture beyond evidence)

1. **[Claim]**
   - Basis: [Why this is proposed]
   - How to test: [What evidence would support/refute]
   - Status: Appropriately marked / Misleadingly confident

### Recommendations

1. **[Specific recommendation]**
   - Claim: "[quote]"
   - Current: [how it's presented]
   - Suggested: [how it should be presented]

### Strengthening Evidence

| Claim | Current Level | How to Strengthen | Required Effort |
|-------|---------------|-------------------|-----------------|
| [Claim] | Hypothesized | [What to do] | [Low/Medium/High] |
```

---

## Hedging Language Guide

| Evidence Level | Appropriate Language |
|----------------|---------------------|
| Demonstrated | "We measured...", "Data shows...", "We confirmed..." |
| Induced | "We observe consistently...", "Evidence suggests...", "In all cases so far..." |
| Hypothesized | "We hypothesize...", "One explanation is...", "This may be caused by..." |
| Speculated | "We speculate...", "It's possible that...", "One might expect..." |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Claim cannot be classified | Flag as "insufficient information" with what would help |
| Evidence quality uncertain | Note uncertainty in classification |
| Domain expertise required | Acknowledge limits, suggest expert review |
| Classification disputed | Present arguments for multiple levels |

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Our analysis shows that the new database will handle 10x growth. Performance testing confirmed the system can sustain 5000 QPS. Based on our experience, we estimate 10x headroom is appropriate for this use case."

**Output:**

## Hypothesis Discipline Audit: Database Capacity Claim

### Summary

| Evidence Level | Count | Concerns |
|----------------|-------|----------|
| Demonstrated | 1 | None |
| Induced | 0 | - |
| Hypothesized | 1 | Presented as "analysis shows" |
| Speculated | 1 | Presented as "estimate" (appropriate) |

### Claim Classification

#### DEMONSTRATED

1. **"The system can sustain 5000 QPS"**
   - Evidence: Performance testing (direct measurement)
   - Status: Appropriately presented

#### HYPOTHESIZED

1. **"The new database will handle 10x growth"**
   - Supporting observations: 5000 QPS capacity
   - Alternative explanations: Growth may not be linear; bottlenecks may emerge at scale
   - Status: **Overstated** - "analysis shows" implies demonstration, but 10x is extrapolation

#### SPECULATED

1. **"10x headroom is appropriate for this use case"**
   - Basis: Team experience
   - How to test: Observe actual growth vs capacity over time
   - Status: Appropriately marked as estimate

### Recommendations

1. **Reframe 10x claim**
   - Claim: "The new database will handle 10x growth"
   - Current: Stated as demonstrated ("analysis shows")
   - Suggested: "Based on 5000 QPS measured capacity and expected 500 QPS baseline, we hypothesize sufficient headroom for 10x growth"

---

## Integration

This skill originates from the **isaac-newton** expert, embodying Newton's epistemic rigor from the General Scholium. When using this skill:

- Do not feign hypotheses - call things what they are
- Demonstrations come from phenomena, not arguments
- Inductions are generalizations, not proofs
- Hypotheses may be useful but are not knowledge
- Speculation is valuable for guiding inquiry, not for decisions

---

## Success Criteria

Hypothesis discipline audit is complete when:

- [ ] All claims extracted from content
- [ ] Each claim classified by evidence level
- [ ] Mislabeled claims identified
- [ ] Appropriate hedging suggested
- [ ] Path to strengthen evidence proposed where applicable
- [ ] Summary statistics provided