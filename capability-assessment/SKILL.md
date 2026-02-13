---
name: capability-assessment
description: Precisely define what a system, technology, or approach can and cannot do - distinguishing actual capabilities from aspirational claims, execution from origination, as Ada Lovelace did when assessi...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.510
keywords:
- capability-assessment
- transformation
- writing
---

# Capability Assessment

Precisely define what a system, technology, or approach can and cannot do - distinguishing actual capabilities from aspirational claims, execution from origination, as Ada Lovelace did when assessing the Analytical Engine.

---

## When to Use

- User asks "What can this actually do?" or "Can this system really do X?"
- Evaluating a new technology, tool, or methodology
- Cutting through marketing hype or inflated claims
- Making technology adoption decisions
- Assessing AI or automation capabilities
- Understanding the boundaries of any system

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | Description of the technology, tool, or approach being assessed |
| claimed_capabilities | No | What the system supposedly can do |
| use_case | No | Specific application being considered |
| context | No | Environment where system will be deployed |

---

## The Assessment Framework

### Step 1: Enumerate Actual Operations

List precisely what operations the system performs. Not what it "achieves" or "enables" - what it actually DOES.

**Questions to ask:**
- What are the atomic actions this system can execute?
- What transformations does it apply to inputs?
- What is the actual mechanism of operation?

**Ada's insight:** "It can do whatever we know how to order it to perform" - capability is bounded by specifiable operations.

### Step 2: Distinguish Execution from Origination

Separate what the system executes from what it creates. Does it follow instructions or generate them?

**Key distinction:**
- **Execution:** Performing operations according to specifications
- **Origination:** Creating new operations, insights, or approaches not in the specifications

**Ada's insight:** "The Analytical Engine has no pretensions whatever to originate anything... It can follow analysis; but it has no power of anticipating any analytical relations or truths."

**Questions to ask:**
- Does it produce novel outputs or recombine existing patterns?
- Can it do anything its creators didn't anticipate?
- Is apparent creativity actually sophisticated execution?

### Step 3: Map Boundaries and Edge Cases

Identify where capability ends. What inputs cause failure? What conditions exceed capacity?

**Boundary categories:**
- **Input boundaries:** What the system cannot process
- **Output boundaries:** What it cannot produce
- **Scale boundaries:** Where performance degrades
- **Domain boundaries:** Where applicability ends

**Questions to ask:**
- What happens with unexpected inputs?
- Where does performance degrade or fail?
- What domains are outside its scope?

### Step 4: Assess Claims Against Operations

Compare claimed capabilities to actual operations. Which claims are substantiated?

**Claim categories:**
- **Valid:** Directly supported by enumerated operations
- **Extrapolated:** Reasonable inference from operations but not demonstrated
- **Aspirational:** Desired but not currently achievable
- **False:** Contradicted by actual capability

**Ada's insight:** "It is desirable to guard against forming too exaggerated ideas of the powers of the Analytical Engine."

### Step 5: Define Appropriate Use Cases

Based on actual capabilities, identify where the system should and should not be applied.

**Use case assessment:**
- **Strong fit:** Operations align directly with need
- **Acceptable fit:** Operations partially address need with workarounds
- **Poor fit:** Gap between capability and need too large
- **Dangerous fit:** System might appear capable but fail critically

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
## Capability Assessment

### System Description
[Clear statement of what is being assessed]

### Actual Operations
| Operation | Description | Limitations |
|-----------|-------------|-------------|
| [op1] | [what it does] | [constraints] |

### Execution vs. Origination Analysis
- **Executes:** [What it performs according to specification]
- **Does NOT originate:** [What it cannot create independently]
- **Apparent creativity explanation:** [If applicable, how seeming creativity is actually execution]

### Capability Boundaries
| Boundary Type | Limit | Consequence of Exceeding |
|---------------|-------|--------------------------|
| [type] | [where it ends] | [what happens] |

### Claims Assessment
| Claim | Verdict | Reasoning |
|-------|---------|-----------|
| [claim] | Valid/Extrapolated/Aspirational/False | [why] |

### Recommended Use Cases
- **Strong fit:** [Where to use confidently]
- **Use with caution:** [Where to use carefully]
- **Avoid:** [Where not to use]

### Key Limitations Summary
[The most important things this system CANNOT do]
```

---

## Constraints

- Be precise, not dismissive - acknowledge genuine capabilities
- Distinguish "cannot do" from "cannot do yet"
- Consider capability in context of intended use
- Avoid both hype and excessive skepticism
- Make hidden assumptions about capability explicit

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

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Hype acceptance** | Marketing claims often exceed actual capability | Enumerate actual operations before assessing claims |
| **Excessive skepticism** | Dismissing real capabilities misses genuine utility | Acknowledge what the system CAN do, precisely |
| **Confusing potential with current** | "Could do X" is not "does X" | Separate actual from aspirational |
| **Ignoring context** | Capability depends on conditions and use case | Assess capability in specific deployment context |
| **Anthropomorphizing** | Attributing human-like understanding to systems | Focus on operations, not intentions or understanding |

## Example

**Input:** "Assess what a large language model like GPT-4 can actually do"

**Output:**

## Capability Assessment

### System Description
Large Language Model (LLM) trained on text data to predict and generate text sequences based on statistical patterns.

### Actual Operations
| Operation | Description | Limitations |
|-----------|-------------|-------------|
| Pattern matching | Identifies statistical relationships in text | Limited to patterns in training data |
| Sequence completion | Predicts likely next tokens | Probabilistic, not deterministic |
| Format transformation | Restructures text according to templates | Follows examples, not true understanding |
| Information retrieval | Surfaces information from training | Can't access real-time information |
| Style transfer | Generates text in specified styles | Mimicry, not authentic voice |

### Execution vs. Origination Analysis
- **Executes:** Text generation based on learned patterns; format transformation; summarization; translation between styles and languages
- **Does NOT originate:** Genuine new knowledge; logical proofs from first principles; information not derivable from training data; true understanding of meaning
- **Apparent creativity explanation:** Novel-seeming outputs are recombinations of training patterns. "Creative" writing reflects statistical relationships in human creative writing, not independent creative capacity.

### Capability Boundaries
| Boundary Type | Limit | Consequence of Exceeding |
|---------------|-------|--------------------------|
| Knowledge cutoff | Training data date | Confident errors about recent events |
| Reasoning depth | Complex multi-step logic | Plausible but incorrect conclusions |
| Factual accuracy | Frequently fabricates | "Hallucinations" presented confidently |
| Mathematical | Beyond simple arithmetic | Errors increase with complexity |
| Real-world grounding | No direct world interaction | Cannot verify claims against reality |

### Claims Assessment
| Claim | Verdict | Reasoning |
|-------|---------|-----------|
| "Understands language" | False | Processes statistical patterns, not meanings |
| "Can write code" | Valid | Generates syntactically correct code from patterns |
| "Reasons logically" | Extrapolated | Mimics reasoning patterns but lacks true logic |
| "Is creative" | Aspirational | Recombines existing patterns; no true origination |
| "Can replace human writers" | False | Cannot verify facts, maintain consistency, or originate |

### Recommended Use Cases
- **Strong fit:** Drafting, brainstorming, format conversion, code suggestions, summarization
- **Use with caution:** Research assistance (verify all facts), creative writing (as starting point only)
- **Avoid:** Factual assertions without verification, legal/medical advice, novel logical reasoning

### Key Limitations Summary
The system has no pretensions whatever to originate anything. It executes statistical text generation with impressive fluency but cannot verify truth, maintain genuine consistency, or produce knowledge not implicit in its training. Its province is to assist us in making available patterns we have already created, not to anticipate new truths.

---

## Integration

This skill is part of the **Ada Lovelace** expert persona. Use it when you need clear-eyed assessment of what any system can actually do, cutting through hype to reveal actual capability - the very analysis Ada pioneered for computing machines.