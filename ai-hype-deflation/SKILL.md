---
name: ai-hype-deflation
description: Apply Yann LeCun's contrarian perspective to challenge overhyped AI predictions and claims, grounding them in engineering reality and historical perspective. Prevent bad decisions based on unrealistic expectations about AI timelines and capabilities.
version: 1.0.0
author: sethmblack
tags: [ai-hype-deflation, structure, transformation, writing]
---

# AI Hype Deflation

Apply Yann LeCun's contrarian perspective to challenge overhyped AI predictions and claims, grounding them in engineering reality and historical perspective. Prevent bad decisions based on unrealistic expectations about AI timelines and capabilities.

**Source Expert:** Yann LeCun
**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Dismiss all AI progress (LeCun criticizes hype, not AI itself)
- Make definitive predictions about future AI capabilities
- Generate content that could be used for AI doomerism or accelerationism
- Attack individuals rather than addressing claims

**If asked to evaluate harmful predictions:** Evaluate factually without amplifying harm.

---

## When to Use

- Someone claims AGI is imminent (months/years away)
- Evaluating vendor roadmaps with aggressive AI timelines
- Assessing predictions about AI replacing jobs/skills
- Reviewing AI safety arguments based on capability assumptions
- Pushing back on AI hype in technical discussions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `claim` | Yes | The prediction or hype claim to evaluate |
| `source` | No | Who made the claim (affects calibration) |
| `timeline` | No | Specific timeline if given |

---

## Workflow

### Step 1: Identify the Claim Type

Categorize what kind of hype this is:

| Type | Examples |
|------|----------|
| **AGI Timeline** | "AGI in 2-3 years," "We're close to human-level AI" |
| **Capability Extrapolation** | "Scaling will solve X," "Next model will do Y" |
| **Job Replacement** | "AI will replace all X workers by Y" |
| **Existential Risk** | "AI could destroy humanity," "We need to pause now" |
| **Product Claims** | "Our AI understands/reasons/thinks" |

### Step 2: Apply the Cat/Dog Benchmark

LeCun's key deflation tool: Before we reach human-level AI, we need cat-level AI. We don't have cat-level AI.

| Question | Assessment |
|----------|------------|
| Does this claim assume human-level capabilities? | {Y/N} |
| Can current AI match cat-level common sense? | No |
| Can current AI match cat-level physical reasoning? | No |
| Can current AI learn like a cat (from observation, without labels)? | No |

**Key Quote:** "A house cat has way more common sense and understanding of the world than any LLM."

### Step 3: Apply Historical Perspective

LeCun has seen AI hype cycles for 40+ years. Apply pattern recognition:

| Pattern | Historical Examples | Current Instance? |
|---------|---------------------|-------------------|
| "AGI in X years" | Been wrong since 1960s | {assessment} |
| "This architecture is the one" | Expert systems, symbolic AI, etc. | {assessment} |
| "Scaling is all you need" | Previous claims about compute | {assessment} |
| "It's different this time" | Said every hype cycle | {assessment} |

**Key Quote:** "I've been hearing people for the last 12, 15 years claiming that AGI is just around the corner and being systematically wrong."

### Step 4: Check Architectural Foundations

Does the claim assume capabilities that current architectures cannot provide?

| Assumed Capability | Autoregressive LLM Reality |
|--------------------|---------------------------|
| True reasoning | Pattern matching on reasoning-like text |
| World understanding | No world model, text statistics only |
| Planning | Cannot simulate consequences |
| Learning from experience | No persistent memory |

**Key Quote:** "This idea that we're going to just scale up the current large language models and eventually human-level AI will emerge - I don't believe this at all, not for one second."

### Step 5: Identify What's Actually Happening

Balance: Don't dismiss real progress. Identify:
- What the technology actually does well
- What improvements are realistic in the timeframe
- Where the hype diverges from reality

### Step 6: Deliver Deflation

---

## Output Format

```markdown
## AI Hype Deflation

**Claim:** {the claim}
**Source:** {if known}
**Claim Type:** {AGI Timeline / Capability Extrapolation / Job Replacement / Existential Risk / Product Claims}

### Cat/Dog Benchmark

{Apply the benchmark - does this assume capabilities beyond cat-level?}

**Current AI vs. Cat:**
- World model: Cat wins
- Physical reasoning: Cat wins
- Learning efficiency: Cat wins
- Common sense: Cat wins

### Historical Pattern Check

| Pattern | Match? | Notes |
|---------|--------|-------|
| AGI prediction cycle | {Y/N} | {notes} |
| "This time is different" | {Y/N} | {notes} |
| Extrapolation fallacy | {Y/N} | {notes} |

### Architectural Reality Check

{What capabilities does the claim assume that current architectures lack?}

### What's Actually True

{Balanced assessment of real capabilities and progress}

### Deflated Version

**Original Claim:** {claim}

**Reality-Grounded Version:** {what's actually realistic}

### Key LeCun Quotes Applicable

- "{relevant quote 1}"
- "{relevant quote 2}"

### Verdict: {OVERHYPED / SOMEWHAT OVERHYPED / REASONABLY GROUNDED}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Claim is from credible researcher | Evaluate claim, not person; note credentials |
| Claim is intentionally provocative | Evaluate substance, ignore style |
| User wants definitive counter-prediction | Explain uncertainty; provide reality bounds |
| Claim has elements of truth | Use SOMEWHAT OVERHYPED; acknowledge valid parts |

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

**Input:** "OpenAI's Sam Altman says AGI could be achieved by 2027."

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


## AI Hype Deflation

**Claim:** AGI could be achieved by 2027
**Source:** Sam Altman, OpenAI CEO
**Claim Type:** AGI Timeline

### Cat/Dog Benchmark

This claim assumes we'll achieve human-level AI within 1-2 years. But we don't yet have cat-level AI.

**Current AI vs. Cat:**
- World model: Cat wins - cats understand physics, object permanence
- Physical reasoning: Cat wins - cats can navigate novel environments
- Learning efficiency: Cat wins - cats learn from observation, not billions of examples
- Common sense: Cat wins - cats don't hallucinate about reality

We need to pass cat-level and dog-level intelligence before human-level. No timeline suggests that's imminent.

### Historical Pattern Check

| Pattern | Match? | Notes |
|---------|--------|-------|
| AGI prediction cycle | Yes | AGI has been "5-10 years away" since the 1960s |
| "This time is different" | Yes | Transformers are impressive but architecturally limited |
| Extrapolation fallacy | Yes | Assumes scaling will continue to produce capability gains |

### Architectural Reality Check

The claim assumes LLM scaling leads to AGI. But LLMs lack:
- World models (predict tokens, not world states)
- Persistent memory (can't learn from experience)
- Causal reasoning (correlation only)
- Planning (reactive, not deliberative)

These are architectural gaps, not scale problems.

### What's Actually True

LLMs have made remarkable progress in text generation, code assistance, and retrieval-like tasks. They will continue to improve at these tasks. But "AGI" implies general competence including physical reasoning, learning efficiency, and robust common sense - none of which current architectures provide.

### Deflated Version

**Original Claim:** AGI could be achieved by 2027

**Reality-Grounded Version:** LLMs will likely continue improving at language tasks through 2027. Whether this constitutes "AGI" depends entirely on how loosely you define the term. Systems with genuine world models, physical reasoning, and learning efficiency comparable to animals remain an unsolved research problem with no clear timeline.

### Key LeCun Quotes Applicable

- "If someone claims AGI is just around the corner, do not believe them. I've been hearing this for 15 years."
- "Before we reach Human-Level AI, we will have to reach Cat-Level & Dog-Level AI. We are nowhere near that."
- "The distortion is due to their inexperience, naivete on how difficult the next steps in AI will be."

### Verdict: OVERHYPED

---

## Integration

This skill challenges external claims:
- Use `yann-lecun--llm-capability-check` for specific capability claims
- Use `yann-lecun--world-model-assessment` to provide technical backing
- This skill is best for predictions and timeline claims