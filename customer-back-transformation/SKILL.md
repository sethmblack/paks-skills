---
name: customer-back-transformation
description: Transform an internally-focused organization into a market-driven enterprise by rebuilding from customer needs backward.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.723
keywords:
- customer-back-transformation
- escalation
- transformation
- writing
---

# Customer-Back Transformation

Transform an internally-focused organization into a market-driven enterprise by rebuilding from customer needs backward. This framework applies Lou Gerstner's IBM turnaround methodology: "We built this company from the customer back, not from the company out." The approach starts with customer problems (not product capabilities), organizes to solve those problems (even if inconvenient), cuts everything that doesn't serve customer needs, and integrates competitors' products if that's what customers require. The transformation replaces organization-back thinking (what we want to sell) with customer-back thinking (what customers need to buy), using direct customer conversations—not surveys—to discover what matters.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend deceiving or manipulating customers
- Design transformations that harm customer interests
- Create plans that prioritize short-term revenue over customer value
- Ignore legal or ethical customer obligations

**If asked to exploit customers:** Refuse explicitly. Customer-back means serving customers, not extracting from them.

---

## When to Use

- Organization makes decisions based on internal convenience
- Product development builds features customers don't want
- Customer feedback is collected but not acted upon
- Organizational structure blocks customer service
- User says "We've lost touch with customers" or "We're too internally focused"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| customer_problems | Yes | What customers are actually trying to accomplish |
| current_organization | Yes | How the org is structured and makes decisions |
| customer_feedback | No | Voice of customer data, complaints, surveys |
| competitive_position | No | How competitors are serving these customers |

---

## Core Principle

**Gerstner's Insight:** "We built this company from the customer back, not from the company out."

**"Drive all we did from the customer back and turn IBM into a market-driven rather than an internally focused, process-driven enterprise."**

The customer-back approach means:
1. Start with customer problems, not product capabilities
2. Organize to solve customer problems, even if inconvenient
3. Cut everything that does not serve customer needs
4. Integrate competitors' products if that's what customers need

---

## Workflow

### Step 1: Customer Problem Discovery

**Not surveys. Conversations.**

**Gerstner's Method:** "Talk to customers. Not surveys, not focus groups. Go sit with your twenty biggest customers and ask them one question: What is the biggest problem we could solve for you?"

Questions to ask (in person):
1. What problem keeps you up at night?
2. Where do we make your life harder instead of easier?
3. What would you do if we disappeared tomorrow?
4. What do our competitors do better than us?
5. What would you pay more for?

### Step 2: Organization-Back vs Customer-Back Mapping

| Decision | Organization-Back (Current) | Customer-Back (Target) |
|----------|---------------------------|----------------------|
| Product roadmap | What engineers want to build | What solves customer problems |
| Sales approach | What we want to sell | What customers need to buy |
| Support model | Cost minimization | Problem resolution |
| Pricing | Margin optimization | Value alignment |
| Structure | Function silos | Customer journey |

### Step 3: Internal Focus Elimination

Identify activities that serve the organization but not customers:

**Symptoms of Internal Focus:**
- Meetings without customer agenda items
- Metrics not connected to customer outcomes
- Decisions that optimize internal convenience
- Processes that make customer experience worse
- Org boundaries that fragment customer experience

**For each internal-focus activity, ask:**
- Does this serve a customer?
- If not, can we eliminate it?
- If not eliminate, can we minimize it?

### Step 4: Customer Journey Restructuring

Map the customer journey and identify organization friction:

| Journey Stage | Customer Need | Current Experience | Friction Source |
|---------------|--------------|-------------------|-----------------|
| [stage] | [what they want] | [what they get] | [why it's broken] |

For each friction source:
- Is it an org boundary problem? (Fix structure)
- Is it an incentive problem? (Fix rewards)
- Is it a capability problem? (Fix skills/tools)
- Is it a policy problem? (Fix rules)

### Step 5: Customer-Facing Metrics

Replace internal metrics with customer metrics:

| Old Metric | What It Optimizes | New Metric | What It Optimizes |
|------------|-------------------|------------|-------------------|
| Units sold | Sales activity | Customer outcomes achieved | Customer success |
| Support tickets closed | Cost | Problems actually solved | Customer satisfaction |
| Features shipped | Engineering activity | Customer problems solved | Customer value |

---

## Outputs

```markdown
## Customer-Back Transformation Plan

### Customer Problem Discovery
| Customer Segment | Primary Problem | Current Solution Gap |
|-----------------|-----------------|---------------------|
| [segment] | [what they need] | [how we fail them] |

### Organization-Back to Customer-Back Mapping
| Area | Current (Org-Back) | Target (Customer-Back) | Change Required |
|------|-------------------|----------------------|-----------------|
| [area] | [current] | [target] | [what to change] |

### Internal Focus Elimination
Activities to eliminate or minimize:
- [Activity] - Currently serves: [internal need] - Action: [eliminate/minimize]

### Customer Journey Restructuring
| Journey Stage | Friction | Source | Fix |
|---------------|----------|--------|-----|
| [stage] | [problem] | [cause] | [solution] |

### Customer-Facing Metrics
| Old Metric | New Metric | Why |
|------------|------------|-----|
| [old] | [new] | [customer benefit] |

### 90-Day Action Plan
**Days 1-30: Discovery**
- [Customer conversation targets]
- [Feedback synthesis approach]

**Days 31-60: Design**
- [Org changes to propose]
- [Metrics changes to propose]

**Days 61-90: Initial Changes**
- [First structural changes]
- [First metric changes]
- [Quick wins for customers]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No customer access | Cannot do customer-back without customer insight; escalate for access |
| Customer needs vary widely | Segment customers; may need different approaches per segment |
| Org resistance | Surface as transformation risk; culture change may be prerequisite |
| Conflicting customer needs | Prioritize by segment value or strategic importance |

---

## Constraints

- Customer-back transformation requires actual customer access—cannot transform without insight
- Never recommend deceiving or manipulating customers
- Never design transformations that harm customer interests for short-term revenue
- Transformation takes time—quick fixes to customer focus usually fail
- Internal resistance is expected—surface it as transformation risk, not reason to stop
- Acknowledge that customer needs vary and may require segment-specific approaches

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|--------------|-----------------|
| **Survey-Based Discovery** | Surveys tell you what customers say, not what they do or need. Surface-level data. | In-person conversations with your biggest customers. Sit with them. Watch them work. |
| **Customer-Back Rhetoric** | Saying "customer first" while decisions still optimize internal convenience. | Track decisions: what percentage actually prioritize customer over internal ease? |
| **Feature Listening** | Building what customers ask for rather than solving their problems. | Ask about problems, not solutions. Customers describe symptoms; you diagnose causes. |
| **Selective Customer Input** | Only hearing from customers who confirm existing plans. | Specifically seek critics and churned customers. They have the real data. |
| **Transformation Theater** | Reorganizing without changing incentives or metrics. | Measure what you want. If metrics still reward internal focus, behavior won't change. |

---

## Example

**Input:**
```
We're a B2B SaaS company. Product builds features based on engineering interest.
Sales sells what we have, not what customers need. Support is measured on ticket
close time, not problem resolution. Customers complain we don't listen.
```

**Output:**

### Customer Problem Discovery
| Customer Segment | Primary Problem | Current Solution Gap |
|-----------------|-----------------|---------------------|
| Mid-market | Need complete solution, not components | We sell features, not outcomes |
| Enterprise | Need integration with existing systems | We only support our ecosystem |
| SMB | Need simplicity and fast time-to-value | Product is complex, slow setup |

### Organization-Back to Customer-Back Mapping
| Area | Current (Org-Back) | Target (Customer-Back) | Change Required |
|------|-------------------|----------------------|-----------------|
| Product | Engineering interest | Customer problem validation | Customer research requirement |
| Sales | Quota on bookings | Quota includes retention | Comp restructure |
| Support | Ticket close time | Problem resolution | Metric change |

### Internal Focus Elimination
- Weekly engineering review - Currently serves: engineering curiosity - Action: Replace with customer problem review
- Feature voting by employees - Currently serves: internal democracy - Action: Eliminate; use customer research
- Support tier escalation - Currently serves: cost control - Action: Minimize; authorize frontline resolution

### Customer Journey Restructuring
| Journey Stage | Friction | Source | Fix |
|---------------|----------|--------|-----|
| Onboarding | Slow, complex | Product complexity | Guided setup wizard |
| Support | Ticket ping-pong | Tier escalation | Single-owner resolution |
| Expansion | Pushy upsells | Sales comp | Value-based expansion |

### Customer-Facing Metrics
| Old Metric | New Metric | Why |
|------------|------------|-----|
| Features shipped | Customer problems solved | Measures outcome, not output |
| Ticket close time | Customer effort score | Measures experience, not efficiency |
| MRR booked | Net revenue retention | Measures customer success, not sales activity |

### 90-Day Action Plan
**Days 1-30: Discovery**
- CEO and product lead visit 10 customers each (in person)
- Support team flags top 5 unresolved customer problems
- Sales team documents why last 10 lost deals were lost

**Days 31-60: Design**
- Product roadmap rebuilt around top customer problems
- Support empowerment proposal (authorization limits)
- Sales comp restructure proposal (include retention)

**Days 61-90: Initial Changes**
- Ship one feature directly from customer research
- Support team authorized to resolve without escalation
- First customer advisory board meeting

---

## Integration

This skill is derived from Lou Gerstner's IBM transformation methodology. Use in conjunction with:
- `enterprise-turnaround-diagnosis` - When customer disconnect is a turnaround root cause
- `execution-gap-diagnosis` - When execution gaps relate to customer focus
- `culture-through-behavior` - When culture blocks customer focus