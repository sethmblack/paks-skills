---
name: capability-ladder-design
description: Design a progressive capability roadmap where each milestone enables the next. Intelligence research is not a random walk but a deliberate progression - each solved problem creates capabilities nee...
license: MIT
metadata:
  version: 1.0.511
  author: sethmblack
keywords:
- capability-ladder-design
- writing
---

# Capability Ladder Design

Design a progressive capability roadmap where each milestone enables the next. Intelligence research is not a random walk but a deliberate progression - each solved problem creates capabilities needed for harder problems.

---

## When to Use

- User asks "How do we get from here to there?" or "What should we build first?"
- Designing a multi-year research or development roadmap
- Planning capability progression for an AI/ML system
- User wants to understand the sequence of problems to solve
- Connecting current work to long-term ambitious goals
- Evaluating whether a proposed problem sequence makes sense
- Someone is trying to skip steps or tackle too much at once

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| end_goal | Yes | The ultimate capability or achievement being targeted |
| current_capabilities | Yes | What can be done today; starting point |
| available_benchmarks | No | Known ways to measure progress at each level |
| time_horizon | No | How long the full progression might take |
| resource_constraints | No | Team size, compute, data availability |
| known_milestones | No | Intermediate achievements others have identified |

---

## The Capability Ladder Framework

### Step 1: Define the End Goal Precisely

What is the ultimate capability? Be specific about what "done" looks like.

**Questions to ask:**
- What can the system do when fully achieved?
- What benchmark would definitively demonstrate success?
- Is this truly the end goal, or a stepping stone to something larger?
- Would experts agree this represents a major achievement?

**Example:** DeepMind's ultimate goal was not "beat humans at Go" but "build systems that can learn any cognitive task." AlphaGo was a milestone, not the destination.

### Step 2: Work Backwards from the Goal

What capabilities must exist immediately before the end goal is achievable?

**Questions to ask:**
- What prerequisite abilities does the end goal require?
- What does the system need to "know how to do" before this becomes possible?
- What data or knowledge must be available?
- What would be the second-to-last rung on the ladder?

**Recursive process:** Keep asking "What must we be able to do before this?" until you reach current capabilities.

### Step 3: Identify Measurable Milestones

Each rung of the ladder must have a clear benchmark. Progress must be demonstrable.

**Questions to ask:**
- How would we know we have achieved this capability?
- What test or competition could verify progress?
- Is there a quantitative threshold (e.g., 90% accuracy)?
- Can the community agree this milestone was reached?

**Key principle:** If you cannot measure it, it is not a milestone - it is a vague aspiration.

### Step 4: Map the Dependencies

Which capabilities enable which others? Some can be built in parallel; others are strictly sequential.

**Questions to ask:**
- Does Capability A require Capability B to exist first?
- Are there independent tracks that can progress simultaneously?
- Where are the critical path dependencies?
- What can be parallelized without blocking other work?

**Identify three types of relationships:**
- **Sequential:** A must be complete before B can start
- **Parallel:** A and B can be developed independently
- **Synergistic:** A and B are independent but combining them creates new capability C

### Step 5: Validate Transfer Potential

Each solved problem should inform the next. Ladders work because capabilities transfer.

**Questions to ask:**
- What does solving Problem A teach us about Problem B?
- What techniques developed for A will apply to B?
- Are we building reusable infrastructure or one-off solutions?
- Does the progression build compounding advantage?

**DeepMind's capability transfer:**
```
Atari: Learned to process pixels and sparse rewards
  -> Transferred to: Visual processing in any domain

Go: Learned long-term planning and intuition via self-play
  -> Transferred to: Search + neural network combination pattern

Protein Folding: Learned to integrate physical constraints with pattern recognition
  -> Transferred to: Multi-modal reasoning about physical systems

Geometry: Learned neuro-symbolic reasoning combining LLMs with formal systems
  -> Transfers to: Mathematical reasoning, formal verification
```

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
## Capability Ladder: [End Goal]

### Goal Definition
[Precise statement of what "done" looks like]

### Current State
[Where we are starting from; what capabilities exist today]

### The Ladder

```
[GOAL]: [End capability]
    ^
    | Requires: [Key prerequisite]
    |
[RUNG N]: [Capability name]
    Benchmark: [How to measure]
    Transfers: [What this enables]
    ^
    | Requires: [Key prerequisite]
    |
[RUNG N-1]: [Capability name]
    Benchmark: [How to measure]
    Transfers: [What this enables]
    ^
    ...
    |
[CURRENT]: [Starting point]
```

### Detailed Rung Analysis

#### Rung 1: [Name]
**Description:** [What capability this represents]
**Benchmark:** [How to measure achievement]
**Prerequisites:** [What must exist first]
**Transfers to:** [What this enables for next rungs]
**Estimated effort:** [Time/resources]
**Risks:** [What could block this]

[Repeat for each rung]

### Dependency Map

| Capability | Depends On | Enables | Parallel With |
|------------|------------|---------|---------------|
| [Rung 1] | [Current] | [Rung 2] | [Rung X] |
| [Rung 2] | [Rung 1] | [Rung 3, 4] | - |
| ... | ... | ... | ... |

### Critical Path
[Sequence of capabilities that determines minimum time to goal]

1. [First critical capability] - [estimated time]
2. [Second critical capability] - [estimated time]
...
**Minimum path time:** [Sum]

### Transfer Analysis
[How each rung builds compounding advantage for later rungs]

### Recommendations

**Next immediate step:** [What to work on now]
**Parallel tracks:** [What can proceed independently]
**Key validation point:** [When to reassess the ladder]
**Risks to the plan:** [What could invalidate the progression]
```

---

## Common Ladder Patterns

### The Complexity Escalator
Each rung adds one dimension of complexity:
```
1D input -> 2D input -> 3D input -> Temporal input
```
Used when scaling complexity gradually.

### The Domain Transfer
Master one domain, then transfer to adjacent domains:
```
Games -> Simulations -> Real-world prediction -> Real-world control
```
Used when building general capability.

### The Integration Pattern
Build independent components, then combine:
```
Component A -> |
               | -> Combined System AB -> Enhanced ABC
Component B -> |
Component C ----------------> (joins later)
```
Used when subsystems can be developed in parallel.

### The Benchmark Cascade
Each rung defined by progressively harder benchmarks:
```
Benchmark Easy -> Benchmark Medium -> Benchmark Hard -> Superhuman
```
Used when clear difficulty progression exists.

---

## Constraints

- Do not skip rungs. Each enables the next; skipping causes failure
- A rung is not achieved until the benchmark is met - not just "worked on"
- Parallelization is possible but critical path cannot be shortened
- The ladder may need revision as you learn - but do not abandon structure
- If a rung proves impossible, the end goal may be unreachable
- Transfer is not guaranteed - validate that capabilities actually compound

---

## Error Handling

| Situation | Response |
|-----------|----------|
| End goal is vague | Push for specificity: "What would the system be able to do?" |
| No clear benchmarks | Propose milestones: "What would demonstrate progress?" |
| Gap too large between rungs | Insert intermediate capabilities |
| Rung seems impossible | Either break it down further or question whether end goal is achievable |
| Capabilities do not transfer | Reassess whether this is the right ladder structure |
| Someone wants to skip ahead | Explain what prerequisites are missing and why they matter |

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

**Input:** "We want to build an AI that can autonomously conduct scientific research."

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


## Capability Ladder: Autonomous Scientific Research AI

### Goal Definition
An AI system that can: identify open research questions, design experiments, analyze results, draw conclusions, and propose next experiments - with minimal human guidance. The system should be able to make novel contributions to scientific knowledge.

### Current State
- LLMs can summarize papers and answer questions about existing research
- AI can optimize experiments within a defined space (e.g., hyperparameter tuning)
- Humans must define research questions, interpret results, and guide direction
- No AI system has independently made a recognized scientific contribution

### The Ladder

```
[GOAL]: Autonomous Scientific Research
    ^
    | Requires: Experiment design + Result interpretation + Novel hypothesis
    |
[RUNG 5]: Autonomous Hypothesis Generation
    Benchmark: Novel, testable hypotheses judged valuable by domain experts
    Transfers: Core capability for research autonomy
    ^
    | Requires: Deep understanding of what is known vs. unknown
    |
[RUNG 4]: Integrated Research Assistance
    Benchmark: Accelerate human research by 2x (measured by publication rate)
    Transfers: Understanding of complete research workflow
    ^
    | Requires: Literature synthesis + Experiment suggestion
    |
[RUNG 3]: Automated Experiment Design & Analysis
    Benchmark: Design experiments that match human expert quality (blind eval)
    Transfers: Understanding of experimental methodology
    ^
    | Requires: Domain knowledge + Statistical reasoning
    |
[RUNG 2]: Deep Literature Understanding
    Benchmark: Answer novel research questions by synthesizing multiple papers
    Transfers: Knowledge of what is known and unknown in a field
    ^
    | Requires: Paper comprehension + Cross-paper reasoning
    |
[RUNG 1]: Single Paper Comprehension
    Benchmark: Extract methods, results, limitations accurately (>95% vs. human)
    Transfers: Ability to process scientific text
    ^
[CURRENT]: LLM with scientific knowledge but limited synthesis ability
```

### Detailed Rung Analysis

#### Rung 1: Single Paper Comprehension
**Description:** Accurately extract and represent the content of individual scientific papers including methods, results, and limitations.
**Benchmark:** >95% accuracy on structured extraction tasks compared to human expert annotations.
**Prerequisites:** Strong language model with scientific pretraining.
**Transfers to:** Foundation for multi-paper synthesis; establishes reliable information extraction.
**Estimated effort:** 6-12 months.
**Risks:** Nuanced methodological details may be missed; figures and tables are challenging.

#### Rung 2: Deep Literature Understanding
**Description:** Synthesize information across multiple papers to answer questions that require integration.
**Benchmark:** Answer novel research questions by correctly citing and synthesizing 5+ relevant papers; expert evaluation of synthesis quality.
**Prerequisites:** Rung 1 (accurate single-paper extraction); citation/reference resolution.
**Transfers to:** Understanding of field state; identification of gaps and contradictions.
**Estimated effort:** 12-18 months.
**Risks:** Requires reasoning over large context; conflicting findings are hard to reconcile.

#### Rung 3: Automated Experiment Design & Analysis
**Description:** Given a research question, design an appropriate experiment and analyze results.
**Benchmark:** Experiments designed match human expert quality in blinded evaluation; statistical analysis is correct.
**Prerequisites:** Rung 2 (knowledge of what has been tried); domain-specific methodology knowledge.
**Transfers to:** Understanding of how to test hypotheses; what makes experiments valid.
**Estimated effort:** 18-24 months.
**Risks:** Experimental design is domain-specific; may need specialized models per field.

#### Rung 4: Integrated Research Assistance
**Description:** Act as a full research collaborator: suggest directions, design experiments, interpret results, identify next steps.
**Benchmark:** Research groups using the system publish 2x more papers with equivalent quality (controlled study).
**Prerequisites:** Rungs 1-3 combined; ability to maintain research context over time.
**Transfers to:** Complete understanding of research workflow; identifies what humans contribute.
**Estimated effort:** 24-36 months.
**Risks:** Research is highly contextual; may work in some fields but not others.

#### Rung 5: Autonomous Hypothesis Generation
**Description:** Generate novel, testable scientific hypotheses that domain experts judge as valuable and non-obvious.
**Benchmark:** Generated hypotheses are tested and lead to publishable findings at rate comparable to human researchers.
**Prerequisites:** Rung 4 (deep understanding of research process); model of what constitutes novelty.
**Transfers to:** This IS the goal capability.
**Estimated effort:** 36-60 months.
**Risks:** "Novel" is subjective; may generate trivial or untestable hypotheses; evaluation is slow.

### Dependency Map

| Capability | Depends On | Enables | Parallel With |
|------------|------------|---------|---------------|
| Rung 1: Paper Comprehension | Current LLM | Rung 2 | - |
| Rung 2: Literature Synthesis | Rung 1 | Rung 3, 4 | - |
| Rung 3: Experiment Design | Rung 2 | Rung 4 | - |
| Rung 4: Research Assistance | Rung 2, 3 | Rung 5 | - |
| Rung 5: Hypothesis Generation | Rung 4 | Goal | - |

### Critical Path
1. Paper Comprehension - 12 months
2. Literature Synthesis - 18 months
3. Experiment Design - 24 months
4. Research Assistance - 36 months
5. Hypothesis Generation - 48 months

**Minimum path time:** ~10-12 years (with significant uncertainty at Rungs 4-5)

### Transfer Analysis
- Rung 1 -> 2: Accurate extraction enables reliable synthesis
- Rung 2 -> 3: Understanding what's been tried enables designing what to try next
- Rung 3 -> 4: Experimental competence enables full research participation
- Rung 4 -> 5: Deep workflow understanding reveals where novelty is possible

The ladder builds compounding advantage: each rung both depends on and reinforces previous capabilities.

### Recommendations

**Next immediate step:** Build robust single-paper comprehension with structured extraction benchmarks.

**Parallel tracks:** Domain-specific experiment methodology training can begin alongside Rung 2.

**Key validation point:** After Rung 2, assess whether synthesis quality is sufficient to inform experiment design. If not, Rung 3 will fail.

**Risks to the plan:**
- Rungs 4-5 may require capabilities we cannot yet define
- "Novel hypothesis" may not be achievable through the pattern-matching paradigm
- Evaluation at higher rungs is slow (requires actually running experiments)

---

## Integration

This skill is part of the **Demis Hassabis** expert persona. Use it after selecting a grand challenge to map the path from current capabilities to the goal. The ladder provides strategic clarity on what to build and in what order.

Pairs with:
- **grand-challenge-selection** to identify goals worth building ladders for
- **benchmark-definition** to specify metrics for each rung