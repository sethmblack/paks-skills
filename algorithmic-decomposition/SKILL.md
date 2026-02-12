---
name: algorithmic-decomposition
description: Break complex problems into fundamental operations, identifying recursive
  structures, base cases, and step-by-step computational approaches - just as Ada
  Lovelace decomposed the Bernoulli number ca...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- algorithmic-decomposition
- transformation
- writing
---

# Algorithmic Decomposition

Break complex problems into fundamental operations, identifying recursive structures, base cases, and step-by-step computational approaches - just as Ada Lovelace decomposed the Bernoulli number calculation into the first computer program.

---

## When to Use

- User asks "How do I break this down?" or "Design an algorithm for this"
- Facing an overwhelming problem that needs systematic approach
- Creating processes, workflows, or computational solutions
- Teaching problem-solving methodology
- Any situation requiring step-by-step breakdown of complexity

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | Description of the complex problem to decompose |
| constraints | No | Limitations on resources, operations, or approach |
| desired_output | No | What the solution should produce |
| context | No | Domain or situation where this will be applied |

---

## The Five-Step Framework

### Step 1: Identify the Base Case

Find the simplest instance that can be solved directly without further decomposition.

**Questions to ask:**
- What is the trivial version of this problem?
- When does the problem become immediately solvable?
- What is the smallest unit I can handle directly?

**Ada's insight:** "Every complex calculation rests upon simpler ones. Find the foundation."

### Step 2: Define the Recursive Relation

Determine how complex cases relate to simpler ones. How does solving case N-1 help solve case N?

**Questions to ask:**
- If I had the solution to a slightly smaller problem, how would I extend it?
- What operation transforms a solved subproblem into the current problem?
- Is there a pattern where each step uses previous results?

**Ada's insight:** "The Bernoulli numbers are particularly amenable because they are defined recursively: we may use the first to determine the second, the second for the third, and so on."

### Step 3: Specify Elementary Operations

List the fundamental operations required. What are the atomic actions that cannot be further divided?

**Categories of operations:**
- Input/Output: Reading values, storing results
- Arithmetic: Addition, multiplication, comparison
- Control: Branching, iteration, conditional execution
- State: Remembering intermediate values, updating positions

**Ada's insight:** "The object is not simplicity or facility of computation, but the illustration of the powers of the engine" - choose operations that illuminate the structure.

### Step 4: Manage State and Variables

Identify what must be remembered between operations. How is information passed and preserved?

**Questions to ask:**
- What intermediate values must be stored?
- How are variables indexed or named?
- When are values overwritten vs. preserved?
- What is the memory footprint of the solution?

**Ada's insight:** In Note G, she pioneered notation for indexed variables (V0, V1, V2...) and tracked which values persisted through operations.

### Step 5: Verify the Weave

Trace through the algorithm to confirm it produces correct results. The pattern must hold.

**Verification approaches:**
- Walk through with simple examples
- Check boundary conditions (base cases, edge cases)
- Confirm the recursion terminates
- Verify state is correctly managed throughout

**Ada's insight:** "Close scrutiny shows that this scheme... would have worked" - even without a running machine, logical verification is possible.

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
## Algorithmic Decomposition

### Problem Restatement
[Clear, precise statement of what must be solved]

### Base Case
- **Condition:** [When the trivial solution applies]
- **Solution:** [Direct answer for the base case]

### Recursive Relation
- **From case N-1 to N:** [How simpler solutions build to complex ones]
- **Pattern:** [The generalizable relationship]

### Elementary Operations
1. [Operation 1]: [Description]
2. [Operation 2]: [Description]
...

### State Management
| Variable | Purpose | Lifecycle |
|----------|---------|-----------|
| [var1] | [what it holds] | [when created/modified/consumed] |

### Algorithm (Pseudocode)
```
[Step-by-step procedure using the above elements]
```

### Verification
- **Base case check:** [Confirmation it works]
- **Recursive step check:** [Confirmation pattern holds]
- **Edge cases:** [Boundary conditions addressed]
```

---

## Constraints

- Maintain precision - vague steps are not operations
- Ensure termination - recursion must reach base case
- Consider resources - memory and operation counts matter
- Preserve generality - solve the class of problems, not just one instance
- Document assumptions - make implicit requirements explicit

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

## Example

**Input:** "I need to calculate factorial of any positive integer"

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


## Algorithmic Decomposition

### Problem Restatement
Given a positive integer n, compute n! = n x (n-1) x (n-2) x ... x 2 x 1

### Base Case
- **Condition:** n = 1 (or n = 0)
- **Solution:** factorial(1) = 1, factorial(0) = 1

### Recursive Relation
- **From case N-1 to N:** factorial(n) = n x factorial(n-1)
- **Pattern:** Each factorial is the current number multiplied by all previous factorials

### Elementary Operations
1. **Multiply:** Combine two values into their product
2. **Decrement:** Reduce counter by 1
3. **Compare:** Check if base case reached
4. **Store:** Hold intermediate and final results

### State Management
| Variable | Purpose | Lifecycle |
|----------|---------|-----------|
| n | Current number | Input, decremented each step |
| result | Accumulated product | Initialized to 1, multiplied each step |

### Algorithm (Pseudocode)
```
function factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

Or iteratively:
```
function factorial(n):
    result = 1
    for i from 2 to n:
        result = result * i
    return result
```

### Verification
- **Base case check:** factorial(1) = 1 (correct by definition)
- **Recursive step check:** factorial(4) = 4 x factorial(3) = 4 x 6 = 24 (correct)
- **Edge cases:** factorial(0) = 1 (by convention), negative inputs should be rejected

---

## Integration

This skill is part of the **Ada Lovelace** expert persona. Use it when facing any problem that can be systematically broken into repeatable steps - the essence of what Ada pioneered with the first computer program.