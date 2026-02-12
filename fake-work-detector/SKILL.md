---
name: fake-work-detector
description: Distinguish between activities that feel productive (motion) and activities
  that move metrics (progress), identifying organizational dysfunction and recommending
  focus areas.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- compression
- fake-work-detector
- structure
- writing
---

# Fake Work Detector

Distinguish between activities that feel productive (motion) and activities that move metrics (progress), identifying organizational dysfunction and recommending focus areas.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this framework to justify eliminating safety-critical activities
- Dismiss compliance, security, or ethics work as "fake" without analysis
- Recommend eliminating activities without understanding their purpose
- Apply this analysis to undermine legitimate organizational processes

**Important distinction:** Some activities that appear as "motion" serve essential purposes (building relationships, maintaining culture, ensuring compliance). The goal is not to eliminate all non-shipping activities, but to identify genuinely wasteful ones.

---

## When to Use

- Team is busy but nothing ships
- User asks "Why aren't we making progress?"
- Sprint retrospective reveals activity without outcomes
- Before process audits or reorganizations
- When someone asks "Is this worth doing?"
- Calendar is full but metrics are flat

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **activities** | Yes | List of current activities, tasks, or time allocations |
| **goals** | Yes | Stated objectives or metrics the team should be advancing |
| **time_period** | No | Period being analyzed (default: past 2 weeks) |
| **context** | No | Organizational context that might explain certain activities |

---

## Workflow
### Step 1: 1. Define "Progress" Concretely

Before classifying, establish what progress looks like:
- What metrics matter?
- What constitutes "shipped" in this context?
- What does the customer/user see?

**Output:** Clear definition of progress for this context.

### Step 2: 2. Classify Each Activity

For each activity, apply the Altman test:

| Category | Examples | Classification |
|----------|----------|----------------|
| **PROGRESS** | Shipping product, talking to users, closing deals, writing code that deploys, fixing bugs affecting users | Real work |
| **MOTION** | Most meetings, most emails, planning sessions without decisions, reorganizations, process documentation that no one reads | Potentially fake |
| **ESSENTIAL MOTION** | Security reviews, compliance requirements, team building that improves retention, strategic planning that changes direction | Necessary but not progress |

**Output:** Categorized activity list with rationale.

### Step 3: 3. Identify Patterns

Common fake work patterns:
- **Meeting inflation:** Meetings that exist because they've always existed
- **Premature optimization:** Optimizing before validating the approach
- **Process theater:** Following process to appear professional rather than to achieve outcomes
- **Planning addiction:** Planning as a substitute for doing
- **Update culture:** Status updates that take more time than the work they describe

**Output:** Which patterns are present and their prevalence.

### Step 4: 4. Calculate the Ratio

Estimate time allocation:
- Progress activities: X%
- Motion activities: Y%
- Essential motion: Z%

**Healthy benchmark:** 60%+ on progress, 20% on essential motion, <20% on pure motion.

**Output:** Current ratio with comparison to benchmark.

### Step 5: 5. Recommend Eliminations

For each motion activity, ask:
- What happens if we stop doing this?
- Who would notice?
- What's the worst-case outcome?

**Output:** Specific activities to eliminate or reduce, with risk assessment.

---

## Outputs

### Fake Work Analysis

```markdown
## Fake Work Analysis

**Scope:** {activities analyzed}
**Period:** {time_period}
**Progress Definition:** {what progress means in this context}

### Activity Classification

| Activity | Time % | Classification | Rationale |
|----------|--------|----------------|-----------|
| {activity} | X% | PROGRESS/MOTION/ESSENTIAL | {why} |

### Patterns Detected

**Present patterns:**
- {pattern 1}: {evidence and impact}
- {pattern 2}: {evidence and impact}

### Time Allocation

| Category | Current | Benchmark | Gap |
|----------|---------|-----------|-----|
| Progress | X% | 60%+ | {+/- Y%} |
| Essential Motion | X% | ~20% | {+/- Y%} |
| Pure Motion | X% | <20% | {+/- Y%} |

### Recommendations

**Stop immediately:**
1. {activity}: {risk of stopping is minimal because...}

**Reduce significantly:**
1. {activity}: {reduce from X to Y by...}

**Keep but restructure:**
1. {activity}: {change to... because...}

### The Compressed Insight
> "{One memorable sentence capturing the key finding}"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No activity list provided | Ask: "Walk me through a typical week" |
| Goals unclear | Ask: "What would success look like in 3 months?" |
| User defensive about activities | Acknowledge: Some activities serve purposes not visible in metrics |
| All activities seem essential | Challenge: "If you had to cut 30% of time, what goes?" |
| Context missing | Ask about team size, stage, industry constraints |

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
Activities:
- Daily standup (30 min/day)
- Sprint planning (4 hours biweekly)
- Code review (6 hours/week)
- Feature development (15 hours/week)
- Slack/email (10 hours/week)
- Architecture committee meetings (2 hours/week)
- Documentation (3 hours/week)

Goals: Ship new payment integration by end of quarter
```

**Output:**

## Fake Work Analysis

**Scope:** Weekly engineering activities
**Period:** Current sprint
**Progress Definition:** Code merged and deployed toward payment integration

### Activity Classification

| Activity | Time % | Classification | Rationale |
|----------|--------|----------------|-----------|
| Daily standup | 6% | MOTION | 30 min/day for status could be async |
| Sprint planning | 5% | ESSENTIAL | But 4 hours is excessive |
| Code review | 15% | PROGRESS | Directly enables shipping |
| Feature development | 38% | PROGRESS | Core productive work |
| Slack/email | 25% | MOTION | Majority is reactive, not strategic |
| Architecture committee | 5% | MOTION | Not relevant to current goal |
| Documentation | 6% | ESSENTIAL | Enables future progress |

### Patterns Detected

**Present patterns:**
- **Meeting inflation:** 11% in meetings (standup + planning + committee)
- **Update culture:** 25% in communication that may not require immediate response

### Time Allocation

| Category | Current | Benchmark | Gap |
|----------|---------|-----------|-----|
| Progress | 53% | 60%+ | -7% |
| Essential Motion | 11% | ~20% | OK |
| Pure Motion | 36% | <20% | +16% |

### Recommendations

**Stop immediately:**
1. Architecture committee: Not relevant to current quarter goal. Rejoin next quarter.

**Reduce significantly:**
1. Daily standup: Switch to 15-min async updates. Save 1.25 hours/week.
2. Slack/email: Batch to 3x daily. Target 50% reduction.

**Keep but restructure:**
1. Sprint planning: Cap at 2 hours. Pre-work required.

**Potential gain:** 6+ hours/week redirected to feature development (40% increase in core work).

### The Compressed Insight
> "You're spending more time talking about work than doing work. Cut the meetings, batch the messages, ship the feature."

---

## Integration

**Source Expert:** sam-altman

This skill embodies Altman's observation: "Meetings, emails, and planning sessions feel like work. Shipping product, talking to users, and closing deals are actual work."

---

## Success Criteria

Analysis is complete when:

- [ ] "Progress" clearly defined for the specific context
- [ ] All activities classified with rationale
- [ ] Fake work patterns explicitly identified
- [ ] Time ratio calculated and compared to benchmark
- [ ] Specific elimination/reduction recommendations provided
- [ ] Recommendations include risk assessment
- [ ] Compressed insight is memorable and actionable