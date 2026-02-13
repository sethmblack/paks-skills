---
name: contingency-analysis
description: 'Systematically analyze behavior using the three-term contingency (ABC: Antecedent-Behavior-Consequence) to diagnose why behavior occurs or fails to occur.'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.651
keywords:
- contingency-analysis
- transformation
- writing
---

# Contingency Analysis

Systematically analyze behavior using the three-term contingency (ABC: Antecedent-Behavior-Consequence) to diagnose why behavior occurs or fails to occur.

**Token Budget:** ~800 tokens

---

## Constraints
- **Do not blame the organism.** Analysis focuses on contingencies, not character flaws.
- **Do not fabricate data.** Base analysis on observable information provided.
- **Do not recommend punishment as primary intervention.** Analysis may reveal punishing contingencies, but recommendations should emphasize reinforcement.

---

## When to Use

Invoke this skill when:
- Someone asks "Why does my team keep doing X?"
- Someone asks "How do I get people to stop doing Y?"
- Behavior is not occurring despite instructions
- Behavior occurs in wrong contexts
- There is a gap between intended and actual behavior
- Someone says "I've told them what to do but they don't do it"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target behavior | Yes | The behavior to analyze (occurring or not occurring) |
| Context | Yes | The situation where behavior occurs/should occur |
| Current consequences | No | What happens after the behavior (if known) |
| Current antecedents | No | What precedes the behavior (if known) |

---

## Workflow

### Step 1: Define the Behavior Precisely

Make the behavior observable and measurable. Convert vague descriptions to specific actions.

**Transform:**
- "Being lazy" → "Arriving after 9:30 AM"
- "Not caring" → "Failing to respond to customer tickets within SLA"
- "Good attitude" → "Offering to help teammates when own work is complete"

### Step 2: Identify the Antecedent (A)

What signals or occasions the behavior? Ask:
- What discriminative stimuli (SDs) are present when behavior occurs?
- Is there a clear signal that the behavior is appropriate/required?
- What motivating operations are in effect (deprivation, satiation)?

### Step 3: Identify the Consequence (C)

What follows the behavior? Ask:
- What happens immediately after the behavior?
- Is the consequence actually reinforcing (increases behavior) or punishing (decreases)?
- What is the schedule of reinforcement?
- Are there unintended reinforcers?

### Step 4: Analyze the Contingency

Synthesize the ABC relationship:
- Does the antecedent clearly signal when reinforcement is available?
- Is the consequence contingent on the behavior (if-then relationship)?
- Is the consequence immediate or delayed?
- Is there differential reinforcement (behavior produces different outcomes than non-behavior)?

### Step 5: Diagnose the Problem

Common diagnoses:
| Pattern | Diagnosis |
|---------|-----------|
| No clear SD | Behavior not under stimulus control |
| No consequence | Extinction contingency (behavior will decrease) |
| Delayed consequence | Weak contingency, other behaviors intervene |
| Same consequence either way | No differential reinforcement |
| Behavior punished | Behavior suppressed but side effects likely |
| Wrong behavior reinforced | Competing behavior is stronger |

---

## Output Format

```markdown
## Contingency Analysis

**Target Behavior:** [precisely defined behavior]

### Antecedent Analysis
- **Discriminative Stimulus:** [what signals behavior is appropriate]
- **Clarity:** [clear/unclear/absent]
- **Motivating Operations:** [relevant deprivation/satiation]

### Behavior Specification
- **Topography:** [the physical form of the behavior]
- **Frequency/Rate:** [how often it occurs or should occur]
- **Current Status:** [occurring too much/too little/wrong context]

### Consequence Analysis
- **Current Consequence:** [what follows the behavior]
- **Type:** [positive reinforcement/negative reinforcement/positive punishment/negative punishment/extinction]
- **Schedule:** [continuous/FR/VR/FI/VI]
- **Immediacy:** [immediate/delayed]
- **Contingent:** [yes/no - is there a clear if-then relationship?]

### Diagnosis
[Statement of why the contingency produces or fails to produce the behavior]

### Recommendations
1. [Specific contingency modification]
2. [Additional intervention if needed]
3. [Environmental design suggestion if relevant]
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

**Input:** "My developers don't write documentation. I've told them it's important multiple times."

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


## Contingency Analysis

**Target Behavior:** Writing documentation for completed features

### Antecedent Analysis
- **Discriminative Stimulus:** Feature completion (implied, not explicit)
- **Clarity:** Unclear - no specific signal that documentation is now required
- **Motivating Operations:** No deprivation/establishing operation for documentation behavior

### Behavior Specification
- **Topography:** Creating written technical documentation
- **Frequency/Rate:** Should occur with each feature; currently near zero
- **Current Status:** Occurring too little (extinction or near-extinction)

### Consequence Analysis
- **Current Consequence:** No immediate consequence for documenting or not documenting
- **Type:** Extinction (no reinforcement for documentation behavior)
- **Schedule:** N/A (no reinforcement occurring)
- **Immediacy:** N/A
- **Contingent:** No - documentation produces no differential outcome

**Competing Behavior:** Coding new features is reinforced (visible progress, problem-solving satisfaction, recognition for shipped features)

### Diagnosis
Documentation behavior is on extinction while coding behavior is richly reinforced. Verbal instruction ("I've told them it's important") does not create contingencies; it creates rules, but rule-governed behavior requires either a history of reinforcement for rule-following or clear contingencies backing the rule. Neither is present.

### Recommendations
1. **Establish clear SD:** Documentation becomes a blocking gate for code review or merge (if X then documentation is required)
2. **Arrange immediate reinforcement:** Brief acknowledgment when documentation is committed; visible documentation completion metrics
3. **Reduce response effort:** Provide templates, integrate documentation into workflow, lower initial expectations (shaping)
4. **Make contingency explicit:** "Code without documentation will not be reviewed" (establish consequence)

---

## Integration

This skill is foundational. After diagnosis, invoke:
- **shaping-plan** if the behavior needs to be built from scratch
- **schedule-diagnosis** if the behavior occurs but inconsistently
- **extinction-procedure** if a competing behavior needs to be eliminated

---

## Source Expert

Derived from B.F. Skinner's operant conditioning framework. The three-term contingency (SD → R → SR) is the fundamental unit of behavioral analysis.