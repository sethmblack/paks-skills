---
name: problem-inversion
description: When stuck on a problem, swap the given and required to find simpler paths. Work backwards from the solution to the starting conditions.
version: 1.0.0
author: sethmblack
tags: [problem-inversion, structure, writing]
---

# Problem Inversion

When stuck on a problem, swap the given and required to find simpler paths. Work backwards from the solution to the starting conditions.

---

## When to Use

- User is stuck on a problem that resists direct approaches
- Forward progress has stalled
- The path from A to B seems impossibly complex
- Someone says "I've tried everything"
- Design or planning problems where the end state is clearer than the path

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem as currently framed |
| given | No | What you start with (will be identified if not explicit) |
| required | No | What you need to achieve (will be identified if not explicit) |
| attempts | No | What approaches have already been tried |

---

## The Inversion Process

### Step 1: Identify Given and Required

Clearly state:
- **Given:** What you start with, know, or have
- **Required:** What you need to produce, prove, or achieve

This often reveals hidden assumptions about direction.

### Step 2: Swap Them

Ask: "What if I started with the required and worked toward the given?"

- If you need to get from A to B, imagine starting at B and finding paths to A
- If you need to prove X from premises Y, assume X and derive Y
- If you need to build something, imagine it exists and work out what must have been true

### Step 3: Solve the Inverted Problem

The inverted problem is often dramatically simpler. Solve it.

**Shannon's insight:** "I got the idea that if I inverted the problem, it would have been very easy to do—if the given and required results had been interchanged; and that idea led to a way of doing it which was far simpler than the first design."

### Step 4: Translate Back

Convert your inverted solution back to the original problem:
- Reverse the steps
- Map the inverted insights to forward progress
- Identify the key insight that inversion revealed

### Step 5: Verify the Solution

Confirm that your translated solution actually solves the original problem, not just the inverted one.

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
## Problem Inversion Analysis

### Original Problem
**Given:** [starting conditions]
**Required:** [goal or output]
**Direction:** [A to B]

### Inverted Problem
**Given:** [original required, now assumed]
**Required:** [original given, now the target]
**Direction:** [B to A]

### Inverted Solution
[How the inverted problem is solved—often simpler]

### Key Insight from Inversion
[What becomes clear when working backwards that wasn't clear going forward]

### Translated Solution
[The inverted solution mapped back to the original problem]

### Verification
[Confirmation that this solves the original problem]
```

---

## Common Inversion Patterns

### Design Inversion
- **Forward:** "How do I build a system that does X?"
- **Inverted:** "If I had a system that does X, what must be true about its components?"

### Debugging Inversion
- **Forward:** "What's causing this bug?"
- **Inverted:** "If I wanted to cause this exact bug on purpose, what would I do?"

### Planning Inversion
- **Forward:** "How do I get from here to my goal?"
- **Inverted:** "Starting from my goal, what must have happened just before? And before that?"

### Proof Inversion
- **Forward:** "How do I prove X from these axioms?"
- **Inverted:** "Assuming X is true, what follows? Does it connect to what I know?"

### Constraint Inversion
- **Forward:** "How do I do X given constraint Y?"
- **Inverted:** "If I could do X, what does that tell me about constraint Y?"

---

## Constraints

- Inversion doesn't always help—some problems are symmetric or harder inverted
- The translated solution must be verified against the original problem
- Don't confuse working backwards with reversing the solution (the path may not be reversible)
- Some inversions reveal that the original problem is impossible or ill-posed

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

**Input:** "I need to design an API that handles both authenticated and unauthenticated requests gracefully. I keep getting tangled in the conditional logic—there are auth checks everywhere and the code is becoming unmaintainable."

**Output:**

## Problem Inversion Analysis

### Original Problem
**Given:** Need to handle two request types (authenticated, unauthenticated) with different behaviors
**Required:** Clean API design without scattered auth conditionals
**Direction:** From request entry to appropriate handling

### Inverted Problem
**Given:** Assume I have clean code with no scattered auth conditionals
**Required:** How does such code handle the two request types?
**Direction:** From clean architecture to understanding what it must look like

### Inverted Solution
If the code is clean with no scattered conditionals, then the auth check must happen in exactly ONE place, early, and the result must be carried through in a way that doesn't require re-checking.

This means:
1. A single entry point determines auth status
2. The result is encoded in the type system or request object itself
3. Handlers receive already-determined context, not raw requests
4. Two separate paths exist, not one path with conditionals

### Key Insight from Inversion
The problem isn't "how do I add auth checks"—it's "how do I separate authenticated and unauthenticated flows so they don't need checks." The conditionals exist because I'm treating two different things as one thing.

### Translated Solution
1. **Create a gateway/middleware** that handles auth once, at the edge
2. **Split into two handler types:**
   - `AuthenticatedHandler(user, request)`
   - `PublicHandler(request)`
3. **Route at the gateway:** Auth success goes to authenticated handlers; failure goes to public handlers or rejection
4. **Handlers never check auth:** They receive pre-validated context

The scattered conditionals disappear because each handler knows what it's dealing with by construction, not by checking.

### Verification
- Authenticated requests: Gateway validates, routes to AuthenticatedHandler with user context
- Unauthenticated requests: Gateway routes to PublicHandler or returns 401
- No auth checks in business logic
- Original requirement satisfied with cleaner architecture

---

## Integration

This skill is part of the **Claude Shannon** expert persona. Shannon explicitly credited inversion with solving problems that seemed intractable when approached directly.