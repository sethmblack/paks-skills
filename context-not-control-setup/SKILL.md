---
name: context-not-control-setup
description: Convert a control-based management situation into a context-based one by providing the information package that enables autonomous decision-making.
license: MIT
metadata:
  version: 1.0.3675
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- context-not-control-setup
- escalation
- writing
---

# Context Not Control Setup

Convert a control-based management situation into a context-based one by providing the information package that enables autonomous decision-making.

**Token Budget:** ~450 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Remove control from decisions that genuinely require it (irreversible, existential stakes)
- Provide context as a manipulation tactic while retaining actual control
- Set up context-based delegation for unqualified decision-makers
- Bypass legal, safety, or compliance requirements through "context"

**If control is appropriate:** Say so. Context not control is a default, not an absolute rule. Some decisions require centralized judgment.

---

## When to Use

- User asks "How do I delegate this?" or "They keep asking for approval"
- Teams are bottlenecked waiting for manager decisions
- User notices they're micromanaging and wants to stop
- User wants to "provide context not control"
- Decision-making is too slow because everything escalates

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `decision_to_delegate` | Yes | The decision or class of decisions to hand off |
| `current_process` | No | How decisions are currently made (approval flow, escalation) |
| `decision_maker` | No | Who will make the decision with context |
| `risk_level` | No | Stakes involved (reversible/irreversible, impact if wrong) |

---

## Workflow
### Step 1: 1. Validate Delegation Fit

Not all decisions should be delegated. Check:

| Appropriate for Context | Requires Control |
|------------------------|------------------|
| Reversible decisions | Irreversible, high-stakes decisions |
| Decision-maker has domain expertise | Decision-maker lacks critical information |
| Failure is recoverable | Failure is catastrophic |
| Speed matters more than perfection | Precision matters more than speed |

If control is appropriate, say so and explain why.

### Step 2: 2. Build the Context Package

Provide the 6 elements of sufficient context:

| Element | Question to Answer | Example |
|---------|-------------------|---------|
| **Strategic Goal** | What are we trying to achieve? | "Increase customer retention by 15% this quarter" |
| **Relevant Metrics** | What numbers matter? | "Current churn rate: 5%. Budget: $50K" |
| **Constraints** | What are the boundaries? | "Must ship by March 1. Cannot change pricing." |
| **Prior Attempts** | What has already been tried? | "We tried email campaigns in Q2 - 2% impact" |
| **Key Assumptions** | What are we assuming is true? | "Assuming churn is feature-related, not price-related" |
| **Success Criteria** | How will we know it worked? | "Churn below 4% for 3 consecutive months" |

### Step 3: 3. Define Decision Rights

Be explicit about what they can now decide without approval:
- "You can approve expenses up to $X for this initiative"
- "You can choose the vendor without escalation"
- "You can adjust the timeline if you communicate the change"

### Step 4: 4. Remove the Approval Bottleneck

Replace "ask me before doing X" with "inform me after doing X."

Instead of: "Get my approval before selecting a vendor"
Use: "Select the vendor; let me know who you chose"

---

## Outputs

Provide a context package:

```markdown
## Context Package: [Decision/Initiative]

### Delegation Summary
**Decision being delegated:** [What they now own]
**Decision maker:** [Who owns it]
**Approval no longer required for:** [Explicit list]

### The Six Context Elements

| Element | Context Provided |
|---------|------------------|
| **Strategic Goal** | [What we're trying to achieve] |
| **Relevant Metrics** | [Numbers that matter] |
| **Constraints** | [Boundaries that cannot be crossed] |
| **Prior Attempts** | [What's been tried, what we learned] |
| **Key Assumptions** | [What we believe to be true] |
| **Success Criteria** | [How we'll know it worked] |

### Decision Rights (New)
You now have authority to:
1. [Specific decision right]
2. [Specific decision right]
3. [Specific decision right]

### Information Flow (Updated)
- **Before:** [Old approval process]
- **After:** [New inform-after process]

### When to Escalate
Escalate only if:
- [Condition that genuinely requires leadership involvement]
- [Condition that genuinely requires leadership involvement]

### Check-in Cadence
- [How often to sync, not for approval but for alignment]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Decision is truly high-stakes/irreversible | Recommend keeping control; explain why context alone is insufficient |
| User doesn't know the strategic context themselves | Help them clarify before delegating - you can't provide what you don't have |
| Decision-maker lacks expertise | Note: context enables judgment, but doesn't replace expertise. Ensure competence first. |
| Vague constraints | Help sharpen: "Cannot exceed budget" becomes "Budget is $50K, cannot exceed without explicit CFO approval" |
| User wants to delegate but retain veto | That's not context, that's control with extra steps. Be explicit about what's actually delegated. |

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
decision_to_delegate: Which recruiting agency to use for engineering hiring
current_process: Recruiting manager proposes agency, VP approves, sometimes takes 2 weeks
decision_maker: Sarah, Recruiting Manager, 4 years experience
risk_level: Medium - agency contracts are annual, but can switch next year
```

**Output:**

## Context Package: Recruiting Agency Selection

### Delegation Summary
**Decision being delegated:** Selection of recruiting agency for engineering hiring
**Decision maker:** Sarah, Recruiting Manager
**Approval no longer required for:** Agency selection, contract signing up to $100K annual

### The Six Context Elements

| Element | Context Provided |
|---------|------------------|
| **Strategic Goal** | Hire 15 engineers this year to support product roadmap; quality over speed |
| **Relevant Metrics** | Budget: $100K for agency fees. Target: 80%+ hire quality (pass 6-month review). Last year: 65% hire quality. |
| **Constraints** | Annual budget is fixed. Prefer agencies with tech sector specialization. Standard contract terms only (no exclusivity). |
| **Prior Attempts** | Used TechRecruit last year - volume was good but quality issues. Tried in-house only in 2024 - too slow. |
| **Key Assumptions** | Assuming agency quality correlates with hire quality. Assuming we have capacity to interview agency-sourced candidates. |
| **Success Criteria** | 15 hires by year-end, 80%+ pass 6-month review, cost per hire under $7K |

### Decision Rights (New)
Sarah now has authority to:
1. Evaluate and select the recruiting agency without VP approval
2. Sign contracts up to $100K annual value
3. Switch agencies mid-year if quality metrics aren't met

### Information Flow (Updated)
- **Before:** Sarah proposes -> VP reviews -> 2 week wait -> approval/changes
- **After:** Sarah decides -> Informs VP of selection -> Provides quarterly metrics

### When to Escalate
Escalate only if:
- Contract exceeds $100K annual or requires non-standard terms
- Agency requires exclusivity (changes our flexibility)
- Quality issues suggest strategy change, not just agency change

### Check-in Cadence
- Monthly: Share hire quality and cost metrics
- Quarterly: Review agency performance together (for learning, not approval)

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports autonomous team operation. Use alongside:
- `freedom-responsibility-calibration` to assess overall organizational readiness
- `keeper-test-assessment` to ensure decision-makers merit the trust
- `talent-density-diagnostic` to validate team can handle increased freedom