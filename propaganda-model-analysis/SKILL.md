---
name: propaganda-model-analysis
description: A skill for applying Chomsky and Herman's five filters to analyze media coverage - understanding how consent is manufactured in democratic societies.
version: 1.0.0
author: sethmblack
tags: [propaganda-model-analysis, writing]
---

# Propaganda Model Analysis

A skill for applying Chomsky and Herman's five filters to analyze media coverage - understanding how consent is manufactured in democratic societies.

## When to Use

- When analyzing why certain stories get coverage and others don't
- When explaining systematic bias without conspiracy
- When predicting how media will cover a topic
- When teaching critical media literacy

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow

### Step 1: Analyze who owns the media outlet:

- What corporation or conglomerate owns it?
- What are that owner's other business interests?
- How might those interests affect coverage?
- Who sits on the board?

### Step 2: Identify organized pushback mechanisms:

- What organizations exist to criticize media coverage?
- How have past criticisms affected this outlet?
- What complaints generate response?
- What positions invite attack?

### Step 3: Analyze the dominant ideology:

- What assumptions are shared across "both sides"?
- What positions are treated as common sense?
- What alternatives are simply not considered?
- What would be "too extreme" to discuss?



## Output Format

A propaganda model analysis including:
1. Overview of coverage being analyzed
2. Filter 1 analysis (ownership)
3. Filter 2 analysis (advertising)
4. Filter 3 analysis (sourcing)
5. Filter 4 analysis (flak)
6. Filter 5 analysis (ideology)
7. Synthesis and predictions vs. actual coverage
8. Implications and conclusions

## Constraints

- The model explains tendencies, not every article
- Individual journalists may resist filters
- New media complicates the model
- Confirmation bias can affect analysis
- The model doesn't predict content, only constraints

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

**Input**: Analyze coverage of labor dispute at major retailer

**Output**:
"Ownership: Major outlets owned by conglomerates with retail investments - unlikely to strongly support workers. Advertising: Retailer is major advertiser in regional markets - outlets dependent on ad revenue will be cautious. Sourcing: Company PR gets prominent placement; worker voices filtered through 'both sides' framing; union sources treated as interested parties while company sources treated as factual. Flak: Business-aligned think tanks prepared with criticism of pro-labor coverage; no equivalent flak organization for anti-labor coverage. Ideology: Shared assumption that 'business climate' matters; worker demands framed as 'costs' rather than 'justice'; disruption is automatically bad. Prediction: Coverage will present company and worker perspectives as equivalent, emphasize disruption to consumers, quote company sources more prominently, frame worker demands as potentially harmful to economy. Comparison to actual: [Assess fit with predictions]."

## Integration

Works with:
- **spectrum-of-debate**: The filters create the spectrum's boundaries
- **institutional-incentive-analysis**: Filters are institutional incentives
- **media-appetite-analysis**: Appetite is shaped by filters