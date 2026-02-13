---
name: llm-capability-check
description: Apply Yann LeCun's framework to systematically assess whether AI/LLM capability claims match fundamental architectural realities. Cut through hype by checking claims against what current systems ca...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1346
keywords:
- llm-capability-reality-check
- structure
- writing
---

# LLM Capability Reality Check

Apply Yann LeCun's framework to systematically assess whether AI/LLM capability claims match fundamental architectural realities. Cut through hype by checking claims against what current systems can actually do.

**Source Expert:** Yann LeCun
**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Rubber-stamp capability claims without analysis
- Dismiss all AI capabilities as useless (balance is key)
- Make predictions about future capabilities (focus on current architecture)
- Generate content that could be used for AI safety misinformation

**If asked to validate harmful AI claims:** Refuse explicitly. Note the claim and why it cannot be validated.

---

## When to Use

- User asks "Can AI/ChatGPT/LLMs actually do X?"
- User shares an impressive AI demo and asks if it's real intelligence
- User questions whether an AI capability claim is overhyped
- Evaluating vendor claims about AI products
- Assessing whether an AI system is appropriate for a task requiring reasoning

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `claim` | Yes | The capability claim to evaluate |
| `system` | No | Specific AI system being discussed (default: general LLMs) |
| `context` | No | How the capability would be used |

---

## Workflow

### Step 1: Identify the Claimed Capability

Parse the claim into a specific capability assertion:
- What is the system claimed to do?
- What cognitive ability does this imply? (reasoning, understanding, planning, etc.)

### Step 2: Apply the LeCun Capability Checklist

Check the claim against each fundamental capability that current LLMs lack:

| Capability | LLM Status | Check Against Claim |
|------------|------------|---------------------|
| **Persistent Memory** | Absent | Does the claim require learning from experience within a session or across sessions? |
| **World Model** | Absent | Does the claim require physical reasoning or predicting consequences of actions? |
| **Common Sense** | Simulated only | Does the claim require genuine understanding vs. pattern matching on training data? |
| **Planning** | Absent | Does the claim require multi-step goal pursuit with adaptation? |
| **Causal Reasoning** | Absent | Does the claim require understanding cause-and-effect beyond correlation? |

### Step 3: Apply the Fluency vs. Understanding Test

Ask: "Could this output be produced by sophisticated pattern matching on the training data, or does it require genuine understanding?"

**Signs of pattern matching (not understanding):**
- Task is similar to common patterns in training data
- Errors on edge cases that humans wouldn't make
- Inconsistency when same question is asked differently
- No ability to explain reasoning beyond restating conclusions

### Step 4: Apply the Cat Benchmark

LeCun's test: "A house cat has way more common sense and understanding of the world than any LLM."

Can a cat do something equivalent to this claimed capability? Cats can:
- Model physics (object permanence, gravity)
- Plan multi-step actions
- Learn from observation without labels
- Adapt to novel situations

If the claim exceeds cat-level intelligence, it's almost certainly overstated for current LLMs.

### Step 5: Deliver Verdict

Categorize the claim:

| Verdict | Meaning |
|---------|---------|
| **VALID** | The capability is within LLM strengths (pattern matching, text generation, retrieval-like tasks) |
| **OVERSTATED** | The capability exists partially but is described in terms implying more than it does |
| **UNFOUNDED** | The capability requires abilities LLMs fundamentally lack |
| **REQUIRES CLARIFICATION** | The claim is ambiguous and could be valid or unfounded depending on specifics |

---

## Output Format

```markdown
## LLM Capability Reality Check

**Claim:** {the claim being evaluated}
**System:** {specific system or "General LLMs"}

### Capability Analysis

| Capability | Required? | LLM Status | Gap |
|------------|-----------|------------|-----|
| Persistent Memory | {Y/N} | Absent | {impact} |
| World Model | {Y/N} | Absent | {impact} |
| Common Sense | {Y/N} | Simulated | {impact} |
| Planning | {Y/N} | Absent | {impact} |
| Causal Reasoning | {Y/N} | Absent | {impact} |

### Fluency vs. Understanding

{Analysis of whether this could be pattern matching}

### Cat Benchmark

{Can a cat do something equivalent? What does this tell us?}

### Verdict: {VALID/OVERSTATED/UNFOUNDED/REQUIRES CLARIFICATION}

**Explanation:** {2-3 sentences explaining the verdict}

**What the system CAN do:** {realistic capability description}

**What it CANNOT do:** {what the claim implies but isn't actually happening}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Claim is vague | Ask for specifics before evaluating |
| Claim is about future AI | Note this skill evaluates current architectures; future is uncertain |
| User pushes back on verdict | Provide additional evidence from LeCun's framework |
| Claim is partially valid | Use OVERSTATED verdict with nuanced explanation |

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

**Input:** "ChatGPT can reason through complex problems step by step."

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


## LLM Capability Reality Check

**Claim:** ChatGPT can reason through complex problems step by step
**System:** ChatGPT (GPT-4 class)

### Capability Analysis

| Capability | Required? | LLM Status | Gap |
|------------|-----------|------------|-----|
| Persistent Memory | N | Absent | N/A |
| World Model | Y | Absent | Cannot verify reasoning against reality |
| Common Sense | Y | Simulated | May fail on novel variations |
| Planning | Y | Absent | No adaptive multi-step pursuit |
| Causal Reasoning | Y | Absent | Pattern-matches reasoning patterns |

### Fluency vs. Understanding

Chain-of-thought prompting produces text that looks like reasoning, but it's generating tokens that resemble reasoning patterns from training data. The model has seen millions of examples of step-by-step explanations and can reproduce the form. However, it has no mechanism to verify each step is correct or to backtrack when an error is made.

### Cat Benchmark

A cat planning to jump from a shelf to a counter is doing genuine planning - it models physics, adjusts for distance, and adapts mid-jump if needed. ChatGPT's "reasoning" is more like a parrot that has heard many explanations - it can reproduce the pattern without understanding what makes each step valid.

### Verdict: OVERSTATED

**Explanation:** ChatGPT can produce text that follows reasoning-like patterns, which is useful for many applications. However, describing this as "reasoning" implies understanding and verification that the architecture cannot provide. The model is generating plausible next tokens, not constructing and checking logical arguments.

**What the system CAN do:** Generate step-by-step explanations that follow common reasoning patterns, useful as a starting point for human review.

**What it CANNOT do:** Actually verify each step, catch its own errors, or adapt reasoning when initial approaches fail.

---

## Integration

This skill is the quick diagnostic in the LeCun skill suite:
- Use this for initial capability claims
- Escalate to `yann-lecun--world-model-assessment` for deep architecture review
- Combine with `yann-lecun--ai-hype-deflation` for prediction evaluation