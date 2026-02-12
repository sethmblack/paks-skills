---
name: premortem-analysis
description: Before finalizing a major decision, imagine the initiative has completely
  failed one year from now. Work backward to identify what went wrong, surfacing risks
  and concerns that optimism typically s...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- premortem-analysis
- writing
---

# Premortem Analysis

Before finalizing a major decision, imagine the initiative has completely failed one year from now. Work backward to identify what went wrong, surfacing risks and concerns that optimism typically suppresses.

---

## When to Use

- About to launch a product, project, or initiative
- Making a significant investment or commitment
- Starting a new venture or partnership
- Implementing organizational change
- Any high-stakes decision where failure would be costly
- User asks "What could go wrong?" or "Run a premortem"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision | Yes | The decision or initiative being considered |
| timeframe | No | How far in the future to imagine (default: 1 year) |
| context | No | Relevant background on the situation |

---

## The Kahneman-Klein Method

The premortem technique, developed by Gary Klein and championed by Daniel Kahneman as "his single most valuable decision-making tool," uses **prospective hindsight** to overcome optimism bias.

### Why It Works

1. **Legitimizes doubt** - In organizations that don't like pessimists, it gives permission to voice concerns
2. **Overcomes groupthink** - Creates space to disagree with the prevailing optimism
3. **Leverages hindsight bias** - Uses the "I knew it all along" effect constructively
4. **Surfaces hidden knowledge** - Team members often have concerns they haven't voiced

### The Key Insight

"The premortem works because it makes it safe to be the skeptic. When the question is 'What concerns do you have?', people stay quiet. When the question is 'It failed - why?', everyone has answers."

---

## Process

### Step 1: Set the Scene
Imagine it is [timeframe] from now. The decision has been implemented. **It has failed completely.** Not partially failed - completely failed.

### Step 2: Generate Failure Modes
Without censorship or debate, list all the reasons why this failure might have occurred. Consider:

**Internal Factors:**
- Resource constraints (time, money, people)
- Execution problems
- Team dynamics or capability gaps
- Competing priorities
- Loss of key personnel

**External Factors:**
- Market changes or competition
- Customer/stakeholder reactions
- Regulatory or legal issues
- Economic conditions
- Technological shifts

**Assumption Failures:**
- What assumptions are we making?
- Which would be fatal if wrong?

**Unknown Unknowns:**
- What might we be completely blind to?
- What has caused similar initiatives to fail?

### Step 3: Prioritize Risks
Rank failure modes by:
- **Likelihood** - How probable is this?
- **Impact** - How severe if it occurs?
- **Detectability** - Would we see it coming?

### Step 4: Develop Mitigations
For high-priority risks:
- Can we prevent this?
- Can we detect it early?
- Can we reduce the impact?
- Should we reconsider the decision?

---

## Output Format

```markdown
## Premortem Analysis

### The Decision
[What is being decided]

### The Failure Scenario
It is [timeframe] from now. [The initiative] has failed completely.

### Why It Failed

#### High-Priority Failure Modes
1. **[Failure mode]**
   - Likelihood: [High/Medium/Low]
   - Impact: [Severe/Moderate/Minor]
   - Root cause: [Why this might happen]
   - Warning signs: [Early indicators]
   - Mitigation: [What to do about it]

2. **[Failure mode]**
   [...]

#### Medium-Priority Failure Modes
[List with brief descriptions]

#### Assumption Vulnerabilities
- [Key assumption] - If wrong because [reason]
- [Key assumption] - If wrong because [reason]

### The Premortem Verdict

**Proceed with modifications:** [Specific changes to make]

**Critical success factors:** [What must go right]

**Kill criteria:** [Conditions that should stop the initiative]

### Kahneman's Reminder
"The main virtue of the premortem is that it legitimizes doubt. You're not the wet blanket - you're doing the exercise."
```

---

## Constraints

- This is not about predicting failure - it's about **imagining** it to surface concerns
- Don't allow debate during brainstorming - collect all failure modes first
- Encourage wild speculation - "unlikely" failures sometimes aren't
- The goal is not to prevent the decision but to **improve** it
- A premortem that finds no risks probably wasn't done honestly

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

**Input:** "We're about to acquire a competitor for $50M. The due diligence looks good. Should we proceed?"

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


## Premortem Analysis

### The Decision
Acquire [Competitor] for $50M based on favorable due diligence.

### The Failure Scenario
It is 18 months from now. The acquisition has failed. We've written off most of the investment, key people have left, and we've lost market position.

### Why It Failed

#### High-Priority Failure Modes

1. **Key Talent Exodus**
   - Likelihood: High
   - Impact: Severe
   - Root cause: Their best engineers left within 6 months because they didn't want to work for us, their equity was cashed out, and our culture clashed with theirs
   - Warning signs: Key people not signing retention agreements, vague answers about future plans
   - Mitigation: Identify 5 must-keep individuals; design retention packages tied to 3-year outcomes; interview them pre-acquisition about concerns

2. **Hidden Technical Debt**
   - Likelihood: Medium
   - Impact: Severe
   - Root cause: Their platform required a ground-up rebuild we didn't anticipate. Due diligence was financial, not deep technical.
   - Warning signs: Engineering team reluctance to show codebase, high server costs, frequent outages
   - Mitigation: Bring in external technical due diligence; talk to their engineering team independently; review last 12 months of incident reports

3. **Customer Concentration Risk**
   - Likelihood: Medium
   - Impact: Severe
   - Root cause: 40% of revenue came from 2 customers who left when the acquisition was announced
   - Warning signs: Check customer concentration in diligence; understand contract renewal dates and terms
   - Mitigation: Talk to top 5 customers before closing; build retention plans; consider earnout tied to customer retention

4. **Integration Paralysis**
   - Likelihood: High
   - Impact: Moderate
   - Root cause: We spent 18 months trying to integrate systems and cultures instead of serving customers. Neither organization could move forward.
   - Warning signs: No clear integration plan before closing; competing visions for combined entity
   - Mitigation: Decide before closing: full integration vs. operate independently; assign dedicated integration team; set 90-day integration milestones

#### Medium-Priority Failure Modes
- **Regulatory surprise** - Their pending lawsuit wasn't disclosed
- **Competitive response** - Larger player dropped prices 30% to take their customers
- **Founder departure** - Founders left after 12-month lockup, taking relationships with them

#### Assumption Vulnerabilities
- **"Their technology is solid"** - If wrong because due diligence was surface-level
- **"Their customers will stay"** - If wrong because customers bought the relationship, not the product
- **"Our cultures are compatible"** - If wrong because we only met leadership, not the team

### The Premortem Verdict

**Proceed with modifications:**
1. Add technical due diligence by independent engineering team
2. Identify and lock in top 5 talent with 3-year retention agreements
3. Talk to top 5 customers before closing
4. Create 90-day integration plan before signing

**Critical success factors:**
- Retain at least 3 of 5 key engineers for 2+ years
- Keep 80%+ of revenue in first year
- Achieve first integration milestone in 90 days

**Kill criteria:**
- More than 2 key engineers refuse retention packages
- Any of top 3 customers express intent to leave
- Technical diligence reveals fundamental platform problems

### Kahneman's Reminder
"The premortem makes people compete to identify threats. Before, they were competing to be optimistic. Same people, different incentives."

---

## Integration

This skill is part of the **Daniel Kahneman** expert persona. It is his single most valuable decision-making technique, designed to overcome the optimism bias that affects most planning.

Related skills:
- **Reference Class Forecasting** - The outside view on similar decisions
- **WYSIATI Check** - What information are we missing?
- **Cognitive Bias Detection** - What biases might be operating?