---
name: single-point-accountability-design
description: Design accountability structures where one person owns every aspect of an outcome - every trade-off, every decision, every result.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4987
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- single-point-accountability-design
- transformation
- writing
---

# Single-Point Accountability Design

Design accountability structures where one person owns every aspect of an outcome - every trade-off, every decision, every result.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create accountability structures that enable individual misconduct without oversight
- Remove all checks and balances from high-risk decisions
- Design accountability that concentrates power without corresponding responsibility
- Eliminate collaborative input in favor of dictatorial authority

**If asked to remove all oversight:** Refuse explicitly. Single-point accountability means one owner, not one unchecked autocrat.

---

## When to Use

- Projects stall because "no one owns this"
- Decisions take too long due to committee structures
- Responsibility is diffused across multiple stakeholders
- People can veto but no one can approve
- Outcomes are blamed on "the team" with no individual ownership
- Trade-offs are avoided because no one has authority to make them

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **initiative_description** | Yes | What outcome needs an owner |
| **current_structure** | Yes | Who is involved now; how decisions are made |
| **stakeholder_map** | Yes | Who has input, who is affected, who currently decides |
| **decision_bottlenecks** | No | Where decisions get stuck |
| **authority_gaps** | No | Where people have responsibility without authority |

---

## Core Philosophy

Mary Barra's Chief Engineer Model:

> "Every vehicle has its own chief engineer, and it's single-point accountability. I have seen a real transformation in just the short few months since we've made that change."

The principle: **Diffused accountability is no accountability.**

When everyone owns something, no one owns it. When no one can make trade-offs, trade-offs do not get made. When outcomes are "the team's" responsibility, no individual wakes up at 3am thinking about how to fix it.

---

## Workflow
### Step 1: Phase 1: Outcome Definition

**1.1 Define the Outcome Clearly**
- What is the specific result this owner will be accountable for?
- How will success be measured?
- What is the scope boundary?

**1.2 Identify Trade-Off Authority**
- What decisions will this owner need to make?
- What trade-offs are inherent in this outcome?
- What conflicts will need resolution?

### Step 2: Phase 2: Owner Selection

**2.1 Selection Criteria**
The owner must have:
- Deep knowledge of the domain
- Ability to understand all trade-offs
- Willingness to own outcomes (not just activities)
- Credibility with stakeholders
- Sufficient seniority for the scope

**2.2 Authority Definition**
Define explicitly:
- What can this owner decide unilaterally?
- What requires consultation (input) but not approval?
- What requires escalation?
- What resources does this owner control?

### Step 3: Phase 3: Structure Design

**3.1 Remove Competing Accountability**
- Identify who else currently "owns" pieces of this outcome
- Clarify their new role (input, resource, constraint - but not owner)
- Dissolve committees that share ownership of this outcome

**3.2 Establish Input Channels**
- Who provides input to the owner?
- How is input gathered? (The owner decides how, not stakeholders)
- Input is welcome; veto is not

**3.3 Define Escalation**
- What does the owner escalate and to whom?
- What triggers escalation?
- Escalation does not mean shared accountability

### Step 4: Phase 4: Implementation

**4.1 Public Announcement**
- Announce the owner clearly to all stakeholders
- Explain the authority and scope
- Redirect questions and decisions to the owner

**4.2 Protection**
- Shield the owner from end-runs
- Redirect those who try to bypass the owner
- Back the owner's decisions publicly

**4.3 Review Cadence**
- How often does the owner report on progress?
- What does success look like at checkpoints?
- When and how is the owner evaluated?

---

## Outputs

| Output | Format | Purpose |
|--------|--------|---------|
| Owner Selection | Name + rationale | Clear accountability assignment |
| Authority Charter | Decision matrix | Define what owner controls |
| RACI Clarification | Updated stakeholder roles | Remove competing accountability |
| Escalation Protocol | Triggers and paths | Handle exceptions |
| Communication Plan | Announcement + redirects | Establish new structure |

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


## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| "Co-owners" | Diffusion disguised as collaboration | One name. Period. |
| "Owner with steering committee" | Owner has no real authority | Owner decides; committee advises |
| "Owner subject to consensus" | Veto power everywhere | Consultation, not approval |
| "Rotating ownership" | No one owns it for long enough | Stable ownership through completion |
| "Owner without resources" | Responsibility without authority | Authority includes resources |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No one wants to own it | Either the outcome is not important, or the organization has an accountability culture problem |
| Multiple people qualified | Pick one; second-best owner is better than shared ownership |
| Owner lacks some expertise | Owner can get input; lack of expertise does not require shared ownership |
| Stakeholders resist losing control | This is expected; hold the line on single-point accountability |
| Owner fails | Owner is accountable; address owner performance, do not revert to committee |

---

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
```
Initiative: New product launch (software platform)
Current structure: Product committee (5 people), Engineering lead, Marketing lead, Sales lead - all "co-own" the launch
Stakeholders: Product, Engineering, Marketing, Sales, Support, Finance, Legal
Bottleneck: Feature prioritization takes 3 weeks due to committee debate
Authority gap: No one can say "no" to feature requests
```

**Output:**

## Single-Point Accountability Design

### Owner Assignment
**Launch Owner:** Product Lead (Sarah Chen)

**Rationale:** Deepest understanding of customer needs and trade-offs; can make product decisions with engineering input; has credibility across functions.

### Authority Charter

| Decision Type | Authority Level |
|---------------|----------------|
| Feature prioritization | Sarah decides (Engineering input) |
| Launch timing | Sarah decides (Sales input) |
| Resource allocation within budget | Sarah decides |
| Budget changes >10% | Escalate to VP |
| Legal/compliance requirements | Constraint (Legal defines, Sarah incorporates) |

### RACI Clarification

| Stakeholder | Old Role | New Role |
|-------------|----------|----------|
| Product Committee | Co-owner | Dissolved; members become advisors |
| Engineering Lead | Co-owner | Responsible for delivery; Sarah defines what |
| Marketing Lead | Co-owner | Input on positioning; Sarah decides priorities |
| Sales Lead | Co-owner | Input on timing; Sarah decides launch date |
| Support | Stakeholder | Input on supportability requirements |
| Finance | Approver | Constraint provider (budget); not approver |
| Legal | Approver | Constraint provider (compliance); not approver |

### Key Changes
1. **Feature prioritization:** Sarah decides in 48 hours, not 3 weeks
2. **"No" authority:** Sarah can say no to feature requests without committee approval
3. **Trade-offs:** Sarah makes them explicitly; stakeholders provide input

### Communication
"Effective immediately, Sarah Chen owns the platform launch. All decisions about scope, timing, and priorities go through Sarah. Provide your input to Sarah; she will decide. If you disagree with a decision, discuss with Sarah. If unresolved, Sarah escalates to me."

---

## Integration

This skill is derived from Mary Barra's Chief Engineer model at GM, where each vehicle has one owner who understands every trade-off and owns every outcome.

Use in conjunction with:
- `bureaucracy-simplification` when accountability redesign reveals policy complexity
- `crisis-to-culture-change` when crisis reveals diffuse responsibility

---

## Success Criteria

Accountability design is successful when:
- [ ] One name is publicly identified as owner
- [ ] Owner has authority matching responsibility
- [ ] Competing accountability is dissolved
- [ ] Decision speed improves measurably
- [ ] Trade-offs are made explicitly by owner
- [ ] Escalation path is clear but rarely used
- [ ] Owner wakes up at 3am thinking about the outcome