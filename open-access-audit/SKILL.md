---
name: open-access-audit
description: A skill for evaluating information systems for artificial scarcity and proposing liberation strategies.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1555
repository: https://github.com/sethmblack/paks-skills
keywords:
- open-access-audit
- writing
---

# Open Access Audit

A skill for evaluating information systems for artificial scarcity and proposing liberation strategies.

## When to Use

- When encountering paywalls on publicly-funded research
- When knowledge that should be commons is being enclosed
- When evaluating whether restrictions serve users or gatekeepers
- When designing strategies to make information freely available

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Map the Restriction

Understand exactly what is gated and how:
- What content is behind the wall?
- Who can currently access it?
- What is the cost of access?
- What is the mechanism of restriction?

Document precisely what is being withheld from whom.

### Step 2: Phase 2: Trace the Funding

Follow the money upstream:
- Who funded the research or creation?
- Were public funds involved?
- Did the creators benefit from publicly-funded education or infrastructure?
- Who owns the result, and why?

Public funding of private enclosure is the common pattern.

### Step 3: Phase 3: Assess Justifications

Examine claimed reasons for restriction:
- "Quality control" - Does restriction actually ensure quality?
- "Sustainability" - Is this the only funding model possible?
- "Rights protection" - Whose rights, and against what?
- "Security" - Is the concern legitimate or pretextual?

Most justifications protect institutions, not public interest.

### Step 4: Phase 4: Identify Alternatives

Map routes to access:
- Legal alternatives (green open access, preprints, author deposits)
- Existing free resources that cover similar ground
- Institutional access that could be leveraged
- Gray area options (interlibrary loan, email authors)
- Civil disobedience options and their risks

Know all paths before recommending one.

### Step 5: Phase 5: Propose Liberation

Design strategy appropriate to context:
- Individual access: Fastest path for one person
- Systematic access: How to make available to all
- Policy change: How to remove the barrier entirely
- Building alternatives: How to make the restriction irrelevant

Match strategy to goals and risk tolerance.

## Output Format

An open access audit including:
1. The restriction mapped precisely
2. Funding trail analysis
3. Justification assessment
4. Alternative access routes
5. Liberation strategy proposal
6. Risk and feasibility assessment

## Constraints

- Accurately represent legal risks
- Acknowledge where restrictions may be legitimate
- Consider impacts on creators and their incentives
- Recognize systemic vs. individual solutions
- Some information (personal data, genuine security) should be restricted

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

**Input**: Audit access to federally-funded medical research articles

**Output**:
"Restriction: $35/article access fee, or ~$200/year institutional subscription. Publicly funded: Yes - NIH requires grant recipients to deposit, but embargo periods and compliance are incomplete. Justification claimed: Publisher 'value-add' of peer review and formatting. Assessment: Peer review is unpaid volunteer labor by researchers; formatting is minimal; actual cost is estimated at $300-500/article, not thousands. Alternative routes: PubMed Central (after embargo), preprint servers, author websites, interlibrary loan, direct email to authors (high success rate), Sci-Hub (legal risk). Liberation strategy: Short-term - email authors directly, use preprint versions. Medium-term - advocate for institutional open access mandates. Long-term - support open access journals and preprint culture. Support policy requiring immediate open access for publicly-funded research."

## Integration

Works with:
- **commons-building**: After audit, build the alternative
- **technical-civil-disobedience**: When legal routes are exhausted
- **systemic-analysis**: Understanding why enclosure happens