---
name: startup-investment-evaluation
description: 'Evaluate a startup or opportunity using John Doerr''s venture capital
  investment criteria: the Five Criteria for Series A investments and the missionaries
  vs mercenaries team assessment framework.'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- startup-investment-evaluation
- writing
---

# Startup Investment Evaluation

Evaluate a startup or opportunity using John Doerr's venture capital investment criteria: the Five Criteria for Series A investments and the missionaries vs mercenaries team assessment framework.

**Token Budget:** ~900 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Evaluate companies engaged in clearly illegal activities
- Provide investment advice that requires licensure (clarify this is a framework, not financial advice)
- Endorse schemes that would harm consumers or investors

**Disclaimer:** This evaluation framework is for analytical purposes. It does not constitute investment advice. Consult qualified professionals for investment decisions.

---

## When to Use

- User says "Evaluate this startup", "Should I invest in this?", "Assess this opportunity"
- User is evaluating a pitch deck or investment opportunity
- User is assessing whether to join a startup
- User is deciding whether to partner with or acquire a company

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| company | Yes | Company description, pitch, or overview |
| team | Yes | Information about founders and key team members |
| market | No | Market size, dynamics, timing |
| financials | No | Revenue, growth, funding history |

---

## Workflow

### Step 1: Evaluate the Five Criteria

**Criterion 1: Technical Excellence**
- Is the product/technology differentiated?
- Does the engineering team demonstrate excellence?
- Is there a defensible technical advantage?
- Score: Strong / Adequate / Weak

**Criterion 2: Outstanding Leadership**
- Is there business leadership beyond technical skill?
- Does leadership understand operations, culture, go-to-market?
- Is there a complete leadership team or gaps?
- Score: Strong / Adequate / Weak

**Criterion 3: Strategic Focus on Large Market**
- Is the target market large enough (10x+ return potential)?
- Is the market rapidly growing?
- Is the timing right? (Better too early than too late)
- Score: Strong / Adequate / Weak

**Criterion 4: Reasonable Financing Structure**
- Are incentives aligned between founders and investors?
- Is the valuation reasonable for the stage?
- Is the cap table clean?
- Score: Strong / Adequate / Weak

**Criterion 5: Tremendous Sense of Urgency**
- Is the team moving fast?
- Is there weekly/daily iteration?
- Do they have clear OKRs and accountability?
- Score: Strong / Adequate / Weak

### Step 2: Apply the Team Test

**Missionaries vs Mercenaries Assessment:**

| Trait | Missionaries | Mercenaries |
|-------|-------------|-------------|
| Motivation | Purpose and passion | Profit and exit |
| Durability | Sustain through hard times | Fade when difficult |
| Focus | Customers and mission | Competition and returns |
| Learning | Always learning, humble | Know-it-all attitude |

Classify the team: Strong Missionaries / Mixed / Mercenaries

### Step 3: The Trust Question

Ask: "Do I want to get in trouble with this founder? Because we will get in trouble together."

- Would you want to work through crises with this person?
- Do they have your back?
- Are they willing to make new mistakes together?

### Step 4: Synthesize Recommendation

Based on all criteria:
- **Strong Recommend:** 4-5 criteria strong, missionary team
- **Conditional Recommend:** 3+ criteria strong, addressable gaps
- **Pass:** Major gaps in team, market, or execution capability

---

## Output Format

```markdown
## Startup Evaluation: [Company Name]

### Five Criteria Assessment

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Technical Excellence | Strong/Adequate/Weak | [Key observation] |
| Outstanding Leadership | Strong/Adequate/Weak | [Key observation] |
| Large Market | Strong/Adequate/Weak | [Key observation] |
| Financing Structure | Strong/Adequate/Weak | [Key observation] |
| Sense of Urgency | Strong/Adequate/Weak | [Key observation] |

### Team Assessment

**Classification:** Missionaries / Mixed / Mercenaries

**Evidence:**
- [Observation 1]
- [Observation 2]

**Trust Question:** [Would you want to get in trouble with this founder?]

### Key Strengths
1. [Strength 1]
2. [Strength 2]

### Key Concerns
1. [Concern 1]
2. [Concern 2]

### Recommendation

**Verdict:** Strong Recommend / Conditional Recommend / Pass

**Rationale:** [2-3 sentence summary]

**If proceeding, key questions to resolve:**
1. [Question 1]
2. [Question 2]
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
Company: AI-powered code review tool
Team: Two ex-Google engineers, first-time founders
Market: Developer tools, $50B market
Traction: 1,000 users, $10K MRR, 20% MoM growth
```

**Output:**

## Startup Evaluation: AI Code Review Tool

### Five Criteria Assessment

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Technical Excellence | Strong | Ex-Google engineers, differentiated AI approach |
| Outstanding Leadership | Adequate | Technical strength but no business/GTM leader |
| Large Market | Strong | $50B market, clear secular trend to AI |
| Financing Structure | Not assessed | No financials provided |
| Sense of Urgency | Strong | 20% MoM growth indicates execution speed |

### Team Assessment

**Classification:** Strong Missionaries

**Evidence:**
- Left Google to pursue vision (not for money)
- Building in space they experienced as users
- Demonstrate learning orientation (first-time founders)

**Trust Question:** Preliminary yes - left lucrative roles, mission-driven

### Key Strengths
1. Strong technical foundation from Google pedigree
2. Clear product-market fit signal (20% MoM growth)
3. Large, growing market with AI tailwind

### Key Concerns
1. No business/GTM leader - need to hire
2. First-time founders - execution risk in scaling
3. Competitive market - need to move fast

### Recommendation

**Verdict:** Conditional Recommend

**Rationale:** Strong technical team in a large market with early traction. The missionary orientation is clear. The gap is business leadership which should be addressable.

**If proceeding, key questions to resolve:**
1. What is the plan to hire a business-oriented co-founder or VP Sales?
2. How will they compete against GitHub Copilot and established players?
3. What is the path to $1M ARR?

---

## Integration

This skill integrates with the **john-doerr** expert persona. Apply Doerr's lens: teams matter most, missionaries over mercenaries, urgency is critical, better too early than too late.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient team info | Flag as critical gap; cannot evaluate without team data |
| No market size data | Estimate or note as requiring research |
| Obvious red flags | Highlight prominently; recommend pass if severe |