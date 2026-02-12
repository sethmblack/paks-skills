---
name: speed-constraint-analysis
description: Apply Patrick Collison's insight that "slow and expensive usually go
  together" to identify where temporal constraints can force simplicity, reduce cost,
  and accelerate execution.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- speed-constraint-analysis
- structure
- writing
---

# Speed Constraint Analysis

Apply Patrick Collison's insight that "slow and expensive usually go together" to identify where temporal constraints can force simplicity, reduce cost, and accelerate execution.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend speed at the cost of safety-critical systems
- Suggest cutting corners on security, compliance, or user safety
- Apply speed pressure to decisions that genuinely require deliberation (trapdoor decisions)
- Encourage burnout or unsustainable pace

**If asked to speed up safety-critical work:** Clarify that some work cannot be rushed. Apply speed constraints only to non-critical path items.

---

## When to Use

- Project feels slower than it should be
- Timeline is being questioned or extended
- Team is waiting for things that feel unnecessary
- Budget is growing with timeline
- User asks: "This is taking too long" "How can we go faster?" "Apply speed audit" "Challenge our timeline"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| project_or_process | Yes | What is taking longer than expected |
| current_timeline | Yes | How long it's expected to take |
| target_timeline | No | Desired timeline (if known) |
| blockers | No | Known reasons for slowness |
| constraints | No | Things that genuinely cannot change |

---

## The Speed Philosophy

"The 'good, cheap, fast—choose two' maxim is devious misinformation spread by the slow."

Patrick Collison's core insight: **Speed and quality are not opposed. Speed constraints force simplicity. Simplicity enables quality. Slow and expensive go together.**

### Why Speed Reduces Cost

1. **It takes time to spend** - The longer a project runs, the more opportunities to add scope
2. **Temporal constraints force prioritization** - When you have less time, you must choose what matters
3. **Waiting accumulates overhead** - Coordination, context-switching, status updates
4. **Simplicity emerges from pressure** - Complex solutions take time; simple solutions ship

### The Speed Questions

Ask in every meeting:
- "Could we do that faster?"
- "What is the minimum increment required to ship?"
- "What are we waiting for that we don't need to wait for?"

---

## Workflow

### Step 1: Map the Current Timeline

| Phase | Duration | What Happens | Actually Essential? |
|-------|----------|--------------|---------------------|
| [Phase 1] | [Time] | [Activities] | [Yes/No] |
| [Phase 2] | [Time] | [Activities] | [Yes/No] |
| ... | ... | ... | ... |
| **Total** | **[Time]** | | |

### Step 2: Identify Wait States

Where is the project waiting rather than moving?

| Wait State | Duration | Waiting For | Is Wait Essential? |
|------------|----------|-------------|-------------------|
| [Wait 1] | [Time] | [What/Who] | [Yes/No/Partially] |
| [Wait 2] | [Time] | [What/Who] | [Yes/No/Partially] |

**Common non-essential waits:**
- Waiting for the "right" hire before moving forward
- Waiting for quarterly planning cycles
- Waiting for perfect information to decide
- Waiting for approvals that add little value
- Waiting for alignment that isn't actually needed

### Step 3: Apply the Time Constraint Test

What would happen if this project had to be done in half the time?

| If we had half the time... | What we'd cut/change |
|---------------------------|---------------------|
| Scope | [What would be descoped] |
| Process | [What steps would be eliminated] |
| Quality bar | [What "polish" would be skipped] |
| Coordination | [What alignment would be dropped] |
| Sequence | [What would be parallelized] |

**Key question:** Looking at that list, how many of those cuts would actually hurt the outcome?

### Step 4: Calculate the Slow Tax

What is the cost of the current timeline?

| Cost Category | Impact |
|---------------|--------|
| Direct cost | [Salaries, resources for extra time] |
| Opportunity cost | [What else could be done] |
| Market cost | [Competitor movement, timing windows] |
| Morale cost | [Team energy, momentum] |
| Scope creep risk | [Added complexity over time] |

**The Collison Insight:** "Lopping a year off a project schedule often reduces cost substantially."

### Step 5: Generate Speed Interventions

For each intervention, specify what changes and the expected time savings.

---

## Output Format

```markdown
## Speed Constraint Analysis: [Project/Process]

### Current State
**Timeline:** [Current expected duration]
**Target:** [Desired timeline, if any]
**Gap:** [Difference]

### Timeline Breakdown

| Phase | Duration | Essential? | Speed Opportunity |
|-------|----------|------------|-------------------|
| [Phase] | [Time] | [Y/N] | [What could change] |

### Wait State Audit

| Wait | Duration | Essential? | Resolution |
|------|----------|------------|------------|
| [Wait] | [Time] | [Y/N] | [How to eliminate] |

**Total non-essential waiting:** [Time]

### The Half-Time Test

If this had to ship in [half the time]:
- **We'd cut:** [List]
- **We'd change:** [List]
- **We'd parallelize:** [List]
- **We'd descope:** [List]

**Verdict:** [How many of these cuts would actually hurt?]

### The Slow Tax

| Cost | Impact |
|------|--------|
| Direct | [$$$ or person-weeks] |
| Opportunity | [What's delayed] |
| Market | [Timing risk] |
| Morale | [Energy drain] |

**Total slow tax:** [Summary]

### Speed Interventions

#### High Impact (Save > 1 week)
1. **[Intervention]**
   - Change: [What changes]
   - Saves: [Time]
   - Risk: [What could go wrong]

2. **[Intervention]**
   - Change: [What changes]
   - Saves: [Time]
   - Risk: [What could go wrong]

#### Medium Impact (Save 2-5 days)
1. **[Intervention]**
   - Change: [What changes]
   - Saves: [Time]

#### Quick Wins (Save < 2 days)
1. **[Intervention]** - Saves: [Time]

### The Collison Question

"Could we do that faster? What is the minimum increment required to ship?"

**Minimum shippable increment:** [What is the smallest thing that delivers value]
**Time to minimum increment:** [How fast could that ship]
**Current plan vs minimum:** [Gap]

### Recommendation

**Original timeline:** [X]
**Achievable timeline:** [Y]
**Savings:** [X - Y]

**Key moves:**
1. [Most important intervention]
2. [Second most important]
3. [Third most important]

### Speed vs Safety Check

- [ ] No safety-critical work is being rushed
- [ ] Security and compliance are protected
- [ ] Quality bar is appropriate for stage (pre-PMF vs post-PMF)
- [ ] Team pace is sustainable
```

---

## Constraints

- Never sacrifice safety for speed
- Distinguish between trapdoor decisions (need care) and two-way doors (can move fast)
- Recognize that some coordination is genuinely necessary
- Sustainable pace matters for long-term execution

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Timeline is already aggressive | Validate that it's achievable. Look for hidden waits. |
| Project is genuinely complex | Focus on parallelization and minimum increments. |
| External dependencies are real | Identify what can proceed while waiting. |
| Team is already stretched | Focus on elimination, not acceleration. |
| Safety-critical work | Apply speed only to non-critical path. |

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:** "Our infrastructure migration is planned for 6 months. Leadership is asking if it can be done in 3. Is that realistic?"

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


## Speed Constraint Analysis: Infrastructure Migration

### Current State
**Timeline:** 6 months
**Target:** 3 months
**Gap:** 3 months (50% reduction requested)

### Timeline Breakdown

| Phase | Duration | Essential? | Speed Opportunity |
|-------|----------|------------|-------------------|
| Planning & Design | 6 weeks | Partially | Reduce from 6 to 2 weeks by deciding, not perfecting |
| Vendor Evaluation | 4 weeks | No | Already know the answer. Cut to 1 week confirmation. |
| Proof of Concept | 4 weeks | Yes | Run parallel with planning. |
| Migration Development | 8 weeks | Yes | Focus on automation, not manual processes. |
| Testing | 4 weeks | Yes | Continuous testing, not phase. |
| Rollout | 2 weeks | Yes | Canary + progressive, not big-bang. |

### Wait State Audit

| Wait | Duration | Essential? | Resolution |
|------|----------|------------|------------|
| Vendor contract negotiation | 3 weeks | Partially | Legal parallelization, accept standard terms |
| Architecture review committee | 2 weeks | No | Single decision-maker, 1 meeting |
| Budget approval cycle | 2 weeks | Partially | Emergency approval process |
| Hiring "right" team | Ongoing | No | Start with who you have |

**Total non-essential waiting:** 5+ weeks

### The Half-Time Test

If this had to ship in 3 months:
- **We'd cut:** Vendor evaluation (we know who), extensive PoC (minimal PoC), design perfection (iterate post-migration)
- **We'd change:** Sequential to parallel (planning + PoC + vendor simultaneously)
- **We'd parallelize:** Testing with development, documentation with rollout
- **We'd descope:** Non-critical workloads migrate in phase 2

**Verdict:** Most of these cuts don't hurt the outcome. They remove "nice to have" perfection.

### The Slow Tax

| Cost | Impact |
|------|--------|
| Direct | 3 additional months of team = $450K |
| Opportunity | New feature work blocked |
| Market | Competitor launches on new infra |
| Morale | Team fatigue from long project |

**Total slow tax:** ~$500K+ direct cost, significant opportunity cost

### Speed Interventions

#### High Impact (Save > 1 week)
1. **Parallel planning + PoC + vendor**
   - Change: Start all three week 1, not sequentially
   - Saves: 4 weeks
   - Risk: Rework if PoC invalidates plan (acceptable)

2. **Single decision-maker for architecture**
   - Change: VP Eng decides, no committee
   - Saves: 2 weeks
   - Risk: Less consensus (VP is accountable)

3. **Phase migration by workload criticality**
   - Change: Critical services first, rest in phase 2
   - Saves: 3 weeks
   - Risk: Phase 2 needs planning later

#### Medium Impact (Save 2-5 days)
1. **Accept vendor standard contract**
   - Change: Skip negotiation of non-critical terms
   - Saves: 2 weeks

2. **Continuous testing from day 1**
   - Change: Test harness runs daily, not after dev
   - Saves: 2 weeks

### The Collison Question

"Could we do that faster? What is the minimum increment required to ship?"

**Minimum shippable increment:** Migration of 3 critical services to new infrastructure
**Time to minimum increment:** 6 weeks
**Current plan vs minimum:** 6 months vs 6 weeks (10x gap)

### Recommendation

**Original timeline:** 6 months
**Achievable timeline:** 3 months (phased approach)
**Minimum viable timeline:** 6 weeks (critical services only)
**Savings:** 3 months / $450K direct cost

**Key moves:**
1. Start all phases in parallel from week 1
2. Single decision-maker (VP Eng) for all architecture calls
3. Phase by criticality - critical services by month 3, rest by month 5

### Speed vs Safety Check

- [x] No safety-critical work is being rushed - migration is phased, canary rollout
- [x] Security and compliance are protected - same controls apply
- [x] Quality bar is appropriate - continuous testing from day 1
- [x] Team pace is sustainable - parallel work, not overtime

**Verdict: 3 months is achievable.** The 6-month plan contains 3 months of non-essential waiting and sequential work. Parallel execution + single decision-maker + phased rollout gets you there.

---

## Integration

This skill is part of the **Patrick Collison** expert persona. Use it when timelines feel too long or projects are accumulating cost. It pairs well with:
- **trapdoor-decision-filter** to identify which decisions can move fast
- **pre-pmf-post-pmf-diagnosis** to calibrate appropriate speed for stage
- **seven-lines-of-code-audit** to simplify technical complexity