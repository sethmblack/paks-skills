---
name: remarkable-product-audit
description: Evaluate whether a product, service, or content is remarkable enough to spread through word-of-mouth, based on Seth Godin's Purple Cow methodology.
version: 1.0.0
author: sethmblack
tags: [remarkable-product-audit, storytelling, transformation, writing]
---

# Remarkable Product Audit

Evaluate whether a product, service, or content is remarkable enough to spread through word-of-mouth, based on Seth Godin's Purple Cow methodology.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help make harmful products more appealing or spreadable
- Assist with deceptive marketing or misleading positioning
- Evaluate products designed to exploit vulnerable populations

**If asked to audit harmful products:** Decline and explain why.

---

## When to Use

- Evaluating a product, service, or content before launch
- Diagnosing why something isn't spreading or gaining traction
- Brainstorming how to make something more remarkable
- User asks: "Is this remarkable?" "Would anyone talk about this?" "How do I stand out?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `product_description` | Yes | What the product/service/content is |
| `target_audience` | No | Who it's intended for |
| `competitive_landscape` | No | What alternatives exist |
| `current_positioning` | No | How it's currently described/marketed |

---

## Workflow

### Step 1: Apply the Purple Cow Test

Evaluate against Seth Godin's four remarkability questions:

1. **Would someone make a remark about this to a friend?**
   - Not "could they" - would they actually choose to?
   - What would they say? Can you hear the conversation?
   - Is there a story worth telling?

2. **Is it safe (and therefore risky)?**
   - Safe = blends in = invisible
   - "Very good" is the enemy of remarkable
   - What edge or risk has been sanded off?

3. **What's the story people would tell?**
   - Not your marketing story - their story
   - In one sentence, what makes this worth mentioning?
   - Is it simple enough to spread?

4. **Who's the early adopter who'd love this?**
   - Not "who might buy it" - who would be obsessed?
   - Would sneezers (people with audiences) spread this?
   - Is it remarkable to a specific someone, or generically "good"?

### Step 2: Score Remarkability

Rate each dimension (1-5):

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Remark-worthy** | 1-5 | Would people actually mention this? |
| **Differentiation** | 1-5 | Does it stand out from alternatives? |
| **Story clarity** | 1-5 | Is there a clear, spreadable narrative? |
| **Sneezer appeal** | 1-5 | Would early adopters champion this? |

**Total Score Interpretation:**
- 16-20: Truly remarkable - ready to spread
- 12-15: Promising but needs sharpening
- 8-11: Too safe - significant rework needed
- 4-7: Invisible - fundamental rethinking required

### Step 3: Generate Recommendations

For scores below 16, provide specific recommendations:

1. **What to amplify** - What existing element could become the purple cow?
2. **What to cut** - What "safe" elements are diluting distinctiveness?
3. **The story reframe** - How would you reposition this to be remarkable?
4. **The ideal sneezer** - Who specifically should hear about this first?

---

## Outputs

Deliver a structured audit:

```markdown
## Remarkable Product Audit

### The Product
{one-sentence description}

### The Purple Cow Test

**1. Would someone remark on this?**
{assessment}

**2. Is it dangerously safe?**
{assessment}

**3. What's the spreadable story?**
{current story or "no clear story"}

**4. Who's the obsessed early adopter?**
{specific persona or "too generic"}

### Remarkability Score: {X}/20

| Dimension | Score | Notes |
|-----------|-------|-------|
| Remark-worthy | X/5 | {brief} |
| Differentiation | X/5 | {brief} |
| Story clarity | X/5 | {brief} |
| Sneezer appeal | X/5 | {brief} |

### Recommendations

**To make this remarkable:**
1. {specific action}
2. {specific action}
3. {specific action}

**The story should be:**
"{one-sentence spreadable story}"

**First tell:**
{specific sneezer/audience}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No product description provided | Ask for basic details before auditing |
| Product is already clearly remarkable | Confirm and identify what makes it work |
| Harmful or deceptive product | Decline to audit |
| User pushes back on "not remarkable" | Explain that remarkable is earned, not claimed |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "We're launching a new project management tool with AI features."

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


## Remarkable Product Audit

### The Product
AI-powered project management software

### The Purple Cow Test

**1. Would someone remark on this?**
Unlikely. "Project management tool with AI" is now table stakes. There are dozens of these. Nothing in this description would prompt a conversation.

**2. Is it dangerously safe?**
Yes. This is positioned as "like others, but with AI" - the safest possible positioning in 2026. Safe = invisible.

**3. What's the spreadable story?**
No clear story. "It has AI" is not a story anyone tells. What specific outcome does the AI enable that was impossible before?

**4. Who's the obsessed early adopter?**
Too generic. "People who manage projects" is everyone and no one.

### Remarkability Score: 6/20

| Dimension | Score | Notes |
|-----------|-------|-------|
| Remark-worthy | 1/5 | Nothing to talk about |
| Differentiation | 2/5 | AI is now commodity |
| Story clarity | 1/5 | No story exists |
| Sneezer appeal | 2/5 | No specific champion |

### Recommendations

**To make this remarkable:**
1. Find ONE thing your AI does that competitors cannot - make that the entire product
2. Choose a specific, narrow audience (agencies? hardware startups? nonprofits?) and make it perfect for them
3. Remove features, don't add them - what can you take away that makes you different?

**The story should be:**
"It's the project tool that [specific surprising outcome] in [specific context]"

**First tell:**
Identify 10 people who have publicly complained about existing tools - your first sneezers.

---

## Integration

This skill originates from the **seth-godin** expert. When invoked within that expert context, maintain Seth's characteristic brevity and question-driven voice.

---

## Success Criteria

Audit is complete when:
- [ ] All four Purple Cow questions answered
- [ ] Remarkability score calculated with evidence
- [ ] Specific, actionable recommendations provided
- [ ] Spreadable story articulated (or gap identified)
- [ ] First sneezer/audience identified (or gap identified)