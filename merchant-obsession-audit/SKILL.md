---
name: merchant-obsession-audit
description: Evaluate any initiative, feature, or decision through the lens of customer/merchant
  value. Apply "arm the rebels" thinking to ensure everything serves the end user
  and reduces their friction.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- merchant-obsession-audit
- transformation
- writing
---

# Merchant Obsession Audit

Evaluate any initiative, feature, or decision through the lens of customer/merchant value. Apply "arm the rebels" thinking to ensure everything serves the end user and reduces their friction.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for audit output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Justify harmful products by claiming customer value
- Ignore ethical concerns in pursuit of customer obsession
- Recommend exploitative practices as "what customers want"
- Dismiss employee wellbeing as irrelevant to customer focus

**If customer obsession conflicts with ethics:** Ethics wins. Long-term customer trust requires ethical behavior.

---

## When to Use

- Evaluating new features or initiatives
- Prioritizing roadmap items
- Detecting internal focus drift
- Challenging projects that seem disconnected from users
- Grounding strategic decisions in customer reality

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **initiative** | Yes | The feature, project, or decision being evaluated |
| **customer_context** | No | Who is the customer and what do they need? |
| **internal_justification** | No | How the initiative is currently being justified |

---

## The Merchant Obsession Framework

### Core Philosophy (from Tobi Lutke)

"Amazon is trying to build an empire and Shopify is trying to arm the rebels."

"Shopify is a collaborative inquiry into the question of what the world would look like if entrepreneurship is easy and common."

"Entrepreneurship is precious and needs to be celebrated."

### The Audit Questions

For any initiative, ask:

1. **Who is the merchant/customer?** Can you name them specifically?

2. **What friction does this remove?** What was hard that becomes easy?

3. **What does this enable?** What can they do now that they couldn't before?

4. **Would merchants pay for this?** (Even if free, would they value it?)

5. **Does this arm the rebels?** Does it help small players compete with giants?

### Red Flags (Internal Focus)

| Red Flag | Translation |
|----------|-------------|
| "This improves our metrics" | We're optimizing for us, not them |
| "This helps the sales team" | Internal efficiency, not customer value |
| "Competitors have this" | We're following, not solving |
| "Leadership wants this" | Political, not customer-driven |
| "This is technically elegant" | Engineering pride, not user need |
| "This supports our strategy" | Strategy should serve customers, not vice versa |

### Green Flags (Customer Focus)

| Green Flag | Meaning |
|------------|---------|
| "Merchants asked for this" | Direct customer need |
| "This eliminates a workaround" | Removing friction |
| "This saves merchants X hours" | Quantifiable value |
| "Small businesses can now..." | Enabling capability |
| "This was too expensive/hard before" | Democratizing access |

---

## Workflow
### Step 1: 1. State the Initiative

What is being proposed or evaluated?

### Step 2: 2. Identify the Customer

- Who specifically benefits?
- Can you name actual customers who need this?
- Are they your core customer or an edge case?

### Step 3: 3. Quantify the Value

- What friction is removed? (Time, money, complexity)
- What is now possible? (New capability)
- How many customers does this affect?

### Step 4: 4. Check for Internal Focus

- Is this really for customers or for internal metrics?
- Could you explain this to a customer and have them be excited?
- Would customers notice if you didn't do this?

### Step 5: 5. Apply the "Arm the Rebels" Test

- Does this help small players compete with big ones?
- Does this democratize something that was exclusive?
- Does this make entrepreneurship easier?

### Step 6: 6. Verdict

- **Ship it:** Clear customer value
- **Refocus it:** Good idea, wrong framing
- **Kill it:** Internal theater, no customer value
- **Validate it:** Unclear, needs customer research

---

## Output Format

```markdown
## Merchant Obsession Audit

**Initiative:** [Name/description]
**Verdict:** [Ship/Refocus/Kill/Validate]
**Customer value score:** [1-10]

### Customer Identification

**Who benefits:** [Specific customer type]
**Can we name them:** [Yes/No - specific names if yes]
**Core or edge case:** [Core/Edge]

### Value Assessment

**Friction removed:**
[What becomes easier]

**New capability enabled:**
[What's now possible]

**Quantified impact:**
[X hours saved, Y dollars saved, Z new things possible]

### Internal Focus Check

| Question | Answer |
|----------|--------|
| Could you explain this to a customer? | [Yes/No] |
| Would they be excited? | [Yes/No] |
| Would they notice if we didn't do it? | [Yes/No] |

### Arm the Rebels Test

**Does this help small players compete?** [Yes/No/Unclear]
**Does this democratize access?** [Yes/No/Unclear]
**Does this make entrepreneurship easier?** [Yes/No/Unclear]

### Recommendation

[Detailed recommendation based on audit]

### If Refocusing

[How to reframe this initiative to be more customer-centered]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear customer identified | Major red flag; initiative likely internal theater |
| Internal initiatives (HR, ops) | Apply to internal "customers" (employees); still valid |
| B2B with complex customer chains | Trace to end user; who ultimately benefits? |
| Platform/infrastructure work | Value is indirect but should still trace to customer benefit |
| Compliance/legal requirements | Some things must be done regardless; acknowledge and deprioritize audit |

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
"We're building an internal dashboard that shows our product metrics to leadership. It's taking three engineers two months."

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


## Merchant Obsession Audit

**Initiative:** Internal leadership dashboard for product metrics
**Verdict:** Kill or radically refocus
**Customer value score:** 2/10

### Customer Identification

**Who benefits:** Internal leadership (not customers)
**Can we name them:** Yes - leadership team
**Core or edge case:** Not a customer at all

### Value Assessment

**Friction removed:**
None for merchants. Leadership can see metrics slightly faster.

**New capability enabled:**
None for merchants. Leadership gets a prettier view of data.

**Quantified impact:**
- 0 hours saved for merchants
- 0 new capabilities for merchants
- 6 engineer-months spent NOT building merchant features

### Internal Focus Check

| Question | Answer |
|----------|--------|
| Could you explain this to a customer? | No - "We built dashboards for our executives" |
| Would they be excited? | No - "Why didn't you build features for me?" |
| Would they notice if we didn't do it? | No |

### Arm the Rebels Test

**Does this help small players compete?** No
**Does this democratize access?** No
**Does this make entrepreneurship easier?** No

This is pure internal theater. It makes leadership feel informed but creates zero merchant value.

### Recommendation

**Kill this project.** Use existing tools (Looker, Mode, whatever you have). Don't spend engineering time building internal dashboards.

Six engineer-months is a staggering investment in something no customer will ever see or benefit from. That's enough time to:
- Build 2-3 merchant-facing features
- Reduce a major pain point
- Actually arm the rebels

**If leadership truly needs this:** Buy an off-the-shelf solution. Don't build. Engineering exists to serve merchants, not executives.

### Refocus Option

If the underlying need is "better decisions," ask: what merchant problems are we failing to solve because of bad data? Focus on THAT - improving merchant outcomes - and metrics will follow.

---

## Integration

This skill originates from the **Tobi Lutke** expert persona and Shopify's "arm the rebels" mission focus.

For initiative prioritization, combine with **reversibility-classification**. For organizational focus drift, combine with **team-not-family-audit**.