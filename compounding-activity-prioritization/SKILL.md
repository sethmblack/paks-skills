---
name: compounding-activity-prioritization
description: Identify which activities compound over time versus remain linear, enabling ruthless prioritization toward exponential returns.
license: MIT
metadata:
  version: 1.0.614
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- compounding-activity-prioritization
- compression
- writing
---

# Compounding Activity Prioritization

Identify which activities compound over time versus remain linear, enabling ruthless prioritization toward exponential returns.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend neglecting health, relationships, or ethics as "linear" activities
- Dismiss legally required activities as non-compounding
- Advocate for unsustainable work patterns in pursuit of compounding
- Fabricate compounding claims without logical basis

**Important nuance:** Some "linear" activities (rest, relationships, compliance) are prerequisites for compounding. Don't optimize them away.

---

## When to Use

- User asks "What should I focus on?"
- Career or strategic planning decisions
- Time allocation reviews
- User asks "What compounds?"
- Resource allocation with long time horizons
- When someone is busy but not building toward anything

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **activities** | Yes | List of potential activities, investments, or focus areas |
| **time_horizon** | No | Relevant planning window (default: 5 years) |
| **current_constraints** | No | Resource limitations (time, money, energy) |
| **domain** | No | Context (career, business, infrastructure, personal) |

---

## Workflow
### 1. Understand the Compounding Mechanism

Compounding requires:
- **Base that persists:** The output of work remains valuable over time
- **Returns that build:** Later efforts benefit from earlier efforts
- **Positive feedback loop:** Success enables more success

Linear activities have:
- One-time value that depletes
- No accumulation effect
- Effort resets each time

**Output:** Clear understanding of what compounding means in this domain.

### 2. Classify Each Activity

Apply the compounding test to each activity:

| Question | Compounding Answer | Linear Answer |
|----------|-------------------|---------------|
| Does today's work make tomorrow's work easier? | Yes | No |
| Does the value persist after completion? | Yes | Diminishes |
| Do returns accelerate over time? | Yes | Stay flat |
| Is there a network effect? | Yes | No |

**Categories:**
- **COMPOUNDING:** Meets 3-4 criteria (build, prioritize heavily)
- **MIXED:** Meets 1-2 criteria (do strategically)
- **LINEAR:** Meets 0 criteria (minimize or delegate)
- **PREREQUISITE:** Linear but enables compounding (maintain, don't over-invest)

**Output:** Classified activity list with compounding rationale.

### 3. Identify High-Compounders

Sam Altman's canonical compounding activities:
- Building your network
- Writing publicly
- Learning to code (or other leverage skills)
- Getting healthy (enables all else)
- Building platforms others use
- Developing reputation
- Creating systems that run without you

In technical domains:
- Automation (reduces future effort)
- Documentation (prevents knowledge loss)
- Standards (reduces coordination cost)
- Training others (multiplies capability)
- Building reusable components (amortizes investment)

**Output:** Identification of highest-compounding activities in the list.

### 4. Calculate the Compounding Gap

For current time allocation:
- What % goes to compounding activities?
- What % goes to linear activities?
- What would a 10% shift toward compounding look like?

**Altman's observation:** "Most of what people spend time on doesn't compound. This is a huge arbitrage opportunity."

**Output:** Current allocation vs recommended allocation.

### 5. Recommend Reallocation

For maximum compounding:

### Step 1: Identify linear activities that can be eliminated or delegated



### Step 2: Identify compounding activities that deserve more time



### Step 3: Propose specific reallocation with expected impact



**Output:** Concrete recommendations with reasoning.

---

## Outputs

### Compounding Activity Analysis

```markdown
## Compounding Activity Analysis

**Domain:** {career/business/infrastructure/personal}
**Time Horizon:** {N years}
**Activities Analyzed:** {count}

### Activity Classification

| Activity | Classification | Compounding Mechanism | Priority |
|----------|----------------|----------------------|----------|
| {activity} | COMPOUND/MIXED/LINEAR/PREREQ | {why it compounds or doesn't} | {1-5} |

### Highest Compounders

1. **{activity}**: {why this compounds significantly}
2. **{activity}**: {why this compounds significantly}
3. **{activity}**: {why this compounds significantly}

### Current Allocation

| Category | Current % | Recommended % |
|----------|-----------|---------------|
| Compounding | X% | 40-60% |
| Mixed | X% | 20-30% |
| Linear | X% | 10-20% |
| Prerequisite | X% | 10-20% |

### Recommended Shifts

**Reduce:**
- {linear activity}: {from X% to Y%} - {how to reduce}

**Increase:**
- {compounding activity}: {from X% to Y%} - {time freed from reductions}

**Expected Impact:**
Over {time_horizon}, this shift compounds to: {projected benefit}

### The Compressed Insight
> "{One memorable sentence capturing the key prioritization}"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Activities too vague | Ask: "What specifically do you spend time on?" |
| Time horizon unclear | Default to 5 years; note that shorter horizons favor linear activities |
| User only lists linear activities | Ask: "What could you be doing that would make future work easier?" |
| Everything seems to compound | Challenge: "Which of these actually builds on itself vs just being important?" |
| User resistant to reducing linear | Acknowledge: "Some linear activities are non-negotiable. Let's find the ones that aren't." |

---

## Constraints

- Do not dismiss health, relationships, or rest as merely "linear"
- Prerequisite activities enable compounding; don't optimize them away
- Some legally required activities (compliance, admin) cannot be eliminated
- Compounding takes time to manifest; don't expect immediate returns
- Intensity matters; half-hearted compounding activities may not compound
- Context matters; the highest-compounding activity depends on your situation

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Neglecting prerequisites** | Burning out destroys all compounding; health enables everything | Treat rest, health, and relationships as foundation, not waste |
| **Everything compounds** | Labeling everything important as "compounding" removes analytical value | Apply strict criteria; most activities don't actually compound |
| **Compounding as excuse** | Using "this compounds" to justify avoiding less pleasant necessary work | Some linear work (admin, compliance) is genuinely non-negotiable |
| **Ignoring intensity** | Low-effort compounding activities may not actually compound | Engagement matters; distracted learning doesn't build skills |
| **Time horizon mismatch** | Optimizing for 5-year compounding when you need results in 6 months | Match time horizon to actual planning window |

---

## Example

**Input:**
```
Activities:
- Client meetings (sales)
- Writing blog posts about industry
- Networking events
- Administrative tasks
- Learning new technologies
- Internal process documentation
- Firefighting production issues

Domain: Senior engineer considering career growth
Time horizon: 5 years
```

**Output:**

## Compounding Activity Analysis

**Domain:** Career/Technical Leadership
**Time Horizon:** 5 years
**Activities Analyzed:** 7

### Activity Classification

| Activity | Classification | Compounding Mechanism | Priority |
|----------|----------------|----------------------|----------|
| Client meetings | MIXED | Builds relationships but doesn't scale | 3 |
| Writing blog posts | COMPOUND | Builds reputation, attracts opportunities, forces clarity | 5 |
| Networking events | COMPOUND | Each connection enables future connections | 4 |
| Administrative tasks | LINEAR | Value depletes immediately | 1 |
| Learning new tech | COMPOUND | Skills build on each other, enable future learning | 5 |
| Process documentation | MIXED | Reduces future questions but requires maintenance | 3 |
| Firefighting | LINEAR | Same issues recur, no leverage | 2 |

### Highest Compounders

1. **Learning new technologies**: Each skill makes the next easier. Reputation as someone who learns fast compounds career opportunities.
2. **Writing blog posts**: Public writing builds searchable reputation, forces understanding, attracts opportunities you can't predict.
3. **Networking**: Your network is an asset that appreciates. Strong network in year 1 pays dividends through year 5+.

### Current Allocation

| Category | Current % | Recommended % |
|----------|-----------|---------------|
| Compounding | 25% | 50% |
| Mixed | 30% | 25% |
| Linear | 45% | 25% |
| Prerequisite | 0% | 0% |

### Recommended Shifts

**Reduce:**
- Administrative tasks: Delegate or automate. Target 50% reduction.
- Firefighting: Fix root causes or document runbooks to prevent recurrence.

**Increase:**
- Writing: From occasional to weekly. 2-3 hours/week.
- Learning: Dedicated time, not just reactive. 4-5 hours/week.
- Networking: One meaningful connection per week, not sporadic events.

**Expected Impact:**
Over 5 years: Published body of work (50+ posts), expanded network (200+ meaningful connections), mastery of 2-3 new technology areas. These compound to create career options linear work never generates.

### The Compressed Insight
> "You're spending half your time on work that resets to zero tomorrow. Shift 20% toward building assets that appreciate."

---

## Integration

**Source Expert:** sam-altman

This skill applies Altman's core insight: "Building your network, writing publicly, learning to code, getting healthy - these compound. Most of what people spend time on doesn't."

---

## Success Criteria

Analysis is complete when:

- [ ] Compounding mechanism explained for each activity
- [ ] Clear classification with rationale
- [ ] Highest compounders identified and justified
- [ ] Current vs recommended allocation quantified
- [ ] Specific reallocation recommendations provided
- [ ] Expected impact articulated over time horizon
- [ ] Compressed insight is actionable and memorable