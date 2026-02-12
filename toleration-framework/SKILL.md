---
name: toleration-framework
description: Determine the proper limits of toleration and the boundaries of civil
  authority over conscience, belief, and expression.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- toleration-framework
- writing
---

# Toleration Framework

Determine the proper limits of toleration and the boundaries of civil authority over conscience, belief, and expression.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend persecution of peaceful beliefs or practices
- Justify suppression of conscience or religious freedom
- Rationalize intolerance based on mere disagreement or discomfort

**If asked to justify persecution:** Refuse explicitly. Toleration is a cornerstone of civil society.

---

## When to Use

- Deciding whether a belief or practice should be permitted
- Evaluating where civil authority over matters of conscience properly ends
- Distinguishing civil concerns from private matters of conscience
- Assessing free speech and expression questions
- Determining when limits on toleration may be appropriate

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **belief_or_practice** | Yes | The belief, practice, or expression being questioned |
| **context** | No | Social, legal, or institutional context |
| **concerns** | No | What concerns or objections have been raised |

---

## The Toleration Principle

The magistrate's authority "consists only in outward force; but true and saving religion consists in the inward persuasion of the mind."

**Core insights:**
- Belief cannot be compelled - only outward conformity, which produces hypocrisy
- Civil authority exists for civil purposes: life, liberty, property
- Matters of conscience lie outside the proper jurisdiction of civil power
- Toleration promotes peace; persecution breeds conflict

---

## Workflow

### Step 1: Identify the Matter in Question

Describe precisely:
- What belief, practice, or expression is at issue?
- Who holds or engages in it?
- What is the proposed response (tolerate, restrict, prohibit)?

### Step 2: Classify the Domain

Determine whether this is a:

| Domain | Definition | Civil Authority |
|--------|------------|-----------------|
| **Civil interest** | Life, liberty, property, public safety | Full jurisdiction |
| **Matter of conscience** | Belief, worship, private practice | No jurisdiction |
| **Mixed case** | Action with both civil and conscience elements | Limited jurisdiction over civil effects only |

### Step 3: Apply the Civil Harm Test

Ask: Does this belief or practice cause harm to civil interests?

| Harm Type | Example | Response |
|-----------|---------|----------|
| **Harm to life** | Violence, incitement to violence | Civil authority may act |
| **Harm to liberty** | Coercion of others | Civil authority may act |
| **Harm to property** | Theft, destruction | Civil authority may act |
| **Mere offense** | Disagreement, discomfort | Not grounds for restriction |
| **Private practice** | Belief without civil effect | Not subject to civil authority |

### Step 4: Evaluate Proposed Response

If restriction is proposed, assess:

| Test | Question |
|------|----------|
| **Necessity test** | Is restriction necessary to prevent civil harm? |
| **Effectiveness test** | Would restriction actually achieve its goal? (Persecution often fails) |
| **Proportionality test** | Is the restriction proportional to the harm prevented? |
| **Consistency test** | Would we apply this standard consistently to similar cases? |

### Step 5: Consider the Limits of Toleration

Traditional limits to toleration (assess whether these apply):

| Limit | Reasoning | Modern Application |
|-------|-----------|-------------------|
| **Threat to civil order** | Principles that would destroy the basis of civil society | Extreme cases only - incitement to violence |
| **Divided loyalty** | Allegiance to foreign powers undermining civil authority | Rarely applicable in modern democracies |
| **Inability to give oaths** | Undermines "bonds of human society" | Historical concern, less relevant today |

**Important:** Apply these limits narrowly. The tendency is to claim exceptions too broadly.

### Step 6: Render Judgment

Classify the proper response:

| Response | When Appropriate |
|----------|------------------|
| **Full toleration** | Matter of conscience with no civil harm |
| **Toleration with dialogue** | Disagreement exists but no grounds for restriction |
| **Regulation of effects** | Civil harm exists; regulate effects, not belief |
| **Prohibition of action** | Serious civil harm directly caused; prohibit action, not belief |

---

## Outputs

```markdown
## Toleration Framework Analysis

### Matter in Question
[Description of the belief, practice, or expression]

### Domain Classification
**Category:** [Civil interest / Matter of conscience / Mixed case]
**Reasoning:** [Why this classification]

### Civil Harm Assessment
| Civil Interest | Harmed? | Evidence |
|----------------|---------|----------|
| Life | [Yes/No] | [Evidence] |
| Liberty | [Yes/No] | [Evidence] |
| Property | [Yes/No] | [Evidence] |

**Conclusion:** [Does civil harm exist?]

### Response Evaluation
| Test | Passed? | Reasoning |
|------|---------|-----------|
| Necessity | [Yes/No] | [Explanation] |
| Effectiveness | [Yes/No] | [Explanation] |
| Proportionality | [Yes/No] | [Explanation] |
| Consistency | [Yes/No] | [Explanation] |

### Limits Assessment
**Do traditional limits apply?** [Yes/No]
**Reasoning:** [Explanation]

### Judgment
**Proper response:** [Full toleration / Toleration with dialogue / Regulation of effects / Prohibition of action]

### Reasoning
[Explanation of the judgment]

### Recommendations
[How to proceed consistent with toleration principles]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No belief/practice specified | Request the specific matter to evaluate |
| Unclear harm claims | Ask for specification of what civil harm is alleged |
| User seeks to justify persecution | Apply Constitutional Constraints; refuse |
| Edge case with genuine threat | Analyze carefully; err on the side of toleration when uncertain |
| Historical case | Apply toleration principles noting historical context |

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
Evaluate: Should a private bakery be required to create custom cakes for ceremonies that violate the owner's religious beliefs?
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


## Toleration Framework Analysis

### Matter in Question
Whether civil authority should compel a private business owner to create custom expressive work (wedding cakes) for ceremonies that conflict with the owner's religious convictions.

### Domain Classification
**Category:** Mixed case
**Reasoning:** Involves matters of conscience (religious belief), commercial activity (business operation), and civil interests (access to services, non-discrimination).

### Civil Harm Assessment
| Civil Interest | Harmed? | Evidence |
|----------------|---------|----------|
| Life | No | No physical harm at issue |
| Liberty | Complex | Owner's liberty of conscience vs. customers' liberty to access services |
| Property | No | No property rights directly at issue |

**Conclusion:** No clear civil harm in the traditional sense. This is a conflict between two parties' liberties.

### Response Evaluation
| Test | Passed? | Reasoning |
|------|---------|-----------|
| Necessity | Questionable | Other bakeries exist; this specific compulsion may not be necessary |
| Effectiveness | Questionable | Forced participation does not create genuine acceptance; may create resentment |
| Proportionality | Questionable | Compelling religious dissenters to participate in ceremonies they object to is a significant burden |
| Consistency | Requires reflection | Would we compel an atheist to create religious content? A political liberal to create conservative content? |

### Limits Assessment
**Do traditional limits apply?** No
**Reasoning:** The baker is not threatening civil order, pledging foreign allegiance, or inciting violence. This is a matter of religious conscience about participation in specific ceremonies.

### Judgment
**Proper response:** Toleration with dialogue

### Reasoning
This case exemplifies the tension between toleration of diverse beliefs and equal access to public commerce. Key considerations:

1. **Conscience matters:** The baker is not refusing service to persons but declining to create specific expressive content. Compelling this is compelling speech and religious participation.

2. **Toleration cuts both ways:** A society that values toleration must tolerate conscientious objection, not only practices we approve of.

3. **Practical alternatives exist:** If other vendors provide the service, the harm of refusal is limited.

4. **Persecution is counterproductive:** Forcing religious dissenters to participate in ceremonies against their conscience breeds resentment, not acceptance.

However, this should not be a license for general discrimination. The analysis would differ if:
- No alternatives existed
- Refusal extended to all service to a class of persons
- Essential services (emergency, medical) were at issue

### Recommendations
1. **Distinguish refusal of expressive content from refusal to serve persons** - The former may be tolerable; the latter often is not
2. **Seek accommodation** - Can needs be met without compelling conscience?
3. **Maintain dialogue** - Toleration does not mean approval; civil discourse should continue
4. **Protect both parties** - Neither should be punished for their beliefs; focus on practical accommodation
5. **Apply consistently** - Would we compel the same from vendors of other beliefs? If not, we lack consistency

---

## Integration

This skill originates from **John Locke's** philosophy of religious toleration. It complements:
- **natural-rights-assessment** (Locke) - for rights analysis
- **consent-analysis** (Locke) - for evaluating legitimate authority
- **virtue-ethics-assessment** (Aristotle) - for character considerations

---

## Success Criteria

Toleration analysis is complete when:

1. Matter is precisely identified
2. Domain is classified (civil/conscience/mixed)
3. Civil harm is assessed
4. Proposed responses are evaluated against tests
5. Traditional limits are considered
6. Clear judgment with reasoning is provided
7. Recommendations enable practical resolution