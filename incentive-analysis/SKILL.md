---
name: incentive-analysis
description: Apply Munger's fundamental insight—"Show me the incentive and I will show you the outcome"—to understand and predict behavior.
license: MIT
metadata:
  version: 1.0.1172
  author: sethmblack
keywords:
- incentive-analysis
- writing
---

# Incentive Analysis

Apply Munger's fundamental insight—"Show me the incentive and I will show you the outcome"—to understand and predict behavior.

---

## When to Use

- Trying to understand why people or organizations behave as they do
- Designing compensation, policies, or systems
- Evaluating a partnership, vendor, or employee
- Diagnosing organizational dysfunction
- User asks "What are the incentives?" or "Why are they acting this way?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The behavior or situation to analyze |
| parties | Yes | The people, roles, or entities involved |
| observed_behavior | No | Current behaviors that seem puzzling or problematic |

---

## Munger's Incentive Principle

"Show me the incentive and I will show you the outcome."

"Never, ever think about something else when you should be thinking about the power of incentives."

"I think I've been in the top 5% of my age cohort all my life in understanding the power of incentives, and all my life I've underestimated it."

Incentives are the most powerful force in human behavior. People respond to their actual incentives, not to what they say they value or what you hope they'll do. Understanding incentive structures explains behavior that otherwise seems irrational.

---

## Types of Incentives

### Financial
- Compensation structure
- Bonuses and commissions
- Equity and ownership
- Fines and penalties

### Career
- Promotion criteria
- Performance metrics
- Reputation effects
- Future opportunities

### Social
- Status and recognition
- Peer approval
- Fear of embarrassment
- Tribal membership

### Psychological
- Sense of purpose
- Autonomy and control
- Mastery and growth
- Identity confirmation

### Structural
- Rules and policies
- Monitoring and accountability
- Time horizons
- Information access

---

## The Framework (7 Steps)

**Step 1: Identify All Parties**
Who are the relevant actors in this situation? Include parties you might overlook (regulators, future actors, hidden stakeholders).

**Step 2: Map Each Party's Incentives**
For each party, ask:
- What are they rewarded for?
- What are they punished for?
- What is easy for them?
- What is hard for them?
- What are their time horizons?

**Step 3: Predict Behavior from Incentives**
Based purely on incentives, what behavior would you expect? (Not what you hope, what incentives predict.)

**Step 4: Compare to Observed Behavior**
Does observed behavior match incentive prediction? If yes, you understand the system. If no, you're missing something.

**Step 5: Identify Misalignments**
Where do incentives conflict with desired outcomes? These are your problem areas.

**Step 6: Look for Perverse Incentives**
Are there incentives that actively reward bad behavior or punish good behavior?

**Step 7: Propose Incentive Redesign**
If behavior needs to change, how must incentives change?

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
## Incentive Analysis

### Situation
[What behavior or system is being analyzed]

### Party Incentive Map

#### [Party 1]
| Incentive Type | Specific Incentive | Behavior It Encourages |
|---------------|-------------------|----------------------|
| Financial | [Incentive] | [Expected behavior] |
| Career | [Incentive] | [Expected behavior] |
| Social | [Incentive] | [Expected behavior] |
| ... | ... | ... |

**Net predicted behavior:** [What incentives predict this party will do]

#### [Party 2]
[Same structure]

### Incentive Alignment Analysis

| Desired Outcome | Aligned Incentives | Misaligned Incentives |
|-----------------|-------------------|---------------------|
| [Outcome 1] | [What pushes toward it] | [What pushes away] |
| ... | ... | ... |

### Perverse Incentives Detected
[Incentives that actively reward bad outcomes]

### Behavior Explained
[How observed behavior follows from incentive structure]

### Recommendations
[How to change incentives to change behavior]

### The Munger Test
"Show me the incentive and I will show you the outcome."
[Summary of key incentive-behavior links]
```

---

## Common Incentive Traps

| Trap | Description | Example |
|------|-------------|---------|
| Paying for A while hoping for B | Rewarding one thing but expecting another | Paying salespeople on revenue while expecting them to maintain margins |
| Short-term vs. long-term | Time horizon mismatch | Quarterly bonuses encouraging short-term thinking |
| Principal-agent | Agent incentives differ from principal's | Real estate agent incentivized to close quickly, not get best price |
| Gaming metrics | People optimize the metric, not the goal | Call center measuring call duration, not problem resolution |
| Risk asymmetry | Upside for risk-taking, no downside | Traders who get bonuses for wins but no penalty for losses |

---

## Constraints

- **Follow the money** - Financial incentives usually dominate, but don't ignore others
- **Consider time horizons** - What someone's incented to do this quarter vs. over career may differ
- **Look for hidden incentives** - Status, identity, and convenience often matter more than stated
- **Don't assume alignment** - Just because incentives should be aligned doesn't mean they are

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

**Input:** "Our software developers keep shipping buggy code despite our quality initiatives. They know bugs are bad. Why do they keep doing this?"

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


## Incentive Analysis

### Situation
Software development team consistently ships buggy code despite expressed commitment to quality.

### Party Incentive Map

#### Developers

| Incentive Type | Specific Incentive | Behavior It Encourages |
|---------------|-------------------|----------------------|
| Career | Performance reviews emphasize features shipped | Ship features fast, fix later |
| Financial | No bonus impact from bugs | Bugs are someone else's problem |
| Social | Recognition for big feature launches | Rush to be the one who ships |
| Psychological | Boredom with testing, excitement with building | Skip tedious quality work |
| Structural | Deadline pressure from management | Cut corners to make dates |
| Structural | QA team exists to catch bugs | "That's their job, not mine" |

**Net predicted behavior:** Ship fast, don't sweat bugs, let QA catch problems, move to next exciting feature.

#### Engineering Managers

| Incentive Type | Specific Incentive | Behavior It Encourages |
|---------------|-------------------|----------------------|
| Career | Measured on roadmap delivery | Push team to ship on schedule |
| Career | Feature launches are visible wins | Prioritize features over quality |
| Social | Pressure from product/sales | Promise aggressive timelines |
| Structural | Bug debt impacts next quarter, not this one | Borrow from future self |

**Net predicted behavior:** Accept quality shortcuts to hit dates, deal with bugs later.

#### QA Team

| Incentive Type | Specific Incentive | Behavior It Encourages |
|---------------|-------------------|----------------------|
| Career | Measured on bugs found | Find bugs, but finding bugs ≠ preventing bugs |
| Structural | Enter process late (after development) | Can only catch, not prevent |
| Social | Adversarial relationship with developers | Enforce rules rather than collaborate |

**Net predicted behavior:** Catch some bugs, but systemically unable to prevent the problem.

### Incentive Alignment Analysis

| Desired Outcome | Aligned Incentives | Misaligned Incentives |
|-----------------|-------------------|---------------------|
| High-quality code | (Almost none) | Feature count metrics, deadline pressure, late-stage QA |
| Fast feature delivery | Developer recognition, manager metrics, promotion criteria | Quality requirements, bug fix costs |

### Perverse Incentives Detected

1. **Features count, bugs don't**: Developers are evaluated on what they build, not on the quality of what they build. Shipping buggy code is rewarded; careful code is invisible.

2. **Separate QA team**: The existence of QA creates moral hazard. "Someone else will catch my bugs" removes responsibility from developers.

3. **Short-term deadlines over long-term quality**: Managers are rewarded for hitting quarterly goals. Bug debt accumulates in future quarters, when it's someone else's problem.

4. **No individual accountability for bugs**: If bugs can't be traced to individual decisions, there's no career consequence.

### Behavior Explained

The developers are behaving exactly as their incentives predict. You've created a system that:
- Rewards feature velocity
- Does not penalize bugs (at the individual level)
- Separates quality ownership from development
- Applies deadline pressure

**The developers aren't bad. The incentive system is.**

### Recommendations

**Change incentives to change behavior:**

1. **Attach bugs to their creators**: Each production bug is publicly attributed to its author. Not for punishment, but for ownership.

2. **Measure quality in reviews**: Add "bugs per feature" or "code that ships without QA rework" to performance criteria.

3. **Make developers own quality**: Eliminate separate QA or make QA advisory. Developers are responsible for testing their own code.

4. **Create time for quality**: If deadlines preclude quality, the deadline is wrong. Push back on unrealistic timelines.

5. **Celebrate quality wins**: Publicly recognize developers who ship high-quality code, not just those who ship features fast.

6. **Align manager incentives**: Measure engineering managers on bug rates, not just feature delivery.

### The Munger Test

"Show me the incentive and I will show you the outcome."

You're paying for features shipped. You're getting features shipped—with bugs. Want quality? Pay for quality.

---

## Integration

This skill is part of the **Charlie Munger** expert persona. Use it to understand that people respond to their actual incentives, not to your hopes.