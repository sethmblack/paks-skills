---
name: inversion-analysis
description: Apply Charlie Munger's inversion thinking to identify failure modes and
  systematically avoid them.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- inversion-analysis
- writing
---

# Inversion Analysis

Apply Charlie Munger's inversion thinking to identify failure modes and systematically avoid them.

---

## When to Use

- Planning a major initiative, project, or life change
- Developing strategy for a business or personal goal
- Trying to improve outcomes in an area where you've struggled
- Evaluating a decision by understanding what could go wrong
- User asks "How would this fail?" or "Invert this problem" or "What should I avoid?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| goal | Yes | What you're trying to achieve |
| context | No | Current situation, constraints, resources |
| past_failures | No | Previous attempts that didn't work |

---

## Munger's Inversion Principle

"All I want to know is where I'm going to die, so I'll never go there."

"Invert, always invert: Turn a situation or problem upside down. Look at it backwards. What happens if all our plans go wrong? Where don't we want to go, and how do you get there? Instead of looking for success, make a list of how to fail instead."

Inspired by mathematician Carl Jacobi's maxim: "man muss immer umkehren" (invert, always invert).

The power of inversion:
- **Forces objectivity** - Easier to see failure modes than success paths
- **Defeats first-conclusion bias** - Challenges initial assumptions
- **Reveals hidden risks** - Forward planning often misses dangers obvious in reverse
- **Simplifies complexity** - Often clearer what to avoid than what to do

---

## The Framework (6 Steps)

**Step 1: State the Goal Clearly**
What exactly are you trying to achieve? Be specific.

**Step 2: Invert the Goal**
Ask: "What would guarantee failure?" or "How would I definitely NOT achieve this?" or "If I wanted the opposite outcome, what would I do?"

**Step 3: Generate Failure Modes**
List all the ways you could fail. Be comprehensive. Think about:
- Common mistakes in this domain
- Your personal weaknesses and blind spots
- External factors that could derail you
- Stupid decisions that would be obvious in hindsight
- Slow erosion vs. sudden collapse failure modes

**Step 4: For Each Failure Mode, Identify the Countermeasure**
What specific action prevents or mitigates each failure mode?

**Step 5: Build an Avoidance-First Strategy**
Your strategy becomes: avoid all identified failure modes. This often simplifies decision-making dramatically.

**Step 6: Then (and Only Then) Optimize for Success**
With failure modes addressed, add positive actions that increase probability of success.

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
## Inversion Analysis

### Goal
[Clear statement of what you're trying to achieve]

### The Inversion Question
"How would I guarantee [FAILURE/OPPOSITE OF GOAL]?"

### Failure Modes

| # | Failure Mode | How It Causes Failure | Probability | Impact |
|---|-------------|----------------------|-------------|--------|
| 1 | [Failure mode] | [Mechanism] | High/Med/Low | High/Med/Low |
| 2 | [Failure mode] | [Mechanism] | High/Med/Low | High/Med/Low |
| ... | ... | ... | ... | ... |

### Countermeasures

| Failure Mode | Countermeasure | Implementation |
|-------------|----------------|----------------|
| [Failure mode 1] | [How to prevent/mitigate] | [Specific action] |
| [Failure mode 2] | [How to prevent/mitigate] | [Specific action] |
| ... | ... | ... |

### Avoidance-First Strategy
[Strategy built around avoiding failure modes]

### Success Additions
[Positive actions to add after avoidance is addressed]

### The Munger Test
"All I want to know is where I'm going to die, so I'll never go there."
[Summary of key places to never go]
```

---

## Failure Mode Categories

Consider each of these when generating failure modes:

**Self-Inflicted**
- Obvious stupidity you might commit
- Known personal weaknesses
- Predictable emotional responses
- Laziness and short-term thinking

**Structural**
- Wrong incentives
- Poor team or partner selection
- Inadequate resources or time
- Flawed assumptions

**Environmental**
- Market or industry changes
- Competitive responses
- Regulatory or legal issues
- Black swan events

**Behavioral**
- Overconfidence
- Confirmation bias
- Social proof following
- Sunk cost fallacy

---

## Constraints

- **Be brutally honest** - Include embarrassing failure modes. Self-deception defeats the exercise.
- **Think second-order** - Consider failures that result from your responses to initial problems
- **Include obvious stupidity** - "Things that would be embarrassing to fail from" are often most important
- **Don't stop at three** - Push for at least 7-10 failure modes before considering yourself done

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

**Input:** "I want to build a successful side business while keeping my full-time job."

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


## Inversion Analysis

### Goal
Build a profitable side business while maintaining full-time employment.

### The Inversion Question
"How would I guarantee my side business fails while also damaging my career?"

### Failure Modes

| # | Failure Mode | How It Causes Failure | Probability | Impact |
|---|-------------|----------------------|-------------|--------|
| 1 | Burnout from overwork | Physical/mental exhaustion kills both | High | High |
| 2 | Neglecting day job performance | Get fired, lose income and health insurance | Medium | High |
| 3 | Violating employment contract | Legal issues, termination, reputation damage | Medium | High |
| 4 | Choosing wrong idea | Spend months on unviable concept | High | Medium |
| 5 | Never actually shipping | Perpetual "building" without revenue | High | High |
| 6 | Underpricing to feel safe | Unsustainable economics from day one | High | Medium |
| 7 | Telling everyone too early | Social pressure without substance | Medium | Low |
| 8 | Spending savings on startup costs | Financial stress forcing bad decisions | Medium | High |
| 9 | No customer validation | Building what nobody wants | High | High |
| 10 | Partner/spouse conflict | Relationship damage derails everything | Medium | High |

### Countermeasures

| Failure Mode | Countermeasure | Implementation |
|-------------|----------------|----------------|
| Burnout from overwork | Set hard time limits, protect sleep | Maximum 15 hrs/week on side business, bed by 10:30 PM |
| Neglecting day job | Define "minimum acceptable" day job performance | Write it down; if slipping below, pause side project |
| Violating employment contract | Read contract carefully, get legal review if needed | Ensure no IP conflicts, no competing, no using employer resources |
| Choosing wrong idea | Validate before building | Require 5 paying customers before committing fully |
| Never shipping | Set public launch deadline | Launch MVP in 90 days maximum, no exceptions |
| Underpricing | Price based on value, not comfort | 3x what feels comfortable as starting point |
| Telling everyone too early | Stealth mode until revenue | No announcements until $1K MRR |
| Spending savings | Bootstrap completely | $0 in startup costs until profitable |
| No customer validation | Talk to customers first | 20 customer interviews before writing code |
| Partner/spouse conflict | Explicit agreement upfront | Written agreement on time, money, expectations |

### Avoidance-First Strategy

The business will succeed if I simply avoid the top failure modes:

1. **Protected energy**: 15 hours/week maximum, sleep non-negotiable
2. **Day job first**: Define minimum acceptable performance, pause project if slipping
3. **Legal clarity**: Contract reviewed, no gray areas
4. **Validation before building**: 5 paying customers or 20 interviews before committing
5. **Ship quickly**: 90-day maximum to MVP, then iterate
6. **Sustainable economics**: Price for value, bootstrap only
7. **Relationship alignment**: Explicit agreement with partner

### Success Additions

After avoiding failure modes, add:
- Specific, narrow niche with clear pain point
- Simple first product, complexity later
- One marketing channel mastered, not five dabbled
- Weekly reviews against plan
- Network of other side-business founders for support

### The Munger Test
"All I want to know is where I'm going to die, so I'll never go there."

Never go:
- Into chronic sleep deprivation
- Forward without customer validation
- Beyond 15 hours/week until it pays my salary
- Into any legal gray areas with employer
- Public before proof of concept

---

## Integration

This skill is part of the **Charlie Munger** expert persona. Use it to identify exactly where you're going to die—so you'll never go there.