---
name: bhag-creation
description: Create compelling Big Hairy Audacious Goals (BHAGs) - bold 10-25 year goals that serve as unifying focal points and catalysts for team spirit, with clear finish lines and energizing power.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.455
keywords:
- absurdist
- bhag-creation
- transformation
- writing
---

# BHAG Creation

Create compelling Big Hairy Audacious Goals (BHAGs) - bold 10-25 year goals that serve as unifying focal points and catalysts for team spirit, with clear finish lines and energizing power.

**Token Budget:** ~800 tokens. Reserve tokens for BHAG output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create BHAGs that are merely stretch goals or annual targets
- Accept vague aspirations without clear finish lines
- Generate BHAGs without understanding core values and purpose
- Create goals with near-100% or near-0% chance of success

**If values are unclear:** A BHAG without core values is dangerous. Recommend values clarification first.

---

## When to Use

- User asks "What's our big goal?" or "What should we aim for?"
- Organization needs a compelling long-term vision
- Strategic planning requires a unifying focal point
- Team lacks inspiration and shared direction
- User explicitly requests BHAG development

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `organization_context` | Yes | What the organization does, core purpose | Must have clear identity |
| `core_values` | Yes | Fundamental principles that won't change | At least 3-5 enduring values |
| `current_state` | Yes | Where the organization is today | Honest assessment |
| `time_horizon` | No | Preferred BHAG timeline | Default: 10-25 years |
| `bhag_type` | No | Preferred BHAG category | If known |

---

## Background: The BHAG

From Collins and Porras' *Built to Last* research:

> "A BHAG is a huge and daunting goal - like a big mountain to climb. It is clear, compelling, and people 'get it' right away. A BHAG serves as a unifying focal point of effort, galvanizing people and creating team spirit as people strive toward a finish line."

**Key characteristics:**
- Clear finish line (you know when you've achieved it)
- Engages people emotionally, not just intellectually
- 50-70% chance of success (not guaranteed, not impossible)
- 10-25 year time horizon
- Consistent with core values

---

## Workflow
### Phase 1: Validate Prerequisites

Before creating a BHAG, verify:

**Core Values Check:**
- Are the values truly enduring (would hold for 100 years)?
- Are they authentic (not aspirational)?
- Are there 3-5 core values maximum?

**Core Purpose Check:**
- Is there a reason for being beyond making money?
- Would the purpose remain valid even if the industry changed?

**If prerequisites are weak:** Recommend values/purpose work before BHAG creation.

### Phase 2: Determine BHAG Type

Collins and Porras identify four BHAG categories:

| Type | Description | Best For |
|------|-------------|----------|
| **Target** | Quantitative or qualitative target | Clear metrics available |
| **Common Enemy** | David vs. Goliath against a competitor | Strong rival exists |
| **Role Model** | Become like another admired organization | Aspirational model exists |
| **Internal Transformation** | Fundamental change in what organization is | Need dramatic reinvention |

**Questions to determine type:**

### Step 1: Is there a clear metric that would represent audacious success? (Target)



### Step 2: Is there a dominant competitor you want to dethrone? (Common Enemy)



### Step 3: Is there an organization you greatly admire and want to emulate? (Role Model)



### Step 4: Does the organization need to become something fundamentally different? (Transformation)



### Phase 3: Generate BHAG Candidates

**For Target BHAGs:**
- What would represent 10X current performance?
- What achievement would make headlines?
- What milestone would make current leaders proud decades later?

Example format: "Achieve [specific measurable outcome] by [year]"

**For Common Enemy BHAGs:**
- Who is the Goliath in your industry?
- What would it mean to beat them?
- What specific victory would symbolize triumph?

Example format: "Beat [competitor] in [specific dimension] by [year]"

**For Role Model BHAGs:**
- What organization do you most admire?
- What qualities would you need to emulate?
- What would it mean to be "the [X] of your industry"?

Example format: "Become the [admired company] of [your industry] in [time]"

**For Transformation BHAGs:**
- What would your organization need to become?
- What current identity would you leave behind?
- What fundamental change is required?

Example format: "Transform from [current state] to [future state] by [year]"

### Phase 4: Apply BHAG Tests

Each candidate must pass:

| Test | Question | Pass Criteria |
|------|----------|---------------|
| Finish Line | Can you know when you've achieved it? | Yes, objectively verifiable |
| Engagement | Does it grab people in the gut? | Emotional response, not just intellectual |
| Probability | 50-70% chance of success? | Bold but not absurd |
| Time Horizon | 10-25 years out? | Long enough to be audacious |
| Values Aligned | Consistent with core values? | Achieving it wouldn't violate values |

### Phase 5: Deliver BHAG

---

## Output Format

```markdown
## BHAG Development: [Organization Name]

### Prerequisites Check

**Core Values:** [Validated/Needs Work]
- [List verified core values]

**Core Purpose:** [Validated/Needs Work]
- [Purpose statement]

### BHAG Type Selected: [Target/Common Enemy/Role Model/Transformation]

**Rationale:** [Why this type fits]

### Proposed BHAG

> "[The BHAG statement]"

### BHAG Analysis

**Finish Line:** [How you'll know it's achieved]

**Time Horizon:** [Target year/timeframe]

**Probability Assessment:** [X]% chance of success
- Factors in favor: [List]
- Factors against: [List]

**Emotional Engagement Test:**
- Does it inspire? [Assessment]
- Do people "get it" immediately? [Assessment]
- Does it create team spirit? [Assessment]

**Values Alignment:**
- [How BHAG aligns with each core value]

### Alternative BHAGs (if applicable)

**Option 2:** "[Alternative BHAG]"
- Type: [Type]
- Trade-offs: [Comparison to primary]

### Implementation Considerations

**What must be true** for this BHAG to be achieved:
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

**Near-term implications:**
- [What changes now because of this BHAG]

**Warning signs** the BHAG may be wrong:
- [Early indicator 1]
- [Early indicator 2]

### Famous BHAG Examples (Reference)

- JFK: "Land a man on the moon and return him safely to the earth before this decade is out"
- Microsoft (1980s): "A computer on every desk and in every home"
- Sony (1950s): "Become the company most known for changing the worldwide poor-quality image of Japanese products"
- Walmart (1990): "Become a $125 billion company by the year 2000"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Values aren't clear | Stop; recommend values work first - BHAG without values is dangerous |
| BHAG is too easy (90%+ probability) | Not a BHAG - it's just a goal. Push for more audacity. |
| BHAG is absurd (10% probability) | Not a BHAG - it's a fantasy. Ground in possibility. |
| No clear finish line | Revise until achievement is objectively verifiable |
| User wants multiple BHAGs | Organizations need ONE primary BHAG at a time for focus |
| BHAG feels uninspiring | Go back to what they're passionate about; BHAG must engage emotionally |

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

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill is part of the **Jim Collins** expert persona. When invoked:
- Emphasize the balance: audacious but achievable (50-70%)
- Connect to core values and purpose
- Insist on clear finish lines
- Reference Built to Last research examples

---

## Success Criteria

BHAG creation is complete when:

1. Core values and purpose have been validated
2. BHAG type has been selected with rationale
3. BHAG statement is clear with specific finish line
4. Probability has been assessed (50-70% target)
5. Emotional engagement has been tested
6. Values alignment has been confirmed
7. Implementation considerations are noted