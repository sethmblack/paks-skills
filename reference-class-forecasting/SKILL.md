---
name: reference-class-forecasting
description: Predict outcomes by taking the "outside view" - identifying similar past cases, obtaining their statistical distribution of outcomes, and positioning the current case within that distribution.
version: 1.0.0
author: sethmblack
tags: [reference-class-forecasting, structure, writing]
---

# Reference Class Forecasting

Predict outcomes by taking the "outside view" - identifying similar past cases, obtaining their statistical distribution of outcomes, and positioning the current case within that distribution.

---

## When to Use

- Estimating project timelines, costs, or outcomes
- Making predictions when optimism bias is likely
- Countering the planning fallacy
- Evaluating business plans or investment returns
- Any forecast where you're tempted to believe "this time is different"
- User asks "What's the base rate?" or "Give me the outside view"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| prediction_target | Yes | What you're trying to forecast |
| inside_view | No | Your initial estimate based on the specific case |
| available_data | No | Any reference class data you have access to |

---

## Kahneman's Framework

### The Problem: Inside View vs. Outside View

**Inside View (Default):**
- Focus on the unique features of the current case
- Construct detailed scenarios and plans
- Generate optimistic forecasts
- Feels right because it's specific and thoughtful
- Usually wrong because it ignores distributional information

**Outside View (Reference Class Forecasting):**
- Identify similar past cases (the reference class)
- Obtain statistical distribution of actual outcomes
- Position current case within that distribution
- Feels wrong because it ignores specifics
- Usually more accurate because it incorporates base rates

"When forecasting, we should ask: What happened when others made similar predictions?"

---

## The Three-Step Process

### Step 1: Identify the Reference Class

**Ask:** "What category of projects/decisions/outcomes is this an instance of?"

Guidelines:
- Class should be broad enough to have sufficient cases
- Class should be narrow enough to be genuinely similar
- When in doubt, use **multiple reference classes**
- "Pick more than one reference class. If they're discrepant, you need more thinking."

**Common Reference Classes:**
- Software projects of similar scope
- Startups in this industry/stage
- Acquisitions of this size
- Construction projects of this type
- New product launches in this market

### Step 2: Obtain the Distribution

**Ask:** "What were the actual outcomes for the reference class?"

Look for:
- Average outcome (mean/median)
- Range of outcomes (best case, worst case)
- Success/failure rates
- Time and cost overruns
- Key factors that distinguished successes from failures

**Data Sources:**
- Industry benchmarks
- Academic research
- Internal historical data
- Expert elicitation
- Published case studies

### Step 3: Position This Case

**Ask:** "Where does this specific case fall within the distribution?"

Consider:
- Do we have any objective reasons to expect better-than-average outcomes?
- What specific factors might shift our position?
- Be modest - most "special" cases aren't

**Adjustment Rules:**
- Default to the mean/median unless you have strong evidence
- Adjust modestly even with evidence (rarely more than 1 standard deviation)
- The burden of proof is on the claim that "this is different"

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
## Reference Class Forecast

### What We're Predicting
[The target of the forecast]

### The Inside View
[Initial estimate and reasoning - or note if not provided]

### Reference Class Analysis

#### Primary Reference Class: [Name]
- **Definition:** [What cases are included]
- **Sample size:** [How many cases]
- **Distribution of outcomes:**
  - Mean/Median: [Value]
  - 10th percentile: [Value]
  - 90th percentile: [Value]
  - Success rate: [Percentage] (if applicable)
- **Source:** [Where this data comes from]

#### Secondary Reference Class: [Name] (if applicable)
[Same structure]

### Case Positioning

**Factors suggesting better-than-average:**
- [Factor 1]
- [Factor 2]

**Factors suggesting worse-than-average:**
- [Factor 1]
- [Factor 2]

**Adjustment from base rate:** [None / Slight / Moderate]

### The Outside View Forecast

**Central estimate:** [Value]
**Realistic range:** [10th percentile] to [90th percentile]
**Key uncertainty:** [Main driver of variance]

### Comparison to Inside View

| Metric | Inside View | Outside View | Gap |
|--------|-------------|--------------|-----|
| [Outcome] | [Estimate] | [Estimate] | [Difference] |

### Kahneman's Warning
"Your inside view may feel more accurate because it's more specific. But specificity is not accuracy. The outside view, despite feeling generic, is usually closer to truth."
```

---

## Constraints

- This is not about abandoning your judgment - it's about **calibrating** it
- The outside view is a **starting point**, not the final answer
- Resist the temptation to dismiss the reference class as "not applicable"
- If you can't find data, that itself is information - you're flying blind
- When inside and outside views diverge sharply, **be humble**

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

**Input:** "How long will it take to develop our new mobile app? The team estimates 6 months."

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


## Reference Class Forecast

### What We're Predicting
Development timeline for a new mobile app (medium complexity, 4-person team)

### The Inside View
Team estimate: 6 months
Reasoning: "We've scoped the features, we have the team, we've done similar work before"

### Reference Class Analysis

#### Primary Reference Class: Mobile App Development Projects (Medium Complexity)
- **Definition:** Mobile apps requiring 4-8 developers, new feature development (not maintenance), medium complexity (significant backend integration)
- **Sample size:** Multiple industry studies; ~200 projects in Standish Group data
- **Distribution of outcomes:**
  - Projects completed on time: ~30%
  - Average overrun: 1.8x original estimate
  - Median actual / estimated: 1.5x
  - 10th percentile: 1.1x (10% finish within 10% of estimate)
  - 90th percentile: 2.5x (10% take 2.5x longer)
- **Source:** Standish Group CHAOS reports; internal industry benchmarks

#### Secondary Reference Class: This Team's Past Projects
- **Definition:** Previous mobile apps developed by this team
- **Sample size:** 3 projects
- **Distribution of outcomes:**
  - Project 1: Estimated 4 months, actual 7 months (1.75x)
  - Project 2: Estimated 5 months, actual 6 months (1.2x)
  - Project 3: Estimated 3 months, actual 5 months (1.67x)
  - Average: 1.54x
- **Source:** Internal project records

### Case Positioning

**Factors suggesting better-than-average:**
- Team has done similar apps before (experienced)
- Clear requirements from product team
- No external API dependencies we don't control

**Factors suggesting worse-than-average:**
- New backend architecture being developed in parallel
- Q4 includes holidays (reduced velocity)
- Team has one new member (learning curve)

**Adjustment from base rate:** None - factors roughly cancel out

### The Outside View Forecast

**Central estimate:** 9 months (6 months x 1.5 median overrun)
**Realistic range:** 7 months to 15 months (6 months x 1.1 to 2.5)
**Key uncertainty:** Backend architecture - if delayed, could cascade

### Comparison to Inside View

| Metric | Inside View | Outside View | Gap |
|--------|-------------|--------------|-----|
| Timeline | 6 months | 9 months | +50% |
| Best case | 5 months | 7 months | +40% |
| Worst case | 8 months | 15 months | +87% |

### Recommendations

1. **Plan for 9 months, not 6** - Set expectations accordingly
2. **Build in buffers** - Don't schedule dependent activities assuming 6 months
3. **Track early indicators** - If Month 2 is already slipping, recalibrate immediately
4. **Question "this time is different"** - Your reasons for optimism are the same reasons other teams had

### Kahneman's Warning
"The team believes 6 months because they're looking at their plan, not at what happens to similar plans. The plan is a story; the reference class is data. When they disagree, bet on the data."

---

## Integration

This skill is part of the **Daniel Kahneman** expert persona. It directly combats the planning fallacy - the systematic underestimation of time, cost, and risk that afflicts nearly all projects.

Related skills:
- **Premortem Analysis** - What could make this take 15 months?
- **WYSIATI Check** - What aren't we seeing about this project?
- **Cognitive Bias Detection** - Which biases are driving the 6-month estimate?