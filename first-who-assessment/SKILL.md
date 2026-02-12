---
name: first-who-assessment
description: Evaluate team composition against Jim Collins' "First Who, Then What"
  criteria. Assess whether the right people are on the bus, in the right seats, before
  addressing strategy.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- first-who-assessment
- transformation
- writing
---

# First Who Assessment

Evaluate team composition against Jim Collins' "First Who, Then What" criteria. Assess whether the right people are on the bus, in the right seats, before addressing strategy.

**Token Budget:** ~800 tokens. Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide assessment for purposes of unfair termination or discrimination
- Make judgments without behavioral evidence
- Skip the self-motivation assessment
- Provide simplistic "fire them" recommendations without nuance

**If used for harm:** This framework is for building great teams, not for justifying predetermined decisions.

---

## When to Use

- User asks "Do we have the right team?" or "Who should be on the bus?"
- Hiring decisions need to be evaluated
- Team restructuring is being considered
- Strategy discussions are happening without team assessment
- User explicitly requests First Who analysis

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `team_context` | Yes | Organization, team purpose, scope | Must define the "bus" |
| `team_members` | Yes | Who is currently on the team | At least basic role info |
| `observed_behaviors` | Yes | What people actually do, not job titles | Concrete evidence |
| `strategic_direction` | No | Where the bus is going | Used for seat assessment |

---

## Background: First Who, Then What

From Jim Collins' *Good to Great* research:

> "The executives who ignited the transformations from good to great did not first figure out where to drive the bus and then get people to take it there. No, they first got the right people on the bus (and the wrong people off the bus) and then figured out where to drive it."

**Three simple truths:**

1. **Adaptability:** If you begin with "who" rather than "what," you can more easily adapt to a changing world.

2. **Self-motivation:** The right people don't need to be tightly managed or fired up; they will be self-motivated by the inner drive to produce the best results.

3. **Great vision requires great people:** If you have the wrong people, it doesn't matter whether you discover the right direction; you still won't have a great company.

**The three dimensions:**
- Right people ON the bus
- Wrong people OFF the bus
- Right people in the RIGHT SEATS

---

## Workflow
### Phase 1: Define the Bus

Before assessing who's on it, clarify what the bus is:

**Questions:**

### Step 1: What is this team's purpose?



### Step 2: What journey is this bus taking?



### Step 3: What makes someone "right" for THIS bus specifically?



Different buses need different people. A startup bus differs from a turnaround bus differs from a scaling bus.

### Phase 2: Assess "Right Person" Criteria

Collins' research identified characteristics of right people:

| Criterion | Assessment Question | Evidence to Look For |
|-----------|---------------------|---------------------|
| **Character** | Do they share core values? | Alignment in difficult decisions |
| **Capability** | Can they be the best at their role? | Track record, not potential |
| **Self-motivation** | Do they need to be managed/motivated? | Internal drive, not external |
| **Commitment** | Are they committed to this specific bus? | Actions, not words |
| **Chemistry** | Do others want them on the bus? | Team dynamics, trust |

**Key insight:** "Right person" is about character and capability, not specific skills. Skills can be taught; character cannot.

### Phase 3: The Bus Audit

For each team member, assess:

**On/Off Assessment:**
- Would you enthusiastically rehire this person?
- If they told you they were leaving, would you fight to keep them?
- If you could go back, would you hire them again?

**Right Seat Assessment:**
- Are they in a role that uses their strengths?
- Are they in a role where they can be the best?
- Is there energy or depletion in their current role?

### Phase 4: Seat Analysis

Even right people in wrong seats fail:

| Seat Problem | Indicators | Solution |
|--------------|------------|----------|
| Overstretched | Overwhelmed, dropping balls | Reduce scope or add support |
| Underutilized | Bored, disengaged, checking out | Expand responsibility |
| Mismatched | Competent but wrong fit | Find better-fit seat |
| Absent | Seat is empty | Fill with right person |

**Warning:** An empty seat is better than a wrong person. Let a seat go unfilled until you find the right person.

### Phase 5: Decision Framework

**When to keep and develop:**
- Right person, developing capability
- Right person, wrong seat (can move)
- Right person, temporary underperformance

**When to move to a different seat:**
- Right person, clearly wrong role
- Strengths lie elsewhere
- Would thrive in different position

**When to help off the bus:**
- Wrong person (character or values)
- Cannot be best at any needed role
- Requires constant management/motivation
- Bringing down others

### Phase 6: Deliver Assessment

---

## Output Format

```markdown
## First Who Assessment: [Team/Organization Name]

### The Bus Definition

**Purpose:** [What is this team for?]
**Journey:** [Where is the bus going?]
**Right Person Profile:** [What makes someone right for THIS bus?]

### Team Audit Summary

| Status | Count | Action Needed |
|--------|-------|---------------|
| Right person, right seat | X | Retain, challenge, grow |
| Right person, wrong seat | X | Move to better fit |
| Wrong person on bus | X | Help off with dignity |
| Empty seats | X | Fill with right people |

### Individual Assessments

**[Person 1 Name/Role]**
- Bus Status: [Right person / Wrong person]
- Seat Status: [Right seat / Wrong seat / Needs evaluation]
- Evidence: [Specific observations]
- Recommendation: [Action]

**[Person 2 Name/Role]**
[Same format]

### Key Findings

**Strength patterns:**
- [What's working well with current team composition]

**Gap patterns:**
- [Missing capabilities or roles]

**Concern patterns:**
- [Systemic issues with team composition]

### The Hard Questions

1. **If you were starting over, who would you enthusiastically rehire?**
   - [Assessment]

2. **Who are you holding onto that you shouldn't be?**
   - [Assessment]

3. **What seats are empty that you've been tolerating?**
   - [Assessment]

### Recommendations

**Immediate (30 days):**
1. [Specific action]

**Near-term (90 days):**
1. [Specific action]

**Ongoing:**
1. [Disciplined approach to "First Who"]

### Hiring Principles Going Forward

1. When in doubt, don't hire - keep looking
2. When you know you need to make a people change, act
3. Put your best people on your biggest opportunities, not your biggest problems
4. Great vision without great people is irrelevant
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient behavioral evidence | Cannot assess; request specific observations |
| Assessment request to justify predetermined decision | Refuse; this is for honest assessment |
| All people marked as "wrong" | Unlikely to be accurate; re-examine criteria or leadership |
| User wants to skip to strategy | Redirect; First Who is literally first |
| People being assessed are absent from input | Note what cannot be assessed |

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
- Insist that people come before strategy
- Emphasize character over skills
- Challenge the "good enough" person in wrong seat
- Reference the research: right people are self-motivated

---

## Success Criteria

Assessment is complete when:

1. The bus has been clearly defined
2. Each team member has been assessed on right person criteria
3. Seat fit has been evaluated
4. Clear recommendations exist for each person
5. Hard questions have been honestly answered
6. Hiring principles for the future are established