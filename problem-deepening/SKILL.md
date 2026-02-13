---
name: problem-deepening
description: Deeply understand problems before attempting solutions - spending 55 minutes on the problem and 5 minutes on solutions. Most problems persist because they are not well understood.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4738
repository: https://github.com/sethmblack/paks-skills
keywords:
- problem-deepening
- problem-solving
- transformation
- writing
---

# Problem Deepening

Einstein reportedly said: "If I had an hour to solve a problem, I'd spend 55 minutes thinking about the problem and five minutes thinking about solutions." Most problems persist not because solutions are hard to find, but because the problem isn't well understood. This skill develops deep understanding of any problem - its root causes, hidden assumptions, true nature, and real constraints - before attempting solutions. The most costly error in problem-solving is elegantly solving the wrong problem. Time spent deepening problem understanding is not delay; it's the most direct path to effective action.

---

## When to Use

- You're about to invest significant effort in solving something
- Solutions aren't working and you don't know why
- You suspect you might be solving the wrong problem
- The problem keeps recurring despite solutions
- User asks "Help me understand this problem" or "Am I solving the right problem?"
- Someone says "We've tried everything" or "Why is this actually hard?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem as currently understood or stated |
| context | No | Background information, history, prior attempts |
| stakeholders | No | Who is affected, who defined the problem |
| constraints | No | Known limitations (may contain hidden assumptions) |

---

## Core Principle

The quality of your solution is bounded by the quality of your understanding. A problem well-stated is half-solved; a problem poorly understood will resist every solution. Most "stuck" situations exist because the stated problem isn't the real problem - it's a symptom, a side effect, or someone else's frame imposed on your situation. Deepen before you solve.

---

## Methodology

### Phase 1: Surface the Stated Problem
1. Write down the problem as currently understood
2. Note who defined it this way and when
3. Identify what solution frame is implied by this definition
4. Ask: "What assumptions does this framing smuggle in?"

The way a problem is stated often predetermines the solution space. "How do I get more done?" assumes doing more is the goal. "How do I do what matters?" opens different possibilities.

### Phase 2: Question the Assumptions
1. List everything being taken for granted
2. For each assumption, ask: "What if the opposite were true?"
3. Identify constraints accepted without examination
4. Ask: "Why do I think this is a problem? Whose problem is this really?"

**Key questions:**
- What am I taking for granted?
- What would happen if the opposite were true?
- Why do I believe this constraint is real?

### Phase 3: Identify Root Causes
1. Apply the "Five Whys" technique - keep asking why until you reach something fundamental
2. Distinguish symptoms from causes
3. Look for patterns: When doesn't this problem occur?
4. Identify the system dynamics that produce this problem repeatedly

**Five Whys example:**
- We're missing deadlines. Why?
- Features take longer than estimated. Why?
- Requirements change mid-development. Why?
- We don't understand customer needs at start. Why?
- We start building before validating. Why?
- We feel pressure to show progress.
- Root cause: Culture rewards activity over understanding.

### Phase 4: Map Constraints
1. **Genuine constraints:** Physics, law, absolute limits - must work within these
2. **Perceived constraints:** Assumptions, conventions, habits - feel like limits but could be challenged
3. **Self-imposed constraints:** Beliefs, fears, preferences - come from within and can be changed

Many problems become easy when perceived constraints are recognized and removed.

### Phase 5: Reframe the Problem
1. With deeper understanding, reformulate the problem statement
2. Try multiple reframings: invert it, expand it, contract it, flip the subject
3. Ask: "What question, if answered, would make this problem dissolve?"
4. Test: Does the reframed problem suggest different solutions?

### Phase 6: Generate Better Questions
1. The output of problem deepening is better questions, not answers
2. Good questions open new solution spaces and challenge hidden assumptions
3. Transform the original question into a question that points toward root causes

---

## Output Format

```markdown
## Problem Deepening: [Topic]

### Stated Problem
[How the problem is currently framed]
**Who defined it:** [source of this framing]
**Implied solution frame:** [what solutions this framing suggests]

### Hidden Assumptions
- [Assumption 1]: What if this isn't true?
- [Assumption 2]: What if this isn't true?

### Root Cause Analysis
**Surface symptom:** [what's visible]
**First why:** [immediate cause]
**Second why:** [cause of cause]
**Third why:** [deeper cause]
**Fourth why:** [structural cause]
**Fifth why:** [root cause or system dynamic]

**Root cause identified:** [the fundamental issue]

### Constraints Analysis
**Genuine constraints (must accept):**
- [Constraint]: [why it's real]

**Perceived constraints (can challenge):**
- [Constraint]: [why it might not be real]

**Self-imposed constraints (can change):**
- [Constraint]: [where it comes from]

### Reframed Problem
**Original:** [initial framing]
**Reframed:** [better framing based on deeper understanding]

### Better Questions
- [Question that opens new solution space]
- [Question that challenges assumptions]
- [Question that addresses root cause]

### What Solving the Reframed Problem Requires
[Key insight about what must change]
```

---

## Constraints

- Do not skip to solutions - the purpose is deepening, not solving
- Acknowledge when you're uncertain about root causes
- Distinguish your analysis from the user's stated problem
- Recognize that some problems are genuinely complex and resist simple root causes
- Surface political/emotional factors when they're part of the real problem
- Don't remove constraints that are actually constraints

---

## Anti-Patterns to Avoid

- **Jumping to Solutions**: The most common failure. You hear a problem and immediately think of solutions. The discipline is to stay with the problem longer than feels comfortable.

- **Accepting the Stated Problem**: Taking the problem as given without questioning who framed it and what assumptions that framing contains. The stated problem is often wrong.

- **Surface-Level Why**: Asking "why" once and stopping. Real root causes are usually 4-5 levels deep. Keep digging.

- **Problem Statement as Solution**: "I need to implement X" isn't a problem statement - it's a solution embedded in a problem frame. Extract the actual problem.

- **Urgency as Excuse**: "We don't have time to understand, we need to act!" This is how you spend six months on the wrong solution. Understanding is the fastest path.

---

## Examples

### Example 1: Procrastination

**Situation**: "I need help solving my procrastination problem."

**Application**:
- Stated problem: "I procrastinate and need to stop"
- Hidden assumptions: Procrastination is the problem (not a symptom); more willpower will help; the tasks should be done
- Root cause analysis: Why procrastinate? Overwhelmed when starting. Why? Task seems too big. Why? Haven't broken it into steps. Why? Anxious about discovering how hard it is. Why? Because if I fail after trying, I can't protect my self-image.
- Root cause: Procrastination serves as ego protection

**Output**:
Reframed problem: "How do I make starting feel safe enough that I don't need procrastination to protect my self-image?"

Better questions:
- What would happen if I gave myself permission to do it badly?
- What's the smallest possible action that would count as starting?
- When do I not procrastinate, and what's different about those situations?

### Example 2: Team Communication

**Situation**: "My team doesn't communicate well. We need better tools."

**Application**:
- Stated problem: Poor team communication, need tools
- Hidden assumptions: Communication is a tool problem; more tools = better communication; everyone wants to communicate
- Root cause analysis: Why don't they communicate? Messages go unanswered. Why? People are too busy. Why? Because they're in meetings. Why? Because we "communicate" through meetings. Why? Because text feels inefficient for important things.
- Root cause: Mismatch between communication modes and communication needs

**Output**:
Reframed problem: "What makes asynchronous communication feel unreliable for important matters, and how do we fix that?"

Better questions:
- What gets communicated well, and what doesn't? What's different?
- What would make people trust async communication for important decisions?
- Are we communicating too much about the wrong things?

### Example 3: Revenue Growth

**Situation**: "We need to grow revenue by 30%."

**Application**:
- Stated problem: Revenue must increase by 30%
- Hidden assumptions: Revenue is the right metric; 30% is the right target; growth is the right strategy
- Root cause analysis: Why 30%? Board expectation. Why that expectation? Based on comparable companies. Why comparable? Same market, different stage. Why is growth the path? Assumed, not examined.
- Realization: The goal is proving a viable business; revenue growth is one path among several

**Output**:
Reframed problem: "What would make the board confident in the business's viability? Is revenue growth the most credible signal?"

Better questions:
- What is the board actually trying to assess with the 30% target?
- What evidence would be more convincing than revenue growth?
- Is 30% revenue growth achievable and, if so, at what cost to other metrics?

---

## Integration

**Works with:**
- **problem-inversion**: Swap given and required after deepening to find new approaches
- **problem-simplification**: Strip down the deepened understanding to essentials
- **root-cause-diagnosis**: Structured approach to the root cause portion

**When to prefer this skill:**
- Before investing significant effort in any solution
- When previous solutions haven't worked
- When the problem statement itself feels off

**Cautions:**
- Analysis paralysis is real - at some point you must act
- Not every problem needs deep analysis - small problems can be solved directly
- Sometimes the stated problem actually is the real problem