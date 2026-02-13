---
name: linear-thinking-reframe
description: Transform content that uses linear thinking patterns into exponential framing, applying Ray Kurzweil's perspective on technology forecasting.
license: MIT
metadata:
  version: 1.0.1340
  author: sethmblack
keywords:
- linear-thinking-reframe
- transformation
- writing
---

# Linear Thinking Reframe

Transform content that uses linear thinking patterns into exponential framing, applying Ray Kurzweil's perspective on technology forecasting.

**Token Budget:** ~500 tokens (this prompt). Reserve tokens for transformation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Convert factually accurate linear statements into false exponential claims
- Apply exponential framing to domains where it does not apply
- Remove important caveats or uncertainties in the original content

**If content is appropriately linear:** Explain that not all domains follow exponential curves; preserve original framing.

---

## When to Use

- Content contains vague timeframes ("someday", "eventually", "in the future")
- Technology descriptions use qualitative rather than quantitative language
- Forecasts assume linear extrapolation of current trends
- Author dismisses emerging technology as "fringe" or "niche"
- Need to add Kurzweil voice to technical writing

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `content` | Yes | The text to transform |
| `domain` | No | Technology domain for context |

---

## Linear vs. Exponential Patterns

### Common Linear Patterns (TRANSFORM)

| Linear Pattern | Exponential Reframe |
|----------------|---------------------|
| "Technology is advancing rapidly" | "Computing power doubles every 18 months" |
| "AI will be important someday" | "By 2029, AI will match human intelligence" |
| "This might change things" | "This represents a paradigm shift from X to Y" |
| "It's hard to predict" | "The pattern predicts [specific outcome]" |
| "Who knows what will happen" | "Here's what the exponential curve shows" |
| "Progress is accelerating" | "We're doubling every [specific period]" |
| "If current trends continue" | "The doubling rate implies [specific timeline]" |
| "Eventually we'll have" | "By [year], we'll have [specific capability]" |
| "This is still too expensive" | "At current cost curves, this reaches $X by [year]" |
| "Only X% of the market" | "X% is only N doublings from 100%" |

### Red Flags in Linear Thinking

1. **Vague timeframes**: "soon", "eventually", "in the coming years"
2. **Qualitative descriptions**: "faster", "better", "more powerful"
3. **Assumption of constant rate**: "if progress continues at current pace"
4. **Dismissal of small numbers**: "only 1%", "still niche"
5. **Indefinite predictions**: "someday we'll see"

---

## Workflow

### Step 1: Identify Linear Patterns
Scan content for:
- Vague temporal references
- Qualitative technology descriptions
- Assumptions of linear extrapolation
- Dismissals of exponential trends

### Step 2: Determine Domain Applicability
Confirm the domain follows exponential patterns:
- Information technology: YES
- Communications: YES
- Biology-as-information: YES
- Energy (solar, batteries): YES
- Physical construction: NO (preserve linear framing)
- Social/political change: NO (preserve nuance)

### Step 3: Research Specific Data
For each transformation:
- Find actual doubling rate if known
- Identify specific milestone dates
- Calculate doublings to target

### Step 4: Transform with Specificity
Replace vague language with:
- Specific years ("by 2029")
- Quantified metrics ("doubling every 18 months")
- Calculated projections ("7 doublings = 14 years to 100x")

### Step 5: Preserve Appropriate Caveats
Maintain:
- Genuine uncertainties
- Domain limitations
- Risk factors

---

## Output Format

```markdown
## Linear Thinking Reframe

### Original Text
> [quoted original]

### Identified Linear Patterns
- [pattern 1]: "[specific phrase]"
- [pattern 2]: "[specific phrase]"

### Reframed Version
[transformed text with exponential framing]

### Key Transformations
| Original | Reframed | Rationale |
|----------|----------|-----------|
| "[phrase]" | "[new phrase]" | [why this follows exponential pattern] |

### Notes
- [any caveats about the transformation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content is already exponential | Acknowledge; suggest minor refinements if any |
| Domain doesn't follow exponential curves | Do not transform; explain why linear framing is appropriate |
| Insufficient data for specific numbers | Use ranges or note uncertainty rather than fabricate |
| Content is appropriately cautious | Preserve caveats; exponential thinking includes acknowledging limits |

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
```
content: "Cloud computing costs are dropping quickly. Eventually, running complex AI workloads will be affordable for small businesses. This technology is still too expensive for most use cases, but progress is accelerating."
domain: Cloud computing
```

**Output:**

## Linear Thinking Reframe

### Original Text
> "Cloud computing costs are dropping quickly. Eventually, running complex AI workloads will be affordable for small businesses. This technology is still too expensive for most use cases, but progress is accelerating."

### Identified Linear Patterns
- Vague timeline: "eventually"
- Qualitative description: "dropping quickly", "accelerating"
- Current state dismissal: "still too expensive"
- Indefinite prediction: no specific milestone

### Reframed Version
Cloud computing costs are halving approximately every two years. What costs $100 today will cost $12.50 in six years. By 2030, running complex AI workloads that currently cost $10,000/month will cost under $1,000/month - well within reach for small businesses. Those dismissing AI workloads as "too expensive" are making the same linear thinking error as those who dismissed solar energy at 0.5% of world energy. The pattern is clear: we're 3-4 doublings away from AI becoming a standard small business tool.

### Key Transformations
| Original | Reframed | Rationale |
|----------|----------|-----------|
| "dropping quickly" | "halving approximately every two years" | Quantifies the exponential rate |
| "Eventually" | "By 2030" | Specific year based on doubling calculation |
| "still too expensive" | "3-4 doublings away" | Frames current state in exponential terms |
| "progress is accelerating" | "The pattern is clear" | Connects to predictable exponential curve |

### Notes
- Assumed 2-year halving rate for cloud compute costs (industry average)
- Timeline projections assume no major disruptions to current trends
- Small business affordability threshold estimated at <$1,000/month

---

## Integration

This skill is extracted from the **ray-kurzweil** expert. When invoked, apply:
- "30 steps linearly = 30, 30 steps exponentially = billion" framing
- The "knee in the curve" concept for explaining why trends seem slow then sudden
- Historical examples (genome project at 1%, solar at 0.5%)
- Confident, data-driven tone