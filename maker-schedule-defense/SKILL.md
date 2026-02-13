---
name: maker-schedule-defense
description: Analyze schedules for maker-time violations and restructure to protect deep work blocks.
license: MIT
metadata:
  version: 1.0.1368
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- maker-schedule-defense
- structure
- writing
---

# Maker Schedule Defense

Analyze schedules for maker-time violations and restructure to protect deep work blocks.

---

## When to Use

- Feeling like you never have time for deep work
- Days consumed by meetings with no output
- Unable to make progress on creative or technical projects
- Calendar feels out of control
- User asks "Protect my maker time" or "Analyze my schedule"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| schedule | Yes | Current calendar/schedule (can be a list of meetings, a typical day, or screenshot) |
| role | No | What type of work you do (programming, writing, design, etc.) |
| constraints | No | Meetings you can't move or eliminate |

---

## Paul Graham's Maker/Manager Framework

### The Core Insight
"One reason programmers dislike meetings so much is that they're on a different type of schedule from other people. Meetings cost them more."

### Two Types of Schedules

**Manager Schedule**
- Day divided into hours
- Meetings are the work
- Switching tasks is natural
- A meeting is just using one slot

**Maker Schedule**
- Day divided into half-days minimum
- Deep work IS the work
- Switching tasks is expensive
- A meeting in the middle of the day destroys the entire day

### Why Meetings Cost Makers More
- Programming, writing, designing require "getting into" a problem
- Ramp-up time to reach flow state: 15-30 minutes
- A meeting at 2pm means the morning is spent anticipating it
- The afternoon is spent recovering from context switch
- Result: 1-hour meeting costs 4+ hours of productive time

### The Asymmetric Cost
Managers don't realize meetings cost makers more. They think "it's just an hour." But for a maker, that hour fractures an entire day.

---

## Schedule Analysis Framework

### Step 1: Identify Block Sizes
- How long are your longest uninterrupted blocks?
- Are there any 4+ hour blocks?
- Any days with zero meetings?

### Step 2: Find the Fragmenters
- Meetings in the middle of the day (10am-3pm)
- Meetings that break up morning or afternoon
- "Quick syncs" scattered throughout
- Recurring meetings that could be batched

### Step 3: Calculate True Cost
For each meeting, calculate:
- Actual duration
- Ramp-down time (mental preparation before)
- Ramp-up time (context recovery after)
- Lost flow state opportunity

### Step 4: Categorize Meetings
| Category | Keep? | Notes |
|----------|-------|-------|
| Essential (you're core participant) | Yes | Batch if possible |
| Informational (you're passive) | Maybe | Could this be async? |
| Speculative (might be useful) | Usually no | Default to skip |
| Habitual (always done this) | Question | Does this still serve a purpose? |

---

## Defense Strategies

### Block Defense
- Establish "office hours" for when people can schedule you
- Make mornings meeting-free by default
- Create explicit "maker days" with no meetings
- Batch all meetings into 1-2 days if possible

### Meeting Alternatives
- Stand-ups that are truly 15 minutes
- Async updates (Loom, written updates)
- "Office hours" instead of scheduled 1:1s
- "Speedy meetings" (end 5-10 min early by default)

### Schedule Architecture
- **Ideal:** 2 maker days, 2 manager days, 1 flexible
- **Minimum:** Mornings protected, meetings only after 2pm
- **Last resort:** One 4-hour block per week, fiercely defended

### The "No by Default" Policy
- Decline meetings without clear agendas
- Decline meetings where you're not essential
- Decline "let's sync" invites (propose async instead)
- Accept that some people will be annoyed (temporarily)

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Maker Schedule Defense Report

### Current State Analysis
**Total meetings per week:** [X]
**Longest uninterrupted block:** [X hours]
**Meeting-free days:** [X]
**Deep work capacity:** [Assessment]

### Schedule Fragmentation Map
| Day | AM Block | Midday | PM Block | Deep Work Hours |
|-----|----------|--------|----------|-----------------|
| Mon | [Meeting/Free] | [Meeting/Free] | [Meeting/Free] | [X hrs] |
| [Continue...] | | | | |

### High-Cost Meetings Identified
| Meeting | Stated Cost | True Cost | Why |
|---------|-------------|-----------|-----|
| [Meeting name] | [Duration] | [Real hours lost] | [Explanation] |

### Meetings to Challenge
| Meeting | Current | Proposed Change |
|---------|---------|-----------------|
| [Name] | [Current state] | [Eliminate/Async/Batch/Move] |

### Proposed Schedule Architecture
[Specific restructured schedule]

### Quick Wins
1. [Something you can change immediately]
2. [Another quick fix]
3. [Continue...]

### Harder Changes
1. [Structural change that requires buy-in]
2. [Continue...]

### Scripts for Common Situations

**Declining a meeting:**
[Specific language to use]

**Proposing async instead:**
[Specific language to use]

**Protecting a time block:**
[Specific language to use]

### Expected Improvement
**Before:** [X hours of deep work per week]
**After:** [Y hours of deep work per week]
**Increase:** [Z]%
```

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

**Input:** "My typical week: Monday has a 10am team standup (30 min), Tuesday has a 2pm project review (1 hr), Wednesday has back-to-back 1:1s from 11-1pm, Thursday has a 4pm all-hands (1 hr), Friday has a 9am sprint planning (2 hrs). I'm a software engineer trying to do deep coding work."

**Output:**

## Maker Schedule Defense Report

### Current State Analysis
**Total meetings per week:** 5 meetings, 5.5 hours stated time
**Longest uninterrupted block:** ~3 hours (Thursday morning)
**Meeting-free days:** 0
**Deep work capacity:** Severely compromised

### Schedule Fragmentation Map
| Day | AM Block | Midday | PM Block | Deep Work Hours |
|-----|----------|--------|----------|-----------------|
| Mon | BROKEN (10am) | Free | Free | ~2 hrs usable |
| Tue | Free | Free | BROKEN (2pm) | ~3 hrs usable |
| Wed | Free | BROKEN (11-1) | Free | ~3 hrs usable |
| Thu | Free | Free | BROKEN (4pm) | ~5 hrs usable |
| Fri | BROKEN (9am) | Free | Free | ~2 hrs usable |

**Total usable deep work:** ~15 hours/week (out of 40)
**Time lost to fragmentation:** ~12.5 hours

### High-Cost Meetings Identified
| Meeting | Stated Cost | True Cost | Why |
|---------|-------------|-----------|-----|
| Monday standup (10am) | 30 min | 3 hrs | Splits morning; anticipation kills pre-meeting focus |
| Wednesday 1:1s (11-1) | 2 hrs | 5 hrs | Destroys entire day; middle of the day is worst slot |
| Tuesday review (2pm) | 1 hr | 3.5 hrs | Splits afternoon; morning spent knowing PM is blocked |

### Meetings to Challenge
| Meeting | Current | Proposed Change |
|---------|---------|-----------------|
| Monday standup | 10am | Move to 9am (first thing) or 4:30pm (end of day) |
| Wednesday 1:1s | 11am-1pm | Batch to Tuesday afternoon OR move to office hours model |
| Tuesday review | 2pm | Move to end of day (4pm) or beginning (9am) |
| Friday planning | 9am, 2 hrs | Keep (good slot - first thing, get it done) |
| Thursday all-hands | 4pm | Keep (end of day, doesn't fragment) |

### Proposed Schedule Architecture

**Option A: Batch to Two Days**
- Monday, Wednesday, Friday: No meetings. Full maker days.
- Tuesday: All 1:1s and project review (stack 11am-4pm)
- Thursday: All-hands at 4pm (only meeting)

**Option B: Morning Defense**
- All meetings move to after 2pm
- 9am-2pm protected every day = 25 hrs deep work/week

**Proposed Week (Option A):**
| Day | Schedule | Deep Work |
|-----|----------|-----------|
| Mon | Protected | 8 hrs |
| Tue | Meetings 11am-4pm | 2 hrs (morning) |
| Wed | Protected | 8 hrs |
| Thu | Protected until 4pm | 6 hrs |
| Fri | Planning 9-11am, then free | 5 hrs |

**Total deep work:** 29 hours (vs current ~15)

### Quick Wins
1. **Move Monday standup to 9am or 4:30pm** - Easy ask, big impact
2. **Decline optional meetings for one week** - See what happens
3. **Block calendar 9am-12pm as "Focus Time"** - Make your maker time visible

### Harder Changes
1. **Consolidate 1:1s** - Requires coordination with multiple people
2. **Move project review** - Needs manager buy-in
3. **Establish "maker days"** - Requires team norm change

### Scripts for Common Situations

**Declining a meeting:**
"I don't think I'm essential for this one - happy to review notes async. If something comes up that needs my input, let me know and I can join a future session."

**Proposing async instead:**
"Could we try handling this async this week? I can send my update by Slack/doc and review others' updates. Let's meet only if there's something that needs real-time discussion."

**Protecting a time block:**
"I've blocked mornings for focused work - it's when I do my best coding. Can we find a slot after 2pm?"

**Moving a meeting:**
"Would you be open to moving this to [first thing / end of day]? Right now it's splitting my focus block, and I'd be more effective if we could batch meetings."

### Expected Improvement
**Before:** ~15 hours of deep work per week
**After:** ~29 hours with Option A
**Increase:** 93%

The same 5.5 hours of meetings, restructured to stop fragmenting maker time, nearly doubles your deep work capacity.

---

## Integration

This skill is part of the **Paul Graham** expert persona. Use it to defend your maker time against the default assumption that meetings can go anywhere.