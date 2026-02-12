---
name: root-cause-diagnosis
description: Trace any problem to its root cause by distinguishing symptoms from causes
  and identifying whether it's a people problem or a machine (process/system) problem.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- root-cause-diagnosis
- writing
---

# Root Cause Diagnosis

Trace any problem to its root cause by distinguishing symptoms from causes and identifying whether it's a people problem or a machine (process/system) problem.

---

## When to Use

- A problem keeps recurring despite attempts to fix it
- User asks "Why does this keep happening?"
- Need to understand what's really causing an issue
- Treating symptoms hasn't resolved the underlying problem
- Analyzing a failure to prevent recurrence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The symptom or issue being experienced |
| history | No | How often this happens, previous attempts to fix it |
| context | No | People involved, processes in place, relevant circumstances |

---

## The Framework

### Core Principle

Most problems people try to solve are symptoms, not root causes. Treating symptoms provides temporary relief but the problem returns. Root causes, when addressed, eliminate the problem at its source.

**Dalio's insight:** "Distinguish symptoms from causes—and treat the causes. Don't just fix problems as they occur; prevent them from recurring by addressing their root causes."

### Step 1: Define the Problem Clearly

Be precise about what's actually happening.

**Questions to clarify:**
- What specifically is the problem? (observable behavior or outcome)
- When does it occur?
- How often does it occur?
- What's the impact?

**Avoid:**
- Vague descriptions ("things aren't working")
- Assumed causes stated as problems ("the team isn't motivated" is a cause, not a symptom)
- Multiple problems conflated into one

### Step 2: Trace the Cause-and-Effect Chain

Use the "5 Whys" technique—ask "Why?" repeatedly until you reach something actionable.

**Process:**
1. State the problem
2. Ask: Why did this happen?
3. Answer, then ask: Why did THAT happen?
4. Continue until you reach a root cause
5. A root cause is something you can directly address that will prevent the problem

**Example:**
- Problem: We missed the deadline
- Why? The final review took longer than expected
- Why? We found significant errors that needed fixing
- Why? The errors weren't caught earlier
- Why? We don't have a review process before final stage
- Root cause: **Missing intermediate review process**

### Step 3: Classify: People vs. Machine

This is critical for choosing the right solution.

**People Problem:**
The issue stems from the individual(s) involved:
- Skill gap: They don't know how to do it
- Will gap: They don't want to do it (motivation, engagement)
- Fit gap: They're not right for this role/task
- Judgment gap: They made a poor decision

**Machine Problem:**
The issue stems from the system/process:
- Missing process: No defined way to do this
- Flawed process: The process doesn't work
- Missing guardrails: No checks to catch errors
- Wrong tools: Technology doesn't support the need
- Incentive misalignment: System rewards wrong behavior

**Both:**
Often problems are a combination. A person made an error AND the system didn't catch it.

**Dalio's insight:** "Don't blame bad outcomes on anyone until you've looked at the machine that created those outcomes. If the machine is good, but the person operating it isn't, you have a people problem. If good people are operating a bad machine, you have a machine problem."

### Step 4: Validate the Root Cause

Before designing solutions, confirm you've found the actual root cause.

**Validation questions:**
- If we address this, will the problem be eliminated (not just reduced)?
- Is this cause within our control to change?
- Does this explain why the problem recurs?
- Would others who examine the evidence reach the same conclusion?

### Step 5: Design the Solution

Match the solution to the root cause type.

**For People Problems:**
| Root Cause | Solution Type |
|------------|---------------|
| Skill gap | Training, coaching, resources |
| Will gap | Motivation conversation, incentive adjustment, or removal |
| Fit gap | Move to different role or remove |
| Judgment gap | Better frameworks, mentorship, or role reassessment |

**For Machine Problems:**
| Root Cause | Solution Type |
|------------|---------------|
| Missing process | Create and document process |
| Flawed process | Redesign process |
| Missing guardrails | Add checks, reviews, automation |
| Wrong tools | Evaluate and implement better tools |
| Incentive misalignment | Restructure incentives |

---

## Output Format

```markdown
## Root Cause Diagnosis: [Problem Name]

### Problem Definition
**Symptom:** [What's actually happening—observable]
**Frequency:** [How often]
**Impact:** [Why this matters]

### Cause-and-Effect Chain
1. **Symptom:** [The problem as observed]
2. **Why?** [First-level cause]
3. **Why?** [Second-level cause]
4. **Why?** [Third-level cause]
5. **Root Cause:** [The fundamental, actionable cause]

### Classification
**Type:** [People Problem / Machine Problem / Both]

**If People Problem:**
- Whose? [Who is involved]
- What type? [Skill / Will / Fit / Judgment]
- Evidence: [Why you believe this]

**If Machine Problem:**
- Which system/process? [Identify it]
- What's wrong with it? [Missing / Flawed / No guardrails / Wrong tools / Misaligned incentives]
- Evidence: [Why you believe this]

### Validation
- [ ] Addressing this will eliminate (not just reduce) the problem
- [ ] This cause is within our control
- [ ] This explains the pattern of recurrence
- [ ] Others would reach the same conclusion from evidence

### Recommended Solution
**Solution:** [Specific action to address root cause]
**Why this addresses the root cause:** [Explanation of the link]
**Expected result:** [What should change]
**How to verify:** [How you'll know it worked]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

## Constraints

- Don't accept the first answer—dig deeper
- Don't assume people problems when it might be machine problems (and vice versa)
- Don't design solutions until root cause is validated
- Don't skip the classification step—it determines solution type
- Acknowledge when you need more information to diagnose

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

**Input:** "Our sales team keeps giving customers discounts that hurt our margins. I've told them to stop multiple times but it keeps happening."

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


## Root Cause Diagnosis: Excessive Sales Discounting

### Problem Definition
**Symptom:** Sales team gives discounts that reduce margins below acceptable levels
**Frequency:** Ongoing; has been addressed verbally "multiple times" without resolution
**Impact:** Margin erosion affecting profitability; potentially training customers to expect discounts

### Cause-and-Effect Chain
1. **Symptom:** Sales reps give excessive discounts
2. **Why?** They want to close deals and discounting helps close
3. **Why?** Their incentives reward closed deals, not margin preservation
4. **Why?** Commission structure pays on revenue, not on margin or discount discipline
5. **Root Cause:** **Incentive structure rewards behavior you want to discourage**

### Classification
**Type:** Machine Problem (primarily), with possible People Problem component

**Machine Problem:**
- Which system? Compensation/incentive structure
- What's wrong? Incentive misalignment—salespeople are rationally responding to incentives that reward revenue over margin
- Evidence: "Told them to stop multiple times" but behavior continues = verbal instruction can't override financial incentives

**Possible People Problem:**
- If incentives are restructured and specific individuals still discount excessively, that becomes a people problem (skill in negotiation, or fit for the role)
- But this is secondary—first fix the machine

### Validation
- [x] Addressing incentive misalignment will eliminate (not just reduce) excessive discounting
- [x] Compensation structure is within our control to change
- [x] This explains why verbal instructions haven't worked—they're fighting incentives
- [x] Others would recognize that people respond to incentives

### Recommended Solution

**Solution:** Restructure sales compensation to include margin or discount limits

Options:
1. **Pay on margin, not revenue:** Commission = % of gross margin, not % of revenue
2. **Discount approval gates:** Discounts above X% require manager approval
3. **Discount budget:** Each rep has a quarterly discount budget; exceeding it reduces commission
4. **Margin floor:** Deals below margin floor don't count toward quota

**Why this addresses the root cause:** Salespeople are economic actors. When the incentive structure rewards margin preservation, behavior will shift. No amount of verbal instruction can sustainably override financial incentives.

**Expected result:** Discount frequency and depth should decrease within one quarter of implementation. Some deals may be lost initially, but margin per deal should improve.

**How to verify:**
- Track average discount % before and after change
- Track gross margin per deal
- Track deal close rate (to ensure it doesn't crater)
- Survey sales team for feedback on the new structure

### Note on Implementation
The verbal instruction approach failed because it treated this as a people problem ("they need to stop doing this") when it's actually a machine problem (the system rewards the behavior). This is a common diagnostic error. When people keep doing something despite being told not to, look at what the system is incentivizing.

---

## Integration

This skill is part of the **Ray Dalio** expert persona. Use it when a problem keeps recurring and surface-level solutions haven't worked. The people/machine distinction is particularly valuable for organizational issues.