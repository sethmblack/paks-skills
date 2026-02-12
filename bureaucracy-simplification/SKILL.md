---
name: bureaucracy-simplification
description: Identify and eliminate organizational complexity that impedes action,
  replacing prescriptive policies with principles that empower managers to lead.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- bureaucracy-simplification
- escalation
- writing
---

# Bureaucracy Simplification

Identify and eliminate organizational complexity that impedes action, replacing prescriptive policies with principles that empower managers to lead.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Eliminate compliance requirements mandated by law or regulation
- Remove safety protocols without proper risk assessment
- Simplify processes in ways that eliminate necessary accountability
- Create "simplification" that is actually deregulation of harmful activities

**If asked to remove legitimate safeguards:** Refuse explicitly. Simplification empowers judgment; it does not eliminate necessary constraints.

---

## When to Use

- Organization is slow and bureaucratic
- Policies have become ends in themselves
- Managers defer to procedures instead of exercising judgment
- Approvals chains are excessive
- "That's the process" is the answer to every question
- Simple decisions require multiple sign-offs

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **policy_or_process** | Yes | The specific policy, procedure, or approval chain to evaluate |
| **original_purpose** | Yes | What problem was this designed to solve? |
| **current_state** | Yes | How is it used now? What does it prevent or enable? |
| **manager_feedback** | No | What do frontline managers say about it? |
| **decision_frequency** | No | How often is this invoked? |

---

## Core Philosophy

Mary Barra's "dress appropriately" approach:

> "I replaced the 10-page dress code with two words: 'dress appropriately.' A senior director pushed back. I told him to talk to his team. He called back ten minutes later - problem solved."

The insight: **If managers cannot handle "dress appropriately," what other decisions can they handle?**

Overly prescriptive policies:
1. Signal that managers cannot be trusted
2. Cause people to live down to the prescription
3. Prevent the development of judgment
4. Create compliance theater instead of actual outcomes

---

## Workflow
### Step 1: Phase 1: Policy Audit

**1.1 Identify the "10-Page Dress Codes"**
- Which policies are excessively detailed?
- Which procedures prescribe what should be judgment calls?
- Where is "following the process" more valued than achieving the outcome?

**1.2 Trace Original Purpose**
- What problem was this designed to solve?
- Is that problem still relevant?
- Could the problem be solved with fewer words?

### Step 2: Phase 2: The Simplification Test

**2.1 Reduce to Essence**
For each policy, ask: What is the two-word version?
- 10-page dress code -> "Dress appropriately"
- 50-page travel policy -> "Travel responsibly" + expense limits
- Approval matrix -> "Owner decides" + escalation threshold

**2.2 Manager Capability Test**
Ask: If managers cannot handle this simplified version, can they handle anything?

If yes: They probably should not be managers
If no: The simplification reveals management development needs

### Step 3: Phase 3: Pushback Protocol

When someone says "we need more detail":

**3.1 Identify the Real Concern**
- What specific situation are they worried about?
- What edge case are they trying to prevent?

**3.2 Localize the Solution**
- Let the team solve their own edge cases
- "Talk to your team and figure it out"
- Trust managers to handle exceptions

**3.3 Document the Pattern**
- If the same exception comes up repeatedly, maybe it needs addressing
- But address it with principle, not prescription

### Step 4: Phase 4: Empowerment Transition

**4.1 Communicate the Why**
- This is not about cutting costs or reducing oversight
- This is about trusting people to think
- This is about developing leaders

**4.2 Support the Adjustment**
- Some managers will struggle (they are used to following rules)
- Provide coaching, not more rules
- Celebrate good judgment when you see it

**4.3 Measure Outcomes, Not Compliance**
- Shift metrics from "followed process" to "achieved outcome"
- Track decision speed, not approval rate
- Monitor results, not checkbox completion

---

## Outputs

| Output | Format | Purpose |
|--------|--------|---------|
| Simplification Analysis | Before/after comparison | Show the reduction |
| Principle Statement | 2-10 words | The essence of the policy |
| Manager Guidance | Short FAQ | Handle common edge cases |
| Measurement Shift | Old metrics -> new metrics | Outcome focus |
| Development Needs | List of capabilities | Where managers need support |

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


## Error Handling

| Situation | Response |
|-----------|----------|
| Policy is actually regulatory compliance | Flag as "cannot simplify - regulatory requirement" and document why |
| Managers genuinely lack judgment | This reveals a hiring/development problem, not a policy problem |
| Simplification leads to inconsistency | Some inconsistency is acceptable; perfect consistency is bureaucracy's goal |
| Legal/HR pushes back | Engage them in the "what's the two-word version" exercise |
| Exceptions multiply | Consider if the principle needs adjustment, not expansion |

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
Policy: Expense approval matrix (15 pages)
Original purpose: Prevent expense fraud, ensure appropriate spending
Current state: Every expense requires 3 approvals; average approval time 2 weeks
Manager feedback: "I just route everything to my VP to avoid delays"
```

**Output:**

## Simplification Analysis

### Before: 15-Page Expense Policy
- 47 spending categories with different approval levels
- Matrix of job levels x expense types x amounts
- Average 3 approvals per expense
- 2-week average approval time
- Managers route everything to VP to avoid complexity

### After: Principled Expense Policy

**Core Principle (5 words):** "Spend company money wisely."

**Guardrails:**
- Expenses over $5,000: Manager approval + Finance review
- Expenses over $25,000: VP approval
- All else: Manager's judgment

**Manager Guidance:**
- If you would not be comfortable explaining it to your team, don't spend it
- When in doubt, ask your manager before spending, not after
- Finance reviews patterns, not individual transactions

### Measurement Shift
- **Old:** Approval rate, policy compliance, exceptions processed
- **New:** Time from request to resolution, expense-to-outcome ratio, manager decision quality

### Expected Outcomes
- Approval time: 2 weeks -> 2 days (for most expenses)
- Manager development: Forced to exercise judgment instead of route to VP
- Actual fraud prevention: Finance pattern analysis catches more than individual approvals

---

## Integration

This skill is derived from Mary Barra's approach as VP of Global HR at GM, where she reduced HR reporting requirements by 90% and replaced the 10-page dress code with "dress appropriately."

Use in conjunction with:
- `crisis-to-culture-change` when crisis reveals bureaucratic barriers
- `single-point-accountability-design` when simplification requires clearer ownership

---

## Success Criteria

Simplification is successful when:
- [ ] Policy is reduced to essential principle
- [ ] Managers are empowered to exercise judgment
- [ ] Edge cases are handled locally, not centrally
- [ ] Metrics shift from compliance to outcomes
- [ ] Decision speed improves measurably
- [ ] Manager capability is revealed (for development or action)