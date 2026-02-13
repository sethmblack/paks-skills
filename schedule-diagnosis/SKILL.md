---
name: schedule-diagnosis
description: Analyze the reinforcement schedule currently operating and diagnose how it explains behavior patterns, then recommend schedule modifications for desired patterns.
license: MIT
metadata:
  version: 1.0.1838
  author: sethmblack
keywords:
- schedule-diagnosis
- writing
---

# Schedule Diagnosis

Analyze the reinforcement schedule currently operating and diagnose how it explains behavior patterns, then recommend schedule modifications for desired patterns.

**Token Budget:** ~700 tokens

---

## Constraints
- **Do not assume one schedule is universally best.** Different goals require different schedules.
- **Do not ignore competing schedules.** Multiple contingencies operate simultaneously.
- **Do not recommend changes without explaining the expected behavioral effect.**

---

## When to Use

Invoke this skill when:
- Behavior is inconsistent or erratic
- Someone says "They only work hard right before the deadline"
- Recognition or incentive programs are not working
- There is a pattern to when behavior occurs and doesn't occur
- Performance spikes and dips predictably
- Someone asks "Why is this happening in cycles?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Behavior pattern | Yes | Description of when behavior occurs/doesn't occur |
| Current reinforcement | Yes | What follows the behavior and when |
| Desired pattern | No | What pattern is wanted (steady, high rate, etc.) |
| Context | No | Environmental factors |

---

## Schedule Reference

| Schedule | Pattern | Description | Example |
|----------|---------|-------------|---------|
| **Continuous (CRF)** | Every response | Fast acquisition, fast extinction | New skill training |
| **Fixed Ratio (FR-n)** | Every n responses | High rate, pause after reinforcement | Piece-rate pay |
| **Variable Ratio (VR-n)** | Average n responses | Highest rate, most resistant to extinction | Sales commissions, gambling |
| **Fixed Interval (FI-n)** | First response after n time | Scallop (low-high-reinforce-low) | Quarterly reviews |
| **Variable Interval (VI-n)** | Average n time | Steady, moderate rate | Random audits, pop quizzes |

---

## Workflow

### Step 1: Describe the Behavior Pattern

Document the observed pattern:
- When does the behavior occur?
- When does it not occur?
- Is there a cycle? What is its period?
- What is the rate (high/moderate/low/variable)?

### Step 2: Identify Current Schedule

Based on the pattern, identify the operating schedule:

| If you see... | The schedule is likely... |
|---------------|---------------------------|
| Steady high rate | Variable ratio |
| High rate with pauses after reinforcement | Fixed ratio |
| Low rate with bursts before deadline | Fixed interval |
| Steady moderate rate | Variable interval |
| Rapid extinction when reinforcement stops | Continuous |

### Step 3: Explain the Pattern

Connect the schedule to the observed pattern using behavioral principles:
- Why does this schedule produce this pattern?
- What does the organism "expect" based on reinforcement history?
- Are there competing schedules affecting the behavior?

### Step 4: Recommend Schedule Modification

Based on desired outcomes:
| If you want... | Use... | Because... |
|----------------|--------|------------|
| Fast initial learning | Continuous | Every response reinforced builds behavior quickly |
| Steady high performance | Variable ratio | Unpredictable reinforcement maintains high rates |
| Resistance to extinction | Variable ratio or interval | Intermittent schedules build persistence |
| Consistent steady work | Variable interval | Time-based unpredictability prevents scalloping |
| Transition from training to maintenance | CRF → VR | Shift from acquisition to maintenance schedule |

---

## Output Format

```markdown
## Schedule Diagnosis

**Observed Pattern:** [description of behavior pattern]

### Current Schedule Analysis

**Identified Schedule:** [CRF/FR/VR/FI/VI with parameters if known]
**Evidence:** [what in the pattern indicates this schedule]

### Pattern Explanation

[Why this schedule produces this pattern. Include:
- The contingency relationship
- What the organism has learned to expect
- Any competing schedules]

### Diagnosis

[Summary statement connecting schedule to problem/goal]

### Recommended Schedule Modification

**Target Schedule:** [recommended schedule]
**Expected Effect:** [how behavior pattern will change]
**Implementation:**
1. [Specific step to modify schedule]
2. [Specific step]
3. [Specific step]

**Transition Plan:** [if moving from one schedule to another]
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

## Example

**Input:** "Our engineering team only pushes hard on OKRs in the last two weeks of the quarter. The first month is slow, then panic mode hits."

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


## Schedule Diagnosis

**Observed Pattern:** Low activity in first 2/3 of quarter, high burst of activity in final 2 weeks, then drop after quarter end

### Current Schedule Analysis

**Identified Schedule:** Fixed Interval (FI-12 weeks / quarterly)
**Evidence:**
- Classic "scallop" pattern: low rate followed by acceleration toward reinforcement point
- Behavior peaks just before the fixed time point (quarter end)
- Drop in rate immediately after reinforcement (post-quarter lull)

### Pattern Explanation

Quarterly OKR reviews operate on a fixed interval schedule. The team has learned that reinforcement (recognition, performance assessment, goal credit) occurs at fixed 12-week intervals. Since reinforcement is time-based rather than response-based, there is no differential reinforcement for early work versus late work—only for work completed by the deadline.

Rational behavior under FI is exactly what you observe: minimal responding until the interval nears its end, then rapid responding to produce the reinforced outcome before the deadline. This is not laziness or poor planning; it is the predictable behavioral effect of the schedule you have arranged.

### Diagnosis

The quarterly OKR system has inadvertently created a fixed interval schedule that produces scalloping. The team has adapted optimally to the contingencies as arranged.

### Recommended Schedule Modification

**Target Schedule:** Variable Ratio (VR) layered on FI

**Expected Effect:** Steadier work rate throughout quarter; reduced deadline panic; maintained quarterly accountability

**Implementation:**
1. **Add variable ratio component:** Random check-ins where progress earns recognition (not punishment for lack of progress)
2. **Create intermediate reinforcement points:** Monthly milestone celebrations for OKR progress (converts FI-12 to something closer to FI-4)
3. **Add response-based reinforcement:** Acknowledge and recognize specific OKR work as it happens, not just at quarter end
4. **Make early progress visible:** Dashboard showing real-time progress provides continuous feedback (approximating CRF for visibility)

**Transition Plan:**
- Keep quarterly structure (maintains accountability)
- Add monthly check-ins with light reinforcement for progress
- Implement random "progress spotlights" in team meetings (VR component)
- Gradually reduce emphasis on deadline-only assessment

---

## Common Schedule Patterns in Organizations

| Situation | Likely Schedule | Typical Problem |
|-----------|----------------|-----------------|
| Annual reviews | FI-12 months | Extreme scalloping, behavior concentrated in review prep |
| Quarterly bonuses | FI-13 weeks | Scalloping, deadline panic |
| Sales quotas (monthly) | FI-4 weeks | End-of-month surge, early-month drought |
| Piece-rate work | FR-n | High rate but post-reinforcement pauses |
| Random recognition | VR | Desired: steady high performance |
| Random audits | VI | Desired: consistent compliance |

---

## Integration

Use after **contingency-analysis** identifies that the behavior exists but occurs in problematic patterns. Schedule diagnosis explains the pattern and guides modification.

---

## Source Expert

Derived from B.F. Skinner and Charles Ferster's *Schedules of Reinforcement* (1957). Schedule effects are among the most replicable findings in behavioral science.