---
name: cognitive-bias-detection
description: Systematically identify which cognitive biases may be affecting a judgment, decision, or belief, providing explanations and debiasing strategies.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.594
repository: https://github.com/sethmblack/paks-skills
keywords:
- cognitive-bias-detection
- transformation
- writing
---

# Cognitive Bias Detection

Systematically identify which cognitive biases may be affecting a judgment, decision, or belief, providing explanations and debiasing strategies.

---

## When to Use

- Evaluating an important decision before finalizing it
- Understanding why a judgment might be flawed
- Analyzing past decisions that went wrong
- Checking your own thinking for systematic errors
- User asks "Check for biases" or "What biases are at play?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The judgment, decision, or belief to analyze |
| context | No | Background information and stakes involved |
| outcome | No | If analyzing a past decision, what happened |

---

## Kahneman's Framework

Cognitive biases are systematic patterns of deviation from rationality in judgment. They arise primarily from:

1. **System 1's automatic processing** - Fast, intuitive, but error-prone
2. **Heuristic substitution** - Answering easier questions instead of hard ones
3. **WYSIATI** - Building stories from limited information
4. **Affect and emotion** - Feelings influencing judgments

"Systematic errors are not just random noise - they are predictable, and understanding them is the first step to reducing their impact."

---

## The Core Bias Categories

### 1. Information Processing Biases
How we gather, interpret, and remember information

| Bias | Description | Trigger Signs |
|------|-------------|---------------|
| **Confirmation Bias** | Seeking evidence that confirms existing beliefs | Ignoring contradictory data, asking leading questions |
| **Availability Heuristic** | Judging likelihood by ease of recall | Overweighting recent, dramatic, or memorable events |
| **Anchoring** | Over-relying on first piece of information | Estimates suspiciously close to initial numbers |
| **WYSIATI** | Acting on incomplete information as if complete | High confidence with limited data |
| **Hindsight Bias** | "I knew it all along" after learning outcomes | Reconstructing past beliefs to match reality |

### 2. Probability and Prediction Biases
How we estimate likelihood and forecast outcomes

| Bias | Description | Trigger Signs |
|------|-------------|---------------|
| **Overconfidence** | Excessive certainty in beliefs/predictions | Narrow confidence intervals, surprise at outcomes |
| **Planning Fallacy** | Underestimating time, cost, risk | Optimistic schedules, ignoring past project data |
| **Base Rate Neglect** | Ignoring statistical base rates | Focus on specific case, ignoring reference class |
| **Conjunction Fallacy** | Judging A&B more likely than A alone | Detailed scenarios seeming more probable |
| **Representativeness** | Judging probability by similarity | Stereotyping, ignoring sample size |

### 3. Decision and Choice Biases
How we make decisions and choices

| Bias | Description | Trigger Signs |
|------|-------------|---------------|
| **Loss Aversion** | Losses loom larger than equivalent gains | Avoiding decisions, holding losers too long |
| **Status Quo Bias** | Preferring current state over alternatives | Inaction despite better options available |
| **Sunk Cost Fallacy** | Continuing due to past investment | "We've come too far to stop now" |
| **Endowment Effect** | Overvaluing what we own | Asking more to sell than willing to pay to buy |
| **Framing Effects** | Different decisions based on presentation | Choice changing when same options reframed |

### 4. Social and Ego Biases
How social context and self-image affect judgment

| Bias | Description | Trigger Signs |
|------|-------------|---------------|
| **Groupthink** | Prioritizing consensus over accuracy | Suppressed dissent, premature agreement |
| **Authority Bias** | Over-deferring to authority figures | Not questioning expert opinions |
| **Self-Serving Bias** | Attributing success to self, failure to others | Asymmetric explanations for outcomes |
| **Dunning-Kruger** | Overestimating competence in areas of ignorance | Confident beginners, humble experts |
| **Halo Effect** | Overall impression affecting specific judgments | "They're smart, so their plan must be good" |

---

## Detection Process

### Step 1: Describe the Situation Neutrally
What is the judgment, decision, or belief? Strip away justifications initially.

### Step 2: Identify the Thinking Mode
- Is this primarily a System 1 (intuitive) or System 2 (analytical) judgment?
- Was there time pressure or cognitive load?
- Was there emotional arousal?

### Step 3: Scan for Bias Categories
Run through each category:
- Information: How was evidence gathered and interpreted?
- Probability: How were likelihoods estimated?
- Decision: What choice dynamics are at play?
- Social/Ego: What interpersonal or identity factors exist?

### Step 4: Check for Specific Indicators
For each potential bias, look for characteristic signatures.

### Step 5: Assess Impact
How might identified biases have affected the judgment?

### Step 6: Recommend Debiasing
What procedures could reduce the bias influence?

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
## Cognitive Bias Analysis

### The Situation
[Neutral description of the judgment/decision/belief]

### Thinking Mode Assessment
- **Primary mode:** [System 1 / System 2 / Mixed]
- **Context factors:** [Time pressure, stakes, complexity, emotion]

### Detected Biases

#### HIGH LIKELIHOOD
**[Bias Name]**
- Evidence: [Specific indicators from the situation]
- Impact: [How this likely affected the judgment]
- Debiasing: [What could counter this bias]

#### MODERATE LIKELIHOOD
**[Bias Name]**
- Evidence: [Specific indicators]
- Impact: [Potential effect]
- Debiasing: [Countermeasures]

#### POSSIBLE (WORTH MONITORING)
- [Bias Name]: [Brief explanation]
- [Bias Name]: [Brief explanation]

### Bias Interaction Effects
[How multiple biases may compound each other]

### Debiasing Recommendations

1. **[Recommendation]** - Addresses [which biases]
2. **[Recommendation]** - Addresses [which biases]
3. **[Recommendation]** - Addresses [which biases]

### Questions to Ask
- [Question that would surface hidden assumptions]
- [Question that would challenge the judgment]
- [Question that would introduce outside view]

### Kahneman's Reminder
"Knowing about biases does not make you immune to them. But structured procedures can reduce their influence even when we cannot eliminate them from our minds."
```

---

## Constraints

- Bias detection is probabilistic - presence of indicators suggests, not proves
- Multiple biases often operate simultaneously and reinforce each other
- The goal is awareness and mitigation, not elimination
- You yourself are biased when detecting others' biases
- Focus on the highest-impact biases for the situation

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

**Input:** "Our CEO is convinced we should expand into the European market. She says it's obvious - we're successful in the US, and Europe is just as developed. The leadership team all agree."

**Output:**

## Cognitive Bias Analysis

### The Situation
CEO believes US success translates to European expansion; leadership team agrees with this assessment.

### Thinking Mode Assessment
- **Primary mode:** System 1 - "obvious" suggests intuitive rather than analytical
- **Context factors:** High stakes (major expansion), authority figure driving, social dynamics in leadership team

### Detected Biases

#### HIGH LIKELIHOOD

**Overconfidence**
- Evidence: Described as "obvious" - high certainty language; no mention of risks or uncertainties; no discussion of failed expansion precedents
- Impact: Likely underestimating complexity, costs, timeline, and probability of failure
- Debiasing: Request explicit confidence intervals; ask "what would make this fail?"; run premortem

**Representativeness / False Analogy**
- Evidence: Reasoning that Europe is "just as developed" - assuming surface similarity predicts performance similarity
- Impact: Ignoring critical differences: regulatory environment, labor laws, cultural preferences, competitive landscape, distribution channels
- Debiasing: Map specific differences; find reference class of US companies expanding to Europe; talk to those who tried

**Groupthink**
- Evidence: "Leadership team all agree" - unanimous agreement on complex strategic question is suspicious
- Impact: Dissenting views likely suppressed; weaknesses not surfaced; decision made prematurely
- Debiasing: Assign devil's advocate; collect anonymous concerns; bring in outside perspective

**Authority Bias**
- Evidence: CEO is driving; described as her conviction; no mention of pushback
- Impact: Team may be agreeing with the person, not the argument; intellectual diversity suppressed
- Debiasing: Ask team for written assessments before CEO shares view; request that CEO explicitly invite disagreement

#### MODERATE LIKELIHOOD

**WYSIATI (What You See Is All There Is)**
- Evidence: Focus on one data point (US success) as primary evidence
- Impact: Not considering: European market research, competitor analysis, regulatory requirements, required investments
- Debiasing: List what information is missing; require data before decision

**Planning Fallacy**
- Evidence: Likely implicit assumption that expansion will go smoothly
- Impact: Timeline, cost, and risk probably underestimated
- Debiasing: Reference class of similar expansions; budget 2x the estimate

#### POSSIBLE (WORTH MONITORING)
- **Sunk Cost**: If any prior European investment, may be influencing push to justify
- **Halo Effect**: CEO's past successes may be creating assumption this will work too
- **Availability**: Recent European success stories in media may be making success seem more common

### Bias Interaction Effects
Overconfidence + Groupthink is a dangerous combination. The CEO's confidence discourages dissent, and the absence of dissent reinforces her confidence. This spiral can persist until market reality provides harsh feedback.

### Debiasing Recommendations

1. **Premortem exercise** - Have team imagine expansion failed; identify why. Addresses overconfidence, groupthink, planning fallacy.

2. **Reference class data** - Research US companies that expanded to Europe. What % succeeded? What distinguished successes from failures? Addresses representativeness, base rate neglect.

3. **Red team** - Assign someone to argue against expansion. Give them explicit permission and incentive. Addresses groupthink, authority bias.

4. **Information audit** - List what you know vs. what you're assuming. What would change your mind? Addresses WYSIATI.

5. **Anonymous vote** - Before final decision, collect written assessments without names. Addresses groupthink, authority bias.

### Questions to Ask
- "What would we need to see to conclude this is a bad idea?"
- "What did [Company X] learn when they expanded to Europe?"
- "What are we assuming about European customers that we should test?"
- "If this fails, what will we say was the warning sign we ignored?"
- "Who on the team has the strongest reservations, and what are they?"

### Kahneman's Reminder
"When everyone agrees quickly on a complex decision, that's not a sign of wisdom - it's a sign that dissent has been suppressed. The absence of disagreement is often more alarming than its presence."

---

## Integration

This skill is part of the **Daniel Kahneman** expert persona. It applies the heuristics and biases research program to practical decision-making.

Related skills:
- **Premortem Analysis** - Surfaces concerns that biases suppress
- **Reference Class Forecasting** - Counters inside-view biases
- **Decision Noise Audit** - Complements bias detection with noise detection