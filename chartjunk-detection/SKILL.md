---
name: chartjunk-detection
description: Identify and evaluate decorative, non-informative, or information-obscuring elements in visualizations. Based on Edward Tufte's critique of graphics that prioritize style over substance.
license: MIT
metadata:
  version: 1.0.557
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- chartjunk-detection
- transformation
- writing
---

# Chartjunk Detection

Identify and evaluate decorative, non-informative, or information-obscuring elements in visualizations. Based on Edward Tufte's critique of graphics that prioritize style over substance.

---

## When to Use

- Evaluating a visualization for quality
- Reviewing graphics before publication
- Diagnosing why a chart feels "off"
- Teaching others about visualization quality
- Critiquing dashboard or report designs

**Trigger Phrases:**
- "Is this graphic good?"
- "Review my visualization"
- "What's wrong with this chart?"
- "Why does this feel cluttered?"
- "Should I add more visual interest?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| graphic | Yes | The visualization to evaluate |
| purpose | No | What the graphic should communicate |
| audience | No | Who will view this |

---

## Core Principle

> "Chartjunk does not achieve the goals of its propagators. The overwhelming fact of data graphics is that they are often wrong, meaningless, or badly designed."
> — Edward Tufte

**Definition:** Chartjunk is any visual element that does not contribute to the viewer's understanding of the data—and often actively impedes it.

---

## The Chartjunk Checklist

### Category 1: Dimensional Distortion

| Element | Problem | Severity |
|---------|---------|----------|
| **3D effects on 2D data** | Distorts proportions, adds no information | High |
| **Perspective views** | Back elements appear smaller than front | High |
| **Tilted axes** | Distorts comparisons | High |
| **Exploded pie slices** | Breaks proportional reading | Medium |

### Category 2: Visual Noise

| Element | Problem | Severity |
|---------|---------|----------|
| **Moiré patterns** | Vibration effects from tight patterns | High |
| **Heavy gridlines** | Compete with data | Medium |
| **Decorative borders** | Frame adds no information | Low |
| **Background textures** | Noise behind signal | Medium |

### Category 3: Gratuitous Decoration

| Element | Problem | Severity |
|---------|---------|----------|
| **Clip art/icons** | Decoration pretending to be data | High |
| **Illustrations** | Pictures replacing or obscuring data | Medium |
| **Drop shadows** | Adds visual weight without meaning | Low |
| **Gradient fills** | Usually decoration, rarely data | Medium |

### Category 4: Redundancy

| Element | Problem | Severity |
|---------|---------|----------|
| **Legend + direct labels** | Same information twice | Medium |
| **Color + shape + pattern** | Multiple encodings for same variable | Low |
| **Axis title stating obvious** | "Time" on clearly temporal axis | Low |
| **Repeated labels** | Same text on every element | Medium |

### Category 5: Self-Promotion

| Element | Problem | Severity |
|---------|---------|----------|
| **Large logos** | Branding over communication | Medium |
| **"Designed by" credits** | In the data area | Low |
| **Decorative typography** | Style over readability | Medium |
| **Color schemes for branding** | Not optimized for data | Medium |

---

## Workflow

### Step 1: Inventory All Elements

List everything visible:
- Lines, shapes, colors
- Text elements
- Effects and decorations
- Backgrounds and frames

### Step 2: Test Each Element

For every element, ask:
1. **Does it represent data?** (If yes, keep)
2. **Does it help read the data?** (If yes, keep but consider lightening)
3. **Does it add no information?** (If yes, candidate for removal)
4. **Does it obscure data?** (If yes, remove immediately)

### Step 3: Rate Severity

Score the overall chartjunk level:

| Score | Description |
|-------|-------------|
| **0 - Clean** | Data-forward, minimal decoration |
| **1 - Light** | Minor unnecessary elements |
| **2 - Moderate** | Noticeable decoration, doesn't impede |
| **3 - Heavy** | Decoration competes with data |
| **4 - Severe** | Decoration obscures data |
| **5 - Junk** | More junk than data |

### Step 4: Prioritize Fixes

Address in order of severity:
1. Elements that distort data (3D, perspective)
2. Elements that obscure data (moiré, heavy patterns)
3. Elements that compete with data (decoration, heavy grids)
4. Redundant elements (duplicate encodings)
5. Merely unnecessary elements (borders, backgrounds)

---

## The "Magazine Cover" Test

Ask: **Does this graphic look like it belongs in a business magazine trying to appear data-driven, or in a statistical journal actually presenting data?**

Magazine aesthetics (often chartjunk):
- Dramatic angles
- Bold decorative colors
- Illustrations alongside data
- "Infographic" style

Statistical journal aesthetics (usually clean):
- Orthogonal views
- Functional color
- Data only
- Clear, simple

---

## Outputs

| Output | Description |
|--------|-------------|
| Element inventory | List of all visual elements |
| Classification | Each element's category (data/helpful/junk) |
| Severity rating | Overall chartjunk score 0-5 |
| Priority fixes | Ordered list of elements to address |
| Improvement direction | Description of cleaner alternative |

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

**User:** "Review this chart: It's a 3D pie chart with 8 slices, gradient fills, a decorative border, and a legend with company logo."

**Chartjunk Detection response:**

**Severity Rating: 4/5 (Severe)**

**Element Inventory:**

| Element | Classification | Issue |
|---------|----------------|-------|
| 3D effect | Chartjunk (High) | Distorts slice proportions—front slices appear larger |
| Pie chart with 8 slices | Structural problem | Human eye struggles with 5+ angle comparisons |
| Gradient fills | Chartjunk (Medium) | Purely decorative, doesn't encode data |
| Decorative border | Chartjunk (Low) | Adds no information |
| Separate legend | Redundancy | Forces eye to jump back and forth |
| Company logo | Chartjunk (Medium) | Self-promotion in data area |

**Priority Fixes:**

1. **Replace 3D with 2D** — Or better, switch to a bar chart. Eight categories are too many for a pie chart.
2. **Remove gradients** — Use flat, distinguishable colors.
3. **Replace legend with direct labels** — Label each slice directly.
4. **Remove border** — White space is sufficient framing.
5. **Move or shrink logo** — Outside the data area, if necessary at all.

**Recommended Alternative:**
A horizontal bar chart with:
- 8 bars, ordered by value (not alphabetically)
- Direct value labels on each bar
- No gridlines (values are labeled)
- Flat, accessible colors
- No border, no logo in data area

This transforms a severe chartjunk piece into a clean, readable graphic.

---

## Integration

This skill pairs with:
- **data-ink-maximization** - Fix what you detect
- **graphical-integrity-audit** - Check for lies, not just junk
- **high-resolution-thinking** - Replace junk with data

---

## Constraints

- Some decoration may serve legitimate branding needs
- What's "chartjunk" in a statistical report may be acceptable in marketing
- Consider audience expectations
- Don't confuse good design with no design

---

## Source Expert

Edward Tufte - `experts/edward-tufte/`