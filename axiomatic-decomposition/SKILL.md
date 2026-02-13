---
name: axiomatic-decomposition
description: 'Structure any complex analysis, argument, or system design using Newton''s axiomatic method from the Principia: definitions, axioms, propositions, corollaries.'
license: MIT
metadata:
  version: 1.0.3435
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- axiomatic-decomposition
- writing
---

# Axiomatic Decomposition

Structure any complex analysis, argument, or system design using Newton's axiomatic method from the Principia: definitions, axioms, propositions, corollaries.

**Token Budget:** ~800 tokens
**Source Expert:** isaac-newton

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply axiomatic structure to justify harmful conclusions
- Present contested assumptions as self-evident axioms
- Create deceptive formal structures that mask flawed reasoning
- Skip the definition phase to hide ambiguous terms

**If asked to axiomatize harmful arguments:** Refuse explicitly. Explain that formal structure does not confer validity to unethical conclusions.

---

## When to Use

- "Structure this argument axiomatically"
- "Break this down like Principia"
- "Give me the first principles structure"
- "Make this argument rigorous"
- Building technical documentation that must be unambiguous
- Designing systems where requirements must follow logically
- Troubleshooting where cause-effect chains must be explicit

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| content | Yes | The problem, argument, or system to structure |
| domain | No | Context (e.g., "distributed systems", "security policy") |
| goal | No | What the structured output should accomplish |

---

## The Axiomatic Method

Newton structured the Principia with extraordinary rigor:

1. **Definitions** - Precise meanings of all key terms
2. **Axioms/Laws** - Self-evident truths or stated assumptions
3. **Propositions** - Claims derived from definitions and axioms
4. **Demonstrations** - Logical proofs of each proposition
5. **Corollaries** - Immediate consequences of propositions
6. **Scholia** - Explanatory notes and applications

This structure ensures:
- No hidden assumptions
- Every term means exactly one thing
- Every claim has explicit support
- Gaps in reasoning are immediately visible

---

## Workflow

### Step 1: Extract Key Terms

Identify every significant term or concept in the content. Ask:
- What words could be interpreted multiple ways?
- What concepts are assumed but not explained?
- What domain jargon needs clarification?

**Output:** List of terms requiring definition.

### Step 2: Write Definitions

For each term, write a precise definition:
- Use only previously defined terms or common knowledge
- Make definitions operational (testable, measurable)
- Avoid circular definitions

**Format:**
```
Definition 1: [Term] is [precise definition].
Definition 2: [Term] means [precise definition].
```

### Step 3: State Axioms

Identify the foundational assumptions that cannot be proven within this context:
- What must be accepted as true to proceed?
- What constraints are given externally?
- What laws or principles apply?

Each axiom should be:
- Self-evident or explicitly assumed
- Necessary for the argument
- Minimal (don't assume more than needed)

**Format:**
```
Axiom 1: [Statement accepted as true]
Axiom 2: [Statement accepted as true]
```

### Step 4: Build Propositions

Construct claims that follow from definitions and axioms:
- Start with simple propositions close to axioms
- Build toward complex conclusions
- Each proposition references only definitions, axioms, or previous propositions

**Format:**
```
Proposition 1: [Claim]
Demonstration: By Definition [X] and Axiom [Y], it follows that...

Proposition 2: [More complex claim]
Demonstration: From Proposition 1 and Axiom [Z]...
```

### Step 5: Derive Corollaries

State immediate consequences of key propositions:
- What follows obviously from what we've proven?
- What special cases are worth noting?

**Format:**
```
Corollary 1.1: [Immediate consequence of Proposition 1]
Corollary 2.1: [Immediate consequence of Proposition 2]
```

### Step 6: Add Scholia (Optional)

Provide explanatory context:
- Real-world applications
- Limitations of the analysis
- Connections to other domains
- Historical or practical notes

---

## Output Format

```markdown
## Axiomatic Analysis: [Title]

### Definitions

**Definition 1:** [Term] - [Precise definition]
**Definition 2:** [Term] - [Precise definition]

### Axioms

**Axiom 1:** [Foundational assumption]
**Axiom 2:** [Foundational assumption]

### Propositions

**Proposition 1:** [Claim]
*Demonstration:* [Logical derivation from definitions and axioms]

**Proposition 2:** [Claim]
*Demonstration:* [Logical derivation from previous propositions]

### Corollaries

**Corollary 1.1:** [Consequence of Proposition 1]
**Corollary 2.1:** [Consequence of Proposition 2]

### Scholium

[Explanatory notes, applications, limitations]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content too vague to axiomatize | Request clarification of scope and terms |
| Circular definitions detected | Flag and request alternative formulation |
| Axioms contain hidden conclusions | Decompose into more primitive assumptions |
| Proposition doesn't follow | Show the logical gap, suggest fix |
| Too many axioms | Apply parsimony - reduce to essential assumptions |

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

**Input:** "Explain why microservices should communicate asynchronously"

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


## Axiomatic Analysis: Asynchronous Microservice Communication

### Definitions

**Definition 1:** A *microservice* is an independently deployable component with a single responsibility, communicating with other components via network.

**Definition 2:** *Synchronous communication* is a pattern where the caller blocks until the callee responds.

**Definition 3:** *Asynchronous communication* is a pattern where the caller continues execution without waiting for the callee's response.

**Definition 4:** *Availability* is the probability that a service can respond to requests at a given time.

**Definition 5:** *Coupling* is the degree to which one component depends on another's internal state or availability.

### Axioms

**Axiom 1:** Network communication can fail or be delayed unpredictably.

**Axiom 2:** The availability of a chain of synchronous calls is the product of individual availabilities.

**Axiom 3:** Tight coupling reduces independent deployability.

### Propositions

**Proposition 1:** Synchronous communication creates tight temporal coupling between services.
*Demonstration:* By Definition 2, synchronous communication requires the caller to wait. By Axiom 1, this waiting may extend unpredictably. The caller's behavior therefore depends on the callee's response time, which is tight coupling per Definition 5.

**Proposition 2:** A chain of N synchronous services has availability A^N, where A is individual service availability.
*Demonstration:* By Axiom 2 directly. If each service is 99% available, three services yield 97% availability.

**Proposition 3:** Asynchronous communication decouples service availability.
*Demonstration:* By Definition 3, the caller does not wait. By Axiom 1, the callee may be temporarily unavailable. But since the caller continues, its availability is not reduced by the callee's availability. This reduces coupling per Definition 5.

### Corollaries

**Corollary 2.1:** System availability degrades exponentially with synchronous call chain depth.

**Corollary 3.1:** Asynchronous patterns (message queues, event buses) preserve independent deployability per Definition 1.

### Scholium

This analysis assumes requests can tolerate eventual consistency. For operations requiring immediate confirmation (e.g., payment authorization), synchronous patterns may be necessary despite availability costs.

---

## Integration

This skill originates from the **isaac-newton** expert, embodying Newton's methodology from the Principia Mathematica. When using this skill, maintain the voice of rigorous precision:

- Every term must be defined before use
- Every claim must be demonstrable from what precedes it
- Gaps are explicitly acknowledged, not hidden
- "Hypotheses non fingo" - do not present speculation as proof

---

## Success Criteria

Axiomatic decomposition is complete when:

- [ ] All key terms are explicitly defined
- [ ] All assumptions are stated as axioms (none hidden)
- [ ] Each proposition references only prior definitions/axioms/propositions
- [ ] Demonstrations are logically valid
- [ ] Corollaries follow immediately from propositions
- [ ] No circular reasoning exists