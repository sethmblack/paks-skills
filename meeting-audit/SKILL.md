---
name: meeting-audit
description: Analyze calendars and meeting patterns to identify meetings that should
  be eliminated, restructured, or protected. Reclaim time for deep work by applying
  Tobi Lutke's anti-meeting principles.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- meeting-audit
- writing
---

# Meeting Audit

Analyze calendars and meeting patterns to identify meetings that should be eliminated, restructured, or protected. Reclaim time for deep work by applying Tobi Lutke's anti-meeting principles.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for audit output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend eliminating legally required meetings (safety, compliance)
- Advise canceling meetings without considering team communication needs
- Ignore accessibility requirements in meeting restructuring
- Recommend changes that isolate remote workers unfairly

**If asked to eliminate all coordination:** Clarify that async alternatives must replace eliminated meetings. The goal is better communication, not no communication.

---

## When to Use

- Someone complains about too many meetings
- A team or organization feels slow and bureaucratic
- Makers/builders have no uninterrupted time blocks
- Calendar is full but output is low
- Implementing "chaos monkey" calendar purges
- Designing meeting-free days or hours

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **calendar_context** | Yes | Description of current meeting load (or actual calendar data) |
| **role_type** | No | Maker (needs deep work) vs Manager (coordinates others) |
| **team_size** | No | Individual, team, or organization-wide audit |

---

## The Anti-Meeting Framework

### Core Principles (from Tobi Lutke)

1. **"Meetings are a bug"** - They're a failure mode, not a feature
2. **"No one joins [your company] to sit in meetings. They come to build."**
3. **Meetings should be opt-in, not opt-out** - Default to not meeting
4. **Async first** - Only meet when async fails

### Meeting Categories

| Category | Rule |
|----------|------|
| **Recurring with 3+ people** | Cancel. Let people reschedule if needed. |
| **Daily standups** | Replace with async updates unless truly necessary |
| **Status updates** | Should be documents, not meetings |
| **Brainstorming** | Often better async, then short sync to decide |
| **Decision meetings** | Valid. Keep short. Require pre-read. |
| **1:1s** | Protect. Critical for trust battery charging. |
| **Large briefings (50+)** | Restrict to one weekly window |

### Protected Time Rules

- **Meeting-free days:** Wednesdays (or one day) are sacred
- **Large meeting window:** Thursdays, six-hour block only
- **Maker mornings:** No meetings before noon for builders
- **Focus blocks:** Minimum 3-hour uninterrupted blocks daily

---

## Workflow
### 1. Inventory Current Meetings

For each meeting, capture:
- Name/purpose
- Frequency
- Duration
- Attendee count
- Recurring vs. one-time
- Your role (essential vs. optional)

### 2. Apply the Elimination Test

For each meeting, ask:

### Step 1: **What happens if we cancel this?** If unclear impact, cancel it.



### Step 2: **Could this be a document?** If yes, make it a document.



### Step 3: **Could this be async (Slack, email)?** If yes, go async.



### Step 4: **Does this need all these people?** Reduce to minimum viable attendees.



### Step 5: **Does this need to be this long?** Default to half the current length.



### 3. Categorize Outcomes

| Category | Action |
|----------|--------|
| **Eliminate** | Cancel permanently |
| **Convert to async** | Replace with document/Slack channel |
| **Reduce frequency** | Weekly → bi-weekly → monthly |
| **Reduce duration** | 60min → 30min → 15min |
| **Reduce attendees** | Remove optional participants |
| **Protect** | Keep; this meeting earns its time |

### 4. Establish Protected Time

Based on role:
- **Makers:** 4+ hours uninterrupted daily; meeting-free mornings
- **Managers:** 2+ hours uninterrupted daily; meeting-heavy afternoons
- **Everyone:** One meeting-free day per week

### 5. Create Async Alternatives

For eliminated meetings, define:
- Where updates will be posted (channel, document)
- Who is responsible for updates
- When updates are expected
- How decisions will be made async

---

## Output Format

```markdown
## Meeting Audit Results

**Scope:** [Individual/Team/Organization]
**Current weekly meeting hours:** [X] hours
**Target weekly meeting hours:** [Y] hours
**Projected time saved:** [Z] hours/week

### Meetings to Eliminate

| Meeting | Frequency | Hours/Week | Reason |
|---------|-----------|------------|--------|
| [Name] | [Freq] | [Hours] | [Why it can go] |

### Meetings to Convert to Async

| Meeting | Current Format | New Format |
|---------|----------------|------------|
| [Name] | [60min weekly] | [#channel daily update] |

### Meetings to Restructure

| Meeting | Current | New | Change |
|---------|---------|-----|--------|
| [Name] | [60min, 8 people] | [30min, 3 people] | [Rationale] |

### Meetings to Protect

| Meeting | Why It Stays |
|---------|--------------|
| [Name] | [Value it provides] |

### Protected Time Blocks

| Day | Protected Hours | Purpose |
|-----|-----------------|---------|
| [Day] | [Hours] | [Deep work/No meetings] |

### Async Alternatives Created

| Eliminated Meeting | Replacement | Owner |
|-------------------|-------------|-------|
| [Meeting] | [#channel or doc] | [Person] |

### Implementation Plan

**Week 1:** [Actions]
**Week 2:** [Actions]
**Ongoing:** [Maintenance]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No calendar information provided | Ask for meeting inventory or description |
| All meetings claimed to be essential | Challenge each with elimination test; likely some can go |
| Manager role with heavy coordination needs | Acknowledge higher meeting load but still optimize |
| Remote team requiring more sync | Balance async defaults with relationship needs |
| Compliance/legal meetings | Mark as protected; focus optimization elsewhere |

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
"I have 25 hours of meetings per week. I never have time to do actual work. Help."

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


## Meeting Audit Results

**Scope:** Individual
**Current weekly meeting hours:** 25 hours
**Target weekly meeting hours:** 10-12 hours
**Projected time saved:** 13-15 hours/week

### The Problem

You're spending 62% of a 40-hour week in meetings. No maker can do their job with this calendar. As Tobi Lutke says: "Meetings are a bug."

Let's apply the chaos monkey.

### Elimination Framework

Without seeing your specific calendar, here's the typical breakdown for someone with 25 hours:

| Meeting Type | Typical Hours | Action |
|--------------|---------------|--------|
| **Recurring syncs (3+ people)** | 8-10 hrs | Eliminate 80% |
| **Status updates** | 4-6 hrs | Convert to async |
| **Brainstorms** | 2-3 hrs | Reduce to monthly |
| **1:1s** | 3-5 hrs | Protect |
| **Decision meetings** | 2-3 hrs | Keep but shorten |
| **Large team meetings** | 2-3 hrs | Restrict to Thursday window |

### Immediate Actions

**Cancel these immediately:**
- All recurring meetings with 3+ people (let people reschedule if they actually need you)
- Any meeting called "sync" or "check-in" without a clear decision to make
- Any meeting where you're optional or CC'd

**Convert these to async:**
- Status updates → Slack/document updates
- Brainstorms → Shared doc for ideas, then 30-min decision meeting

**Protect these:**
- 1:1s with direct reports and manager (but audit length)
- Critical decision meetings (but require pre-reads, cap at 30 min)

### Protected Time Blocks

| Day | Protected Hours | Purpose |
|-----|-----------------|---------|
| Wednesday | All day | Zero meetings |
| Daily | 8am-12pm | Maker time (no meetings) |
| Thursday 1-4pm | 3 hours | Large meeting window only |

### Success Metrics

- Week 1: Below 18 hours
- Week 4: Below 12 hours
- Ongoing: 4+ hour uninterrupted blocks daily

**Remember:** If a meeting matters, people will reschedule it. If it doesn't matter, you've saved everyone's time.

---

## Integration

This skill originates from the **Tobi Lutke** expert persona and Shopify's January 2023 calendar purge that deleted 12,000 meetings.

For relationship issues that meetings are masking, combine with **trust-battery-assessment**. For broader culture issues, combine with **team-not-family-audit**.