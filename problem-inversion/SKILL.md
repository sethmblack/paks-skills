---
name: problem-inversion
description: When stuck on a problem, swap the given and required to find simpler paths. Work backwards from the solution to the starting conditions. Claude Shannon's technique.
license: MIT
metadata:
  version: 1.0.1675
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- problem-inversion
- problem-solving
- structure
- writing
---

# Problem Inversion

Claude Shannon credited problem inversion with solving challenges that seemed intractable: "I got the idea that if I inverted the problem, it would have been very easy to do - if the given and required results had been interchanged; and that idea led to a way of doing it which was far simpler than the first design." When you're stuck going from A to B, try starting at B and working toward A. The inverted problem is often dramatically simpler, and solving it reveals insights that translate back to the original. This asymmetry - forward is hard, backward is easy - appears constantly in mathematics, engineering, and life.

---

## When to Use

- User is stuck on a problem that resists direct approaches
- Forward progress has stalled
- The path from A to B seems impossibly complex
- Someone says "I've tried everything"
- Design or planning problems where the end state is clearer than the path
- Debugging: easier to ask "how would I create this bug?" than "what causes it?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem as currently framed |
| given | No | What you start with (will be identified if not explicit) |
| required | No | What you need to achieve (will be identified if not explicit) |
| attempts | No | What forward approaches have been tried |

---

## Core Principle

Problems have direction: from given conditions to required results. But this direction is often arbitrary. When forward progress stalls, the inverted problem - assuming the required and deriving the given - frequently has a simpler structure. Solving the easier inverted problem reveals insights that translate back to the original. Inversion exploits the asymmetry between forward and backward reasoning.

---

## Methodology

### Phase 1: Identify Given and Required
1. Clearly state what you start with (given conditions)
2. Clearly state what you need to achieve (required results)
3. Note the implicit direction of the problem
4. Identify assumptions about how to get from given to required

### Phase 2: Swap Them
1. Assume the required results exist (or are true)
2. Ask: "Starting from here, what would lead to the given conditions?"
3. Work backward from the solution toward the starting point
4. Note what becomes obvious from this direction that wasn't obvious forward

### Phase 3: Solve the Inverted Problem
1. The inverted problem is often dramatically simpler
2. Use whatever tools work for the inverted direction
3. Document the solution path from required to given
4. Note the key insights that emerge

### Phase 4: Translate Back
1. Reverse the solution steps to get a forward path
2. Map inverted insights to forward progress
3. Identify what was blocking forward progress that inversion revealed
4. Construct the solution to the original problem

### Phase 5: Verify
1. Confirm the translated solution solves the original problem
2. Check that no steps were lost in translation
3. Note whether the path is actually reversible
4. Document the key insight that made inversion work

---

## Output Format

```markdown
## Problem Inversion Analysis

### Original Problem
**Given:** [starting conditions]
**Required:** [goal or output]
**Direction:** [A to B]
**Why forward is hard:** [what's blocking direct progress]

### Inverted Problem
**Given:** [original required, now assumed]
**Required:** [original given, now the target]
**Direction:** [B to A]

### Inverted Solution
[How the inverted problem is solved - often simpler]

### Key Insight from Inversion
[What becomes clear when working backwards that wasn't clear going forward]

### Translated Solution
[The inverted solution mapped back to the original problem]

### Verification
[Confirmation that this solves the original problem]
```

---

## Constraints

- Inversion doesn't always help - some problems are symmetric or harder inverted
- The translated solution must be verified against the original problem
- The path may not be reversible - translation requires care
- Some inversions reveal the original problem is impossible or ill-posed
- Inversion is a technique, not a guarantee

---

## Anti-Patterns to Avoid

- **Mechanical Reversal**: Simply reversing the steps isn't inversion. Inversion means assuming the end state and deriving what must have been true - not just running the forward solution backwards.

- **Forgetting to Translate Back**: Solving the inverted problem is only half the work. You must translate the insights back to the original problem structure.

- **Assuming Symmetry**: Not all problems are symmetric. Sometimes inversion doesn't help because the backward problem is just as hard or harder.

- **Skipping Verification**: The translated solution must actually solve the original problem. Inversion can reveal insights that don't quite translate - verify before declaring victory.

- **Using Inversion When Forward is Obvious**: If you can see the forward path clearly, take it. Inversion is for when you're stuck.

---

## Examples

### Example 1: API Design

**Situation**: "I need to design an API that handles both authenticated and unauthenticated requests gracefully. I keep getting tangled in conditional logic - auth checks everywhere."

**Application**:
- Given: Need to handle two request types with different behaviors
- Required: Clean API without scattered conditionals
- Inverted: Assume clean code with no scattered conditionals exists. How does it handle two request types?

**Output**:
Inverted solution: If code is clean with no scattered conditionals, then auth check happens in exactly ONE place, early. The result is encoded in types or context. Handlers receive pre-determined context, never raw requests. Two paths exist, not one path with conditionals.

Key insight: The problem isn't "how do I add auth checks" - it's "how do I separate authenticated and unauthenticated flows so they don't need checks."

Translated solution:
1. Create gateway/middleware that handles auth once, at the edge
2. Split into AuthenticatedHandler(user, request) and PublicHandler(request)
3. Route at gateway - handlers never check auth
4. Handlers know what they're dealing with by construction, not by checking

### Example 2: Debugging

**Situation**: "This bug appears randomly. Sometimes the calculation is wrong by exactly 1. I can't reproduce it consistently."

**Application**:
- Given: System produces wrong results sometimes
- Required: Find the bug
- Inverted: If I wanted to create a bug that produces off-by-one errors randomly, how would I do it?

**Output**:
Inverted solution: To create random off-by-one errors, I would:
- Use a shared counter that sometimes gets accessed without locking
- Have an array with fence-post confusion (loop says < vs <=)
- Rely on rounding that differs based on floating point state

Key insight: The "random" appearance suggests shared state or timing, not deterministic logic error.

Translated solution: Look for shared mutable state, race conditions, or floating-point rounding - not for logic errors in the calculation itself.

### Example 3: Goal Planning

**Situation**: "I want to write a book but I don't know where to start. There's so much to figure out."

**Application**:
- Given: Current state (no book, just an idea)
- Required: Published book
- Inverted: The book exists and is published. What must have happened just before publication? And before that?

**Output**:
Inverted solution (working backwards):
- Book published <- manuscript submitted to publisher <- manuscript complete <- chapters written <- outline complete <- research done <- concept validated <- idea chosen

Key insight: Working forward, everything seems overwhelming because you're trying to figure out all steps at once. Working backward, each step has a clear predecessor.

Translated solution: The next step isn't "write a book" - it's "validate the concept." Then "do research." Then "complete outline." The forward path becomes clear when you derive it from the backward path.

---

## Integration

**Works with:**
- **problem-simplification**: Simplify before or after inverting
- **problem-deepening**: Understand the problem deeply before inverting
- **debugging-methodology**: Inversion is especially powerful for debugging

**When to prefer this skill:**
- When forward progress has completely stalled
- When the end state is clearer than the path
- When debugging mysterious issues

**Cautions:**
- Don't use inversion when forward is obvious - it adds unnecessary complexity
- Always verify the translated solution against the original problem
- Some problems genuinely don't benefit from inversion