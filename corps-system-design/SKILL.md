---
name: corps-system-design
description: Design organizational structures that balance autonomy with coordination,
  allowing parallel action and rapid concentration.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- corps-system-design
- escalation
- writing
---

# Corps System Design

Design organizational structures that balance autonomy with coordination, allowing parallel action and rapid concentration.

---

## When to Use

- Designing organizational structure
- Need both flexibility and coordination
- Current structure is too centralized or too fragmented
- Scaling an organization while maintaining agility
- User asks "How should I structure my organization?" or "I need flexibility and coordination"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| organization | Yes | The team, company, or group being structured |
| objectives | No | What the organization needs to accomplish |
| constraints | No | Size, resources, geographic distribution |
| current_problems | No | Issues with existing structure |

---

## Workflow
Napoleon's corps system revolutionized military organization. Each corps (15,000-30,000 soldiers) was self-sufficient, containing infantry, cavalry, and artillery. Corps could march independently yet combine rapidly for battle.

This created unprecedented operational flexibility: the army could cover more ground, adapt to circumstances, and concentrate overwhelming force at the decisive moment.

### Step 1: The Problem the Corps System Solves

**Too centralized:**
- Bottlenecks at the top
- Slow adaptation to local conditions
- Over-reliance on single leader
- Cannot scale beyond leader's attention span

**Too decentralized:**
- No coordination when needed
- Duplicate efforts
- Cannot mass for decisive action
- Fragmented strategy

**The corps solution:**
- Autonomous units that can act independently
- Clear coordination mechanisms for combined action
- Self-sufficiency eliminates constant support requirements
- Shared mission creates alignment without constant communication

### Step 2: The Four Principles

#### 1. Self-Sufficiency
Each unit has everything needed to operate independently for a defined period.

**In military terms:** Infantry, cavalry, artillery, supplies
**In organizational terms:** Complete capability to deliver value without dependencies

**Questions to test self-sufficiency:**
- Can this unit accomplish its mission without waiting on others?
- What cross-unit dependencies exist? Can they be internalized?
- How long can this unit operate before needing central support?

#### 2. Clear Mission Alignment
Units operate toward the same strategic objective even without communication.

**In military terms:** All corps understand the campaign goal; they can make decisions consistent with overall strategy
**In organizational terms:** Clear strategic intent that guides autonomous decisions

**Questions to test alignment:**
- If communication were cut, would units make consistent decisions?
- Does each unit understand the "why" behind the strategy?
- Can a unit leader explain how their work serves the whole?

#### 3. Rapid Concentration
When decisive action is needed, units can combine quickly.

**In military terms:** Corps march separately, fight together; diamond formation allows any direction of concentration
**In organizational terms:** Teams can temporarily combine capabilities for major initiatives

**Questions to test concentration:**
- How quickly can units combine for a critical initiative?
- What coordination mechanisms exist for rapid assembly?
- Can you mass organizational force at a decisive point?

#### 4. Economy of Coordination
Coordinate only when necessary; default to autonomous operation.

**In military terms:** Corps don't need permission for local decisions; only strategic moves require coordination
**In organizational terms:** Teams don't escalate routine decisions; only cross-cutting issues require centralization

**Questions to test coordination economy:**
- What requires central approval? Can that list be shortened?
- Are teams waiting on each other unnecessarily?
- Does coordination add value or just add time?

---

## The Design Process

### Step 1: Define the Unit of Autonomy

What is the right size for a self-sufficient unit?
- Large enough to have complete capability
- Small enough to be cohesive and fast
- Typically 5-15 people in modern organizations

### Step 2: Determine Self-Sufficiency Requirements

What capabilities must each unit contain?
- What functions are needed to deliver value?
- Which capabilities can be shared? Which must be embedded?
- What resources does each unit control?

### Step 3: Establish Strategic Alignment Mechanisms

How do units stay aligned without constant coordination?
- Mission and strategy communication
- Shared metrics and goals
- Cultural norms and principles
- Regular (but infrequent) strategic sync points

### Step 4: Design Concentration Protocols

How do units combine when needed?
- What triggers concentration (types of initiatives)?
- Who decides when to concentrate?
- What does temporary combination look like?
- How do units return to autonomous operation?

### Step 5: Minimize Coordination Requirements

What can be removed from central coordination?
- Default to unit autonomy
- Escalate only what truly requires it
- Reduce approval chains
- Trust units to make local decisions

---

## Output Format

```markdown
## Corps System Design

### Organization Overview
- **Current state:** [How it's structured now]
- **Key challenges:** [What problems exist]
- **Strategic objectives:** [What success looks like]

### The Corps Structure

#### Unit Definition
- **Unit size:** [Number of people per autonomous unit]
- **Unit count:** [How many units total]
- **Unit naming:** [How units are identified]

#### Self-Sufficiency Package
Each unit contains:
| Capability | How Embedded | Rationale |
|------------|--------------|-----------|
| [Function 1] | [Dedicated/Fractional/Shared] | [Why this choice] |

#### Alignment Mechanisms
- **Mission cascade:** [How strategy reaches units]
- **Shared metrics:** [What all units track]
- **Cultural principles:** [Decision-making norms]
- **Sync cadence:** [How often units align]

#### Concentration Protocols
- **Triggers:** [What causes units to combine]
- **Decision authority:** [Who calls concentration]
- **Combination mechanics:** [How it works]
- **Duration norms:** [How long combinations last]

#### Coordination Minimization
- **Unit authority:** [What units decide alone]
- **Escalation criteria:** [What goes up]
- **Approval chains:** [What's been eliminated]

### Migration Path
1. [Step to move from current to target state]
2. [Step to move from current to target state]
3. [Step to move from current to target state]

### The Napoleonic Maxim
[Relevant quote or principle]
```

---

## Constraints

- Never create units that cannot operate independently for meaningful periods
- Never design coordination mechanisms that become bottlenecks
- Never assume communication will always flow; design for communication failures
- Never forget that the goal is effectiveness, not organizational elegance

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

**Input:** "We're a 50-person software company with a traditional structure: Engineering, Product, Design, Sales, Marketing, Support. Projects require constant coordination between teams. Decisions take forever because everything needs multiple approvals. How should we restructure?"

**Output:**

## Corps System Design

### Organization Overview
- **Current state:** Functional silos (Engineering, Product, Design, Sales, Marketing, Support); matrix coordination for projects
- **Key challenges:** Decision latency from cross-functional dependencies; no single owner for customer outcomes; specialists protecting territory rather than serving mission
- **Strategic objectives:** Ship faster, respond to customers better, reduce coordination overhead

### The Corps Structure

#### Unit Definition
- **Unit size:** 6-8 people per autonomous unit
- **Unit count:** 5 product squads + 2 support functions (Platform, GTM)
- **Unit naming:** Squads named by customer outcome (e.g., "Onboarding Squad," "Enterprise Squad")

#### Self-Sufficiency Package
Each product squad contains:
| Capability | How Embedded | Rationale |
|------------|--------------|-----------|
| Engineering (2-3) | Dedicated | Core delivery capability |
| Product (1) | Dedicated | Decision authority for scope |
| Design (0.5-1) | Dedicated or strong embed | User experience ownership |
| Analytics | Shared platform | Not enough work for dedicated |
| Customer contact | Direct access | Squad owns relationship with customer segment |

Support functions:
- **Platform squad:** Shared infrastructure, DevOps, security
- **GTM squad:** Sales, marketing, customer success (coordinates across product squads)

#### Alignment Mechanisms
- **Mission cascade:** Quarterly OKRs set company direction; squads define their contribution; monthly all-hands shares progress
- **Shared metrics:** ARR, NPS, deployment frequency visible to all
- **Cultural principles:** "Own the outcome, not the task"; "Ask forgiveness, not permission"; "Ship beats perfection"
- **Sync cadence:** Weekly 30-min cross-squad sync (updates only, no decisions); quarterly strategy day

#### Concentration Protocols
- **Triggers:** Major product launches; critical customer escalations; platform emergencies
- **Decision authority:** CPO can call concentration; squad leads can volunteer
- **Combination mechanics:** Affected squads pause normal work; single owner appointed; daily standups until resolution
- **Duration norms:** 2-week maximum for concentration events; then squads return to normal operation

#### Coordination Minimization
- **Unit authority:** Squads decide their roadmap within OKR targets; ship without approval; hire within budget; set their own processes
- **Escalation criteria:** Cross-squad dependencies requiring resource reallocation; strategy changes; budget exceptions
- **Approval chains:** Eliminated: design reviews, code reviews for shipping, feature prioritization approvals, tooling decisions

### Migration Path
1. **Week 1-2:** Define squads and assign people; communicate clearly that this is how we work now
2. **Week 3-4:** Each squad establishes their mission, metrics, and first sprint; platform squad identifies shared services
3. **Week 5-8:** Operate in new structure with training wheels (daily cross-squad sync, available escalation support)
4. **Week 9+:** Reduce training wheels; move to weekly sync; trust the system

### The Napoleonic Maxim
"The whole art of war consists in getting at what is on the other side of the hill." In a traditional structure, every team waits to see what every other team will do. In a corps structure, each unit can act on what it sees directly, trusting that others are doing the same. The army that moves fastest wins - and that army marches in independent columns that can concentrate when it matters.

---

## Integration

This skill is part of the **Napoleon Bonaparte** expert persona. Use it when designing organizations that need both autonomy and coordination.