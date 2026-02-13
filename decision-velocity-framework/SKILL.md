---
name: decision-velocity-framework
description: Break through analysis paralysis and chronic organizational indecision to enable forward movement while maintaining decision quality.
license: MIT
metadata:
  version: 1.0.758
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- decision-velocity-framework
- transformation
- writing
---

# Decision Velocity Framework

Break through analysis paralysis and chronic organizational indecision to enable forward movement while maintaining decision quality.

**Origin:** Bob Iger methodology - "Chronic indecision is not only inefficient and counterproductive, but it is deeply corrosive to morale."

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Rush decisions that genuinely require more information (safety, legal, ethical implications)
- Recommend decisions that cause irreversible harm without adequate consideration
- Fabricate urgency where none exists
- Override legitimate concerns with artificial decisiveness

**If asked to force a decision that requires more information:** Explain what specific information is needed and propose a bounded timeline to obtain it.

---

## When to Use

- User says "We're stuck" or "We keep going in circles"
- Analysis paralysis is preventing progress
- Decisions are being repeatedly delayed
- Teams cannot reach consensus
- Morale is suffering from indecision
- Perfectionism is blocking good-enough action

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **decision_context** | Yes | What decision needs to be made |
| **information_available** | Yes | What we know now |
| **stakeholders** | No | Who is involved in or affected by the decision |
| **delay_costs** | No | What is being lost by not deciding |
| **reversibility** | No | Can this decision be undone or adjusted later? |

---

## Workflow

### Step 1: Diagnose the Paralysis

**Why are we stuck?**

| Paralysis Type | Symptoms | Root Cause |
|---------------|----------|------------|
| Information addiction | "We need more data" (repeatedly) | Fear of being wrong |
| Consensus seeking | "Not everyone agrees" | Conflict avoidance |
| Perfectionism | "It's not ready" | Fear of imperfection |
| Scope creep | "What about X?" (endless additions) | Lack of boundaries |
| Authority confusion | "Who decides?" | Unclear decision rights |
| Analysis loops | Same discussion, different meeting | No decision framework |

### Step 2: Apply the Decision Readiness Test

**The 70% Rule:** If you have 70% of the information you wish you had, you have enough to decide.

**Readiness Questions:**
1. Do we understand the core problem? (Yes/No)
2. Do we know the main options? (Yes/No)
3. Do we understand the key tradeoffs? (Yes/No)
4. Will waiting materially improve our information? (Yes/No/Uncertain)
5. What is the cost of delay? (Specific answer required)

**If answers are Yes, Yes, Yes, No, and you can articulate delay cost:** Decide now.

### Step 3: Set a Decision Deadline

**The Iger Principle:** All decisions can and should be made in a timely way.

**Deadline Protocol:**
1. Name the decision explicitly
2. Set a specific deadline (date and time)
3. Identify the decision-maker (one person)
4. Define the decision format (what does "decided" look like?)
5. Communicate the deadline to all stakeholders

**Default deadlines:**
- Reversible decisions: 24-48 hours
- Important but adjustable decisions: 1 week
- Major strategic decisions: 2 weeks maximum

### Step 4: Frame the Decision Clearly

**Decision Statement Template:**
"We need to decide [specific question] by [deadline]. The decision-maker is [name]. The options are [A, B, C]. The key tradeoffs are [X vs Y]. We will know we decided when [specific output]."

**Remove false options:**
- Eliminate options no one would actually choose
- Combine options that are essentially the same
- Identify the real choice (often binary)

### Step 5: Decide and Commit

**Decision Meeting Protocol:**
1. Restate the decision question (2 minutes)
2. Present options with tradeoffs (10 minutes maximum)
3. Gather input (bounded time)
4. Decision-maker decides (out loud, documented)
5. Articulate next steps (who does what by when)
6. End meeting immediately after decision

**Post-Decision Rules:**
- No re-litigation without new information
- Disagree and commit
- Review scheduled for [date] to assess and adjust

### Step 6: Build Review Mechanism

**Because decisions can be adjusted:**
- Schedule a review date (not "when we have time")
- Define what would trigger reconsideration
- Make clear that "decided" does not mean "unchangeable forever"

This removes perfectionism pressure: we are deciding what to do NOW, not what is perfect forever.

---

## Outputs

### Decision Protocol Document

```markdown
## Decision Protocol: [Decision Name]

**Current Status:** Stuck since [date]
**Paralysis Type:** [Information addiction / Consensus seeking / etc.]
**Delay Cost:** [Specific impact of continued indecision]

---

## The Decision

**Question:** [Clear, specific question]
**Decision-Maker:** [One person]
**Deadline:** [Date and time]

---

## Options

| Option | Pros | Cons | Reversibility |
|--------|------|------|---------------|
| A: [Name] | [Key pros] | [Key cons] | [Easy/Moderate/Difficult] |
| B: [Name] | [Key pros] | [Key cons] | [Easy/Moderate/Difficult] |

---

## Readiness Assessment

| Question | Answer |
|----------|--------|
| Understand core problem? | [Yes/No] |
| Know main options? | [Yes/No] |
| Understand key tradeoffs? | [Yes/No] |
| Will waiting improve info? | [Yes/No/Uncertain] |
| Cost of delay | [Specific] |

**Verdict:** [Ready to decide / Need specific information: X]

---

## Decision Meeting

**Scheduled:** [Date/Time]
**Duration:** [X minutes maximum]
**Required attendees:** [Names]
**Decision documentation:** [Where it will be recorded]

---

## Post-Decision

**Review date:** [Date]
**Reconsideration triggers:** [What would cause us to revisit]
**Commitment protocol:** Disagree and commit after [deadline]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Decision genuinely needs more information | Identify specific information needed; set bounded timeline to obtain it |
| Stakeholder refuses to commit | Escalate to next authority level; document the blockage |
| Decision-maker is unavailable | Escalate or delegate decision authority |
| Decision gets re-litigated | Point to commitment protocol; require new information to reopen |
| All options seem bad | Reframe as "least bad" choice; indecision is also a choice with costs |

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
Decision context: Whether to launch new product feature in March or delay to June
Information available: 80% of testing complete, positive early results, team divided
Delay costs: Competitor launching similar feature in April
Reversibility: Feature can be rolled back if problems emerge
```

**Output:**

## Decision Protocol: March vs June Feature Launch

**Current Status:** Stuck since January 15
**Paralysis Type:** Consensus seeking + Perfectionism
**Delay Cost:** Competitor launches in April; we lose first-mover advantage

---

## The Decision

**Question:** Do we launch the feature in March or delay to June?
**Decision-Maker:** VP of Product
**Deadline:** January 30, 3:00 PM

---

## Options

| Option | Pros | Cons | Reversibility |
|--------|------|------|---------------|
| A: Launch March | Beat competitor; momentum; learning | 20% testing incomplete; risk | Easy (can roll back) |
| B: Launch June | More testing; polish | Miss competitor; delay learning | N/A |

---

## Readiness Assessment

| Question | Answer |
|----------|--------|
| Understand core problem? | Yes - timing vs. polish tradeoff |
| Know main options? | Yes - March or June |
| Understand key tradeoffs? | Yes - speed vs. completeness |
| Will waiting improve info? | No - remaining 20% is edge cases |
| Cost of delay | Specific: Competitor advantage, 3 months market learning lost |

**Verdict:** Ready to decide. 80% information is sufficient for reversible decision.

---

## Recommendation

**Decide March launch** with rollback plan. Competitive timing matters; feature is reversible; remaining testing is diminishing returns.

---

## Integration

**Source Expert:** Bob Iger
**Complementary Skills:** strategic-priority-framework (to ensure decision aligns with priorities), acquisition-evaluation (for M&A decisions specifically)

---

## Success Criteria

The protocol is successfully applied when:
- [ ] Paralysis type is diagnosed
- [ ] Decision readiness is assessed
- [ ] Clear deadline is set
- [ ] Single decision-maker is named
- [ ] Decision is made by deadline
- [ ] Review mechanism is established
- [ ] Team commits (disagree and commit if needed)