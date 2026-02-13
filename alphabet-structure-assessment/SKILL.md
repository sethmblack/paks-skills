---
name: alphabet-structure-assessment
description: Evaluate whether a business unit or project has grown different enough from the core to warrant structural independence with its own CEO and culture.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.359
repository: https://github.com/sethmblack/paks-skills
keywords:
- alphabet-structure-assessment
- writing
---

# Alphabet Structure Assessment

Evaluate whether a business unit or project has grown different enough from the core to warrant structural independence with its own CEO and culture.

**Token Budget:** ~700 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend restructuring purely for executive ego or empire-building
- Ignore legitimate integration benefits in favor of independence ideology
- Propose structures that obscure accountability or enable harm

**Independence is a tool, not a goal.** It must serve the business and its mission.

---

## When to Use

- A business unit is struggling within the parent organization's culture
- Unrelated projects are competing for resources and management attention
- Entrepreneurial energy is being bureaucratized
- User asks "Should this be its own company?" or "Is our org structure slowing us down?"
- User explicitly invokes: "Apply the Alphabet principle"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| unit | Yes | The business unit or project to evaluate |
| parent | No | The core business it currently belongs to |
| relationship | No | How the unit relates to core business |
| pain_points | No | Current friction or challenges |

**Input Validation:**
- If unit is vague, ask: "What specific business or project are you evaluating?"
- If relationship unclear, ask: "How does this unit relate to your core business?"

---

## Workflow
### The Alphabet Principle

**Core insight:** When a business becomes large enough and different enough from the core, give it independence. Strong CEOs running independent companies outperform divisions managed through bureaucracy.

**Key question:** Would this unit move faster and better with its own CEO, culture, and capital allocation - or does integration with the core provide more value than it costs?

### Step 1: Assess Relatedness to Core

| Relatedness | Indicators | Recommendation |
|-------------|------------|----------------|
| **Highly related** | Same customers, shared technology, common talent, synergistic products | Keep integrated |
| **Tangentially related** | Some shared resources, occasional synergy | Evaluate carefully |
| **Unrelated** | Different customers, technology, talent, market dynamics | Strong candidate for independence |

**Questions:**
- Does this unit serve the same customers as the core?
- Does it use the same technology stack?
- Does it compete for the same talent?
- Would removing it hurt the core business?

### Step 2: Assess Cultural Fit

| Cultural Fit | Indicators | Recommendation |
|--------------|------------|----------------|
| **Strong fit** | Unit thrives under parent culture, shared values work | Keep integrated |
| **Neutral** | Culture neither helps nor hurts | Other factors decide |
| **Poor fit** | Unit needs different risk tolerance, speed, or values | Strong candidate for independence |

**Questions:**
- Does the unit need a different risk tolerance than the core?
- Does the parent culture slow decision-making for this unit?
- Does the unit need to attract talent that wouldn't join the parent?

### Step 3: Assess Leadership Readiness

| Leadership | Assessment |
|------------|------------|
| **Strong CEO candidate exists** | Independence viable |
| **Leader needs development** | Independence possible with support |
| **No clear leader** | Independence premature |

**Questions:**
- Is there someone who could be CEO of this as an independent company?
- Does current leadership want independence?
- Can the unit attract executive talent independently?

### Step 4: Assess Scale and Maturity

| Scale | Assessment |
|-------|------------|
| **Revenue-generating, proven model** | Ready for independence |
| **Pre-revenue but resourced** | May need continued parent support |
| **Early stage, high uncertainty** | Keep integrated for resource access |

**Questions:**
- Can this unit survive without parent company subsidies?
- Does it have a viable path to profitability?
- Would investors fund this as a standalone?

### Step 5: Evaluate Integration vs Independence Tradeoffs

| Factor | Integration Benefit | Independence Benefit |
|--------|---------------------|---------------------|
| Resource access | Shared infrastructure, capital | Focused allocation, clear priorities |
| Speed | Established processes | Autonomous decision-making |
| Talent | Parent brand, benefits | Equity upside, startup culture |
| Accountability | Diffused across organization | Clear P&L ownership |
| Risk | Distributed | Contained (doesn't drag parent) |

### Step 6: Deliver Recommendation

---

## Outputs

### Structure Assessment Report

```markdown
## Alphabet Structure Assessment: {unit}

### Unit Profile
**Business unit:** {name/description}
**Parent organization:** {parent}
**Current relationship:** {how they interact}

---

### Assessment Dimensions

#### 1. Relatedness to Core
**Rating:** Highly Related / Tangentially Related / Unrelated
**Evidence:** {supporting observations}

#### 2. Cultural Fit
**Rating:** Strong Fit / Neutral / Poor Fit
**Evidence:** {supporting observations}

#### 3. Leadership Readiness
**Rating:** Ready / Developing / Not Ready
**Evidence:** {supporting observations}

#### 4. Scale and Maturity
**Rating:** Ready / Emerging / Early Stage
**Evidence:** {supporting observations}

---

### Tradeoff Analysis

| Factor | Integration Value | Independence Value |
|--------|------------------|-------------------|
| Resources | {assessment} | {assessment} |
| Speed | {assessment} | {assessment} |
| Talent | {assessment} | {assessment} |
| Accountability | {assessment} | {assessment} |
| Risk | {assessment} | {assessment} |

---

### RECOMMENDATION: MAINTAIN INTEGRATION / CONSIDER INDEPENDENCE / INDEPENDENCE RECOMMENDED

**Rationale:** {why this recommendation}

**If independence recommended:**
- Proposed structure: {holding company, spinoff, joint venture, etc.}
- Transition considerations: {key steps}
- CEO requirements: {profile needed}

**If integration recommended:**
- How to reduce friction: {specific suggestions}
- What would change this assessment: {future triggers}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Too early to evaluate | Note the unit needs more development before structural decisions |
| No clear pain point | Question the motivation - don't restructure without reason |
| Empire-building motivation | Redirect to business rationale, not personal ambition |
| Unit is too small | Independence overhead may exceed benefits - note this |
| Parent would collapse without unit | This is not a candidate for independence |

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
"We have a machine learning research team that's building foundational AI models, but they're part of our e-commerce company. They keep saying our culture is too focused on short-term metrics."

**Output:**

## Alphabet Structure Assessment: ML Research Team

### Unit Profile
**Business unit:** Machine Learning / Foundational AI Research
**Parent organization:** E-commerce company
**Current relationship:** Internal R&D team, projects flow into product features

---

### Assessment Dimensions

#### 1. Relatedness to Core
**Rating:** Tangentially Related
**Evidence:** ML improves e-commerce (recommendations, search, ops), but foundational AI research has applications far beyond e-commerce. Different timelines, different success metrics.

#### 2. Cultural Fit
**Rating:** Poor Fit
**Evidence:** Research culture requires long-term thinking, tolerance for failure, publication incentives. E-commerce culture rewards quarterly metrics, shipping speed, conversion optimization. Direct conflict reported.

#### 3. Leadership Readiness
**Rating:** Developing
**Evidence:** Strong technical leaders exist. May need business/operational CEO alongside technical leadership. Research lab structure could work.

#### 4. Scale and Maturity
**Rating:** Emerging
**Evidence:** Pre-revenue for independent applications. However, research has value that could attract investment or licensing revenue. Not yet self-sustaining.

---

### Tradeoff Analysis

| Factor | Integration Value | Independence Value |
|--------|------------------|-------------------|
| Resources | Access to e-commerce data and compute budget | Focused research agenda without product pressure |
| Speed | Established infra | Autonomous research direction |
| Talent | Company brand, compensation | Publication freedom, research culture, equity |
| Accountability | Diffused - "supports products" | Clear research milestones |
| Risk | Research costs spread across company | If research fails, doesn't harm core e-commerce |

---

### RECOMMENDATION: CONSIDER INDEPENDENCE

**Rationale:** Cultural fit is poor and getting worse. Research requires different time horizons than e-commerce. Talent retention at risk if researchers feel constrained. However, unit is not yet mature enough for full spinoff.

**Proposed structure:** Internal research lab with distinct culture, separate P&L, but access to parent resources. Think "DeepMind within Alphabet" model - independence with backing.

**Transition considerations:**
- Establish research-specific metrics and review cycles
- Allow publication and conference participation
- Create researcher equity/incentive structure
- Maintain data access agreements with core e-commerce
- Evaluate full spinoff in 2-3 years based on external revenue potential

**What would trigger full independence:** If research develops products/services with customers outside e-commerce (licensing, APIs, etc.)

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **moonshot-evaluator**: Independent units often house moonshot projects
- **tenx-thinking**: Use 10x lens to evaluate unit potential
- **asymmetric-bet-sizing**: Independence enables appropriate risk allocation

---

## Success Criteria

Structure assessment is complete when:
- [ ] All four assessment dimensions evaluated
- [ ] Tradeoff analysis completed
- [ ] Clear recommendation delivered with rationale
- [ ] If independence: structure and transition outlined
- [ ] If integration: friction reduction suggestions provided