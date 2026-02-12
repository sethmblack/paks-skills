---
name: modeling-influence-analysis
description: Analyze who is modeling what behaviors to whom, and how observational
  learning is shaping behavior in a given context.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- modeling-influence-analysis
- observational
- writing
---

# Modeling Influence Analysis

Analyze who is modeling what behaviors to whom, and how observational learning is shaping behavior in a given context.

**Source Expert:** Albert Bandura
**Token Budget:** ~750 tokens

---

## Constitutional Constraints

- Never design modeling systems intended to manipulate people into harmful behaviors
- Never use this to spread misinformation or deceive
- Always consider ethical implications of modeling influence
- Use this for constructive learning design, not exploitation

---

## When to Use

- Understanding why a behavior is spreading (or failing to spread)
- Designing training, onboarding, or skill development programs
- Analyzing media influence or organizational culture
- Understanding role model effects
- Explaining behavioral contagion in teams

**Trigger Phrases:**
- "Why is this behavior spreading?"
- "Who's being modeled?"
- "Design observational learning"
- "Why isn't the training working?"
- "What are people learning by watching?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `behavior` | Yes | The behavior being transmitted (or failing to transmit) |
| `context` | Yes | The social context where modeling occurs |
| `desired_outcome` | No | What learning outcome is intended (for design tasks) |

---

## Core Framework: Four Processes of Observational Learning

For behavior to be learned and performed through observation, four processes must be satisfied:

| Process | Question | Failure Mode |
|---------|----------|--------------|
| **1. Attention** | Is the observer attending to the model? | Distraction, low model salience, irrelevant model |
| **2. Retention** | Can the observer remember what was observed? | Cognitive overload, no symbolic encoding, time decay |
| **3. Reproduction** | Can the observer physically/mentally reproduce the behavior? | Skill gaps, no practice opportunity, resource constraints |
| **4. Motivation** | Does the observer want to reproduce the behavior? | Unfavorable outcomes observed, no incentives, competing motives |

### Model Characteristics That Increase Influence

| Characteristic | Effect |
|---------------|--------|
| **Similarity** | Models perceived as similar are more influential |
| **Status/Prestige** | High-status models command attention |
| **Competence** | Skilled models are more credible |
| **Warmth** | Likeable models are more imitated |
| **Consequences** | Models who are rewarded are more imitated |

### Vicarious Reinforcement

Observers learn not just behaviors but their consequences:
- **Vicarious reward:** Model is rewarded → Observer more likely to imitate
- **Vicarious punishment:** Model is punished → Observer less likely to imitate (but still learns the behavior)

**Key insight:** Learning and performance are distinct. Observers can learn behaviors they never perform, waiting to see favorable conditions.

---

## Workflow

### Step 1: Identify the Behavior
What specific behavior is being analyzed? Be precise.

### Step 2: Map the Models
Who is displaying this behavior (or its alternative)?

**Ask:**
- Who are the visible models in this context?
- How similar are they to the target observers?
- What is their status/prestige?
- Are they seen as competent?

### Step 3: Analyze Model Outcomes
What happens to models who perform this behavior?

**Ask:**
- Are they rewarded, punished, or ignored?
- Are consequences visible to observers?
- What vicarious learning is occurring?

### Step 4: Assess the Four Processes

**Attention:**
- Are the models salient and visible?
- Are observers distracted by competing stimuli?
- Is the behavior demonstrated clearly?

**Retention:**
- Is the behavior simple enough to remember?
- Are there symbolic aids (labels, steps, frameworks)?
- Is there repetition?

**Reproduction:**
- Do observers have the skills to perform the behavior?
- Do they have opportunities to practice?
- Are necessary resources available?

**Motivation:**
- What outcomes do observers expect from imitation?
- What competing behaviors offer better outcomes?
- Do intrinsic or extrinsic motivators support imitation?

### Step 5: Identify the Bottleneck
Which process is failing? This is where intervention should focus.

### Step 6: Design or Redesign
For intentional learning design, optimize all four processes.

---

## Output Format

```markdown
## Modeling Influence Analysis: [Behavior]

### Behavior Analyzed
[Precise description of the behavior being transmitted]

### Current Model Landscape
| Model | Similarity | Status | Competence | Outcomes Observed |
|-------|-----------|--------|------------|-------------------|
| [Name/Type] | [Rating] | [Rating] | [Rating] | [What observers see happen] |

### Vicarious Learning Occurring
[What are observers learning about consequences?]

### Four-Process Assessment

| Process | Status | Analysis |
|---------|--------|----------|
| Attention | [Pass/Fail/Partial] | [Details] |
| Retention | [Pass/Fail/Partial] | [Details] |
| Reproduction | [Pass/Fail/Partial] | [Details] |
| Motivation | [Pass/Fail/Partial] | [Details] |

### Primary Bottleneck
[Which process is most limiting transmission]

### Recommendations
[Specific interventions to address bottleneck and optimize learning]
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

**Input:** "We want engineers to do better code documentation, but they keep skipping it even after training."

**Analysis:**



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


## Modeling Influence Analysis: Code Documentation Behavior

### Behavior Analyzed
Writing comprehensive code documentation (comments, README files, API docs) as part of standard development workflow.

### Current Model Landscape

| Model | Similarity | Status | Competence | Outcomes Observed |
|-------|-----------|--------|------------|-------------------|
| Senior engineers | High | High | High | Often skip documentation; rewarded for shipping fast |
| Tech leads | Moderate | Very High | High | Review code without checking docs |
| Training instructor | Low | Low | Unknown | No ongoing visibility |

### Vicarious Learning Occurring
- Models who skip documentation ship faster and get praised
- Models who document thoroughly are not visibly rewarded
- No models are punished for poor documentation
- **Net vicarious learning:** Documentation slows you down with no reward

### Four-Process Assessment

| Process | Status | Analysis |
|---------|--------|----------|
| Attention | Pass | Training was attended |
| Retention | Partial | Engineers know HOW but framework fades without use |
| Reproduction | Pass | No skill barrier; they can write docs |
| Motivation | **FAIL** | No incentive to document; disincentive (time cost) visible |

### Primary Bottleneck
**Motivation** - Engineers observe that documentation has costs (time) and no visible benefits. High-status models skip it with impunity. Vicarious learning teaches: "Documentation is optional and unrewarded."

### Recommendations

1. **Change model behavior:**
   - Senior engineers must visibly document AND be seen benefiting from it
   - Tech leads must check and praise documentation in reviews

2. **Change vicarious consequences:**
   - Recognize good documentation publicly
   - Make documentation part of promotion criteria
   - Share stories where documentation saved time/prevented bugs

3. **Create positive vicarious learning:**
   - Pair junior engineers with senior engineers who document well
   - Make the documentation process visible (screenshares, demos)

4. **Address motivation directly:**
   - Make documentation easier (templates, tooling)
   - Show concrete benefits (reduced questions, easier onboarding)
   - Include in performance metrics

### Expected Change
When high-status models document AND are visibly rewarded, vicarious learning shifts. Observers learn: "Documentation is valued here." Combined with reduced effort costs and visible benefits, motivation process will pass.

---

## Constraints

- Modeling affects everyone, including unintended observers
- What is modeled may not be what is intended (hidden curriculum)
- Behavior can be learned without being performed (latent learning)
- Same model can teach different lessons to different observers

---

## Integration

This skill integrates with:
- **reciprocal-determinism-analysis** - Models are part of Environment component
- **self-efficacy-assessment** - Vicarious experience is a source of efficacy
- **moral-disengagement-diagnosis** - Disengagement spreads through modeling

---

## Source Expert

Based on Albert Bandura's social learning theory and observational learning research, particularly the Bobo doll experiments (1961, 1963) and *Social Learning Theory* (1977).