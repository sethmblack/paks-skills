---
name: acquisition-evaluation
description: Evaluate potential acquisitions against strategic fit, cultural compatibility, and integration feasibility using the Iger framework proven across Pixar, Marvel, Lucasfilm, and 21st Century Fox.
license: MIT
metadata:
  version: 1.0.2873
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- acquisition-evaluation
- writing
---

# Acquisition Evaluation

Evaluate potential acquisitions against strategic fit, cultural compatibility, and integration feasibility using the Iger framework proven across Pixar, Marvel, Lucasfilm, and 21st Century Fox.

**Origin:** Bob Iger methodology - "What capability are we acquiring that we cannot build?"

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend acquisitions designed to harm competition through predatory means
- Fabricate financial, cultural, or strategic assessments
- Provide guidance on acquisitions intended to strip and liquidate for short-term gain
- Ignore cultural and talent factors in favor of purely financial analysis

**If asked to evaluate a harmful acquisition:** Refuse explicitly. Explain what you cannot evaluate and why.

---

## When to Use

- User asks "Should we acquire this company?"
- Evaluating M&A targets or acquisition opportunities
- Conducting strategic due diligence beyond financials
- Assessing whether an acquisition serves strategic priorities
- Determining integration complexity before deal commitment

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target_profile** | Yes | Target company description, capabilities, brand, talent |
| **acquirer_priorities** | Yes | Strategic priorities of the acquiring company |
| **cultural_factors** | Yes | Target's culture, leadership, creative/talent dynamics |
| **strategic_rationale** | Yes | Why this acquisition is being considered |
| **financial_context** | No | Valuation, deal structure considerations |
| **integration_timeline** | No | Expected timeline for integration |

---

## Workflow
### Step 1: Apply the Five Acquisition Questions

**Question 1: What capability are we acquiring that we cannot build?**
- If the answer is "content libraries" or "production capacity," that is not enough
- What you cannot easily build: creative culture, trusted brands, talent that other talent wants to work with
- Score: Essential (must have clear answer) / Weak (could build internally) / None (no unique capability)

**Question 2: Does this strengthen our core brand?**
- Does the acquisition enhance or dilute brand perception?
- Will customers see this as a natural extension or a confusing departure?
- Score: Strengthens / Neutral / Dilutes

**Question 3: Can we preserve what made them valuable?**
- What specifically makes this target valuable?
- Can we protect those elements post-acquisition?
- What would destroy the value? (culture imposition, leadership replacement, autonomy reduction)
- Score: Yes with clear plan / Uncertain / High risk of value destruction

**Question 4: Will the talent stay?**
- Creative businesses are talent businesses
- Who are the key people? What are their flight risks?
- What would make them stay? What would make them leave?
- Score: Strong retention confidence / Moderate risk / High flight risk

**Question 5: Does this serve our strategic priorities?**
- Name the specific priorities this serves
- If it does not clearly serve at least one priority, it is a distraction
- Score: Strongly aligned / Partially aligned / Not aligned

### Step 2: Assess Cultural Compatibility

| Factor | Assessment |
|--------|------------|
| Leadership style compatibility | [Compatible / Requires adjustment / Incompatible] |
| Decision-making culture | [Similar / Different but manageable / Fundamental conflict] |
| Creative autonomy expectations | [Can be preserved / Needs negotiation / Will be violated] |
| Geographic/operational independence | [Feasible / Challenging / Impractical] |

### Step 3: Evaluate Integration Approach

**The Pixar Template:**
- Maintain headquarters and independent culture
- Keep leadership in place - they know what made it work
- Social issues before economic issues
- Patience - integration measured in years, not quarters

**Integration Risk Assessment:**
- What must change? What must NOT change?
- Who makes creative decisions post-acquisition?
- How will synergies be captured without destroying value?

### Step 4: Trust Factor Analysis

**Iger insight:** "George Lucas only considered selling to Disney after seeing how we treated Pixar. Trust compounds."

- What is our reputation for treating acquired companies?
- How will this acquisition affect future M&A opportunities?
- Are we building a track record that attracts or repels great companies?

---

## Outputs

### Acquisition Evaluation Report

```markdown
## Acquisition Evaluation: [Target Name]

**Evaluation Date:** [Date]
**Strategic Rationale:** [One-sentence summary]

### Five Question Assessment

| Question | Finding | Score |
|----------|---------|-------|
| Unique capability? | [Analysis] | Essential / Weak / None |
| Brand strengthening? | [Analysis] | Strengthens / Neutral / Dilutes |
| Value preservation? | [Analysis] | Yes / Uncertain / High risk |
| Talent retention? | [Analysis] | Strong / Moderate / High flight risk |
| Priority alignment? | [Analysis] | Strong / Partial / Not aligned |

### Cultural Compatibility Assessment

[Analysis of cultural factors]

### Integration Approach Recommendation

[Specific recommendations for preserving value]

### Key Risks

1. [Risk 1] - Mitigation: [Approach]
2. [Risk 2] - Mitigation: [Approach]
3. [Risk 3] - Mitigation: [Approach]

### Recommendation

**[PROCEED / PROCEED WITH CONDITIONS / DO NOT PROCEED]**

**Rationale:** [2-3 sentences]

**If proceeding, key conditions:**
1. [Condition]
2. [Condition]

**Trust impact:** [How this affects future M&A reputation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Target is purely financial play | Flag as outside framework scope; redirect to financial analysis |
| Acquirer has no clear strategic priorities | Pause evaluation; recommend establishing priorities first |
| Cultural assessment is incomplete | Request additional information; do not proceed without it |
| Target leadership is departing | Major red flag; reassess value proposition entirely |
| Acquisition does not serve any priority | Recommend against unless strategic priorities are updated |

---

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
Target: Creative animation studio (200 employees, strong IP, beloved brand)
Acquirer priorities: 1) Best content, 2) Technology innovation, 3) Global growth
Strategic rationale: Acquire animation capability and IP library
Cultural factors: Founder-led, tight-knit culture, located in different city
```

**Output:**

## Acquisition Evaluation: StudioX Animation

**Evaluation Date:** January 2026
**Strategic Rationale:** Acquire proven animation capability and beloved IP to strengthen content portfolio

### Five Question Assessment

| Question | Finding | Score |
|----------|---------|-------|
| Unique capability? | Creative talent and storytelling culture that takes decades to build; cannot be replicated through hiring | **Essential** |
| Brand strengthening? | StudioX brand has strong family audience loyalty; natural complement to existing portfolio | **Strengthens** |
| Value preservation? | Value is 80% culture and talent, 20% IP; high risk if we impose our processes | **Uncertain** |
| Talent retention? | Founder committed but approaching retirement; key creative directors have limited non-competes | **Moderate risk** |
| Priority alignment? | Directly serves Priority 1 (best content); potential for Priority 2 (tech) via their proprietary tools | **Strong** |

### Cultural Compatibility Assessment

StudioX operates with high creative autonomy and informal decision-making. Our more structured approach could clash. The geographic distance (different city) is actually an advantage - it creates natural separation that protects culture.

Key concern: Founder is the cultural anchor. Succession plan is unclear.

### Integration Approach Recommendation

1. **Maintain StudioX headquarters** - Do not consolidate
2. **Keep creative leadership in place** - Founder stays minimum 3 years as creative chair
3. **Negotiate founder succession** - Identify and develop internal successor during overlap
4. **Limit integration to distribution, marketing, and finance** - Creative decisions stay with StudioX
5. **Protect from corporate bureaucracy** - Shield from our approval processes

### Key Risks

1. **Founder departure** - Mitigation: 3-year commitment plus equity retention incentives
2. **Cultural contamination** - Mitigation: Strict integration boundaries, executive sponsor to protect autonomy
3. **Key talent flight** - Mitigation: Retention packages for top 20 creatives, no relocation requirements

### Recommendation

**PROCEED WITH CONDITIONS**

**Rationale:** StudioX provides essential creative capability that cannot be built internally. The brand is complementary. Primary risks (talent, culture) can be mitigated with disciplined integration approach.

**If proceeding, key conditions:**
1. Founder commits to minimum 3-year creative leadership role
2. Integration boundaries documented and enforced by executive sponsor
3. Retention agreements secured for top 20 creatives before close

**Trust impact:** Successful integration enhances reputation for respecting creative cultures, improving future M&A opportunities.

---

## Integration

**Source Expert:** Bob Iger
**Complementary Skills:** strategic-priority-framework (to ensure priorities exist), cultural-integration-guide (for post-close integration), brand-stewardship-audit (to assess brand impact)

---

## Success Criteria

The evaluation is complete when:
- [ ] All five acquisition questions are answered with evidence
- [ ] Cultural compatibility is assessed
- [ ] Integration approach is defined with specific recommendations
- [ ] Key risks are identified with mitigations
- [ ] Clear recommendation (proceed/conditions/do not proceed) is provided
- [ ] Trust/reputation impact is considered