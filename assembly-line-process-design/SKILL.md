---
name: assembly-line-process-design
description: Transform complex workflows into simple, repeatable, scalable production processes by breaking work into discrete steps that anyone can master.
license: MIT
metadata:
  version: 1.0.400
  author: sethmblack
keywords:
- assembly-line-process-design
- transformation
- writing
---

# Assembly Line Process Design

Transform complex workflows into simple, repeatable, scalable production processes by breaking work into discrete steps that anyone can master.

**Token Budget:** ~600 tokens
**Origin:** Henry Ford methodology (Highland Park assembly line)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design processes that dehumanize or endanger workers
- Create systems that eliminate meaningful work without consideration
- Optimize for speed at the expense of safety or quality
- Apply assembly line thinking where creativity and judgment are essential

**If asked to apply this skill harmfully:** Refuse explicitly. The assembly line serves workers and customers, not the reverse.

---

## When to Use

- User asks to "optimize this workflow"
- Cycle time reduction needed
- Process scalability required
- User says "this process is too slow/inconsistent"
- Onboarding new team members to complex processes
- Standardization of ad-hoc procedures

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| process | Yes | The workflow or process to optimize |
| current_cycle_time | No | How long the process takes end-to-end |
| pain_points | No | Known bottlenecks or problems |
| scale_target | No | Desired throughput or frequency |

---

## Workflow

### Step 1: Map the Current Process

Document every step, exactly as it happens today:
- Who does what?
- How long does each step take?
- What waits between steps?
- Where do things go wrong?

### Step 2: Identify Waste

Apply the Ford waste taxonomy:

| Waste Type | Definition | Look For |
|------------|------------|----------|
| **Waiting** | Work sitting idle | Queues, approvals, handoffs |
| **Motion** | People moving unnecessarily | Context switching, meetings, searching |
| **Defects** | Work that must be redone | Errors, rollbacks, rework |
| **Overproduction** | Doing more than needed | Unused features, over-engineering |
| **Transportation** | Moving work unnecessarily | Tool switching, data transfers |

### Step 3: Decompose into Stations

Break the process into discrete "stations" where:
- One type of work happens
- One person (or system) is responsible
- The work is simple enough to master quickly
- Output flows directly to the next station

### Step 4: Standardize Each Station

For each station, define:
- Exact inputs required
- Exact steps to perform
- Exact outputs produced
- Quality criteria for "done"
- Time target

### Step 5: Create Flow

Design how work moves:
- Pull-based: Next station pulls when ready
- No batching: Single-piece flow where possible
- Visual signals: Status visible to all
- No accumulation: Work never waits between stations

### Step 6: Document for Reproduction

Create documentation so clear that:
- A new person can execute on day one
- Quality is consistent regardless of who executes
- Improvements can be captured and shared

---

## Outputs

Format the design as:

```markdown
## Assembly Line Process Design: [Process Name]

### Current State
| Metric | Value |
|--------|-------|
| Steps | [N] |
| Cycle time | [X minutes/hours] |
| Handoffs | [N] |
| Wait time | [X%] |

### Waste Identified

| Waste | Location | Impact |
|-------|----------|--------|
| [Type] | [Where] | [Time/quality cost] |

### Proposed Stations

| Station | Input | Process | Output | Time |
|---------|-------|---------|--------|------|
| 1. [Name] | [What arrives] | [What happens] | [What leaves] | [X min] |
| 2. [Name] | [What arrives] | [What happens] | [What leaves] | [X min] |

### Flow Design

```
[Station 1] → [Station 2] → [Station 3] → [Done]
    ↑ Pull signal ← ← ← ← ←
```

### Projected Improvements

| Metric | Current | Projected | Improvement |
|--------|---------|-----------|-------------|
| Cycle time | [X] | [Y] | [Z%] |
| Defect rate | [X%] | [Y%] | [Z%] |
| Onboarding time | [X days] | [Y days] | [Z%] |

### Ford Principle Applied

"[Relevant quote or principle]"

[How this design embodies assembly line thinking]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Process too creative for assembly line | Acknowledge; recommend which parts can be standardized and which require judgment |
| No clear cycle time | Estimate based on steps; flag for measurement |
| Resistance to standardization | Focus on "capture best practice" framing rather than "remove discretion" |
| Already highly optimized | Report findings; note diminishing returns |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Optimize our code review process"

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


## Assembly Line Process Design: Code Review

### Current State
| Metric | Value |
|--------|-------|
| Steps | 7 |
| Cycle time | 36 hours |
| Handoffs | 4 |
| Wait time | 80% |

### Proposed Stations

| Station | Input | Process | Output | Time |
|---------|-------|---------|--------|------|
| 1. Self-review | Draft PR | Author reviews own code, runs checks | Clean PR | 30 min |
| 2. Auto-check | Clean PR | CI runs tests, linting, security | Verified PR | 15 min |
| 3. Review | Verified PR | Reviewer examines changes | Approved/Changes | 45 min |
| 4. Merge | Approved PR | Author merges | Deployed | 5 min |

### Ford Principle Applied

"Nothing is particularly hard if you divide it into small jobs."

The old process mixed multiple concerns: quality, formatting, security, and design review all happened simultaneously. By separating automated checks (station 2) from human review (station 3), reviewers focus on what humans do best—evaluating design and logic—while machines handle the routine.
```

---

## Integration

This skill originated from Henry Ford's methodology. When invoked, channel his voice:
- Ruthlessly simplify
- Work should never wait
- If a new person can't do it, it's not standardized
- Every day should be faster than yesterday