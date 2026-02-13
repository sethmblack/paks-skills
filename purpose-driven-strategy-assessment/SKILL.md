---
name: purpose-driven-strategy-assessment
description: Evaluate whether a business strategy authentically integrates purpose with profit, distinguishing genuine transformation from CSR theater.
license: MIT
metadata:
  version: 1.0.4771
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- purpose-driven-strategy-assessment
- transformation
- writing
---

# Purpose-Driven Strategy Assessment

Evaluate whether a business strategy authentically integrates purpose with profit, distinguishing genuine transformation from CSR theater.

**Token Budget:** ~800 tokens. Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Rubber-stamp purpose statements without evidence of core business integration
- Validate "purpose-washing" that masks harmful business practices
- Approve strategies that externalize social/environmental costs while claiming purpose
- Ignore stakeholder harm in pursuit of shareholder value

**If the strategy causes measurable harm:** Flag it explicitly. Purpose cannot coexist with harm.

---

## When to Use

- User asks "How do I make my business more purposeful?"
- User asks "Is our purpose authentic or performative?"
- User wants to evaluate strategy-purpose alignment
- User is designing a purpose-driven transformation
- User needs to distinguish CSR from core business purpose

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **strategy_description** | Yes | Current or proposed business strategy |
| **purpose_statement** | No | Existing purpose/mission statement (if any) |
| **stakeholder_map** | No | Key stakeholders and their needs |
| **financial_context** | No | Revenue model, constraints, investor expectations |

---

## The Nooyi Test: Four Pillars

Authentic purpose-driven strategy must address ALL four pillars:

### 1. Human Sustainability
Does the strategy improve outcomes for people who use your products/services?
- Not: "We donate to charity"
- Yes: "We reformulated products to reduce harm"
- Test: Would customers be healthier/better off if they consumed MORE of what you sell?

### 2. Environmental Sustainability
Does the strategy reduce environmental impact of CORE operations?
- Not: "We offset carbon with credits"
- Yes: "We reduced water consumption 26% per unit produced"
- Test: Is sustainability embedded in operations or bolted on?

### 3. Talent Sustainability
Does the strategy create workplaces where people thrive?
- Not: "We have a wellness program"
- Yes: "We redesigned work to enable people to have careers AND lives"
- Test: Would your best employees recommend this workplace to their children?

### 4. Financial Performance
Does purpose DRIVE financial returns (not compete with them)?
- Not: "Purpose is good but expensive"
- Yes: "Purpose attracts talent, customers, and long-term investors"
- Test: Can you show how purpose investments generate returns?

---

## Workflow
### Step 1: Purpose Authenticity Check
Evaluate the purpose statement against three tests:

| Test | Question | Red Flag |
|------|----------|----------|
| **Core business** | Does purpose change what you sell or how you operate? | Purpose is only in CSR/marketing |
| **Measurable** | Are there public targets with accountability? | Vague aspirations without metrics |
| **Defensible** | Would you defend this against short-term pressure? | Purpose abandoned when profits dip |

### Step 2: Four Pillar Assessment
Score each pillar 1-5:
- 1: Not addressed
- 2: Mentioned but performative
- 3: Some initiatives, not integrated
- 4: Integrated into operations
- 5: Core to business model

### Step 3: Stakeholder Value Audit
For each major stakeholder, answer:
- What value does this strategy create for them?
- What harm does it create or fail to prevent?
- Is the value proposition sustainable long-term?

### Step 4: Integration Gap Analysis
Identify where purpose and profit diverge:
- Where do short-term profits conflict with purpose?
- What investments are needed to close gaps?
- What must be abandoned to make room for purpose?

### Step 5: Transformation Roadmap
Create actionable path from current state to purpose integration.

---

## Outputs

### Purpose-Driven Strategy Assessment Report

```markdown
## Assessment: [Organization/Strategy Name]

### Purpose Authenticity Score: [X/15]

| Test | Score (1-5) | Evidence |
|------|-------------|----------|
| Core business integration | X | [specific evidence] |
| Measurable targets | X | [specific evidence] |
| Defensible under pressure | X | [specific evidence] |

### Four Pillar Assessment: [X/20]

| Pillar | Score (1-5) | Assessment |
|--------|-------------|------------|
| Human Sustainability | X | [analysis] |
| Environmental Sustainability | X | [analysis] |
| Talent Sustainability | X | [analysis] |
| Financial Performance | X | [analysis] |

### Stakeholder Value Analysis

| Stakeholder | Value Created | Harm/Gaps | Sustainability |
|-------------|---------------|-----------|----------------|
| Customers | [value] | [gaps] | [long-term?] |
| Employees | [value] | [gaps] | [long-term?] |
| Communities | [value] | [gaps] | [long-term?] |
| Environment | [value] | [gaps] | [long-term?] |
| Shareholders | [value] | [gaps] | [long-term?] |

### Integration Gaps

1. [Gap 1]: [description and investment needed]
2. [Gap 2]: [description and investment needed]

### Verdict

**AUTHENTIC PURPOSE** (30-35): Strategy transforms core business
**PROMISING** (20-29): Good foundation, needs deeper integration
**PERFORMATIVE** (10-19): Purpose is bolted on, not built in
**PURPOSE-WASHING** (<10): Marketing without substance

### Recommendations

1. [Priority 1 action]
2. [Priority 2 action]
3. [Priority 3 action]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No strategy provided | Request strategy description before assessment |
| Strategy clearly harmful | Flag harm explicitly, refuse to "purpose-wash" |
| Purpose is only philanthropy | Explain difference between CSR and core business purpose |
| Financial data missing | Assess qualitatively, note uncertainty |
| Stakeholders undefined | Help identify key stakeholder groups |

---

## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences

## Example

**Input:**
"Our beverage company wants to add a purpose statement about 'refreshing the world.' We'll donate 1% of profits to clean water initiatives."

**Assessment:**

### Purpose Authenticity Score: 5/15

| Test | Score | Evidence |
|------|-------|----------|
| Core business integration | 1 | Purpose doesn't change products or operations |
| Measurable targets | 2 | 1% donation is measurable but doesn't drive business |
| Defensible under pressure | 2 | Donations are first cut when profits decline |

### Four Pillar Assessment: 6/20

| Pillar | Score | Assessment |
|--------|-------|------------|
| Human Sustainability | 1 | Products unchanged; sugar content not addressed |
| Environmental Sustainability | 2 | Clean water donations don't reduce operational impact |
| Talent Sustainability | 1 | No workplace transformation mentioned |
| Financial Performance | 2 | Donations are cost, not driver of returns |

### Verdict: PURPOSE-WASHING

This is philanthropy, not purpose-driven strategy. "Refreshing the world" while selling high-sugar beverages creates cognitive dissonance.

**To become authentic:**
1. Reformulate products to reduce sugar/artificial ingredients
2. Set public targets for portfolio shift (50% healthier options by 2030)
3. Measure water usage per unit produced, not just donations
4. Make clean water part of supply chain, not charity

---

## Integration

This skill is derived from **Indra Nooyi's** "Performance with Purpose" framework at PepsiCo. Her key insight: purpose must transform the core business, not exist alongside it.

When using this skill, maintain Nooyi's voice:
- Long-term orientation over quarterly appeasement
- Skepticism of "purpose-washing" and CSR theater
- Insistence that purpose and profit are complementary
- Honest acknowledgment of trade-offs and investments required