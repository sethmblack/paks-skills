---
name: parallel-project-portfolio-review
description: Assess and optimize a portfolio of parallel initiatives to maintain momentum and innovation using Thomas Edison's Invention Factory methodology.
license: MIT
metadata:
  version: 1.0.4638
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- parallel-project-portfolio-review
- writing
---

# Parallel Project Portfolio Review

Assess and optimize a portfolio of parallel initiatives to maintain momentum and innovation using Thomas Edison's Invention Factory methodology.

**Token Budget:** ~550 tokens (this prompt). Reserve tokens for review output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend adding projects that would burn out the team
- Encourage spreading resources so thin that nothing succeeds
- Dismiss critical maintenance work in favor of "innovation"
- Support abandoning commitments without proper stakeholder communication

**If asked to overload a team:** Refuse explicitly. Edison worked hard but systematically.

---

## When to Use

- Team feels stuck on a single blocking problem
- R&D portfolio needs assessment
- Innovation velocity has slowed
- Resources need rebalancing across initiatives
- User asks "Are we working on the right things?" or "Team feels stuck"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_projects** | Yes | List of active initiatives |
| **team_capacity** | Yes | Available resources (people, time, budget) |
| **strategic_objectives** | No | What the organization is trying to achieve |
| **current_blockers** | No | What is preventing progress |

---

## Workflow
### Phase 1: Portfolio Inventory

Assess current state of all initiatives:

For each project:

### Step 1: **Status** - Active, stalled, or completed?



### Step 2: **Progress** - On track, behind, or ahead?



### Step 3: **Blockers** - What is preventing progress?



### Step 4: **Learning** - What has been learned so far?



### Step 5: **Resources** - How much capacity is allocated?



### Phase 2: Balance Analysis

Evaluate portfolio composition:

| Portfolio Health Check | Good | Warning | Problem |
|-----------------------|------|---------|---------|
| Active projects | 3-5 per team | 6-8 per team | 9+ per team |
| Stalled projects | <10% | 10-25% | >25% |
| Resource utilization | 70-85% | 85-95% | >95% or <70% |
| Completion rate | Regular | Occasional | Rare |

**Edison principle:** "Work on several inventions at any given time... shift attention when one stalls."

### Phase 3: Momentum Assessment

Identify where momentum is strongest and weakest:

### Step 1: **High Momentum** - Projects making regular progress



### Step 2: **Stuck** - Projects blocked without clear path forward



### Step 3: **Zombie** - Projects neither progressing nor officially cancelled



### Step 4: **Promising** - Projects with recent breakthroughs



### Phase 4: Rebalancing Recommendations

Propose portfolio adjustments:

### Step 1: **Continue** - Projects worth sustained investment



### Step 2: **Accelerate** - Projects deserving more resources



### Step 3: **Pause** - Projects to set aside temporarily



### Step 4: **Cancel** - Projects to formally end



### Step 5: **Start** - New projects to fill gaps



### Phase 5: Execution Planning

Plan the transitions:

### Step 1: **Communication** - Who needs to know about changes?



### Step 2: **Resource Shifts** - How will capacity move?



### Step 3: **Knowledge Capture** - What must be documented from pausing/cancelling?



### Step 4: **Timeline** - When do changes take effect?



---

## Outputs

Produce a **Parallel Portfolio Review**:

```markdown
## Parallel Project Portfolio Review

**Review Date:** {date}
**Team Capacity:** {people/hours}
**Active Projects:** {count}
**Utilization:** {percentage}

---

### Portfolio Inventory

| Project | Status | Progress | Blockers | Capacity |
|---------|--------|----------|----------|----------|
| {name} | {status} | {%} | {what} | {resources} |

### Portfolio Health

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Active projects | {X} | {Y} | {good/warning/problem} |
| Stalled rate | {X%} | <10% | {good/warning/problem} |
| Utilization | {X%} | 70-85% | {good/warning/problem} |
| Completion rate | {X/quarter} | {Y/quarter} | {good/warning/problem} |

### Momentum Analysis

**High Momentum:**
- {project} - {why momentum is strong}

**Stuck:**
- {project} - {what's blocking, how long stuck}

**Zombie Projects:**
- {project} - {why not cancelled, what to do}

**Promising:**
- {project} - {what breakthrough occurred}

### Rebalancing Recommendations

| Project | Action | Rationale | Resources |
|---------|--------|-----------|-----------|
| {name} | {continue/accelerate/pause/cancel} | {why} | {change} |

### New Project Recommendations

| Opportunity | Strategic Fit | Resources Needed | Priority |
|-------------|---------------|------------------|----------|
| {project} | {alignment} | {capacity} | {H/M/L} |

### Execution Plan

**Week 1:**
- {communication actions}
- {resource shifts}

**Week 2:**
- {knowledge capture}
- {transitions complete}

### Anti-Patterns Identified

{Any issues like too many projects, zombie initiatives, stuck work, etc.}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No projects listed | Help inventory current work |
| All projects critical | Prioritize ruthlessly; everything cannot be #1 |
| Team at 100%+ utilization | Recommend immediate capacity creation or project pause |
| No new opportunities | Focus on unblocking stalled work |
| Cancellation resistance | Acknowledge sunk cost fallacy |

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
current_projects:
- API v2 migration (80% complete, on track)
- New observability platform (40% complete, stalled on vendor decision)
- Tech debt reduction (ongoing, regular progress)
- Experimental ML feature (20% complete, recent breakthrough)
- Legacy system support (ongoing, reactive)

team_capacity: 5 engineers, 40 hours/week each

current_blockers:
- Observability: waiting for procurement approval
- ML feature: needs data engineering support
```

**Output Excerpt:**
```markdown
### Momentum Analysis

**High Momentum:**
- API v2 migration - clear scope, team experienced, finish line visible
- Tech debt reduction - steady progress, measurable results

**Stuck:**
- New observability platform - stalled 3 weeks on vendor decision, team idle

**Promising:**
- Experimental ML feature - recent breakthrough on model accuracy

### Rebalancing Recommendations

| Project | Action | Rationale | Resources |
|---------|--------|-----------|-----------|
| Observability | Pause | Blocked externally, free capacity | -2 engineers |
| ML feature | Accelerate | Breakthrough deserves momentum | +1 engineer |
| API v2 | Continue | Near completion | No change |
| Tech debt | Continue | Sustainable pace | No change |
```

---

## Integration

This skill derives from Thomas Edison's parallel project methodology at Menlo Park. When invoked by the edison expert, maintain Edison's voice: work on many things, shift when stuck, maintain momentum.

---

## Success Criteria

Review is complete when:
- [ ] All current projects inventoried
- [ ] Portfolio health assessed against targets
- [ ] Momentum analyzed for each project
- [ ] Rebalancing recommendations provided
- [ ] Execution plan defined
- [ ] Anti-patterns identified and addressed