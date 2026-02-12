---
name: five-step-algorithm
description: 'Systematically improve any product, process, or system by following
  Elon Musk''s strict sequence: question requirements, delete, simplify, accelerate,
  automate.'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- five-step-algorithm
- writing
---

# Five-Step Algorithm

Systematically improve any product, process, or system by following Elon Musk's strict sequence: question requirements, delete, simplify, accelerate, automate.

---

## When to Use

- Optimizing a manufacturing process
- Reducing costs in a product or service
- Improving team or organizational workflows
- Any situation where someone says "make this more efficient"
- User asks "Apply the algorithm" or "How do I make this better/faster/cheaper?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| process_or_product | Yes | What you're trying to improve |
| current_state | Yes | How it works now (steps, parts, timeline) |
| goal | No | Specific improvement target (cost, speed, quality) |

---

## The Algorithm

Musk calls this "the algorithm"—a distillation of manufacturing wisdom from Tesla and SpaceX. The power lies in the **strict ordering**. You must complete earlier steps before moving to later ones.

### Step 1: Question the Requirements

**"Make the requirements less dumb."**

- Every requirement is suspect until proven necessary
- Requirements from smart people are especially dangerous—you may not question them enough
- Each requirement must have a **name attached** (not a department)
- Ask: "Who originally requested this? Why? Is the reason still valid?"

**Key questions:**
- Why does this requirement exist?
- What happens if we don't meet it?
- Is this a true constraint or a preference?
- Who owns this requirement? Can we talk to them?

**Warning signs of bad requirements:**
- "It's always been done this way"
- "Legal/compliance requires it" (but no specific person can explain why)
- "The customer expects it" (but no actual customer data)
- Requirements from departments, not individuals

### Step 2: Delete Parts or Processes

**"If you're not adding back at least 10% of what you delete, you didn't delete enough."**

- The bias is always toward adding things "just in case"
- Fight this bias ruthlessly
- It's easier to add something back than to delete something that shouldn't exist
- Deletion is the highest-leverage improvement

**Key questions:**
- What would break if we removed this entirely?
- When was this last actually needed?
- Is this a dependency or just a comfort?
- Can we run a test without this?

**Deletion targets:**
- Steps that exist "for documentation"
- Approvals that have never blocked anything
- Parts added for edge cases that haven't occurred
- Reports no one reads

### Step 3: Simplify and Optimize

**"The most common error of a smart engineer is to optimize something that should simply not exist."**

- Only simplify what remains after deletion
- Resist the urge to make unnecessary things better
- Look for ways to combine steps or parts
- Reduce variation and special cases

**Key questions:**
- Can two steps become one?
- Can multiple parts be consolidated?
- Is there a simpler way to achieve the same outcome?
- What would a beginner find confusing?

**Warning:** If you find yourself optimizing, check whether you should delete instead.

### Step 4: Accelerate Cycle Time

**"Every process can be speeded up. But only do this after you have followed the first three steps."**

- Speed of iteration beats perfection of any single iteration
- Look for bottlenecks and constraints
- Parallelize where possible
- Reduce wait times and handoffs

**Key questions:**
- What's the current cycle time?
- Where do things wait?
- What could be done in parallel?
- What's the theoretical minimum time?

**Warning:** If you accelerate a process that should be deleted, you're being efficient at something useless.

### Step 5: Automate

**"Most people start with Step 5, and they automate a process that never should have existed in the first place."**

- Automation is powerful but should be LAST
- Never automate before questioning, deleting, and simplifying
- Automation locks in the current process—make sure it's the right process
- Consider partial automation where full automation is overkill

**Key questions:**
- Have we completed steps 1-4?
- Is this process stable enough to automate?
- What's the cost of automation vs. the benefit?
- Can we automate partially?

---

## Critical Warning

**Musk on his own mistakes:** "I have personally made the mistake of going backwards on all five steps multiple times. In making Tesla's Model 3, I literally automated, accelerated, simplified and then deleted."

The most common error pattern:
1. See a problem
2. Jump to automation (Step 5)
3. Realize the process is wrong
4. Have to undo expensive automation
5. Finally question and delete

**The algorithm prevents this by enforcing order.**

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
## Five-Step Algorithm Analysis

### Target
[What's being improved]

### Current State
[Brief description of current process/product]

---

### Step 1: Question Requirements

**Requirements identified:**
1. [Requirement] - Owner: [Name] - Status: [Valid/Questionable/Delete]
2. [Requirement] - Owner: [Name] - Status: [Valid/Questionable/Delete]
3. [Requirement] - Owner: [Name] - Status: [Valid/Questionable/Delete]

**Requirements to challenge:**
- [Requirement]: [Why it should be questioned] - Action: [What to do]

**Requirements validated as necessary:**
- [Requirement]: [Why it's actually needed]

---

### Step 2: Delete

**Candidates for deletion:**
| Item | Last Actually Needed | What Breaks Without It | Recommendation |
|------|---------------------|------------------------|----------------|
| [Part/step] | [When] | [Impact] | Delete/Keep/Test |

**Deletions to implement:**
1. [Item] - Rationale: [Why]
2. [Item] - Rationale: [Why]

**Expected savings from deletion:** [Time/cost/complexity reduction]

---

### Step 3: Simplify and Optimize

**After deletion, what remains:**
[Simplified process/product description]

**Simplification opportunities:**
1. [Current] → [Simplified] - Benefit: [What improves]
2. [Current] → [Simplified] - Benefit: [What improves]

**Consolidation opportunities:**
- [Multiple items] → [Single item]

---

### Step 4: Accelerate

**Current cycle time:** [Time]
**Bottlenecks identified:**
1. [Bottleneck] - Cause: [Why] - Solution: [How to speed up]
2. [Bottleneck] - Cause: [Why] - Solution: [How to speed up]

**Parallelization opportunities:**
- [Steps that could run in parallel]

**Target cycle time:** [New time]

---

### Step 5: Automate

**Automation candidates (ONLY after steps 1-4):**
| Process | Stability | ROI | Recommendation |
|---------|-----------|-----|----------------|
| [Process] | High/Med/Low | [Estimate] | Automate/Partial/Manual |

**Automation plan:**
1. [What to automate] - Timeline: [When]
2. [What to keep manual] - Reason: [Why]

---

### Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Steps/Parts | [N] | [N] | [%] |
| Cycle Time | [Time] | [Time] | [%] |
| Cost | [Cost] | [Cost] | [%] |

### Next Actions
1. [Immediate action]
2. [Short-term action]
3. [Longer-term action]
```

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

**Input:** "Our code review process takes 3-5 days and engineers are frustrated. How do we speed it up?"

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


## Five-Step Algorithm Analysis

### Target
Code review process

### Current State
- Engineer submits PR
- Assigned to reviewer based on rotation
- Reviewer has 24 hours to start review (policy)
- Review comments go back and forth (avg 2.3 rounds)
- Final approval required from tech lead
- Merge requires green CI and approval
- Average time: 3-5 days

---

### Step 1: Question Requirements

**Requirements identified:**
1. 24-hour start SLA - Owner: Engineering Manager (from 2019) - Status: Questionable
2. Tech lead approval for all PRs - Owner: CTO (2018 security incident) - Status: Questionable
3. Full CI suite must pass - Owner: QA team - Status: Valid
4. Assigned reviewer system - Owner: Unknown - Status: Questionable

**Requirements to challenge:**
- **24-hour SLA:** Creates batching behavior. Reviewers wait until deadline. Action: Talk to Eng Manager about whether this helps or hurts.
- **Tech lead approval for ALL PRs:** Security incident was 6 years ago. Is blanket approval still needed? Action: Get data on what % of PRs tech leads actually change.
- **Assigned reviewer:** Why can't anyone review? Action: Understand original rationale.

**Requirements validated as necessary:**
- CI passing: Real quality gate with demonstrated value

---

### Step 2: Delete

**Candidates for deletion:**
| Item | Last Actually Needed | What Breaks Without It | Recommendation |
|------|---------------------|------------------------|----------------|
| Tech lead approval (small PRs) | Rarely changes outcome | Nothing for <100 lines | Delete for small PRs |
| Assigned reviewer system | — | Anyone could review | Delete, allow self-selection |
| 24-hour SLA | Creates wrong incentive | Faster reviews if removed | Delete |
| Multiple review rounds | Shows unclear requirements | Better first-pass reviews | Reduce |

**Deletions to implement:**
1. Remove tech lead approval for PRs under 100 lines (covers 60% of PRs)
2. Remove assigned reviewer—anyone can pick up any review
3. Remove 24-hour SLA—replace with "same day" culture expectation

**Expected savings from deletion:** 1-2 days average

---

### Step 3: Simplify and Optimize

**After deletion, what remains:**
- Engineer submits PR
- Any available reviewer picks it up
- One round of review (target)
- Tech lead approval only for large PRs
- CI passes
- Merge

**Simplification opportunities:**
1. Review rounds (2.3 → 1): Create PR template with checklist; reviewer blocks only for real issues
2. Large PR threshold: Clear definition (>100 lines OR touches auth/payments)

---

### Step 4: Accelerate

**Current cycle time:** 3-5 days
**Bottlenecks identified:**
1. Waiting for reviewer pickup - Cause: Batching behavior - Solution: Slack notification for open PRs
2. Back-and-forth rounds - Cause: Nitpicking - Solution: "LGTM with comments" option
3. Tech lead availability - Cause: Single person - Solution: 2-3 designated approvers

**Parallelization opportunities:**
- Review and CI can run in parallel (already happening)

**Target cycle time:** <1 day for small PRs, <2 days for large PRs

---

### Step 5: Automate

**Automation candidates (ONLY after steps 1-4):**
| Process | Stability | ROI | Recommendation |
|---------|-----------|-----|----------------|
| PR size classification | High | High | Automate—tag as small/large automatically |
| Reviewer notification | High | Medium | Automate—Slack bot for waiting PRs |
| Auto-merge on approval | Medium | Low | Partial—only for small PRs with green CI |

**Automation plan:**
1. PR size tagging via GitHub Action - Timeline: This week
2. Keep manual review selection—builds ownership

---

### Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Required approvals (small PR) | 2 | 1 | 50% |
| Average rounds | 2.3 | 1.5 | 35% |
| Cycle Time (small) | 3-5 days | <1 day | 70-80% |
| Cycle Time (large) | 3-5 days | <2 days | 50%+ |

### Next Actions
1. **Today:** Talk to CTO about tech lead approval history and data
2. **This week:** Remove 24-hour SLA, announce "same day" culture
3. **Next week:** Implement PR size auto-tagging

---

## Integration

This skill is part of the **Elon Musk** expert persona. Use it to systematically improve anything—but always in the right order.