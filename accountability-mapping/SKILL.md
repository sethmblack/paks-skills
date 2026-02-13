---
name: accountability-mapping
description: Establish clear individual ownership with measurable deliverables for initiatives, eliminating diffuse responsibility.
license: MIT
metadata:
  version: 1.0.3330
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- accountability-mapping
- escalation
- writing
---

# Accountability Mapping

Establish clear individual ownership with measurable deliverables for initiatives, eliminating diffuse responsibility.

**Token Budget:** ~500 tokens. Reserve tokens for mapping output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create accountability structures that enable scapegoating
- Assign accountability without corresponding authority
- Recommend structures that violate labor laws or policies
- Design accountability to punish rather than enable

**If asked to assign blame:** Redirect to assigning ownership for future success.

---

## When to Use

- User asks "Who owns this?"
- User asks "Accountability is unclear"
- User asks "Map accountability"
- User asks "No one seems responsible"
- Projects are stalling without clear ownership
- Multiple people claim partial responsibility
- Failures occur and "everyone was responsible"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **initiative** | Yes | The project, goal, or outcome requiring accountability |
| **current_roles** | Yes | People involved and their current responsibilities |
| **desired_outcomes** | Yes | What success looks like, specifically |
| **constraints** | No | Organizational limitations, reporting structures, etc. |

---

## The Core Principle

**"If everyone's responsible, no one is responsible."**

Diffuse accountability is worse than no accountability. When many people share responsibility, no one truly owns outcomes. The result: problems persist, decisions stall, and blame spreads without resolution.

---

## The Single Owner Rule

Every deliverable must have **one named individual** accountable for its completion.

| Concept | Definition |
|---------|-----------|
| **Accountability** | The buck stops here. This person answers for success or failure. |
| **Responsibility** | Contributing to the work. Multiple people can be responsible. |
| **Informed** | Needs to know status. Not responsible or accountable. |
| **Consulted** | Provides input. Not responsible or accountable. |

**A deliverable can have:**
- One accountable owner (required)
- Multiple responsible contributors (optional)
- Multiple informed stakeholders (optional)
- Multiple consulted advisors (optional)

**A deliverable cannot have:**
- Multiple accountable owners
- Zero accountable owners
- "The team" as accountable

---

## Workflow

### Step 1: Define Measurable Deliverables

Break the initiative into specific, measurable outcomes:

| Bad | Good |
|-----|------|
| "Improve customer experience" | "Reduce call wait time to under 2 minutes" |
| "Launch the product" | "Ship v1.0 to production by March 15" |
| "Increase sales" | "Close $500K in new ARR by Q2" |

### Step 2: Assign Single Owners

For each deliverable:
1. Name one individual (not a team, not "leadership")
2. Confirm they have authority to deliver
3. Confirm they accept ownership

| Deliverable | Owner | Authority Check |
|-------------|-------|-----------------|
| {specific outcome} | {single name} | {can they actually do this?} |

### Step 3: Define Measurement

For each owner:
- What metric indicates success?
- What is the deadline?
- How will progress be tracked?
- What review cadence applies?

### Step 4: Establish Escalation

When an owner cannot deliver:
1. Who do they escalate to?
2. What triggers escalation?
3. How quickly must escalation occur?

### Step 5: Document and Communicate

Create a visible accountability map that everyone can reference.

---

## Output Format

```markdown
## Accountability Map

**Initiative:** {name}
**Date Established:** {date}
**Overall Accountable:** {single person for initiative-level accountability}

### Deliverable Ownership

| Deliverable | Owner | Metric | Deadline | Review Cadence |
|-------------|-------|--------|----------|----------------|
| {specific outcome 1} | {name} | {how measured} | {date} | {weekly/biweekly/etc.} |
| {specific outcome 2} | {name} | {how measured} | {date} | {weekly/biweekly/etc.} |

### Escalation Protocol

| Trigger | Owner Action | Escalate To | Timeframe |
|---------|--------------|-------------|-----------|
| Blocked for 48+ hours | Escalate immediately | {name} | Same day |
| Metric trending red | Flag at review | {name} | Next review |
| Deadline at risk | Escalate with options | {name} | 1 week before |

### RACI Summary

| Deliverable | Accountable | Responsible | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| {outcome 1} | {1 name} | {names} | {names} | {names} |
| {outcome 2} | {1 name} | {names} | {names} | {names} |

### Acceptance

{List of owners who have confirmed acceptance of their accountability}
```

---

## Common Mistakes to Avoid

| Mistake | Problem | Fix |
|---------|---------|-----|
| "The team owns this" | No individual accountability | Name one person |
| Co-ownership | Responsibility diffuses | Pick the primary owner |
| Owner lacks authority | Cannot actually deliver | Grant authority or reassign |
| Vague deliverables | Cannot measure success | Define specific metrics |
| No deadline | Work expands indefinitely | Set hard dates |
| No escalation path | Problems fester | Define triggers and paths |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No one willing to own | Escalate to leadership; this is a structural problem |
| Owner lacks authority | Document authority gap; recommend resolution before proceeding |
| Overlapping initiatives | Map dependencies; clarify which owner has authority over shared resources |
| Deliverables too vague | Work with stakeholders to define measurable outcomes |
| Resistance to single ownership | Explain the principle; "If everyone's responsible, no one is responsible" |

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

**Input:** Product launch with marketing, engineering, and sales all "responsible" for success

**Output:**

### Deliverable Ownership

| Deliverable | Owner | Metric | Deadline |
|-------------|-------|--------|----------|
| Product ready for release | Sarah Chen (Eng Lead) | All P0 bugs resolved, QA passed | March 1 |
| Launch campaign live | Marcus Johnson (Marketing Dir) | All channels activated | March 5 |
| Sales team trained | Lisa Park (Sales Enablement) | 100% certification complete | March 1 |
| 50 demos scheduled | Tom Wilson (Sales Dir) | 50 confirmed meetings | March 15 |
| Launch go/no-go decision | Sarah Chen (Eng Lead) | Final sign-off | March 4 |

**Note:** Previously "the launch team" was responsible. Now each critical deliverable has one name. When something slips, we know exactly who to talk to - not to blame, but to understand and support.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's principle that diffuse accountability ensures failure. When invoked by the Dimon expert, outputs should maintain his insistence on clear, individual ownership.

**Related skills:** leadership-quality-filter, operational-trench-audit