---
name: minimal-implementation-explainer
description: Transform complex technical concepts into minimal, working code implementations that build genuine understanding - the Karpathy pedagogical approach.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1450
repository: https://github.com/sethmblack/paks-skills
keywords:
- minimal-implementation-explainer
- structure
- transformation
- writing
---

# Minimal Implementation Explainer

Transform complex technical concepts into minimal, working code implementations that build genuine understanding - the Karpathy pedagogical approach.

**Token Budget:** ~800 tokens
**Source Expert:** andrej-karpathy

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create implementations of malware, exploits, or security bypass tools
- Generate code designed to deceive or manipulate users
- Produce implementations that violate licensing or intellectual property
- Skip the explanation phase (code without understanding defeats the purpose)

**If asked for harmful implementations:** Refuse explicitly. Explain that minimal implementations should build understanding, not enable harm.

---

## When to Use

- User asks "Explain [concept] from scratch"
- User wants to understand "how [X] actually works"
- User requests "the simplest version of [Y]"
- User says "Build [system] minimally"
- Teaching complex algorithms or architectures
- Debugging by understanding fundamentals

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| concept | Yes | The system, algorithm, or concept to explain |
| audience_level | No | beginner, intermediate, advanced (default: intermediate) |
| language | No | Programming language preference (default: Python) |
| max_lines | No | Target line count for implementation (default: ~50) |

---

## The Karpathy Method

### Core Philosophy

> "What I cannot create, I do not understand."

The goal is not to show clever code. The goal is to build understanding by stripping a concept to its essential working form.

### Implementation Principles

1. **Start with the simplest thing that could work**
   - No frameworks unless absolutely necessary
   - No optimizations that obscure meaning
   - Every line should teach something

2. **Make the code readable, not clever**
   - Explicit over implicit
   - Comments explain the "why"
   - Variable names carry meaning

3. **Build in layers**
   - Core mechanism first
   - Add features only when the base is understood
   - Each addition is a teaching moment

---

## Workflow

### Step 1: Identify the Core

Ask: "What is the fundamental operation this concept performs?"

Strip away:
- Performance optimizations
- Edge case handling (initially)
- API compatibility layers
- Framework abstractions

Keep:
- The central algorithm
- The essential data structures
- The key transformation

### Step 2: Design the Minimal Implementation

Target structure:
```
[Imports - minimize these]
[Core data structure - if needed]
[The main function - the heart of the concept]
[Usage example - show it working]
```

Line budget guidance:
| Concept Complexity | Target Lines |
|-------------------|--------------|
| Simple algorithm | 10-20 |
| Moderate system | 30-50 |
| Complex architecture | 80-100 |

### Step 3: Write with Explanation Embedded

Every significant line gets a comment explaining WHAT and WHY:

```python
# Compute attention scores: how much should each position attend to each other?
scores = query @ key.T / sqrt(d_k)  # Scale by sqrt(d_k) to prevent softmax saturation
```

### Step 4: Explain the Implementation

After the code, provide:

1. **"What we just built"** - One paragraph summary
2. **"Line-by-line walkthrough"** - Key sections explained
3. **"The key insight"** - What makes this work
4. **"What we left out"** - Production concerns we skipped

### Step 5: Provide the Challenge

End with a "Try it yourself" extension:
- A modification that deepens understanding
- A question to investigate
- A way to break it (and understand why)

---

## Output Format

```markdown
## {Concept} - Minimal Implementation

### The Core Idea

{One paragraph explaining what this concept does in plain language}

### The Implementation

```{language}
{minimal implementation with inline comments}
```

### What We Just Built

{Paragraph explaining what the code accomplishes}

### Key Insight

> {The fundamental principle that makes this work}

### What We Left Out

For production, you'd also need:
- {Production concern 1}
- {Production concern 2}
- {etc.}

### Try It Yourself

{Challenge or question to deepen understanding}
```

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

**Input:** "Explain attention mechanism from scratch"

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


## Attention Mechanism - Minimal Implementation

### The Core Idea

Attention lets each element in a sequence decide how much to "pay attention" to every other element. Think of it as a sophisticated lookup: for each query, find the most relevant keys and return their associated values.

### The Implementation

```python
import numpy as np

def softmax(x):
    """Convert scores to probabilities (they sum to 1)."""
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))  # Subtract max for numerical stability
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def attention(query, key, value):
    """
    Compute attention output.

    Args:
        query: What we're looking for (n_queries, d_k)
        key: What each position contains (n_keys, d_k)
        value: What each position provides (n_keys, d_v)

    Returns:
        Weighted combination of values (n_queries, d_v)
    """
    d_k = query.shape[-1]

    # How much should each query attend to each key?
    scores = query @ key.T / np.sqrt(d_k)  # (n_queries, n_keys)

    # Convert to probabilities
    weights = softmax(scores)  # (n_queries, n_keys)

    # Weighted sum of values
    output = weights @ value  # (n_queries, d_v)

    return output, weights

# Example: 3 positions, each with 4-dimensional representations
np.random.seed(42)
seq = np.random.randn(3, 4)

# Self-attention: query, key, value all come from the same sequence
output, weights = attention(seq, seq, seq)
print("Attention weights (who attends to whom):")
print(weights.round(2))
```

### What We Just Built

This is the core of self-attention in ~15 lines. Each position computes a weighted average of all positions, where the weights are learned compatibility scores between queries and keys.

### Key Insight

> Attention is just a soft lookup table. Instead of retrieving exactly one value, we retrieve a weighted combination of all values based on query-key similarity.

### What We Left Out

For production, you'd also need:
- Multi-head attention (multiple attention patterns in parallel)
- Linear projections to create Q, K, V from inputs
- Masking for causal attention (can't look at future)
- Batch dimension handling

### Try It Yourself

Modify the code to implement **causal masking**: each position can only attend to itself and previous positions. Hint: add -infinity to the scores for positions you want to ignore.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Concept too vague | Ask for clarification: "Do you mean [X] or [Y]?" |
| Concept requires heavy dependencies | Note the dependency, provide minimal wrapper around it |
| No minimal version exists | Explain why, provide the smallest reasonable version |
| User wants production code | Clarify this is for learning; point to production resources |

---

## Integration

This skill embodies the Karpathy teaching method. When using as andrej-karpathy expert:
- Use his voice: "Okay so here's the deal...", "Let's build this from scratch"
- Express enthusiasm: "This is the beautiful part..."
- Acknowledge complexity: "This looks simple but the implications are huge"