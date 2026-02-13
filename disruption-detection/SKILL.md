---
name: disruption-detection
description: Analyze a competitive threat or new technology to classify it as sustaining or disruptive innovation, predict its trajectory, and recommend a strategic response.
license: MIT
metadata:
  version: 1.0.3842
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- disruption-detection
- writing
---

# Disruption Detection

Analyze a competitive threat or new technology to classify it as sustaining or disruptive innovation, predict its trajectory, and recommend a strategic response.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide analysis to facilitate market manipulation or anticompetitive behavior
- Make predictions presented as certainties rather than theory-based projections
- Apply disruption theory to situations where it does not fit

**If misapplied:** Explain that not every competitive threat is disruption and clarify the correct classification.

---

## When to Use

- User asks "Is this disruptive?"
- User asks "Should we worry about this new entrant?"
- User presents a competitive threat for analysis
- User asks about a new technology's market trajectory
- Strategic planning discussions about emerging competitors
- Evaluating whether a startup poses a threat to an incumbent

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **threat_description** | Yes | Description of the new entrant, technology, or product |
| **current_market** | Yes | Description of the incumbent's market and customer segments |
| **target_customers** | No | Who the new entrant is serving (if known) |
| **performance_comparison** | No | How the new solution compares on key dimensions |

---

## Workflow

### Step 1: Identify the Target Customer

Determine who the new entrant is targeting:
- Are they serving the incumbent's most demanding customers? (Sustaining)
- Are they serving overserved customers who do not need all the performance? (Low-end disruption)
- Are they serving non-consumers who could not previously access or afford solutions? (New-market disruption)

### Step 2: Assess Initial Performance

Evaluate how the new solution compares:
- Is it better than incumbents on dimensions existing customers value? (Sustaining)
- Is it worse on valued dimensions but good enough for a different segment? (Potentially disruptive)
- Is it introducing different dimensions of performance entirely? (Potentially disruptive)

### Step 3: Analyze the Business Model

Examine the economics:
- Does the new entrant's cost structure allow profitability at lower price points?
- Does their go-to-market approach reach customers the incumbent does not serve?
- Would the incumbent need a different business model to compete?

### Step 4: Project the Trajectory

Apply disruption theory patterns:
- If disruptive: The entrant will improve and eventually become "good enough" for mainstream
- The danger is not today's threat but tomorrow's capability
- Estimate timeline based on rate of improvement

### Step 5: Classify and Recommend

Provide classification with confidence level and recommended response.

---

## Outputs

### Disruption Analysis Report

```markdown
## Disruption Analysis: [Threat Name]

### Classification
**Type:** [Sustaining Innovation | Low-End Disruption | New-Market Disruption | Not Disruption]
**Confidence:** [High | Medium | Low]

### Evidence

**Target Customer Analysis:**
- Current target: [who they are serving now]
- Incumbent's interest in this segment: [high/low and why]

**Performance Assessment:**
- Valued dimensions where incumbent leads: [list]
- Dimensions where entrant is "good enough" or better: [list]
- New dimensions introduced: [list if any]

**Business Model Comparison:**
| Dimension | Incumbent | Entrant |
|-----------|-----------|---------|
| Cost structure | | |
| Target margin | | |
| Go-to-market | | |
| Customer acquisition | | |

### Trajectory Projection

**Current state:** [description]
**Projected evolution:** [description]
**Timeline to mainstream threat:** [estimate with reasoning]

### Historical Parallel
[Reference a relevant case study: disk drives, steel, retail, etc.]

### Strategic Implications

**If Sustaining:** Compete directly. Incumbents have advantages in resources, customer relationships, and distribution.

**If Disruptive:** Do not ignore. Consider:
1. [Specific recommendation 1]
2. [Specific recommendation 2]
3. [Specific recommendation 3]

### Warning Signs to Monitor
- [Signal 1]
- [Signal 2]
- [Signal 3]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Ask clarifying questions about target customers and performance |
| Threat is neither sustaining nor disruptive | Explain it may be a substitute or different market entirely |
| User insists something is disruptive when it is not | Cite Christensen's explicit criteria; note that Uber was NOT considered disruptive |
| Multiple potential classifications | Present each with evidence; note which is most likely |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Is ChatGPT disruptive to Google Search?"

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


## Disruption Analysis: ChatGPT vs Google Search

### Classification
**Type:** New-Market Disruption (partial) with Sustaining elements
**Confidence:** Medium (still early in trajectory)

### Evidence

**Target Customer Analysis:**
- Current target: Users seeking direct answers, code help, explanations - many who previously found search results frustrating
- Incumbent's interest: Google highly values all search users; this is their core market

**Performance Assessment:**
- Valued dimensions where Google leads: Real-time information, source verification, breadth of web access
- Dimensions where ChatGPT is "good enough" or better: Direct answers without link navigation, conversational follow-up, code generation
- New dimensions introduced: Reasoning-based responses, task completion, synthesis across sources

**Business Model Comparison:**
| Dimension | Google | ChatGPT |
|-----------|--------|---------|
| Cost structure | Ad-supported, low marginal cost | Compute-intensive, high marginal cost |
| Target margin | Very high (advertising) | Currently subsidized/subscription |
| Go-to-market | Default browser, Android | Direct consumer, API |
| Customer acquisition | Embedded in ecosystem | Product-led growth |

### Trajectory Projection

**Current state:** ChatGPT serves queries Google handles poorly (explanations, synthesis, creation)
**Projected evolution:** Improving on real-time data, citations, accuracy - the dimensions where Google leads
**Timeline to mainstream threat:** Already mainstream for certain query types; 2-5 years for broader substitution

### Historical Parallel
Similar to Netflix disrupting Blockbuster: started by serving an underserved use case (DVD by mail for patient viewers), then shifted to streaming which directly competed. ChatGPT started with use cases search handles poorly, now expanding.

### Strategic Implications

This is a genuine competitive threat, though not classic low-end disruption:
1. Google cannot ignore this - it targets their core users for certain query types
2. Google must respond with AI integration (which they are doing)
3. The business model question is unresolved - ChatGPT's costs may not support ad-free model at scale

### Warning Signs to Monitor
- ChatGPT accuracy and real-time capabilities improving
- Users defaulting to ChatGPT before trying Google
- Advertisers shifting budgets to AI interfaces

---

## Integration

This skill originates from Clayton Christensen's disruption theory. When invoked, apply Christensen's analytical rigor: theory predicts, correlation describes. Avoid calling everything "disruption" - most innovation is sustaining, and that matters for the correct strategic response.