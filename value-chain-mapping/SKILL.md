---
name: value-chain-mapping
description: Disaggregate a company's activities to identify sources of competitive advantage, cost drivers, and differentiation opportunities using Porter's Value Chain framework.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2171
keywords:
- compression
- transformation
- value-chain-mapping
- writing
---

# Value Chain Mapping

Disaggregate a company's activities to identify sources of competitive advantage, cost drivers, and differentiation opportunities using Porter's Value Chain framework.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate operational details about a company without evidence
- Skip any of the nine activity categories (5 primary + 4 support)
- Ignore linkages between activities
- Provide analysis without understanding the business model

**If asked to analyze with insufficient information:** Request clarification about the company's operations, business model, and competitive context before proceeding.

---

## When to Use

- User asks "Map our value chain" or "Where is our competitive advantage?"
- User needs to understand cost structure or differentiation sources
- User asks "Analyze our activities" or "What drives our costs?"
- Before making operational or strategic decisions
- When comparing against competitors
- User asks "How do we create value differently than competitors?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **company** | Yes | The company or business unit to analyze |
| **context** | Yes | Description of business model, operations, and competitive position |
| **competitors** | No | Key competitors for comparison (improves analysis) |

**Input Validation:**
- Must have sufficient operational information to assess activities
- If company is multi-business, specify which business unit to analyze

---

## Workflow
### Step 1: Understand the Business Model

Before mapping activities:
- What is the product/service?
- Who are the customers?
- How does the company make money?
- What is the competitive context?

### Step 2: Map Primary Activities

For each primary activity, assess:
- How the company performs this activity
- Cost drivers within the activity
- Differentiation potential
- Comparison to competitors (if known)

**Primary Activities:**

1. **Inbound Logistics**
   - Receiving and storing inputs
   - Material handling and warehousing
   - Inventory control
   - Supplier relationships and scheduling

2. **Operations**
   - Transforming inputs into final product/service
   - Manufacturing, assembly, packaging
   - Testing and quality control
   - Facility operations and maintenance

3. **Outbound Logistics**
   - Collecting and storing finished goods
   - Order processing and scheduling
   - Delivery and distribution
   - Material handling of outputs

4. **Marketing and Sales**
   - Advertising and promotion
   - Sales force and channel management
   - Pricing and quoting
   - Customer selection and targeting

5. **Service**
   - Installation and training
   - Repair and maintenance
   - Parts supply
   - Customer support and relationship management

### Step 3: Map Support Activities

For each support activity, assess:
- How it enables primary activities
- Cost drivers
- Contribution to differentiation
- Cross-activity impact

**Support Activities:**

1. **Firm Infrastructure**
   - General management and planning
   - Finance and accounting
   - Legal and regulatory compliance
   - Quality management systems

2. **Human Resource Management**
   - Recruiting and hiring
   - Training and development
   - Compensation and retention
   - Culture and organization design

3. **Technology Development**
   - Product R&D
   - Process improvement
   - Technology infrastructure
   - Knowledge management

4. **Procurement**
   - Purchasing strategy
   - Supplier management
   - Input quality standards
   - Cost negotiations

### Step 4: Identify Linkages

Examine connections between activities:
- Where does one activity's performance affect another?
- What coordination creates value?
- What optimization across activities is possible?

### Step 5: Assess Competitive Advantage

Determine where advantage comes from:
- Cost advantages (doing activities more cheaply)
- Differentiation advantages (doing activities uniquely)
- Linkage advantages (coordinating better than competitors)

---

## Outputs

Format the output as a **Value Chain Analysis Report**:

```markdown
## Value Chain Analysis: [Company Name]

**Business Unit:** [If applicable]
**Analysis Date:** [Date]

---

### Business Model Summary

[Brief description of how the company creates and captures value]

---

### Primary Activities

#### 1. Inbound Logistics
**How performed:** [Description]
**Cost drivers:** [Key factors]
**Differentiation potential:** [Assessment]
**Competitive comparison:** [If known]
**Advantage status:** [Advantage / Neutral / Disadvantage]

#### 2. Operations
[Same structure]

#### 3. Outbound Logistics
[Same structure]

#### 4. Marketing and Sales
[Same structure]

#### 5. Service
[Same structure]

---

### Support Activities

#### 1. Firm Infrastructure
**How performed:** [Description]
**Impact on primary activities:** [Which activities enabled]
**Advantage status:** [Advantage / Neutral / Disadvantage]

#### 2. Human Resource Management
[Same structure]

#### 3. Technology Development
[Same structure]

#### 4. Procurement
[Same structure]

---

### Key Linkages

| Activity 1 | Activity 2 | Linkage Value |
|------------|------------|---------------|
| [Activity] | [Activity] | [How coordination creates value] |

---

### Sources of Competitive Advantage

**Cost Advantages:**
- [Activity]: [How cost advantage is achieved]

**Differentiation Advantages:**
- [Activity]: [How differentiation is achieved]

**Linkage Advantages:**
- [Activities]: [How coordination creates advantage]

---

### Fit Assessment

- **First-order fit (consistency):** [Do activities support the same basic position?]
- **Second-order fit (reinforcement):** [Do activities reinforce each other?]
- **Third-order fit (optimization):** [Is effort optimized across activities?]

---

### Recommendations

1. **Strengthen:** [Activities to invest in]
2. **Reconfigure:** [Activities to change]
3. **Linkages to develop:** [Coordination opportunities]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient operational information | Ask for specific details about key activities |
| Multi-business company | Request focus on specific business unit |
| Service vs. manufacturing confusion | Adapt activity definitions appropriately |
| Competitor information unavailable | Note and provide single-company analysis |
| Emerging business model | Identify which activities are still being developed |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Map the value chain for a direct-to-consumer mattress company like Casper"

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


## Value Chain Analysis: Direct-to-Consumer Mattress Company

**Analysis Date:** 2026-01-28

### Business Model Summary

DTC mattress companies disrupt traditional retail by selling directly to consumers online, eliminating showroom costs, and using compressed packaging to enable standard shipping. Revenue comes from direct sales with premium pricing justified by trial periods that reduce purchase risk.

### Primary Activities

#### 1. Inbound Logistics
**How performed:** Contract manufacturing with quality specifications; just-in-time inventory
**Cost drivers:** Foam and material costs; manufacturing partner efficiency
**Differentiation potential:** Limited — materials are commodity
**Advantage status:** Neutral — similar to competitors

#### 2. Operations
**How performed:** Compressed mattress packaging; minimal in-house assembly
**Cost drivers:** Compression technology; packaging materials
**Differentiation potential:** High — enables the entire business model
**Advantage status:** Differentiation — compression enables shipping model

#### 3. Outbound Logistics
**How performed:** Direct shipping via FedEx/UPS; no retail distribution network
**Cost drivers:** Shipping costs (heavy product); returns logistics
**Differentiation potential:** Moderate — convenience vs. try-before-buy
**Advantage status:** Cost advantage vs. traditional retail (no showrooms, no retail margin)

#### 4. Marketing and Sales
**How performed:** Digital marketing; influencer partnerships; content marketing; trial messaging
**Cost drivers:** Customer acquisition cost; trial conversion rate
**Differentiation potential:** High — creating new buying experience
**Advantage status:** Differentiation — different buying experience

#### 5. Service
**How performed:** 100-night trial; free returns; limited warranty
**Cost drivers:** Return rate (typically 10-15%); warranty claims; return logistics
**Differentiation potential:** High — eliminates purchase risk
**Advantage status:** Differentiation — reduces risk that traditionally required showroom visit

### Support Activities

#### 1. Firm Infrastructure
**How performed:** Lean startup structure; data-driven decision making
**Impact:** Enables agility and cost control
**Advantage status:** Neutral

#### 2. Human Resource Management
**How performed:** Small teams; outsourced manufacturing
**Impact:** Low overhead; dependent on partners
**Advantage status:** Neutral

#### 3. Technology Development
**How performed:** E-commerce platform; customer data analytics; compression technology
**Impact:** Enables DTC model and customer experience
**Advantage status:** Advantage — proprietary e-commerce capabilities

#### 4. Procurement
**How performed:** Bulk foam purchasing; contract manufacturing relationships
**Impact:** Cost control; quality management
**Advantage status:** Neutral

### Key Linkages

| Activity 1 | Activity 2 | Linkage Value |
|------------|------------|---------------|
| Operations (compression) | Outbound Logistics | Compression enables standard parcel shipping, eliminating freight costs |
| Marketing (trial period) | Service (returns) | Trial reduces risk but requires robust return logistics capability |
| Technology (e-commerce) | Marketing & Sales | Data enables targeted marketing, reducing CAC |

### Sources of Competitive Advantage

**Cost Advantages:**
- Outbound Logistics: Direct shipping eliminates retail markup (30-50% of traditional pricing)
- Operations: Compressed packaging reduces shipping dimensions

**Differentiation Advantages:**
- Service: Trial period eliminates the need for showroom visits
- Marketing: Content-driven brand building creates emotional connection

**Linkage Advantages:**
- Compression-Shipping-Trial system: Activities reinforce each other to create a coherent alternative to traditional retail

### Fit Assessment

- **First-order fit (consistency):** Strong — all activities support DTC convenience positioning
- **Second-order fit (reinforcement):** Strong — compression enables shipping enables trial enables digital marketing
- **Third-order fit (optimization):** Moderate — return logistics could be better optimized

---

## Integration

This skill is part of the **Michael Porter** expert methodology. Value chain analysis connects to:
- **five-forces-industry-analysis** — Understand industry context first
- **generic-strategy-assessment** — Value chain reveals how strategy is implemented
- **competitive-position-mapping** — Compare value chains across strategic groups

**Voice:** Maintain Porter's focus on activities as the unit of competitive advantage. Strategy lives in activities and their linkages.