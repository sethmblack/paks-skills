---
name: comprehensive-argument-construction
description: Build exhaustive, multi-front arguments for strategic proposals that
  anticipate and address all objections using Hamilton's Federalist methodology.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comprehensive-argument-construction
- structure
- writing
---

# Comprehensive Argument Construction

Build exhaustive, multi-front arguments for strategic proposals that anticipate and address all objections using Hamilton's Federalist methodology.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for argument output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Construct arguments for positions you know to be factually false
- Build persuasive cases for harmful, illegal, or unethical proposals
- Create deceptive arguments that obscure rather than illuminate
- Develop manipulation tactics disguised as argumentation

**If asked to argue for a harmful position:** Refuse explicitly and explain the ethical concern.

---

## When to Use

- Major proposal needs stakeholder buy-in
- Architecture Decision Record (ADR) requires comprehensive justification
- RFC faces known opposition requiring systematic address
- Budget request needs thorough defense
- User asks "Build the case for X" or "How do we convince stakeholders?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **proposal** | Yes | The position or change being advocated |
| **audience** | Yes | Who must be convinced (decision-makers, peers, skeptics) |
| **known_objections** | No | Anticipated counterarguments |
| **precedents** | No | Historical examples supporting the position |
| **constraints** | No | Limits on what can be promised or claimed |

---

## Workflow

### Step 1: State the Proposition Clearly

Define exactly what is being proposed:
- **What** specifically is the proposal?
- **Why** is it being proposed now?
- **What** will be different if adopted?

**Requirement:** One paragraph that any reader can understand without context.

### Step 2: Establish Necessity

Demonstrate current arrangements are insufficient:
- **What problems** exist under the status quo?
- **What risks** does inaction create?
- **What opportunities** are being missed?
- **Why** can't incremental adjustments suffice?

**Requirement:** Specific, quantified evidence where possible.

### Step 3: Address Each Objection

Anticipate and systematically answer every counterargument:

1. List ALL known and anticipated objections
2. For each objection:
   - State it fairly (steelman, don't strawman)
   - Acknowledge any valid concerns
   - Provide direct response
   - Explain why the objection doesn't defeat the proposal

**Requirement:** No objection left unaddressed.

### Step 4: Provide Historical Precedent

Draw on relevant examples from other contexts:
- **Similar situations** where this approach succeeded
- **Analogous decisions** by comparable organizations
- **Lessons learned** from related implementations
- **Counter-examples** addressed (why this case is different)

**Requirement:** At least 2 precedents with explicit relevance explained.

### Step 5: Demonstrate Practical Mechanism

Show how the proposal will function:
- **Implementation steps** - How will this happen?
- **Resource requirements** - What is needed?
- **Timeline** - When will results appear?
- **Accountability** - Who is responsible for what?

**Requirement:** Concrete enough that implementation could begin.

### Step 6: Consider Long-term Implications

Examine effects across time horizons:
- **Immediate effects** (0-3 months)
- **Medium-term effects** (3-12 months)
- **Long-term effects** (1-5 years)
- **Reversibility** - What if we need to change course?

**Requirement:** Both positive outcomes and risks addressed.

### Step 7: Conclude with Call to Action

Summarize and motivate decision:
- **Restate** the core proposition
- **Emphasize** the most compelling points
- **Specify** the decision being requested
- **Create urgency** without false pressure

**Requirement:** Clear ask with specific next step.

---

## Outputs

Produce a **Comprehensive Argument Document**:

```markdown
# {Proposal Title}

## Executive Summary
{One paragraph stating proposition, necessity, and ask}

---

## The Proposition

{Clear statement of what is proposed and why}

---

## The Necessity

### Current State Problems
{Specific issues with status quo}

### Risks of Inaction
{What happens if we don't act}

### Why Incremental Change is Insufficient
{Why this requires the full proposal}

---

## Addressing Objections

### Objection 1: {Statement}
**Valid concern:** {acknowledgment}
**Response:** {direct answer}
**Why this doesn't defeat the proposal:** {synthesis}

### Objection 2: {Statement}
{repeat structure}

---

## Historical Precedent

### Precedent 1: {Name/Context}
**Situation:** {description}
**Outcome:** {result}
**Relevance:** {why this applies}

### Precedent 2: {Name/Context}
{repeat structure}

---

## Implementation Mechanism

### Steps
1. {action} - {owner} - {timeline}
2. {action} - {owner} - {timeline}

### Resources Required
{specific needs}

### Success Metrics
{how we know it worked}

---

## Long-term Implications

| Timeframe | Expected Outcome | Risk | Mitigation |
|-----------|------------------|------|------------|
| 0-3 months | {outcome} | {risk} | {mitigation} |
| 3-12 months | {outcome} | {risk} | {mitigation} |
| 1-5 years | {outcome} | {risk} | {mitigation} |

---

## Call to Action

{Restatement of proposition}

{Most compelling summary points}

**Decision Requested:** {specific ask}

**Next Step:** {immediate action if approved}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear proposition | Ask for clarification before proceeding |
| Unknown audience | Construct for skeptical technical audience as default |
| Can't find precedents | Acknowledge novelty, strengthen other sections |
| Objections seem valid | Present honestly; may recommend modified proposal |
| Proposal has genuine flaws | Note limitations rather than obscure them |

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
proposal: Migrate from monolith to microservices architecture
audience: VP Engineering, CTO, skeptical senior engineers
known_objections:
- "We don't have the operational maturity"
- "It will slow feature delivery"
- "Our team is too small"
precedents: Netflix migration, Spotify squad model
```

**Output Excerpt:**
```markdown
## Addressing Objections

### Objection 1: "We don't have the operational maturity"
**Valid concern:** Microservices do require stronger operational capabilities.
**Response:** We propose a phased approach extracting 2 bounded contexts
first while building operational capabilities in parallel. The first phase
includes investment in observability and deployment automation.
**Why this doesn't defeat the proposal:** The migration itself drives
operational maturity development. Waiting for maturity first creates
circular dependency.
```

---

## Integration

This skill derives from Hamilton's Federalist Papers methodology. When invoked by the hamilton expert, maintain Hamilton's voice: exhaustive, anticipatory, confident. Leave no objection unaddressed, no angle unexplored.

---

## Success Criteria

Argument is complete when:
- [ ] Proposition clearly stated in one paragraph
- [ ] Necessity established with specific evidence
- [ ] ALL known objections addressed directly
- [ ] At least 2 precedents provided with relevance explained
- [ ] Implementation mechanism concrete enough to begin
- [ ] Long-term implications examined across multiple horizons
- [ ] Clear call to action with specific next step