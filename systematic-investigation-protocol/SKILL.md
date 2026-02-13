---
name: systematic-investigation-protocol
description: Design a rigorous investigation process for any research question or problem, following Marie Curie's measurement-controlled method that led to the discovery of radium.
license: MIT
metadata:
  version: 1.0.2043
  author: sethmblack
keywords:
- systematic-investigation-protocol
- transformation
- writing
---

# Systematic Investigation Protocol

Design a rigorous investigation process for any research question or problem, following Marie Curie's measurement-controlled method that led to the discovery of radium.

---

## When to Use

- User needs to investigate a complex problem systematically
- Designing a research approach or experimental protocol
- Moving from vague curiosity to structured inquiry
- Request for "scientific approach" or "rigorous investigation"
- Starting a project without clear methodology

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| question | Yes | The research question, problem, or phenomenon to investigate |
| resources | No | Available tools, time, expertise, or materials |
| constraints | No | Limitations on approach (time, ethics, access, budget) |
| prior_knowledge | No | What is already known about the subject |

---

## The Six-Step Protocol

### Step 1: Define What You Observe (Baseline Measurement)

Establish the current state of knowledge precisely:
- What do we actually know? (Not assume, not believe—know)
- What has been measured or documented?
- What is the baseline against which we compare?
- What precision do our observations have?

**Curie's principle:** "To answer this, I measured. I tested every compound available, one by one, recording their radioactivity."

### Step 2: Identify What Is Unexpected (Anomaly Detection)

Find the gaps between expectation and observation:
- What observations contradict our models?
- Where does reality exceed or fall short of prediction?
- What doesn't fit the established pattern?
- What have others overlooked or dismissed?

**Curie's principle:** "Pitchblende was more radioactive than pure uranium. This was unexpected—how could the ore exceed its own component?"

### Step 3: Form Testable Hypotheses

Generate explanations that can be verified or falsified:
- What could explain the anomaly?
- What would each hypothesis predict?
- How would we distinguish between explanations?
- What is the simplest explanation consistent with data?

**Curie's principle:** "There must be another substance present, something unknown, something far more radioactive than uranium itself."

### Step 4: Design Measurement-Controlled Tests

Create experiments that generate decisive data:
- What measurement would confirm or refute each hypothesis?
- How can we isolate the variable of interest?
- What precision is required?
- What controls are necessary?

**Curie's principle:** "We dissolved the ore in acid, precipitated different fractions, tested each fraction for radioactivity, and followed the radioactive trail."

### Step 5: Execute with Patient Persistence

Conduct the investigation systematically:
- Follow the protocol rigorously
- Document everything—successes and failures
- Adjust methods based on results, not hope
- Accept that meaningful results take time

**Curie's principle:** "This process took four years. Each day we made progress, however small. That is how science advances—not by leaps, but by countless measured steps."

### Step 6: Conclude with Humility

Draw conclusions appropriate to the evidence:
- What do the measurements actually show?
- What remains uncertain or unknown?
- What are the limits of our conclusions?
- What questions does this open for future investigation?

**Curie's principle:** "I never see what has been done; I only see what remains to be done."

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
## Systematic Investigation Protocol

### Research Question
[Clear statement of what we're trying to learn]

### Baseline: What We Know
- Established fact 1: [measurement/source]
- Established fact 2: [measurement/source]
- Current precision: [level of certainty]

### Anomalies: What's Unexpected
- Anomaly 1: [observation] contradicts [expectation]
- Anomaly 2: [observation] exceeds [prediction]
- Priority anomaly to investigate: [which and why]

### Hypotheses
| Hypothesis | Would Predict | Test Required |
|------------|---------------|---------------|
| H1 | ... | ... |
| H2 | ... | ... |

### Investigation Plan
**Phase 1:** [Initial measurements]
- Measurement: [what to measure]
- Method: [how]
- Expected duration: [time]
- Success criteria: [what would confirm/refute]

**Phase 2:** [Follow-up based on Phase 1]
- If H1 supported: [next steps]
- If H2 supported: [next steps]

### Resources Required
- [List of tools, materials, expertise]

### Constraints and Adaptations
- Constraint: [limitation] → Adaptation: [how to work within it]

### What Remains Unknown
- [Honest acknowledgment of uncertainty]
- [Questions for future investigation]
```

---

## Constraints

- Do not skip measurement—claims without data are not science
- Do not rush to conclusions—let data lead
- Do not ignore anomalies—they are often the most valuable signals
- Do not overstate certainty—acknowledge what remains unknown
- Accept that meaningful investigation takes time

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

**Input:** "I want to understand why our customer retention drops sharply at month 6. We've assumed it's pricing, but I'm not sure."

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


## Systematic Investigation Protocol

### Research Question
What causes the sharp decline in customer retention at month 6, and is pricing the primary factor?

### Baseline: What We Know
- Retention rate months 1-5: 87% (measured from cohort analysis)
- Retention rate month 6: 62% (25 point drop)
- Retention rate months 7-12: 61-63% (stable after drop)
- Current pricing: $X/month, no change at month 6
- Data source: Product analytics, last 8 cohorts

### Anomalies: What's Unexpected
- Anomaly 1: Drop is sudden (one month) not gradual—suggests trigger event, not erosion
- Anomaly 2: Pricing hasn't changed, but assumption is "pricing problem"—why?
- Anomaly 3: Stability after month 6 suggests survivors are committed
- Priority anomaly: The suddenness. Pricing effects typically show gradual decline.

### Hypotheses
| Hypothesis | Would Predict | Test Required |
|------------|---------------|---------------|
| H1: Pricing | Churned users cite cost; staying users have higher budgets | Survey churned users; compare budget segments |
| H2: Feature gap | Users hit limitation at month 6 maturity | Usage analysis of churned vs. retained at month 5 |
| H3: Competitor targeting | Competitors market to 6-month users | Competitive intelligence; ask churned where they went |
| H4: Initial contract/trial end | Commitment point forces decision | Check contract terms; when do trials/promos end? |

### Investigation Plan
**Phase 1:** Contract and pricing structure analysis (1 day)
- Measurement: Do any contracts, trials, or promotional rates end at month 6?
- Method: Review billing data, contract terms
- Success criteria: If yes, explains timing perfectly—pricing hypothesis gains support

**Phase 2:** Churn survey (1 week)
- Measurement: What do churned customers say caused their departure?
- Method: Email survey to month-6 churners, last 3 cohorts
- Success criteria: If >50% cite single reason, strong signal

**Phase 3:** Usage pattern analysis (3 days)
- Measurement: Do retained and churned users behave differently in month 5?
- Method: Compare feature usage, engagement metrics pre-churn
- Success criteria: Distinct behavioral signature predicts churn

### Resources Required
- Access to billing/contract data
- Survey tool and customer email list
- Product analytics access
- 2 weeks total investigation time

### Constraints and Adaptations
- Constraint: Can't interview all churned users → Survey with open-ended option for detailed feedback
- Constraint: Historical data only → Focus on patterns, follow up with prospective study if needed

### What Remains Unknown
- Whether month-6 churners would have stayed with intervention
- Long-term value difference between early vs. late churners
- Competitive landscape at this customer stage

**Next measurement:** Start with Phase 1—if contract terms explain timing, we've found our answer quickly. If not, proceed to parallel execution of Phases 2 and 3.

---

## Integration

This skill is part of the **Marie Curie** expert persona. Use it when you need to transform vague inquiry into rigorous, measurement-controlled investigation.