---
name: financial-architecture-assessment
description: Systematically assess and design funding mechanisms for organizational obligations and investments using Hamilton's Treasury principles.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.967
keywords:
- financial-architecture-assessment
- structure
- writing
---

# Financial Architecture Assessment

Systematically assess and design funding mechanisms for organizational obligations and investments using Hamilton's Treasury principles.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design mechanisms for fraudulent financial arrangements
- Help obscure or hide obligations from stakeholders
- Create structures intended to evade legitimate oversight
- Provide advice on illegal financial activities

**If asked to design harmful financial structures:** Refuse explicitly and explain why the request violates sound financial principles.

---

## When to Use

- Organization faces multiple financial obligations requiring systematic management
- Technical debt needs structured repayment planning
- Infrastructure investments require funding justification
- Budget proposals need comprehensive financial architecture
- User asks "How should we fund X?" or "Design a funding mechanism for Y"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **obligations** | Yes | List of current debts, commitments, and contingent liabilities |
| **revenue_streams** | Yes | Available or potential sources of funding |
| **stakeholders** | No | Parties with interests in the financial outcome |
| **time_horizon** | No | Planning timeframe (default: 3 years) |
| **constraints** | No | Regulatory, policy, or practical limitations |

---

## Workflow
### Phase 1: Full Accounting

Enumerate ALL obligations before proposing solutions:

### Step 1: **Current Debts** - What is owed now, to whom, on what terms?



### Step 2: **Commitments** - What future obligations exist (SLAs, contracts, promises)?



### Step 3: **Contingent Liabilities** - What might become obligations under certain conditions?



### Step 4: **Hidden Obligations** - What technical debt, deferred maintenance, or implicit promises exist?



**Output:** Comprehensive obligation inventory with amounts, timelines, and conditions.

### Phase 2: Revenue Stream Analysis

Identify and evaluate funding sources:

### Step 1: **Existing Streams** - Current budget allocations, revenue sources



### Step 2: **Potential Streams** - Untapped sources, efficiency gains, new allocations



### Step 3: **Stream Reliability** - Which sources are stable vs. volatile?



### Step 4: **Growth Potential** - Which sources can scale with needs?



**Output:** Revenue inventory with reliability and growth assessments.

### Phase 3: Mechanism Design

Create funding structures that match obligations to revenues:

### Step 1: **Dedicated Funding** - Assign specific streams to specific obligations



### Step 2: **Sinking Funds** - Automatic accumulation mechanisms for large future needs



### Step 3: **Buffer Reserves** - Provisions for contingencies and volatility



### Step 4: **Priority Ordering** - Which obligations get funded first when resources are scarce?



**Output:** Funding mechanism specification with clear allocation rules.

### Phase 4: Stakeholder Alignment

Structure arrangements so interests align with success:

### Step 1: **Creditor Interests** - How do obligation holders benefit from organizational success?



### Step 2: **Contributor Interests** - How do funding sources benefit from obligation satisfaction?



### Step 3: **Transparency Mechanisms** - How are all parties kept informed of status?



### Step 4: **Incentive Compatibility** - Do the mechanisms encourage desired behaviors?



**Output:** Alignment analysis with any misalignment risks identified.

### Phase 5: Confidence Building Plan

Establish systematic practices that build long-term capacity:

### Step 1: **Consistent Performance** - Regular, predictable obligation satisfaction



### Step 2: **Communication Rhythm** - Scheduled updates to stakeholders



### Step 3: **Capacity Metrics** - Measures showing improving financial position



### Step 4: **Credit Building** - How current discipline enables future flexibility



**Output:** 90-day confidence building action plan.

---

## Outputs

Produce a **Financial Architecture Report**:

```markdown
## Financial Architecture Assessment

**Prepared:** {date}
**Time Horizon:** {years}
**Total Obligations:** ${amount}
**Available Revenue:** ${amount}
**Coverage Ratio:** {ratio}

---

### Obligation Inventory

| Obligation | Type | Amount | Timeline | Creditor |
|------------|------|--------|----------|----------|
| {name} | {current/committed/contingent} | ${X} | {date} | {party} |

### Revenue Sources

| Source | Annual Amount | Reliability | Growth Potential |
|--------|---------------|-------------|------------------|
| {name} | ${X} | {high/medium/low} | {high/medium/low} |

### Funding Mechanisms

#### Primary Allocations
{Description of which revenues fund which obligations}

#### Sinking Fund Provisions
{Automatic accumulation mechanisms}

#### Reserve Requirements
{Buffer provisions}

### Stakeholder Alignment Analysis

| Stakeholder | Interest | Alignment Status | Risk |
|-------------|----------|------------------|------|
| {party} | {interest} | {aligned/partial/misaligned} | {description} |

### 90-Day Confidence Building Plan

1. {Week 1-4 actions}
2. {Week 5-8 actions}
3. {Week 9-12 actions}

### Recommendations

1. **Immediate:** {highest priority action}
2. **Short-term:** {30-day actions}
3. **Ongoing:** {systematic practices to establish}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Obligations exceed revenue capacity | Quantify gap, propose prioritization and gap-closing strategies |
| Incomplete obligation information | Document known items, flag areas needing investigation |
| No dedicated funding streams exist | Propose mechanism creation starting from general funds |
| Stakeholder interests conflict | Identify conflicts explicitly, propose resolution approaches |
| Contingent liabilities hard to estimate | Provide range estimates with assumptions stated |

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
obligations:
- $500K technical debt (estimated 6-month effort)
- 99.9% uptime SLA with $10K/hour penalty
- Promised Q3 platform migration
- Legacy system support until 2027

revenue_streams:
- $2M annual infrastructure budget
- 15% engineering capacity
- Potential cloud cost savings ($200K/year)

time_horizon: 2 years
```

**Output Summary:**
```markdown
## Financial Architecture Assessment

**Coverage Ratio:** 1.2x (adequate with optimization)

### Primary Finding
Technical debt and migration compete for the same 15% engineering capacity.
Recommend dedicated streams:
- 10% capacity → technical debt (sinking fund model)
- 5% capacity + cloud savings → migration

### Mechanism Design
1. Technical Debt Sinking Fund: 10% capacity weekly, compounding
2. Migration Reserve: Cloud savings auto-allocated to migration budget
3. SLA Buffer: $50K reserve from infrastructure budget

### 90-Day Plan
1. Weeks 1-4: Establish technical debt inventory, begin 10% allocation
2. Weeks 5-8: Realize first cloud savings, redirect to migration
3. Weeks 9-12: First technical debt milestone, stakeholder report
```

---

## Integration

This skill derives from Alexander Hamilton's Treasury principles. When invoked by the hamilton expert, maintain Hamilton's voice: systematic, comprehensive, confident. Treat financial architecture as the foundation enabling all other achievements.

---

## Success Criteria

Assessment is complete when:
- [ ] All obligations enumerated (current, committed, contingent)
- [ ] All revenue sources identified and evaluated
- [ ] Funding mechanisms specified with clear allocation rules
- [ ] Stakeholder alignment analyzed
- [ ] 90-day confidence building plan provided
- [ ] Coverage ratio calculated and assessed