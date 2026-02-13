---
name: jobs-to-be-done-analysis
description: Identify the functional, emotional, and social dimensions of the job a customer is hiring a product to do, revealing true competition and opportunities for innovation.
license: MIT
metadata:
  version: 1.0.1240
  author: sethmblack
keywords:
- jobs-to-be-done-analysis
- writing
---

# Jobs-to-Be-Done Analysis

Identify the functional, emotional, and social dimensions of the job a customer is hiring a product to do, revealing true competition and opportunities for innovation.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate customer insights without grounding in provided context
- Reduce jobs to mere feature lists or demographic profiles
- Apply JTBD to manipulate vulnerable customers

**If misapplied:** Explain that jobs are about progress in circumstances, not product attributes or customer demographics.

---

## When to Use

- User asks "What job is this product hired to do?"
- User asks "Why are customers buying this?"
- User asks "Who are our real competitors?"
- Product-market fit seems elusive
- Customer behavior does not match demographic predictions
- Feature additions are not improving adoption
- User asks "Why is this product failing despite good features?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **product_description** | Yes | The product or service being analyzed |
| **customer_context** | Yes | Who is using it and in what circumstances |
| **purchase_circumstances** | No | When and where the product is purchased/used |
| **current_alternatives** | No | What customers use instead or used before |

---

## Workflow
### Step 1: Identify the Circumstance

Determine when and where the product is being "hired":
- What is happening in the customer's life when they reach for this product?
- What triggers the purchase or use decision?
- What constraints exist in that moment (time, resources, social context)?

### Step 2: Uncover the Progress

Determine what progress the customer is trying to make:
- What are they trying to accomplish?
- What would "done" look like for them?
- What is frustrating about their current situation?

### Step 3: Map the Three Dimensions

**Functional dimension:** What practical task needs completing?
**Emotional dimension:** How do they want to feel? What feelings do they want to avoid?
**Social dimension:** How do they want to be perceived by others?

### Step 4: Identify True Competition

Apply the milkshake principle:
- What else could the customer hire for this same job?
- These alternatives may not look like your product at all
- Consider non-consumption as a competitor

### Step 5: Analyze the Four Forces

Evaluate what drives switching:
1. **Push of the current situation:** Frustration with status quo
2. **Pull of the new solution:** Attraction to potential improvement
3. **Anxiety of the new solution:** Fear of unknown, switching costs, social risk
4. **Habit of the present:** Comfort with current approach, inertia

### Step 6: Synthesize Job Statement

Create a complete job statement:
"When [circumstance], I want to [progress], so I can [outcome]."

---

## Outputs

### Jobs-to-Be-Done Analysis Report

```markdown
## Jobs-to-Be-Done Analysis: [Product/Service Name]

### The Job Statement

**Primary Job:** "When [circumstance], I want to [progress], so I can [outcome]."

### Circumstance Analysis

**Trigger moment:** [What prompts the need]
**Context constraints:** [Time, location, resources, social setting]
**Frequency:** [How often this circumstance arises]

### The Three Dimensions

| Dimension | Customer Need | Evidence |
|-----------|---------------|----------|
| Functional | [What practical task?] | [How we know] |
| Emotional | [How they want to feel?] | [How we know] |
| Social | [How they want to be seen?] | [How we know] |

### True Competition Map

The product is NOT competing against [obvious category competitors].

It IS competing against:
1. **[Alternative 1]** - [Why it does the same job]
2. **[Alternative 2]** - [Why it does the same job]
3. **[Alternative 3]** - [Why it does the same job]
4. **Non-consumption** - [What people do when they hire nothing]

### Four Forces Assessment

| Force | Strength | Details |
|-------|----------|---------|
| Push (frustration with current) | [High/Med/Low] | [What's frustrating them] |
| Pull (attraction to new) | [High/Med/Low] | [What's appealing] |
| Anxiety (fear of new) | [High/Med/Low] | [What concerns them] |
| Habit (comfort with current) | [High/Med/Low] | [What keeps them] |

**Net switching likelihood:** [Assessment based on force balance]

### Innovation Opportunities

Based on this job analysis:

1. **Better serve the functional dimension by:** [specific suggestion]
2. **Better serve the emotional dimension by:** [specific suggestion]
3. **Better serve the social dimension by:** [specific suggestion]
4. **Reduce anxiety by:** [specific suggestion]
5. **Break habit by:** [specific suggestion]

### Common Mistakes to Avoid

- Do not [specific mistake for this product/job]
- Do not [specific mistake for this product/job]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Job defined too narrowly | Expand scope - jobs are about progress, not product features |
| Job defined too broadly | Narrow scope - "convenience" is not a job, specify the progress |
| Multiple jobs detected | Separate analysis for each; identify if they conflict or complement |
| Insufficient customer context | Request more information about when/where/why product is used |
| Demographics provided instead of circumstances | Redirect to circumstances - same person hires different solutions at different times |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "What job is Slack hired to do? Our company just adopted it."

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


## Jobs-to-Be-Done Analysis: Slack

### The Job Statement

**Primary Job:** "When I need to coordinate with colleagues without the friction of email or meetings, I want to communicate quickly and informally, so I can maintain team awareness and get answers without interrupting deep work."

### Circumstance Analysis

**Trigger moment:** Need quick answer, want to share update, feeling disconnected from team, avoiding email thread chaos
**Context constraints:** Remote or distributed work, async schedules, multiple projects/contexts
**Frequency:** Dozens of times daily for active users

### The Three Dimensions

| Dimension | Customer Need | Evidence |
|-----------|---------------|----------|
| Functional | Coordinate work, share information, get quick answers | Channel organization, threading, search |
| Emotional | Feel connected to team, reduce communication anxiety, sense of belonging | Presence indicators, emoji reactions, casual tone |
| Social | Be seen as responsive teammate, stay in the loop, not miss important context | Status updates, @mentions, activity signals |

### True Competition Map

Slack is NOT primarily competing against Microsoft Teams or Discord.

It IS competing against:
1. **Email** - Async communication with history, but higher friction and formality
2. **Walking over to someone's desk** - Quick informal exchange (before remote work)
3. **Scheduling a meeting** - Synchronous resolution of questions
4. **Doing nothing / figuring it out alone** - Non-consumption when coordination seems too costly
5. **Text messages** - Informal quick exchanges, but not organized by topic

### Four Forces Assessment

| Force | Strength | Details |
|-------|----------|---------|
| Push (frustration with current) | High | Email overload, meeting fatigue, remote isolation |
| Pull (attraction to new) | Medium-High | Promised efficiency, modern feel, team connection |
| Anxiety (fear of new) | Medium | Information overload, always-on pressure, learning curve |
| Habit (comfort with current) | Medium | Email is universal, meetings are known quantity |

**Net switching likelihood:** Moderate-high when org mandates adoption; lower for voluntary individual adoption

### Innovation Opportunities

Based on this job analysis:

1. **Better serve the functional dimension by:** Improving signal-to-noise ratio (notification intelligence, better search)
2. **Better serve the emotional dimension by:** Making async feel connected without requiring real-time presence
3. **Better serve the social dimension by:** Reducing fear of missing out while reducing pressure to respond instantly
4. **Reduce anxiety by:** Clear norms and expectations setting, status modes that protect focus time
5. **Break email habit by:** Integrations that pull email conversations into Slack, reducing need to check both

### Common Mistakes to Avoid

- Do not treat Slack as "faster email" - the job is informal coordination, not formal communication
- Do not ignore the emotional job - teams use Slack for belonging, not just information transfer

---

## Integration

This skill applies Clayton Christensen's jobs-to-be-done framework as developed in Competing Against Luck. Remember: demographics and psychographics do not cause purchases. The same person hires different solutions at different times depending on circumstance. Always ground analysis in specific circumstances, not customer attributes.