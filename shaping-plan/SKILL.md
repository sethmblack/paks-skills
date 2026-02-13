---
name: shaping-plan
description: Design a shaping procedure to build complex behavior through successive approximations, specifying starting behavior, terminal behavior, and reinforcement steps.
license: MIT
metadata:
  version: 1.0.1883
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- shaping-plan
- writing
---

# Shaping Plan

Design a shaping procedure to build complex behavior through successive approximations, specifying starting behavior, terminal behavior, and reinforcement steps.

**Token Budget:** ~700 tokens

---

## Constraints
- **Do not expect perfection immediately.** Shaping requires patience and small steps.
- **Do not create ratio strain.** Steps must be small enough to maintain behavior.
- **Do not skip reinforcement.** Each approximation must be reinforced before raising criteria.

---

## When to Use

Invoke this skill when:
- Teaching a new skill or behavior
- Someone asks "How do I train someone to do X?"
- Current behavior is far from desired behavior
- Someone says "They can't do the whole thing yet"
- Building habits or behavioral repertoires
- Someone asks "How do I get from here to there?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Terminal behavior | Yes | The final desired behavior (precisely defined) |
| Starting behavior | Yes | What the person/team can currently do |
| Context | No | The situation where behavior should occur |
| Timeline | No | How quickly behavior needs to develop |
| Available reinforcers | No | What can be used to reinforce approximations |

---

## Workflow

### Step 1: Define Terminal Behavior Precisely

What does success look like? Make it observable and measurable.
- Not: "Good communication skills"
- Instead: "Provides status updates in standup with problem/action format in under 2 minutes"

### Step 2: Identify Starting Behavior

What does the person already do that moves toward the goal?
- What approximation is currently in their repertoire?
- What related behaviors exist?
- Where is the natural starting point?

### Step 3: Map the Approximation Path

Identify 3-8 successive approximations between start and terminal.
- Each step should be achievable given the previous step
- Steps should be small enough that behavior is maintained
- Steps should be large enough that progress is visible

### Step 4: Specify Reinforcement for Each Step

For each approximation:
- What reinforcer will be used?
- When will it be delivered (immediately after behavior)
- What schedule (continuous during acquisition)
- What is the criterion for moving to next step?

### Step 5: Plan for Schedule Transition

After terminal behavior is acquired:
- Move from continuous to intermittent reinforcement
- Specify the fading schedule
- Identify natural reinforcers to maintain behavior

---

## Output Format

```markdown
## Shaping Plan

**Terminal Behavior:** [precisely defined final behavior]
**Starting Behavior:** [what is currently in repertoire]

### Approximation Sequence

| Step | Approximation | Criterion for Advancement | Reinforcer |
|------|---------------|---------------------------|------------|
| 1 | [first approximation] | [when to move on] | [what reinforcer] |
| 2 | [second approximation] | [when to move on] | [what reinforcer] |
| ... | ... | ... | ... |
| N | [terminal behavior] | [maintenance criterion] | [natural reinforcer] |

### Reinforcement Specifications

- **Acquisition Schedule:** Continuous (every correct response)
- **Advancement Criterion:** [number of successful responses before raising criterion]
- **Maintenance Schedule:** [schedule after terminal behavior is acquired]

### Ratio Strain Prevention

- **Warning Signs:** [what indicates criteria are too demanding]
- **Recovery Procedure:** [how to recover if ratio strain occurs]

### Timeline Estimate

[Estimated time to reach terminal behavior, with caveats]
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

**Input:** "I want to train a junior developer to conduct code reviews independently. Currently they just look at code and say 'looks good.'"

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


## Shaping Plan

**Terminal Behavior:** Conducts independent code reviews that identify at least one substantive issue per review and provides actionable feedback with code suggestions
**Starting Behavior:** Looks at code, provides non-specific approval ("looks good")

### Approximation Sequence

| Step | Approximation | Criterion for Advancement | Reinforcer |
|------|---------------|---------------------------|------------|
| 1 | Identifies any single observation about the code (even obvious or stylistic) | 3 consecutive reviews with at least 1 observation | Verbal acknowledgment + "Good observation" |
| 2 | Identifies one potential issue or question per review | 3 consecutive reviews with substantive observation | Acknowledgment + discussion of the observation |
| 3 | Provides specific line reference with observation | 3 reviews with line-specific feedback | Senior review of their review + feedback |
| 4 | Suggests a specific change or asks a clarifying question | 3 reviews with actionable feedback | Public recognition in team channel |
| 5 | Identifies multiple issues per review (2+) | 5 reviews meeting criterion | Reduced oversight, increased autonomy |
| 6 | Conducts independent review with actionable feedback on all substantive issues | Consistent performance over 10 reviews | Natural reinforcer: influence on codebase, team trust |

### Reinforcement Specifications

- **Acquisition Schedule:** Continuous - acknowledge every approximation during early steps
- **Advancement Criterion:** 3 successful responses before raising criterion (prevents accidental advancement)
- **Maintenance Schedule:** Variable ratio (approximately every 3rd good review receives explicit acknowledgment)

### Ratio Strain Prevention

- **Warning Signs:** Junior dev avoiding code reviews, producing lower quality observations than before, expressing frustration
- **Recovery Procedure:** Drop back one step, reinforce current approximation until strong, then advance more gradually

### Timeline Estimate

Approximately 4-6 weeks to reach terminal behavior, assuming 3-5 code reviews per week. Individual variation expected; some may progress faster if starting behavior is stronger than assessed.

---

## Common Mistakes to Avoid

1. **Steps too large:** If behavior deteriorates, steps are too big
2. **Advancing too quickly:** Reinforce each approximation until strong
3. **Inconsistent reinforcement:** During acquisition, reinforce every correct response
4. **No clear criteria:** Specify exactly when to advance
5. **Forgetting to fade:** After acquisition, transition to intermittent schedule

---

## Integration

Use after **contingency-analysis** has identified that the behavior does not exist and must be built. Shaping builds new repertoires; it does not fix existing contingencies.

---

## Source Expert

Derived from B.F. Skinner's shaping through successive approximations. "You cannot reinforce behavior that does not occur—you must shape it."