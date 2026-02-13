---
name: okr-diagnosis
description: Diagnose why an organization's OKR system is not delivering results using John Doerr's Four Superpowers framework and common mistake patterns from *Measure What Matters*.
license: MIT
metadata:
  version: 1.0.4600
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- okr-diagnosis
- writing
---

# OKR Diagnosis

Diagnose why an organization's OKR system is not delivering results using John Doerr's Four Superpowers framework and common mistake patterns from *Measure What Matters*.

**Token Budget:** ~900 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend removing accountability for harmful behavior
- Suggest OKR modifications that would enable unethical practices
- Diagnose systems designed for harmful purposes

**If asked to diagnose harmful systems:** Refuse and explain the concern.

---

## When to Use

- User says "Why aren't our OKRs working?", "Evaluate our OKR system"
- Organization has OKRs but is not seeing results
- Team feels OKR process is bureaucratic overhead
- Goals are set but not driving behavior change
- OKRs are being gamed or ignored

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| okrs | Yes | The existing OKRs to evaluate |
| symptoms | No | Problems or dysfunction being observed |
| context | No | Organization size, industry, OKR maturity |

---

## Workflow

### Step 1: Evaluate Against Four Superpowers

**Superpower 1: Focus and Commit**
- Are there too many OKRs? (Should be 3-5 per level)
- Are priorities clear or is everything "priority one"?
- Can people articulate what the organization says "no" to?
- Is there top-down commitment from leadership?

**Superpower 2: Align and Connect**
- Are OKRs transparent and visible to everyone?
- Do individual OKRs connect to team OKRs connect to company OKRs?
- Are cross-functional dependencies identified and coordinated?
- Do people understand how their work contributes to larger goals?

**Superpower 3: Track for Accountability**
- Are OKRs reviewed regularly (weekly recommended)?
- Is progress data-driven or anecdotal?
- Are off-track OKRs identified early and addressed?
- Is there a grading cadence at end of cycle?

**Superpower 4: Stretch for Amazing**
- Are goals ambitious enough (60-70% confidence)?
- Is there a mix of committed and aspirational OKRs?
- Are people afraid to miss OKRs (indicates coupling with performance reviews)?
- Are "sandbagged" easy goals being set?

### Step 2: Check for Common Mistakes

| Mistake | Symptoms |
|---------|----------|
| Too many OKRs | Diluted focus, everything is priority |
| Committed/Aspirational confusion | Wrong effort allocation |
| Low-Value Objectives | Completed OKRs no one notices |
| Tasks as Key Results | Measuring activity not outcomes |
| Performance review coupling | Fear of stretch goals |
| No re-evaluation | Stale objectives carried forward |

### Step 3: Identify Root Cause

Determine the primary dysfunction:
- Leadership commitment issue
- Structure/design issue
- Process/cadence issue
- Culture/fear issue

### Step 4: Provide Remediation

For each identified issue:
1. Explain the problem clearly
2. Provide specific fix with before/after example
3. Recommend implementation approach
4. Warn about common pitfalls of the fix

---

## Output Format

```markdown
## OKR System Diagnosis

### Summary
[One paragraph summarizing overall health and primary issues]

### Superpower Assessment

| Superpower | Status | Key Finding |
|------------|--------|-------------|
| Focus & Commit | Red/Yellow/Green | [Finding] |
| Align & Connect | Red/Yellow/Green | [Finding] |
| Track | Red/Yellow/Green | [Finding] |
| Stretch | Red/Yellow/Green | [Finding] |

### Issues Identified

#### Issue 1: [Name]
**Symptoms:** [What is being observed]
**Root Cause:** [Why this is happening]
**Impact:** [Consequences of not fixing]
**Fix:** [Specific remediation]

**Before:** [Example of current problematic OKR]
**After:** [Example of fixed OKR]

[Repeat for each issue]

### Priority Remediation Plan

1. [First action - highest impact]
2. [Second action]
3. [Third action]

### Expected Timeline
[How long to see improvement with these fixes]
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

**Input:**
```
OKRs:
- Objective: Be the best company
  - KR1: Make customers happy
  - KR2: Hire great people
  - KR3: Innovate

Symptoms: Nobody looks at OKRs after Q1 planning
```

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


## OKR System Diagnosis

### Summary
This OKR system is fundamentally broken due to vague, unmeasurable key results and no tracking cadence. The OKRs are functioning as aspirational slogans rather than operational tools. Immediate restructuring required.

### Superpower Assessment

| Superpower | Status | Key Finding |
|------------|--------|-------------|
| Focus & Commit | Yellow | Only 1 objective, but too vague to drive focus |
| Align & Connect | Red | Cannot align to unmeasurable goals |
| Track | Red | No tracking because nothing is measurable |
| Stretch | Yellow | Unknown - goals too vague to assess ambition |

### Issues Identified

#### Issue 1: Unmeasurable Key Results
**Symptoms:** "Make customers happy" has no number, no baseline, no target
**Root Cause:** Confusion between objectives and key results; KRs written as objectives
**Impact:** No way to know if making progress; no accountability
**Fix:** Rewrite each KR with specific metric, baseline, target, and date

**Before:** KR1: Make customers happy
**After:** KR1: Increase NPS from 42 to 60 by end of Q2

#### Issue 2: No Tracking Cadence
**Symptoms:** OKRs forgotten after planning
**Root Cause:** No structured review process; OKRs not integrated into regular meetings
**Impact:** OKRs become shelf-ware; no course correction
**Fix:** Institute weekly 15-minute OKR check-in; appoint OKR shepherd

### Priority Remediation Plan

1. Rewrite all KRs with specific metrics (this week)
2. Appoint OKR shepherd to own the process
3. Add OKR review to weekly leadership meeting
4. End of quarter: Grade and reflect on what worked

### Expected Timeline
1-2 quarters to build muscle; improvement should be visible within first cycle

---

## Integration

This skill integrates with the **john-doerr** expert persona. Apply Doerr's diagnostic lens: measurement-focused, execution-oriented, no tolerance for vague goals.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No OKRs provided | Request the OKRs to evaluate |
| OKRs are actually fine | Acknowledge strengths, identify minor optimizations |
| Fundamental goal-setting aversion | Address cultural resistance before process fixes |