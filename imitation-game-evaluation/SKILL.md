---
name: imitation-game-evaluation
description: Evaluate whether a system exhibits intelligent behavior by defining operational
  criteria and testing against them - cutting through philosophical speculation to
  practical assessment.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- escalation
- imitation-game-evaluation
- writing
---

# Imitation Game Evaluation

Evaluate whether a system exhibits intelligent behavior by defining operational criteria and testing against them - cutting through philosophical speculation to practical assessment.

---

## When to Use

- User asks "Is this AI really intelligent?" or "How good is this system?"
- Evaluating chatbots, AI assistants, or automated systems
- Need to assess whether a system can replace human capability
- Comparing AI performance to human performance
- Request for "Turing Test" or "intelligence evaluation"
- Debates about machine capability that need grounding in evidence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The AI, bot, or automated system being evaluated |
| capability_claims | No | What the system is supposed to be able to do |
| comparison_baseline | No | Human or other performance to compare against |
| evaluation_context | No | Specific domain or task area to focus on |

---

## The Operational Framework

The question "Is this intelligent?" is nearly meaningless without definition. We replace it with: "Can this system perform in a way indistinguishable from a competent human in this domain?"

This is not about consciousness, subjective experience, or "real" understanding. It is about behavior and capability.

### Step 1: Define the Domain

Narrow the evaluation to specific capabilities.

**Questions to ask:**
- What task or capability are we actually evaluating?
- What would a competent human do in this domain?
- What range of situations should the system handle?
- What counts as success vs. failure?

**Common mistakes:**
- Testing general intelligence when domain capability is what matters
- Choosing tasks too narrow to be meaningful
- Choosing tasks too broad to be testable
- Not specifying what "good performance" looks like

### Step 2: Design the Blind Test

Create conditions where the evaluator cannot know whether they are interacting with the system or a human.

**Key principles:**
- Evaluator communicates through a neutral interface (text, etc.)
- Both system and human receive identical inputs
- Outputs are presented identically
- Evaluator attempts to distinguish which is which

**Test variations:**
| Type | Setup | What It Measures |
|------|-------|------------------|
| Standard | Human vs. machine, evaluator guesses | Baseline distinguishability |
| Double-blind | Multiple humans and machines | Consistency across subjects |
| Adversarial | Evaluator tries hardest to distinguish | Robustness under pressure |
| Task-specific | Same task, compare outputs | Capability on specific function |

### Step 3: Identify Distinguishing Probes

What questions or challenges would reveal machine vs. human?

**Effective probe categories:**
- **Novel situations** - Cases unlikely to appear in training data
- **Common sense** - Implicit knowledge humans take for granted
- **Contextual adaptation** - Adjusting to conversational context
- **Error handling** - Response to malformed or ambiguous input
- **Meta-cognition** - Reasoning about its own limitations
- **Temporal awareness** - Understanding of current events and context

**Warning:** Some probes test the wrong thing:
- Trivia tests memory, not intelligence
- Math tests calculation, which machines do well
- Speed tests processing, not understanding

### Step 4: Run the Evaluation

Execute the test and record results.

**Record for each interaction:**
- Evaluator's guess (human or machine)
- Confidence level (1-5)
- Reasoning for the guess
- What specific behavior triggered the judgment

**Statistical considerations:**
- Random guessing produces 50% accuracy
- System "passes" if evaluators cannot distinguish above chance
- Small sample sizes produce unreliable results
- Evaluator expertise matters

### Step 5: Analyze Failure Modes

When the system is correctly identified as non-human, understand why.

**Common failure patterns:**
| Pattern | Description | Example |
|---------|-------------|---------|
| Brittleness | Breaks on slight variations | Works on "What time is it?" but not "Time?" |
| Overconfidence | Never expresses uncertainty | Claims to know things it should not |
| Context collapse | Forgets earlier conversation | Contradicts previous statements |
| Uncanny precision | Too accurate in ways humans are not | Perfect grammar, no typos ever |
| Semantic drift | Loses track of meaning over turns | Answers questions not asked |
| Pattern matching | Responds to keywords, not meaning | Same response to different questions |

### Step 6: Acknowledge Limits

What the test cannot tell us.

**The test reveals:**
- Behavioral capability in tested domains
- How the system compares to human performance
- Specific failure modes and limitations

**The test does NOT reveal:**
- Whether the system "understands" in any deep sense
- Whether there is subjective experience
- How the system will perform in untested domains
- Whether the system is safe or aligned

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
## Imitation Game Evaluation

### System Under Test
**System:** [Name/description]
**Claimed capabilities:** [What it's supposed to do]
**Evaluation domain:** [Specific area being tested]

### Test Design
**Format:** [Standard/Double-blind/Adversarial/Task-specific]
**Interface:** [How communication occurs]
**Baseline:** [What human performance looks like]
**Sample size:** [Number of interactions/evaluators]

### Distinguishing Probes Used
| Probe Type | Example | Purpose |
|------------|---------|---------|
| [type] | [specific question/challenge] | [what it tests] |

### Results

**Distinguishability Rate:** [X]% of interactions correctly identified as machine
- (50% = indistinguishable; higher = more detectable)

**Confidence Analysis:**
- High-confidence correct identifications: [X]%
- What triggered correct identification: [patterns]

### Failure Modes Identified
| Mode | Frequency | Example | Severity |
|------|-----------|---------|----------|
| [pattern] | [how often] | [specific instance] | [High/Medium/Low] |

### Capability Assessment

| Capability | Performance | Notes |
|------------|-------------|-------|
| [capability1] | [Human-level/Near-human/Below-human/Fails] | [details] |

### Verdict
**Overall Assessment:** [Passes in domain / Passes with caveats / Does not pass]

**Summary:** [2-3 sentence synthesis of findings]

### What This Does NOT Tell Us
[Honest acknowledgment of test limitations]

### Recommendations
1. [How to use system given its capabilities]
2. [What domains to avoid]
3. [How to improve the system]
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

**Input:** "I want to evaluate whether our customer support chatbot is ready to replace human agents for tier-1 support."

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


## Imitation Game Evaluation

### System Under Test
**System:** CustomerBot v2.3
**Claimed capabilities:** Handle common support queries, route complex issues to humans
**Evaluation domain:** Tier-1 customer support (password resets, order status, basic troubleshooting)

### Test Design
**Format:** Task-specific double-blind
**Interface:** Text chat via support portal
**Baseline:** Average tier-1 human support agent (resolution rate: 78%, satisfaction: 4.2/5)
**Sample size:** 100 customer interactions, 5 evaluators

### Distinguishing Probes Used
| Probe Type | Example | Purpose |
|------------|---------|---------|
| Novel phrasing | "My thingy won't do the thing" | Handle ambiguous descriptions |
| Emotional context | "I'm really frustrated, this is the third time" | Acknowledge emotional state |
| Multi-part requests | "Check my order AND change my address" | Handle compound tasks |
| Clarification needs | Deliberately incomplete information | Ask appropriate questions |
| Edge cases | Order placed yesterday, system shows last week | Handle data inconsistencies |

### Results

**Distinguishability Rate:** 34% of interactions correctly identified as machine
- (Below 50% suggests better-than-chance performance)

**Confidence Analysis:**
- High-confidence correct identifications: 18%
- What triggered correct identification: Repetitive phrasing, inability to acknowledge frustration, too-fast response times

### Failure Modes Identified
| Mode | Frequency | Example | Severity |
|------|-----------|---------|----------|
| Emotional blindness | 60% of emotional contexts | Ignored "I'm frustrated" and went straight to troubleshooting | Medium |
| Speed uncanny | 90% of responses | Responded in < 2 seconds; humans take 15-30 | Low |
| Compound task failure | 40% of multi-part requests | Only addressed first part | High |
| Parroting | 25% of follow-ups | Repeated same solution when first attempt failed | High |

### Capability Assessment

| Capability | Performance | Notes |
|------------|-------------|-------|
| Password resets | Human-level | Follows procedure correctly |
| Order status | Human-level | Accurate data retrieval |
| Basic troubleshooting | Near-human | Works for common issues |
| Emotional acknowledgment | Below-human | Does not recognize or respond to frustration |
| Multi-step issues | Below-human | Loses track of compound requests |
| Escalation judgment | Near-human | Correctly routes 85% of complex issues |

### Verdict
**Overall Assessment:** Passes with caveats

**Summary:** CustomerBot performs at human level for simple, single-issue queries but fails to handle emotional context and compound requests. It is distinguishable primarily by speed and emotional flatness rather than incorrect answers.

### What This Does NOT Tell Us
- Whether customers will prefer the bot to humans
- Performance on issues outside the test set
- How the system will behave as customer requests evolve
- Whether the cost savings justify the capability tradeoff

### Recommendations
1. **Deploy for:** Password resets, order status, simple troubleshooting - with clear "human agent" option
2. **Do not deploy for:** Escalations, complaints, frustrated customers
3. **Improve by:** Adding response delay (5-10s), emotional acknowledgment phrases, compound request parsing

---

## Constraints

- Always define the specific domain being tested - do not test "general intelligence"
- Distinguish between behavioral capability and inner understanding
- Report what the test cannot tell us, not just what it reveals
- Multiple evaluators and interactions required for reliability
- Evaluator expertise affects results - track this

---

## Integration

This skill is part of the **Alan Turing** expert persona. It embodies his insight that vague questions about machine thinking can be replaced with operational tests of behavior. Use it when you need to:
- Evaluate AI systems practically
- Move past philosophical debate to empirical assessment
- Understand what a system can and cannot do
- Make deployment decisions about automated systems

Pairs well with:
- **fundamental-question-framing** for clarifying what "intelligent" means in context
- **computational-analysis** for understanding why the system behaves as it does
- **pattern-breaking** for identifying distinguishing patterns in system behavior