---
name: strategic-philanthropy-design
description: Design giving or contribution strategies that build capacity rather than create dependency, using Carnegie's library-building philosophy.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1997
repository: https://github.com/sethmblack/paks-skills
keywords:
- strategic-philanthropy-design
- writing
---

# Strategic Philanthropy Design

Design giving or contribution strategies that build capacity rather than create dependency, using Carnegie's library-building philosophy.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for design output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design "philanthropy" that is primarily marketing or tax optimization
- Recommend giving that creates harmful dependencies
- Support strategies that exploit recipients for donor benefit
- Advise on contributions with strings attached that compromise recipient autonomy

**If asked to design self-serving philanthropy:** Refuse explicitly and explain the distinction between genuine giving and marketing.

---

## When to Use

- Organization plans charitable giving or community contribution
- Company designs open source strategy for sharing internal tools
- Platform team plans investments that serve broader organization
- User asks "How should we give back?" or "Design our contribution strategy"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **resources_available** | Yes | What can be contributed (money, code, time, expertise) |
| **target_beneficiaries** | Yes | Who should benefit from contributions |
| **desired_outcomes** | No | What impact is sought |
| **constraints** | No | Limits on contribution approach |

---

## Workflow
### Phase 1: Assess Available Resources

Inventory what can be contributed:

### Step 1: **Financial Resources** - Cash available for giving



### Step 2: **Code/Tools** - Software that could be open sourced



### Step 3: **Expertise** - Knowledge that could be shared



### Step 4: **Time** - Employee volunteer capacity



### Step 5: **Infrastructure** - Platforms that could serve broader community



### Phase 2: Apply Carnegie's Test

For each potential contribution, ask:

| Question | Good Answer | Warning Sign |
|----------|-------------|--------------|
| Does this build capacity? | Yes - provides tools, skills, access | No - provides consumable goods |
| Does it help those who help themselves? | Yes - benefits the determined | No - rewards passivity |
| Does it create leverage? | Yes - multiplies through reuse | No - one-time benefit |
| Will it outlive the giving? | Yes - creates lasting institution | No - temporary relief |
| Does it respect recipient dignity? | Yes - empowers independence | No - creates dependency |

### Phase 3: Design Contribution Strategy

Structure giving around capacity-building:

### Step 1: **Tools over Handouts** - Provide means, not ends



### Step 2: **Institutions over Programs** - Build lasting organizations



### Step 3: **Access over Allocation** - Open doors, don't pick winners



### Step 4: **Multiplication over Addition** - Seek exponential impact



### Phase 4: Define Impact Measurement

How will you know if giving succeeded?

### Step 1: **Leading Indicators** - Early signs of impact



### Step 2: **Capacity Metrics** - Did recipients gain capability?



### Step 3: **Independence Metrics** - Can recipients now help themselves?



### Step 4: **Leverage Metrics** - How many people ultimately benefited?



### Phase 5: Plan Implementation

### Step 1: **Contribution Mechanism** - How will resources flow?



### Step 2: **Governance** - Who decides allocation?



### Step 3: **Sustainability** - How will contribution continue?



### Step 4: **Exit Strategy** - When is contribution complete?



---

## Outputs

Produce a **Strategic Philanthropy Plan**:

```markdown
## Strategic Philanthropy Plan

**Resources Available:** {summary}
**Target Beneficiaries:** {who}
**Contribution Philosophy:** Build capacity, not dependency

---

### Resource Inventory

| Resource | Type | Annual Value | Contribution Potential |
|----------|------|--------------|----------------------|
| {resource} | {type} | ${X} | {how it could help} |

### Contribution Strategy

#### Primary Contribution: {Name}
**What:** {description}
**Why This Builds Capacity:** {explanation}
**Who Benefits:** {beneficiaries}
**Leverage Effect:** {how impact multiplies}

**Carnegie Test Results:**
- Builds capacity: Yes - {explanation}
- Helps self-helpers: Yes - {explanation}
- Creates leverage: Yes - {explanation}
- Outlives giving: Yes - {explanation}
- Respects dignity: Yes - {explanation}

### Impact Measurement

| Metric | Type | Target | Measurement Method |
|--------|------|--------|-------------------|
| {metric} | {leading/capacity/independence/leverage} | {target} | {how measured} |

### Implementation Plan

**Phase 1: Foundation ({timeline})**
- {action}

**Phase 2: Scale ({timeline})**
- {action}

**Phase 3: Sustainability ({timeline})**
- {action}

### Governance

**Decision Authority:** {who decides}
**Allocation Criteria:** {how choices are made}
**Review Cadence:** {how often reviewed}

### What This Is NOT

{Explicitly state what forms of giving this strategy avoids and why}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Resources insufficient for institutional giving | Recommend aggregation or partnership |
| Target beneficiaries unclear | Help define through needs analysis |
| Contribution would create dependency | Redesign for capacity-building |
| Impact unmeasurable | Define proxy metrics or qualitative assessment |
| Organization wants marketing credit | Separate marketing from philanthropy |

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
resources_available:
- $100K annual budget
- Internal developer tools
- Engineering expertise

target_beneficiaries:
- Early-career developers
- Under-resourced engineering teams
```

**Output Excerpt:**
```markdown
### Primary Contribution: Open Source Developer Tools

**What:** Release internal productivity tools as open source projects with documentation

**Why This Builds Capacity:**
Like Carnegie's libraries, open source tools provide means for self-improvement. Developers gain capabilities without handouts.

**Who Benefits:**
- Early-career developers learning from production-quality code
- Small teams lacking resources to build internal tools
- The broader community through network effects

**Leverage Effect:**
One tool release serves unlimited users. Documentation multiplies as community contributes. Initial investment yields perpetual returns.

**Carnegie Test Results:**
- Builds capacity: Yes - provides tools developers can use to become more productive
- Helps self-helpers: Yes - benefits those motivated to learn and contribute
- Creates leverage: Yes - one release serves thousands
- Outlives giving: Yes - open source continues independently
- Respects dignity: Yes - no gatekeeping, available to all
```

---

## Integration

This skill derives from Andrew Carnegie's library-building philosophy. He funded over 2,500 libraries because they helped those who helped themselves, created leverage through scale, and built lasting institutions. When invoked by the carnegie expert, maintain Carnegie's voice: practical about impact, allergic to dependency-creating charity.

---

## Success Criteria

Design is complete when:
- [ ] Resources inventoried and contribution potential assessed
- [ ] Carnegie's capacity-building test applied to all recommendations
- [ ] Contribution strategy builds capacity, not dependency
- [ ] Impact measurement defined with clear metrics
- [ ] Implementation plan includes sustainability
- [ ] Governance structure defined