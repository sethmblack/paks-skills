---
name: spectrum-of-debate
description: A skill for identifying how public discourse is bounded to exclude certain positions - the invisible walls that define what's thinkable.
license: MIT
metadata:
  version: 1.0.1950
  author: sethmblack
keywords:
- spectrum-of-debate
- writing
---

# Spectrum of Debate

A skill for identifying how public discourse is bounded to exclude certain positions - the invisible walls that define what's thinkable.

## When to Use

- When analyzing why certain positions never appear in mainstream discourse
- When explaining how "both sides" can be on the same side
- When identifying excluded alternatives
- When breaking out of bounded debate

## Inputs

1. **The topic**: What issue or debate are you analyzing?
2. **The apparent spectrum**: What positions are presented as the range of options?
3. **The excluded positions**: What alternatives aren't discussed?
4. **The context**: What media, institutions, or forums are you examining?

## Workflow

### Step 1: Document what positions appear in mainstream discourse:

- What is Position A (often labeled "left" or "progressive")?
- What is Position B (often labeled "right" or "conservative")?
- What are the "moderate" positions in between?
- How is debate between these positions characterized?

### Step 2: Identify positions that simply don't appear:

- What positions are logically possible but never discussed?
- What historical positions have disappeared from debate?
- What positions exist in other countries but not here?
- What positions would challenge the shared premises?

### Step 3: Identify what keeps the spectrum stable:

- Who benefits from the current boundaries?
- What institutions enforce them?
- How are boundary-crossers treated?
- What would expand or shift the spectrum?



## Output Format

A spectrum analysis including:
1. The visible spectrum mapped (A to B)
2. Shared premises between A and B
3. Excluded positions catalogued
4. Exclusion mechanisms identified
5. Boundary maintenance analysis
6. Strategies for spectrum expansion

## Constraints

- Some positions may be rightly excluded (genuine extremism)
- Analysis can become self-serving (my excluded position is the right one)
- Spectrums vary by context, medium, and time
- Not all absence from debate is suppression
- Breaking out of spectrum is very difficult

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

**Input**: Analyze the spectrum of debate on healthcare policy in US media

**Output**:
"Visible spectrum: Position A ('left') - Expand ACA, public option, possibly Medicare-for-all with caveats. Position B ('right') - Reduce regulation, expand health savings accounts, repeal ACA. Debate characterized as 'more government vs. less government.' Shared premises: Healthcare is primarily a market; insurance is the delivery mechanism; employer-provided coverage is normal; cost containment is paramount; 'we can't afford' certain options. Excluded: Fully socialized medicine (providers are public employees); healthcare as right disconnected from employment; cost irrelevance (we don't ask 'can we afford' military). Exclusion mechanisms: Single-payer labeled 'unrealistic' without examination; advocates treated as naive; 'how will you pay for it' asked of left positions but not military spending or tax cuts. Boundary maintenance: Insurance industry advertising; think tanks funded by healthcare interests; revolving door between government and industry. Expansion strategies: Focus on shared premise challenges ('why is employment connected to healthcare?'); point to international comparisons; shift from 'afford' frame to 'values' frame."

## Integration

Works with:
- **propaganda-model-analysis**: Filters create the spectrum
- **defamiliarization**: Outside perspective reveals spectrum as constructed
- **institutional-incentive-analysis**: Incentives maintain spectrum boundaries