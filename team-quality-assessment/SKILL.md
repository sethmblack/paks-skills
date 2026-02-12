---
name: team-quality-assessment
description: Assess team quality using John Doerr's missionaries vs mercenaries framework
  and execution capability criteria from his venture capital investment philosophy.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- team-quality-assessment
- writing
---

# Team Quality Assessment

Assess team quality using John Doerr's missionaries vs mercenaries framework and execution capability criteria from his venture capital investment philosophy.

**Token Budget:** ~700 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Make assessments based on protected characteristics
- Recommend discriminatory hiring or firing decisions
- Assess teams for harmful or illegal purposes

**If asked to assess inappropriately:** Refuse and explain the concern.

---

## When to Use

- User says "Evaluate this team", "Are they missionaries or mercenaries?"
- Assessing a founding team for investment or partnership
- Evaluating a team before joining a company
- Determining execution capability for a project

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| team | Yes | Information about team members, roles, backgrounds |
| behaviors | No | Observed behaviors, track record, decisions |
| context | No | Situation being evaluated (investment, hiring, project) |

---

## Workflow

### Step 1: Classify Missionaries vs Mercenaries

**Missionary Indicators:**
- Left lucrative positions to pursue vision
- Building in a space they personally experienced as users
- Talk about customers and mission more than competition and exits
- Demonstrate genuine passion for the problem
- Stay through hard times
- Focus on long-term value creation

**Mercenary Indicators:**
- Primarily motivated by financial outcome
- Talk about exits, valuations, competition
- History of job-hopping for title/money
- Focus on short-term metrics
- Fade when things get difficult
- Optimize for personal gain over team success

**Classification:**
- **Strong Missionaries:** 5-6 missionary indicators, 0-1 mercenary
- **Lean Missionary:** 3-4 missionary indicators, 1-2 mercenary
- **Mixed:** Balance of both
- **Lean Mercenary:** 3-4 mercenary indicators
- **Strong Mercenaries:** 5-6 mercenary indicators

### Step 2: Assess Learning Orientation

"The best entrepreneurs are always learning. They don't know what they don't know, so they attempt to do the impossible."

Evaluate:
- Do they seek feedback?
- How do they respond to criticism?
- Do they adapt based on new information?
- Are they curious or know-it-all?

Score: High Learning / Moderate Learning / Low Learning

### Step 3: Evaluate Execution Capability

- **Track record:** Have they shipped before? What have they built?
- **Urgency:** Are they moving fast? Weekly iteration?
- **Accountability:** Clear goals and ownership?
- **Formidability:** Do they seem like they will win?

Score: High Execution / Moderate Execution / Low Execution

### Step 4: Synthesize Assessment

Combine all factors:
- Missionaries + High Learning + High Execution = Invest
- Mixed signals = Caution, dig deeper
- Mercenaries or Low Execution = Pass

---

## Output Format

```markdown
## Team Quality Assessment: [Team/Company Name]

### Missionaries vs Mercenaries

**Classification:** [Strong Missionaries / Lean Missionary / Mixed / Lean Mercenary / Strong Mercenaries]

**Evidence:**

| Indicator | Observed Behavior | Signal |
|-----------|-------------------|--------|
| [Indicator 1] | [Behavior] | Missionary/Mercenary |
| [Indicator 2] | [Behavior] | Missionary/Mercenary |

### Learning Orientation

**Score:** [High / Moderate / Low]

**Evidence:**
- [Observation 1]
- [Observation 2]

### Execution Capability

**Score:** [High / Moderate / Low]

**Evidence:**
- Track record: [What they've shipped]
- Urgency: [Speed of movement]
- Accountability: [Goal clarity]

### The Trust Question

"Do I want to get in trouble with this founder?"
[Your assessment and reasoning]

### Summary

**Overall Assessment:** [Strong Team / Promising Team / Caution / Avoid]

**Key Strengths:**
1. [Strength 1]
2. [Strength 2]

**Key Concerns:**
1. [Concern 1]
2. [Concern 2]

**Recommendation:**
[Specific recommendation for the context: invest, join, partner, pass]
```

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
Team: Two founders
- CEO: Former product manager at Stripe, left to start company, 3 years at current startup
- CTO: Self-taught engineer, previously built and sold a small SaaS for $500K

Context: Evaluating for Series A investment
```

**Output:**

## Team Quality Assessment: Founders Duo

### Missionaries vs Mercenaries

**Classification:** Strong Missionaries

**Evidence:**

| Indicator | Observed Behavior | Signal |
|-----------|-------------------|--------|
| Left lucrative position | CEO left Stripe PM role | Missionary |
| Long tenure at startup | 3 years at current company | Missionary |
| Self-made builder | CTO built and sold SaaS independently | Missionary |
| Problem passion | Building in space CEO experienced at Stripe | Missionary |

### Learning Orientation

**Score:** High

**Evidence:**
- CEO has product background (customer-focused by training)
- CTO is self-taught (demonstrates learning capability)
- Previous exit shows ability to learn and adapt

### Execution Capability

**Score:** High

**Evidence:**
- Track record: CEO shipped at Stripe; CTO built and exited a company
- Urgency: 3 years of consistent building demonstrates persistence
- Accountability: Previous exit shows ability to deliver

### The Trust Question

"Do I want to get in trouble with this founder?"

Yes. The CEO left a prestigious role at Stripe (not chasing easy money) and has stayed 3 years building (not a quitter). The CTO has actually built and sold something (proven execution). These are people who finish what they start.

### Summary

**Overall Assessment:** Strong Team

**Key Strengths:**
1. Clear missionary orientation - building from genuine problem experience
2. Proven execution - both have shipped real things
3. Complementary skills - product + technical founder combo

**Key Concerns:**
1. First time working together (team chemistry unknown)
2. CTO's previous exit was small ($500K) - unknown how they scale

**Recommendation:**
Proceed with investment. This is a strong founding team with missionary orientation and demonstrated execution. Recommend diligence on team chemistry and CTO's ability to build larger engineering organization.

---

## Integration

This skill integrates with the **john-doerr** expert persona. Apply Doerr's lens: missionaries over mercenaries, always ask the trust question, back teams that seem formidable.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient team info | Flag as critical gap; request more data |
| Only one data point | Note limited evidence, caveat conclusions |
| Team has mixed signals | Recommend deeper diligence |