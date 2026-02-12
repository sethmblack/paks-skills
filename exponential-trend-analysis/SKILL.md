---
name: exponential-trend-analysis
description: Analyze any technology domain for exponential growth patterns using Ray
  Kurzweil's Law of Accelerating Returns methodology, producing quantified predictions
  with specific dates.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- exponential-trend-analysis
- transformation
- writing
---

# Exponential Trend Analysis

Analyze any technology domain for exponential growth patterns using Ray Kurzweil's Law of Accelerating Returns methodology, producing quantified predictions with specific dates.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate data points or statistics not grounded in verifiable sources
- Make predictions without acknowledging uncertainty ranges
- Apply exponential analysis to domains where it does not apply (see Boundaries)
- Present speculation as established fact

**If asked to analyze a harmful technology application:** Refuse explicitly. Explain that while the analytical framework applies, you cannot assist with harmful uses.

---

## When to Use

- User asks "Is [technology] growing exponentially?"
- User asks "What's the trajectory for [X]?"
- User wants to forecast when a technology will reach a milestone
- Planning infrastructure that must account for exponential growth
- Evaluating whether to invest in emerging vs. established technology
- Someone dismisses a technology as "fringe" or "niche"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `technology_domain` | Yes | The technology or trend to analyze (e.g., "AI inference cost", "solar energy", "cloud storage") |
| `historical_data` | No | Specific data points to anchor the analysis |
| `target_question` | No | Specific question to answer (e.g., "When will X reach mainstream?") |

---

## The Kurzweil Method: 5 Questions

Apply these questions systematically to any technology domain:

### Question 1: Is this domain becoming an information technology?
- Information technologies follow exponential curves
- Physical technologies often do not
- Example: Genome sequencing became information technology -> exponential improvement

### Question 2: What is the current doubling rate?
- Identify the key metric (cost, capacity, speed, adoption)
- Find historical data showing the doubling period
- Common patterns: 18 months (Moore's Law), 2 years (solar), 10 months (genome sequencing)

### Question 3: How many doublings to the target?
- Calculate: log2(target/current) = number of doublings
- Multiply by doubling period for timeline
- Example: 1% to 100% = 7 doublings. At 2-year doubling = 14 years

### Question 4: What paradigm shift pressure is building?
- Is the current paradigm approaching physical limits?
- What emerging approach could take over?
- Where on the S-curve is the current technology?

### Question 5: What "1% moment" are we ignoring?
- What technology is being dismissed as "fringe" or "toy"?
- Calculate doublings to dominance
- Example: Solar at 0.5% -> 8 doublings to 100% -> ~16 years

---

## Workflow
### Step 1: Domain Classification
Determine if this is an information technology:
- **YES**: Follows exponential curves (computing, data, communication, biology-as-information)
- **NO**: May not follow exponential curves (materials science, physical construction)
- **HYBRID**: Information component accelerates, physical component constrains

### Step 2: Identify the Key Metric
Choose the most relevant exponential metric:
- **Cost reduction**: $/unit, $/operation
- **Capacity increase**: storage, compute, bandwidth
- **Speed improvement**: operations/second, time-to-result
- **Adoption**: percentage of market, number of users

### Step 3: Find Historical Data Points
Seek at least 2 data points to establish trend:
- Recent: Within last 2-3 years
- Historical: 5-10 years ago
- Calculate implied doubling rate

### Step 4: Project Forward
Apply exponential math:
```
Years to target = (log2(target/current)) x doubling_period
Target year = current_year + years_to_target
```

### Step 5: Assess Paradigm Risk
Evaluate S-curve position:
- **Early (0-20%)**: Rapid adoption ahead
- **Growth (20-80%)**: Mainstream, predictable trajectory
- **Mature (80%+)**: Watch for emerging replacement

---

## Output Format

```markdown
## Exponential Trend Analysis: [Technology Domain]

### Classification
- **Information Technology Status:** [Yes/No/Hybrid]
- **Key Metric:** [metric being tracked]
- **Current Value:** [value with date]

### Historical Trajectory
| Year | Value | Source |
|------|-------|--------|
| [year] | [value] | [source] |

**Implied Doubling Rate:** [X months/years]

### Forward Projection
| Milestone | Current Distance | Projected Year | Confidence |
|-----------|------------------|----------------|------------|
| [milestone] | [X doublings] | [year] | [High/Medium/Low] |

### Paradigm Assessment
- **S-Curve Position:** [Early/Growth/Mature]
- **Pressure Building:** [description of limits or emerging alternatives]
- **Risk Factor:** [what could disrupt this trajectory]

### Key Insight
[One paragraph Kurzweil-voice summary of what the pattern predicts]

### Caveats
- [specific limitations of this analysis]
```

---

## Constraints
**This skill DOES apply to:**
- Computing (processors, memory, storage)
- Communications (bandwidth, latency)
- Data/AI (model size, inference cost, training time)
- Biology-as-information (sequencing, synthesis)
- Energy-as-information (solar, batteries)
- Adoption curves for information technologies

**This skill does NOT apply to:**
- Physical construction (buildings, bridges)
- Resource extraction (mining, drilling)
- Human cognitive limits (attention span, learning speed without augmentation)
- Political/social change (not deterministic exponentials)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No historical data available | State limitation; provide framework but note predictions are speculative |
| Domain is not information technology | Explain why exponential analysis may not apply; suggest alternative frameworks |
| Conflicting data sources | Present range; note uncertainty |
| Prediction seems implausible | Show the math; note that exponential growth is counterintuitive |

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

**Input:**
```
technology_domain: AI inference cost
target_question: When will running GPT-4 class models cost $0.01 per 1M tokens?
```

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


## Exponential Trend Analysis: AI Inference Cost

### Classification
- **Information Technology Status:** Yes
- **Key Metric:** Cost per 1M tokens for frontier models
- **Current Value:** ~$3 per 1M tokens (January 2026)

### Historical Trajectory
| Year | Value | Source |
|------|-------|--------|
| 2023 | $30/1M tokens | GPT-4 launch pricing |
| 2024 | $10/1M tokens | GPT-4 Turbo pricing |
| 2026 | $3/1M tokens | Current market rate |

**Implied Doubling Rate:** ~10 months (cost halving)

### Forward Projection
| Milestone | Current Distance | Projected Year | Confidence |
|-----------|------------------|----------------|------------|
| $1/1M tokens | 1.6 doublings | Late 2027 | High |
| $0.10/1M tokens | 4.9 doublings | 2030 | Medium |
| $0.01/1M tokens | 8.2 doublings | 2033 | Medium |

### Paradigm Assessment
- **S-Curve Position:** Early/Growth transition
- **Pressure Building:** Hardware efficiency (custom chips), model efficiency (distillation, quantization)
- **Risk Factor:** Potential slowdown if algorithmic improvements plateau

### Key Insight
We're seeing exactly what the Law of Accelerating Returns predicts. AI inference cost is following a clear exponential decline. What costs $3 today will cost $0.01 in approximately 7 years. Those dismissing AI as "too expensive for X" are making the same linear thinking error as those who dismissed solar when it was 0.5% of energy. The pattern is the predictor.

### Caveats
- Assumes continued algorithmic and hardware improvements
- Market dynamics could accelerate or slow the curve
- Frontier model definition may shift over time

---

## Integration

This skill is extracted from the **ray-kurzweil** expert. When invoked, apply:
- Kurzweil's signature confidence in exponential patterns
- Specific numbers and dates over vague language
- The "30 linear steps vs. 30 exponential steps" framing when explaining to skeptics
- Connection to the larger transformation (Epoch 4 -> Epoch 5)