---
name: extinction-procedure
description: Design a procedure to eliminate unwanted behavior by identifying and removing the maintaining reinforcer, with preparation for extinction burst and differential reinforcement of alternative behavior.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3965
repository: https://github.com/sethmblack/paks-skills
keywords:
- extinction-procedure
- writing
---

# Extinction Procedure

Design a procedure to eliminate unwanted behavior by identifying and removing the maintaining reinforcer, with preparation for extinction burst and differential reinforcement of alternative behavior.

**Token Budget:** ~700 tokens

---

## Constraints
- **Do not recommend punishment as primary intervention.** Extinction is preferred; punishment has side effects.
- **Do not ignore the extinction burst.** Warn that behavior will temporarily increase.
- **Do not leave a behavioral vacuum.** Always specify an alternative behavior to reinforce.

---

## When to Use

Invoke this skill when:
- Unwanted behavior persists despite requests to stop
- Someone asks "How do I eliminate this behavior?"
- Verbal instruction has failed to stop behavior
- A habit or pattern needs to be broken
- Someone says "They keep doing X no matter what I say"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Unwanted behavior | Yes | The behavior to eliminate (precisely defined) |
| Context | Yes | When/where the behavior occurs |
| Current consequences | No | What follows the behavior (what reinforces it) |
| Desired alternative | No | What behavior should replace it |

---

## Workflow

### Step 1: Identify the Maintaining Reinforcer

What consequence is reinforcing the unwanted behavior? Common maintainers:

| Behavior Type | Common Reinforcer |
|---------------|-------------------|
| Attention-seeking | Attention (even negative) |
| Escape/avoidance | Removal of aversive task/situation |
| Tangible | Access to objects, privileges |
| Sensory/automatic | Internal reinforcement from the behavior itself |

Ask: "What does the person get by doing this behavior?"

### Step 2: Design the Extinction Contingency

Remove the reinforcer completely and consistently:
- If attention-maintained: Withhold all attention following the behavior
- If escape-maintained: Do not allow escape following the behavior
- If tangible-maintained: Do not provide the tangible following the behavior
- If automatically reinforced: This is hardest; may need response blocking or enriched environment

**Critical:** Extinction must be 100% consistent. Intermittent reinforcement during extinction will strengthen the behavior.

### Step 3: Prepare for the Extinction Burst

When reinforcement stops, behavior temporarily increases before it decreases. This is the extinction burst.

Characteristics:
- Higher frequency of the behavior
- Higher intensity of the behavior
- Novel variations of the behavior
- Emotional responses (frustration)

**The extinction burst is normal and expected.** If you reinforce during the burst, you teach the organism that persistence pays off.

### Step 4: Plan Differential Reinforcement of Alternative Behavior (DRA)

Never leave a behavioral vacuum. Specify:
- What alternative behavior should replace the unwanted behavior
- What reinforcer will maintain the alternative
- The alternative should be incompatible with the unwanted behavior if possible

DRA types:
| Type | Description |
|------|-------------|
| DRA | Reinforce any acceptable alternative behavior |
| DRI | Reinforce behavior physically incompatible with unwanted behavior |
| DRO | Reinforce absence of unwanted behavior for a time period |

### Step 5: Plan for Spontaneous Recovery

After extinction, the behavior may temporarily return. This is spontaneous recovery.
- Maintain the extinction contingency
- Do not re-reinforce the recovered behavior
- Continue reinforcing the alternative

---

## Output Format

```markdown
## Extinction Procedure

**Unwanted Behavior:** [precisely defined behavior]
**Context:** [when/where it occurs]

### Functional Analysis

**Maintaining Reinforcer:** [what is reinforcing this behavior]
**Evidence:** [how do you know this is the reinforcer]
**Function:** [attention/escape/tangible/automatic]

### Extinction Contingency

**Procedure:** [how to withhold the reinforcer]
**Consistency Required:** 100% - all instances, all people, all contexts
**Who Must Implement:** [everyone who encounters the behavior]

### Extinction Burst Preparation

**Expected Burst:** [what the burst will look like]
**Duration Estimate:** [how long before extinction takes effect]
**Warning:** Reinforcing during the burst will strengthen the behavior. Maintain extinction through the burst.

### Differential Reinforcement

**Alternative Behavior:** [what to reinforce instead]
**Reinforcer:** [what consequence maintains the alternative]
**Schedule:** [continuous during acquisition, then intermittent]
**DRA Type:** [DRA/DRI/DRO]

### Spontaneous Recovery Plan

**Expected:** Behavior may return briefly after apparent extinction
**Response:** Maintain extinction contingency; do not re-reinforce
**Timeline:** Full extinction typically requires [estimate] with consistent implementation
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

**Input:** "A team member constantly interrupts in meetings to push their own ideas. I've asked them to stop but they keep doing it."

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


## Extinction Procedure

**Unwanted Behavior:** Interrupting others in meetings to insert own ideas before speakers finish
**Context:** Team meetings, especially during brainstorming or problem-solving

### Functional Analysis

**Maintaining Reinforcer:** Attention and discussion of their ideas; possibly escape from having to listen to others
**Evidence:** Interruptions typically result in the speaker stopping and the interrupter getting floor time; their ideas get discussed
**Function:** Attention + tangible (idea gets considered)

### Extinction Contingency

**Procedure:**
1. When interruption occurs, the current speaker continues as if no interruption occurred
2. Facilitator says "Let [speaker] finish" without further attention to the interrupter
3. Do not address or discuss the interrupter's point until they have raised it appropriately
4. If they continue, proceed with the meeting without acknowledgment

**Consistency Required:** 100% - all meeting participants must respond identically
**Who Must Implement:** All team members, especially the facilitator

### Extinction Burst Preparation

**Expected Burst:**
- Increased frequency of interruptions (more attempts)
- Increased intensity (louder, more insistent)
- Emotional frustration (visible annoyance, complaints about being ignored)
- Novel variations (talking over the "Let them finish" statement)

**Duration Estimate:** 2-3 meetings of consistent extinction before significant decrease

**Warning:** If anyone engages with the interruption during the burst, you will reinforce persistence. The behavior will become more resistant to future extinction.

### Differential Reinforcement

**Alternative Behavior:** Raising hand or using meeting signal (e.g., chat indicator) and waiting to be recognized before speaking
**Reinforcer:**
- Immediate recognition when signal is used: "Good, what's your thought?"
- Full attention and consideration of idea when raised appropriately
- Verbal acknowledgment: "I appreciate you waiting—go ahead"

**Schedule:** Continuous during acquisition (acknowledge every appropriate signal)
**DRA Type:** DRI (waiting is incompatible with interrupting)

### Spontaneous Recovery Plan

**Expected:** After 1-2 successful meetings, interrupting may briefly return
**Response:** Apply same extinction contingency; reinforce alternative when used
**Timeline:** Full extinction typically requires 4-6 meetings with consistent implementation. Maintenance reinforcement of the alternative should continue indefinitely.

---

## Common Mistakes to Avoid

1. **Intermittent reinforcement during extinction:** Even occasional attention strengthens the behavior
2. **Giving in during the burst:** This teaches that persistence pays off
3. **No alternative behavior:** Creates frustration without a productive outlet
4. **Inconsistent application:** Different people responding differently undermines extinction
5. **Expecting immediate results:** Extinction takes time; the burst comes first

---

## When Extinction May Not Work

- **Automatically reinforced behavior:** The behavior provides its own reinforcement (sensory, physiological)
- **Unable to control the reinforcer:** Someone else provides reinforcement
- **Safety concerns:** Extinction burst may be dangerous
- **Behavior too entrenched:** May need additional interventions

In these cases, consider:
- Response blocking (prevent the behavior from occurring)
- Environmental enrichment (make alternative more reinforcing than unwanted behavior)
- Differential reinforcement of other behavior (DRO) without pure extinction

---

## Integration

Use after **contingency-analysis** has identified that the behavior exists and is maintained by identifiable reinforcement. Combine with **shaping-plan** if the alternative behavior needs to be built.

---

## Source Expert

Derived from B.F. Skinner's work on extinction and reinforcement. "Behavior that is not reinforced will eventually cease."