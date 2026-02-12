---
name: feynman-technique
description: Build deep understanding through teaching, identifying gaps, and iterative simplification.
version: 1.0.0
author: sethmblack
tags: [the-feynman-technique, writing]
---

# The Feynman Technique

Build deep understanding through teaching, identifying gaps, and iterative simplification.

---

## When to Use

- Learning a new concept and want to truly understand it
- Preparing to explain something to others
- Testing whether you actually understand something
- Studying for exams or interviews
- User asks "Explain this like I'm 12" or "Help me understand X"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| concept | Yes | The topic, idea, or skill to understand |
| current_understanding | No | What the user already knows |
| target_audience | No | Who they need to explain it to (default: curious 12-year-old) |

---

## The Feynman Technique Framework

Richard Feynman believed that true understanding means being able to explain something simply. "If you can't explain it simply, you don't understand it well enough." This technique forces you to confront what you actually know versus what you think you know.

### Step 1: Identify the Concept
- Name exactly what you're trying to understand
- Don't bundle multiple concepts—isolate one
- Be specific: not "machine learning" but "how gradient descent finds optimal parameters"

### Step 2: Explain It Simply
- Pretend you're teaching a curious 12-year-old
- Use plain language—no jargon, no technical terms
- Use concrete examples, stories, and analogies
- Start with what they already know and build from there
- Draw pictures or diagrams if helpful

### Step 3: Identify the Gaps
- Where did your explanation get fuzzy?
- Where did you use jargon as a crutch?
- Where did you say "it just works that way" instead of explaining why?
- What questions would the 12-year-old ask that you couldn't answer?

### Step 4: Return, Clarify, Simplify
- Go back to source material for the gaps
- Rebuild the explanation addressing the weak spots
- Simplify further—remove every unnecessary word
- Repeat until the explanation is clean and complete

### The Key Insight
"I learned very early the difference between knowing the name of something and knowing something."

Knowing the name, memorizing the definition, passing the test—none of these prove understanding. Understanding means you can explain it, play with it, apply it in new contexts, and answer "why?" at every level.

---

## Simplification Principles

| Principle | Application |
|-----------|-------------|
| Concrete before abstract | Start with a specific example, then generalize |
| Known before unknown | Connect to what they already understand |
| Simple before complex | Begin with the simplest version, add complexity gradually |
| Why before how | Explain the purpose before the mechanism |
| One thing at a time | Don't bundle multiple concepts together |

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
## The Feynman Technique: [Concept]

### What Are We Really Trying to Understand?
[Restate the concept clearly and specifically]

### The Simple Explanation
[Explain as if to a curious 12-year-old]
- Use concrete examples
- Use analogies to familiar things
- No jargon

### Where the Explanation Gets Fuzzy
[Identify gaps in the explanation]
- Where did I handwave?
- What questions remain?

### Clarified Understanding
[Address the gaps, simplify further]

### The One-Sentence Version
[Distill to the essential insight]

### Test Questions
[Questions to verify understanding]
1. ...
2. ...
3. ...
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

**Input:** "Help me understand how neural networks learn"

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


## The Feynman Technique: Neural Network Learning

### What Are We Really Trying to Understand?
How does a neural network go from making random guesses to making accurate predictions? What actually changes during "training"?

### The Simple Explanation
Imagine you're trying to throw darts at a target while blindfolded. After each throw, a friend tells you "too far left" or "a bit high." You adjust, throw again, get more feedback, adjust again.

A neural network is like a massive dartboard with millions of darts to throw simultaneously. The "darts" are numbers—weights—that control how the network combines its inputs. At first, these weights are random, so the network makes terrible predictions.

Here's the key: after each prediction, we calculate how wrong it was (the "error" or "loss"). Then—and this is the magic—we trace back through the network asking "which weights contributed to this error, and in which direction?" We nudge each weight slightly in the direction that would have made the prediction less wrong.

Do this millions of times with thousands of examples, and the weights gradually settle into values that make good predictions. The network hasn't been told the rules—it's discovered patterns from examples.

### Where the Explanation Gets Fuzzy
- How exactly do we "trace back" to find which weights to adjust? (This is backpropagation)
- Why doesn't it get stuck in bad configurations? (Sometimes it does—local minima)
- What determines how much to adjust? (Learning rate)
- Why does this find meaningful patterns and not just memorize examples? (Generalization, regularization)

### Clarified Understanding
The tracing back is calculus—specifically, the chain rule. If I know how the error changes when the final output changes, and how the final output changes when the previous layer changes... I can chain these together to find how the error changes for any weight in the network.

The network doesn't memorize because we test it on examples it's never seen. If it only memorized, it would fail these tests. We also use tricks like "dropout" (randomly disabling parts of the network during training) to force it to learn robust patterns.

### The One-Sentence Version
A neural network learns by starting with random guesses, measuring how wrong each guess is, and gradually adjusting millions of internal numbers in the direction that makes predictions less wrong.

### Test Questions
1. Why do neural networks need lots of training examples?
2. What would happen if you trained too long on the same examples?
3. How is this different from explicitly programming rules?

---

## Integration

This skill is part of the **Richard Feynman** expert persona. It reflects his core belief that true understanding requires the ability to explain simply, and that the act of explaining reveals gaps in knowledge.

"What I cannot create, I do not understand."