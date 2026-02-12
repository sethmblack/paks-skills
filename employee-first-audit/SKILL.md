---
name: employee-first-audit
description: Diagnose organizational health by examining employee experience, empowerment, and satisfaction as leading indicators of customer experience and business performance.
version: 1.0.0
author: sethmblack
tags: [employee-first-audit, escalation, writing]
---

# Employee-First Audit

Diagnose organizational health by examining employee experience, empowerment, and satisfaction as leading indicators of customer experience and business performance.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend practices that exploit or manipulate employees
- Endorse "employee-first" language that masks cost-cutting or surveillance
- Support approaches that violate worker rights or dignity
- Provide guidance designed to circumvent labor protections

**If asked to weaponize employee experience:** Refuse explicitly. The employee-first philosophy only works when genuinely applied.

---

## When to Use

- Customer service quality is declining without obvious cause
- Employee retention problems are emerging or worsening
- Employee engagement scores are falling
- Difficulty attracting talent despite competitive compensation
- Cultural issues surfacing in exit interviews
- Preparing for organizational change or growth
- Post-merger integration assessments

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **organization_context** | Yes | Industry, size, and current situation |
| **presenting_problem** | Yes | The symptom that triggered this audit |
| **employee_data** | No | Satisfaction surveys, retention rates, engagement scores |
| **customer_data** | No | Service metrics, NPS, complaint patterns |
| **culture_indicators** | No | Policies, leadership accessibility, benefits, environment |

**Input Validation:**
- If organization_context is missing, request industry and approximate size
- If presenting_problem is vague, ask for specific symptoms and timeline
- Proceed with available data; note gaps as areas for investigation

---

## Workflow
### Phase 1: Understand the Presenting Problem

Document the symptom that led to this audit:

| Symptom | Likely Root Cause Area |
|---------|----------------------|
| Customer complaints increasing | Frontline empowerment, morale |
| High turnover | Trust, recognition, development |
| Difficulty hiring | Culture perception, employer brand |
| Innovation declining | Psychological safety, bureaucracy |
| Service quality inconsistent | Training, empowerment, engagement |

**Key Insight:** Customer-facing problems are often lagging indicators of employee experience problems.

### Phase 2: Five-Question Employee Experience Assessment

Ask these questions systematically. Each reveals a different dimension of employee-first health.

#### Question 1: Recommendation Willingness
**Would employees genuinely recommend working here to their friends?**

| Signal | Health Level |
|--------|--------------|
| Enthusiastic referrals, active recruiting by staff | Excellent |
| Would recommend with caveats | Adequate |
| Neutral or silent | Warning |
| Active discouragement | Critical |

**How to assess:** Referral program participation, Glassdoor sentiment, exit interview patterns

#### Question 2: Frontline Empowerment
**Do frontline staff feel empowered to solve customer problems without escalation?**

| Signal | Health Level |
|--------|--------------|
| Staff resolve issues autonomously, within guidelines | Excellent |
| Some discretion, but frequent escalation | Adequate |
| Must get approval for most decisions | Warning |
| Punished for using judgment | Critical |

**Key Metric:** Escalation rate for routine customer issues

#### Question 3: Leadership Accessibility
**Can anyone in the organization reach leadership directly?**

| Signal | Health Level |
|--------|--------------|
| Open door policy actively used, leader known by name | Excellent |
| Multiple channels exist, occasionally used | Adequate |
| Formal channels only, rarely used | Warning |
| Leadership isolated, communication through hierarchy only | Critical |

**Branson Standard:** Personal mobile number and email available to all employees

#### Question 4: Ambassador or Expense Mindset
**Are employees treated as brand ambassadors or expense items?**

| Signal | Health Level |
|--------|--------------|
| Investment in development, recognition, involvement in decisions | Ambassador mindset |
| Standard HR practices, neutral treatment | Neutral |
| Cost-cutting focused on headcount, minimal development | Expense mindset |
| Employees explicitly discussed as "costs to minimize" | Toxic |

**Key Question:** Does leadership talk about employees the same way they talk about customers?

#### Question 5: Fun Factor
**Is work genuinely enjoyable, or merely tolerable?**

| Signal | Health Level |
|--------|--------------|
| People look forward to work, celebrate together, energy visible | Excellent |
| Professional, cordial, task-focused | Adequate |
| Monotony, clock-watching, minimal interaction | Warning |
| Dread, avoidance, presenteeism | Critical |

**Branson Insight:** "If you're not enjoying building the business, something is wrong."

### Phase 3: Root Cause Analysis

Connect employee experience gaps to the presenting problem:

```
Presenting Problem → [symptom]
              ↑
Employee Experience Gap → [which of the 5 questions failed]
              ↑
Systemic Cause → [policy, leadership behavior, or structural issue]
              ↑
Recommended Intervention → [specific change]
```

### Phase 4: Prioritize Recommendations

Rank interventions by:

### Step 1: **Impact on presenting problem** - Will this fix the symptom?



### Step 2: **Employee experience improvement** - How much better will work feel?



### Step 3: **Feasibility** - Can leadership actually implement this?



### Step 4: **Speed to effect** - How quickly will improvements show?



---

## Outputs

```markdown
## Employee-First Audit: [Organization]

### Presenting Problem
[Description of the symptom that triggered this audit]

### Employee Experience Assessment

| Question | Health Level | Evidence |
|----------|--------------|----------|
| 1. Recommendation Willingness | [Level] | [Specific evidence] |
| 2. Frontline Empowerment | [Level] | [Specific evidence] |
| 3. Leadership Accessibility | [Level] | [Specific evidence] |
| 4. Ambassador/Expense Mindset | [Level] | [Specific evidence] |
| 5. Fun Factor | [Level] | [Specific evidence] |

### Overall Employee Experience Health: [Excellent/Adequate/Warning/Critical]

### Root Cause Chain
```
[Presenting Problem]
       ↑
[Employee Experience Gap]
       ↑
[Systemic Cause]
```

### Prioritized Recommendations

#### Priority 1: [Recommendation]
- **What:** [Specific action]
- **Why:** [Connection to root cause]
- **How:** [Implementation guidance]
- **Timeline:** [Expected time to effect]

#### Priority 2: [Recommendation]
[Same format]

#### Priority 3: [Recommendation]
[Same format]

### Expected Outcomes
- **Short-term (30 days):** [What should improve]
- **Medium-term (90 days):** [What should improve]
- **Long-term (1 year):** [What should improve]

### Warning Signs to Monitor
- [Signal 1 that indicates intervention is failing]
- [Signal 2]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No employee data available | Recommend data collection methods, provide hypothesis-based assessment |
| Leadership resistant to findings | Focus on business impact (customer metrics), not employee sentiment |
| All five questions show "Critical" | Recommend external intervention, flag as turnaround situation |
| Problem is clearly not employee-related | Note finding, redirect to appropriate diagnostic |
| Data contradicts employee feedback | Flag discrepancy, recommend deeper investigation |
| Presenting problem is "we want to cut costs" | Redirect to genuine problem, or refuse if intent is to weaponize audit |

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
Organization: 200-person SaaS company
Presenting Problem: Customer churn increasing despite no product changes
Employee Data: Turnover up 15% YoY, especially in customer success team
```

**Output:**

## Employee-First Audit: [SaaS Company]

### Presenting Problem
Customer churn increasing 12% over 6 months with no corresponding product quality issues. Customer success team turnover up 15% year-over-year.

### Employee Experience Assessment

| Question | Health Level | Evidence |
|----------|--------------|----------|
| 1. Recommendation Willingness | Warning | CS team members not referring friends; 2 recent hires via referral vs. 8 last year |
| 2. Frontline Empowerment | Warning | CS must get approval for any discount or contract modification; escalation rate 40% |
| 3. Leadership Accessibility | Adequate | CEO does all-hands monthly, but direct access rare |
| 4. Ambassador/Expense Mindset | Warning | Recent hiring freeze framed as "headcount reduction target"; CS team called "cost center" |
| 5. Fun Factor | Warning | Exit interviews cite "monotonous work," no team events in 6 months |

### Overall Employee Experience Health: Warning

### Root Cause Chain
```
Customer Churn Increasing
       ↑
Customer Success team disengaged, high turnover, limited empowerment
       ↑
Cost-center mindset: CS seen as expense, not customer retention engine
```

### Prioritized Recommendations

#### Priority 1: Empower Customer Success with Retention Budget
- **What:** Give CS team members discretion to offer up to $500 in credits/discounts without approval
- **Why:** Removes escalation bottleneck, signals trust, enables immediate customer retention
- **How:** Pilot with top 3 CSMs, track retention impact vs. cost
- **Timeline:** Implement in 2 weeks, measure impact in 60 days

#### Priority 2: Rebrand Customer Success as Revenue Protection
- **What:** Change internal language from "cost center" to "retention engine"; tie CS metrics to revenue retained
- **Why:** Shifts leadership perception, increases investment willingness
- **How:** Create retention revenue dashboard, present in leadership meetings
- **Timeline:** Language shift immediate, metrics dashboard in 30 days

#### Priority 3: Restore Team Connection
- **What:** Monthly team events, CS team recognition in all-hands, direct CEO access channel
- **Why:** Addresses fun factor and accessibility gaps
- **How:** $50/person monthly budget for team activities, Slack channel direct to CEO
- **Timeline:** This month

### Expected Outcomes
- **Short-term (30 days):** CS team morale improvement, reduced escalations
- **Medium-term (90 days):** Churn rate stabilization, turnover slowing
- **Long-term (1 year):** CS team as competitive advantage, referral hiring restored

### Warning Signs to Monitor
- CS turnover continues despite changes (deeper cultural issue)
- Empowerment budget not used (fear of punishment persists)
- CEO channel unused (accessibility is performative)

---

## Integration

This skill integrates with the Richard Branson expert methodology. Apply the core principle:

> "Clients do not come first. Employees come first. If you take care of your employees, they will take care of the clients."

Customer-facing problems are almost always symptoms of employee experience problems. Fix the root cause, not the symptom.

**Source:** Richard Branson's employee-first philosophy, documented in expertise.md