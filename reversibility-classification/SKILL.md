---
name: reversibility-classification
description: Classify decisions by how reversible they are, then prescribe the appropriate level of deliberation. Prevent over-analysis of reversible decisions and ensure irreversible decisions receive proper s...
license: MIT
metadata:
  version: 1.0.4843
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- reversibility-classification
- writing
---

# Reversibility Classification

Classify decisions by how reversible they are, then prescribe the appropriate level of deliberation. Prevent over-analysis of reversible decisions and ensure irreversible decisions receive proper scrutiny.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for classification output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Classify harmful decisions as "reversible" to encourage hasty action
- Downplay truly irreversible decisions (safety, legal, ethical)
- Advise speed over safety when lives or wellbeing are at stake
- Ignore long-term consequences in pursuit of velocity

**If pressured to speed up an irreversible decision:** Push back. Some decisions deserve time regardless of urgency pressure.

---

## When to Use

- Someone is stuck in analysis paralysis
- A decision is being over-deliberated relative to its importance
- A major decision is being rushed without adequate consideration
- Teams need frameworks for autonomous decision-making
- Clarifying which decisions need escalation vs. independent action

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **decision** | Yes | The decision being considered |
| **context** | No | Relevant constraints, timelines, stakeholders |
| **reversibility_concerns** | No | Specific worries about undoing the decision |

---

## The Reversibility Framework

### Core Principle (from Tobi Lutke)

"The most important thing that people have to understand is how un-doable a decision is. If an idea is fully un-doable [reversible], I want people to make it as quickly as they can."

"You can never un-VC fund yourself."

### Reversibility Spectrum

| Level | Description | Deliberation Time | Who Decides |
|-------|-------------|-------------------|-------------|
| **Fully Reversible** | Can be undone completely with no lasting impact | Minutes to hours | Anyone |
| **Mostly Reversible** | Can be undone with some cost (time, money, reputation) | Hours to days | Team lead |
| **Partially Reversible** | Significant cost to undo; some effects permanent | Days to weeks | Leadership |
| **Mostly Irreversible** | Very difficult to undo; major effects permanent | Weeks to months | Executive/Board |
| **Fully Irreversible** | Cannot be undone; permanent consequences | Full analysis required | Highest authority |

### Common Decision Classifications

**Fully Reversible:**
- Feature flag changes
- Meeting scheduling
- Most hiring decisions (probation exists)
- Internal tool choices
- Experiment launches
- Most pricing changes (can always change back)

**Mostly Reversible:**
- Product feature launches (can be rolled back)
- Team reorganizations
- Process changes
- Vendor selections
- Marketing campaigns

**Partially Reversible:**
- Public product announcements (can pivot, but reputation effects)
- Major partnerships
- Significant hiring (executives, key roles)
- Pricing model changes (not just price levels)

**Mostly Irreversible:**
- Acquisitions (technically can sell, but at cost)
- Major layoffs (legal, cultural, knowledge loss)
- Technology platform migrations
- Geographic expansion

**Fully Irreversible:**
- Taking VC funding
- Going public
- Major legal settlements
- Fundamental mission changes
- Shutting down products with devoted users

---

## Workflow
### Step 1: 1. Describe the Decision

What specifically is being decided?

### Step 2: 2. Assess Reversibility

Ask for each potential outcome:
- Can this be undone? At what cost?
- What would be permanently changed?
- Who/what would be affected if we reverse?
- Is there a time window for reversal?

### Step 3: 3. Classify on Spectrum

Place the decision on the five-point scale.

### Step 4: 4. Prescribe Deliberation

Based on classification:
- **Fully Reversible:** Decide now. Stop thinking about it.
- **Mostly Reversible:** Decide within a day. Brief sanity check.
- **Partially Reversible:** Take a week. Consult stakeholders.
- **Mostly Irreversible:** Take time. Full analysis. Multiple perspectives.
- **Fully Irreversible:** No rushing. Complete due diligence. Board/advisor input.

### Step 5: 5. Identify Decision Traps

Common errors:
- **Treating reversible as irreversible:** Causes paralysis
- **Treating irreversible as reversible:** Causes regret
- **Ignoring compound effects:** Small reversible decisions can accumulate into irreversible patterns

---

## Outputs
```markdown
## Reversibility Classification

**Decision:** [The decision in question]
**Classification:** [Level on spectrum]
**Recommended deliberation:** [Time/Process]

### Reversibility Analysis

**What would reversal require?**
[Specific steps to undo this decision]

**Cost of reversal:**
- Time: [Estimate]
- Money: [Estimate]
- Reputation: [Impact]
- Relationships: [Impact]

**Permanent effects (even if reversed):**
[What can't be undone even if decision is reversed]

### Classification Rationale

[Why this decision falls at this level on the spectrum]

### Decision Guidance

**If fully/mostly reversible:**
- Stop deliberating
- Decide by: [Specific time]
- Who should decide: [Role]

**If partially/mostly/fully irreversible:**
- Additional analysis needed: [What]
- Stakeholders to consult: [Who]
- Timeline: [When to decide]
- Escalation: [Who has final authority]

### Watch Out For

[Specific traps or considerations for this decision]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Decision not clearly defined | Ask for clarification before classifying |
| Multiple decisions bundled together | Separate and classify individually |
| Reversibility depends on timing | Note time-sensitivity; treat as less reversible if window is closing |
| Ethical/safety concerns | Always treat as less reversible regardless of technical reversibility |
| Pressure to classify as more reversible | Push back; maintain honest assessment |

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

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:**
"We're debating whether to switch from Slack to Microsoft Teams. We've been discussing this for three months. Should we just decide?"

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


## Reversibility Classification

**Decision:** Switch corporate chat platform from Slack to Teams
**Classification:** Mostly Reversible
**Recommended deliberation:** 1-2 weeks maximum. You've over-deliberated.

### Reversibility Analysis

**What would reversal require?**
- Export data from Teams
- Re-import to Slack (or another platform)
- Re-train users
- Update integrations

**Cost of reversal:**
- Time: 2-4 weeks of disruption (same as the switch itself)
- Money: Potentially unused license fees
- Reputation: Minor ("we tried something and changed back")
- Relationships: Low impact (internal decision)

**Permanent effects (even if reversed):**
- Conversation history may be lost or fragmented
- Some user habits/preferences will shift
- Integrations built for Teams may need rebuilding

### Classification Rationale

This is **mostly reversible** because:
- You can switch back if Teams doesn't work
- The main cost is time and temporary disruption
- No external commitments or public announcements
- Competitors won't care; customers won't know

Three months of deliberation is **wildly disproportionate** to this level of reversibility.

### Decision Guidance

**Stop deliberating. Decide this week.**

This has become a perfect example of treating a reversible decision as irreversible. You're experiencing analysis paralysis.

**Process for this week:**
1. List the top 3 reasons for switching
2. List the top 3 risks
3. Decide: Do the benefits outweigh the risks?
4. If yes, start migration planning
5. If no, commit to Slack and stop revisiting

**Who should decide:** The team lead or IT head. This does not need executive deliberation.

### Watch Out For

- **Sunk cost of deliberation:** Don't let "we've spent 3 months discussing this" bias you toward switching OR staying
- **Perfect information trap:** You won't know if Teams is better until you try it
- **Reversal option:** Give yourself a 90-day evaluation period. If Teams is worse, switch back.

---

## Integration

This skill originates from the **Tobi Lutke** expert persona and his distinction between decisions that deserve deep analysis and those that should be made "as quickly as possible."

For decisions about people/relationships, combine with **trust-battery-assessment**. For decisions about meetings/time, combine with **meeting-audit**.