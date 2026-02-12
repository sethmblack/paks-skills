---
name: expectations-analysis
description: Map the recursive structure of expectations in coordination problems - what people believe others believe.
version: 1.0.0
author: sethmblack
tags: [compression, expectations-analysis, writing]
---

# Expectations Analysis

Map the recursive structure of expectations in coordination problems - what people believe others believe.

---

## When to Use

- Analyzing market behavior that seems disconnected from fundamentals
- Understanding political dynamics and coalition formation
- Navigating situations where everyone is trying to anticipate everyone else
- Explaining bubbles, panics, and sudden shifts in consensus
- User asks "Is this about fundamentals or psychology?" or "Beauty contest analysis"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The coordination problem or market/social dynamic |
| actors | Yes | Key participants and their positions |
| observable_beliefs | No | What people are saying or how they're acting |

---

## Keynes's Beauty Contest

In Chapter 12 of *The General Theory*, Keynes described professional investment as similar to a newspaper beauty contest:

> "Professional investment may be likened to those newspaper competitions in which the competitors have to pick out the six prettiest faces from a hundred photographs, the prize being awarded to the competitor whose choice most nearly corresponds to the average preferences of the competitors as a whole; so that each competitor has to pick, not those faces which he himself finds prettiest, but those which he thinks likeliest to catch the fancy of the other competitors, all of whom are looking at the problem from the same point of view."

### The Levels of Reasoning

**Level 0 (Naive):** Pick what YOU think is best
**Level 1:** Pick what you think OTHERS will pick
**Level 2:** Pick what you think others think others will pick
**Level 3+:** Recursive expectations about expectations...

Keynes noted: "We have reached the third degree where we devote our intelligences to anticipating what average opinion expects the average opinion to be."

### The Key Insight

In coordination games, what IS true matters less than what people BELIEVE is true, and what they believe OTHERS believe. Markets can rationally diverge from fundamental value because everyone is trying to anticipate everyone else.

---

## The Analysis Framework

### Step 1: Map the Levels

| Level | Question | Analysis |
|-------|----------|----------|
| 0 | What is the fundamental truth/value? | [Objective analysis] |
| 1 | What do key actors believe? | [Stated and revealed beliefs] |
| 2 | What do they believe others believe? | [How they position based on others] |
| 3 | What is the common knowledge? | [What everyone knows everyone knows] |

### Step 2: Identify the Coordination Point

Where will expectations converge? Coordination points are often:
- Focal points (salient, obvious choices)
- Historical precedents
- Authoritative pronouncements
- Self-fulfilling prophecies

### Step 3: Assess Stability

- **Stable equilibrium**: Beliefs and reality reinforce each other
- **Unstable equilibrium**: Small shocks could shift expectations dramatically
- **Multiple equilibria**: Different coordination points are possible

### Step 4: Strategic Implications

Given the expectation structure:
- Where is the opportunity? (Mismatch between levels)
- What could shift the coordination point?
- How vulnerable is the current consensus?

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
## Expectations Analysis (Beauty Contest)

### Situation
[Brief description of coordination problem]

### Level Mapping

**Level 0 - Fundamentals:**
[What is objectively true or valuable]

**Level 1 - First-Order Beliefs:**
[What key actors believe]
- Actor A believes: [X]
- Actor B believes: [Y]

**Level 2 - Second-Order Beliefs:**
[What actors believe others believe]
- Actor A thinks others believe: [X']
- Actor B thinks others believe: [Y']

**Level 3 - Common Knowledge:**
[What everyone knows everyone knows]

### Coordination Point
[Where expectations are converging, or could converge]

### Stability Assessment
[Stable / Unstable / Multiple Equilibria Possible]

### Divergences and Opportunities
| Level Gap | Implication |
|-----------|-------------|
| [Gap identified] | [Strategic opportunity or risk] |

### Strategic Recommendations
1. [Recommendation]
2. [Recommendation]

### The Keynesian Verdict
[Summary of the expectation dynamics]
```

---

## Common Patterns

### The Self-Fulfilling Prophecy
When expectations create the reality they expect:
- Bank runs: Belief that a bank will fail causes withdrawal, causing failure
- Bubbles: Belief that prices will rise causes buying, causing prices to rise
- Recessions: Belief that recession is coming causes reduced spending, causing recession

### The Coordination Trap
When everyone is stuck in a bad equilibrium because no one wants to move first:
- Everyone knows X would be better
- Everyone knows everyone knows X would be better
- But no one switches because they expect others won't switch
- Result: Stuck at inferior Y

### The Keynesian Beauty Contest Trap
Trying to out-guess others' guesses:
- You buy not because it's valuable, but because you think others will buy
- This works until everyone tries it simultaneously
- Result: Prices disconnected from value, vulnerable to sudden reversal

### The Schelling Point
When coordination succeeds because of obvious focal points:
- No communication needed
- Salient features guide convergence
- But: Which features are salient can shift

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

**Input:** "Our industry has been talking about moving from Technology A to Technology B for years. Everyone agrees B is better. But nobody is switching. Why, and what should we do?"

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


## Expectations Analysis (Beauty Contest)

### Situation
Industry-wide technology transition that everyone agrees should happen but hasn't.

### Level Mapping

**Level 0 - Fundamentals:**
Technology B is objectively superior. Technical analysis supports transition. This is not disputed.

**Level 1 - First-Order Beliefs:**
- Most firms believe B is better (stated in conferences, publications)
- Most firms believe the transition "will happen eventually"
- Most firms believe they should "wait and see"

**Level 2 - Second-Order Beliefs:**
- Firms believe others will not switch yet (too risky to go first)
- Firms believe early movers will bear switching costs while laggards learn from their mistakes
- Firms believe the industry is "not ready" (meaning: others aren't ready)

**Level 3 - Common Knowledge:**
- Everyone knows B is better
- Everyone knows everyone is waiting
- Everyone knows this is a coordination problem
- But: No one knows WHO will move first or WHEN

### Coordination Point
Currently stuck at Technology A. Potential triggers for coordination shift:
- Major player commits publicly
- Regulatory mandate
- Critical mass of small players demonstrates viability
- Technology A suffers visible failure

### Stability Assessment
**Unstable equilibrium.** The gap between Level 0 (B is better) and current behavior (stay on A) creates tension. Once a credible coordination signal emerges, rapid cascade is likely. The question is not IF but WHEN and WHO triggers it.

### Divergences and Opportunities

| Level Gap | Implication |
|-----------|-------------|
| L0 vs. L1: "B is better" vs. "not yet" | First mover could capture advantage if switching costs are manageable |
| L1 vs. L2: "I should switch" vs. "Others won't" | Coalition formation could break the deadlock |
| Universal waiting | Whoever provides credible coordination signal captures influence |

### Strategic Recommendations

1. **Assess your switching costs privately.** The common assumption that "going first is risky" may be wrong for you specifically. Run the numbers without assuming you must wait.

2. **Form a coalition.** If several medium-sized players commit together, you achieve critical mass without anyone going alone. The coordination problem becomes solvable.

3. **Create a Schelling point.** Announce a specific date or milestone for your transition. Make it public. Others may coordinate around your signal.

4. **Watch for the trigger.** If you won't lead, at least be ready. When the cascade starts, laggards will face compressed timelines and premium costs.

5. **Don't confuse "the industry isn't ready" with "I'm not ready."** "The industry" is just a collection of firms all saying the same thing about each other.

### The Keynesian Verdict

You are in a beauty contest where everyone is picking A because they think others will pick A, even though everyone knows B is prettier. This is not a fundamentals problem - it's a coordination problem. Fundamentals say B wins. But markets and industries don't run on fundamentals alone; they run on expectations about expectations.

The question isn't whether B will win - it will. The question is whether you'll be positioned to benefit from the transition or scrambling to catch up. "Worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally" - but worldly wisdom is expensive when the convention shifts.

---

## Integration

This skill is part of the **John Maynard Keynes** expert persona. Use it to understand situations where what people believe matters as much as what is true.