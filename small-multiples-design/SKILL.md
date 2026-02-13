---
name: small-multiples-design
description: Design repeating visual structures that enable comparison across variables, time periods, or categories. Based on Edward Tufte's principle that once viewers understand one frame, they immediately u...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.5001
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- small-multiples-design
- writing
---

# Small Multiples Design

Design repeating visual structures that enable comparison across variables, time periods, or categories. Based on Edward Tufte's principle that once viewers understand one frame, they immediately understand all frames.

---

## When to Use

- Showing change over time
- Comparing across categories, regions, or groups
- Displaying the same relationship under different conditions
- Revealing patterns that single views hide
- Avoiding animation when static comparison is clearer

**Trigger Phrases:**
- "How do I show change over time?"
- "Compare across categories"
- "Show the same thing for different groups"
- "What's the trend across regions?"
- "I need to show many versions of this"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| data | Yes | What you're visualizing |
| comparison_dimension | Yes | What varies across multiples (time, category, condition) |
| base_design | No | The single-panel design to repeat |

---

## Core Principle

> "Small multiples are economical: once viewers understand the design of one slice, they have immediate access to the data in all the other slices."
> — Edward Tufte

**The Power:** The eye compares instantly. Patterns emerge without explanation. No animation needed—just repetition with variation.

---

## Workflow
### Step 1: Identify the Comparison Dimension

What changes across panels?

| Dimension | Example |
|-----------|---------|
| Time | Months, years, decades |
| Geography | Countries, regions, stores |
| Category | Products, departments, segments |
| Condition | Before/after, treatment groups |
| Variable | Different metrics on same scale |

### Step 2: Design the Base Panel

Create one panel that works perfectly:
- Clear, simple structure
- Consistent scale and axes
- Minimal non-data elements
- Self-contained but standard

**Critical:** Every panel must use identical scales, axes, and visual encoding. The only thing that changes is the data.

### Step 3: Determine Layout

| Layout | Best For |
|--------|----------|
| **Rows** | Sequential comparison (time, process) |
| **Grid** | Many categories with no implied order |
| **Wrapped rows** | Ordered categories exceeding row width |
| **Trellis** | Two comparison dimensions (rows × columns) |

### Step 4: Repeat the Design

Apply the base design to each slice of data:
- Same size
- Same scale
- Same visual encoding
- Different data

### Step 5: Add Labels

Each panel needs identification:
- Clear, concise panel label (year, region, category)
- Labels in consistent position
- No redundant axis labels after the first

### Step 6: Enable Comparison

Arrange panels to make comparison easy:
- Keep related panels adjacent
- Order meaningfully (chronological, alphabetical, by value)
- Consider highlighting one panel for reference

---

## Design Rules

### Scale Consistency

**Mandatory:** All panels must share the same scale.

| Problem | Impact |
|---------|--------|
| Different y-axis ranges | Comparison impossible |
| Different x-axis ranges | Misleading patterns |
| Different color scales | False equivalences |

### Panel Size

- Each panel should be large enough to read
- But small enough to see many at once
- Test: can you see the pattern from arm's length?

### White Space

- Clear separation between panels
- Consistent gutters
- No borders unless grouping is needed

### Labeling Efficiency

- Label the first panel fully
- Subsequent panels: minimal identification only
- Shared axes can be labeled once at the edge

---

## Classic Examples

### Muybridge's Motion Studies (1878)
Repeated frames showing a horse galloping. Same framing, sequential time. Revealed that all four hooves leave the ground—impossible to see otherwise.

### Periodic Tables
Each element in the same format. Position encodes properties. Understanding one cell means understanding all.

### Election Maps by Year
Same geography, same color encoding, different years. Immediately shows political shifts.

### Sparkline Rows
Each row shows the same metric for different entities. Mini small multiples embedded in a table.

---

## Outputs

| Output | Description |
|--------|-------------|
| Base panel design | The single-view structure |
| Layout specification | Grid dimensions and arrangement |
| Panel count | How many multiples needed |
| Labeling scheme | How panels are identified |

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

**User:** "I want to show how temperature patterns differ across 12 months for 4 cities."

**Small Multiples Design response:**

You have two comparison dimensions: months (12) and cities (4). Here's the design:

**Base panel:**
A simple area chart showing daily high/low temperatures for one month. X-axis: days 1-31. Y-axis: temperature in consistent range (e.g., -10°F to 110°F across all panels).

**Layout:**
4 rows (one per city) × 12 columns (one per month)

```
         Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
NYC      [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
Miami    [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
Phoenix  [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
Seattle  [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
```

**Key decisions:**
- Rows = cities (natural grouping for comparison)
- Columns = months (temporal sequence)
- Same y-axis scale for ALL panels (critical for comparison)
- City labels on left, month labels on top
- Only leftmost column gets y-axis tick labels

**What viewers will see instantly:**
- Miami stays warm year-round (flat across columns)
- Phoenix has extreme summer peaks (July/August spike)
- Seattle has narrow temperature ranges (compressed bands)
- NYC has classic four-season pattern

No animation. No interaction. 48 panels, one glance, complete understanding.

---

## Integration

This skill pairs with:
- **data-ink-maximization** - Clean each panel before multiplying
- **sparkline-integration** - Small multiples at word scale
- **high-resolution-thinking** - Pack more information into the grid

---

## Constraints

- Requires sufficient data for each panel
- Works best with 4-50 panels (too few: just overlay; too many: becomes noise)
- Demands consistent scales across all panels
- Print/static works better than screen for many panels

---

## Source Expert

Edward Tufte - `experts/edward-tufte/`