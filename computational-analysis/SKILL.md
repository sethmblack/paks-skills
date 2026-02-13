---
name: computational-analysis
description: Break any process, system, or problem into its computational components to reveal hidden structure, identify failure points, and understand exactly how things work.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3182
repository: https://github.com/sethmblack/paks-skills
keywords:
- computational-analysis
- transformation
- writing
---

# Computational Analysis

Break any process, system, or problem into its computational components to reveal hidden structure, identify failure points, and understand exactly how things work.

---

## When to Use

- User asks "How does this work?" or "What's the algorithm?"
- Need to understand a complex workflow or system
- Diagnosing why a process is failing
- Request for "computational breakdown" or "Turing analysis"
- Something is not working and the cause is unclear
- Need to document or explain a process precisely

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| process | Yes | The system, workflow, algorithm, or problem to analyze |
| objective | No | What the process should accomplish (will be inferred if not provided) |
| failure_point | No | Where things seem to be going wrong (if known) |

---

## The Computational Framework

Every process - whether a computer program, a business workflow, a biological system, or a decision-making procedure - can be decomposed into five fundamental components.

### Component 1: Inputs

What data, materials, or information does the process start with?

**Questions to ask:**
- What raw materials or data enter the system?
- Where do inputs come from?
- What format are they in?
- Are all necessary inputs present?
- What happens when inputs are missing or malformed?

**Common issues:**
- Missing inputs that are assumed to exist
- Inputs in wrong format or structure
- Hidden inputs that are not acknowledged
- Inputs that vary in ways the process cannot handle

### Component 2: States

What conditions can the system be in at any point during execution?

**Questions to ask:**
- What are the possible states of the system?
- How does the system know which state it is in?
- Are there illegal or undefined states?
- Can the system get stuck in a state?

**Common issues:**
- States that are not clearly defined
- Missing states that should exist
- Illegal states the system can reach but cannot handle
- State transitions that should exist but do not

### Component 3: Operations

What transformations are performed on inputs as the process executes?

**Questions to ask:**
- What specific actions does the process take?
- In what order do operations occur?
- What triggers each operation?
- What does each operation require and produce?

**Common issues:**
- Operations that depend on undefined inputs
- Operations in wrong order
- Operations that should be atomic but are not
- Missing operations between states

### Component 4: Outputs

What does the process produce when it completes?

**Questions to ask:**
- What is the intended output?
- What outputs are actually produced?
- In what format are outputs delivered?
- Who or what consumes the outputs?

**Common issues:**
- Outputs not matching what downstream processes expect
- Missing outputs that should exist
- Outputs in wrong format
- Side effects that are not acknowledged as outputs

### Component 5: Termination

When and how does the process stop?

**Questions to ask:**
- What conditions cause the process to complete?
- Does the process always terminate?
- What happens on successful completion vs. failure?
- Can the process hang or run forever?

**Common issues:**
- No clear termination condition
- Infinite loops under certain inputs
- Premature termination
- Failure modes that are not handled

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
## Computational Analysis

### Process Summary
[1-2 sentence description of what is being analyzed]

### Inputs
| Input | Source | Format | Required | Notes |
|-------|--------|--------|----------|-------|
| [input1] | [where it comes from] | [data type/format] | [Yes/No] | [any issues] |

### States
| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| [state1] | [what this state means] | [how system enters] | [how system exits] |

### Operations
| Operation | Trigger | Inputs | Outputs | Notes |
|-----------|---------|--------|---------|-------|
| [op1] | [what causes it] | [what it needs] | [what it produces] | [issues/details] |

### Outputs
| Output | Format | Consumer | Status |
|--------|--------|----------|--------|
| [output1] | [type/format] | [who/what uses it] | [OK/Issue] |

### Termination Analysis
- **Normal completion:** [how process ends successfully]
- **Failure modes:** [how process can fail]
- **Halting guarantee:** [Does this always terminate? Under what conditions?]

### Diagnosis
**Identified Issues:**
1. [Issue 1 - where in the computational structure it occurs]
2. [Issue 2]

**Root Cause:** [The fundamental computational problem, if identifiable]

**Recommendations:**
1. [Specific fix for the computational structure]
2. [Additional recommendations]
```

---

## Analysis Process

1. **Define the boundary** - What is inside the system being analyzed? What is outside?

2. **Trace the flow** - Follow a single example through from input to output, noting each transformation.

3. **Enumerate states** - List every condition the system can be in.

4. **Map operations to state transitions** - Each operation should move the system from one state to another.

5. **Check termination** - Can you prove the process always finishes? What would prevent termination?

6. **Identify gaps** - Look for:
   - Inputs with no operations that use them
   - States with no exit transitions
   - Operations that require undefined inputs
   - Outputs that are never produced

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Assuming operations exist** | Many processes fail because a transition doesn't actually exist | Verify each operation; trace a concrete example through the entire system |
| **Skipping termination analysis** | Many problems stem from halting failures (infinite loops, stuck states) | Always analyze: does this always terminate? Under what conditions? |
| **Vague state definitions** | "Processing" or "in progress" without clear entry/exit conditions | Define states with specific entry and exit conditions |
| **Ignoring human decisions** | Treating human steps as black boxes | Model human decisions as operations with inputs and outputs |
| **Analyzing only happy path** | Missing failure modes that cause real problems | Enumerate all possible states, including error and stuck states |

---

## Example

**Input:** "Our user onboarding process keeps failing. New users sign up but never become active."

**Output:**

## Computational Analysis

### Process Summary
Analyzing user onboarding flow from signup to first active use of the product.

### Inputs
| Input | Source | Format | Required | Notes |
|-------|--------|--------|----------|-------|
| Email | User form | String | Yes | Validated format |
| Password | User form | String | Yes | Min 8 chars |
| User intent | Implicit | None | **Missing** | Why did they sign up? |
| Product context | Marketing source | None | **Missing** | What were they promised? |

### States
| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Signed Up | Account exists | Form submitted | Email verified |
| Verified | Email confirmed | Clicked link | **Undefined** |
| Onboarding | Tutorial state | **No trigger** | Tutorial complete |
| Active | Regular user | First value action | N/A |

### Operations
| Operation | Trigger | Inputs | Outputs | Notes |
|-----------|---------|--------|---------|-------|
| Create account | Form submit | Email, password | Account record | Works |
| Send verification | Account created | Email | Email sent | Works |
| Verify email | Link clicked | Token | Verified state | Works |
| Start onboarding | **None defined** | Verified user | **None** | **Gap identified** |
| Complete tutorial | Tutorial finished | User actions | Active state | Never reached |

### Outputs
| Output | Format | Consumer | Status |
|--------|--------|----------|--------|
| Active user | Account state | Product | **Not produced** |
| Engagement email | Email | User | Sent to verified, not onboarding |

### Termination Analysis
- **Normal completion:** User becomes Active after tutorial
- **Failure modes:** User stays in Verified state indefinitely
- **Halting guarantee:** Process halts at Verified with no forward path

### Diagnosis
**Identified Issues:**
1. **Missing state transition:** No operation moves users from Verified to Onboarding
2. **Missing input:** User intent not captured - cannot personalize onboarding
3. **Missing trigger:** Onboarding never starts automatically after verification

**Root Cause:** The computational structure has a gap between Verified and Onboarding states. There is no operation that bridges them. Users enter Verified and halt because no forward transition exists.

**Recommendations:**
1. Add operation: "Initiate onboarding" triggered automatically after email verification
2. Capture user intent during signup to personalize the onboarding path
3. Add timeout operation: if user in Verified for 24 hours with no activity, trigger re-engagement

---

## Constraints

- Always trace at least one concrete example through the entire system
- Do not assume operations exist - verify each transition
- Termination analysis is not optional - many problems stem from halting failures
- If the process involves humans, model their decisions as operations with inputs and outputs
- Acknowledge when information is insufficient to complete the analysis

---

## Integration

This skill is part of the **Alan Turing** expert persona. It embodies his fundamental insight that any process can be understood as computation. Use it when you need to:
- Understand how something works
- Find where a process is failing
- Document a system precisely
- Design a new process

Pairs well with:
- **fundamental-question-framing** for clarifying what needs to be analyzed
- **pattern-breaking** for finding regularities in process behavior
- **morphogenesis-thinking** for understanding how process behavior emerges from rules