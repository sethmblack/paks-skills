---
name: media-appetite-analysis
description: A skill for identifying what stories journalists want to tell - the narratives, anxieties, and trends that make certain fictions irresistible.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1417
repository: https://github.com/sethmblack/paks-skills
keywords:
- media-appetite-analysis
- storytelling
- writing
---

# Media Appetite Analysis

A skill for identifying what stories journalists want to tell - the narratives, anxieties, and trends that make certain fictions irresistible.

## When to Use

- Before designing a media hoax to ensure it feeds existing appetites
- When analyzing why certain stories go viral while others don't
- When understanding media's role in constructing reality
- When predicting what kinds of misinformation will spread

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Track Current Coverage

Monitor what's getting attention:
- Trending topics across major outlets
- Stories that get picked up widely vs. ignored
- Angles being pursued on breaking news
- Features and human interest patterns

What are they already writing about? That's what they want more of.

### Step 2: Phase 2: Identify Narrative Templates

Recognize recurring story shapes:
- **Trend piece**: "X is the new Y" / "Everyone is doing Z now"
- **David vs. Goliath**: Small challenger takes on powerful institution
- **Hidden danger**: Everyday thing is secretly harmful
- **Secret solution**: Simple fix the establishment doesn't want you to know
- **Moral panic**: New technology/behavior threatening children/society
- **Comeback story**: Fallen figure rises again
- **Too good to be true**: Heartwarming story that confirms faith in humanity

These templates are magnetic. Stories fitting them get coverage.

### Step 3: Phase 3: Map Current Anxieties

Identify what the public (and journalists) are worried about:
- Technology concerns (AI, social media, privacy)
- Health fears (new diseases, hidden toxins, mental health)
- Economic anxiety (jobs, housing, inequality)
- Political polarization (extremism, threats to democracy)
- Environmental crisis (climate, pollution, extinction)

Stories that connect to active anxieties have built-in audience.

### Step 4: Phase 4: Find the Gaps

Look for underserved appetites:
- Topics getting attention but lacking good sources
- Emerging concerns without established experts
- Stories everyone wants to write but can't find
- Beats where journalists are hungry for leads

The gap is the opportunity.

### Step 5: Phase 5: Test Your Analysis

Validate by prediction:
- Guess which stories will get pickup, which won't
- Track your accuracy
- Refine your model based on results

## Output Format

A media appetite analysis including:
1. Current trending topics and coverage patterns
2. Active narrative templates with examples
3. Dominant anxieties in target media
4. Identified gaps and opportunities
5. Predictions with reasoning

## Constraints

- Appetites shift quickly - analysis has shelf life
- Different outlets have different appetites
- What journalists want may differ from what editors approve
- Confirmation bias affects analysis - verify with data
- Understanding appetites doesn't mean all hoaxes will succeed

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

**Input**: Analyze media appetite around workplace technology (for potential hoax design)

**Output**:
"Current coverage: heavy focus on AI replacing jobs, remote work surveillance, productivity tracking. Narrative templates active: 'hidden danger' (your employer is watching more than you know), 'trend piece' (companies doing X to monitor workers). Active anxieties: job security, privacy, work-life balance erosion. Gap identified: limited expert sources on 'employee resistance to surveillance.' Opportunity: fictional organization helping workers detect/counter workplace monitoring would fit trend piece + David vs. Goliath templates, addresses privacy anxiety, fills expert gap. Prediction: would get significant pickup from labor-friendly outlets within 2 weeks of credible pitch."

## Integration

Works with:
- **media-hoax-design**: Appetite analysis informs hoax design
- **propaganda-model-analysis**: Deeper structural understanding of media
- **spectrum-of-debate**: Understanding what falls within/outside acceptable coverage