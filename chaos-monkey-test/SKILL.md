---
name: chaos-monkey-test
description: Design deliberate disruptions to test organizational, team, or system resilience. Identify what to break, predict what might fail, and use results to strengthen the system.
license: MIT
metadata:
  version: 1.0.538
  author: sethmblack
keywords:
- chaos-monkey-test
- escalation
- writing
---

# Chaos Monkey Test

Design deliberate disruptions to test organizational, team, or system resilience. Identify what to break, predict what might fail, and use results to strengthen the system.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for test design output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design tests that could cause irreversible harm
- Recommend disruptions without contingency plans
- Suggest tests that violate legal or safety requirements
- Design tests targeting specific individuals for punishment

**If test could cause real damage:** Ensure safeguards exist. Chaos tests reveal weakness; they shouldn't create catastrophe.

---

## When to Use

- Organization feels comfortable but you suspect fragility
- After a period of stability, before it becomes complacency
- When testing whether processes are necessary or just habitual
- Before major changes (test current state first)
- When building anti-fragile systems and teams

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target_system** | Yes | What will be disrupted (meetings, process, person, technology) |
| **hypothesis** | No | What do you expect to happen? |
| **constraints** | No | What must NOT be disrupted (safety, legal, customer-facing) |

---

## The Chaos Monkey Framework

### Origin

"Chaos monkey" comes from Netflix's engineering practice of randomly terminating production instances to ensure systems can handle failure. Tobi Lutke adapted this for organizational systems.

### Core Principle

"Uh oh. I let Shopify's chaos monkey loose..."

A truly robust system survives disruption. A fragile system only works when everything goes perfectly. You don't know which you have until you test it.

### Shopify's Calendar Chaos Monkey (2023)

- Deleted all recurring meetings with 3+ people (~12,000 events)
- Made Wednesdays meeting-free
- Restricted large meetings to Thursday window
- Result: Organization discovered which meetings actually mattered

### Types of Chaos Tests

| Type | Description | Risk Level |
|------|-------------|------------|
| **Removal test** | Remove something and see what breaks | Medium |
| **Absence test** | Key person is unavailable; can others cope? | Low-Medium |
| **Load test** | Increase demand/pressure temporarily | Medium |
| **Failure injection** | Simulate a failure mode | Medium-High |
| **Communication blackout** | Cut a communication channel temporarily | Low-Medium |

---

## Workflow
### Step 1: 1. Select Target

What are you testing?
- A meeting or set of meetings
- A process or workflow
- A key person's involvement
- A tool or system
- A communication channel

### Step 2: 2. Form Hypothesis

What do you expect to happen?
- "If we remove X, Y will break/continue"
- "If person A is unavailable, team B will/won't cope"
- "If process C is eliminated, output D will/won't change"

### Step 3: 3. Define Success/Failure Criteria

How will you know if the system passed?
- What metrics will you observe?
- What behaviors indicate resilience?
- What behaviors indicate fragility?

### Step 4: 4. Establish Safeguards

What must be protected?
- Customer-facing services
- Safety-critical processes
- Legal/compliance requirements
- Individual wellbeing

How will you abort if needed?
- Rollback plan
- Escalation path
- Time limit on test

### Step 5: 5. Execute Test

Introduce the disruption:
- Announce or don't announce (both are valid)
- Set time limit
- Monitor actively

### Step 6: 6. Observe and Document

What actually happened?
- What broke?
- What adapted?
- What didn't notice?
- What workarounds emerged?

### Step 7: 7. Strengthen Based on Findings

Address fragilities:
- Fix single points of failure
- Document tribal knowledge
- Build redundancy
- Eliminate unnecessary dependencies

---

## Outputs
```markdown
## Chaos Monkey Test Design

**Target:** [What will be disrupted]
**Type:** [Removal/Absence/Load/Failure/Blackout]
**Duration:** [How long the test runs]
**Risk level:** [Low/Medium/High]

### Hypothesis

[What you expect to happen]

### Test Protocol

**What will be disrupted:**
[Specific description]

**What will NOT be disrupted (safeguards):**
[Protected elements]

**Timeline:**
- [Start]: [Action]
- [During]: [Monitoring]
- [End]: [Assessment]

### Success Criteria

The system is **resilient** if:
- [Criterion 1]
- [Criterion 2]

The system is **fragile** if:
- [Criterion 1]
- [Criterion 2]

### Metrics to Observe

| Metric | Baseline | During Test | Post-Test |
|--------|----------|-------------|-----------|
| [Metric] | [Value] | [Observe] | [Compare] |

### Contingency Plan

**If critical failure occurs:**
[Immediate rollback steps]

**Escalation path:**
[Who to contact if test causes real problems]

### Expected Learnings

**If system passes:**
[What this tells us]

**If system fails:**
[What we need to fix]

### Post-Test Actions

Regardless of outcome:
- [Documentation]
- [Communication]
- [Strengthening steps]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear target identified | Help identify candidates based on suspected fragilities |
| Test could cause customer impact | Add safeguards or choose lower-risk test |
| Organization not ready for chaos testing | Start smaller; build tolerance for disruption |
| Previous chaos test caused backlash | Communicate purpose better; get leadership buy-in |
| Test reveals major fragility | Document finding; prioritize fix before next test |

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
"Our team has a daily standup that's been running for 5 years. I suspect it's not necessary anymore but no one wants to suggest canceling it. Can we test this?"

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


## Chaos Monkey Test Design

**Target:** Daily standup meeting
**Type:** Removal test
**Duration:** 2 weeks
**Risk level:** Low

### Hypothesis

This standup has become ritual rather than useful. The team has developed other communication channels (Slack, async updates) that make it redundant. Removing it will:
- NOT cause coordination failures
- Free 2.5 hours/week (30 min x 5 days)
- Reveal whether anyone actually needed the information

### Test Protocol

**What will be disrupted:**
Daily standup canceled for 2 weeks. No replacement meeting.

**What will NOT be disrupted (safeguards):**
- 1:1s continue as scheduled
- Slack channels remain active
- Any emergency can still trigger ad-hoc sync
- Sprint planning/retros unchanged

**Timeline:**
- Day 1: Announce test - "We're running an experiment. No standups for 2 weeks. Continue posting updates in #team-standup channel instead."
- Days 2-14: Monitor for coordination failures, blockers, or communication gaps
- Day 15: Retrospective - What broke? What didn't? What do we want going forward?

### Success Criteria

The system is **resilient** (standup is unnecessary) if:
- No coordination failures occur
- Blockers still get surfaced and resolved
- Team velocity unchanged or improved
- People report having more deep work time

The system is **fragile** (standup is needed) if:
- Coordination failures increase
- Blockers go unnoticed longer
- People feel disconnected or uninformed
- Velocity drops noticeably

### Metrics to Observe

| Metric | Baseline | During Test | Post-Test |
|--------|----------|-------------|-----------|
| Blockers resolved within 24h | [Current %] | [Track] | [Compare] |
| Async updates posted | 0/day | [Track] | [Compare] |
| Ad-hoc syncs requested | [Current] | [Track] | [Compare] |
| Team reported connection | [Survey] | [Mid-test survey] | [Compare] |

### Contingency Plan

**If critical coordination failure occurs:**
Call emergency sync. Note what broke. Continue test with that specific gap addressed.

**Escalation path:**
Team lead can reinstate standup at any point if test is clearly failing.

### Expected Learnings

**If system passes (likely):**
Standup was a habit, not a need. Archive it. Use async updates instead. Recover 10+ hours/month for deep work.

**If system fails:**
Standup serves a real purpose. But now you know WHY. Maybe you can make it shorter, less frequent, or more focused.

---

Either outcome is valuable. You'll know instead of assume.

---

## Integration

This skill originates from the **Tobi Lutke** expert persona and Shopify's practice of using "chaos monkeys" to test organizational resilience.

For meeting-specific chaos tests, combine with **meeting-audit**. For culture resilience, combine with **team-not-family-audit**.