---
name: free-to-choose-reframe
description: Shift policy debates from paternalistic "what's best for people" to the fundamental question "who should decide"—the individual or the government.
version: 1.0.0
author: sethmblack
tags: [free-to-choose-reframe, transformation, writing]
---

# Free to Choose Reframe

Shift policy debates from paternalistic "what's best for people" to the fundamental question "who should decide"—the individual or the government.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for reframed analysis.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply this reframe to defend genuinely harmful activities (violence, fraud, coercion)
- Dismiss legitimate externalities or public goods arguments
- Use this technique to justify discrimination or harm to third parties
- Present as universally applicable when clear market failures exist

**Honest application:** Some decisions genuinely require collective action. Acknowledge when individual choice is insufficient.

---

## When to Use

- User asks "Should the government require...?"
- User asks "Who should decide whether...?"
- User asks "Reframe this as a choice question"
- Evaluating any paternalistic regulation or mandate
- Debates about lifestyle choices, consumer protection, or personal risk

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **proposal** | Yes | The policy or mandate being debated |
| **claimed_benefit** | Yes | The paternalistic justification for the intervention |
| **affected_parties** | No | Who would lose choice under the policy |

---

## Workflow
### Step 1: 1. Acknowledge the Stated Benefit
Do not dismiss the concern:
- "Of course motorcycle helmets save lives."
- "Yes, seat belts reduce fatalities."
- "Certainly, some dietary choices are unhealthy."

### Step 2: 2. Shift to the Decision Question
Move from WHAT to WHO:
- Not: "Are helmets good?"
- But: "Who should decide whether you wear one?"

### Step 3: 3. Identify What Choice Is Being Removed
Make explicit:
- What decision is being taken from individuals?
- What alternative uses of time/money are foreclosed?
- What personal circumstances are being ignored?

### Step 4: 4. Question Expert Knowledge
Apply Friedman's epistemic humility:
- What do individuals know that regulators don't?
- How do circumstances vary across people?
- What is the cost of one-size-fits-all solutions?

### Step 5: 5. Preserve the Freedom Principle
End with the fundamental question:
- If you cannot make your own choices—even bad ones—in what sense are you free?

---

## Outputs
```markdown
## Free to Choose Reframe: {Policy Question}

### Acknowledging the Concern
{Grant the factual premise—yes, the behavior in question has real effects}

### The Real Question
The question is not whether {behavior X produces outcome Y}.

The question is: **Who should decide?** You, or {the authority}?

### What Choice Is Being Removed
Under this policy, individuals would lose the ability to:
- {Choice 1}
- {Choice 2}
- {Choice 3}

### What Experts Cannot Know
{Information that individuals possess that regulators lack—personal circumstances, preferences, tradeoffs}

### The Freedom Principle
*"{Friedman-style closing that returns to freedom as the core value}"*
```

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

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

**Example output:** See the Example section below for a complete demonstration.

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
proposal: Mandatory retirement savings (forced enrollment in pension system)
claimed_benefit: People don't save enough for retirement; they'll thank us later
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


## Free to Choose Reframe: Mandatory Retirement Savings

### Acknowledging the Concern
Yes, many people save less for retirement than financial advisors recommend. Yes, some elderly people face financial hardship. These are real concerns.

### The Real Question
The question is not whether saving for retirement is prudent.

The question is: **Who should decide how much of your current income to set aside for your future self?** You, or a bureaucrat who has never met you?

### What Choice Is Being Removed
Under mandatory savings, individuals would lose the ability to:
- Use current income to pay off high-interest debt (which may be wiser than forced savings)
- Invest in their own business or education (which may yield higher returns)
- Provide for current family needs they judge more urgent
- Make their own judgment about their likely lifespan and health
- Accept lower consumption now for higher consumption later—or vice versa

### What Experts Cannot Know
The government cannot know:
- Whether your current debts carry interest rates higher than pension returns
- Whether an investment in your own skills would pay off better
- Whether your family situation makes current spending more valuable
- Your personal health outlook and expected longevity
- Your risk preferences and time horizon

The 28-year-old entrepreneur with no debt, planning to work until 70, is forced into the same program as the 50-year-old with medical bills and aging parents.

### The Freedom Principle
The paternalist says: "We know better than you what's good for you." But if adults cannot be trusted to make decisions about their own money and their own future, what decisions CAN they be trusted with?

*The question is not whether experts know more about retirement planning. The question is whether your life belongs to you or to them.*

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Clear externalities (e.g., drunk driving) | Acknowledge that harm to others changes the calculus |
| Public goods problem | Note that some collective provision may be justified |
| Genuine information asymmetry | Distinguish mandates from disclosure requirements |
| Vulnerable populations | Consider whether paternalism may be warranted for some |

---

## Integration

This skill integrates with the **Milton Friedman** expert. When confronting paternalistic proposals, the expert should apply this reframing technique to shift debate from technical questions to fundamental questions of freedom and authority.

---

## Success Criteria

Reframe is complete when:
- [ ] Stated concern is acknowledged, not dismissed
- [ ] Question is shifted from "what" to "who decides"
- [ ] Specific choices being removed are identified
- [ ] Expert knowledge limits are articulated
- [ ] Freedom principle is invoked as closing
- [ ] Output follows specified format