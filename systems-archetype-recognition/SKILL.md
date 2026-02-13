---
name: systems-archetype-recognition
description: Recognize common system patterns (archetypes) that produce predictable dynamics. Enable faster diagnosis by matching current situations to well-understood structures with proven intervention strate...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2045
keywords:
- escalation
- systems-archetype-recognition
- writing
---

# Systems Archetype Recognition

Recognize common system patterns (archetypes) that produce predictable dynamics. Enable faster diagnosis by matching current situations to well-understood structures with proven intervention strategies.

---

## When to Use

- When a situation feels familiar but you can't quite name it
- When fixes keep backfiring
- When success creates its own problems
- When competition spirals out of control

**Trigger Phrases:**
- "This pattern seems familiar"
- "We've seen this before"
- "The fix made things worse"
- "Success is creating new problems"
- "It's a race to the bottom"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The problem or pattern observed |
| history | No | How it developed |
| symptoms | No | Current manifestations |

---

## The Core Archetypes

### 1. Fixes That Fail

**Pattern:** A quick fix alleviates symptoms but creates side effects that eventually make the original problem worse.

**Structure:**
```
Problem → Quick Fix → Symptom Relief (short-term)
                ↓
         Side Effects → Worsened Problem (long-term)
```

**Examples:**
- Pesticides kill pests but create resistant strains
- Pain medication masks symptoms, allowing injury to worsen
- Firefighting in code creates technical debt

**Warning Signs:**
- "We've fixed this before"
- Problems recur, often worse
- Increasing dependency on the fix

**Intervention:**
- Address root cause, not symptoms
- If quick fix necessary, set a sunset date
- Monitor for side effects

---

### 2. Shifting the Burden

**Pattern:** A symptomatic solution is used instead of a fundamental solution. Over time, the capacity to implement the fundamental solution atrophies.

**Structure:**
```
Problem → Symptomatic Solution → Symptom Relief
                ↓
         Atrophy of Fundamental Solution Capacity
```

**Examples:**
- Outsourcing to contractors instead of building internal capability
- Debt to cover expenses instead of reducing costs
- Heroic efforts instead of fixing the process

**Warning Signs:**
- Increasing dependence on the workaround
- Declining ability to solve root problem
- "We couldn't survive without [the symptomatic solution]"

**Intervention:**
- Invest in fundamental solution while maintaining short-term
- Rebuild atrophied capabilities
- Plan the transition explicitly

---

### 3. Limits to Growth

**Pattern:** A reinforcing growth process hits a constraint that slows, stops, or reverses the growth.

**Structure:**
```
Growth → More Success → More Growth (reinforcing)
                ↓
         Constraint Engaged → Slowing/Stopping Condition (balancing)
```

**Examples:**
- Market saturation
- Resource depletion
- Infrastructure bottlenecks
- Organizational complexity

**Warning Signs:**
- Growth slowing despite effort
- Same tactics producing less results
- Emerging bottlenecks or constraints

**Intervention:**
- Identify the limiting factor before hitting it
- Remove or expand the constraint
- Redefine success in sustainable terms

---

### 4. Tragedy of the Commons

**Pattern:** Individuals acting in their own interest deplete a shared resource, harming everyone including themselves.

**Structure:**
```
Individual Gain → More Use → Resource Depletion → Harm to All
                           ↓
                 Each Individual: "But MY use is small..."
```

**Examples:**
- Overfishing, overgrazing, pollution
- Traffic congestion (road is the commons)
- Shared budget overruns
- Technical debt in shared codebases

**Warning Signs:**
- "Everyone else is doing it"
- Shared resource degrading
- Individual gains, collective loss

**Intervention:**
- Make the commons visible
- Align individual incentives with collective welfare
- Privatize the commons (if possible) or regulate access

---

### 5. Escalation

**Pattern:** Two or more parties respond to each other's actions in ways that amplify both, creating a spiral.

**Structure:**
```
Party A Acts → Party B Perceives Threat → Party B Responds
                                              ↓
         Party A Perceives Threat ← Party A Responds (escalated)
```

**Examples:**
- Arms races
- Price wars
- Political polarization
- Feature wars between competitors

**Warning Signs:**
- "We had to respond to what they did"
- Mutual escalation
- Original purpose lost in competition

**Intervention:**
- Unilateral de-escalation (risky but effective)
- Negotiated cease-fire
- Change the metric of success
- Introduce a ceiling or limit

---

### 6. Success to the Successful

**Pattern:** Winners get more resources to win more, while losers get less resources and fall further behind.

**Structure:**
```
Winner Succeeds → Winner Gets More Resources → Winner Succeeds More
        ↕
Loser Struggles → Loser Gets Less Resources → Loser Struggles More
```

**Examples:**
- Wealth concentration
- Network effects (rich get richer)
- Star systems in organizations
- Platform monopolies

**Warning Signs:**
- Growing inequality
- "The best get the best opportunities"
- Compounding advantage/disadvantage

**Intervention:**
- Redistribute resources periodically
- Create separate arenas for competition
- Invest in leveling mechanisms
- Question whether inequality serves the whole

---

### 7. Growth and Underinvestment

**Pattern:** Growth approaches a limit that could be expanded by investment, but the investment is delayed or never made, causing growth to stall.

**Structure:**
```
Growth → Approaches Capacity → Performance Declines
                                    ↓
         Excuse to Not Invest ← "See, growth is slowing anyway"
```

**Examples:**
- Infrastructure that can't keep up with growth
- Training not provided because "we're too busy"
- Maintenance deferred until breakdown

**Warning Signs:**
- "We can't afford to invest right now"
- Performance declining despite effort
- Capacity constraints treated as permanent

**Intervention:**
- Invest before the constraint bites
- Don't confuse capacity-limited performance with fundamental limits
- Invest in cycles, not at crises

---

## The Diagnosis Protocol

### Step 1: Describe the Behavior

What pattern are you seeing?
- Recurring problems that get fixed and return
- Declining performance despite effort
- Escalating conflict or competition
- Growing inequality
- Resource depletion

### Step 2: Match to Archetype

Compare your situation to the archetype structures:
- Which loops are present?
- Which dynamics match?
- Multiple archetypes can be present simultaneously

### Step 3: Test the Match

Does the archetype predict:
- What's happened so far?
- What will happen if unchanged?
- Why previous interventions failed?

### Step 4: Apply Known Interventions

Each archetype has proven intervention strategies. Apply or adapt them.

### Step 5: Monitor for Other Archetypes

Solving one archetype can create another. Watch for new patterns emerging.

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
| Archetype identification | Which pattern(s) apply |
| Structure diagram | Loops and dynamics mapped |
| Predicted trajectory | What happens if unchanged |
| Known interventions | Proven strategies for this pattern |
| Warning signs | What to watch for |

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

- Do not recommend approaches beyond stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Verify recommendations are implementable before suggesting them
- Consider maintainability and long-term implications

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

**User:** "We used to have great team culture. But our best performers started leaving because they felt held back by slower colleagues. So we gave top performers more resources and opportunities. Now the gap is huge—superstars get everything, everyone else is demoralized and leaving."

**Systems Archetype Recognition response:**

This is a clear case of **Success to the Successful**.

**The structure in your situation:**
```
Top performers succeed →
  Get more resources/opportunities →
    Succeed more, grow faster →
      Gap widens →
        Others demoralized, leave →
          Fewer resources for remaining non-stars →
            They fall further behind
```

You created a reinforcing loop that amplifies initial differences. What started as a retention strategy for top performers became a sorting mechanism that drives out everyone else.

**Predicted trajectory if unchanged:**
- Top performers become indispensable (single points of failure)
- Middle performers leave or check out
- Culture becomes competitive rather than collaborative
- New hires can't compete with established stars
- Eventually stars leave for new challenges (nothing left to prove here)

**Why this archetype is tricky:**

The initial logic seems sound: reward your best people. But the archetype shows that differential investment doesn't just reward—it compounds. The gap doesn't stay fixed; it grows.

**Known interventions for Success to the Successful:**

1. **Create separate arenas:** Let different people succeed at different things. Not everyone needs to compete on the same dimension.

2. **Invest in the middle:** The highest-leverage investment isn't in people who will succeed anyway—it's in people who could succeed with support.

3. **Redistribute periodically:** Rotate opportunities. Give stretch assignments to developing talent, not just proven performers.

4. **Question the metric:** What makes someone a "top performer"? If it's individual output, you're missing collaboration. If it's visibility, you're missing the people who make others better.

5. **Watch for the flip:** Eventually your stars will be hired away by someone offering them fresh challenges. Then you'll have neither stars nor developed middle.

**The cultural lever:**

What you're really deciding is: what kind of organization are you? A star system where a few elites carry the load? Or a development system where many people grow? Both can work. But you can't accidentally slide from one to the other and expect the culture to survive.

---

## Integration

This skill pairs with:
- **feedback-loop-mapping** - See the loops that create the archetype
- **leverage-point-analysis** - Find where to intervene
- **stock-flow-analysis** - Understand the accumulations that create momentum

---

## Source Expert

Donella Meadows - `experts/donella-meadows/`