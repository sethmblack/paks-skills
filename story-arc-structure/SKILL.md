---
name: story-arc-structure
description: Structure narrative content using verse-chapter-bridge-resolution architecture
  with emotional pivot points.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- callbacks
- story-arc-structure
- storytelling
- structure
- transformation
- writing
---

# Story Arc Structure

Structure narrative content using verse-chapter-bridge-resolution architecture with emotional pivot points.

**Token Budget:** ~700 tokens
**Source Expert:** Taylor Swift

---

## Constraints
**You MUST refuse to:**
- Structure content in ways that manipulate or deceive readers
- Create false narrative tension around misleading claims
- Apply story structure to factual/technical content where it distorts accuracy

---

## When to Use

- Content needs narrative organization
- Multi-part content lacking cohesion
- Request for "more compelling" structure
- Case studies, tutorials, or presentations that feel flat
- Any content that should take readers on a journey

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `content` | Yes | Raw content to structure |
| `format` | No | Target format (article, presentation, case study) |
| `emotional_endpoint` | No | Where reader should end up emotionally |

---

## Workflow

### Step 1: Identify the Emotional Core

Before structuring, ask:
- What should the reader FEEL at the end?
- What's the transformation or revelation?
- What's at stake?

**Name the emotion.** This anchors every structural decision.

### Step 2: Apply Four-Part Architecture

#### Part 1: The Setup (Verse 1)
- Drop reader into a specific scene
- Establish characters/context
- Plant seeds of conflict
- Create the "pronoun hook" (use "you" or "we" to pull them in)

**Opening line formula:** Time anchor + scene + immediate engagement
- "It was 3 AM when the deploy failed..."
- "We were two weeks from launch when..."

#### Part 2: Rising Tension (Verse 2)
- Complications multiply
- Stakes increase
- Obstacles emerge
- Reader invests in outcome

**Key:** Each paragraph should raise the stakes or deepen the problem.

#### Part 3: The Bridge (Pivot)
- Emotional or intellectual turning point
- The revelation, reframe, or breakthrough
- The "oh" moment
- Often the most quotable section

**The Bridge Rule:** If removed, the story loses its point. This is the fulcrum.

#### Part 4: Resolution (Final Chorus)
- Deliver the emotional payoff
- Show the transformation
- Connect back to opening
- Leave reader with clear takeaway

**Bookend technique:** Echo the opening image/phrase but with new meaning.

### Step 3: Add Temporal Anchors

Ground each section in time:
- Specific times: "At 2 AM," "Three weeks later," "That December"
- Relative time: "Before we knew," "After everything changed"
- Season/weather: "It was the coldest winter," "August heat"

### Step 4: Insert Symbolic Objects

Identify one physical object that can carry emotional weight through the narrative:
- Introduced in Part 1
- Gains significance in Part 2
- Transforms meaning in Part 3
- Returns with full weight in Part 4

**Examples:** A whiteboard diagram, a Slack message, a coffee mug, a deploy button

### Step 5: Verify Arc Integrity

Check:
- [ ] Opening hooks immediately (no throat-clearing)
- [ ] Each section raises stakes or deepens understanding
- [ ] Bridge contains the turn/revelation
- [ ] Ending echoes beginning with new meaning
- [ ] Emotional core is served by structure

---

## Outputs

Structured content with:
- Clear four-part architecture
- Temporal anchors throughout
- Symbolic object woven through
- Strong opening hook
- Satisfying resolution

**Format:** Restructured content with section markers (can be removed for final version).

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content is purely technical/factual | Adapt: use problem→investigation→solution→lesson arc |
| No clear emotional endpoint | Ask: "What should the reader feel when finished?" |
| Content too short for full arc | Use mini-arc: hook → complication → resolution |

---

## Example

**Input:** Flat incident report about a production outage

**Output Structure:**

```
[SETUP]
At 2:47 AM on a Tuesday, Sarah's phone buzzed with the alert that would
define the next 72 hours. The dashboard showed red across every metric.

[RISING TENSION]
By sunrise, the team had tried three fixes. Each one failed. The CEO
was asking questions. Customers were asking for refunds. And the actual
root cause was still hiding somewhere in 400,000 lines of code.

[BRIDGE - THE TURN]
Then Marcus, the newest engineer, asked a question no one had
considered: "What if the bug isn't in our code at all?"

[RESOLUTION]
Two hours later, they found it—a silent update from a third-party
service. Sarah still keeps that Slack thread bookmarked. Not because
it solved the outage, but because it taught her team something they
use every day: the best debugging question is the one you're afraid
sounds stupid.
```

---

## Integration

This skill handles macro-level narrative structure. For sentence-level emotional impact, combine with `specific-universal-transform`. The two skills are complementary: structure shapes the journey, specificity makes each moment land.

**Expert voice:** When invoked by the Taylor Swift expert, emphasize emotional turns, bridge pivots, and bookend callbacks.