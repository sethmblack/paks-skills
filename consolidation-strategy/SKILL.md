---
name: consolidation-strategy
description: Analyze fragmented systems, tools, or processes and develop a unification strategy to reduce redundancy, improve efficiency, and bring order to chaos.
version: 1.0.0
author: sethmblack
tags: [consolidation-strategy, writing]
---

# Consolidation Strategy

Analyze fragmented systems, tools, or processes and develop a unification strategy to reduce redundancy, improve efficiency, and bring order to chaos.

**Token Budget:** ~600 tokens
**Origin:** John D. Rockefeller methodology (Standard Oil consolidation approach)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend consolidation that eliminates necessary diversity or resilience
- Ignore legitimate reasons for current fragmentation
- Force consolidation on stakeholders without considering their needs
- Prioritize uniformity over functionality

**If asked to apply this skill harmfully:** Refuse explicitly. Consolidation serves efficiency, not control for its own sake.

---

## When to Use

- User says "We have too many tools doing the same thing"
- Platform rationalization needed
- Tool sprawl review requested
- User asks "How do we consolidate our systems?"
- Technical debt review related to fragmentation
- M&A integration planning

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| domain | Yes | The area to analyze (tools, processes, systems) |
| inventory | No | Current list of items (will discover if not provided) |
| constraints | No | Items that cannot be consolidated |
| success_criteria | No | What good consolidation looks like |

---

## Workflow

### Step 1: Inventory the Fragmentation

Document all items in the domain:

| Item | Purpose | Users | Age | Cost | Owner |
|------|---------|-------|-----|------|-------|
| [Name] | [What it does] | [Who uses it] | [How old] | [$X] | [Who maintains] |

### Step 2: Identify Overlap

Create a capability matrix:

| Capability | Tool A | Tool B | Tool C |
|------------|--------|--------|--------|
| [Function 1] | Yes | Yes | No |
| [Function 2] | Yes | No | Yes |
| [Function 3] | No | Yes | Yes |

Calculate overlap percentage: (Shared capabilities / Total capabilities) x 100

### Step 3: Assess Consolidation Candidates

For each potential consolidation:

| Factor | Assessment |
|--------|------------|
| **Capability coverage** | Can one tool serve all needs? |
| **Migration cost** | What does switching require? |
| **User impact** | How disruptive to workflows? |
| **Maintenance savings** | Ongoing cost reduction? |
| **Risk** | What could go wrong? |

### Step 4: Evaluate Consolidation Paths

Three primary approaches:

1. **Select winner** - Choose best existing tool, migrate others
   - Best when: Clear capability leader exists
   - Risk: Forcing users onto suboptimal tool

2. **Build unified** - Create new tool incorporating best features
   - Best when: No existing tool is adequate
   - Risk: Time, cost, adoption uncertainty

3. **Federate** - Keep separate but integrate via standards
   - Best when: Consolidation cost exceeds benefit
   - Risk: Incomplete rationalization

### Step 5: Develop Migration Roadmap

For each consolidation:
1. Define target state
2. Identify migration phases
3. Plan parallel running period
4. Define cutover criteria
5. Plan decommissioning

---

## Outputs

Format the strategy as:

```markdown
## Consolidation Strategy: [Domain]

### Current State

**Items inventoried:** [X]
**Estimated overlap:** [Y%]
**Current total cost:** [$Z]

### Fragmentation Map

| Item | Primary Purpose | Overlap With | Users | Annual Cost |
|------|-----------------|--------------|-------|-------------|
| [Name] | [Purpose] | [Other items] | [N] | [$X] |

### Consolidation Opportunities

#### Opportunity 1: [Name]
**Current state:** [X tools] doing [Y function]
**Recommended path:** [Select winner/Build unified/Federate]
**Target state:** [Single tool/Unified platform/Integrated federation]
**Projected savings:** [$X/year] + [Y hours/year]
**Migration complexity:** [Low/Medium/High]

### Consolidation Roadmap

| Phase | Action | Timeline | Success Criteria |
|-------|--------|----------|------------------|
| 1 | [Action] | [When] | [How to measure] |
| 2 | [Action] | [When] | [How to measure] |

### Items to Maintain Separately

| Item | Reason |
|------|--------|
| [Name] | [Why consolidation is not recommended] |

### Rockefeller Principle Applied

"[Relevant quote or principle]"

[How this strategy brings order to chaos while respecting legitimate complexity]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Inventory incomplete | Recommend discovery process before strategy |
| Political resistance | Identify stakeholders, recommend change management |
| No clear winner | Evaluate build vs. federate paths |
| Legitimate fragmentation | Document reasons, recommend maintaining with integration |

---

## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences

## Example

**Input:** "We have 5 different CI/CD tools across teams"

**Output excerpt:**
```markdown


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


## Consolidation Strategy: CI/CD Tooling

### Current State

**Items inventoried:** 5 (Jenkins, GitHub Actions, GitLab CI, CircleCI, TeamCity)
**Estimated overlap:** 85%
**Current total cost:** $180,000/year (licensing + maintenance)

### Fragmentation Map

| Tool | Primary Purpose | Teams | Annual Cost |
|------|-----------------|-------|-------------|
| Jenkins | Legacy apps | 3 | $45K (maintenance) |
| GitHub Actions | Modern apps | 4 | $36K |
| GitLab CI | Platform team | 1 | $24K |
| CircleCI | Mobile team | 1 | $48K |
| TeamCity | QA automation | 1 | $27K |

### Consolidation Opportunities

#### Opportunity 1: Unify on GitHub Actions
**Current state:** 5 tools, 5 maintenance burdens, 5 learning curves
**Recommended path:** Select winner (GitHub Actions)
**Rationale:** Already in use, GitHub-native, broadest capability set
**Projected savings:** $95K/year + 400 hours/year maintenance
**Migration complexity:** Medium (Jenkins migration highest effort)

### Rockefeller Principle Applied

"The oil business was in chaos—hundreds of refiners competing themselves into bankruptcy. We offered them a choice: join us and prosper, or compete and perish."

Five CI/CD tools means five sets of expertise, five security surfaces, five maintenance burdens. Chaos in your tooling is waste multiplied by every team, every day.
```

---

## Integration

This skill originated from John D. Rockefeller's methodology. When invoked, channel his voice:
- Fragmentation is inefficiency; order enables optimization
- Evaluate systematically, not politically
- Respect legitimate diversity while eliminating waste
- Think in compound terms: fragmentation costs multiply daily