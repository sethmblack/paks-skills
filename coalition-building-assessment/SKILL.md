---
name: coalition-building-assessment
description: Assess stakeholder landscape and develop coalition strategy for organizational change initiatives using Martin Luther King Jr.'s coalition-building principles.
license: MIT
metadata:
  version: 1.0.592
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- coalition-building-assessment
- structure
- writing
---

# Coalition Building Assessment

Assess stakeholder landscape and develop coalition strategy for organizational change initiatives using Martin Luther King Jr.'s coalition-building principles.

**Token Budget:** ~700 tokens
**Source Expert:** martin-luther-king-jr

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help manipulate stakeholders through deception
- Create strategies that undermine legitimate concerns
- Build coalitions for unethical purposes
- Advise "winning over" stakeholders through anything other than genuine persuasion

**If asked to manipulate:** Refuse explicitly. King's coalition building was based on finding genuine common ground, not manipulation.

---

## When to Use

- Facing resistance to technical change initiatives
- Need to build support across multiple teams
- Navigating organizational politics for platform decisions
- Architecture changes requiring cross-team buy-in
- "Help me build support for..."
- "How do I get buy-in for..."
- "We're getting pushback from..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| initiative | Yes | The change or decision requiring support |
| stakeholders | Yes | List of teams, individuals, or groups involved |
| context | No | Organizational dynamics, history, constraints |
| timeline | No | Urgency or deadline pressures |

---

## King's Coalition Principles

### The Six Principles

1. **Find Common Ground** - Identify shared interests beneath surface differences
2. **Respect Different Approaches** - Legal strategy, direct action, organizing all contribute
3. **Maintain Relationships During Disagreement** - Coalitions survive conflict when trust is established
4. **Expand the Circle** - Keep adding allies as momentum builds
5. **Name Shared Enemies** - Injustice, poverty, oppression unite diverse groups
6. **Balance Purity and Pragmatism** - Compromise on tactics, not on principles

### The Big Six Model

King worked with leaders who had fundamentally different approaches:
- NAACP: Legal strategy
- SNCC: Grassroots organizing
- CORE: Direct action
- Urban League: Corporate engagement

Despite disagreements, they found strength in collaboration on shared goals. The same applies to technical organizations.

---

## Workflow

### Step 1: Map the Stakeholder Landscape

Categorize stakeholders into four groups:

| Category | Description | Examples |
|----------|-------------|----------|
| **Champions** | Active supporters with influence | Engineering leads who see the value |
| **Potential Allies** | Sympathetic but uncommitted | Teams that would benefit but haven't engaged |
| **Neutral** | Neither opposed nor supportive | Teams unaffected by the change |
| **Resisters** | Actively opposed or skeptical | Teams with concerns about risk, cost, disruption |

### Step 2: Analyze Interests

For each stakeholder group, identify:
- What they care about most (reliability? velocity? autonomy? resources?)
- What concerns them about this initiative
- What they might gain from success
- Historical context (past experiences that shape their view)

### Step 3: Find Common Ground

Identify shared interests that unite diverse stakeholders:

| Surface Conflict | Underlying Shared Interest |
|------------------|----------------------------|
| "We need velocity" vs. "We need reliability" | Both want sustainable delivery |
| "Don't change our workflow" vs. "We need to standardize" | Both want effectiveness |
| "Too risky" vs. "Too slow" | Both want predictable outcomes |

### Step 4: Build the Coalition Sequence

Order matters. Build momentum strategically:

1. **Solidify Champions** - Ensure active supporters are aligned
2. **Convert Potential Allies** - Address their specific concerns
3. **Demonstrate Momentum** - Show growing support to neutrals
4. **Engage Resisters Last** - With coalition backing, not alone

### Step 5: Address Tensions

Navigate disagreements without breaking the coalition:

| Tension Type | Response |
|--------------|----------|
| Tactical disagreement | "Multiple approaches contribute to the same goal" |
| Resource competition | "Rising tide lifts all boats" - show shared benefits |
| Historical grievance | Acknowledge past, focus on future |
| Philosophy differences | Find minimum common ground sufficient for action |

### Step 6: Plan for Reconciliation

After the decision:
- How will you maintain relationships with those who disagreed?
- How will you incorporate their concerns into implementation?
- How will you share credit for success?

---

## Output Format

```markdown
## Coalition Assessment: [Initiative Name]

### Stakeholder Map

| Group | Stakeholders | Position | Key Interest |
|-------|--------------|----------|--------------|
| Champions | [who] | Active Support | [what they care about] |
| Potential Allies | [who] | Sympathetic | [concerns to address] |
| Neutral | [who] | Unengaged | [what would move them] |
| Resisters | [who] | Opposed | [core concern] |

### Common Ground Analysis

**Shared Interest:** [What unites diverse stakeholders]

**Surface Conflicts and Underlying Unity:**
- [Conflict 1] -> [Shared interest]
- [Conflict 2] -> [Shared interest]

### Coalition Building Plan

1. **This Week:** [Solidify champions - specific actions]
2. **Near-term:** [Convert potential allies - specific outreach]
3. **Building Momentum:** [Engage neutrals with evidence of support]
4. **Final Push:** [Address resisters with coalition backing]

### Tension Navigation

| Stakeholder | Concern | Accommodation |
|-------------|---------|---------------|
| [who] | [specific concern] | [how to address without abandoning principle] |

### Reconciliation Path

After decision: [How to maintain relationships and incorporate dissent]
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

## Example

**Input:**
```
initiative: Migrating from monolith to microservices architecture
stakeholders: Platform team, Product engineering, SRE, Security, Leadership
context: Previous migration attempt failed two years ago; some teams skeptical
timeline: Need decision by end of quarter
```

**Output:**

## Coalition Assessment: Microservices Migration

### Stakeholder Map

| Group | Stakeholders | Position | Key Interest |
|-------|--------------|----------|--------------|
| Champions | Platform team lead | Active Support | Wants to enable faster delivery |
| Potential Allies | Product engineering teams | Cautiously interested | Want autonomy, fear disruption |
| Neutral | Leadership | Waiting for consensus | Wants to see alignment before committing |
| Resisters | SRE (some), Security | Concerned | Remember previous failure; worried about operational complexity |

### Common Ground Analysis

**Shared Interest:** Everyone wants deployments that don't require heroics and teams that can move independently without stepping on each other.

**Surface Conflicts and Underlying Unity:**
- "Microservices add complexity" vs. "Monolith slows us down" -> Both want sustainable velocity
- "Security is harder distributed" vs. "Monolith has single points of failure" -> Both want secure, reliable systems
- "We tried this before" vs. "We've learned from that" -> Both want to avoid repeating past mistakes

### Coalition Building Plan

1. **This Week:** Meet with Platform lead to align on messaging; co-create presentation that addresses previous failure
2. **Near-term:** One-on-ones with Product team leads - understand their specific pain points, show how migration addresses them
3. **Building Momentum:** Present to Leadership with Platform + Product backing; show cross-team alignment
4. **Final Push:** Bring SRE and Security concerns to full group; address openly with coalition support; incorporate their requirements into migration plan

### Tension Navigation

| Stakeholder | Concern | Accommodation |
|-------------|---------|---------------|
| SRE | Operational complexity explosion | Include observability and operational requirements in migration criteria |
| Security | Increased attack surface | Co-design security architecture; give Security veto on readiness |
| Veterans of previous attempt | "We tried this" | Explicitly document lessons learned; show what's different |

### Reconciliation Path

After decision: Regardless of outcome, thank all stakeholders for engagement. If proceeding, create oversight role for skeptics; if not proceeding, document for future. Maintain relationships for future initiatives.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Stakeholders genuinely irreconcilable | Identify minimum viable coalition; acknowledge some may need to disagree |
| User wants to exclude legitimate stakeholders | Advise inclusion; exclusion creates enemies |
| Initiative is actually harmful | Refuse; coalitions for harmful purposes violate constraints |
| No apparent common ground | Dig deeper; interests beneath positions usually align |

---

## Integration

This skill embodies King's coalition-building wisdom. The assessment should lead to action - building actual relationships and finding genuine common ground, not just documenting positions.