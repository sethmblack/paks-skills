---
name: failure-analysis-systems
description: Analyze failures by examining systems rather than blaming individuals—distinguishing errors of ignorance from errors of ineptitude. Based on Atul Gawande's methodology.
version: 1.0.0
author: sethmblack
tags: [failure-analysis-systems, writing]
---

# Failure Analysis Systems

Analyze failures by examining systems rather than blaming individuals—distinguishing errors of ignorance from errors of ineptitude. Based on Atul Gawande's methodology.

---

## When to Use

- Something went wrong and you need to understand why
- Temptation to blame an individual
- Same failures keep recurring
- Need to prevent future failures
- Building a culture of learning from mistakes

**Trigger Phrases:**
- "Why does this keep happening?"
- "Whose fault is this?"
- "We need to hold someone accountable"
- "The same mistake keeps occurring"
- "How do we prevent this in the future?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| failure | Yes | What went wrong |
| immediate_cause | No | What directly caused the failure |
| individuals_involved | No | People who were involved |
| context | No | Circumstances surrounding the failure |

---

## Core Principle

> "We are not built for discipline. We are built for novelty and excitement, not for careful attention to detail."
> — Atul Gawande

**Two types of errors:**

| Type | Definition | Example | Solution |
|------|------------|---------|----------|
| **Errors of ignorance** | We don't know enough | New surgeon lacks skills | Training, education |
| **Errors of ineptitude** | We don't properly use what we know | Experienced surgeon skips step | Systems, checklists |

Most failures in complex environments are errors of ineptitude—not lack of knowledge, but failure to consistently apply knowledge. **The system, not the individual, is usually the right target for intervention.**

---

## Workflow
### Step 1: Resist the Blame Reflex

When something goes wrong, the instinct is to find who's responsible. Resist this.

**Problems with individual blame:**
- It stops the analysis too early
- It doesn't prevent recurrence
- It creates fear that hides future problems
- It misses systemic factors

**Instead ask:** "What in the system allowed or encouraged this failure?"

### Step 2: Classify the Error Type

**Is this an error of ignorance?**
- Did the person lack the knowledge or skill?
- Was this their first time with this situation?
- Was there no way they could have known?

If yes → Solution is training, education, experience

**Is this an error of ineptitude?**
- Did the person have the knowledge but fail to apply it?
- Is this a known step that got skipped?
- Would a checklist have caught it?

If yes → Solution is systems, processes, checklists

### Step 3: Map the System

Don't just look at the moment of failure. Map the full system:

**Upstream factors:**
- What happened before that contributed?
- What decisions led to this situation?
- What information was available or missing?

**Environmental factors:**
- Was the person rushed?
- Were they interrupted?
- Were there competing priorities?
- Was the environment set up for success?

**Systemic factors:**
- Is there a checklist for this?
- Is there a forcing function?
- Are there too many steps to reliably remember?
- Are handoffs clear?

### Step 4: Find the Leverage Point

**Ask:** Where could a system change have prevented this?

Often it's not at the moment of failure but earlier:
- The surgeon's error happened in the OR, but the prevention was in pre-surgery prep
- The deployment crash happened at release, but the prevention was in the CI/CD pipeline
- The customer complaint happened at delivery, but the prevention was in order entry

### Step 5: Design the System Fix

Based on the error type and leverage point:

| Finding | Intervention |
|---------|--------------|
| Knowledge gap | Training, documentation, mentorship |
| Step gets skipped | Checklist, forcing function |
| Handoff failure | Communication protocol, confirmation |
| Environmental pressure | Workload management, protected time |
| No feedback loop | Measurement, review process |

### Step 6: Test the Fix

Don't assume the intervention works. Test it:
- Does the failure recur?
- Are there unintended consequences?
- Is the fix actually being used?

---

## The "Blameless Postmortem" Structure

**1. What happened?**
Timeline of events, facts only, no judgments

**2. What was the impact?**
Consequences of the failure

**3. What was the immediate cause?**
The direct trigger (not the person—the action or absence)

**4. What system factors contributed?**
Upstream, environmental, and systemic factors

**5. What type of error was this?**
Ignorance or ineptitude

**6. Where is the leverage point?**
The best place to intervene

**7. What change will we make?**
Specific, testable intervention

**8. How will we know it worked?**
Measurement and timeline

---

## Outputs

| Output | Description |
|--------|-------------|
| Error classification | Ignorance vs. ineptitude |
| System map | Factors that contributed to failure |
| Leverage point | Where intervention is most effective |
| System fix | Specific change to prevent recurrence |
| Success metrics | How to know if fix works |

---



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

**User:** "Our engineer pushed code that took down production. It was Friday at 5pm and they didn't run the full test suite. Should we put them on a performance plan?"

**Failure Analysis response:**

Let's analyze the system before deciding about the individual.

**Step 1: Resist blame**
Your engineer made a mistake. But the question is: why was it possible for this mistake to happen?

**Step 2: Classify the error**
This is an error of ineptitude, not ignorance. The engineer knows they should run tests. They didn't do what they knew to do.

**Step 3: Map the system**

*Upstream factors:*
- Why was deployment happening at 5pm Friday?
- Was there pressure to ship before the weekend?
- Who requested this timing?

*Environmental factors:*
- Was the engineer rushed?
- Were they tired?
- Friday 5pm is known high-risk time for deployments

*Systemic factors:*
- Can code be pushed without tests passing?
- Is there a deploy checklist?
- Is there a "no Friday deploys" policy?
- Does CI/CD require full test suite?

**Step 4: Find the leverage point**

The leverage point is not "engineer runs tests"—that relies on human memory under pressure.

The leverage point is: **Make it impossible to deploy without passing tests.**

**Step 5: Design the fix**

| Problem | System Fix |
|---------|------------|
| Tests can be skipped | CI/CD requires passing tests to deploy |
| Friday deploys are risky | Freeze deploys Friday after 2pm |
| No checklist | Deploy checklist with pause points |
| No peer review | Require approval for production deploys |

**Step 6: About the individual**

Before putting them on a performance plan, ask:
- Have you set them up to succeed?
- Could a conscientious person have made this mistake in this system?

If your system allows deploying without tests, the system is the problem. Fix the system first. If they circumvent a good system, that's a different conversation.

**The principle:** Individuals operating in bad systems will produce bad outcomes. Fix the system.

---

## Integration

This skill pairs with:
- **checklist-design** - Create checklists at leverage points
- **positive-deviance-analysis** - Learn from teams that don't have these failures
- **hard-conversation-framework** - When individual issues do need addressing

---

## Constraints

- Some failures are genuinely individual (malice, repeated negligence)
- System fixes take time; may need interim measures
- Cultural shift required for blameless analysis
- Not all failures are preventable

---

## Source Expert

Atul Gawande - `experts/atul-gawande/`