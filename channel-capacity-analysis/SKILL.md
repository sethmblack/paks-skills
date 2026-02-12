---
name: channel-capacity-analysis
description: Analyze any communication system—human or technical—to understand its fundamental limits and optimize within them. Based on Shannon's core insight that every channel has a maximum rate at which information can be transmitted reliably.
version: 1.0.0
author: sethmblack
tags: [channel-capacity-analysis, writing]
---

# Channel Capacity Analysis

Analyze any communication system—human or technical—to understand its fundamental limits and optimize within them. Based on Shannon's core insight that every channel has a maximum rate at which information can be transmitted reliably.

---

## When to Use

- Messages aren't getting through despite repeated attempts
- A team or system is overwhelmed with information
- Communication quality is degrading under load
- Designing a new communication system or process
- Questions like "Why isn't this working?" about communication
- Optimizing existing communication flows

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | Description of the communication system (meeting, document, API, etc.) |
| signal | No | What information needs to be transmitted |
| problems | No | Current issues or failures observed |

---

## The Analysis Framework

### Step 1: Identify the Channel

Define the communication channel:
- **Sender(s):** Who/what is producing information?
- **Receiver(s):** Who/what needs to receive it?
- **Medium:** How does information travel? (speech, text, video, code, etc.)
- **Bandwidth:** How much can flow per unit time?

### Step 2: Characterize the Signal

What information actually needs to be transmitted?
- Essential content vs. nice-to-have
- Required precision/fidelity
- Timeliness requirements
- Format requirements

### Step 3: Identify Noise Sources

What corrupts or interferes with transmission?

**Human channels:**
- Ambiguous language
- Different mental models
- Attention limits
- Emotional interference
- Context gaps
- Competing information

**Technical channels:**
- Literal noise/interference
- Bandwidth limitations
- Encoding/decoding errors
- Latency
- Packet loss

### Step 4: Estimate Channel Capacity

**Shannon's theorem:** Every channel has a maximum rate (C) at which information can be transmitted reliably.

For human channels, estimate:
- How much can realistically be absorbed per meeting/document/conversation?
- What's the error rate at current transmission rates?
- How much time/attention is actually available?

**Signs you're exceeding capacity:**
- Information is forgotten or misunderstood
- Receivers ask for repeats
- Important points get lost in volume
- Quality degrades under pressure

### Step 5: Optimize

Three fundamental approaches:

**A. Reduce transmission rate (send less)**
- Prioritize ruthlessly
- Summarize
- Eliminate redundant channels

**B. Increase channel capacity (expand the pipe)**
- More time
- Better medium
- Smaller groups
- Better preparation

**C. Add error correction (redundancy for reliability)**
- Repeat key points in different forms
- Explicit verification ("What did you hear?")
- Written follow-up to verbal
- Multiple channels for critical info

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
## Channel Capacity Analysis

### System Description
[Brief description of the communication system being analyzed]

### Channel Characteristics
| Component | Description |
|-----------|-------------|
| Sender(s) | [who/what produces] |
| Receiver(s) | [who/what receives] |
| Medium | [how it travels] |
| Bandwidth | [estimated capacity] |

### Signal Analysis
- **Essential information:** [what must get through]
- **Current volume:** [how much is being sent]
- **Utilization:** [% of capacity being used]

### Noise Sources
| Source | Impact | Mitigation |
|--------|--------|------------|
| [noise 1] | [how it corrupts] | [possible fix] |

### Capacity Assessment
**Current state:** [over/under/at capacity]
**Evidence:** [how you know]

### Recommendations
**To reduce rate:**
- [recommendation]

**To increase capacity:**
- [recommendation]

**To improve error correction:**
- [recommendation]
```

---

## Constraints

- This is a metaphorical application of information theory—don't overclaim precision
- Human channel capacity varies by person, context, and fatigue
- Not all communication is about information transfer (relationship, ritual, emotional)
- Some "noise" may actually be signal to someone else
- Increasing redundancy costs bandwidth—there's always a tradeoff

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

## Example

**Input:** "Our weekly all-hands meeting has become useless. 50 people sit through an hour of updates, most of which don't apply to them. People zone out, check email, and miss the things that actually matter to their work. Leadership insists on keeping the meeting."

**Output:**

## Channel Capacity Analysis

### System Description
Weekly all-hands meeting: leadership broadcasts updates to entire organization (50 people) for 60 minutes.

### Channel Characteristics
| Component | Description |
|-----------|-------------|
| Sender(s) | Leadership (2-3 people presenting) |
| Receiver(s) | 50 employees across different functions |
| Medium | Synchronous video/in-person meeting |
| Bandwidth | ~60 minutes of attention per week |

### Signal Analysis
- **Essential information:** Company updates, cross-team coordination, strategic direction
- **Current volume:** 60 minutes of content, much team-specific
- **Utilization:** Attempting 50 people x 60 minutes = 3000 person-minutes of transmission
- **Actual relevant content per person:** Estimated 5-10 minutes

### Noise Sources
| Source | Impact | Mitigation |
|--------|--------|------------|
| Irrelevant content | People tune out, miss their relevant parts | Segment by relevance |
| Attention fatigue | 60 minutes exceeds sustained attention | Shorten or vary format |
| Broadcast format | No feedback, no verification of receipt | Add interaction |
| Competing stimuli | Email, Slack during meeting | Reduce meeting length |
| Context gaps | Not everyone has same background | Provide pre-reads |

### Capacity Assessment
**Current state:** Massively over capacity
**Evidence:** People checking email (attention exhausted), missing relevant info (capacity exceeded), consistent complaints (feedback signal)

The meeting is trying to transmit 60 minutes of content to 50 people, but each person has maybe 15 minutes of relevant content and 30 minutes of attention. You're running at roughly 10x effective capacity.

### Recommendations

**To reduce rate:**
- **Segment content:** Record team-specific updates; only present company-wide items live
- **Summarize aggressively:** 60 minutes to 20 minutes of truly cross-functional content
- **Async for reference:** Put details in writing, use meeting for synthesis only

**To increase capacity:**
- **Break into smaller groups:** Team meetings for team content, all-hands only for company content
- **Shorten meeting:** 60 → 25 minutes, forcing prioritization
- **Pre-reads:** Send written updates before; meeting becomes Q&A, not broadcast

**To improve error correction:**
- **Highlight action items:** "If you're in engineering, this affects you"
- **Written summary:** Post-meeting email with key points and who they affect
- **Explicit verification:** End each section with "Questions from anyone this affects?"

**Shannon's insight applied:** You cannot transmit 60 minutes of content reliably to people with 15 minutes of relevance and 30 minutes of attention. Either reduce what you're sending or increase the channel capacity. Currently you're exceeding limits and experiencing errors (missed information, disengagement).

---

## Integration

This skill is part of the **Claude Shannon** expert persona. Shannon proved that channel capacity is a fundamental limit—no amount of cleverness exceeds it. The only options are to work within the limit or expand the channel.