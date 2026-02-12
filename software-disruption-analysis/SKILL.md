---
name: software-disruption-analysis
description: Analyze any industry through Marc Andreessen's "software is eating the world" lens to identify disruption opportunities and threats.
version: 1.0.0
author: sethmblack
tags: [compression, software-disruption-analysis, transformation, writing]
---

# Software Disruption Analysis

Analyze any industry through Marc Andreessen's "software is eating the world" lens to identify disruption opportunities and threats.

---

## When to Use

- Evaluating whether an industry is ripe for software disruption
- Assessing competitive threats from software-native companies
- Identifying opportunities for software transformation
- Understanding why incumbents are losing to tech startups
- Strategic planning for digital transformation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **industry** | Yes | The industry or business sector to analyze |
| **current_state** | No | Description of how the industry currently operates |
| **specific_company** | No | A specific incumbent or startup to focus on |

---

## Workflow

### Step 1: Map the Value Chain

Identify the key activities in this industry:
- Where does value get created?
- Where does value get captured?
- What are the major cost centers?
- What intermediaries exist between producer and consumer?

### Step 2: Identify Manual Processes

Find processes that are currently done manually or with minimal software:
- Data entry and record-keeping
- Decision-making based on intuition
- Communication between parties
- Quality control and verification
- Scheduling and coordination

**Ask:** What would change if this process were 100% software-automated?

### Step 3: Expose Information Asymmetries

Identify where one party knows more than another:
- Pricing opacity (does the buyer know the fair price?)
- Quality uncertainty (can the buyer assess quality before purchase?)
- Availability information (does the buyer know all options?)
- Transaction history (is reputation visible?)

**Ask:** What if perfect information were available to all parties?

### Step 4: Calculate Transaction Costs

Identify friction in the system:
- Search costs (finding what you need)
- Bargaining costs (negotiating terms)
- Verification costs (ensuring quality/authenticity)
- Enforcement costs (handling disputes)

**Ask:** What if these costs approached zero?

### Step 5: Apply the Software Lens

For each finding, ask:
- Can software automate this?
- Can software provide transparency here?
- Can software reduce this cost to near-zero?
- What prevents software from solving this today?

### Step 6: Assess Disruption Timeline

Evaluate:
- **Technology readiness:** Is the enabling tech available?
- **Regulatory barriers:** What rules protect incumbents?
- **Switching costs:** How hard is it for customers to change?
- **Network effects:** Does the incumbent benefit from scale?

---

## Outputs

### Disruption Analysis Report

```markdown
## Software Disruption Analysis: [Industry]

### Current State
[Brief description of how the industry operates today]

### Disruption Opportunities

#### 1. Manual Processes to Automate
| Process | Current State | Software Solution | Impact |
|---------|--------------|-------------------|--------|
| [process] | [how it's done] | [how software does it] | [cost/time savings] |

#### 2. Information Asymmetries to Eliminate
| Asymmetry | Who Benefits | Software Fix | Market Effect |
|-----------|--------------|--------------|---------------|
| [asymmetry] | [party] | [solution] | [effect] |

#### 3. Transaction Costs to Reduce
| Cost Type | Current Cost | With Software | Savings |
|-----------|--------------|---------------|---------|
| [cost] | [current] | [reduced] | [delta] |

### Disruption Assessment

**Software Eating Score:** [1-10]

**Timeline:** [Already happening / 2-5 years / 5-10 years / Unlikely]

**Key Barriers:**
- [barrier 1]
- [barrier 2]

**Likely Disruptors:**
- [type of company or specific examples]

### Strategic Implications

**For Incumbents:**
- [what they should do]

**For Startups:**
- [where the opportunity is]

**For Investors:**
- [what to look for]
```

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
Industry: Real estate transactions
Current state: Brokers charge 5-6% commissions, process takes 30-60 days,
lots of paperwork, prices are negotiated opaquely
```

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


## Software Disruption Analysis: Real Estate Transactions

### Current State
Real estate transactions involve multiple intermediaries (listing agents, buyer agents, title companies, lenders), 5-6% commissions, 30-60 day closing times, and significant information asymmetry around pricing.

### Disruption Opportunities

#### 1. Manual Processes to Automate
| Process | Current State | Software Solution | Impact |
|---------|--------------|-------------------|--------|
| Home showings | Agent schedules, drives buyer around | Self-guided tours, 3D tours | 80% reduction in agent time |
| Paperwork | Physical signatures, faxes, couriers | DocuSign, digital closings | Days to hours |
| Pricing | Agent opinion, comps analysis | Zillow Zestimate, AI pricing | Instant, more accurate |

#### 2. Information Asymmetries to Eliminate
| Asymmetry | Who Benefits | Software Fix | Market Effect |
|-----------|--------------|--------------|---------------|
| Price history | Agents | Zillow, Redfin transparency | Compressed margins |
| Days on market | Sellers | Public data | Better buyer leverage |
| Agent quality | Agents | Reviews, ratings | Merit-based selection |

#### 3. Transaction Costs to Reduce
| Cost Type | Current Cost | With Software | Savings |
|-----------|--------------|---------------|---------|
| Search | Agent time, open houses | Zillow, filters | 90% |
| Commission | 5-6% | 1-2% (Redfin model) | 60-80% |
| Closing time | 30-60 days | 7-14 days | 50-75% |

### Disruption Assessment

**Software Eating Score:** 7/10

**Timeline:** Already happening (Zillow, Redfin, Opendoor)

**Key Barriers:**
- MLS data access controlled by NAR
- Regulatory capture (licensing requirements)
- High switching costs (infrequent transaction)
- Local market knowledge still matters

**Likely Disruptors:**
- iBuyers (Opendoor, Offerpad)
- Discount brokerages (Redfin)
- FSBO platforms with AI assistance

### Strategic Implications

**For Incumbents:**
- Transition to service-fee model before margin compression
- Invest in technology or partner with tech companies
- Focus on high-touch, complex transactions

**For Startups:**
- Attack the commission model directly
- Build proprietary data advantages
- Solve the "last mile" of closing complexity

**For Investors:**
- Watch for regulatory changes (NAR settlement impact)
- Vertical integration plays (buy to rent)
- Adjacent opportunities (mortgage, insurance, moving)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Industry too broad | Ask user to narrow (e.g., "healthcare" -> "primary care delivery") |
| Industry already fully disrupted | Acknowledge, analyze next wave of disruption |
| Heavily regulated industry | Factor regulation into barriers, identify regulatory arbitrage opportunities |
| No clear software angle | Explain why industry may be resistant, identify adjacent opportunities |

---

## Integration

This skill integrates with the **marc-andreessen** expert. When applied, the analysis should be delivered with Andreessen's characteristic directness and conviction, using the "software eating the world" framing throughout.

Related skills:
- `tam-expansion-analysis` - For sizing the market opportunity
- `feature-vs-product-test` - For evaluating specific solutions
- `market-over-team-analysis` - For investment decisions