---
name: graphical-integrity-audit
description: Evaluate visualizations for truthful representation by calculating lie factors and checking for distortion. Based on Edward Tufte's principles of graphical integrity.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1067
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- graphical-integrity-audit
- storytelling
- transformation
- writing
---

# Graphical Integrity Audit

Evaluate visualizations for truthful representation by calculating lie factors and checking for distortion. Based on Edward Tufte's principles of graphical integrity.

---

## When to Use

- Verifying a chart tells the truth
- Reviewing graphics before publication
- Checking for misleading visualizations
- Critiquing data journalism
- Auditing dashboards for accuracy

**Trigger Phrases:**
- "Is this misleading?"
- "Check my chart for accuracy"
- "Does this graphic lie?"
- "Is the visualization honest?"
- "Audit this chart"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| graphic | Yes | The visualization to audit |
| source_data | Recommended | The underlying numbers |
| context | No | How the graphic will be used |

---

## Core Principle

> "Graphical excellence begins with telling the truth about the data."
> — Edward Tufte

**The Lie Factor:**
```
Lie Factor = (Size of effect shown in graphic) / (Size of effect in data)
```

- **LF = 1.0** → Perfect integrity
- **LF > 1.0** → Exaggeration (visual effect is larger than data effect)
- **LF < 1.0** → Understatement (visual effect is smaller than data effect)

Lie factors between 0.95 and 1.05 are acceptable. Beyond that range, the graphic distorts perception.

---

## The Six Principles of Graphical Integrity

### 1. Proportional Representation
The visual representation of numbers must be directly proportional to the numerical quantities represented.

**Check:** If value A is twice value B, does the visual element for A appear twice as large?

### 2. Clear Labeling
Clear, detailed, and thorough labeling defeats graphic distortion.

**Check:** Are all elements labeled? Can the viewer verify the data from the graphic?

### 3. Show Data Variation, Not Design Variation
Variation in the graphic should reflect variation in the data, not variation in the design.

**Check:** Is visual interest coming from the data, or from decorative elements?

### 4. Standardize Money
In time-series displays of money, use deflated (constant) dollars.

**Check:** If showing monetary values over time, has inflation been accounted for?

### 5. Context
Don't quote data out of context. Show relevant comparisons.

**Check:** Is there enough context to interpret the data correctly?

### 6. Source Transparency
Show the data source. Enable verification.

**Check:** Can the viewer find and check the original data?

---

## Integrity Audit Workflow

### Step 1: Calculate Lie Factor

If the graphic shows a change from value A to value B:

**Data change:** (B - A) / A × 100 = X%

**Visual change:** Measure the visual elements
- For bars: Compare heights or lengths
- For areas: Compare areas (not diameters)
- For 3D: Check for perspective distortion

**Lie Factor:** Visual change % / Data change %

### Step 2: Check for Common Distortions

| Distortion | How to Detect | Severity |
|------------|---------------|----------|
| **Truncated axis** | Y-axis doesn't start at zero | High |
| **Inconsistent scale** | Axis intervals vary | High |
| **Area/volume for 1D data** | Using circles, cubes for linear values | High |
| **Dual axes** | Two y-axes with different scales | Medium |
| **Cherry-picked range** | Time period selected to support narrative | High |
| **Missing data** | Gaps not acknowledged | Medium |
| **3D perspective** | Distorts relative sizes | High |

### Step 3: Verify Context

| Question | Pass/Fail |
|----------|-----------|
| Is the comparison fair? | |
| Is the time period representative? | |
| Are relevant comparisons shown? | |
| Is the baseline appropriate? | |
| Are outliers acknowledged? | |

### Step 4: Check Source and Labeling

| Question | Pass/Fail |
|----------|-----------|
| Is the data source cited? | |
| Can the data be verified? | |
| Are all elements labeled? | |
| Are units specified? | |
| Is the date/time clear? | |

---

## Common Distortion Techniques

### The Truncated Y-Axis

**What it does:** Makes small changes look dramatic.

**Example:** A stock moving from $98 to $102 (4% gain) shown on an axis from $96 to $104 looks like a 75% visual increase.

**Lie factor:** 18.75 (75% visual / 4% data)

**Fix:** Start y-axis at zero, or clearly mark the break.

### The Area/Volume Inflation

**What it does:** Uses 2D or 3D shapes to show 1D data.

**Example:** Doubling the diameter of a circle to show a 2× increase actually makes the area 4× larger and the perceived volume 8× larger.

**Lie factor:** 4.0 to 8.0 depending on perception

**Fix:** Use length (bars, lines) for quantitative comparison.

### The Cherry-Picked Timeframe

**What it does:** Selects a start and end point to support a narrative.

**Example:** Showing stock performance from its lowest point to its highest.

**Detection:** Ask: "Why this start date? Why this end date?"

**Fix:** Show longer timeframes with context.

### The Dual Axis Deception

**What it does:** Places two unrelated scales side by side to imply correlation.

**Example:** Plotting "ice cream sales" and "drowning deaths" on different scales to make them appear correlated.

**Detection:** Check if the two axes are on comparable scales.

**Fix:** Normalize data or use separate charts.

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

## Outputs

| Output | Description |
|--------|-------------|
| Lie factor | Calculated ratio (data effect vs visual effect) |
| Distortions found | List of integrity violations |
| Severity rating | Low/Medium/High/Deceptive |
| Corrections needed | Specific fixes to restore integrity |
| Integrity score | Overall rating of truthfulness |

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


## Integrity Score

| Score | Description |
|-------|-------------|
| **A (Excellent)** | Lie factor 0.95-1.05, no distortions, full source |
| **B (Good)** | Lie factor 0.8-1.2, minor issues, source present |
| **C (Acceptable)** | Lie factor 0.5-2.0, some distortions, partial context |
| **D (Poor)** | Lie factor outside 0.5-2.0, multiple distortions |
| **F (Deceptive)** | Intentional distortion, missing/false source |

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

## Example

**User:** "Check this bar chart. It shows our customer satisfaction going from 3.8 to 4.2 (on a 5-point scale). The y-axis runs from 3.5 to 4.5."

**Graphical Integrity Audit response:**

**Lie Factor Calculation:**

Data change: (4.2 - 3.8) / 3.8 = 10.5% increase

Visual change: On an axis from 3.5 to 4.5 (range = 1.0):
- 3.8 position: (3.8 - 3.5) / 1.0 = 30% up the axis
- 4.2 position: (4.2 - 3.5) / 1.0 = 70% up the axis
- Visual change: 70% - 30% = 40 percentage points, or 133% increase from the starting visual position

**Lie Factor: 133% / 10.5% = 12.7**

This graphic exaggerates the change by a factor of nearly 13.

**Distortions Found:**
1. **Truncated y-axis** (High severity) - Axis should start at 0 or 1 (bottom of scale)
2. **Compressed scale** - Full range is 1-5; showing only 3.5-4.5

**Corrections Needed:**
- Option A: Show axis from 1 to 5 (the full scale). The 0.4 increase will be visible but appropriately sized.
- Option B: If you must zoom, clearly break the axis and show the full context nearby.
- Option C: Report the number textually: "Satisfaction increased from 3.8 to 4.2 (11% improvement)"

**Integrity Score: D (Poor)**

The current graphic makes a 10% improvement look like a dramatic transformation. While not necessarily deceptive in intent, it fails the integrity test.

---

## Integration

This skill pairs with:
- **chartjunk-detection** - Different concern: junk vs lies
- **data-ink-maximization** - After ensuring integrity, reduce ink
- **case-based-writing** - Tell the true story the data reveals

---

## Constraints

- Not all truncated axes are lies (context matters)
- Some distortion is perceptual (logarithmic scales can be honest)
- Intention matters for ethics, but not for the viewer's perception
- Cultural conventions affect interpretation

---

## Source Expert

Edward Tufte - `experts/edward-tufte/`