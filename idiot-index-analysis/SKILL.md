---
name: idiot-index-analysis
description: Calculate the ratio of final cost to raw material cost to identify cost reduction opportunities and assess manufacturing efficiency.
version: 1.0.0
author: sethmblack
tags: [compression, idiot-index-analysis, writing]
---

# Idiot Index Analysis

Calculate the ratio of final cost to raw material cost to identify cost reduction opportunities and assess manufacturing efficiency.

---

## When to Use

- Evaluating whether a product's price can be dramatically reduced
- Assessing manufacturing efficiency opportunities
- Deciding whether to build vs. buy a component
- Analyzing competitor cost structures
- User asks "What's the idiot index?" or "How much room is there to reduce cost?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| product | Yes | The product or component to analyze |
| final_cost | Yes | Current price or manufacturing cost |
| material_cost | No | Raw material cost (will estimate if not provided) |

---

## The Idiot Index Concept

The idiot index is a simple but powerful metric that reveals how much of a product's cost is fundamental (materials) versus process (manufacturing, overhead, margins).

**Formula:**
```
Idiot Index = Final Cost / Raw Material Cost
```

**Interpretation:**
| Index | Meaning | Opportunity |
|-------|---------|-------------|
| 1.0 | Perfect efficiency (impossible) | None |
| 1.5-2.0 | Excellent | Limited—focus elsewhere |
| 2-5 | Good | Moderate improvement possible |
| 5-10 | Typical | Significant opportunity |
| 10-50 | Poor | Large opportunity |
| 50+ | Terrible | Revolutionary opportunity |

### Why It Works

A high idiot index means most of the cost is process, not physics. Process costs are:
- Labor (can be automated or reduced)
- Overhead (can be streamlined)
- Margins (can be compressed with scale)
- Inefficiency (can be engineered out)

Only material costs represent fundamental physics constraints.

---

## The SpaceX Example

**Falcon 1 rocket (early SpaceX):**
- Industry price for comparable rocket: $30+ million
- Raw materials (aluminum, titanium, copper, carbon fiber): ~$200,000
- Idiot index: 150+

**Musk's insight:** "The materials cost is only 2% of the price. The rest is process inefficiency that we can engineer out."

**Result:** SpaceX reduced launch costs by 10x while still making profit.

---

## How to Calculate

### Step 1: Identify All Raw Materials
Break down the product to its material inputs:
- Metals (aluminum, steel, titanium, copper)
- Plastics and polymers
- Glass and ceramics
- Electronics components (at their material level)
- Other raw inputs

### Step 2: Find Commodity Prices
Look up current commodity prices for each material:
- Metal prices: LME (London Metal Exchange)
- Plastic resins: Plastics Exchange
- Electronics: Component distributors (approximate)

### Step 3: Calculate Material Cost
```
Material Cost = Σ (Material Quantity × Commodity Price)
```

Add reasonable allowance for:
- Waste/scrap (typically 5-15%)
- Basic processing (melting, forming)

### Step 4: Calculate Index
```
Idiot Index = Final Price / Material Cost
```

### Step 5: Interpret Results
- **Index 1-2:** Near optimal. Look for design changes, not process changes.
- **Index 2-5:** Healthy room for improvement. Standard optimization applies.
- **Index 5-20:** Significant opportunity. Question every process step.
- **Index 20+:** Massive opportunity. Industry is ripe for disruption.

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
## Idiot Index Analysis

### Product
[Name and description]

### Cost Breakdown

**Final Cost:** $[amount]

**Material Analysis:**
| Material | Quantity | Unit Price | Subtotal |
|----------|----------|------------|----------|
| [Material 1] | [Amount] | $[Price]/unit | $[Total] |
| [Material 2] | [Amount] | $[Price]/unit | $[Total] |
| [Material 3] | [Amount] | $[Price]/unit | $[Total] |
| **Waste allowance** | — | — | $[Amount] |
| **Total Material Cost** | — | — | **$[Total]** |

### Idiot Index Calculation

```
Idiot Index = $[Final Cost] / $[Material Cost] = [X]
```

### Interpretation
[What this index means for this product/industry]

### Opportunity Assessment

**Index Rating:** [Excellent/Good/Typical/Poor/Terrible]

**Cost Breakdown:**
- Material cost: [X]% of final price
- Process/overhead/margin: [Y]% of final price

**Implication:** [What this suggests about improvement potential]

### Recommendations

**If pursuing cost reduction:**
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

**Target idiot index:** [Achievable target] (would mean [X]% cost reduction)

### Caveats
[Any factors that complicate this analysis]
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

**Input:** "A friend says starting a furniture company is impossible because IKEA's prices are too low to compete with. What's the idiot index on a basic wooden bookshelf?"

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


## Idiot Index Analysis

### Product
Basic wooden bookshelf (similar to IKEA BILLY: 80cm x 28cm x 202cm)

### Cost Breakdown

**Final Cost:** $79 (IKEA BILLY retail)

**Material Analysis:**
| Material | Quantity | Unit Price | Subtotal |
|----------|----------|------------|----------|
| Particleboard/MDF | 2.5 sq meters | $3/sq m | $7.50 |
| Veneer/laminate | 5 sq meters | $1/sq m | $5.00 |
| Hardware (dowels, screws) | 1 set | $1.50 | $1.50 |
| Backing board | 0.4 sq m | $2/sq m | $0.80 |
| Packaging | 1 unit | $2.00 | $2.00 |
| **Waste allowance (10%)** | — | — | $1.70 |
| **Total Material Cost** | — | — | **$18.50** |

### Idiot Index Calculation

```
Idiot Index = $79 / $18.50 = 4.3
```

### Interpretation
An idiot index of 4.3 is in the "Good" range—IKEA has already optimized significantly. Most furniture has indexes of 8-15, so IKEA's process efficiency is above average.

### Opportunity Assessment

**Index Rating:** Good (but not exceptional)

**Cost Breakdown:**
- Material cost: 23% of final price
- Process/overhead/margin: 77% of final price

**Implication:** IKEA has significant process efficiency, but 77% non-material cost still leaves room. However, their scale advantages are formidable.

### Recommendations

**For competing with IKEA:**
1. **Don't compete on identical products** - Their scale means lower costs on commodity items
2. **Target higher index products** - Custom furniture, solid wood, and specialty items have indexes of 10-20
3. **Vertical integration on materials** - Source direct from mills to capture their material margin
4. **Local manufacturing for speed** - Trade some cost efficiency for faster delivery

**For alternative approaches:**
1. **Premium segment:** Solid wood bookshelves have index of 8-12—more room to compete on quality
2. **Custom/made-to-order:** Eliminates inventory cost; customers pay premium for customization
3. **Different material:** Metal shelving has different cost structure and may have weaker competitors

**Target idiot index:** For a new entrant without IKEA's scale, targeting index of 5-6 on commodity products is realistic. For differentiated products, index of 3-4 could create sustainable margins.

### Caveats
- IKEA's material costs benefit from massive scale purchasing
- Their flat-pack design minimizes shipping costs (not included in material analysis)
- Retail margin is embedded in the $79 price
- A competitor would need to add distribution costs

### The Musk Perspective
Your friend is right that IKEA is efficient—but wrong that it's "impossible" to compete. The question isn't whether you can beat IKEA at their game; it's whether there's a different game with higher idiot indexes. Custom furniture, solid wood, and rapid delivery segments all have worse incumbents and higher indexes.

---

## Advanced Applications

### Comparative Analysis
Calculate idiot index for multiple competitors to find the most vulnerable:
```
| Competitor | Final Price | Est. Material | Idiot Index |
|------------|-------------|---------------|-------------|
| IKEA       | $79         | $18.50        | 4.3         |
| Wayfair    | $129        | $22           | 5.9         |
| Local shop | $249        | $35           | 7.1         |
```

### Trend Analysis
Track idiot index over time to see if industry is getting more or less efficient.

### Make vs. Buy
Compare your potential idiot index against supplier prices to decide whether to insource.

---

## Integration

This skill is part of the **Elon Musk** expert persona. Use it to quickly assess whether a product's price reflects physics or inefficiency—and how much room exists for disruption.