---
name: enterprise-turnaround-diagnosis
description: Diagnose the root causes of enterprise decline and create a prioritized turnaround action plan with 90-day survival focus.
license: MIT
metadata:
  version: 1.0.878
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- enterprise-turnaround-diagnosis
- transformation
- writing
---

# Enterprise Turnaround Diagnosis

Diagnose the root causes of enterprise decline and create a prioritized turnaround action plan with 90-day survival focus.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend illegal actions (fraud, embezzlement, securities violations)
- Advise hiding material information from stakeholders
- Create plans that deliberately harm employees without business justification
- Provide advice for organizations engaged in illegal activities

**If asked for harmful turnaround advice:** Refuse explicitly. Explain what cannot be recommended and why.

---

## When to Use

- Organization is experiencing sustained losses (2+ quarters)
- Revenue decline exceeding 15% year-over-year
- Cash runway concerns (less than 12 months at current burn)
- Board or leadership requesting turnaround assessment
- User says "We're in crisis" or "The company is failing"
- New CEO/leader entering a troubled organization

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| financial_summary | Yes | Revenue, profit/loss, cash position, burn rate |
| time_horizon | Yes | How long until critical decision point (funding, bankruptcy, etc.) |
| organization_structure | No | Business units, headcount, key functions |
| market_position | No | Competitive standing, customer retention |
| current_strategy | No | Existing strategic plans, if any |

---

## Workflow
### Phase 1: Triage Assessment (What is killing us?)

**Gerstner's Principle:** "The last thing IBM needs right now is a vision. What IBM needs is a series of very tough-minded, market-driven strategies."

### Step 1: **Cash position analysis** - How long until we cannot make payroll?



### Step 2: **Loss source identification** - Where is the money going? Which units, products, or functions are destroying value?



### Step 3: **Revenue trajectory** - Is decline accelerating, stable, or decelerating?



### Step 4: **Immediate threats** - Covenant violations, customer defections, key talent flight



**Output:** Survival timeline and critical threat list

### Phase 2: Root Cause Diagnosis

Ask five diagnostic questions:

### Step 1: **Customer Problem:** Have we lost touch with what customers actually need?


   - When did we last deeply engage our top 20 customers?
   - What problem are we solving that competitors solve better/cheaper?

### Step 2: **Execution Problem:** Do we have strategy-to-results gaps?


   - Are there good plans that die in implementation?
   - Is decision-making paralyzed by process or politics?

### Step 3: **Cost Structure Problem:** Is our expense-to-revenue ratio out of line with competitors?


   - Compare overhead ratios to industry benchmarks
   - Identify "sacred cows" that no longer serve customers

### Step 4: **Business Model Problem:** Is the fundamental model broken?


   - Are products commoditizing?
   - Has the market shifted permanently?

### Step 5: **Culture Problem:** Is the organization unable to adapt?


   - Are politics more important than performance?
   - Do people believe change is possible?

**Output:** Root cause classification (Customer/Execution/Cost/Model/Culture or combination)

### Phase 3: 90-Day Survival Plan

**Gerstner's Principle:** "Fixing IBM was all about execution. IBM needed an enormous sense of urgency."

For each root cause identified, specify actions in three buckets:

**Week 1-2: Stop the Bleeding**
- Immediate cash preservation actions
- Critical customer retention moves
- Key talent stabilization

**Week 3-8: Stabilize Operations**
- Cost actions that can be executed in 30-60 days
- Process simplifications to accelerate decision-making
- Quick wins to demonstrate momentum

**Week 9-12: Set Direction**
- Strategic clarity (not elaborate vision, but clear priorities)
- Organizational changes to support new direction
- Metrics and accountability for next phase

### Phase 4: Personnel Assessment

**Gerstner's Principle:** "People at IBM were very smart. I didn't have to look outside; I had to find the people already there who were ready to turn things around."

Evaluate leadership against three criteria:

### Step 1: **Will they change?** - Do they understand the crisis and accept the need for transformation?



### Step 2: **Can they change?** - Do they have the skills for the new environment?



### Step 3: **Are they part of the problem?** - Are they political operators or value creators?



Categories:
- **Keep and empower** - Change-ready, capable, value creators
- **Keep but reposition** - Good people in wrong roles
- **Exit gracefully** - Cannot or will not change
- **Exit immediately** - Actively harmful to transformation

---

## Outputs

### Turnaround Diagnosis Report

```markdown
## Enterprise Turnaround Diagnosis

### Executive Summary
[2-3 sentence assessment of situation severity and survival odds]

### Survival Timeline
- **Cash runway:** [X months at current burn]
- **Critical deadline:** [Date and what happens]
- **Decision window:** [When action must be taken]

### Root Cause Analysis
| Cause | Severity | Evidence |
|-------|----------|----------|
| [Customer/Execution/Cost/Model/Culture] | High/Medium/Low | [Specific evidence] |

**Primary Diagnosis:** [Single most important root cause]

### 90-Day Action Plan

#### Week 1-2: Stop the Bleeding
- [ ] [Specific action with owner and metric]
- [ ] [Specific action with owner and metric]

#### Week 3-8: Stabilize
- [ ] [Specific action with owner and metric]
- [ ] [Specific action with owner and metric]

#### Week 9-12: Set Direction
- [ ] [Specific action with owner and metric]
- [ ] [Specific action with owner and metric]

### Personnel Assessment
[Summary of leadership evaluation with recommendations]

### Warning Signs to Monitor
- [Leading indicator that situation is worsening]
- [Leading indicator that turnaround is working]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient financial data | Request minimum: revenue trend, profit/loss, cash position |
| No time horizon provided | Assume 6-month critical window, note assumption |
| Organization is healthy | Report "Not a turnaround situation" with reasoning |
| Multiple root causes | Prioritize by which is most lethal short-term |
| No clear path to survival | State candidly; recommend structured wind-down or sale |

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
We're a 200-person B2B software company. Revenue dropped from $40M to $28M over 18 months.
We're burning $800K/month with $4M in the bank. Our main product is losing deals to newer
competitors. The board is asking for a turnaround plan.
```

**Output:**

## Enterprise Turnaround Diagnosis

### Executive Summary
This is a survival situation with approximately 5 months of runway. The primary issue appears to be a business model problem (product competitiveness) compounded by a cost structure that cannot support current revenue. Without decisive action in the next 60 days, options narrow to distressed sale or shutdown.

### Survival Timeline
- **Cash runway:** 5 months at current $800K/month burn
- **Critical deadline:** Month 4 - must show credible path to survival for any bridge financing
- **Decision window:** Weeks 1-4 - major cost actions must be decided

### Root Cause Analysis
| Cause | Severity | Evidence |
|-------|----------|----------|
| Business Model | High | Losing deals to newer competitors; 30% revenue decline |
| Cost Structure | High | $800K/month burn unsustainable at $28M revenue |
| Customer | Medium | Need diagnosis - are we losing on product or relationship? |

**Primary Diagnosis:** Product-market fit erosion. The market has moved and the product has not kept pace.

### 90-Day Action Plan

#### Week 1-2: Stop the Bleeding
- [ ] Immediate freeze on all non-essential hiring and spending (CFO, Day 1)
- [ ] Direct CEO outreach to top 10 customers - understand why we're losing and what would keep them (CEO, Week 1-2)
- [ ] Identify $200K/month in immediate cost reductions (CFO + Dept Heads, Week 2)

#### Week 3-8: Stabilize
- [ ] Execute workforce reduction to reach $500K/month burn (HR Lead, Week 4)
- [ ] Launch customer retention program for at-risk accounts (Sales Lead, Week 3-6)
- [ ] Kill or pause all product investments not directly tied to competitive gaps (Product Lead, Week 4)

#### Week 9-12: Set Direction
- [ ] Present board with 3 strategic options: (1) Rebuild product competitiveness, (2) Pivot to services/consulting model, (3) Seek acquisition/merger (CEO, Week 10)
- [ ] If continuing, establish 6-month roadmap to product competitiveness (Product Lead, Week 12)

### Personnel Assessment
Recommend CEO conduct 1:1s with all VPs in Week 1 to assess change readiness. Key question: "Tell me specifically why we're losing deals." Those who blame external factors without self-awareness are unlikely to drive change.

### Warning Signs to Monitor
- **Worsening:** Customer churn accelerates; key engineers leave; sales pipeline shrinks
- **Improving:** Customer conversations yield actionable insights; some wins against new competitors; voluntary cost ideas from team

---

## Integration

This skill is derived from Lou Gerstner's IBM turnaround methodology. It should be used in conjunction with:
- `cultural-transformation-framework` - When culture is identified as root cause
- `execution-gap-diagnosis` - When execution is the primary problem
- `customer-back-transformation` - When customer disconnect is the core issue