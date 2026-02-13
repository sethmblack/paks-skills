---
name: three-magnets-analysis
description: Reveal a third alternative when presented with a binary choice by mapping the attractions and drawbacks of each option, then synthesizing a solution that captures the best features of both while avoiding their drawbacks.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - three-magnets-analysis
  - urban-planning
---

# Three Magnets Analysis

Reveal a third alternative when presented with a binary choice by mapping the attractions and drawbacks of each option, then synthesizing a solution that captures the best features of both while avoiding their drawbacks. Based on Ebenezer Howard's famous Three Magnets diagram from *Garden Cities of To-Morrow* (1898/1902).

---

## Constitutional Constraints

- **Honest limitations** - The third alternative will not solve every problem. Acknowledge what it cannot address.
- **No false synthesis** - Some choices truly are binary. If no genuine third option exists, say so.
- **Practical mechanisms** - Every synthesis must include concrete mechanisms, not just aspirational blending.
- **Respect trade-offs** - Do not pretend trade-offs disappear. Show how they are managed or rebalanced.

---

## When to Use

- Binary choice presented: "Should we do A or B?"
- False dichotomy suspected: "We must choose between X and Y"
- Trade-off framing: "The cost of this benefit is that drawback"
- Planning dilemmas: urban vs. rural, growth vs. preservation, efficiency vs. equity
- Policy debates stuck between two inadequate options
- Strategic decisions where both paths have significant drawbacks

---

## Don't Use When

- The choice genuinely is binary with no synthesis possible
- One option is clearly superior (no need for synthesis)
- The user needs a quick decision, not analysis
- The options are not truly in tension

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| option_a | Yes | First option being considered |
| option_b | Yes | Second option being considered |
| context | Yes | Situation, constraints, stakeholders |
| stated_attractions_a | No | Known advantages of option A |
| stated_drawbacks_a | No | Known disadvantages of option A |
| stated_attractions_b | No | Known advantages of option B |
| stated_drawbacks_b | No | Known disadvantages of option B |
| desired_outcomes | No | What success would look like |

---

## Three Magnets Workflow

### Phase 1: Map the First Magnet

Analyze Option A completely:

**Attractions (what draws people to this option):**
- List all genuine advantages
- Include economic, social, practical, emotional benefits
- Note which stakeholders benefit most

**Drawbacks (what repels people from this option):**
- List all genuine disadvantages
- Include costs, risks, externalities
- Note which stakeholders bear the costs

### Phase 2: Map the Second Magnet

Analyze Option B with equal rigor:

**Attractions (what draws people to this option):**
- List all genuine advantages
- Identify advantages that are inverse of A's drawbacks

**Drawbacks (what repels people from this option):**
- List all genuine disadvantages
- Identify drawbacks that are inverse of A's attractions

### Phase 3: Identify the Synthesis Opportunity

Compare the two magnets:

| Question | Analysis |
|----------|----------|
| What attractions does A have that B lacks? | [List] |
| What attractions does B have that A lacks? | [List] |
| What drawbacks of A does B avoid? | [List] |
| What drawbacks of B does A avoid? | [List] |
| Is there overlap in attractions? | [Identify common ground] |
| Are any drawbacks inherent vs. design choices? | [Distinguish] |

**Key insight:** The third alternative combines attractions from both columns while designing out the drawbacks that arise from each option's limitations.

### Phase 4: Design the Third Magnet

Create the synthesis:

**Third Alternative Description:**
- Name the synthesis (what is this new option called?)
- Explain its core principle
- Show how it draws from both A and B

**Attractions (combined and enhanced):**
- List attractions preserved from A
- List attractions preserved from B
- List new attractions that emerge from combination

**Mechanisms (how it actually works):**
- Specific structural elements
- Governance or ownership arrangements
- Physical or organizational design features
- Economic model

**Remaining Trade-offs (honest limitations):**
- What this option still cannot solve
- What compromises are inherent
- What conditions must be met

---

## Output Format

```markdown
## Three Magnets Analysis: [Topic]

### The Question

"[Restate the binary choice being analyzed]"

---

### Magnet 1: [Option A Name]

**Attractions:**
- [Attraction 1]
- [Attraction 2]
- [Attraction 3]

**Drawbacks:**
- [Drawback 1]
- [Drawback 2]
- [Drawback 3]

---

### Magnet 2: [Option B Name]

**Attractions:**
- [Attraction 1]
- [Attraction 2]
- [Attraction 3]

**Drawbacks:**
- [Drawback 1]
- [Drawback 2]
- [Drawback 3]

---

### Magnet 3: [Synthesis Name] (The Third Alternative)

**Core Principle:** [One sentence describing the synthesis]

**Combined Attractions:**
- From [A]: [Attraction preserved]
- From [B]: [Attraction preserved]
- New: [Emergent benefit from combination]

**Key Mechanisms:**
1. [Specific mechanism 1]
2. [Specific mechanism 2]
3. [Specific mechanism 3]

**Honest Limitations:**
- [What this cannot solve]
- [Remaining trade-offs]
- [Required conditions]

---

### Recommendation

[Brief statement on whether the third alternative is viable and what first steps would test it]
```

---

## Example

**Input:** "Our company must choose between centralizing all operations in one headquarters (efficiency, unified culture) or staying fully distributed (flexibility, talent access). Which should we do?"

**Output:**

## Three Magnets Analysis: Company Location Strategy

### The Question

"Should we centralize all operations in one headquarters or remain fully distributed?"

---

### Magnet 1: Centralized Headquarters

**Attractions:**
- Operational efficiency from co-location
- Unified culture and easier collaboration
- Clear identity and brand presence
- Simplified logistics and administration
- Spontaneous interaction and innovation
- Easier onboarding and mentorship

**Drawbacks:**
- Limits talent pool to one geography
- High real estate costs in major markets
- Commute burden on employees
- Single point of failure (disaster, pandemic)
- Forces relocation or excludes remote talent
- One-size-fits-all schedule constraints

---

### Magnet 2: Fully Distributed

**Attractions:**
- Access to global talent regardless of location
- Lower real estate overhead
- Employee flexibility and autonomy
- Resilience to local disruptions
- Better work-life balance for many
- No commute time or cost

**Drawbacks:**
- Harder to build cohesive culture
- Collaboration friction across time zones
- Onboarding and mentorship challenges
- Loneliness and isolation for some workers
- Management complexity increases
- Spontaneous innovation harder to capture

---

### Magnet 3: Hub-and-Spoke Network (The Third Alternative)

**Core Principle:** Multiple regional hubs provide the benefits of co-location while distributed presence preserves talent access and flexibility.

**Combined Attractions:**
- From Centralized: Co-located teams for collaboration (within hubs)
- From Centralized: Physical spaces for culture-building and mentorship
- From Distributed: Access to talent across multiple regions
- From Distributed: Resilience through geographic distribution
- New: Time zone coverage for global operations
- New: Local market presence in multiple regions

**Key Mechanisms:**
1. **Regional hubs** (3-5 locations) where 60-70% of employees work at least 2-3 days/week
2. **Hub selection criteria** based on talent density, cost, time zone coverage
3. **Team clustering** - keep collaborating teams in same hub when possible
4. **Remote-eligible roles** for positions that genuinely don't require co-location (20-30%)
5. **Quarterly all-hands** rotating between hubs for cross-pollination
6. **Standardized async practices** so hub-to-hub collaboration works smoothly

**Honest Limitations:**
- Still excludes talent in non-hub locations unless they are remote-eligible
- More complex than either pure model to manage
- Requires investment in multiple real estate footprints
- Some roles may genuinely need full co-location
- Cultural unity harder than single HQ (though easier than full distribution)

---

### Recommendation

The hub-and-spoke model is viable for companies of 100+ employees with functions that benefit from collaboration. Test by designating one secondary hub and measuring whether collaboration and culture metrics hold while talent access improves. If successful, expand to additional hubs based on strategic priorities.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No genuine third alternative exists | State clearly: "This appears to be a genuine binary choice. The options are mutually exclusive because [reason]." Provide decision criteria instead. |
| User hasn't provided enough context | Ask clarifying questions about stakeholders, constraints, and desired outcomes before proceeding. |
| The "choice" is actually agreement | Note that the options aren't truly opposed; the real question may be sequencing or emphasis. |
| Synthesis is theoretically possible but practically unlikely | Acknowledge the conditions required and assess likelihood. |

---

## Integration

This skill is part of the **Ebenezer Howard** expert persona. Howard invented the Three Magnets diagram to show that town and country were not the only options - a third alternative (the Garden City) could combine the best of both.

Use this skill when:
- Howard expert encounters binary framing
- Urban planning, housing, or community development questions present trade-offs
- Any strategic decision where both options have significant drawbacks

The skill embodies Howard's core insight: **Many apparent dichotomies are false. Creative synthesis can transcend trade-offs - but only with specific mechanisms, not wishful thinking.**

---

## Success Criteria

A successful Three Magnets Analysis:
- [ ] Accurately captures the genuine attractions of both options
- [ ] Honestly names the drawbacks without minimizing
- [ ] Proposes a synthesis with concrete mechanisms (not just "blend both")
- [ ] Acknowledges what the synthesis cannot solve
- [ ] Provides actionable next steps to test the third alternative
