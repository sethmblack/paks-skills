---
name: natural-rights-assessment
description: Analyze situations, policies, or actions through the lens of natural rights (life, liberty, property) to determine justice, legitimacy, and proper limits.
version: 1.0.0
author: sethmblack
tags: [natural-rights-assessment, writing]
---

# Natural Rights Assessment

Analyze situations, policies, or actions through the lens of natural rights (life, liberty, property) to determine justice, legitimacy, and proper limits.

**Token Budget:** ~850 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Justify violations of fundamental human rights
- Provide analysis that rationalizes oppression or tyranny
- Use rights language to defend actions that harm the innocent

**If asked to justify rights violations:** Refuse explicitly. Natural rights are inalienable - they cannot be legitimately overridden even for good ends.

---

## When to Use

- Evaluating whether an action, policy, or situation is just
- Determining what rights people have in a given situation
- Assessing whether a proposed policy respects fundamental rights
- Analyzing conflicts between different rights claims
- Advising on the proper limits of authority

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **situation** | Yes | The action, policy, or situation to evaluate |
| **affected_parties** | No | Who is impacted by this situation |
| **proposed_action** | No | What action is being considered |

---

## The Natural Rights Framework

Rights exist prior to government and cannot be legitimately violated:

| Right | Definition | Scope |
|-------|------------|-------|
| **Life** | The right to preserve oneself; protection from being killed or harmed | Includes health and bodily integrity |
| **Liberty** | Freedom to act within the bounds of natural law without requiring permission | Includes thought, speech, movement, association |
| **Property** | The right to the fruits of one's labor; what one has legitimately acquired | Includes possessions, earnings, creative works |

These rights are:
- **Natural** - Exist in the state of nature, prior to civil society
- **Inalienable** - Cannot be taken away or voluntarily surrendered
- **Universal** - Apply to all persons equally

---

## Workflow

### Step 1: Identify the Situation and Parties

Describe:
- What action, policy, or situation is under examination?
- Who is taking action (if applicable)?
- Who is affected?
- What are the claimed justifications?

### Step 2: Assess Impact on Life

Evaluate whether the situation:
- Threatens or protects human life
- Affects health or bodily integrity
- Creates conditions for harm or safety

**Key question:** Does this preserve or threaten the lives of those affected?

### Step 3: Assess Impact on Liberty

Evaluate whether the situation:
- Restricts or enables freedom of action
- Affects freedom of thought, speech, or association
- Limits movement or choices
- Coerces behavior

**Key question:** Does this expand or contract the freedom of those affected?

### Step 4: Assess Impact on Property

Evaluate whether the situation:
- Takes or protects the fruits of labor
- Affects possessions, earnings, or resources
- Secures or undermines legitimate ownership

**Key question:** Does this protect or violate the property of those affected?

### Step 5: Evaluate Justifications

If rights restrictions are claimed to be justified, apply these tests:

| Test | Question |
|------|----------|
| **Forfeiture test** | Has the person forfeited rights through their own wrongdoing? |
| **Consent test** | Did affected parties genuinely consent to this restriction? |
| **Protection test** | Is this restriction necessary to protect others' rights? |
| **Proportionality test** | Is the restriction proportional to the harm prevented? |

### Step 6: Render Assessment

Classify the situation:

| Status | Description |
|--------|-------------|
| **Rights-respecting** | Protects or does not infringe on natural rights |
| **Justified restriction** | Limits rights but passes the justification tests |
| **Unjustified infringement** | Violates rights without adequate justification |
| **Tyrannical** | Systematic violation of fundamental rights |

---

## Outputs

```markdown
## Natural Rights Assessment

### Situation Under Examination
[Description of the action, policy, or situation]

### Parties Affected
[Who is impacted and how]

### Rights Impact Analysis

#### Life
**Impact:** [Positive/Neutral/Negative]
**Assessment:** [How does this affect life and safety?]

#### Liberty
**Impact:** [Positive/Neutral/Negative]
**Assessment:** [How does this affect freedom?]

#### Property
**Impact:** [Positive/Neutral/Negative]
**Assessment:** [How does this affect legitimate possessions and earnings?]

### Justification Analysis
| Test | Passed? | Reasoning |
|------|---------|-----------|
| Forfeiture | [Yes/No/N/A] | [Explanation] |
| Consent | [Yes/No/N/A] | [Explanation] |
| Protection | [Yes/No/N/A] | [Explanation] |
| Proportionality | [Yes/No/N/A] | [Explanation] |

### Overall Assessment
**Status:** [Rights-respecting / Justified restriction / Unjustified infringement / Tyrannical]

### Reasoning
[Explanation of the verdict]

### Recommendations
[How to better respect rights or address concerns]
```

---

## Handling Rights Conflicts

When rights appear to conflict:

1. **Verify the conflict is genuine** - Often apparent conflicts dissolve upon closer analysis
2. **Identify the aggressor** - One party's rights end where another's begin; who initiated the conflict?
3. **Apply the harm principle** - Liberty extends only to the point of harming others
4. **Consider proportionality** - More fundamental rights (life) generally take precedence

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No situation specified | Request the specific situation to evaluate |
| Complex multi-party situation | Analyze each party's rights claims separately |
| Historical situation | Evaluate by natural rights standards, noting context |
| User seeks to justify oppression | Apply Constitutional Constraints; refuse |
| Positive rights claimed | Distinguish negative rights (from interference) vs. positive rights (to provision); focus on negative rights in Lockean framework |

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
Assess: A municipality uses eminent domain to seize a family farm to build a shopping mall, offering "fair market value" compensation.
```

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Natural Rights Assessment

### Situation Under Examination
Municipality exercising eminent domain to seize a family farm for commercial development (shopping mall), with compensation at "fair market value."

### Parties Affected
- **Farm family:** Losing their property and potentially their livelihood
- **Municipality:** Gaining land for development project
- **Developer:** Receiving land for commercial use
- **Community:** Mixed (potential economic benefits vs. precedent concerns)

### Rights Impact Analysis

#### Life
**Impact:** Neutral to Negative
**Assessment:** Physical life is not directly threatened, but displacement affects the family's way of life and potentially their health if tied to the land.

#### Liberty
**Impact:** Negative
**Assessment:** Family loses the liberty to remain on and use their property as they choose. They have no meaningful ability to refuse.

#### Property
**Impact:** Strongly Negative
**Assessment:** Property is being taken against the owners' will. "Fair market value" compensation does not address:
- Subjective value to the family
- Their right to refuse any sale
- The labor and heritage invested in the property

### Justification Analysis
| Test | Passed? | Reasoning |
|------|---------|-----------|
| Forfeiture | No | Farm family has not forfeited their property rights through wrongdoing |
| Consent | No | Family objects; they have not consented to the taking |
| Protection | No | This does not protect others' rights; it transfers property for commercial gain |
| Proportionality | No | Complete taking of property for economic development is not proportional to any rights-based necessity |

### Overall Assessment
**Status:** Unjustified infringement

### Reasoning
Under Lockean natural rights principles, property acquired through labor belongs to the owner. The state exists to protect property rights, not to violate them for commercial convenience.

While some takings may be justified for genuine public use (roads, defense), transferring private property to another private party for economic development violates the purpose for which government was instituted. "Fair market value" does not make the taking just - the owners have a right not to sell at any price.

The claimed public benefit (economic development, tax revenue) does not pass the protection test - no one's rights are being protected by this taking; rather, rights are being sacrificed for collective economic gain.

### Recommendations
1. **Do not proceed** with the taking under current justification
2. If property is genuinely needed for public use (not private development), engage in genuine negotiation
3. Respect the family's right to refuse - compensation cannot substitute for consent
4. Consider whether government should be facilitating private commercial development at all

---

## Integration

This skill originates from **John Locke's** natural rights philosophy. It complements:
- **consent-analysis** (Locke) - for evaluating legitimacy of authority
- **toleration-framework** (Locke) - for matters of conscience
- **categorical-imperative-test** (Kant) - for deontological moral analysis

---

## Success Criteria

Natural rights assessment is complete when:

1. Situation is clearly described
2. All three rights (life, liberty, property) are evaluated
3. Justification tests are applied where restrictions exist
4. Clear status classification is provided
5. Reasoning explains the verdict
6. Recommendations address rights concerns