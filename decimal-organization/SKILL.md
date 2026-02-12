---
name: decimal-organization
description: Design organizational structures using simple, scalable units with clear
  accountability at each level.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- decimal-organization
- structure
- writing
---

# Decimal Organization

Design organizational structures using simple, scalable units with clear accountability at each level.

**Source Expert:** Genghis Khan
**Category:** Organizational Design / Scaling

---

## When to Use

- Building a new organization or team structure
- Scaling an existing organization
- Accountability is unclear or decisions are slow
- Communication breaks down as the organization grows
- Restructuring after acquisition or merger
- Spans of control have become unmanageable

**Trigger Phrases:**
- "How should I structure this?"
- "How do we scale?"
- "The organization is too complex"
- "Accountability is unclear"
- "Decisions take too long"
- "Who's responsible for what?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `organization_size` | Yes | Current or target size |
| `core_function` | Yes | What the organization does |
| `current_problems` | No | Specific structural issues |
| `constraints` | No | Fixed requirements (geography, regulations, etc.) |

---

## Workflow
### Step 1: The Mongol Decimal System

Genghis Khan reorganized all of Mongol society using a decimal structure that enabled coordination of hundreds of thousands across vast distances:

| Unit | Size | Commander | Accountability |
|------|------|-----------|----------------|
| Arban | 10 | Arban-u darga | Each member accountable; if one flees, all punished |
| Zuun | 100 | Zuun-u darga | Commands 10 arbans |
| Mingghan | 1,000 | Mingghan-u noyan | Commands 10 zuuns |
| Tumen | 10,000 | Tumen-u noyan | Commands 10 mingghans |

**Key Innovation:** Tribal loyalties were deliberately broken by mixing members from different tribes into the same units. Loyalty transferred from tribe to unit to Khan.

### Step 2: Framework

**1. Determine the Base Unit**
What is your "arban" - the smallest self-sufficient team? This unit should be:
- Small enough for everyone to know each other
- Large enough to accomplish meaningful work
- Self-contained for daily operations
- Accountable as a group for outcomes

Typical base units: 5-10 people for knowledge work, 8-12 for operations.

**2. Establish Clear Spans of Control**
Each leader should command a consistent number of units (ideally 5-10). If a leader manages 20 direct reports, communication degrades. If they manage 2, you've created unnecessary hierarchy.

**3. Make Each Level Self-Sufficient**
Each level should be able to operate autonomously for routine matters. The arban doesn't need the tumen's permission for daily decisions. Only escalate when the scope exceeds the unit's authority.

**4. Single Accountability at Each Level**
Every unit has ONE person accountable. Not a committee. Not shared leadership. One person who answers for outcomes.

**5. Break Old Loyalties**
If existing tribal/departmental/team loyalties interfere with the new structure, mix people deliberately. Loyalty should be to the new unit and the mission, not to old affiliations.

**6. Consistent Rules Across All Levels**
The same standards apply to every unit at every level. The prince follows the same rules as the shepherd. Consistency creates predictability and trust.

---

## Output Format

```markdown
## Organizational Structure: [Organization Name]

### Base Unit (Arban Equivalent)
- **Size:** [X people]
- **Function:** [What this unit does independently]
- **Leader:** [Title/role]
- **Accountability:** [What they own]

### Structure Levels

| Level | Size | Units Per Leader | Leader Title | Scope |
|-------|------|------------------|--------------|-------|
| 1 | X | - | [Title] | [Scope] |
| 2 | X*Y | Y | [Title] | [Scope] |
| 3 | X*Y*Z | Z | [Title] | [Scope] |

### Decision Authority by Level
- **Level 1 decides:** [Routine matters]
- **Level 2 decides:** [Cross-unit coordination]
- **Level 3 decides:** [Strategic/resource allocation]

### Loyalty Transfer Required
[What old affiliations need to be broken; how new unit loyalty will be built]

### Accountability Rules
[What happens when a unit fails; how performance is measured]
```

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

**Input:**
- Organization size: Growing from 50 to 200 engineers
- Core function: Software development
- Current problems: Product teams siloed, no clear ownership, decisions require too many meetings
- Constraints: Must maintain some specialization (frontend, backend, data)

**Output:**

## Organizational Structure: Engineering Organization

### Base Unit (Arban Equivalent)
- **Size:** 6-8 engineers
- **Function:** End-to-end feature ownership for one product area
- **Leader:** Tech Lead (senior IC, not people manager)
- **Accountability:** Ship velocity, code quality, on-call for their domain

### Structure Levels

| Level | Size | Units Per Leader | Leader Title | Scope |
|-------|------|------------------|--------------|-------|
| Squad | 6-8 | - | Tech Lead | Feature area |
| Tribe | 30-40 | 5 squads | Engineering Manager | Product domain |
| Division | 100 | 2-3 tribes | Director | Major product line |
| Org | 200 | 2 divisions | VP Engineering | All engineering |

### Decision Authority by Level
- **Squad decides:** Technical approach, sprint priorities, code review standards
- **Tribe decides:** Cross-squad dependencies, hiring for their domain, quarterly goals
- **Division decides:** Architecture standards, resource allocation across tribes, promotions
- **VP decides:** Strategy, org structure changes, senior hiring, budget

### Loyalty Transfer Required
Old affiliations to break:
- "I'm a frontend engineer" -> "I'm on the Checkout squad"
- "Backend team" -> Dissolved; backend engineers distributed to product squads
- Specialists report to product leaders, not functional leaders

Build new loyalty through:
- Squads eat lunch together weekly
- Tribe-level wins celebrated together
- On-call rotation creates mutual dependence
- Performance measured at squad level, not individual

### Accountability Rules
- Squad ships or doesn't ship - measured together
- If a squad consistently underperforms, Tech Lead replaced first
- No individual heroics; if one person is carrying the team, structure is wrong
- On-call failures are squad accountability

---

## Anti-Patterns

**DON'T:**
- Create units too large for genuine relationships (>12)
- Create units too small to accomplish meaningful work (<4)
- Allow multiple people to be "accountable" for the same thing
- Let old tribal loyalties persist over new unit loyalty
- Create special rules for senior people
- Build hierarchy deeper than necessary

**STRUCTURAL DEBT SIGNS:**
- "We need a meeting to decide who decides"
- "I'm not sure who owns that"
- "We have to coordinate with 6 teams to ship anything"
- "The director has 25 direct reports"
- "That team is really just one person"

---

## The Simplicity Test

> "If you cannot explain the structure in one minute, it is too complex."

The Mongol decimal system could be explained to any soldier in moments. Modern organizations should aim for similar clarity. If org charts require legends and footnotes, the structure is failing.

---

## Integration

This skill pairs with:
- **Merit Assessment:** Selecting the right people for each leadership level
- **Talent Absorption:** Integrating acquired teams into the structure
- **Lead from the Front:** Leaders at each level model expected behavior