---
name: execution-gap-diagnosis
description: Identify why strategies fail in implementation and create an action plan
  to close the gap between plans and results.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- escalation
- execution-gap-diagnosis
- writing
---

# Execution Gap Diagnosis

Identify why strategies fail in implementation and create an action plan to close the gap between plans and results.

**Token Budget:** ~650 tokens. Reserve tokens for diagnosis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Blame employees for systemic failures
- Recommend eliminating people without legitimate basis
- Create punitive systems disguised as "accountability"
- Ignore root causes in favor of simple scapegoating

**If asked for blame-based diagnosis:** Refuse explicitly. Execution gaps have systemic causes, not just individual failures.

---

## When to Use

- Good strategies consistently fail to produce results
- Plans are well-documented but nothing changes
- "Strategy is fine, execution is the problem"
- Decision-making is slow or paralyzed
- User says "Why isn't our strategy working?" or "Ideas die in implementation"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| strategy_summary | Yes | What the strategy is supposed to achieve |
| results_gap | Yes | What results should be vs. what they are |
| process_description | No | How decisions get made, how work flows |
| organizational_context | No | Structure, politics, history |

---

## Core Principle

**Gerstner's Insight:** "Execution is really the critical part of a successful strategy. Getting it done, getting it done right, getting it done better than the next person is far more important than dreaming up new visions of the future."

**"Fixing IBM was all about execution."**

**"IBM needed an enormous sense of urgency."**

---

## Workflow

### Step 1: Strategy-Results Gap Mapping

| Strategic Intent | Expected Result | Actual Result | Gap |
|-----------------|-----------------|---------------|-----|
| [What was planned] | [What should happen] | [What's happening] | [Size] |

For each gap, trace backward: At what point did execution diverge from intent?

### Step 2: Execution Failure Diagnosis

Five categories of execution failure:

**1. Clarity Failure**
- Strategy was announced but not translated into actions
- People don't know what they're supposed to do differently
- **Symptoms:** "What does that strategy mean for me?"

**2. Urgency Failure**
- Strategy is understood but treated as "eventually"
- Competing priorities absorb attention
- **Symptoms:** "We'll get to it after..."

**3. Capability Failure**
- People understand and want to execute but can't
- Skills, tools, or resources are missing
- **Symptoms:** "We're trying but..."

**4. Accountability Failure**
- No one owns results
- Success and failure have same consequences
- **Symptoms:** "Whose job is this?"

**5. Gridlock Failure**
- Decisions cannot get made
- Processes create delays without adding value
- **Symptoms:** "We're waiting for approval..."

### Step 3: Gridlock Analysis

Where are decisions stuck?

| Decision Type | Who Decides | How Long | Bottleneck |
|--------------|-------------|----------|------------|
| [e.g., pricing] | [role/committee] | [days/weeks] | [why slow] |

**Gerstner's Method:** "Simplifying the organization for speed" and "breaking the gridlock."

For each bottleneck:
- Can decision rights be pushed down?
- Can the process be eliminated?
- Is the delay adding value or just adding time?

### Step 4: Urgency Injection

How to create urgency without creating panic:

1. **Make the stakes visible** - What happens if we don't execute?
2. **Create near-term milestones** - What must happen in 30 days? 90 days?
3. **Public commitment** - Who will report progress and when?
4. **Consequence clarity** - What happens if milestones are missed?

### Step 5: Accountability Mapping

For each strategic priority:

| Priority | Owner | Milestone | Due Date | Consequence |
|----------|-------|-----------|----------|-------------|
| [What] | [Who - single person] | [Measurable] | [Date] | [If missed] |

**Rule:** No priority without a single owner. No milestone without a date. No date without a consequence.

---

## Outputs

```markdown
## Execution Gap Diagnosis

### Strategy-Results Gap
| Strategic Intent | Gap | Size |
|-----------------|-----|------|
| [intent] | [actual vs expected] | [% shortfall] |

### Failure Category Analysis
| Category | Present? | Evidence |
|----------|----------|----------|
| Clarity | Yes/No | [specific evidence] |
| Urgency | Yes/No | [specific evidence] |
| Capability | Yes/No | [specific evidence] |
| Accountability | Yes/No | [specific evidence] |
| Gridlock | Yes/No | [specific evidence] |

**Primary Failure Mode:** [Category with most impact]

### Gridlock Points
| Decision | Current Time | Target Time | Action |
|----------|-------------|-------------|--------|
| [type] | [days] | [days] | [fix] |

### Urgency Plan
- **Stakes:** [What happens if we don't execute]
- **30-day milestone:** [What must happen]
- **90-day milestone:** [What must happen]
- **Public forum:** [Where progress will be reported]

### Accountability Map
| Priority | Owner | Milestone | Due | Consequence |
|----------|-------|-----------|-----|-------------|
| [what] | [who] | [measure] | [date] | [if missed] |

### Immediate Actions (Next 2 Weeks)
1. [Specific action with owner]
2. [Specific action with owner]
3. [Specific action with owner]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Vague strategy | Cannot diagnose execution without clear strategy; request clarification |
| No results data | Cannot measure gap without results; request metrics |
| Blame-focused request | Redirect to systemic causes; refuse scapegoating |
| Leadership gridlock | Flag that execution will fail without leadership alignment |

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
Strategy: "Become the leading platform for small business finance"
Expected: 50% growth in SMB customers this year
Actual: 10% growth through Q3
We have a great product and marketing plan, but we're not executing.
```

**Output:**

### Strategy-Results Gap
| Strategic Intent | Gap | Size |
|-----------------|-----|------|
| 50% SMB customer growth | 10% actual vs 50% target | 80% shortfall |

### Failure Category Analysis
| Category | Present? | Evidence |
|----------|----------|----------|
| Clarity | Partial | Marketing plan exists; sales quotas unclear |
| Urgency | Yes | "Great product" complacency; competing priorities |
| Capability | No | Team is capable; not a skill issue |
| Accountability | Yes | No single owner for SMB growth target |
| Gridlock | Yes | Product requests for SMB features stuck in backlog |

**Primary Failure Mode:** Accountability + Gridlock

### Gridlock Points
| Decision | Current Time | Target Time | Action |
|----------|-------------|-------------|--------|
| SMB feature prioritization | Weeks (stuck in backlog) | 48 hours | CEO override authority for strategic priorities |
| SMB pricing decisions | 2 weeks (committee) | 3 days | Delegate to product owner with guardrails |

### Urgency Plan
- **Stakes:** At 10% growth, we lose first-mover advantage; competitors filling gap
- **30-day milestone:** 100 new SMB customers with documented win/loss reasons
- **90-day milestone:** 25% annual rate (1000 new customers) or strategy pivot
- **Public forum:** Weekly exec standup; monthly board review

### Accountability Map
| Priority | Owner | Milestone | Due | Consequence |
|----------|-------|-----------|-----|-------------|
| SMB customer growth | VP SMB (new role) | 100 new customers | 30 days | Role reassessed |
| SMB features | Product Lead | 3 SMB features shipped | 60 days | Escalation to CEO |
| SMB marketing | Marketing Lead | 5x lead volume | 45 days | Budget reallocation |

### Immediate Actions (Next 2 Weeks)
1. Appoint VP SMB with full P&L authority (CEO, Week 1)
2. Clear SMB feature backlog with CEO override (CPO, Week 1)
3. Set up weekly SMB metrics review (VP SMB, Week 2)

---

## Integration

This skill is derived from Lou Gerstner's execution-focused turnaround methodology. Use in conjunction with:
- `enterprise-turnaround-diagnosis` - When execution gap is part of broader crisis
- `culture-through-behavior` - When culture creates execution barriers