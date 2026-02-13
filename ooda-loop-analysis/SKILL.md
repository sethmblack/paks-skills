---
name: ooda-loop-analysis
description: Analyze any competitive or conflictual situation through Boyd's Observe-Orient-Decide-Act framework to identify tempo advantages, decision bottlenecks, and opportunities to get inside the opponent'...
license: MIT
metadata:
  version: 1.0.4609
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- ooda-loop-analysis
- writing
---

# OODA Loop Analysis

Analyze any competitive or conflictual situation through Boyd's Observe-Orient-Decide-Act framework to identify tempo advantages, decision bottlenecks, and opportunities to get inside the opponent's decision cycle.

---

## When to Use

- Facing competition and need to understand decision dynamics
- Something feels slow but you can't identify why
- Want to understand how to outmaneuver rather than outspend
- Analyzing why you're losing despite having resources
- Need to accelerate organizational response time
- Request for "OODA analysis" of a competitive situation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | Description of the competitive or conflictual situation |
| parties | No | Key parties involved (will be inferred if not provided) |
| your_position | No | Your role or stake in the situation |

---

## The Four-Phase Framework

### Phase 1: Observe

Map each party's observation capabilities:
- **What can they see?** Information sources, sensors, feedback loops
- **What are they missing?** Blind spots, delayed information, filtered data
- **How fast do observations reach decision-makers?** Information latency

**Key questions:**
- Where is information getting filtered or delayed?
- What signals are being ignored or misinterpreted?
- Who has better situational awareness?

### Phase 2: Orient

Analyze the mental models shaping each party's interpretation:
- **What paradigms are they operating from?** Assumptions, beliefs, frameworks
- **What's their orientation based on?** Experience, culture, doctrine, recent events
- **Where is orientation misaligned with reality?** Outdated models, blind spots

**Boyd's insight:** "Orientation is the schwerpunkt. It shapes the way we observe, the way we decide, the way we act."

**Key questions:**
- What do they believe that isn't true anymore?
- What successful past experience is now misleading them?
- Where does their mental model diverge from reality?

### Phase 3: Decide

Examine each party's decision-making process:
- **How are decisions made?** Process, approvals, stakeholders
- **What's the decision latency?** Time from awareness to decision
- **What constrains decisions?** Politics, risk aversion, consensus requirements

**Key questions:**
- How many nodes does a decision pass through?
- Where do decisions get stuck or watered down?
- What decisions can they make implicitly vs. explicitly?

### Phase 4: Act

Assess each party's action capabilities:
- **What can they actually do?** Capabilities, resources, authorities
- **How fast can they act?** Execution speed, mobilization time
- **What constrains action?** Resources, coordination, dependencies

**Key questions:**
- How quickly does decision translate to action?
- What actions can happen without explicit decision (implicit guidance)?
- Where are execution bottlenecks?

---

## Tempo Analysis

After mapping each party's OODA loop, assess:

### Cycle Time
How long for each party to complete one full OODA cycle?

### Inside vs. Outside
Who is operating inside whose loop? The party with the faster cycle can act while the opponent is still processing their previous action.

### Acceleration Opportunities
Where can your OODA cycle be compressed?
- Better observation (earlier signals, faster information flow)
- Better orientation (more accurate mental models, faster reorientation)
- Faster decisions (fewer approval nodes, more implicit guidance)
- Faster action (better execution capabilities, pre-positioned resources)

### Disruption Opportunities
Where can the opponent's OODA cycle be disrupted?
- Degrade their observation (information denial, deception)
- Attack their orientation (unexpected moves that don't fit their model)
- Slow their decisions (present dilemmas, create uncertainty)
- Impede their actions (interfere with execution, force redirections)

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
## OODA Loop Analysis

### Situation Summary
[2-3 sentence restatement of the competitive dynamic]

### Your OODA Cycle
| Phase | Capability | Bottleneck | Cycle Time Estimate |
|-------|------------|------------|---------------------|
| Observe | ... | ... | ... |
| Orient | ... | ... | ... |
| Decide | ... | ... | ... |
| Act | ... | ... | ... |

### Opponent's OODA Cycle
| Phase | Capability | Bottleneck | Cycle Time Estimate |
|-------|------------|------------|---------------------|
| Observe | ... | ... | ... |
| Orient | ... | ... | ... |
| Decide | ... | ... | ... |
| Act | ... | ... | ... |

### Tempo Assessment
**Who's inside whose loop:** [Assessment]
**Key tempo advantage/disadvantage:** [Specific dynamic]

### Recommendations

**To accelerate your cycle:**
1. [Specific recommendation for observation improvement]
2. [Specific recommendation for orientation improvement]
3. [Specific recommendation for decision speed]
4. [Specific recommendation for action speed]

**To disrupt opponent's cycle:**
1. [Specific recommendation targeting their weakest phase]
2. [Action that will force re-orientation]

### The Boyd Challenge
[End with a sharp question or challenge in Boyd's voice]
```

---

## Constraints

- Focus on tempo and decision dynamics, not just capabilities
- Don't assume faster is always better - orientation accuracy matters
- Identify implicit vs. explicit decision paths
- Be specific about WHERE in the loop problems exist
- Remember: the goal is to operate inside their loop, not just be fast

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

**Input:** "We're a fintech startup competing with traditional banks for small business lending. We can approve loans in 24 hours but they have more capital and brand recognition. How do we think about this competition?"

**Output:**

## OODA Loop Analysis

### Situation Summary
A fintech startup with superior decision speed competes against established banks with superior resources and trust. The competitive dynamic hinges on whether speed can overcome incumbency before resources overwhelm agility.

### Your OODA Cycle
| Phase | Capability | Bottleneck | Cycle Time Estimate |
|-------|------------|------------|---------------------|
| Observe | Real-time application data, digital signals | Limited market feedback at scale | Hours |
| Orient | Modern risk models, market-native team | Unproven in stress scenarios | Hours |
| Decide | Flat structure, algorithm-assisted | Risk committee for edge cases | Hours to 1 day |
| Act | Automated disbursement, digital delivery | Capital constraints | 24 hours |

### Opponent's OODA Cycle (Traditional Banks)
| Phase | Capability | Bottleneck | Cycle Time Estimate |
|-------|------------|------------|---------------------|
| Observe | Branch network, relationship data | Legacy systems, siloed data | Days |
| Orient | Decades of credit experience | Outdated models, institutional inertia | Slow to update |
| Decide | Mature frameworks | Multiple approval layers, committee cycles | 1-4 weeks |
| Act | Massive capital, trusted brand | Legacy processes, compliance overhead | Days to weeks |

### Tempo Assessment
**Who's inside whose loop:** You are operating far inside the bank's decision cycle. By the time they've decided on a customer, you've already served them and moved on.

**Key tempo advantage:** Your 24-hour cycle vs. their 2-4 week cycle means you can serve 14-28 customers in the time they serve one. But their orientation (credit experience) may be more accurate in edge cases.

### Recommendations

**To accelerate your cycle:**
1. **Observe:** Build real-time feedback loops from funded loans to refine signals faster
2. **Orient:** Continuously stress-test models against bank default data; your orientation must stay accurate as you scale
3. **Decide:** Expand the automated decision envelope; reduce cases requiring committee
4. **Act:** Secure additional capital facilities so capital doesn't become the bottleneck

**To disrupt opponent's cycle:**
1. Target their orientation: The market segments they've written off as "too risky" or "too small" are gaps. Prove these segments are profitable and they'll be forced to re-orient their entire small business strategy
2. Force decision paralysis: When you serve their customers faster, they face a choice between speeding up (breaking their process) or losing share (breaking their targets). Either way, you've disrupted their loop.

### The Boyd Challenge
You have tempo. But tempo without accurate orientation leads to accelerated failure. The question isn't "can you move fast?" - you can. The question is: "Is your orientation valid when the credit cycle turns?" If you don't know, you're not cycling through OODA - you're just moving fast in a direction you haven't validated. Fix that.

---

## Integration

This skill is part of the **John Boyd** expert persona. Use it when you need to understand competitive dynamics through the lens of decision speed and tempo rather than just resource comparison.