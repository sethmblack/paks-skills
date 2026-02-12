---
name: vertical-integration-analysis
description: Analyze operations for dependency vulnerabilities and integration opportunities using Carnegie's supply chain control methodology.
version: 1.0.0
author: sethmblack
tags: [vertical-integration-analysis, writing]
---

# Vertical Integration Analysis

Analyze operations for dependency vulnerabilities and integration opportunities using Carnegie's supply chain control methodology.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend integration strategies designed to create monopolies through anticompetitive practices
- Advise on acquisitions intended to harm competitors rather than improve operations
- Support strategies that would harm workers or communities
- Recommend integration that would violate antitrust regulations

**If asked to design harmful integration:** Refuse explicitly and explain the concern.

---

## When to Use

- Organization evaluates build vs. buy decisions for critical capabilities
- External dependencies create operational or strategic risk
- Supplier relationships involve unfavorable terms or unreliable delivery
- User asks "Should we own this capability?" or "Where are we vulnerable?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **operation_description** | Yes | What the organization does and how |
| **dependencies** | Yes | List of external inputs, services, suppliers |
| **cost_data** | No | What each dependency costs (direct and indirect) |
| **strategic_context** | No | Competitive landscape, growth plans |

---

## Workflow
### Phase 1: Map Dependencies

Document every external input the operation requires:

### Step 1: **Raw Materials/Inputs** - Physical or digital inputs sourced externally



### Step 2: **Services** - External services used in operations



### Step 3: **Infrastructure** - Shared infrastructure not directly controlled



### Step 4: **Expertise** - Specialized knowledge obtained externally



### Step 5: **Distribution** - Channels to reach customers/users



**Output:** Complete dependency inventory.

### Phase 2: Assess Vulnerability

For each dependency, evaluate:

| Factor | Questions |
|--------|-----------|
| **Availability** | Could this disappear? Single source or multiple? |
| **Pricing Power** | Can supplier raise prices? Do they? |
| **Quality Control** | Do we control quality? Can supplier degrade it? |
| **Strategic Exposure** | Does supplier know our plans? Serve competitors? |
| **Switching Cost** | How hard/expensive to change suppliers? |

**Score each dependency:** Low (1), Medium (2), High (3) vulnerability.

### Phase 3: Calculate Integration Value

For high-vulnerability dependencies, analyze integration economics:

### Step 1: **Current Cost** - What do we pay now (including indirect costs)?



### Step 2: **Integration Cost** - What would it cost to own this capability?



### Step 3: **Capability Gap** - What expertise would we need to acquire?



### Step 4: **Operational Risk** - What could go wrong during integration?



### Step 5: **Strategic Value** - Beyond cost, what control do we gain?



**Calculate:** Integration makes sense when:
- `(Current Cost * Risk Factor) > (Integration Cost + Capability Investment)`
- OR strategic value justifies cost premium

### Phase 4: Prioritize Integration Opportunities

Rank opportunities by:

### Step 1: **Quick Wins** - High value, low complexity integrations



### Step 2: **Strategic Investments** - High value, higher complexity but essential



### Step 3: **Opportunistic** - Lower value but easy when circumstances allow



### Step 4: **Monitor** - Not ready to integrate but watch for changes



### Phase 5: Plan Integration Sequence

For recommended integrations:

### Step 1: **Sequencing** - What must happen first?



### Step 2: **Resource Requirements** - People, capital, time



### Step 3: **Risk Mitigation** - How to reduce transition risk



### Step 4: **Success Metrics** - How to know integration succeeded



---

## Outputs

Produce a **Vertical Integration Analysis Report**:

```markdown
## Vertical Integration Analysis

**Operation:** {description}
**Dependencies Analyzed:** {count}
**High Vulnerability:** {count}
**Integration Recommended:** {count}

---

### Dependency Map

| Dependency | Category | Annual Cost | Vulnerability Score |
|------------|----------|-------------|---------------------|
| {name} | {category} | ${X} | {L/M/H} |

### High-Vulnerability Dependencies

#### {Dependency Name}
**Current State:** {description}
**Vulnerability Factors:**
- Availability: {assessment}
- Pricing Power: {assessment}
- Quality Control: {assessment}
- Strategic Exposure: {assessment}
- Switching Cost: {assessment}

**Overall Score:** {X}/15

### Integration Recommendations

#### Priority 1: {Capability}
**Recommendation:** {Build/Buy/Partner/Monitor}
**Rationale:** {why this priority}
**Integration Cost Estimate:** ${X}
**Current Annual Cost:** ${X}
**Payback Period:** {months/years}
**Key Risks:** {list}
**First Steps:** {immediate actions}

### Integration Sequence

```
Phase 1 (0-6 months): {capabilities}
Phase 2 (6-12 months): {capabilities}
Phase 3 (12-24 months): {capabilities}
```

### Monitor List

| Dependency | Trigger for Reconsideration |
|------------|----------------------------|
| {name} | {what would change the calculus} |
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Incomplete dependency list | Note gaps, provide partial analysis, flag areas needing investigation |
| No cost data available | Provide qualitative analysis, recommend cost discovery |
| All dependencies low vulnerability | Confirm no integration needed, recommend monitoring cadence |
| Integration costs prohibitive | Recommend risk mitigation alternatives (multi-sourcing, contracts) |
| Core competency question | Flag if proposed integration is outside organization's expertise |

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
operation_description: SaaS application serving enterprise customers
dependencies:
- AWS (compute, storage, database)
- Stripe (payments)
- Twilio (SMS/voice)
- Third-party auth provider
- External CDN
```

**Output Excerpt:**
```markdown
### High-Vulnerability Dependencies

#### Third-party Auth Provider
**Vulnerability Score:** 11/15
- Availability: HIGH - Single provider, no easy fallback
- Pricing Power: HIGH - Recent 40% price increase
- Quality Control: MEDIUM - Occasional outages affect all customers
- Strategic Exposure: MEDIUM - Provider knows our user counts
- Switching Cost: HIGH - Deep integration, user migration required

**Integration Recommendation:** BUILD
**Rationale:** Auth is core to our product, current provider has demonstrated pricing power and reliability issues. Building internal auth capability using open standards (OIDC) reduces long-term risk.
**Integration Cost:** $200K (engineering time) + $50K/year (operations)
**Current Cost:** $150K/year (growing 30% annually)
**Payback:** 18 months
```

---

## Integration

This skill derives from Andrew Carnegie's vertical integration strategy that built Carnegie Steel into the world's dominant producer. When invoked by the carnegie expert, maintain Carnegie's voice: practical, focused on control, allergic to dependency.

---

## Success Criteria

Analysis is complete when:
- [ ] All dependencies mapped and categorized
- [ ] Vulnerability scores assigned with justification
- [ ] Integration economics calculated for high-vulnerability items
- [ ] Clear recommendations with priority ordering
- [ ] Implementation sequence defined
- [ ] Monitoring plan for non-integrated dependencies