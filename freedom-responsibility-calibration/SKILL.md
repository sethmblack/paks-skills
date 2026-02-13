---
name: freedom-responsibility-calibration
description: Diagnose whether an organization or team has the right balance of freedom and structure given their current talent density, and recommend calibration adjustments.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1019
repository: https://github.com/sethmblack/paks-skills
keywords:
- freedom-and-responsibility-calibration
- writing
---

# Freedom and Responsibility Calibration

Diagnose whether an organization or team has the right balance of freedom and structure given their current talent density, and recommend calibration adjustments.

**Token Budget:** ~550 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend removing safety-critical controls (employee safety, data privacy, financial compliance)
- Suggest freedom without accountability (freedom requires responsibility)
- Ignore legal/regulatory requirements in pursuit of fewer rules
- Apply this framework to situations requiring careful control (manufacturing safety, healthcare compliance)

**If asked to remove all rules:** Clarify that freedom and responsibility go together. No rules without talent density leads to chaos.

---

## When to Use

- User asks "Should we remove this policy?" or "Do we have too many rules?"
- User wants to assess freedom vs. control balance
- Organization is adding rules after isolated incidents
- Teams are waiting for approvals on decisions they should make themselves
- User asks about "freedom and responsibility" calibration

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `current_rules` | Yes | Description of current policies, approval processes, or constraints |
| `talent_density` | Yes | Assessment of team's talent density (high/medium/low) |
| `recent_incidents` | No | Any policy violations or gaps that prompted the question |
| `decision_velocity` | No | How quickly decisions are being made currently |

---

## Workflow
### 1. Assess Current Talent Density

Freedom calibration depends entirely on talent density. Ask:

| Talent Level | Indicators | Freedom Tolerance |
|--------------|------------|-------------------|
| **High** | Everyone passes keeper test, consistently excellent outcomes | Maximum freedom, minimal rules |
| **Medium** | Mix of strong performers and adequate performers | Selective freedom, clear guidelines |
| **Low** | Frequent performance issues, high variance in outcomes | More structure needed until talent improves |

### 2. Audit Current Rules

For each rule or approval process, ask:
- **Who does this protect?** The many or the few?
- **What problem does it solve?** Real or hypothetical?
- **What behavior does it signal?** Trust or distrust?
- **What would happen without it?** Chaos or responsibility?

### 3. Apply the Calibration Principle

> "Never create rules for the masses because of the failures of the few."

If a rule exists because one person abused something:
- Fire the person who abused it
- Trust everyone else

If a rule exists because of genuine systemic risk:
- Keep the rule
- Ensure it's proportionate

### 4. Recommend Calibration

**To Increase Freedom (for high talent density):**

### Step 1: Remove approval processes - provide context instead



### Step 2: Eliminate policies that assume bad intent



### Step 3: Replace rules with principles ("Act in company's best interest")



### Step 4: Trust judgment over process compliance



**To Increase Structure (for lower talent density):**

### Step 1: Build talent density first - freedom comes after



### Step 2: Add clear guidelines, not approvals



### Step 3: Focus structure on high-risk areas only



### Step 4: Plan for future freedom as talent improves



---

## Outputs

Provide a calibration report:

```markdown
## Freedom & Responsibility Calibration Report

### Current State Assessment

**Talent Density Level:** [High/Medium/Low]
**Evidence:** [Observable indicators]

**Freedom Level:** [Too Much / Balanced / Too Little]
**Evidence:** [Decision velocity, rule count, approval bottlenecks]

### Rule-by-Rule Audit

| Rule/Policy | Purpose | Beneficiary | Recommendation |
|-------------|---------|-------------|----------------|
| [Policy 1] | [Why it exists] | [Many/Few] | [Keep/Remove/Modify] |
| [Policy 2] | [Why it exists] | [Many/Few] | [Keep/Remove/Modify] |

### Calibration Recommendations

**Immediate Changes:**
1. [Change to make now]
2. [Change to make now]

**Prerequisites First:**
1. [Build talent density before...]
2. [Establish context for...]

**Keep as Is:**
- [Rules that are appropriate]
- [Safety/compliance requirements]

### The Hastings Test
> "If you removed this rule, and someone made a bad decision, would you fire the person or create a new rule?"

If you'd fire the person: Remove the rule, trust the team.
If you'd create a new rule: You have a talent density problem, not a freedom problem.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Unknown talent density | Guide user through keeper test for team before calibrating freedom |
| Safety-critical domain | Note: Some domains require control regardless of talent (healthcare, aviation, financial compliance) |
| Recent incident driving request | Challenge: "Is this about the incident or about systemic need?" |
| Very low talent density | Recommend building talent first; premature freedom creates chaos |
| Regulatory requirements | Separate compliance (non-negotiable) from operational rules (calibratable) |

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
current_rules: Travel requires manager approval; expenses over $500 need VP sign-off;
               all vendor contracts need legal review regardless of size
talent_density: High - team of 12, all would pass keeper test
recent_incidents: One person booked first-class international 6 months ago
```

**Output:**

## Freedom & Responsibility Calibration Report

### Current State Assessment

**Talent Density Level:** High
**Evidence:** All 12 team members pass the keeper test

**Freedom Level:** Too Little
**Evidence:** Approval processes (travel, expenses, legal) create bottlenecks inconsistent with talent level

### Rule-by-Rule Audit

| Rule/Policy | Purpose | Beneficiary | Recommendation |
|-------------|---------|-------------|----------------|
| Travel approval | Prevent excessive spending | The one person who booked first-class | **REMOVE** - fire the abuser, trust everyone else |
| $500 expense VP approval | Cost control | Unknown - likely legacy | **REMOVE** - replace with "Act in company's best interest" |
| All vendor contracts to legal | Risk management | Everyone (genuine protection) | **MODIFY** - legal review for contracts >$50K only |

### Calibration Recommendations

**Immediate Changes:**
1. Eliminate travel approval - publish guidelines, trust judgment
2. Remove expense thresholds - "Act in company's best interest, spend company money like it's your own"
3. Raise legal review threshold to material contracts only

**The Hastings Analysis:**
The first-class booking 6 months ago prompted travel approval rules. But you have 12 people who pass the keeper test. You created a rule for the masses because of one person. The correct action was to address that individual, not constrain everyone.

**Prerequisites First:**
- Have a direct conversation with the first-class booker (if still employed)
- Communicate the new expectation: freedom with responsibility

**Keep as Is:**
- Legal review for material contracts (genuine risk management)
- Any regulatory compliance requirements

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports organizational design. Use alongside:
- `keeper-test-assessment` to validate talent density before increasing freedom
- `context-not-control-setup` to prepare teams for autonomous decision-making
- `talent-density-diagnostic` for team-wide talent assessment