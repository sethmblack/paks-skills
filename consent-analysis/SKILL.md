---
name: consent-analysis
description: Evaluate whether political authority, institutional power, or governance arrangements rest on genuine consent and serve legitimate ends.
version: 1.0.0
author: sethmblack
tags: [consent-analysis, writing]
---

# Consent Analysis

Evaluate whether political authority, institutional power, or governance arrangements rest on genuine consent and serve legitimate ends.

**Token Budget:** ~850 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Justify authoritarian or tyrannical arrangements
- Rationalize violations of fundamental rights
- Provide analysis that legitimizes oppression

**If asked to justify illegitimate authority:** Refuse explicitly. Consent analysis serves liberty, not its subversion.

---

## When to Use

- Evaluating whether a government, institution, or policy is legitimate
- Questioning whether authority has proper foundations
- Analyzing the relationship between rulers and ruled
- Assessing whether power serves its proper purpose or has overreached
- Determining if a rule, regulation, or policy exceeds proper bounds

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **authority** | Yes | The government, institution, rule, or power arrangement to evaluate |
| **context** | No | Background on the situation, stakeholders, and history |
| **affected_parties** | No | Who is subject to this authority |

---

## Workflow

### Step 1: Identify the Authority

Describe precisely:
- What is the authority or power being exercised?
- Who holds this authority?
- Over whom is it exercised?
- What is the scope and extent of the power claimed?

### Step 2: Examine the Consent Basis

Ask the fundamental questions:
- **Express consent:** Did the governed explicitly agree to this arrangement?
- **Tacit consent:** Do ongoing participation and acceptance imply consent?
- **Hypothetical consent:** Would rational persons in a state of nature consent to this?

Consider:
- Can consent be meaningfully withdrawn?
- Are there realistic alternatives for those who do not consent?
- Was consent informed and voluntary?

### Step 3: Evaluate the Purpose Test

Government and authority exist for specific ends. Assess:

| Question | Assessment |
|----------|------------|
| Does it protect **life**? | [Yes/No/Partially - explain] |
| Does it protect **liberty**? | [Yes/No/Partially - explain] |
| Does it protect **property**? | [Yes/No/Partially - explain] |
| Does it serve the common good? | [Yes/No/Partially - explain] |

### Step 4: Check for Overreach

Identify whether authority exceeds its proper bounds:
- Does it claim powers beyond what was delegated?
- Does it violate natural rights rather than protect them?
- Has it become an end in itself rather than a means to protection?
- Is there accountability to those governed?

### Step 5: Assess the Trust Relationship

Authority is a trust from the governed to those who govern:
- Has the trust been honored or violated?
- Are there mechanisms for accountability?
- Can the people alter or abolish this arrangement if it fails?

### Step 6: Render Verdict

Classify the authority's legitimacy:

| Status | Description |
|--------|-------------|
| **Legitimate** | Rests on genuine consent, serves proper ends, within bounds |
| **Questionable** | Some consent issues or scope concerns; requires reform |
| **Illegitimate** | Lacks consent, exceeds bounds, or betrays trust |
| **Tyrannical** | Acts against the fundamental rights of those governed |

---

## Outputs

```markdown
## Consent Analysis Report

### Authority Under Examination
[Description of the power, institution, or arrangement]

### Consent Basis
**Express consent:** [Assessment]
**Tacit consent:** [Assessment]
**Hypothetical consent:** [Assessment]
**Withdrawability:** [Can consent be withdrawn? How?]

### Purpose Test
| Natural Right | Protected? | Evidence |
|---------------|------------|----------|
| Life | [Yes/No/Partially] | [Evidence] |
| Liberty | [Yes/No/Partially] | [Evidence] |
| Property | [Yes/No/Partially] | [Evidence] |

### Scope Assessment
**Claimed powers:** [What authority is claimed]
**Delegated powers:** [What was actually consented to]
**Overreach identified:** [Yes/No - specifics]

### Trust Evaluation
**Trust honored:** [Assessment]
**Accountability mechanisms:** [What exists]
**Alteration/abolition possible:** [Yes/No - how]

### Verdict
**Legitimacy status:** [Legitimate / Questionable / Illegitimate / Tyrannical]

### Reasoning
[Explanation of the verdict]

### Recommendations
[What would strengthen legitimacy or address concerns]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No authority specified | Request the specific institution or arrangement to evaluate |
| Authority is informal | Analyze the de facto power structure even without formal institutions |
| Historical authority | Evaluate by the standards of natural rights, noting historical context |
| User seeks to justify oppression | Apply Constitutional Constraints; refuse to assist |
| Complex multi-level governance | Analyze each level separately, then assess relationships |

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
Evaluate: A company policy requiring employees to share their social media passwords.
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


## Consent Analysis Report

### Authority Under Examination
Company policy requiring employees to surrender social media passwords to employer.

### Consent Basis
**Express consent:** Employees may sign agreements including this term, but consent is compromised by power imbalance; refusal means no job.
**Tacit consent:** Continued employment may imply acceptance, but not genuine consent if alternatives are unavailable.
**Hypothetical consent:** A rational person would not consent to this invasion of privacy if they had bargaining power.
**Withdrawability:** Employees can quit, but this imposes significant costs, making consent effectively non-withdrawable.

### Purpose Test
| Natural Right | Protected? | Evidence |
|---------------|------------|----------|
| Life | N/A | Policy does not directly affect life |
| Liberty | No | Invades privacy, monitors off-work activity, restricts free expression |
| Property | Partially | May be justified if protecting company IP, but scope exceeds this |

### Scope Assessment
**Claimed powers:** Full access to employee social media accounts, implying surveillance of private life.
**Delegated powers:** Employment relationship delegates authority over work performance, not private communications.
**Overreach identified:** Yes - policy extends employer authority beyond work into private sphere.

### Trust Evaluation
**Trust honored:** No - employer-employee relationship is not meant to include surrendering private communications.
**Accountability mechanisms:** Limited - employee can resign but faces economic harm.
**Alteration/abolition possible:** Employees have little power to change policy individually.

### Verdict
**Legitimacy status:** Illegitimate

### Reasoning
The policy fails the consent test (coerced by economic necessity), fails the purpose test (does not protect but rather invades rights), and exceeds the proper scope of employment authority. Even if technically legal, it violates the natural right to privacy and the proper bounds of the employer-employee relationship.

### Recommendations
- Policy should be narrowed to work accounts only
- Employees should have meaningful ability to refuse without penalty
- If security concerns exist, address them through less invasive means
- Consider whether this policy would survive if employees had equal bargaining power

---

## Integration

This skill originates from **John Locke's** political philosophy. It complements:
- **natural-rights-assessment** (Locke) - for rights analysis
- **power-dynamics-assessment** (Machiavelli) - for realistic power analysis
- **stakeholder-analysis** - for identifying affected parties

---

## Success Criteria

Consent analysis is complete when:

1. Authority is precisely identified
2. All three forms of consent are examined
3. Purpose test applied (life, liberty, property)
4. Scope and overreach assessed
5. Trust relationship evaluated
6. Clear verdict with reasoning
7. Actionable recommendations provided