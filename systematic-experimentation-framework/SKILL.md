---
name: systematic-experimentation-framework
description: Guide teams through systematic, documented experimentation when facing difficult technical problems using Thomas Edison's methodology.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2042
keywords:
- escalation
- systematic-experimentation-framework
- writing
---

# Systematic Experimentation Framework

Guide teams through systematic, documented experimentation when facing difficult technical problems using Thomas Edison's methodology.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for experimentation plan output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Encourage experimentation that risks user safety without safeguards
- Support "move fast and break things" when "things" includes user data or critical systems
- Dismiss legitimate concerns about experimentation impact
- Encourage burnout through unrealistic trial demands

**If asked to experiment recklessly:** Refuse explicitly. Edison was systematic, not reckless.

---

## When to Use

- Team has tried multiple approaches without success
- Problem appears "unsolvable" but hasn't been exhaustively tested
- Debugging effort needs structure and documentation
- Optimization requires systematic comparison
- User asks "How do we approach this systematically?" or "We've tried everything"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **problem** | Yes | What is being solved |
| **success_criteria** | Yes | How will success be recognized |
| **tried_so_far** | No | What has already been attempted |
| **resources** | No | Time, people, equipment available |
| **constraints** | No | What cannot be changed or risked |

---

## Workflow
### Phase 1: Preparation

Define the experimentation scope:

### Step 1: **Success Criteria** - What exactly does success look like? Be precise.



### Step 2: **Inventory Attempts** - What has been tried? Document thoroughly.



### Step 3: **Enumerate Possibilities** - What hasn't been tried? List comprehensively.



### Step 4: **Resource Assessment** - What do you have to work with?



### Step 5: **Constraint Mapping** - What cannot be changed?



**Edison principle:** "Stock every conceivable material" - be prepared before you begin.

### Phase 2: Experimentation Design

Structure the systematic trials:

### Step 1: **Trial Categories** - Group possibilities by type



### Step 2: **Priority Ordering** - Which trials first? (feasibility x likelihood)



### Step 3: **Documentation Template** - How will each trial be recorded?



### Step 4: **Time Boxing** - How long per trial before moving on?



### Step 5: **Parallel Opportunities** - What can be tested simultaneously?



**Edison principle:** "I never quit until I get what I'm after."

### Phase 3: Execution and Learning

Conduct trials and extract value:

For each trial:

### Step 1: **Hypothesis** - What do we expect?



### Step 2: **Setup** - What changed from baseline?



### Step 3: **Result** - What happened?



### Step 4: **Learning** - What did we learn?



### Step 5: **Next Action** - Continue, pivot, or escalate?



**Edison principle:** "Negative results are just what I'm after. They are just as valuable to me as positive results."

### Phase 4: Persistence Assessment

Evaluate whether to continue:

| Signal | Continue Experimenting | Consider Stopping |
|--------|----------------------|-------------------|
| Learning rate | Still gaining insights | Same failures repeating |
| Possibility space | Many untried options | Exhausted main categories |
| Resource constraint | Capacity remains | Time/budget depleted |
| Problem importance | Still critical | Importance decreased |

---

## Outputs

Produce a **Systematic Experimentation Plan**:

```markdown
## Systematic Experimentation Plan

**Problem:** {description}
**Success Criteria:** {precise definition}
**Start Date:** {date}

---

### Attempt Inventory

**Previously Tried:**
| # | What Was Tried | Result | Learning |
|---|----------------|--------|----------|
| 1 | {attempt} | {result} | {lesson} |

**Trials Remaining:** {count}

### Experimentation Categories

| Category | Possibilities | Priority | Status |
|----------|--------------|----------|--------|
| {category} | {count} | {H/M/L} | {not started/in progress/complete} |

### Trial Documentation Template

For each experiment, record:
- **ID:** TRIAL-{number}
- **Hypothesis:** {what we expect}
- **Setup:** {what changed}
- **Result:** {what happened}
- **Learning:** {what we learned}
- **Time Spent:** {duration}
- **Next Action:** {continue/pivot/escalate}

### Active Trials

| ID | Category | Hypothesis | Status |
|----|----------|------------|--------|
| {id} | {category} | {hypothesis} | {status} |

### Learnings Log

| Trial | Learning | Implications |
|-------|----------|--------------|
| {id} | {what we learned} | {how this changes approach} |

### Persistence Assessment

**Trials Completed:** {count}
**Success Rate:** {percentage}
**Learning Rate:** {still high / declining / exhausted}
**Resources Remaining:** {assessment}
**Recommendation:** {continue / pivot / escalate}

### Next Steps

1. {immediate next trial}
2. {backup approach if trial fails}
3. {escalation plan if exhausted}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Success criteria unclear | Clarify before beginning experimentation |
| Nothing has been tried yet | Start with highest-probability approaches |
| Everything tried, nothing works | Expand possibility space, question assumptions |
| Time/resources depleted | Prioritize remaining trials ruthlessly |
| Team demoralized | Celebrate learning progress, not just success |

---

## Constraints

- Do not recommend approaches beyond stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Verify recommendations are implementable before suggesting them
- Consider maintainability and long-term implications

## Example

**Input:**
```
problem: Intermittent latency spikes in API responses
success_criteria: P99 latency under 200ms consistently for 7 days
tried_so_far:
- Scaled up database (no change)
- Added caching layer (slight improvement)
- Network analysis (nothing found)
```

**Output Excerpt:**
```markdown
### Experimentation Categories

| Category | Possibilities | Priority | Status |
|----------|--------------|----------|--------|
| Database | Connection pooling, query optimization, read replicas | High | In progress |
| Application | Thread pool tuning, GC settings, profiling | High | Not started |
| Infrastructure | CDN config, load balancer settings, container limits | Medium | Not started |
| Monitoring | Enhanced tracing, request correlation | Medium | Not started |

### Active Trials

| ID | Category | Hypothesis | Status |
|----|----------|------------|--------|
| TRIAL-004 | Database | Connection pool exhaustion causes spikes | In progress |
| TRIAL-005 | Database | Slow query during specific operations | Queued |

### Learnings Log

| Trial | Learning | Implications |
|-------|----------|--------------|
| TRIAL-001 | Scale didn't help | Problem isn't capacity |
| TRIAL-002 | Caching helped slightly | Some requests are cacheable |
| TRIAL-003 | No network issues found | Problem is above network layer |

**Recommendation:** Continue - still learning, multiple categories untried.
```

---

## Integration

This skill derives from Thomas Edison's exhaustive trial methodology that led to 1,093 patents. When invoked by the edison expert, maintain Edison's voice: persistent, documenting, learning from every failure.

---

## Success Criteria

Plan is complete when:
- [ ] Success criteria precisely defined
- [ ] Previous attempts documented with learnings
- [ ] Remaining possibilities enumerated by category
- [ ] Trial documentation template established
- [ ] Persistence assessment criteria defined
- [ ] Clear next steps identified