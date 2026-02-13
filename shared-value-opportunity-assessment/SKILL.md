---
name: shared-value-opportunity-assessment
description: Identify opportunities to create economic value while simultaneously creating value for society using Porter's Creating Shared Value (CSV) framework.
license: MIT
metadata:
  version: 1.0.1884
  author: sethmblack
keywords:
- shared-value-opportunity-assessment
- transformation
- writing
---

# Shared Value Opportunity Assessment

Identify opportunities to create economic value while simultaneously creating value for society using Porter's Creating Shared Value (CSV) framework.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Confuse shared value with philanthropy or CSR
- Recommend social initiatives disconnected from business value
- Ignore the economic case for social impact
- Greenwash — claiming shared value where none exists

**Key distinction:** Shared value is NOT about redistributing existing value. It is about expanding the total pool of economic and social value through business innovation.

---

## When to Use

- User asks "How can we create shared value?" or "CSV analysis"
- User wants to connect social impact with business strategy
- User asks "How can social initiatives drive profit?"
- When developing sustainability or ESG strategy with business impact
- User asks "What's the business case for [social initiative]?"
- When evaluating whether social programs should be strategic priorities

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **company** | Yes | The company to analyze |
| **industry** | Yes | Industry context |
| **social_challenges** | No | Specific social or environmental challenges to consider |
| **operating_context** | No | Key markets, communities, or geographies |

**Input Validation:**
- Must understand the business model to connect social value to economic value
- Must understand operating context to identify relevant social challenges

---

## Workflow

### Step 1: Understand the Business Model

Before identifying shared value opportunities:
- What is the company's value proposition?
- Who are the customers?
- What is the value chain?
- What are the key cost and differentiation drivers?

### Step 2: Analyze Three Levels of Shared Value

**Level 1: Reconceiving Products and Markets**
- What societal needs could be met through products/services?
- What underserved markets could be profitably accessed?
- How could products be redesigned to address social issues?

Questions to ask:
- What social problems intersect with what we sell?
- Who is underserved by current market offerings?
- How could we modify products to be healthier, safer, more accessible, more sustainable?
- What new markets would open if we addressed a social need?

**Level 2: Redefining Productivity in the Value Chain**
- Where do social problems affect productivity?
- Where could social improvements reduce costs?
- Where could employee or community investments improve operations?

Questions to ask:
- Where are there environmental costs embedded in our value chain?
- Where could energy efficiency, water efficiency, or waste reduction improve margins?
- How does employee health, skills, or engagement affect productivity?
- How do supplier capabilities affect our costs and quality?
- Where does community infrastructure affect our operations?

**Level 3: Enabling Local Cluster Development**
- What weaknesses in the local cluster hurt the business?
- What community investments would improve competitiveness?
- What industry-wide improvements would benefit all players?

Questions to ask:
- What skills gaps affect our ability to hire?
- What infrastructure limitations affect our operations?
- What supplier or service provider weaknesses hurt us?
- What regulatory or institutional gaps create friction?

### Step 3: Assess Business Value

For each opportunity, evaluate:
- Revenue impact (new markets, premium pricing, customer loyalty)
- Cost impact (efficiency, risk reduction, productivity)
- Risk reduction (regulatory, reputational, supply chain)
- Competitive advantage (differentiation, barriers to entry)

### Step 4: Assess Social Value

For each opportunity, evaluate:
- Scale of impact (how many people affected?)
- Depth of impact (how significant is the change?)
- Sustainability (does it create lasting change?)
- Measurability (can we track outcomes?)

### Step 5: Prioritize Opportunities

Rank opportunities by:
- Business value potential (High / Medium / Low)
- Social value potential (High / Medium / Low)
- Feasibility (High / Medium / Low)
- Strategic fit with existing capabilities

---

## Shared Value vs. CSR

| Corporate Social Responsibility | Creating Shared Value |
|--------------------------------|----------------------|
| Value: doing good | Value: economic and social benefits relative to cost |
| Citizenship, philanthropy | Joint company and community value creation |
| Discretionary or responding to pressure | Integral to competing |
| Agenda determined externally | Agenda company-specific, internally generated |
| Impact limited by corporate footprint | Realigns entire company budget |
| Example: Fair trade purchasing | Example: Transforming procurement to increase quality and yield |

---

## Outputs

Format the output as a **Shared Value Opportunity Assessment**:

```markdown
## Shared Value Opportunity Assessment: [Company Name]

**Industry:** [Industry]
**Analysis Date:** [Date]

---

### Business Model Summary

[Brief description of how the company creates value]

---

### Level 1: Reconceiving Products and Markets

#### Opportunities Identified

| Opportunity | Social Need Addressed | Business Value | Feasibility |
|-------------|----------------------|----------------|-------------|
| [Opportunity] | [Need] | [Value] | [H/M/L] |

#### Top Opportunity: [Name]
**Social need:** [Description]
**Business case:**
- Revenue impact: [Assessment]
- Differentiation: [Assessment]
- Market expansion: [Assessment]
**Implementation considerations:** [Key factors]

---

### Level 2: Redefining Productivity in the Value Chain

#### Opportunities Identified

| Value Chain Area | Opportunity | Social Benefit | Cost Reduction |
|------------------|-------------|----------------|----------------|
| [Area] | [Opportunity] | [Benefit] | [Savings] |

#### Top Opportunity: [Name]
**Social benefit:** [Description]
**Business case:**
- Cost reduction: [Assessment]
- Risk mitigation: [Assessment]
- Productivity gain: [Assessment]
**Implementation considerations:** [Key factors]

---

### Level 3: Enabling Local Cluster Development

#### Opportunities Identified

| Cluster Weakness | Investment Opportunity | Business Benefit | Community Benefit |
|------------------|----------------------|------------------|-------------------|
| [Weakness] | [Investment] | [Benefit] | [Benefit] |

#### Top Opportunity: [Name]
**Cluster weakness addressed:** [Description]
**Business case:**
- Competitive context improvement: [Assessment]
- Supply chain strengthening: [Assessment]
- Talent pipeline development: [Assessment]
**Implementation considerations:** [Key factors]

---

### Priority Ranking

| Rank | Opportunity | Level | Business Value | Social Value | Feasibility |
|------|-------------|-------|----------------|--------------|-------------|
| 1 | [Name] | [1/2/3] | [H/M/L] | [H/M/L] | [H/M/L] |
| 2 | [Name] | [1/2/3] | [H/M/L] | [H/M/L] | [H/M/L] |
| 3 | [Name] | [1/2/3] | [H/M/L] | [H/M/L] | [H/M/L] |

---

### Recommendations

1. **Immediate action:** [Opportunity with high feasibility and clear value]
2. **Strategic initiative:** [Larger opportunity requiring investment]
3. **Explore further:** [Promising but needs more analysis]

---

### Not Shared Value (CSR/Philanthropy)

[Note any social activities that are valuable but not shared value—they don't create business value. These may still be worth doing but should be classified correctly.]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No obvious shared value opportunities | Focus on Level 2 (value chain) — almost always has opportunities |
| User wants to label philanthropy as shared value | Explain the distinction; both are valid, but different |
| Insufficient information about operations | Focus on industry-typical opportunities |
| Conflicting social and business priorities | Acknowledge tension; shared value is not always possible |
| Skepticism about business case | Ground recommendations in specific economic mechanisms |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Assess shared value opportunities for a large food company"

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


## Shared Value Opportunity Assessment: Large Food Company

**Industry:** Packaged Food
**Analysis Date:** 2026-01-28

### Business Model Summary

Large packaged food company with global operations, sourcing agricultural inputs from thousands of suppliers across multiple continents. Revenue driven by branded consumer products sold through retail channels. Key cost drivers are raw materials, packaging, and marketing.

---

### Level 1: Reconceiving Products and Markets

#### Opportunities Identified

| Opportunity | Social Need Addressed | Business Value | Feasibility |
|-------------|----------------------|----------------|-------------|
| Healthier reformulation | Obesity, diet-related disease | Premium pricing, regulatory favor | High |
| Fortified products for underserved markets | Malnutrition in developing markets | New market access | Medium |
| Sustainable packaging | Plastic waste | Brand differentiation, cost reduction | High |

#### Top Opportunity: Healthier Product Reformulation
**Social need:** Obesity and diet-related disease affecting billions globally
**Business case:**
- Revenue impact: Growing health-conscious consumer segment (15%+ market growth)
- Differentiation: Premium positioning for better-for-you products
- Regulatory advantage: Ahead of potential sugar/sodium taxes
**Implementation considerations:** R&D investment; taste maintenance; reformulation timeline

---

### Level 2: Redefining Productivity in the Value Chain

#### Opportunities Identified

| Value Chain Area | Opportunity | Social Benefit | Cost Reduction |
|------------------|-------------|----------------|----------------|
| Procurement | Sustainable agriculture training | Farmer livelihoods, environment | Yield improvement, supply security |
| Operations | Energy/water efficiency | Environmental impact | 10-20% utility cost reduction |
| Logistics | Distribution optimization | Emissions reduction | Fuel cost reduction |

#### Top Opportunity: Sustainable Agriculture Sourcing
**Social benefit:** Improved farmer livelihoods, environmental sustainability, water conservation
**Business case:**
- Cost reduction: Better agricultural practices improve yields 20-30%, reducing per-unit sourcing costs
- Risk mitigation: Secure supply chains in face of climate volatility
- Quality improvement: Healthier crops produce better ingredients
**Implementation considerations:** Extension service partnerships; certification programs; multi-year investment horizon

---

### Level 3: Enabling Local Cluster Development

#### Opportunities Identified

| Cluster Weakness | Investment Opportunity | Business Benefit | Community Benefit |
|------------------|----------------------|------------------|-------------------|
| Farmer capability | Agricultural extension | Higher quality, reliable supply | Farmer income, food security |
| Rural infrastructure | Cold chain investment | Reduced spoilage | Market access for farmers |
| Skills gaps | Food science training | Talent pipeline | Local employment |

#### Top Opportunity: Agricultural Extension Services
**Cluster weakness addressed:** Smallholder farmers lack access to modern agricultural knowledge and practices
**Business case:**
- Supply chain improvement: Higher quality inputs, more reliable supply
- Cost reduction: Better practices reduce input costs passed through supply chain
- Sustainability claims: Enables authentic marketing of sustainable sourcing
**Implementation considerations:** Partner with NGOs and governments; measure impact on yield and income

---

### Priority Ranking

| Rank | Opportunity | Level | Business Value | Social Value | Feasibility |
|------|-------------|-------|----------------|--------------|-------------|
| 1 | Sustainable agriculture sourcing | 2 | High | High | High |
| 2 | Healthier reformulation | 1 | High | High | High |
| 3 | Agricultural extension services | 3 | Medium | High | Medium |
| 4 | Energy/water efficiency | 2 | Medium | Medium | High |

---

### Recommendations

1. **Immediate action:** Energy and water efficiency in operations — quick wins with clear ROI
2. **Strategic initiative:** Sustainable agriculture sourcing program — requires investment but transforms supply chain
3. **Explore further:** Fortified products for underserved markets — high impact but distribution challenges

---

### Not Shared Value (CSR/Philanthropy)

- Charitable donations to food banks (valuable but not connected to competitive advantage)
- Community grants unrelated to supply chain (good citizenship but not CSV)
- Volunteerism programs (employee engagement but not business value creation)

---

## Integration

This skill is part of the **Michael Porter** expert methodology. Shared value assessment connects to:
- **value-chain-mapping** — Level 2 opportunities emerge from value chain analysis
- **five-forces-industry-analysis** — Shared value can address competitive forces
- **generic-strategy-assessment** — Shared value can support differentiation

**Voice:** Maintain Porter's focus on economic logic. Shared value is not charity—it is a new way to achieve competitive advantage while addressing societal challenges.