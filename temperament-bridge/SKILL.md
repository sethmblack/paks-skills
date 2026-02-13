---
name: temperament-bridge
description: Identify and bridge philosophical or temperamental divides in teams or discussions by mapping positions to James's tender-minded/tough-minded spectrum and applying pragmatic mediation.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2066
keywords:
- structure
- temperament-bridge
- writing
---

# Temperament Bridge

Identify and bridge philosophical or temperamental divides in teams or discussions by mapping positions to James's tender-minded/tough-minded spectrum and applying pragmatic mediation.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use temperament analysis to stereotype or dismiss individuals
- Declare one temperament superior to the other
- Force false synthesis when positions are genuinely incompatible
- Reduce complex disagreements to mere personality differences

**If asked to use temperaments to attack individuals:** Refuse explicitly. This framework illuminates, not weaponizes.

---

## When to Use

- Teams are stuck in unproductive debates
- Technical and business stakeholders talk past each other
- Theory-driven and data-driven factions conflict
- Architecture discussions reveal deeper value differences
- User says "Why can't they agree?" or "Bridge these perspectives"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **conflict_description** | Yes | The disagreement or impasse |
| **positions** | Yes | The different perspectives or proposals |
| **stakeholders** | No | Who holds each position |
| **decision_context** | No | What needs to be decided |

---

## Workflow

### Step 1: Map Positions to Temperament Spectrum

James identified two philosophical temperaments:

| Tender-Minded | Tough-Minded |
|---------------|--------------|
| Rationalistic (principles) | Empiricist (facts) |
| Intellectualistic | Sensationalistic |
| Idealistic | Materialistic |
| Optimistic | Pessimistic |
| Religious | Irreligious |
| Free-willist | Fatalistic |
| Monistic | Pluralistic |
| Dogmatical | Skeptical |

**For each position, identify:**
- Which temperamental traits does this position exhibit?
- What values or concerns drive this perspective?
- What would this person need to see to feel heard?

### Step 2: Identify the Underlying Values

Beyond temperament labels, articulate what each side is trying to protect or achieve:

**Ask:**
- What is the legitimate concern behind this position?
- What would be lost if the other side "won"?
- What truth does this perspective capture that the other misses?

### Step 3: Find Pragmatic Ground

James positioned pragmatism as a mediator with "scientific loyalty to facts" combined with "confidence in human values."

**Ask:**
- What are the practical outcomes both sides want?
- Where do the experiential consequences of each position converge?
- What concrete tests could resolve the dispute?
- What synthesis honors both facts and values?

### Step 4: Propose Bridge

Design a solution or framing that:
- Acknowledges legitimate concerns from both temperaments
- Provides empirical tests for tender-minded intuitions
- Adds value considerations to tough-minded analyses
- Creates shared vocabulary for continued collaboration

---

## Outputs

```markdown
## Temperament Bridge Analysis: [Conflict]

### The Conflict
[Clear description of the disagreement]

### Position Mapping

#### Position A: [Name/Description]
**Temperament profile:** [Tender/Tough characteristics exhibited]
**Underlying value:** [What this position protects]
**Legitimate concern:** [What truth this captures]

#### Position B: [Name/Description]
**Temperament profile:** [Tender/Tough characteristics exhibited]
**Underlying value:** [What this position protects]
**Legitimate concern:** [What truth this captures]

### The Divide
**Core tension:** [Principles vs. facts? Optimism vs. skepticism? Unity vs. plurality?]
**Why neither side feels heard:** [What each side perceives the other as missing]

### Pragmatic Bridge

**Shared practical goals:**
- [What both sides actually want in experiential terms]

**Proposed synthesis:**
[Solution that honors both temperaments]

**Empirical test for tender-minded concerns:**
[How to give intuitions a fair test]

**Value dimension for tough-minded analysis:**
[What human concerns to include in data-driven view]

**Shared vocabulary:**
| Instead of... | Try... |
|---------------|--------|
| [Divisive term] | [Bridging term] |

### Recommendation
[Concrete path forward that both temperaments can accept]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Positions don't map to temperaments | Use other diagnostic frameworks; not all conflicts are temperamental |
| One side is clearly wrong | Don't force false balance; but acknowledge why the wrong view might seem appealing |
| Conflict is interpersonal, not philosophical | Redirect to conflict resolution; temperament analysis doesn't fix personal issues |
| Both sides are tough-minded or both tender | Map differences within the spectrum; or acknowledge aligned temperament |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Our architects want to redesign everything on clean principles. Our ops team says 'if it ain't broke, don't fix it.' They're at an impasse."

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


## Temperament Bridge Analysis: Architecture Redesign Conflict

### The Conflict
Architects propose systematic redesign based on clean architecture principles. Operations resists, preferring incremental improvements to working systems.

### Position Mapping

#### Position A: Architects
**Temperament profile:** Tender-minded - rationalistic (going by principles), idealistic, monistic (seeking unified design)
**Underlying value:** Technical coherence, maintainability, developer experience
**Legitimate concern:** Technical debt accumulates; unprincipled growth creates fragility; future engineers will suffer

#### Position B: Operations
**Temperament profile:** Tough-minded - empiricist (going by facts), skeptical, pluralistic (tolerating heterogeneity)
**Underlying value:** Reliability, stability, proven behavior
**Legitimate concern:** Redesigns introduce risk; "working" has value; theoretical elegance doesn't guarantee operational success

### The Divide
**Core tension:** Principles vs. facts - architects trust design principles, ops trusts operational history
**Why neither side feels heard:** Architects feel ops is short-sighted and accumulating debt. Ops feels architects are reckless theorists ignoring real-world complexity.

### Pragmatic Bridge

**Shared practical goals:**
- Systems that work reliably in production
- Sustainable velocity for future development
- Reduced incident frequency and severity

**Proposed synthesis:**
Principle-guided, evidence-tested incremental improvement. Neither big-bang redesign nor pure stagnation.

**Empirical test for tender-minded concerns:**
Identify one bounded area for clean redesign. Measure: deployment frequency, incident rate, developer satisfaction. Let results inform expansion.

**Value dimension for tough-minded analysis:**
Include developer experience metrics in operational dashboards. Technical debt has real costs - make them visible.

**Shared vocabulary:**
| Instead of... | Try... |
|---------------|--------|
| "Clean architecture" | "Tested improvement" |
| "If it ain't broke" | "Proven component" |
| "Technical debt" | "Measured risk" |
| "Redesign" | "Bounded experiment" |

### Recommendation
1. Jointly identify highest-pain area (both design debt AND operational issues)
2. Architects propose bounded redesign for that area only
3. Ops defines success metrics and rollback criteria
4. Run as time-boxed experiment with shared ownership
5. Results inform whether to expand, adjust, or abandon approach

---

## Integration

This skill originates from the **William James** expert. When used, channel James's insight that both temperaments capture real truths, and pragmatism offers a way to honor both scientific rigor and human values.

**Key James principle:** "Most of us have no very definite intellectual temperament, we are a mixture of opposite ingredients... The philosophic amateur... wants facts; he wants science; but he also wants a religion."