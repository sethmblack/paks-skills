---
name: institutional-incentive-analysis
description: A skill for explaining behavior through structural incentives rather than individual intentions - understanding why institutions do what they do.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4237
repository: https://github.com/sethmblack/paks-skills
keywords:
- institutional-incentive-analysis
- writing
---

# Institutional Incentive Analysis

A skill for explaining behavior through structural incentives rather than individual intentions - understanding why institutions do what they do.

## When to Use

- When trying to understand institutional behavior without resorting to conspiracy
- When individuals in institutions seem to act against their stated values
- When predicting how institutions will respond to situations
- When designing interventions that account for institutional logic

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Map the Incentive Structure

Identify what the institution rewards and punishes:
- What gets people promoted?
- What gets people fired or marginalized?
- What metrics are tracked?
- What behaviors are celebrated?
- What resources flow to whom?

The incentive structure is the institution's true values, regardless of stated mission.

### Step 2: Phase 2: Identify the Actors

Understand who makes decisions:
- Who are the key decision-makers?
- What are their personal incentives within the structure?
- How does their position shape their perspective?
- What pressures do they face?

Individuals respond to their incentives. Their intentions may be good; their behavior follows the structure.

### Step 3: Phase 3: Trace the Logic

Follow the incentives to the behavior:
- Given the incentives, what behavior is rational?
- How does the puzzling behavior serve someone's interests?
- What would happen to someone who behaved differently?
- Who benefits from the current pattern?

Almost always, the behavior makes sense once you understand the incentives.

### Step 4: Phase 4: Test the Analysis

Verify your model:
- Does it predict behavior in other situations?
- Does it explain past behavior?
- Are there counterexamples, and what do they tell you?
- Have incentives changed, and has behavior changed accordingly?

### Step 5: Phase 5: Distinguish from Intention

Separate incentive effects from individual choices:
- Where do individuals follow incentives despite better judgment?
- Where do individuals resist incentives (and what happens to them)?
- What would a good person do in this structure?
- How does the structure select for certain people?

Blaming individuals is usually less accurate than analyzing structures.

### Step 6: Phase 6: Identify Leverage Points

Find where change is possible:
- Which incentives could be altered?
- Who has the power to change the structure?
- What would make different behavior rational?
- How have similar institutions been reformed?

## Output Format

An incentive analysis including:
1. Institution and behavior being analyzed
2. Incentive structure mapped
3. Key actors and their personal incentives
4. Logic tracing incentives to behavior
5. Verification and testing
6. Intention vs. structure distinction
7. Potential leverage points

## Constraints

- Incentive analysis can become deterministic - individuals do resist
- Some behavior is genuinely malicious, not just incentive-following
- Incentive structures can be hard to observe
- Multiple incentive structures interact
- Analysis shouldn't become excuse ("the structure made them do it")

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

**Input**: Explain why hospitals charge uninsured patients more than insured patients

**Output**:
"Institution: Hospital billing system. Behavior: Uninsured patients charged 'chargemaster' rates 3-10x what insurers pay. Puzzle: This seems cruel - punishing those least able to pay. Incentive structure: Hospitals negotiate with insurers for discounts; chargemaster is the starting point for negotiation; actual payment comes from insurers, not list price; uninsured are small percentage of revenue; billing department metrics don't track patient welfare. Actors: Billing staff follow procedures; administrators focus on insurer negotiations; no one's job depends on fair uninsured pricing. Logic: Chargemaster inflated because insurers negotiate down; uninsured get chargemaster because no one negotiated for them; changing this would require resources with no revenue benefit; staff following rules, not making judgment calls. Verification: Hospitals with different incentives (nonprofits with mission focus) sometimes behave differently. Intention vs. structure: Individual billing clerk isn't cruel; the structure produces cruel outcomes. Leverage: Regulation requiring fair pricing; uninsured advocacy creating reputational cost; reorganizing billing department metrics."

## Integration

Works with:
- **propaganda-model-analysis**: Filters are institutional incentives for media
- **structural-critique**: Connects individual cases to systemic causes
- **moral-responsibility**: Balancing structure analysis with individual accountability