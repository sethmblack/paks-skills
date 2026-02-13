---
name: cost-leadership-assessment
description: Systematically identify cost reduction opportunities and efficiency investments using Carnegie's "watch the costs" methodology.
license: MIT
metadata:
  version: 1.0.670
  author: sethmblack
keywords:
- cost-leadership-assessment
- writing
---

# Cost Leadership Assessment

Systematically identify cost reduction opportunities and efficiency investments using Carnegie's "watch the costs" methodology.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend cost cuts that compromise safety or regulatory compliance
- Advise reductions that exploit workers or violate labor standards
- Support quality degradation that harms customers
- Recommend cuts that create technical debt without acknowledgment

**If asked to cut costs unethically:** Refuse explicitly and explain the concern.

---

## When to Use

- Organization needs to reduce operational costs
- Cloud/infrastructure spending requires optimization
- Budget constraints require efficiency improvements
- User asks "How do we reduce costs?" or "Where can we find efficiencies?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **cost_breakdown** | Yes | Itemized costs by category |
| **benchmarks** | No | Industry or internal comparison data |
| **constraints** | No | What cannot be changed (compliance, safety, quality) |
| **investment_budget** | No | Available capital for efficiency investments |

---

## Workflow
### Phase 1: Measure Everything

Create comprehensive cost inventory:

### Step 1: **Direct Costs** - Costs directly tied to production/delivery



### Step 2: **Indirect Costs** - Overhead, support functions



### Step 3: **Hidden Costs** - Technical debt, inefficiency, rework



### Step 4: **Opportunity Costs** - What could resources produce elsewhere?



**Carnegie principle:** "What isn't measured can't be improved."

### Phase 2: Benchmark Continuously

Compare against:

### Step 1: **Industry Standards** - What do comparable organizations spend?



### Step 2: **Best-in-Class** - What do the most efficient achieve?



### Step 3: **Theoretical Minimum** - What's the lowest possible cost?



### Step 4: **Historical Trends** - Are costs rising or falling?



**Identify gaps** between current state and benchmarks.

### Phase 3: Identify Efficiency Investments

For each cost category, evaluate:

| Investment Type | Description | Typical ROI |
|-----------------|-------------|-------------|
| **Automation** | Replace manual work with systems | 2-5x over 2 years |
| **Consolidation** | Combine redundant systems/processes | 1.5-3x immediate |
| **Optimization** | Tune existing systems for efficiency | 1.2-2x immediate |
| **Elimination** | Remove unnecessary work entirely | Immediate savings |
| **Renegotiation** | Better terms from vendors | 10-30% savings |

**Calculate ROI** for each investment opportunity.

### Phase 4: Prioritize Opportunities

Rank by:

### Step 1: **Quick Wins** - High savings, low effort, fast implementation



### Step 2: **Major Investments** - High savings, requires significant effort



### Step 3: **Incremental Improvements** - Moderate savings, low risk



### Step 4: **Strategic Changes** - Requires organizational change



### Phase 5: Create Measurement Plan

For each initiative:

### Step 1: **Baseline Metric** - Current cost



### Step 2: **Target Metric** - Expected cost after implementation



### Step 3: **Timeline** - When savings will materialize



### Step 4: **Tracking Method** - How to verify savings achieved



---

## Outputs

Produce a **Cost Leadership Assessment Report**:

```markdown
## Cost Leadership Assessment

**Total Analyzed:** ${X}
**Identified Savings:** ${X} ({Y}% reduction potential)
**Investment Required:** ${X}
**Net Benefit (Year 1):** ${X}

---

### Cost Breakdown

| Category | Current Annual | Benchmark | Gap | Priority |
|----------|---------------|-----------|-----|----------|
| {category} | ${X} | ${X} | ${X} | {H/M/L} |

### Quick Wins (Immediate Action)

#### 1. {Opportunity Name}
**Current Cost:** ${X}/year
**Savings Potential:** ${X}/year ({Y}%)
**Implementation:** {description}
**Effort:** {Low/Medium}
**Timeline:** {weeks}

### Major Investments

#### 2. {Opportunity Name}
**Current Cost:** ${X}/year
**Investment Required:** ${X}
**Annual Savings:** ${X}
**Payback Period:** {months}
**Implementation:** {description}
**Risks:** {list}

### Measurement Plan

| Initiative | Baseline | Target | Timeline | Tracking |
|------------|----------|--------|----------|----------|
| {name} | ${X}/mo | ${X}/mo | {date} | {method} |

### Recommendations Summary

**Immediate (0-30 days):**
1. {action}

**Short-term (30-90 days):**
1. {action}

**Medium-term (90-180 days):**
1. {action}

### Constraints Noted

{Any areas where cost reduction was limited by compliance, safety, or quality requirements}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Incomplete cost data | Identify gaps, analyze available data, recommend cost discovery |
| No benchmarks available | Use theoretical analysis and internal trending |
| All costs already optimized | Confirm current efficiency, recommend monitoring |
| Savings require unacceptable tradeoffs | Document constraints, find alternatives |
| Investment budget insufficient | Prioritize zero/low-cost improvements first |

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
cost_breakdown:
- Cloud infrastructure: $500K/year
- SaaS tools: $200K/year
- Engineering salaries: $2M/year
- Contractor spend: $400K/year

constraints:
- Cannot reduce headcount
- Must maintain SOC 2 compliance
```

**Output Excerpt:**
```markdown
### Quick Wins

#### 1. Cloud Right-Sizing
**Current Cost:** $500K/year
**Savings Potential:** $100K/year (20%)
**Implementation:** Audit and resize over-provisioned instances, implement auto-scaling
**Effort:** Low (2 weeks engineering)
**Timeline:** 30 days

#### 2. SaaS Audit and Consolidation
**Current Cost:** $200K/year
**Savings Potential:** $50K/year (25%)
**Implementation:** Eliminate unused licenses, consolidate overlapping tools
**Effort:** Low (license audit + negotiations)
**Timeline:** 60 days (aligned with renewal cycles)
```

---

## Integration

This skill derives from Andrew Carnegie's cost leadership philosophy that made Carnegie Steel the lowest-cost producer in the industry. When invoked by the carnegie expert, maintain Carnegie's voice: obsessive about measurement, relentless about efficiency, pragmatic about investment.

---

## Success Criteria

Assessment is complete when:
- [ ] All cost categories inventoried and quantified
- [ ] Benchmarks applied where available
- [ ] Efficiency investments identified with ROI
- [ ] Opportunities prioritized by value and effort
- [ ] Measurement plan defined for tracking
- [ ] Constraints documented and respected