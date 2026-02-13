---
name: trust-battery-assessment
description: Evaluate relationship health and team dynamics using Tobi Lutke's trust battery metaphor. Diagnose current charge levels, identify what's charging or depleting trust, and prescribe specific actions...
license: MIT
metadata:
  version: 1.0.2148
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- trust-battery-assessment
- writing
---

# Trust Battery Assessment

Evaluate relationship health and team dynamics using Tobi Lutke's trust battery metaphor. Diagnose current charge levels, identify what's charging or depleting trust, and prescribe specific actions to rebuild or maintain trust.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this framework to manipulate or deceive others
- Provide assessments designed to unfairly terminate employees
- Diagnose trust issues without considering both parties' perspectives
- Make assessments based on protected characteristics (race, gender, etc.)

**If asked to misuse this framework:** Refuse explicitly. The trust battery is a tool for honest relationship repair, not manipulation.

---

## When to Use

- Someone feels micromanaged or under-trusted
- A working relationship has friction or tension
- After a significant failure or breach of commitment
- When deciding how much autonomy to grant someone
- When trust needs to be discussed without making it personal
- Team dynamics are suffering from unspoken trust issues

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **relationship_context** | Yes | Who are the parties? What is their working relationship? |
| **presenting_issue** | No | What triggered this assessment? Recent events? |
| **perspective** | No | Whose perspective are we assessing from? |

---

## The Trust Battery Framework

### Core Concept

Trust between colleagues operates like a phone battery:
- **Starting charge:** New relationships begin at ~50% (benefit of the doubt)
- **Charging:** Positive interactions increase trust incrementally
- **Depleting:** Negative interactions decrease trust incrementally
- **Low battery warning:** Below ~30%, the relationship consumes mental energy
- **Full charge:** Above ~80%, the relationship enables full autonomy

### Charging Behaviors (+)
| Behavior | Charge Amount |
|----------|---------------|
| Delivered on major commitment | +5-10% |
| Consistently on time to meetings | +0.5% per instance |
| Proactively communicated bad news | +3-5% |
| Took ownership of mistake | +3-5% |
| Exceeded expectations | +2-5% |
| Maintained confidentiality | +1-2% |
| Followed through on small promises | +1% per instance |

### Depleting Behaviors (-)
| Behavior | Depletion Amount |
|----------|-----------------|
| Missed major deadline without warning | -10-15% |
| Broke confidentiality | -15-25% |
| Blamed others for own mistake | -5-10% |
| Chronically late to meetings | -0.5% per instance |
| Made commitment then didn't follow through | -3-5% |
| Surprised with bad news that should have been communicated earlier | -5-10% |
| Overpromised and underdelivered | -3-5% |

---

## Workflow
### Step 1: 1. Establish Current Battery Level

Ask: "If trust were a battery percentage, where would you place this relationship?"

**Calibration anchors:**
- **80-100%:** Full autonomy. You don't think about them. Complete confidence.
- **60-80%:** Healthy working relationship. Minor monitoring.
- **40-60%:** Neutral. Normal oversight. Neither worried nor confident.
- **20-40%:** Concerning. Frequent check-ins feel necessary. Consumes mental energy.
- **0-20%:** Critical. Constant vigilance. Relationship may be unworkable.

### Step 2: 2. Identify Recent Charging/Depleting Events

Map the last 30-90 days:
- What interactions charged the battery?
- What interactions depleted it?
- Was there a single major event or accumulated small events?

### Step 3: 3. Diagnose Root Cause

Common patterns:
- **Competence gap:** Person lacks skills (address through training/support)
- **Reliability gap:** Person is capable but inconsistent (address through commitment clarity)
- **Communication gap:** Work is good but not communicated (address through visibility)
- **Values gap:** Fundamental misalignment (may require separation)

### Step 4: 4. Prescribe Charging Actions

Specific, concrete actions to rebuild trust:
- What commitments should be made and kept?
- What communication rhythms should be established?
- What quick wins would charge the battery fastest?
- What behaviors should stop immediately?

### Step 5: 5. Establish Monitoring Cadence

Based on current battery level:
- **20-40%:** Weekly check-ins until above 50%
- **40-60%:** Bi-weekly check-ins
- **60-80%:** Monthly or natural rhythm
- **80%+:** No special monitoring needed

---

## Output Format

```markdown
## Trust Battery Assessment

**Relationship:** [Party A] → [Party B]
**Current Charge:** [X]%
**Trend:** [Charging/Stable/Depleting]
**Assessment Date:** [Date]

### Battery History (Recent)

| Date/Period | Event | Impact |
|-------------|-------|--------|
| [Date] | [Event] | [+/-X%] |

### Diagnosis

**Root cause:** [Competence/Reliability/Communication/Values gap]

**Key depleting factors:**
1. [Factor with specific examples]
2. [Factor with specific examples]

**Existing charging factors:**
1. [Factor to preserve]
2. [Factor to preserve]

### Charging Plan

**Immediate actions (this week):**
1. [Specific action]
2. [Specific action]

**Sustained behaviors (ongoing):**
1. [Behavior to establish]
2. [Behavior to establish]

**Monitoring:** [Cadence based on battery level]

### Success Metrics

Battery target: [X]% within [timeframe]
Key indicator: [Observable behavior that signals improvement]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No specific relationship provided | Ask for relationship context before proceeding |
| Only one party's perspective available | Note limitation; recommend gathering other perspective |
| Battery at 0-10% | Acknowledge relationship may be unworkable; focus on whether repair is possible |
| Trust issue stems from single catastrophic event | Address whether event is forgivable before charging plan |
| Protected characteristic bias suspected | Refuse assessment; recommend HR/professional intervention |

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
"My new manager has been checking on my work every few hours. It feels like micromanagement. What's going on?"

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


## Trust Battery Assessment

**Relationship:** Manager → You
**Current Charge:** ~35% (estimated from behavior)
**Trend:** Unknown (need more data)
**Assessment Date:** 2026-01-29

### Battery History (Recent)

You're new to this manager. The frequent check-ins suggest the battery hasn't charged past the initial 50%. Something may have depleted it early, or the manager's default is cautious until trust is built.

### Diagnosis

**Root cause:** Likely a combination of:
1. **Newness:** Insufficient time for charging behaviors to accumulate
2. **Manager's past experience:** May have been burned by previous reports
3. **Possible early depletion:** Was there a missed expectation early on?

**Tobi Lutke's insight:** "If you're being micromanaged it's probably because you either don't have the skills or trust of your manager to produce the desired result."

This isn't a moral judgment on you. It's diagnostic. The manager is acting as if the battery is low.

### Charging Plan

**Immediate actions (this week):**
1. **Proactive updates:** Before they check in, send a brief status. Remove the need for them to ask.
2. **Clarify expectations:** Ask explicitly: "What does success look like for this project? What would make you confident I'm on track?"

**Sustained behaviors (ongoing):**
1. **Consistent delivery:** Every commitment kept charges the battery
2. **No surprises:** If something might be late, communicate immediately
3. **Document wins:** Make your successes visible

**Monitoring:** After 2-3 weeks of proactive updates and consistent delivery, observe if check-in frequency decreases.

### Success Metrics

Battery target: 60% within 30 days
Key indicator: Manager reduces check-in frequency without prompting

---

## Integration

This skill originates from the **Tobi Lutke** expert persona. It embodies his belief that trust can be discussed concretely without making it personal, and that the trust battery metaphor "allows people to talk about the trust that exists between two people without actually becoming personal."

For organizational culture issues, combine with **team-not-family-audit**. For calendar/time issues, combine with **meeting-audit**.