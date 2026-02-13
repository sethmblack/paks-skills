---
name: facts-changed-audit
description: Systematically review whether facts underlying a current position have changed, warranting a position change.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3973
repository: https://github.com/sethmblack/paks-skills
keywords:
- facts-changed-audit
- transformation
- writing
---

# Facts Changed Audit

Systematically review whether facts underlying a current position have changed, warranting a position change.

---

## When to Use

- Defending a decision to change your mind
- Questioning whether to maintain or update a position
- Reviewing strategies, beliefs, or commitments over time
- Fighting both rigidity (never changing) and inconsistency (changing too easily)
- User asks "Should I change my position?" or "Have the facts changed?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| current_position | Yes | Your existing stance, strategy, or belief |
| original_reasoning | Yes | Why you held/hold this position |
| new_information | Yes | What has changed or emerged since |

---

## Keynes's Principle

The most famous quote attributed to Keynes:

> "When the facts change, I change my mind. What do you do, sir?"

This was reportedly his response when criticized for inconsistency in his policy recommendations.

### The Deeper Wisdom

Keynes understood two failure modes:

**Rigidity:** Maintaining positions because you've always held them, even when evidence demands revision. This is stubbornness masquerading as principle.

**Inconsistency:** Changing positions based on mood, social pressure, or random fluctuation. This is spinelessness masquerading as flexibility.

The goal is **principled flexibility:** changing when and only when the facts warrant it.

### The Related Insight

> "The difficulty lies not so much in developing new ideas as in escaping from old ones."

Often the hardest part is not seeing the new truth - it's releasing the old belief that made sense before.

---

## The Audit Framework

### Step 1: Reconstruct Original Reasoning

| Element | Original | Still Valid? |
|---------|----------|--------------|
| Key assumption 1 | [What you assumed] | [Y/N/Partially] |
| Key assumption 2 | [What you assumed] | [Y/N/Partially] |
| Key evidence 1 | [What you relied on] | [Still holds?] |
| Key evidence 2 | [What you relied on] | [Still holds?] |
| Predicted outcome | [What you expected] | [Happened?] |

### Step 2: Identify What Has Changed

| Change Type | Before | After | Material? |
|-------------|--------|-------|-----------|
| New information | [Didn't know X] | [Now know X] | [Y/N] |
| Changed circumstances | [Context was Y] | [Context is now Z] | [Y/N] |
| Failed predictions | [Expected A] | [Got B instead] | [Y/N] |
| New options | [Only had choices C, D] | [Now have E] | [Y/N] |

### Step 3: Test Materiality

Not all changes warrant position changes. Ask:

1. **Is this change fundamental or peripheral?**
   - Did the core logic depend on what changed?
   - Or is this a minor detail the position can absorb?

2. **Is this change durable or temporary?**
   - Has the world changed, or just today's data?
   - Will this look the same in a year?

3. **Would you have decided differently with this information?**
   - If you knew then what you know now, would you have chosen differently?
   - This is the crucial test.

### Step 4: Assess Costs of Change vs. Staying

| Factor | Cost of Changing | Cost of Staying |
|--------|------------------|-----------------|
| Reputation | [Perceived inconsistency?] | [Perceived stubbornness?] |
| Resources | [Switching costs] | [Opportunity costs] |
| Relationships | [Trust impact] | [Trust impact] |
| Outcome risk | [New position may be wrong too] | [Current position increasingly wrong] |

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Facts Changed Audit

### Current Position
[Your existing stance]

### Original Reasoning
[Why you took this position]

### Key Assumptions Check

| Assumption | Original | Current Status | Material? |
|------------|----------|----------------|-----------|
| [Assumption 1] | [What you believed] | [Valid/Invalid/Changed] | [Y/N] |
| [Assumption 2] | [What you believed] | [Valid/Invalid/Changed] | [Y/N] |

### Evidence Check

| Evidence | Original | Current Status | Material? |
|----------|----------|----------------|-----------|
| [Evidence 1] | [What you relied on] | [Confirmed/Contradicted/Evolved] | [Y/N] |
| [Evidence 2] | [What you relied on] | [Confirmed/Contradicted/Evolved] | [Y/N] |

### Material Changes Identified
[List the changes that actually matter]

### The Keynes Test
If you knew then what you know now, would you have decided differently?
[YES / NO / UNCLEAR]

### Verdict: [FACTS CHANGED - UPDATE POSITION / FACTS STABLE - MAINTAIN POSITION / MIXED - PARTIAL UPDATE]

### Recommended Action
[Specific guidance based on verdict]

### If Changing: New Position
[What the revised position should be]

### If Maintaining: Why This Isn't Rigidity
[Why staying is principled, not stubborn]

### The Keynesian Verdict
[Summary of the audit conclusion]
```

---

## Common Patterns

### False Change (Noise Disguised as Signal)
- New data point doesn't actually contradict the thesis
- Short-term fluctuation within expected variance
- Information that seems new but was already priced into the original reasoning

**Verdict:** Maintain position. This is discipline, not rigidity.

### Real Change (Signal Disguised as Noise)
- Rationalization: "This is just a temporary setback"
- Denial: "The fundamentals haven't changed" (but they have)
- Sunk cost: "I've invested too much to change now"

**Verdict:** Change position. This is adaptation, not inconsistency.

### Gradual Drift
- No single dramatic change
- Cumulative small changes that collectively transform the situation
- Easy to miss because no individual change triggered review

**Verdict:** Periodic audits are necessary precisely because of gradual drift.

### Changed You, Not Changed Facts
- Your risk tolerance has changed
- Your time horizon has changed
- Your priorities have changed
- The facts are the same; you are different

**Verdict:** This is also a valid reason to change position, but be honest about what changed.

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "A year ago I decided not to take a job offer from Company X because they were a struggling startup with uncertain funding. Now they've raised a massive Series C, tripled in size, and want me to interview again. My friends say I should reconsider, but I already made my decision. Should I change my mind?"

**Output:**

## Facts Changed Audit

### Current Position
Not pursuing employment at Company X (decision made one year ago)

### Original Reasoning
- Company was an early-stage startup with uncertain funding
- Risk of company failure was significant
- Career risk was unacceptably high given alternatives

### Key Assumptions Check

| Assumption | Original | Current Status | Material? |
|------------|----------|----------------|-----------|
| Funding uncertain | High risk of running out of money | Series C raises significantly de-risks | YES |
| Company might fail | Meaningful probability of failure | Much lower now with proven traction | YES |
| Team unproven | Small team, unknown execution ability | Tripled size, demonstrated scaling | YES |
| Role was risky | Joining early = high variance outcome | Joining post-Series C = different profile | YES |

### Evidence Check

| Evidence | Original | Current Status | Material? |
|----------|----------|----------------|-----------|
| Funding stage | Seed/Series A, uncertain runway | Series C, significant runway | YES - Contradicts original concern |
| Company size | Small, early stage | Tripled in size | YES - Different company now |
| Market validation | Unproven | Sufficient to raise major round | YES - Evidence of viability |

### Material Changes Identified

1. **Funding risk materially reduced:** Series C fundamentally changes the survival probability
2. **Company has proven execution:** Tripling size demonstrates ability to scale
3. **Role profile has changed:** This is no longer an "early startup" job; it's a growth-stage company

### The Keynes Test
If you knew then what you know now, would you have decided differently?

**LIKELY YES.** Your original objection was risk from funding uncertainty and company viability. Both have materially changed. The company that wants to interview you is not the same company you declined.

### Verdict: FACTS CHANGED - UPDATE POSITION

### Recommended Action

1. **Take the interview.** You're not reconsidering the same job - you're considering a different opportunity at a transformed company.

2. **Evaluate fresh.** Don't let your past decision anchor your current evaluation. The question is: "Is this opportunity good NOW?" not "Was I wrong before?" (You weren't wrong before - you were right given what you knew.)

3. **Don't conflate consistency with correctness.** Refusing to reconsider because "I already decided" is not principled - it's treating your past self as infallible.

### If Changing: New Position
Actively pursue the interview and evaluate the opportunity on its current merits, not its historical baggage.

### If Maintaining: Why This Isn't Rigidity
N/A - The facts warrant change.

### The Keynesian Verdict

"When the facts change, I change my mind. What do you do, sir?"

The facts have changed. The company you declined no longer exists - it has been replaced by a larger, better-funded, de-risked version of itself. Your decision not to pursue was correct GIVEN THE INFORMATION YOU HAD. It would be incorrect to maintain that decision now that the information has changed.

Consistency is not a virtue when it means ignoring reality. The difficulty lies not in developing new ideas but in escaping from old ones - including the old idea that you already decided this.

You did decide. And you decided correctly. Now you have a new decision to make, with new information. Make it.

---

## Integration

This skill is part of the **John Maynard Keynes** expert persona. Use it to navigate between the twin failures of stubborn rigidity and unprincipled flexibility.