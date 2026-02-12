---
name: problem-simplification
description: Strip any problem down to its essential elements, removing everything
  extraneous until only the core challenge remains. This is Claude Shannon's primary
  problem-solving technique.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- problem-simplification
- structure
- writing
---

# Problem Simplification

Strip any problem down to its essential elements, removing everything extraneous until only the core challenge remains. This is Claude Shannon's primary problem-solving technique.

---

## When to Use

- User presents a complex, tangled problem with many factors
- Someone is overwhelmed by a situation's apparent complexity
- A problem description has grown bloated with irrelevant details
- Request to "simplify this" or "what's the real issue?"
- Before attempting any sophisticated solution approach

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem as currently understood, with all its complexity |
| context | No | Background information, constraints, history |
| goals | No | What success looks like |

---

## The Simplification Process

### Step 1: List All Elements

Enumerate everything currently considered part of the problem:
- Stated requirements
- Assumed constraints
- Stakeholders mentioned
- Technical factors
- Historical context
- Emotional factors
- Dependencies

### Step 2: Identify the Core Objective

Ask: "What is the fundamental thing we're trying to accomplish?"

**Shannon's insight:** "The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point."

That single sentence captures what took others pages to describe. Find your equivalent.

### Step 3: Challenge Each Element

For every element from Step 1, ask:
- Is this actually required, or assumed?
- Does this affect the core objective?
- If we removed this, would we still have the essential problem?
- Is this a constraint or a choice?
- Is this problem or solution?

### Step 4: Remove the Extraneous

Eliminate everything that is:
- An assumed constraint rather than an actual one
- Detail about implementation rather than the goal
- Historical context that doesn't affect the current decision
- Emotional overlay that clouds the technical reality
- Premature solution elements embedded in the problem statement

### Step 5: Restate Simply

Express the simplified problem in one to three sentences. If it takes more, you haven't simplified enough.

### Step 6: Verify Equivalence

Confirm that solving the simplified problem would solve the original. If not, you've removed something essential—add it back.

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
## Problem Simplification

### Original Problem
[Brief restatement of the problem as presented]

### Elements Identified
| Element | Type | Essential? | Reasoning |
|---------|------|------------|-----------|
| [item] | [constraint/requirement/assumption/context] | [Yes/No] | [why] |

### Removed as Extraneous
- [Element 1]: [why it's not essential]
- [Element 2]: [why it's not essential]

### Simplified Problem Statement
[1-3 sentence statement of the essential problem]

### Verification
[Confirmation that solving the simplified problem addresses the original, or notes on what was preserved and why]
```

---

## Constraints

- Do not remove things that are genuinely required—simplify, don't distort
- Preserve constraints that are actually constraints (laws, physics, budgets)
- Keep the problem solvable—if simplification makes it trivial, you may have oversimplified
- Acknowledge when emotional/political factors are essential to the real problem
- State assumptions explicitly when removing "assumed" constraints

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

**Input:** "Our team of 12 engineers across three time zones needs to coordinate on a shared codebase. We've tried Slack, twice-weekly standups, and a wiki, but knowledge keeps getting lost. People duplicate work. The senior engineers in London complain that decisions get made while they're asleep. The junior engineers in Manila say they don't understand the architecture. Our manager wants us to adopt a new project management tool but nobody has time to learn it. We need to improve our communication but we're already in too many meetings."

**Output:**

## Problem Simplification

### Original Problem
A distributed engineering team struggles with knowledge sharing, duplicate work, and timezone-inequitable decision-making despite multiple communication tools.

### Elements Identified
| Element | Type | Essential? | Reasoning |
|---------|------|------------|-----------|
| 12 engineers | Context | Somewhat | Scale matters for solutions |
| Three time zones | Constraint | Yes | Fundamental to coordination challenge |
| Shared codebase | Context | Yes | Defines the coordination domain |
| Tried Slack | History | No | Past attempts inform but don't constrain |
| Tried standups | History | No | Same |
| Tried wiki | History | No | Same |
| Knowledge gets lost | Symptom | Yes | Core problem manifestation |
| Duplicate work | Symptom | Yes | Core problem manifestation |
| London timezone complaints | Symptom | Yes | Indicates inequity in system |
| Manila understanding gap | Symptom | Somewhat | May be separate training issue |
| Manager's tool suggestion | Distraction | No | Solution embedded in problem |
| "Too many meetings" | Constraint | Somewhat | Real capacity limit |

### Removed as Extraneous
- **Specific tools tried (Slack, wiki, standups):** The problem isn't which tools; it's whether information reaches the right people at the right time.
- **Manager's new tool suggestion:** This is a proposed solution, not part of the problem.
- **Number of engineers:** Relevant to solution sizing but not the essential problem.
- **Junior engineer understanding gap:** Likely a separate onboarding/documentation problem that may share solutions but has different root cause.

### Simplified Problem Statement
**Information produced by the team doesn't reliably reach everyone who needs it, when they need it. The current system favors some timezones over others for synchronous decision-making.**

### Verification
Solving for "reliable information distribution with timezone equity" would address: lost knowledge (information reaches people), duplicate work (people know what others are doing), London's decision exclusion (timezone-equitable processes). The Manila understanding issue may need separate attention as a knowledge gap rather than communication gap.

---

## Integration

This skill is part of the **Claude Shannon** expert persona. Shannon considered simplification "probably a very powerful approach" to any problem—his first and most important technique.