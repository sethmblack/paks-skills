---
name: permission-interruption-diagnosis
description: Evaluate marketing and communication strategies against Seth Godin's permission marketing principles to determine if you're earning attention or stealing it.
license: MIT
metadata:
  version: 1.0.1603
  author: sethmblack
keywords:
- permission-vs.-interruption-diagnosis
- writing
---

# Permission vs. Interruption Diagnosis

Evaluate marketing and communication strategies against Seth Godin's permission marketing principles to determine if you're earning attention or stealing it.

**Token Budget:** ~700 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help optimize spam, deceptive marketing, or manipulation tactics
- Advise on circumventing consent or privacy preferences
- Assist with marketing designed to exploit or mislead

**If asked to diagnose harmful marketing:** Decline and explain why.

---

## When to Use

- Evaluating a marketing strategy or campaign
- Diagnosing why marketing efforts aren't working
- Planning customer communication approaches
- User asks: "Am I interrupting or earning permission?" "Is this spam?" "How do I get attention?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `marketing_approach` | Yes | The strategy, campaign, or communication being evaluated |
| `audience_relationship` | No | Current relationship with the audience |
| `touchpoints` | No | How and where you reach people |
| `response_data` | No | Engagement metrics, unsubscribes, complaints |

---

## Workflow

### Step 1: The Three Permission Tests

Evaluate against Seth Godin's core criteria:

**1. Is it anticipated?**
- Did they explicitly ask to hear from you?
- Would they be surprised to receive this?
- Are you showing up when expected, or intruding?

**2. Is it personal?**
- Is this relevant to them specifically?
- Could this message only work for this person?
- Or is it generic broadcast to everyone?

**3. Is it relevant?**
- Does this solve a problem they have right now?
- Is the timing right?
- Would they thank you for this information?

### Step 2: Classify the Approach

| Classification | Characteristics | Example |
|----------------|-----------------|---------|
| **Pure Permission** | All 3 tests pass | Email to subscriber about topic they signed up for |
| **Partial Permission** | 1-2 tests pass | Relevant email but unexpected timing |
| **Interruption** | 0 tests pass | Cold outreach, uninvited ads |

### Step 3: Locate on the Permission Ladder

Where does the current relationship sit?

| Level | Description | Examples |
|-------|-------------|----------|
| 5. **Intravenous** | They've delegated decisions to you | Amazon Subscribe & Save |
| 4. **Points/Loyalty** | Transactional trust | Frequent flyer programs |
| 3. **Personal** | Direct relationship | Followed creator |
| 2. **Brand Trust** | General positive association | Familiar company |
| 1. **Situation** | One-time, context-specific | Single transaction |
| 0. **Stranger** | No relationship | Cold prospect |

### Step 4: Diagnose and Recommend

Based on classification:

**If Interruption:**
- What permission could you earn first?
- What value could you provide before asking?
- How can you become anticipated?

**If Partial Permission:**
- Which test is failing?
- How can you increase relevance or personalization?
- What's eroding the permission you had?

**If Pure Permission:**
- How do you maintain and deepen it?
- What's the next level of the ladder?
- How do you earn more permission over time?

---

## Outputs

Deliver a structured diagnosis:

```markdown
## Permission vs. Interruption Diagnosis

### The Approach
{one-sentence description of what's being evaluated}

### The Three Permission Tests

| Test | Result | Evidence |
|------|--------|----------|
| **Anticipated** | Pass/Fail | {why} |
| **Personal** | Pass/Fail | {why} |
| **Relevant** | Pass/Fail | {why} |

### Classification: {Pure Permission / Partial Permission / Interruption}

### Permission Ladder Position

**Current Level:** {level name and number}
**Next Level:** {what it would take to advance}

### Diagnosis

{2-3 sentences explaining the core issue or strength}

### Recommendations

**To earn more permission:**
1. {specific action}
2. {specific action}
3. {specific action}

**Stop doing:**
{what to eliminate that's eroding permission}

**Start doing:**
{what to add that builds permission}

### The Permission Test

Before every communication, ask:
> "Would they miss this if it didn't arrive?"

If the answer is no, you haven't earned the right to send it.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| "But everyone does cold outreach" | Just because it's common doesn't mean it works. Diagnose alternatives. |
| Low response rates provided | Use as evidence for interruption diagnosis |
| User believes they have permission they don't | Gently challenge - did they ask, or did you assume? |
| Clearly spam/deceptive | Decline to optimize; explain ethical alternatives |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "We're sending weekly emails to people who downloaded our ebook. Open rates dropped from 40% to 12%."

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


## Permission vs. Interruption Diagnosis

### The Approach
Weekly emails to ebook download leads

### The Three Permission Tests

| Test | Result | Evidence |
|------|--------|----------|
| **Anticipated** | Partial | They opted in, but for an ebook - weekly emails may not have been expected |
| **Personal** | Fail | If open rates are 12%, content likely isn't personally relevant |
| **Relevant** | Fail | Declining engagement suggests timing or content isn't resonating |

### Classification: Partial Permission (eroding)

### Permission Ladder Position

**Current Level:** 2 - Brand Trust (and declining)
**Next Level:** 3 - Personal Relationship (requires relevance and anticipation)

### Diagnosis

You had permission at download, but you're spending it faster than you're earning it. Every irrelevant email trains them to ignore you. The 40% to 12% drop is your permission eroding in real-time.

### Recommendations

**To earn more permission:**
1. **Segment ruthlessly** - What did they download the ebook for? Send different content to different interests.
2. **Ask what they want** - Send one email asking: "What are you struggling with? Reply and tell me." Then actually address it.
3. **Reduce frequency, increase value** - Better to send one remarkable email a month than four forgettable ones.

**Stop doing:**
Weekly emails that feel like obligations. Generic content that could go to anyone.

**Start doing:**
Emails so valuable they forward them. Content so specific they think "how did they know I needed this?"

### The Permission Test

Before every communication, ask:
> "Would they miss this if it didn't arrive?"

At 12% open rate, 88% of your list wouldn't notice if you disappeared. That's your signal.

---

## Integration

This skill originates from the **seth-godin** expert. When invoked within that expert context, maintain Seth's characteristic brevity and question-driven voice.

---

## Success Criteria

Diagnosis is complete when:
- [ ] All three permission tests evaluated with evidence
- [ ] Classification clearly stated
- [ ] Current ladder position identified
- [ ] Specific, actionable recommendations provided
- [ ] User understands the permission they have (or don't have)