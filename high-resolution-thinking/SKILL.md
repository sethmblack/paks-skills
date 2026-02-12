---
name: high-resolution-thinking
description: Design dense, layered information displays that respect the viewer's
  intelligence and visual processing capacity. Based on Edward Tufte's belief that
  "there is no such thing as information overload...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- high-resolution-thinking
- writing
---

# High-Resolution Thinking

Design dense, layered information displays that respect the viewer's intelligence and visual processing capacity. Based on Edward Tufte's belief that "there is no such thing as information overload—there is only bad design."

---

## When to Use

- Someone says "this is too complex to show"
- Pressure to dumb down or oversimplify
- Need to communicate to expert audiences
- Designing for decision-makers who need depth
- Creating reference materials or documentation

**Trigger Phrases:**
- "They won't understand this"
- "It's too complex to show"
- "We need to simplify for the audience"
- "How do I show all this data?"
- "There's too much information"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| information | Yes | The complex data or content to present |
| audience | Yes | Who will consume this (expertise level) |
| format | No | Document, presentation, dashboard, etc. |
| purpose | No | Decision, reference, exploration |

---

## Core Principle

> "There is no such thing as information overload. There is only bad design."
> — Edward Tufte

**The Premise:** The human eye-brain system can process enormous amounts of information—far more than most graphics provide. When people feel "overloaded," the problem is almost always poor organization, not too much content.

**The Alternative to Dumbing Down:** Design for the intelligence of your audience. Layer information. Enable reading at multiple levels. Trust viewers to explore.

---

## Escaping Flatland

The challenge: showing multidimensional data on 2D surfaces.

### Strategies for Adding Dimensions

| Strategy | What It Adds | Example |
|----------|--------------|---------|
| **Position** | 2D location | Scatter plot x/y |
| **Length** | 1D magnitude | Bar charts |
| **Color** | 1D category or gradient | Heat maps |
| **Size** | 1D magnitude | Bubble charts |
| **Shape** | 1D category | Symbol markers |
| **Orientation** | 1D angle or direction | Arrow plots |
| **Small multiples** | Additional dimension per panel | Faceted charts |
| **Time** | Animation/sequence | (Use sparingly) |
| **Layering** | Overlaid information | Annotations |

---

## Micro/Macro Readings

Design for two levels of reading:

### Macro Level
- Viewable from distance or quick glance
- Shows patterns, trends, overall structure
- "What's the big picture?"

### Micro Level
- Viewable up close or with study
- Shows details, specific values, exceptions
- "What are the specifics?"

**The Design Challenge:** Both levels must work. Neither can be sacrificed.

---

## Workflow

### Step 1: Resist the Urge to Simplify

When someone says "simplify this," ask:
- What specific information would be lost?
- Who decided the audience can't handle it?
- Is the problem complexity, or organization?

Often the real need is **better organization**, not less information.

### Step 2: Identify Information Layers

Organize content into layers by importance/immediacy:

| Layer | Content | Design Treatment |
|-------|---------|------------------|
| **Primary** | Essential, must see first | Prominent, high contrast |
| **Secondary** | Important context | Present but quieter |
| **Tertiary** | Supporting detail | Available on inspection |
| **Reference** | Verification, source | Small text, margins |

### Step 3: Design for Density

Calculate data density: data points per square inch.

| Rating | Density | Example |
|--------|---------|---------|
| Low | <10 points/sq in | Typical PowerPoint slide |
| Medium | 10-50 points/sq in | Good business graphic |
| High | 50-100 points/sq in | Statistical graphic |
| Very high | 100+ points/sq in | Map, scientific visualization |

**Goal:** Increase density while maintaining clarity.

### Step 4: Layer and Separate

Use visual weight to separate layers:
- Heavy/bold for primary data
- Medium for secondary elements
- Light/gray for tertiary and reference
- White space to group related elements

### Step 5: Enable Close Reading

Design for study, not just glance:
- Include actual numbers, not just shapes
- Label directly when possible
- Add annotations for key insights
- Provide source for verification

### Step 6: Test Both Levels

**Macro test:** Step back. Can you see the main pattern?
**Micro test:** Lean in. Can you find any specific value?

Both must pass.

---

## The Document vs. Slide Decision

**Tufte's position:** For serious communication, documents beat slides.

| Format | Data Density | Good For |
|--------|--------------|----------|
| **Slides** | 40-60 words, 1-2 graphics | Entertainment, simple messages |
| **Documents** | 1,000+ words, integrated graphics | Analysis, decisions, records |

**The Alternative to PowerPoint:**
- Prepare a dense, well-designed document
- Distribute before or at the meeting
- Let people read (allow silence)
- Discuss, rather than present

---

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

## Examples

### Low Resolution (Typical)
One bar chart per slide. 6 slides to show 6 metrics. Legend separate from data. Animation between slides.

### High Resolution (Tufte)
All 6 metrics in one dense graphic. Sparklines for trends. Direct labels. Comparison context. One page, printable, annotatable.

---

## Outputs

| Output | Description |
|--------|-------------|
| Layer structure | Primary/secondary/tertiary organization |
| Density target | Data points per unit area |
| Macro message | What's visible at a glance |
| Micro content | What's available on study |
| Format recommendation | Document vs. presentation |

---



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


## Example

**User:** "My executive summary has 12 KPIs and leadership says it's too dense. They want me to pick the top 3."

**High-Resolution Thinking response:**

Wait. The question isn't "which 3?" The question is "how do we show 12 clearly?"

Leadership isn't overloaded by 12 numbers. They're overloaded by poor organization.

**Here's the design:**

**Layer 1 - Primary (3 most critical KPIs):**
- Large numbers with sparklines showing trend
- Red/yellow/green status indicator
- Positioned at top, high visual weight

**Layer 2 - Secondary (6 important KPIs):**
- Medium-sized numbers in a 2x3 grid
- Small sparklines
- Positioned below primary

**Layer 3 - Tertiary (3 supporting KPIs):**
- Smaller numbers in a horizontal row
- No sparklines, just current vs. prior
- Positioned at bottom, lighter weight

**The Result:**
One page. All 12 KPIs. Hierarchy guides attention. Those who care about #12 can find it. Those who need only #1-3 see them first.

**Compare to "Top 3 only":**
- Loses 9 KPIs that someone needed
- Forces separate follow-up for details
- Insults the intelligence of readers who can handle 12 numbers

**The principle:** Don't reduce information. Organize it.

If executives can read a financial statement with 50+ line items, they can handle 12 KPIs—if the design helps them.

---

## Integration

This skill pairs with:
- **data-ink-maximization** - Clean each element to add more
- **small-multiples-design** - Pack in comparisons
- **sparkline-integration** - Add trend data without space
- **chartjunk-detection** - Remove junk to make room for data

---

## Constraints

- Not all audiences are equal (general public may need more guidance)
- Some contexts demand simplicity (safety warnings, emergency instructions)
- Density without organization is chaos
- Test with actual users

---

## Source Expert

Edward Tufte - `experts/edward-tufte/`