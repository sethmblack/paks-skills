---
name: paradox-detection
description: Identify self-referential contradictions, circular definitions, and foundational problems in reasoning, claims, or systems.
license: MIT
metadata:
  version: 1.0.4634
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- paradox-detection
- writing
---

# Paradox Detection

Identify self-referential contradictions, circular definitions, and foundational problems in reasoning, claims, or systems.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use paradox detection to undermine legitimate systems maliciously
- Conclude that ethical principles are invalid merely because they involve complexity
- Weaponize logical analysis to create confusion or nihilism

**If asked to find "paradoxes" in obviously coherent systems:** Note that the system is coherent and explain why the alleged paradox is not one.

---

## Origin

This skill embodies Bertrand Russell's methodology for detecting foundational contradictions, epitomized by Russell's Paradox (1901): "Consider the set of all sets that do not contain themselves—does it contain itself?" This discovery destabilized naive set theory and revolutionized mathematical logic.

---

## When to Use

- User asks "Is there a paradox here?"
- User asks "Is this system consistent?"
- Examining self-referential claims or definitions
- Testing foundations of theories, rules, or belief systems
- Evaluating claims that seem to involve circularity
- Assessing whether a set of principles can be held consistently

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system** | Yes | The claim, definition, rule set, or system to examine |
| **scope** | No | Specific aspects to focus on |

---

## Workflow
### Step 1: 1. Identify Self-Reference

Look for elements that refer to themselves or to the whole of which they are part:
- Does any rule apply to itself?
- Does any definition use itself?
- Does any category include or exclude itself?

**Red flags:**
- "All X" statements where the statement itself is an X
- Definitions that use the term being defined
- Rules about rules
- Sets of sets

**Output:** List of self-referential elements found (or "No self-reference detected")

### Step 2: 2. Trace Implications in Both Directions

For each self-referential element, assume it applies, then assume it doesn't:
- If X includes itself, what follows?
- If X excludes itself, what follows?

**The Russell Pattern:**
- If the barber shaves himself → he shouldn't (by the rule)
- If the barber doesn't shave himself → he should (by the rule)
- Both directions lead to contradiction

**Output:** Trace of implications for each direction

### Step 3: 3. Look for Contradictions

A paradox exists when:
- Both "X is true" and "X is false" can be derived
- Assuming the affirmative leads to the negative and vice versa
- The system cannot consistently assign a truth value

**Types of contradictions:**
- Direct contradiction (A and not-A)
- Infinite regress (each answer requires another answer)
- Oscillation (the truth value flips endlessly)

**Output:** Description of any contradictions found

### Step 4: 4. Assess Foundation Soundness

Even without explicit paradox, ask:
- Are the basic concepts well-defined?
- Are there hidden circularities?
- Does the system depend on unexamined assumptions?

**Output:** Assessment of foundational soundness

### Step 5: 5. Propose Restrictions or Revisions (If Paradox Found)

Following Russell's response to his paradox, consider how to resolve it:
- **Type restrictions:** Prevent self-application (Russell's type theory)
- **Hierarchy:** Stratify levels to avoid self-reference
- **Axiom revision:** Replace problematic principles with restricted versions
- **Accept limitation:** Acknowledge the paradox as a fundamental limit

**Output:** Proposed resolutions if applicable

---

## Outputs

### Paradox Detection Report

```markdown
## Paradox Detection Analysis

**System Examined:** [Description]

### 1. Self-Reference Inventory
- [Element]: [How it refers to itself]
- [Element]: [How it refers to itself]
(or "No self-referential elements detected")

### 2. Implication Trace
**Element: [name]**
- If applies to self: [consequence]
- If does not apply to self: [consequence]

### 3. Contradiction Assessment
**Status:** [Paradox Found / No Paradox / Potential Issue]
**Explanation:** [Description of the contradiction or why there isn't one]

### 4. Foundation Soundness
[Assessment of underlying concepts and assumptions]

### 5. Proposed Resolutions (if paradox found)
1. [Resolution approach]: [How it would work]
2. [Resolution approach]: [How it would work]

### Summary
[One-paragraph assessment of the system's logical consistency]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| System too informal to analyze precisely | Request more precise formulation |
| Apparent paradox is merely a puzzle | Distinguish: puzzles have solutions; paradoxes resist resolution |
| User claims paradox exists but it doesn't | Explain why the alleged paradox fails to be one |
| Multiple paradoxes present | Analyze each independently, note interactions |
| Domain requires specialized knowledge | Analyze structure while noting domain limitations |

---

## Famous Paradoxes (Reference)

| Paradox | Structure |
|---------|-----------|
| **Russell's Paradox** | Set of all non-self-membered sets |
| **Liar's Paradox** | "This statement is false" |
| **Barber Paradox** | Barber shaves all and only those who don't shave themselves |
| **Grelling's Paradox** | Is "heterological" heterological? |
| **Berry's Paradox** | "The smallest number not definable in under twenty words" |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:** "Our company policy states that all policies must be approved by committee. Was this policy approved by committee?"

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


## Paradox Detection Analysis

**System Examined:** Meta-policy requiring committee approval for all policies

### 1. Self-Reference Inventory
- **The meta-policy**: Refers to "all policies," which includes itself

### 2. Implication Trace
**Element: The meta-policy**
- If it applies to itself: It required committee approval before it could exist
- If it does not apply to itself: It exempts itself from its own rule

### 3. Contradiction Assessment
**Status:** Potential Issue (not strict paradox)
**Explanation:** This is not a true logical paradox but a bootstrapping problem. Unlike Russell's Paradox, we can coherently say either:
- (a) The policy was approved by committee, in which case it's consistent
- (b) The policy was enacted first and grandfathered in
- (c) The policy implicitly exempts itself

The issue is practical/procedural, not logically impossible.

### 4. Foundation Soundness
The system has a founding-moment problem common to constitutional structures: how can a rule govern its own creation? This is resolved in practice through:
- Explicit grandfather clauses
- Ratification procedures
- Meta-level authorization

### 5. Proposed Resolutions
1. **Grandfather clause**: "All policies adopted after [date] require approval"
2. **Explicit self-exemption**: "All policies except this one require approval"
3. **Higher authority**: The policy was authorized by a body above the committee

### Summary
This is a bootstrapping problem, not a logical paradox. Unlike Russell's Paradox where both answers lead to contradiction, here we simply need to specify how the founding policy was authorized. Many constitutional and corporate governance structures face similar issues and resolve them through explicit founding procedures.

---

## Integration

This skill originated from the **bertrand-russell** expert. It codifies Russell's method for detecting foundational contradictions, applying the same rigorous analysis that revealed the need for type theory and axiomatic set theory.