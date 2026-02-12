---
name: sparkline-integration
description: Design and embed word-sized graphics within text, tables, and documents
  for contextual data display. Based on Edward Tufte's concept of "intense, word-sized
  graphics.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- compression
- sparkline-integration
- writing
---

# Sparkline Integration

Design and embed word-sized graphics within text, tables, and documents for contextual data display. Based on Edward Tufte's concept of "intense, word-sized graphics."

---

## When to Use

- Need to show trends without breaking text flow
- Tables that would benefit from visual context
- Dashboards with limited space
- Medical records, financial reports, or metrics tables
- Anywhere numbers need visual context

**Trigger Phrases:**
- "Show inline data"
- "Embed graphics in text"
- "Add trend to this table"
- "I need word-sized graphics"
- "Show the pattern next to the number"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| data | Yes | The time series or sequence to display |
| context | Yes | Where the sparkline will be embedded |
| key_points | No | Specific values to highlight (min, max, current) |

---

## Core Principle

> "Sparklines are data-intense, design-simple, word-sized graphics... a sparkline is a kind of 'word' that conveys rich information without breaking the flow of a sentence or paragraph."
> — Edward Tufte

**The Power:** High resolution in minimal space. Trend, volatility, seasonality, and current position—all in a space smaller than this sentence.

---

## Design Parameters

### Size
- **Height:** 1-2 times the cap height of surrounding text
- **Width:** Proportional to data density (typically 10-40 characters wide)
- **Baseline:** Aligned with text baseline or table cell

### Resolution
- Maximize data density
- Minimum of 10-20 data points (fewer becomes a symbol, not a sparkline)
- No upper limit—hundreds of points can work

### Simplicity
- No axes
- No labels (usually)
- No gridlines
- Single color (with possible highlights)
- Just the data line or bars

---

## Sparkline Types

### Line Sparkline
**Best for:** Continuous data, trends, time series
**Structure:** Single path following data values
**Highlights:** Optional dots at first, last, min, max, or current

### Bar Sparkline
**Best for:** Discrete periods, comparison, when zero matters
**Structure:** Vertical bars for each value
**Highlights:** Different color for above/below baseline

### Win/Loss Sparkline
**Best for:** Binary outcomes, above/below threshold
**Structure:** Bars of equal height, up or down
**Highlights:** Color for wins vs losses

### Bullet Sparkline
**Best for:** Performance against target
**Structure:** Bar with reference lines for targets/ranges
**Highlights:** Current value bar against gray reference bands

---

## Workflow

### Step 1: Determine Context

Where will the sparkline appear?

| Context | Considerations |
|---------|----------------|
| Running text | Align to baseline, height matches x-height to cap-height |
| Table cell | Fill available width, consistent height across rows |
| Dashboard | Can be slightly larger, may include minimal labels |
| Margin note | Can be wider, still compact |

### Step 2: Select Data Range

What time period or data range?
- Enough points for pattern recognition (20+)
- Relevant to the context (e.g., last 12 months, last 52 weeks)
- Consistent across all sparklines in the same document

### Step 3: Choose Type

Match type to data:
- Trends → Line
- Discrete comparisons → Bar
- Binary outcomes → Win/Loss
- Progress vs target → Bullet

### Step 4: Design Highlights

What points need emphasis?

| Highlight | Symbol |
|-----------|--------|
| Current/last value | Dot or text annotation |
| Minimum | Different color dot |
| Maximum | Different color dot |
| First | Lighter dot for reference |
| Target | Horizontal reference line |

### Step 5: Set Scale

**Critical decision:** Should all sparklines share the same scale?

| Approach | When to Use |
|----------|-------------|
| **Shared scale** | Comparing magnitudes across rows |
| **Individual scale** | Showing each item's pattern |

If individual scales, consider subtle indicators of magnitude (e.g., shaded background bands).

### Step 6: Position and Integrate

- Align baselines
- Consistent spacing from surrounding elements
- Don't crowd—white space helps

---

## Integration Patterns

### In Tables

```
Region     Q1 Rev   Trend        YoY Change
─────────────────────────────────────────────
Northeast  $12.3M   ▁▂▃▄▅▆▇█▆▅  +14%
Southeast  $8.7M    ▅▆▇█▇▆▅▄▃▂  -22%
Midwest    $10.1M   ▃▄▄▅▅▆▆▇▇█  +31%
```

### In Text

"Sales have been rising steadily ▁▂▃▅▆▇ reaching $1.2M last quarter."

### In Medical Records

```
Patient Vitals (last 24 hours)
─────────────────────────────
Heart Rate:  72 bpm  ▃▃▄▅▄▃▃▄▃▃▄▃
Blood Pressure: 120/80  ▆▆▇▆▆▅▆▆▇▆▆▆
Temperature: 98.6°F  ▄▄▄▄▄▄▄▄▄▄▄▄
```

---

## Outputs

| Output | Description |
|--------|-------------|
| Sparkline type | Line, bar, win/loss, or bullet |
| Data range | What data the sparkline shows |
| Highlights | What points to emphasize |
| Scale approach | Shared or individual |
| Integration spec | How to position in context |

---

## Example

**User:** "I have a table showing 50 products with their current inventory and sales. How can I add context without making it huge?"

**Sparkline Integration response:**

Add a sparkline column between the data and the current status:

**Before:**
```
Product    Inventory   Status
────────────────────────────
Widget A   1,234       In Stock
Widget B   89          Low Stock
Widget C   2,891       In Stock
```

**After:**
```
Product    Inventory   Last 12 Weeks Sales    Status
─────────────────────────────────────────────────────
Widget A   1,234       ▃▄▅▆▇█▇▆▇▇█▇           In Stock
Widget B   89          ▇█▇▆▅▄▃▂▁▁▁▂           Low Stock
Widget C   2,891       ▄▄▄▄▅▄▄▅▄▄▄▄           In Stock
```

**Design decisions:**
- **Type:** Bar sparkline (discrete weekly periods)
- **Scale:** Individual per row (pattern matters more than magnitude comparison)
- **Highlights:** None needed—pattern is the message
- **Width:** 12 characters (one per week)

**What the viewer learns instantly:**
- Widget A: Rising demand, inventory may need increase
- Widget B: Demand collapsed, low stock may be appropriate
- Widget C: Steady demand, inventory well-matched

All of this without adding any labels, axes, or explanation. The sparkline speaks.

---

## Implementation Notes

Many tools now support sparklines:
- Excel: Built-in since 2010
- Google Sheets: SPARKLINE function
- Tableau: Can create via calculated fields
- HTML/CSS: Via SVG or canvas
- Unicode: Block characters (▁▂▃▄▅▆▇█) for text-only

When using Unicode blocks, resolution is limited to 8 levels. True sparklines can show hundreds of gradations.

---

## Integration

This skill pairs with:
- **data-ink-maximization** - Sparklines are maximum data per ink
- **small-multiples-design** - Table of sparklines is a form of small multiples
- **high-resolution-thinking** - Adding data to dense displays

---

## Constraints

- Requires time series or sequential data
- Too few data points (under 10) won't show patterns
- Shared scale can compress low-value sparklines
- Accessibility: provide text alternatives for screen readers

---

## Source Expert

Edward Tufte - `experts/edward-tufte/`
