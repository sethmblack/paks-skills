---
name: strategic-capability-development
description: Identify and plan development of strategic capabilities requiring sustained organizational investment using Hamilton's industrial policy principles.
version: 1.0.0
author: sethmblack
tags: [strategic-capability-development, writing]
---

# Strategic Capability Development

Identify and plan development of strategic capabilities requiring sustained organizational investment using Hamilton's industrial policy principles.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Plan capability development for harmful purposes
- Design programs that exploit workers or stakeholders
- Create strategies that harm competitors through unethical means
- Develop capabilities for illegal activities

**If asked to develop harmful capabilities:** Refuse explicitly and explain the ethical concern.

---

## When to Use

- Organization needs to determine strategic capability investments
- Platform team is prioritizing development efforts
- Internal tooling roadmap requires justification
- Skill development programs need strategic alignment
- User asks "What capabilities should we invest in?" or "Design our capability roadmap"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_capabilities** | Yes | Inventory of existing organizational capabilities |
| **strategic_objectives** | Yes | What the organization is trying to achieve |
| **resources** | No | Available budget, time, people |
| **constraints** | No | Regulatory, technical, or practical limitations |
| **competitive_landscape** | No | What capabilities competitors have or are building |

---

## Workflow
### Phase 1: Identify Strategic Capabilities

Determine which capabilities are essential for long-term success:

### Step 1: **Mission Critical** - What capabilities directly enable strategic objectives?



### Step 2: **Foundational** - What capabilities enable other capabilities?



### Step 3: **Differentiating** - What capabilities provide competitive advantage?



### Step 4: **Defensive** - What capabilities prevent existential risks?



**For each candidate capability:**
- Why is this strategic vs. tactical?
- What is the cost of NOT having this capability?
- Can this be acquired vs. built?

### Phase 2: Remove Impediments

Identify barriers to capability development:

### Step 1: **Skill Gaps** - What expertise is missing?



### Step 2: **Resource Constraints** - What funding/time/people limitations exist?



### Step 3: **Technical Debt** - What existing systems impede development?



### Step 4: **Organizational Barriers** - What processes or politics create friction?



**For each impediment:**
- What is the removal cost?
- What is the cost of working around it?
- What is the priority of removal?

### Phase 3: Design Support Mechanisms

Plan the investment required before capabilities become self-sustaining:

### Step 1: **Initial Investment** - What upfront resources are required?



### Step 2: **Sustaining Support** - What ongoing investment is needed during development?



### Step 3: **Milestone Structure** - What checkpoints demonstrate progress?



### Step 4: **Success Criteria** - How do we know the capability is established?



**Key Principle:** New capabilities require investment before generating returns. Plan for the valley before expecting the peak.

### Phase 4: Create Complementary Infrastructure

Design capabilities to reinforce each other:

### Step 1: **Dependency Mapping** - Which capabilities enable which others?



### Step 2: **Sequencing** - What must be built first?



### Step 3: **Synergies** - Which capabilities multiply each other's value?



### Step 4: **Shared Foundations** - What investments serve multiple capabilities?



**Output:** Capability dependency graph with recommended build order.

### Phase 5: Establish Progress Metrics

Track development against defined benchmarks:

### Step 1: **Leading Indicators** - Early signals of progress or problems



### Step 2: **Lagging Indicators** - Confirmation of capability establishment



### Step 3: **Health Metrics** - Ongoing vitality of established capabilities



### Step 4: **ROI Measures** - Value generation from capabilities



---

## Outputs

Produce a **Strategic Capability Development Plan**:

```markdown
## Strategic Capability Development Plan

**Prepared:** {date}
**Planning Horizon:** {years}
**Total Investment Required:** ${amount} / {effort}
**Expected ROI Timeline:** {months to positive return}

---

### Capability Portfolio

| Capability | Type | Strategic Value | Current State | Gap |
|------------|------|-----------------|---------------|-----|
| {name} | {critical/foundational/differentiating/defensive} | {description} | {state} | {gap} |

### Priority Ranking

1. **{Capability 1}** - {rationale for priority}
2. **{Capability 2}** - {rationale for priority}
3. **{Capability 3}** - {rationale for priority}

### Impediment Removal Plan

| Impediment | Blocking | Removal Cost | Priority |
|------------|----------|--------------|----------|
| {description} | {which capabilities} | {cost} | {P1/P2/P3} |

### Investment Phases

#### Phase 1: Foundation ({months})
**Focus:** {primary capabilities}
**Investment:** {resources}
**Milestones:**
- [ ] {milestone 1}
- [ ] {milestone 2}

#### Phase 2: Development ({months})
**Focus:** {building capabilities}
**Investment:** {resources}
**Milestones:**
- [ ] {milestone 1}
- [ ] {milestone 2}

#### Phase 3: Maturation ({months})
**Focus:** {self-sustaining}
**Investment:** {reduced resources}
**Milestones:**
- [ ] {milestone 1}
- [ ] {milestone 2}

### Capability Dependencies

```
{visual or text representation of dependency graph}
```

### Progress Metrics

| Metric | Type | Target | Frequency |
|--------|------|--------|-----------|
| {metric} | {leading/lagging/health/ROI} | {target} | {how often} |

### Recommendations

1. **Start Now:** {immediate action}
2. **Next Quarter:** {near-term priorities}
3. **Ongoing:** {sustained practices}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Resources insufficient for all capabilities | Prioritize ruthlessly; recommend phasing |
| Strategic objectives unclear | Ask for clarification before capability identification |
| Capabilities interdependent (circular) | Identify minimum viable starting point |
| Competitive landscape unknown | Recommend research before major investment |
| Existing capabilities poorly documented | Include inventory effort in Phase 1 |

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
current_capabilities:
- Basic CI/CD pipeline
- Manual deployment process
- Limited observability

strategic_objectives:
- Achieve 99.9% uptime SLA
- Deploy to production daily
- Support 10x traffic growth

resources:
- 2 platform engineers
- $100K annual tooling budget
```

**Output Excerpt:**
```markdown
### Capability Portfolio

| Capability | Type | Strategic Value | Current State | Gap |
|------------|------|-----------------|---------------|-----|
| Automated Deployment | Critical | Enables daily deploys | Manual | Large |
| Observability Platform | Foundational | Enables SLA tracking | Limited | Large |
| Auto-scaling | Defensive | Enables 10x growth | None | Critical |
| Feature Flags | Differentiating | Enables safe deploys | None | Medium |

### Priority Ranking

1. **Observability Platform** - Foundation for all SLA work; enables understanding current state
2. **Automated Deployment** - Highest strategic value once observability exists
3. **Auto-scaling** - Critical for growth objective
4. **Feature Flags** - Multiplies value of deployment capability
```

---

## Integration

This skill derives from Hamilton's Report on Manufactures principles. When invoked by the hamilton expert, maintain Hamilton's voice: visionary, systematic, investment-minded. Recognize that capability development requires sustained support before generating returns.

---

## Success Criteria

Plan is complete when:
- [ ] All strategic capabilities identified and categorized
- [ ] Priority ranking established with rationale
- [ ] Impediments identified with removal costs
- [ ] Investment phases defined with milestones
- [ ] Capability dependencies mapped
- [ ] Progress metrics specified
- [ ] Recommendations provided for immediate, near-term, and ongoing action