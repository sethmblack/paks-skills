---
name: action-bias-assessment
description: Evaluate decisions against action-orientation criteria and break through analysis paralysis to capture time-sensitive opportunities.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2874
repository: https://github.com/sethmblack/paks-skills
keywords:
- action-bias-assessment
- writing
---

# Action Bias Assessment

Evaluate decisions against action-orientation criteria and break through analysis paralysis to capture time-sensitive opportunities.

---

## Purpose

You help users determine when they have enough information to act and what they can do today while continuing to learn. While you're analyzing, someone else is doing. Your goal is to break paralysis, accelerate learning cycles, and ensure missed opportunities don't accumulate.

---

## When to Use

Invoke this skill when users are:
- Stuck in analysis paralysis with a decision
- Debating whether to ship or wait for more polish
- Uncertain whether they have enough data to proceed
- Facing time-sensitive opportunities that may expire
- Over-planning instead of executing and learning

**Trigger phrases:** "analysis paralysis," "should we wait," "need more data," "when to ship," "is it ready," "we're still planning"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## The Speed Imperative Framework

### Core Principles

1. **Perfect is the enemy of done** - A shipped 80% solution beats an unshipped 100% solution
2. **Mistakes can be fixed; missed opportunities cannot** - Errors in production are correctable; time lost is gone
3. **Ship and iterate beats plan and delay** - Real feedback teaches what planning cannot
4. **Every day of delay is opportunity lost** - What learning are you not getting while waiting?

### The 70% Rule

**If you have 70% of the information you need, decide.**

The remaining 30% often takes 10x the time to gather and rarely changes the decision. The cost of waiting usually exceeds the cost of being slightly wrong.

---

## Assessment Process

### Step 1: Diagnose the Paralysis

**Questions to answer:**
- What specific decision is being delayed?
- What information are you waiting for?
- What would change your decision if you learned it?
- How long have you been in this state?

### Step 2: Calculate the Cost of Delay

**Questions to answer:**
- What learning are you NOT getting while waiting?
- What opportunity might expire or diminish?
- What competitor action might occur?
- What is the actual cost per day/week/month of not acting?

### Step 3: Assess Reversibility

**Questions to answer:**
- If this decision is wrong, can it be reversed?
- What is the cost of reversing?
- Are you treating a reversible decision as irreversible?
- What's the minimum viable commitment that preserves options?

### Step 4: Define Minimum Viable Action

**Questions to answer:**
- What is the smallest step that moves forward?
- What can you ship today that generates real feedback?
- What experiment would resolve your uncertainty faster than analysis?
- What can you do now while continuing to gather information?

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

When assessing a decision:

```markdown
## Action Bias Assessment: [Decision/Situation]

### Current State
- Decision under consideration: [What]
- Time in analysis: [How long]
- Information gap: [What's missing]

### Cost of Delay Analysis
| Factor | Impact |
|--------|--------|
| Learning foregone | [What you're not learning] |
| Opportunity risk | [What might expire] |
| Competitive risk | [What others might do] |
| Estimated cost per [unit] | [Quantify if possible] |

### Reversibility Assessment
- Reversibility: High / Medium / Low
- Reversal cost: [What it takes to undo]
- Minimum commitment: [Smallest step forward]

### Information Assessment
- Current confidence: [X]%
- Information needed for 100%: [What's missing]
- Time to gather remaining: [Estimate]
- Would it change decision: Likely / Unlikely / Unknown

### Recommendation
- **Action:** [Proceed / Wait / Experiment]
- **Rationale:** [Why]
- **Minimum Viable Action:** [Specific next step]
- **What to do TODAY:** [Immediate action]

### If Proceeding
1. [First action to take now]
2. [What to monitor for feedback]
3. [Trigger to reassess]
```

---

## Decision Accelerators

Use these to break common paralysis patterns:

### "We need more data"
- **Ask:** What specific data would change your decision?
- **If unclear:** You have enough data
- **Alternative:** Ship something that generates the data you need

### "We're not sure it's ready"
- **Ask:** Ready for what? Production? Feedback? Learning?
- **If for learning:** It's ready. Ship it.
- **Alternative:** Define "ready" with specific criteria, then ship when met

### "What if we're wrong?"
- **Ask:** Is this reversible? What's the actual cost of being wrong?
- **If reversible:** Being wrong is how you learn
- **Alternative:** Find a smaller commitment that limits downside

### "We need buy-in first"
- **Ask:** Can you ship something that demonstrates value to get buy-in?
- **If yes:** Showing beats telling
- **Alternative:** What's the minimum viable demonstration?

### "The timing isn't right"
- **Ask:** What would make timing right? Is that in your control?
- **If not in control:** Waiting doesn't help
- **Alternative:** What can you do now to be ready when timing is right?

---

## Constraints

- Do not encourage recklessness—some decisions genuinely require more information
- Acknowledge when stakes are genuinely high and irreversible
- Recognize regulatory, safety, or compliance requirements that mandate caution
- Distinguish between analysis (productive) and paralysis (stuck)
- Consider team readiness and organizational capacity to absorb risk

---

## Anti-Patterns

| Paralysis Pattern | What It Really Is | Action Response |
|-------------------|-------------------|-----------------|
| "Need more research" | Fear of commitment | Define what would change your mind |
| "Let's schedule another meeting" | Avoiding decision ownership | Decide now, inform in the meeting |
| "We should get more stakeholder input" | Diffusing accountability | Make the call, get feedback after |
| "The data isn't conclusive" | Waiting for certainty that won't come | Decide with what you have |
| "We're still socializing the idea" | Endless consensus-seeking | Set a decision deadline |

---

## The Bottom Line

**Two questions:**
1. What can we do TODAY while we learn?
2. What's the cost of doing nothing for another day?

If the cost of delay exceeds the cost of a correctable mistake, move. Now.

---

*The two most important requirements for major success are: first, being in the right place at the right time, and second, doing something about it. You might be in the right place. Are you doing something about it?*

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

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].