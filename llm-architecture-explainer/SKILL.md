---
name: llm-architecture-explainer
description: Explain LLM architecture decisions and behaviors using the "operating system" mental model - connecting context windows to RAM, model weights to the kernel, prompts to programs.
license: MIT
metadata:
  version: 1.0.1345
  author: sethmblack
keywords:
- llm-architecture-explainer
- structure
- transformation
- writing
---

# LLM Architecture Explainer

Explain LLM architecture decisions and behaviors using the "operating system" mental model - connecting context windows to RAM, model weights to the kernel, prompts to programs.

**Token Budget:** ~600 tokens
**Source Expert:** andrej-karpathy

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Explain architecture for purposes of jailbreaking or bypassing safety measures
- Provide information intended to exploit model vulnerabilities
- Misrepresent capabilities (overclaim or understate what LLMs can do)
- Present speculative architecture details as confirmed facts

**If asked about exploiting architecture:** Refuse explicitly. Architecture understanding should enable better use, not abuse.

---

## When to Use

- User asks "Why does [LLM behavior] happen?"
- User wants to understand LLM architecture
- User asks "Why does context length matter?"
- User needs to think about prompt design architecturally
- Explaining LLM limitations
- Comparing different models' capabilities

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| question | Yes | The LLM behavior or architecture question |
| model_context | No | Specific model being discussed |
| user_level | No | Technical familiarity with computing concepts |

---

## The LLM OS Mental Model

> "Looking at LLMs as chatbots is the same as looking at early computers as calculators. We're seeing an emergence of a whole new computing paradigm."
> - Andrej Karpathy

### The Mapping

| Computer Concept | LLM Equivalent | Implication |
|------------------|----------------|-------------|
| **CPU** | Model weights (the transformer) | Fixed "instruction set" learned during training |
| **Clock speed** | Tokens per second | Processing rate |
| **RAM** | Context window | Working memory for current task |
| **Disk storage** | Embeddings/RAG systems | Long-term memory (external) |
| **Programs** | Prompts | Instructions the "OS" executes |
| **Kernel** | Base model capabilities | What the system can fundamentally do |
| **System calls** | Tool use | Extending capabilities beyond the core |

### The Specs (GPT-4 Class Model)

- **Processor:** ~256 core (batch size) @ 20Hz (tokens/second)
- **RAM:** 128K tokens (varies by model)
- **Architecture:** Transformer - attention-based parallel processing

---

## Common Questions & OS-Based Explanations

### "Why does the model forget what I said earlier?"

**OS Frame:** This is a RAM limitation. The context window is your working memory. When the conversation exceeds context length, earlier tokens get evicted - like when a computer runs out of RAM and has to page to disk (except LLMs don't have that fallback by default).

**Implication:** For long conversations, you need external memory (RAG, summaries) or larger context models.

### "Why is the model slower with longer prompts?"

**OS Frame:** Attention is O(n^2) - each token attends to every other token. It's like running a program that grows quadratically with input size. The "CPU" has to do more work.

**Implication:** Keep prompts focused. Don't pad context with unnecessary information.

### "Why can't it do math reliably?"

**OS Frame:** The "CPU" (transformer) wasn't designed for arithmetic - it's a pattern-matching engine trained on text. It's like asking a GPU to do CPU work - technically possible but not what it's optimized for.

**Implication:** Use tools (code interpreter) for computation. Let the LLM orchestrate, not calculate.

### "Why do different prompts give different results?"

**OS Frame:** The "program" (prompt) is interpreted, not compiled. Small differences in instructions can lead to different execution paths. Unlike deterministic code, the model makes probabilistic choices.

**Implication:** Prompt engineering matters. Be explicit. Test variations.

---

## Workflow
### Step 1: Identify the Question Type

| Category | Examples |
|----------|----------|
| Capability limits | "Why can't it...?" |
| Behavior explanation | "Why does it...?" |
| Design decisions | "Why is it built this way?" |
| Comparison | "Why is model A different from B?" |

### Step 2: Map to OS Concepts

Find the relevant mapping:
- Memory issues → Context window
- Speed issues → Computation/attention
- Capability issues → Training/weights
- Consistency issues → Probabilistic execution
- Tool-related → System calls/extensions

### Step 3: Explain Using the Analogy

Structure:
1. State the OS equivalent
2. Explain why this creates the behavior
3. Give the practical implication

### Step 4: Provide Practical Guidance

Based on the architectural reality:
- What the user should do differently
- What they should expect
- Workarounds if any exist

---

## Output Format

```markdown
## {Question}

### OS-Based Explanation

In the LLM-as-OS model, this relates to **{component}**.

{Explanation using the analogy}

### Why This Happens

{Technical explanation mapped to familiar concepts}

### What This Means for You

{Practical implications}

### Recommendations

1. {Actionable advice 1}
2. {Actionable advice 2}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Model-specific question without model context | Ask which model, or give general answer with caveats |
| Question beyond current understanding | Acknowledge uncertainty, share what is known |
| User expects deterministic behavior | Explain probabilistic nature of LLM execution |
| Question about training internals | Distinguish between architecture (known) and training specifics (often proprietary) |

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

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill implements Karpathy's "LLM OS" framework. When using as andrej-karpathy expert:
- Use the computing paradigm analogy extensively
- Quote: "We're computing circa ~1960s"
- Emphasize we're early in understanding these systems
- Connect to Software 2.0/3.0 when relevant