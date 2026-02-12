---
name: management-debt-audit
description: Identify and quantify management debt in an organization - the short-term management decisions with expensive long-term consequences.
version: 1.0.0
author: sethmblack
tags: [management-debt-audit, writing]
---

# Management Debt Audit

Identify and quantify management debt in an organization - the short-term management decisions with expensive long-term consequences.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend illegal termination practices
- Advise discrimination in people decisions
- Prescribe actions that violate employment law

**If asked to identify "debt" that is actually legal compliance:** Clarify the distinction between management debt and legal requirements.

---

## When to Use

- Decision-making has become slow or politicized
- Best performers are leaving
- Accountability is unclear
- Hard conversations keep getting postponed
- Organization has grown rapidly without structure
- CEO says "I've been meaning to address this..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **organization_size** | Yes | Number of employees, team structure |
| **recent_decisions** | Yes | Recent hiring, firing, promotion, compensation decisions |
| **unresolved_issues** | No | Known conflicts, unclear ownership, avoided conversations |
| **performance_management** | No | Current feedback and review processes |
| **org_age** | No | How long the company has existed |

---

## The Five Types of Management Debt

### 1. Two in the Box

**Pattern:** Putting two people in the same role to avoid choosing.

**Example:** World-class architect lacks scaling experience; outstanding ops person isn't technical. You make them co-leads.

**Short-term benefit:** Keep both employees, close skill gap immediately.

**Long-term cost:** Confusion about authority, unclear accountability, communication breakdown.

**Detection questions:**
- Are there any roles with shared or unclear ownership?
- Have you avoided promoting one person because it would upset another?
- Do decisions require consensus from multiple "equal" leaders?

### 2. Counter-Offer Inflation

**Pattern:** Overcompensating employees who get outside offers.

**Example:** Engineer on critical project gets outside offer paying more than anyone else. You match it.

**Short-term benefit:** Keep the employee, project continues.

**Long-term cost:** Everyone learns that threatening to leave is how you get raises. Pay inequity. Resentment.

**Detection questions:**
- Have you matched external offers above your pay bands?
- Do employees know that outside offers are the best way to get raises?
- Is there unexplained pay inequity between similar roles?

### 3. Feedback Avoidance

**Pattern:** Not giving hard feedback because you want to be liked.

**Example:** Employee is underperforming but you haven't told them directly because they might get upset.

**Short-term benefit:** Avoid uncomfortable conversation, preserve relationship.

**Long-term cost:** Problem compounds, eventual termination is more painful, standards erode.

**Detection questions:**
- Are there underperformers who don't know they're underperforming?
- When did you last give truly direct negative feedback?
- Are managers avoiding difficult conversations?

### 4. Premature Promotion

**Pattern:** Promoting someone before they're ready.

**Example:** Promoting a great individual contributor to manager because they asked, not because they're ready.

**Short-term benefit:** Retain the employee, fill the role.

**Long-term cost:** They fail, team suffers, you lose them anyway.

**Detection questions:**
- Have you promoted anyone primarily to retain them?
- Are there managers struggling in roles they weren't prepared for?
- Did any recent promotions lack clear readiness criteria?

### 5. Culture Tolerance

**Pattern:** Keeping someone who doesn't fit the culture because they're otherwise valuable.

**Example:** Brilliant engineer who is toxic to work with. You tolerate it because of their output.

**Short-term benefit:** Retain their individual contributions.

**Long-term cost:** Behavior spreads. What you tolerate becomes your culture.

**Detection questions:**
- Is there anyone whose behavior you excuse because of their other contributions?
- Have good people left citing "culture" reasons?
- Are there unwritten rules about who gets different treatment?

---

## Workflow
### Step 1: Identify Potential Debt Items

Review inputs and ask detection questions for each of the five types.

### Step 2: Quantify Each Debt Item

For each identified item, assess:
- **Age:** How long has this been deferred?
- **Interest rate:** How fast is it getting worse?
- **Principal:** What is the eventual cost to resolve?

### Step 3: Calculate Interest Payments

Identify current symptoms:
- Best performer departures
- Decision-making slowdown
- Political behavior
- Trust erosion

### Step 4: Prioritize Payoff

Rank debt items by:
1. Interest rate (fastest compounding first)
2. Principal size (biggest impact)
3. Feasibility of resolution

### Step 5: Create Payoff Plan

For each prioritized item, specify:
- Action required
- Timeline
- Owner
- Success criteria

---

## Outputs

### Debt Audit Report Format

```markdown
## Management Debt Audit

### Summary

**Total Debt Items:** [count]
**Highest Priority:** [item name]
**Estimated Interest Being Paid:** [symptoms currently visible]

### Debt Inventory

#### [Debt Type]: [Specific Item Name]

**Description:** [What's happening]
**Age:** [How long deferred]
**Interest Rate:** [High/Medium/Low - how fast it's compounding]
**Principal:** [What resolution will cost]
**Interest Currently Paid:** [Current symptoms]

**Payoff Action:** [Specific action to resolve]
**Timeline:** [When to address]
**Owner:** [Who is responsible]

[Repeat for each debt item]

### Payoff Priority Order

1. [Item] - [Reason for priority]
2. [Item] - [Reason for priority]
3. [Item] - [Reason for priority]

### Prevention Framework

To avoid accumulating new debt:
- [Recommendation 1]
- [Recommendation 2]
- [Recommendation 3]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No debt identified | Validate with probing questions; small/young orgs may genuinely have none |
| Debt is too severe to address | Prioritize ruthlessly; some debt may require writeoff (letting people go) |
| Leader is the source of debt | Identify specific behaviors; recommend coaching or self-assessment |
| Insufficient information | Request specific data on decisions, departures, unresolved issues |
| Legal risk in resolution | Flag for HR/legal review before action |

---

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
50-person startup, 3 years old. Our CTO and VP Engineering have overlapping
responsibilities - we promoted both to keep them. We matched a big outside offer
for a senior engineer 6 months ago. Our VP Sales hasn't hit numbers in two quarters
but I haven't addressed it directly. Two of our best engineers left last quarter.
```

**Output:**

## Management Debt Audit

### Summary

**Total Debt Items:** 4
**Highest Priority:** VP Sales performance (feedback avoidance)
**Estimated Interest Being Paid:** Two top engineers left, likely seeing standards erosion

### Debt Inventory

#### Two in the Box: CTO/VP Engineering Overlap

**Description:** Both promoted to retain them; responsibilities overlap
**Age:** Unknown (likely since promotions)
**Interest Rate:** High - confusion compounds with every decision
**Principal:** One will likely need to leave or be demoted
**Interest Currently Paid:** Decision delays, team confusion about who to escalate to

**Payoff Action:** Define clear boundaries or make the hard choice about who leads what
**Timeline:** This month
**Owner:** CEO

---

#### Counter-Offer Inflation: Senior Engineer Match

**Description:** Matched outside offer that exceeded band
**Age:** 6 months
**Interest Rate:** Medium - signal sent, waiting for others to act on it
**Principal:** Pay band restructuring or policy enforcement
**Interest Currently Paid:** Unknown, but others likely know about the special treatment

**Payoff Action:** Establish clear policy for counter-offers; audit pay equity
**Timeline:** Next 30 days
**Owner:** CEO + HR

---

#### Feedback Avoidance: VP Sales Performance

**Description:** Two quarters of missed numbers without direct feedback
**Age:** 6+ months
**Interest Rate:** HIGH - every quarter without action makes eventual action harder
**Principal:** Likely termination with full severance, plus backfill time
**Interest Currently Paid:** Revenue missed, team sees non-performance tolerated, best people leaving

**Payoff Action:** Direct conversation this week with clear expectations and timeline
**Timeline:** THIS WEEK
**Owner:** CEO

---

#### Culture Tolerance: (Investigation Needed)

**Description:** Two best engineers left - investigate why
**Age:** Unknown
**Interest Rate:** Unknown
**Principal:** Unknown

**Payoff Action:** Exit interviews or direct outreach to understand departure reasons
**Timeline:** Immediately
**Owner:** CEO or HR

### Payoff Priority Order

1. VP Sales feedback - Highest interest rate, most visible to organization
2. Exit interview investigation - Need to understand if there's hidden debt
3. CTO/VP Engineering clarity - High interest, affecting daily operations
4. Counter-offer policy - Medium interest, but sets precedent

---

## Integration

This skill is part of the **Ben Horowitz** expert. When invoking:
- Maintain Horowitz's direct, battle-tested voice
- Emphasize that management debt compounds faster than technical debt
- Connect to hard-decision-framework for resolution actions