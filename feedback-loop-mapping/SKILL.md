---
name: feedback-loop-mapping
description: Identify and map the reinforcing and balancing feedback loops that drive system behavior. Reveal why interventions succeed or fail by understanding the loops that amplify or resist change.
version: 1.0.0
author: sethmblack
tags: [feedback-loop-mapping, writing]
---

# Feedback Loop Mapping

Identify and map the reinforcing and balancing feedback loops that drive system behavior. Reveal why interventions succeed or fail by understanding the loops that amplify or resist change.

---

## When to Use

- When patterns repeat despite intervention
- When things spiral out of control (positive or negative)
- When the system seems to resist change
- When you need to understand "why this keeps happening"

**Trigger Phrases:**
- "It keeps getting worse"
- "Why does this cycle?"
- "The harder we push, the more it resists"
- "There's a vicious cycle"
- "It's a self-fulfilling prophecy"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system to analyze |
| problem_behavior | No | What pattern is observed |
| attempted_fixes | No | What has been tried |

---

## Core Concepts

### Feedback Loop

A closed chain of causal connections where a change in one element eventually circles back to affect that same element.

```
A → B → C → A (loop closes)
```

### Reinforcing (Positive) Loops

**Effect:** Amplify change in the same direction. Growth or collapse.

**Behavior:** Exponential—accelerating change that feeds on itself.

**Examples:**
- Compound interest: More money → more interest → more money
- Viral spread: More infected → more spreading → more infected
- Trust erosion: Distrust → withholding information → more distrust

**Visual marker:** Often labeled "R" or "+" in diagrams.

### Balancing (Negative) Loops

**Effect:** Resist change, seek equilibrium. Stabilizing or goal-seeking.

**Behavior:** Oscillation toward a target—may overshoot and correct.

**Examples:**
- Thermostat: Too cold → heater on → warmer → heater off
- Hunger: Low energy → eat → high energy → stop eating
- Market prices: High price → less demand → lower price

**Visual marker:** Often labeled "B" or "-" in diagrams.

---

## The Mapping Protocol

### Step 1: Identify the Behavior Pattern

What are you seeing?
- **Growth/explosion:** Something increasing faster and faster
- **Collapse/spiral:** Something decreasing faster and faster
- **Oscillation:** Swings around a level, over-and underreaching
- **S-curve:** Growth that slows and levels off
- **Stagnation:** Stuck at an undesired level

### Step 2: Identify Key Variables

What changes? Name the stocks (things that accumulate):
- Population, revenue, inventory, reputation, trust, skill level
- What goes up? What goes down? What stays stuck?

### Step 3: Trace Causal Chains

For each variable, ask:
- What causes it to increase?
- What causes it to decrease?
- What does its level affect?

Follow the chain until it loops back (or connects to another loop).

### Step 4: Classify Each Loop

**Reinforcing:** Each arrow increases the next (or even number of decreases)
- A↑ → B↑ → C↑ → A↑ (reinforcing growth)
- A↑ → B↓ → C↓ → A↑ (reinforcing through double-negative)

**Balancing:** Odd number of "opposite direction" effects
- A↑ → B↑ → C↓ → A↓ (balancing)

### Step 5: Identify Dominant Loops

Which loop is currently "winning"?
- In growth, a reinforcing loop dominates
- In stability, a balancing loop dominates
- In transition, dominance is shifting

### Step 6: Find Delays

Where are time lags between cause and effect?
- Delays cause oscillation and overshoot
- Delays obscure feedback, making learning difficult

---

## Common Patterns

### Vicious Cycle

A reinforcing loop running in an undesirable direction.

**Example: Employee Burnout**
```
High turnover →
  Remaining employees overworked →
    Stress and burnout →
      More turnover →
        (loop repeats, accelerating)
```

**Intervention:** Break the loop by addressing any link.

### Virtuous Cycle

A reinforcing loop running in a desirable direction.

**Example: Reputation Building**
```
Good work →
  Positive reputation →
    Better opportunities →
      More good work →
        (loop repeats, accelerating)
```

**Caution:** Can reverse if any link fails.

### Balancing Loop with Delay

Delay between action and result causes oscillation.

**Example: Inventory Management**
```
Low inventory → Order more → (delay) → Inventory arrives → High inventory → Order less → (delay) → Inventory depletes
```

**Result:** Boom-bust cycles instead of smooth adjustment.

### Competing Loops

Multiple loops operate on the same stock.

**Example: Business Growth**
```
R: Success → Resources → More investment → More success
B: Growth → Complexity → Inefficiency → Limits success
```

**Behavior depends on which loop dominates at current scale.**

---

## Diagram Notation

### Simple Arrow Diagram

```
Variable A  ──(+)──>  Variable B
            same direction

Variable A  ──(-)──>  Variable B
            opposite direction
```

### Loop Diagram

```
        ┌────(+)────┐
        ▼           │
    Variable A ─────┘
        │
       (R) = Reinforcing

        ┌────(-)────┐
        ▼           │
    Variable A ─────┘
        │
       (B) = Balancing
```

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

## Outputs

| Output | Description |
|--------|-------------|
| Loop diagram | Visual map of feedback structure |
| Loop inventory | List of all identified loops |
| Loop classification | Reinforcing vs. balancing for each |
| Dominance analysis | Which loops currently drive behavior |
| Delay identification | Where timing lags exist |
| Intervention points | Where loops can be broken or strengthened |

---



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


## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**User:** "Our product quality keeps declining. We fix one issue and two more appear. We've hired more QA but it doesn't help."

**Feedback Loop Mapping response:**

Let me map the loops operating here.

**Variables to track:**
- Product quality (stock)
- Developer capacity
- Technical debt
- Bug count
- Customer complaints
- Pressure to ship

**Loop 1: Quality-Capacity Spiral (Reinforcing - Vicious)**
```
↓ Quality →
  ↑ Bugs →
    ↑ Time fixing bugs →
      ↓ Time for new development →
        ↑ Pressure to cut corners →
          ↓ Quality
          (R)
```

**Loop 2: Technical Debt Accumulation (Reinforcing - Vicious)**
```
↓ Quality →
  ↑ Technical debt →
    ↑ Complexity →
      ↑ Likelihood of new bugs →
        ↓ Quality
        (R)
```

**Loop 3: QA Overload (Balancing - Failing)**
```
↓ Quality →
  ↑ QA workload →
    (attempting to stabilize)
    BUT: QA capacity < Bug generation rate
    Loop is dominated by reinforcing loops
```

**Why more QA doesn't help:**

Adding QA is a balancing loop trying to counteract the reinforcing loops. But:
- The balancing loop is weaker than the reinforcing loops
- QA catches bugs *after* they're created—it doesn't reduce creation rate
- The reinforcing loops create bugs faster than QA can catch them

**Where the leverage is:**

Don't strengthen the balancing loop (more QA). Weaken the reinforcing loops:

1. **Break the corner-cutting link:** Reduce pressure to ship quickly
2. **Reduce technical debt:** Pay it down to reduce complexity
3. **Reduce bug creation rate:** Improve practices, not just catching

**The delays to watch:**

- Quality improvements take time to show up in metrics
- Technical debt paydown feels unproductive short-term
- Pressure to ship will increase before benefits appear

The vicious cycles are dominating. Adding more QA is trying to bail out a sinking boat without fixing the leak.

---

## Integration

This skill pairs with:
- **leverage-point-analysis** - Find where to intervene in the loops
- **systems-archetype-recognition** - Match patterns to known archetypes
- **stock-flow-analysis** - Understand the accumulations driving loops

---

## Source Expert

Donella Meadows - `experts/donella-meadows/`