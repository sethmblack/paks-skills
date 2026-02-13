---
name: problem-simplification
description: Strip any problem down to its essential elements, removing everything extraneous until only the core challenge remains. Claude Shannon's primary technique.
license: MIT
metadata:
  version: 1.0.1676
  author: sethmblack
keywords:
- problem-simplification
- problem-solving
- structure
- writing
---

# Problem Simplification

Claude Shannon considered simplification "probably a very powerful approach" - his first and most important technique. Any problem presented to you comes wrapped in layers: historical context, assumed constraints, emotional overlay, premature solutions embedded in problem statements, details about implementation rather than goals. Simplification strips all this away until only the essential challenge remains. Shannon's definition of the fundamental problem of communication - "reproducing at one point either exactly or approximately a message selected at another point" - captured in one sentence what others needed pages to describe. Your job is to find the equivalent essential statement for any problem.

---

## When to Use

- User presents a complex, tangled problem with many factors
- Someone is overwhelmed by a situation's apparent complexity
- A problem description has grown bloated with irrelevant details
- Request to "simplify this" or "what's the real issue?"
- Before attempting any sophisticated solution approach
- When solutions keep failing and you suspect the problem is misstated

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem as currently understood, with all its complexity |
| context | No | Background information, constraints, history |
| goals | No | What success looks like |
| previous_attempts | No | What has been tried (may reveal what's essential) |

---

## Core Principle

Every problem has an essential core surrounded by noise. The noise includes: assumed constraints that aren't real, implementation details that don't affect the goal, historical context that doesn't constrain the present, emotional overlay that clouds technical reality, and solutions embedded in problem statements. Simplification removes the noise to reveal what you're actually trying to accomplish. A problem well-simplified often suggests its own solution.

---

## Methodology

### Phase 1: List All Elements
1. Enumerate everything currently considered part of the problem
2. Include: stated requirements, assumed constraints, stakeholders, technical factors, historical context, emotional factors, dependencies
3. Don't judge yet - just list everything that's been mentioned or implied

### Phase 2: Identify the Core Objective
1. Ask: "What is the fundamental thing we're trying to accomplish?"
2. State it in one sentence
3. If you need more than one sentence, you haven't found the core yet
4. The core should be independent of any particular solution approach

### Phase 3: Challenge Each Element
For every element from Phase 1, ask:
- Is this actually required, or just assumed?
- Does this affect the core objective?
- If we removed this, would we still have the essential problem?
- Is this a constraint or a choice?
- Is this problem or solution?

### Phase 4: Remove the Extraneous
Eliminate everything that is:
- An assumed constraint rather than an actual one
- Detail about implementation rather than the goal
- Historical context that doesn't affect current decision
- Emotional overlay that clouds technical reality
- Premature solution elements embedded in the problem
- Context that informs but doesn't constrain

### Phase 5: Restate Simply
1. Express the simplified problem in 1-3 sentences
2. If it takes more, you haven't simplified enough
3. Include only genuine constraints
4. Use clear, direct language

### Phase 6: Verify Equivalence
1. Confirm that solving the simplified problem would solve the original
2. If not, you've removed something essential - add it back
3. Check with stakeholders if possible
4. Note what was removed and why

---

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
- [Element]: [why it's not essential]
- [Element]: [why it's not essential]

### Simplified Problem Statement
[1-3 sentence statement of the essential problem]

### Why This Simplification Works
[Confirmation that solving this addresses the original]

### What Solutions This Opens
[If the simplification suggests approaches that weren't visible before]
```

---

## Constraints

- Do not remove things that are genuinely required - simplify, don't distort
- Preserve constraints that are actually constraints (laws, physics, real budgets)
- Keep the problem solvable - if simplification makes it trivial, you may have oversimplified
- Acknowledge when emotional/political factors are essential to the real problem
- State assumptions explicitly when removing "assumed" constraints
- Be willing to add elements back if verification fails

---

## Anti-Patterns to Avoid

- **Removing Real Constraints**: The goal is to remove noise, not to pretend constraints don't exist. Physics, law, and genuine resource limits are real. Don't simplify them away.

- **Oversimplifying to Trivial**: If your simplified problem is "just do the thing," you've gone too far. The essential challenge should still be recognizably challenging.

- **Preserving Emotional Elements as Requirements**: "The CEO wants it blue" might be a real constraint or might be a preference. Don't preserve emotional attachment as technical requirement.

- **Conflating Simplification with Solution**: Simplifying the problem isn't solving it. You should still have a problem at the end - just a clearer one.

- **Ignoring Stakeholder Frames**: Sometimes what seems like noise (politics, history, relationships) is actually essential to the real problem. Verify before removing.

---

## Examples

### Example 1: Distributed Team Communication

**Situation**: "Our team of 12 engineers across three time zones needs to coordinate on a shared codebase. We've tried Slack, twice-weekly standups, and a wiki, but knowledge keeps getting lost. People duplicate work. The senior engineers in London complain that decisions get made while they're asleep. Our manager wants us to adopt a new project management tool but nobody has time to learn it."

**Application**:
- List: 12 engineers, three time zones, shared codebase, Slack, standups, wiki, knowledge loss, duplicate work, London complaints, manager's tool suggestion, no time for new tool
- Core objective: Team members need to know what others are doing and participate in decisions

**Output**:
Elements removed as extraneous:
- Specific tools tried (Slack, wiki, standups) - past attempts, not current constraints
- Manager's tool suggestion - solution embedded in problem
- Number of engineers - scale matters for solutions but not for problem statement
- "No time for new tool" - may be excuse, not constraint

Simplified problem: "Information produced by the team doesn't reliably reach everyone who needs it, when they need it. The current system favors some time zones over others for synchronous decision-making."

### Example 2: Product Launch

**Situation**: "We need to launch by Q3 to hit the holiday season, but engineering says they need 6 more months, marketing hasn't started the campaign, sales wants different features than we've built, and the CEO is asking about progress every day."

**Application**:
- List: Q3 deadline, 6-month engineering estimate, marketing delay, sales feature requests, CEO pressure
- Core objective: Unclear - is it "launch by Q3" or "launch successfully" or "satisfy CEO"?

**Output**:
The problem reveals multiple problems conflated:
1. Misalignment between desired launch date and engineering reality
2. Misalignment between built features and sales needs
3. Stakeholder management (CEO)
4. Marketing readiness

Simplified problem depends on what's actually being solved:
- If deadline is immovable: "What can we ship by Q3 that would be worth shipping?"
- If features are immovable: "How do we reset stakeholder expectations?"
- If neither: "What is success, and who decides?"

The original problem statement assumes all constraints are fixed. Simplification reveals they can't all be fixed.

### Example 3: Career Transition

**Situation**: "I want to change careers from finance to tech but I'm 38 and have a mortgage and kids, and I don't have time to go back to school, and tech companies won't look at my resume, and I'd take a huge pay cut, and my spouse isn't sure about it."

**Application**:
- List: Age concern, mortgage, kids, no time for school, resume rejection, pay cut, spouse uncertainty
- Core objective: Work in tech industry instead of finance

**Output**:
Elements analysis:
- Age: Perceived constraint (38 is not unusual for career change)
- Mortgage/kids: Real constraint - need income stability
- No school time: Assumed constraint - depends on what education is actually needed
- Resume rejection: May be approach problem, not fundamental blocker
- Pay cut: May be real, may be avoidable depending on role
- Spouse: Real constraint - but nature unclear (information need? fear? preference?)

Simplified problem: "How do I transition from finance to tech while maintaining income sufficient for my family obligations?"

This reveals: the problem isn't "can I do it" but "how do I do it without financial disruption." Suggests different solutions: transition roles within current company, move to fintech, consulting bridges, etc.

---

## Integration

**Works with:**
- **problem-deepening**: Simplify after deepening to capture essential insight
- **problem-inversion**: Invert the simplified problem for new approaches
- **root-cause-diagnosis**: Simplification often reveals root causes

**When to prefer this skill:**
- When problems feel overwhelming
- When previous solutions keep failing
- As first step before any complex problem-solving
- When stakeholders are confused about what they're trying to do

**Cautions:**
- Verify simplification with stakeholders when possible
- Don't mistake "simpler" for "easy"
- Some problems are genuinely complex and resist simplification
- Preserve what's essential even if it's uncomfortable