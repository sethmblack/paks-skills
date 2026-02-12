---
name: problem-deepening
description: A structured approach to deeply understanding problems before attempting
  solutions—spending "55 minutes on the problem and 5 minutes on solutions.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- problem-deepening
- transformation
- writing
---

# Problem Deepening

A structured approach to deeply understanding problems before attempting solutions—spending "55 minutes on the problem and 5 minutes on solutions."

---

## Purpose

Before solving, develop deep understanding of the problem—its root causes, hidden assumptions, true nature, and real constraints. Prevent the costly error of elegantly solving the wrong problem.

---

## When to Use

- You're about to invest significant effort in solving something
- Solutions aren't working and you don't know why
- You suspect you might be solving the wrong problem
- The problem keeps recurring despite solutions
- You want to ensure you understand before you act

**Trigger Phrases:**
- "Help me understand this problem better"
- "What am I really dealing with?"
- "Why is this actually hard?"
- "Deepen my understanding before I solve"
- "Am I solving the right problem?"
- "What am I missing about this situation?"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## The Six-Step Process

### Step 1: Surface the Stated Problem

Write down the problem as currently understood:
- How has it been described?
- Who defined it this way?
- What solution frame is implied by this definition?

The way a problem is stated often smuggles in assumptions about solutions. "How do I get more done?" assumes doing more is the goal. "How do I work less?" assumes work is the problem. Same situation, different framings, different solutions.

### Step 2: Question the Assumptions

Every problem statement contains hidden assumptions. Make them explicit:

**Questions to ask:**
- What am I taking for granted?
- What constraints have I accepted without examination?
- What would happen if the opposite were true?
- Why do I think this is a problem?
- Whose problem is this really?

**Example:** "I need to hire more engineers" assumes the solution is more people. Assumptions: current engineers are working efficiently, the work requires engineers, more people means more output. Each assumption might be false.

### Step 3: Identify Root Causes

Surface symptoms aren't the problem—they're signals. Dig deeper:

**The "Five Whys" technique:**
- Why is this happening?
- Why is that?
- Why is that?
- Why is that?
- Why is that?

Usually by the fifth "why," you've reached something more fundamental than the surface symptom.

**Example:**
- Problem: We're missing deadlines
- Why? Features take longer than estimated
- Why? Requirements change mid-development
- Why? We don't fully understand customer needs at start
- Why? We start building before validating
- Why? We feel pressure to show progress
- Root cause: Culture rewards activity over understanding

### Step 4: Map Real vs. Perceived Constraints

Separate constraints into categories:

**Genuine constraints** (physics, law, absolute limits):
- These cannot be changed; solutions must work within them
- Be sure they're really immutable—many "laws" are actually conventions

**Perceived constraints** (assumptions, conventions, habits):
- These feel like limits but could be challenged
- "We've always done it this way" is a perceived constraint

**Self-imposed constraints** (beliefs, fears, preferences):
- These come from within and can be changed by choice
- "I couldn't possibly ask for that" is self-imposed

Many problems become easy when perceived constraints are removed.

### Step 5: Reframe the Problem

With deeper understanding, reformulate the problem:

**Reframing techniques:**
- **Invert it:** Instead of "How do I succeed?" ask "How would I guarantee failure?"
- **Expand it:** What's the bigger problem this is part of?
- **Contract it:** What's the smallest version of this problem?
- **Flip the subject:** Instead of "How do I get them to...?" ask "What would make them want to...?"
- **Change the metric:** Instead of "How do I do more?" ask "How do I do what matters?"

A well-reframed problem often suggests its own solution.

### Step 6: Generate Better Questions

The output of problem deepening isn't answers—it's better questions.

**Good questions:**
- Open new solution spaces
- Challenge hidden assumptions
- Point toward root causes
- Suggest where to look for answers

**Example transformation:**
- Original: "How do I get my team to communicate better?"
- After deepening: "What makes honest communication feel unsafe here?"

The second question opens entirely different solutions.

---

## Warning Signs of Shallow Problem Definition

- Jumping immediately to solutions
- Only one stakeholder's perspective considered
- Problem statement includes the solution ("How do I implement X?")
- No constraints identified
- Problem has been defined by the same person who must approve solutions
- Urgency used to skip understanding
- "We just need to execute"

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

## Outputs
When deepening a problem, provide:

1. **Stated Problem** (How it's currently defined)
2. **Hidden Assumptions** (What's being taken for granted)
3. **Root Cause Analysis** (Five Whys or equivalent)
4. **Constraints Analysis** (Real vs. perceived vs. self-imposed)
5. **Reframed Problem** (Better formulation)
6. **Better Questions** (What to explore now)

---

## Example Application

**Input:** "I need help solving my procrastination problem"

**Problem Deepening:**

**Stated Problem:** "I procrastinate and need to stop."

**Hidden Assumptions:**
- Procrastination is the problem (not a symptom)
- The solution is to overcome or defeat it
- More willpower or better techniques will help
- The tasks being procrastinated on should be done
- Starting earlier would improve outcomes

**Root Cause Analysis (Five Whys):**
- Why do you procrastinate? "I feel overwhelmed when I start"
- Why overwhelmed? "The task seems too big and unclear"
- Why unclear? "I haven't broken it into steps"
- Why not? "I'm anxious about discovering how hard it really is"
- Why anxious? "Because if I fail after trying, I can't protect my self-image"

Root cause: Procrastination serves as ego protection. As long as you haven't really tried, you can believe you would have succeeded if you had.

**Constraints Analysis:**
- Real: Tasks have actual deadlines; some tasks are genuinely required
- Perceived: "I must feel motivated to start"; "I need uninterrupted time"
- Self-imposed: "If I start imperfectly, I've failed"; "I should want to do this"

**Reframed Problem:**
"How do I make starting feel safe enough that I don't need procrastination to protect my self-image?"

**Better Questions:**
- What would happen if I gave myself permission to do it badly?
- What's the smallest possible action that would count as starting?
- What am I afraid I'll discover about myself or the task?
- What would I tell a friend in this situation?
- When do I not procrastinate, and what's different about those situations?

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

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

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

## Integration

This skill draws from the **Albert Einstein Expert** persona and his principle: "If I had an hour to solve a problem, I'd spend 55 minutes thinking about the problem and five minutes thinking about solutions." For full Einsteinian analysis, invoke the complete Einstein expert.

---

## Remember

The quality of your solution is bounded by the quality of your understanding. Most problems persist not because solutions are hard to find but because the problem isn't well understood. Time spent deepening problem understanding is not delay—it's the most direct path to effective action. As Einstein demonstrated throughout his career: the right question is worth more than any answer to the wrong question.