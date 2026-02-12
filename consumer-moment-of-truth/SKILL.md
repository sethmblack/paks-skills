---
name: consumer-moment-of-truth
description: Analyze the consumer experience at the two critical moments: the purchase decision (First Moment) and the usage experience (Second Moment).
version: 1.0.0
author: sethmblack
tags: [consumer-moment-of-truth, writing]
---

# Consumer Moment of Truth

Analyze the consumer experience at the two critical moments: the purchase decision (First Moment) and the usage experience (Second Moment).

**Token Budget:** ~550 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Analyze how to manipulate or deceive consumers
- Help exploit psychological vulnerabilities
- Develop dark patterns or deceptive practices

---

## When to Use

- User asks "Why do consumers choose us?" or "Do we win at the shelf?"
- User is analyzing brand or product performance
- User is making marketing or product development investments
- User asks about consumer experience or preference
- User wants to understand competitive dynamics from consumer perspective

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `product_service` | Yes | The product or service being analyzed |
| `consumer_segment` | Yes | The specific consumer being analyzed |
| `competitors` | No | Key competitive alternatives |
| `current_data` | No | Any existing consumer research or data |

---

## Workflow
### Step 1: 1. Define the Consumer

Before analyzing moments of truth:
- Who specifically is the consumer?
- What problem are they trying to solve?
- What are their unarticulated needs (not just what they say)?

**Principle:** "The consumer is boss."

### Step 2: 2. Analyze the First Moment of Truth

The **First Moment** occurs at the purchase decision:

**Physical retail:**
- At the shelf, what do they see?
- How do we stand out vs. alternatives?
- What triggers the choice?

**Digital:**
- In search results or marketplace
- On the website or app
- At the conversion point

**Key questions:**
- Why do they choose us over alternatives?
- What would make them choose a competitor?
- What friction exists in choosing us?
- Is our promise clear and compelling?

### Step 3: 3. Analyze the Second Moment of Truth

The **Second Moment** occurs during usage:

- Does the product/service deliver on the promise?
- Are they delighted or just satisfied?
- Would they repurchase?
- Would they recommend to others?

**Key questions:**
- What is the actual usage experience?
- Does reality match or exceed expectations?
- What frustrations exist?
- What moments create delight?

### Step 4: 4. Assess Win/Lose Status

For each moment:
- **WIN** - Consumer consistently chooses us / delighted
- **COMPETITIVE** - Split with alternatives / satisfied
- **LOSE** - Competitors preferred / disappointed

### Step 5: 5. Identify Improvement Priorities

Based on assessment:
- What must change to win both moments?
- Which moment is the bigger problem?
- What investments would shift consumer choice?

---

## Outputs

Produce a **Moment of Truth Assessment**:

```markdown
## Consumer Moment of Truth: [Product/Service]

### Consumer Definition
- **Who:** [specific consumer]
- **Problem:** [what they're solving]
- **Unarticulated needs:** [what they don't say but need]

### First Moment of Truth (Purchase)

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Visibility | [Strong/Weak] | [data] |
| Promise clarity | [Strong/Weak] | [data] |
| Competitive differentiation | [Strong/Weak] | [data] |
| Friction | [Low/High] | [data] |

**Verdict:** WIN / COMPETITIVE / LOSE

**Why they choose us:** [or why they don't]

### Second Moment of Truth (Usage)

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Promise delivery | [Exceeds/Meets/Falls short] | [data] |
| Delight moments | [Many/Few/None] | [data] |
| Pain points | [Few/Many] | [data] |
| Repurchase intent | [High/Medium/Low] | [data] |

**Verdict:** WIN / COMPETITIVE / LOSE

**Usage reality:** [key insight]

### Summary Assessment

|  | First Moment | Second Moment |
|--|--------------|---------------|
| Status | [WIN/LOSE] | [WIN/LOSE] |
| Priority | [1-5] | [1-5] |

### Improvement Priorities
1. **[Priority]** - Impact on [moment]: [expected shift]
2. **[Priority]** - Impact on [moment]: [expected shift]

### Consumer Insight
[One key insight about this consumer that should drive decisions]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Generic "customers" discussed | Require: "Who specifically? Tell me about her life." |
| No consumer data | Recommend: "We need to observe consumers, not assume" |
| Focus on just one moment | Warn: "Must win both moments - one without the other fails" |
| Product-focused discussion | Redirect: "Let's start with what the consumer needs, not what we make" |

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
Product: Olay Regenerist moisturizer
Consumer: Women 35-50 who want to fight visible aging but aren't ready for expensive prestige brands
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


## Consumer Moment of Truth: Olay Regenerist

### Consumer Definition
- **Who:** Women 35-50, mass-market shoppers, aging concerns emerging
- **Problem:** Want to address visible aging signs without prestige prices
- **Unarticulated needs:** Want to feel they're taking action on aging; want "permission" to use serious skincare at accessible price

### First Moment of Truth (Purchase)

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Visibility | Strong | Premium placement in mass retail, distinctive packaging |
| Promise clarity | Strong | "Regenerist" name implies renewal; clinical claims visible |
| Competitive differentiation | Strong | Prestige-quality positioning at mass price |
| Friction | Low | Available everywhere she shops |

**Verdict:** WIN

**Why they choose us:** Offers prestige-style skincare promise at an accessible price point. She feels she's "doing something serious" about aging without the guilt of overspending.

### Second Moment of Truth (Usage)

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Promise delivery | Meets expectations | Visible smoothing, hydration; clinical efficacy |
| Delight moments | Moderate | Premium texture, subtle fragrance |
| Pain points | Few | Some find texture too heavy for morning use |
| Repurchase intent | High | Strong loyalty among core users |

**Verdict:** WIN

**Usage reality:** Product delivers on "serious skincare" promise. Texture and experience feel more premium than price suggests. She feels she made a smart choice.

### Summary Assessment

|  | First Moment | Second Moment |
|--|--------------|---------------|
| Status | WIN | WIN |
| Priority | 3 (maintain) | 3 (maintain) |

### Improvement Priorities
1. **Lighter-weight formulation option** - Impact on Second Moment: Address morning-use concern, expand usage occasions
2. **Strengthen clinical messaging** - Impact on First Moment: Reinforce prestige-quality positioning

### Consumer Insight
She wants to feel smart, not cheap. The value proposition isn't "save money" - it's "get prestige quality without prestige price." The emotional win is feeling savvy, not frugal.

---

## Integration

This skill connects to:
- `where-to-play-analysis` - Consumer segment defines where-to-play
- `how-to-win-diagnosis` - Winning moments of truth is the proof of how-to-win
- `winning-aspiration-definition` - Winning with consumers is the ultimate aspiration

**Source:** A.G. Lafley, P&G "Two Moments of Truth" framework (2005)