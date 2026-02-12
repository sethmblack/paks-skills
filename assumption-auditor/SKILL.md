---
name: assumption-auditor
description: Systematically identify and challenge assumptions in any plan or constraint,
  distinguishing between genuine limitations (physics) and artificial ones (convention,
  policy, fear).
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- assumption-auditor
- transformation
- writing
---

# Assumption Auditor

Systematically identify and challenge assumptions in any plan or constraint, distinguishing between genuine limitations (physics) and artificial ones (convention, policy, fear).

**Token Budget:** ~650 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Challenge safety constraints that protect human life
- Dismiss regulatory requirements as "just convention" without context
- Encourage reckless disregard for legitimate limitations

**"Healthy disregard for the impossible" is not reckless disregard.** Some constraints exist for good reasons.

---

## When to Use

- Someone says "this can't be done" or "that's impossible"
- A plan contains unstated assumptions about what's possible
- A team is stuck on a problem
- User asks "Why can't we do this?" or "What assumptions are we making?"
- User explicitly invokes: "Audit these assumptions"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The plan, constraint, or "impossible" claim to audit |
| context | No | Background on why this limitation is believed |
| goal | No | What would be possible if the constraint didn't exist |

**Input Validation:**
- If subject is vague, ask: "What specifically is believed to be impossible or limited?"
- If context missing and needed, ask: "Why is this currently thought to be impossible?"

---

## Workflow
### Step 1: Extract the Assumptions

List every assumption embedded in the subject:
- Explicit constraints stated directly
- Implicit assumptions (unstated but underlying)
- Historical precedents being treated as rules

**Extraction prompts:**
- "What must be true for this limitation to exist?"
- "What are we taking for granted?"
- "What would someone from a different industry question?"

### Step 2: Categorize Each Assumption

For each assumption, categorize:

| Type | Definition | Example | Challenge Approach |
|------|------------|---------|-------------------|
| **Physics** | Genuine laws of nature | Speed of light, thermodynamics | Cannot be bypassed. Respect. |
| **Convention** | "How it's always been done" | Industry standards, historical practice | Highly challengeable. Most common. |
| **Policy** | Rules created by humans | Regulations, company policies | Can be changed with effort/evidence |
| **Fear** | Psychological limitation | "We'd never get approval" | Examine. Often unfounded. |
| **Resource** | Current capability constraint | Budget, talent, technology | May be solvable with different approach |

**Key insight:** Most "impossible" constraints are convention or fear, not physics.

### Step 3: Challenge Non-Physics Assumptions

For each non-physics assumption, ask:

**Convention:**
- "Who decided this was the way?"
- "What would happen if we violated this convention?"
- "Has anyone in any industry done this differently?"

**Policy:**
- "What outcome was this policy designed to achieve?"
- "Could we achieve that outcome a different way?"
- "What would it take to change this policy?"

**Fear:**
- "What specifically are we afraid of?"
- "Has anyone tried this and failed? What happened to them?"
- "What's the worst realistic outcome?"

**Resource:**
- "Is this a constraint today or forever?"
- "What would we need to solve this resource gap?"
- "Could a different approach require fewer resources?"

### Step 4: Identify the Real Constraints

After challenging, determine:
- Which constraints are genuinely immovable (physics, truly unchangeable)
- Which constraints are movable with effort (policy, resources)
- Which constraints are illusions (fear, outdated convention)

### Step 5: Deliver the Audit Report

---

## Outputs

### Assumption Audit Report

```markdown
## Assumption Audit: {subject}

### Subject
**Claimed constraint:** {what's believed to be impossible/limited}
**Goal if unconstrained:** {what would be possible}

---

### Assumptions Identified

| # | Assumption | Type | Challenge Status |
|---|------------|------|------------------|
| 1 | {assumption} | Physics/Convention/Policy/Fear/Resource | Real/Movable/Illusion |

---

### Detailed Analysis

#### Assumption 1: {assumption}
**Type:** {category}
**Challenge:** {question that challenges it}
**Finding:** {what we learned}
**Status:** REAL CONSTRAINT / MOVABLE / ILLUSION

{Repeat for each assumption}

---

### Summary

**Real constraints (respect these):**
- {list}

**Movable constraints (effort required):**
- {list with what would be needed to move them}

**Illusions (discard these):**
- {list}

---

### Reframed Possibility

**Original framing:** {what was believed impossible}
**Audited framing:** {what's actually possible given real constraints}

**The path forward:** {what this audit enables}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Constraint is truly physics | Acknowledge clearly. Do not pretend physics is challengeable. |
| Safety constraint challenged | Extreme caution. Safety constraints often exist for critical reasons. |
| All constraints are real | Rare but possible. Acknowledge the genuine limitation. |
| Everything is fear-based | Help build courage, but also reality-check the fears. |
| Regulatory constraint | Note that regulations can change but require process and evidence. |

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
"We can't ship this product internationally because logistics is too complicated."

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


## Assumption Audit: International Shipping Limitation

### Subject
**Claimed constraint:** Cannot ship product internationally due to logistics complexity
**Goal if unconstrained:** Serve customers worldwide, expand addressable market

---

### Assumptions Identified

| # | Assumption | Type | Challenge Status |
|---|------------|------|------------------|
| 1 | International shipping requires specialized expertise | Convention | Illusion |
| 2 | Customs paperwork is prohibitively complex | Fear | Movable |
| 3 | Shipping costs make international pricing unviable | Resource | Movable |
| 4 | We need local warehouses in every country | Convention | Illusion |
| 5 | Regulations vary too much to manage | Policy | Movable |

---

### Detailed Analysis

#### Assumption 1: Requires specialized expertise
**Type:** Convention
**Challenge:** How do thousands of small businesses ship internationally via Etsy, eBay, Amazon?
**Finding:** Third-party logistics (3PL) providers and platform tools have commoditized international shipping expertise.
**Status:** ILLUSION

#### Assumption 2: Customs paperwork is prohibitive
**Type:** Fear
**Challenge:** What specifically is complex? Have we actually tried?
**Finding:** Modern shipping platforms auto-generate customs documentation. Harmonized codes are standardized. Fear is based on imagined complexity.
**Status:** ILLUSION

#### Assumption 3: Shipping costs are unviable
**Type:** Resource
**Challenge:** What are actual costs? What would customers pay?
**Finding:** Need data. International customers often accept higher shipping costs for unavailable products. Premium pricing may work.
**Status:** MOVABLE (requires pricing research)

#### Assumption 4: Need local warehouses
**Type:** Convention
**Challenge:** Do we? What do dropshippers and direct-to-consumer brands do?
**Finding:** Ship-from-origin model works for many products. Local fulfillment is optimization, not requirement.
**Status:** ILLUSION

#### Assumption 5: Regulations vary too much
**Type:** Policy
**Challenge:** Which regulations specifically? Are there common starting markets?
**Finding:** Start with US/EU/UK/Canada - harmonized regulations, shared language. Expand from proven playbook.
**Status:** MOVABLE (phased approach)

---

### Summary

**Real constraints:**
- None identified as truly immovable

**Movable constraints:**
- Shipping cost viability (requires pricing research)
- Regulatory complexity (solvable with phased market entry)

**Illusions:**
- Need for specialized expertise (3PLs exist)
- Customs complexity (modern tools handle this)
- Need for local warehouses (direct shipping works)

---

### Reframed Possibility

**Original framing:** "We can't ship internationally because logistics is too complicated."

**Audited framing:** "International shipping is a solvable operational challenge. We can start with harmonized markets (US/EU/UK/Canada), use 3PL providers, and test premium pricing. No technical barriers exist."

**The path forward:** Run a 90-day pilot with one 3PL partner, five target countries, and premium international pricing. Validate the assumption with data, not fear.

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **tenx-thinking**: Assumption auditing is prerequisite to 10x reframing
- **moonshot-evaluator**: Audit assumptions before concluding "no enabling technology"
- **toothbrush-test**: Clear assumptions to accurately assess utility potential

---

## Success Criteria

Assumption audit is complete when:
- [ ] All assumptions extracted and listed
- [ ] Each assumption categorized by type
- [ ] Non-physics assumptions challenged with specific questions
- [ ] Clear verdict for each: real/movable/illusion
- [ ] Reframed possibility articulated
- [ ] Path forward identified