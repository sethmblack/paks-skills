---
name: expected-behaviors-design
description: Design a set of explicit expected behaviors for a team or organization, formatted for easy reference and accountability conversations.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.924
repository: https://github.com/sethmblack/paks-skills
keywords:
- expected-behaviors-design
- writing
---

# Expected Behaviors Design

Design a set of explicit expected behaviors for a team or organization, formatted for easy reference and accountability conversations.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for output generation.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create behaviors designed to suppress dissent or honest feedback
- Design behaviors that enable discrimination or harassment
- Build behavior lists as tools for arbitrary punishment
- Create expectations that violate ethical or legal standards

**If asked to create suppressive behaviors:** Refuse explicitly. Explain that expected behaviors should elevate, not control.

---

## When to Use

- User needs to establish team or organizational values
- Current values are vague or not actionable
- User asks "What behaviors should we expect?"
- Team culture is drifting and needs anchoring
- New team formation needs behavioral foundation
- User wants to create a "culture card" or values document

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **context** | Yes | Team/organization type and mission |
| **existing_values** | No | Current stated values (if any) |
| **challenges** | No | Specific cultural challenges to address |
| **format** | No | Desired output format (card, poster, document) |

**Input Validation:**
- `context`: Must describe the team/org clearly enough to tailor behaviors

---

## Workflow
### Step 1: 1. Identify Behavioral Categories

Standard categories (adapt based on context):

| Category | Focus |
|----------|-------|
| Excellence | Craft, quality, continuous improvement |
| Communication | Clarity, candor, transparency |
| Relationships | Trust, respect, collaboration |
| Accountability | Ownership, follow-through, results |
| Culture | Fun, inclusion, psychological safety |
| Values | Integrity, service, role modeling |

### Step 2: 2. Draft Behaviors

For each category, create 2-3 specific, observable behaviors:

**Format:** "[Action verb] + [specific behavior] + [brief why/how]"

**Good examples:**
- "Demonstrate functional and technical excellence - Master your domain"
- "Communicate clearly, concisely, and candidly - Clarity over comfort"
- "Have fun, never at others' expense - Joy that lifts everyone"

**Avoid:**
- Vague: "Be professional"
- Abstract: "Show integrity"
- Unmeasurable: "Care about quality"

### Step 3: 3. Balance Positive and Boundary-Setting

Include both:
- **Aspirational:** What we strive for
- **Boundary:** What we never do

Example boundary behavior:
- "Have fun, never at others' expense" (includes boundary)

### Step 4: 4. Test for Observability

For each behavior, ask:
- Can I observe this in action?
- Can I give specific feedback referencing this?
- Would two people agree on whether someone is doing this?

### Step 5: 5. Format for Daily Reference

Create physical artifact:
- Card-sized: 10-16 behaviors, brief descriptions
- Poster: Full descriptions with examples
- Digital: Searchable with examples and stories

---

## Outputs

### Expected Behaviors Card

```markdown
# [Team/Organization Name] Expected Behaviors

## Excellence
- **[Behavior 1]** - [Brief description]
- **[Behavior 2]** - [Brief description]

## Communication
- **[Behavior 3]** - [Brief description]
- **[Behavior 4]** - [Brief description]

## Relationships
- **[Behavior 5]** - [Brief description]
- **[Behavior 6]** - [Brief description]

## Accountability
- **[Behavior 7]** - [Brief description]
- **[Behavior 8]** - [Brief description]

## Culture
- **[Behavior 9]** - [Brief description]
- **[Behavior 10]** - [Brief description]

## Values
- **[Behavior 11]** - [Brief description]
- **[Behavior 12]** - [Brief description]

---

*These behaviors are expectations for everyone. Own them. Model them. Hold each other accountable to them.*
```

### Accountability Framework

```markdown
## Using Expected Behaviors

### For Feedback
Reference specific behavior:
"I want to acknowledge how you [specific action] - that's exactly what we mean by [behavior name]."

"I noticed [specific action]. Can we talk about how that relates to our expectation to [behavior name]?"

### For Hiring
Evaluate candidates against behaviors:
- Can they demonstrate [behavior]?
- Do their references confirm [behavior]?
- Did interview reveal [behavior] or its opposite?

### For Evaluation
Rate against each behavior:
- Consistently demonstrates
- Usually demonstrates
- Inconsistently demonstrates
- Rarely demonstrates

### Values vs. Skills Rule
- **Values violations:** Zero tolerance. Address immediately.
- **Skill gaps:** Patience and coaching. Develop over time.

"Skills can be taught; character cannot."
```

---

## Reference Behaviors (Adapt, Don't Copy)

From Alan Mulally's One Ford Card:

| Behavior | Description |
|----------|-------------|
| Demonstrate functional and technical excellence | Master your domain |
| Have a continuous improvement philosophy | Always get better |
| Build strong relationships | Trust enables speed |
| Communicate clearly, concisely, and candidly | Clarity over comfort |
| Improve quality, safety, and sustainability | Non-negotiable standards |
| Have fun, never at others' expense | Joy without cruelty |
| Set high expectations and inspire others | Lead by example |
| Hold each other accountable | Mutual accountability, not blame |
| Foster teamwork | Work together as one team |
| Own working together | Personal responsibility for culture |
| Role model [organization] values | Embody what you expect |
| Have a "can do, find a way" attitude | Emotional resilience |
| Ensure process discipline | Structure creates results |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Too many behaviors (>16) | Consolidate; more than 16 loses memorability |
| Behaviors too vague | Add specific actions and examples |
| All aspirational, no boundaries | Add "never" statements for critical boundaries |
| Conflict with existing stated values | Reconcile or recommend replacing existing |
| Leadership doesn't model behaviors | Note as implementation risk; behaviors fail if not modeled |

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
context: 20-person DevOps team responsible for platform reliability
existing_values: "Move fast and fix things" (informal)
challenges: Blame culture after incidents, silos between sub-teams,
           inconsistent on-call practices
format: wallet card
```

**Output:** [12 behaviors organized by category, addressing specific challenges like "Treat incidents as learning opportunities, not blame opportunities" and "Share knowledge across teams proactively." Formatted for card printing with accountability guide.]

---

## Integration

This skill integrates with:
- **values-first-evaluation** - Uses expected behaviors for evaluation criteria
- **transparency-culture-launch** - "Communicate candidly" supports transparency
- **business-plan-review-design** - BPR rules should reference expected behaviors

**Source Expert:** Alan Mulally - Based on the One Ford Card with 16 expected behaviors distributed to all employees.