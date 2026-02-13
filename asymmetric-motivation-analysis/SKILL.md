---
name: asymmetric-motivation-analysis
description: Predict competitive dynamics by analyzing who is motivated to attack and who is motivated to retreat in a market.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2958
repository: https://github.com/sethmblack/paks-skills
keywords:
- asymmetric-motivation-analysis
- writing
---

# Asymmetric Motivation Analysis

Predict competitive dynamics by analyzing who is motivated to attack and who is motivated to retreat in a market.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide analysis designed to facilitate predatory market practices
- Make predictions presented as certainties rather than theory-based projections
- Ignore ethical considerations in competitive strategy

**If misapplied:** Explain that asymmetric motivation analysis describes market dynamics, not prescribes exploitation.

---

## When to Use

- User asks "How will competitors respond?"
- User asks "Should we pursue this market?"
- User asks "Will incumbents fight back?"
- User asks "What's the competitive trajectory?"
- Evaluating market entry strategy
- Predicting incumbent response to new business models
- Understanding why competitors act the way they do

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **market_segments** | Yes | Description of market segments from low-end to high-end |
| **players** | Yes | List of competitors with their current positions |
| **margin_structure** | Yes | Relative margins across segments |
| **proposed_action** | No | Specific strategic move being evaluated |

---

## Workflow

### Step 1: Map the Market Segments

Identify segments from low-end to high-end:
- What are the margin profiles of each segment?
- Which segments do incumbents consider attractive vs unattractive?
- Where are incumbents currently concentrated?

### Step 2: Analyze Incumbent Motivation

For each incumbent, assess:
- Which direction are they motivated to move? (Usually upmarket for higher margins)
- What would they gladly abandon? (Low-margin segments that dilute their average)
- What would they defend fiercely? (Core high-value customers)

### Step 3: Analyze Entrant Motivation

For potential entrants, assess:
- Where can they establish a beachhead? (Usually where incumbents are least motivated to defend)
- Which direction are they motivated to move? (Usually upmarket once established)
- What would make them attractive to investors? (Upmarket trajectory)

### Step 4: Project the Dynamics

Based on motivations:
- Who is motivated to attack each segment?
- Who is motivated to retreat from each segment?
- What moves are rational for each player?

### Step 5: Identify Strategic Windows

Find opportunities where:
- Incumbents are motivated to retreat rather than fight
- Entrants can establish position without triggering retaliation
- The improvement trajectory leads to more attractive segments

---

## Outputs

### Asymmetric Motivation Analysis Report

```markdown
## Asymmetric Motivation Analysis: [Market Name]

### Market Segment Map

| Segment | Margin | Incumbent Interest | Current Defenders |
|---------|--------|-------------------|-------------------|
| [Low-end] | [X%] | [Low/Med/High] | [who] |
| [Mid-market] | [X%] | [Low/Med/High] | [who] |
| [High-end] | [X%] | [Low/Med/High] | [who] |

### Player Motivation Matrix

#### [Incumbent A]
- **Current position:** [where in market]
- **Motivated to move:** [which direction and why]
- **Would gladly cede:** [which segments]
- **Would defend fiercely:** [which segments]
- **Rational response to low-end attack:** [what they would do]

#### [Incumbent B]
[Same structure]

#### [Entrant/Potential Entrant]
- **Natural entry point:** [where and why]
- **Improvement trajectory:** [where they would move next]
- **Ultimate ambition:** [where they are heading]

### Competitive Dynamics Projection

**Phase 1 (0-2 years):**
- [Predicted moves and responses]

**Phase 2 (2-5 years):**
- [Predicted moves and responses]

**Phase 3 (5+ years):**
- [Predicted market structure]

### Strategic Windows

| Window | Description | Timing | Risk |
|--------|-------------|--------|------|
| [Window 1] | [Opportunity] | [When] | [What could go wrong] |
| [Window 2] | [Opportunity] | [When] | [What could go wrong] |

### Historical Parallel

[Reference relevant case: steel minimills, disk drives, etc.]

### Key Insight

[Core asymmetry that drives the dynamics]

### Recommendations

For [player perspective being advised]:
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Unclear margin structure | Request information about profitability across segments |
| Only one player considered | Expand analysis to include all relevant competitors |
| Assuming rational response means no response | Clarify that "rational" includes retreat - which is often the rational choice |
| Confusing motivation with capability | Separate what players want to do from what they can do |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "How will enterprise software vendors respond to open-source alternatives?"

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


## Asymmetric Motivation Analysis: Enterprise Software vs Open Source

### Market Segment Map

| Segment | Margin | Incumbent Interest | Current Defenders |
|---------|--------|-------------------|-------------------|
| Individual/small team | 0-5% | Very Low | None (mostly free) |
| SMB self-service | 10-20% | Low | Some SaaS vendors |
| Mid-market with sales | 30-50% | Medium | Established vendors |
| Enterprise with custom | 60-80%+ | Very High | Oracle, SAP, Salesforce |

### Player Motivation Matrix

#### Enterprise Incumbents (Oracle, SAP, Salesforce)
- **Current position:** Enterprise and upper mid-market
- **Motivated to move:** Upmarket - larger deals, more customization, more lock-in
- **Would gladly cede:** SMB, self-service, anything requiring low-touch sales
- **Would defend fiercely:** Enterprise accounts, regulated industries, complex integrations
- **Rational response to open-source attack on low-end:** Retreat upmarket, emphasize support/compliance/integration

#### Open Source Projects/Companies
- **Natural entry point:** Developers, small teams, cost-sensitive organizations
- **Improvement trajectory:** Better enterprise features, manageability, support options
- **Ultimate ambition:** Become credible enterprise alternative (then often get acquired or go proprietary)

### Competitive Dynamics Projection

**Phase 1 (0-2 years):**
- Open source establishes in developer and SMB segments
- Incumbents happy to cede - these segments dilute their margins
- Incumbents publicly dismiss open source as "not enterprise ready"

**Phase 2 (2-5 years):**
- Open source improves, becomes "good enough" for mid-market
- Some incumbents acquire open source companies
- Others create "open core" versions to hedge
- Mid-market disruption begins

**Phase 3 (5+ years):**
- Open source credible for enterprise in many categories
- Incumbents concentrated in most complex/regulated/integrated use cases
- Market bifurcated between commodity (open) and premium (proprietary)

### Strategic Windows

| Window | Description | Timing | Risk |
|--------|-------------|--------|------|
| Land-and-expand | Enter via developers, expand to enterprise | Now | Requires patience for upmarket move |
| Enterprise support layer | Build enterprise layer on open source | 2-3 years | Open source project may commercialize itself |
| Incumbent hedging | Create open source version before disrupted | Now | Cannibalization concerns will limit investment |

### Historical Parallel

Steel minimills followed this exact pattern: attacked rebar (lowest margin), incumbents retreated happily, minimills improved, eventually made sheet steel. Each retreat was rational in isolation; the cumulative effect was devastating.

### Key Insight

Enterprise software vendors are **motivated** to retreat upmarket when attacked from below because it improves their average margins. This rational response creates the opening for open source to improve and expand. The vendors know this is happening but their cost structure and investor expectations make fighting for low-margin segments economically irrational.

### Recommendations

For an enterprise incumbent:
1. Consider acquiring promising open source projects early (before they threaten core)
2. Create a separate unit with different economics to compete in lower segments
3. Focus enterprise positioning on dimensions open source cannot match (compliance, support, liability)

For an open source entrant:
1. Target segments incumbents are happy to abandon
2. Build improvement trajectory toward enterprise features
3. Expect incumbents to ignore you until you are already established

---

## Integration

This skill applies Clayton Christensen's analysis of asymmetric motivation from the steel minimill and disk drive case studies. The key insight: rational profit maximization at each step leads incumbents to retreat rather than fight, creating the conditions for their eventual displacement.