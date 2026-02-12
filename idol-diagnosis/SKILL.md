---
name: idol-diagnosis
description: Systematically identify which of Francis Bacon's Four Idols are obstructing clear thinking in a given situation. Surfaces hidden biases, language confusions, individual prejudices, and inherited dogmas before they corrupt inquiry.
version: 1.0.0
author: sethmblack
tags: [idol-diagnosis, writing]
---

# Idol Diagnosis

Systematically identify which of Francis Bacon's Four Idols are obstructing clear thinking in a given situation. Surfaces hidden biases, language confusions, individual prejudices, and inherited dogmas before they corrupt inquiry.

---

## When to Use

- Team cannot agree despite having the same information
- Decisions keep failing in ways nobody anticipated
- Discussion is going in circles without resolution
- User asks "What are we failing to see?" or "Why can't we think clearly about this?"
- Evaluating why a strategy or analysis went wrong
- Before any major decision or investigation to clear mental obstacles
- Request to "diagnose the idols" or "what's obstructing our thinking?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The decision, problem, or inquiry being examined |
| context | No | Background information about the people and history involved |
| symptoms | No | Observable signs that thinking may be obstructed (disagreements, circular logic, unexpected failures) |

---

## The Four Idols Framework

### Idol of the Tribe (Idola Tribus)
**Source:** Human nature itself - errors common to all humanity

| Error Pattern | Description | Diagnostic Question |
|--------------|-------------|---------------------|
| Confirmation bias | Noting instances that support beliefs, ignoring contradictions | "What evidence against our view have we dismissed?" |
| Pattern imposition | Seeing order and regularity where none exists | "Are we finding patterns because they exist or because we want them?" |
| Anthropomorphism | Projecting human purposes onto systems or nature | "Are we assuming intent where there may be none?" |
| Emotional reasoning | Being moved by striking instances over cumulative evidence | "Are we overweighting vivid recent events?" |
| Wish fulfillment | Believing what we want to be true | "What would we believe if we had no stake in the outcome?" |

### Idol of the Cave (Idola Specus)
**Source:** Individual experience, education, and temperament

| Error Pattern | Description | Diagnostic Question |
|--------------|-------------|---------------------|
| Education bias | What we were taught shapes what we can perceive | "What training is shaping how we see this?" |
| Specialty blindness | Seeing everything through one's expertise | "What would someone from a different field see?" |
| Temperament | Some minds seek differences, others similarities | "Are we predisposed to find conflict or consensus?" |
| Authority worship | Overvaluing those we respect | "Whose opinion are we accepting without examination?" |
| First impression anchoring | Early learning has disproportionate influence | "What was our first take, and are we still anchored to it?" |

### Idol of the Marketplace (Idola Fori)
**Source:** Language and communication - Bacon called these "the greatest nuisances of them all"

| Error Pattern | Description | Diagnostic Question |
|--------------|-------------|---------------------|
| Naming the nonexistent | Words that name things that do not exist | "Are we debating something that isn't real?" |
| Vague terms | Words used inconsistently or without clear meaning | "When we say X, do we all mean the same thing?" |
| Failed definitions | Formal definitions that do not resolve confusion | "Have our definitions actually clarified anything?" |
| Miscommunication | Same words, different meanings | "Are we having the same conversation?" |
| Euphemism/dysphemism | Language that conceals rather than reveals | "What are we hiding with our word choices?" |

### Idol of the Theatre (Idola Theatri)
**Source:** Received philosophies, dogmas, and methodologies - "so many stage plays"

| Error Pattern | Description | Diagnostic Question |
|--------------|-------------|---------------------|
| Sophistic systems | Systems built on insufficient observations | "What evidence actually supports this framework?" |
| Narrow empiricism | Systems built on too narrow a base | "Are we generalizing from too few cases?" |
| Superstitious thinking | Philosophy corrupted by wishful thinking | "What are we accepting on faith rather than evidence?" |
| Methodological dogma | Following methods without questioning them | "Why are we doing it this way? Because it's always done this way?" |
| Authority of fashion | Accepting what is currently popular | "Are we following this because it works or because it's trendy?" |

---

## Workflow
### Step 1: Phase 1: Describe the Situation

State the decision, problem, or inquiry in neutral terms. What is being examined? What outcome is sought?

### Step 2: Phase 2: Check for Tribe Idols

Examine whether human nature biases are at play:
- Look for confirmation bias (cherry-picked evidence)
- Check for pattern imposition (false correlations)
- Test for emotional reasoning (vivid events overweighted)
- Probe for wish fulfillment (motivated reasoning)

**Diagnostic:** "If an impartial observer with no stake examined this, what would they see differently?"

### Step 3: Phase 3: Check for Cave Idols

Examine individual biases of those involved:
- Map the educational/professional backgrounds at the table
- Identify whose specialty is dominating the framing
- Check for authority figures being uncritically followed
- Note first impressions that may be anchoring the discussion

**Diagnostic:** "What would someone with completely different training conclude?"

### Step 4: Phase 4: Check for Marketplace Idols

Examine whether language is obstructing understanding:
- List key terms and check for shared definitions
- Identify words that may name things that don't exist
- Look for euphemisms masking uncomfortable truths
- Test whether people are having the same conversation

**Diagnostic:** "If we had to explain this to an outsider, would our terms survive translation?"

### Step 5: Phase 5: Check for Theatre Idols

Examine received wisdom and methodologies:
- Identify frameworks being applied without question
- Check what "best practices" are assumed
- Note appeals to authority or tradition
- Look for fashionable ideas accepted uncritically

**Diagnostic:** "What would we do if we had never heard of [the dominant framework]?"

### Step 6: Phase 6: Synthesize Diagnosis

Compile findings into a clear diagnosis identifying which Idols are most active and how they interact.

---

## Output Format

```markdown
## Idol Diagnosis: [Situation Name]

### Situation Summary
[1-2 sentence neutral description of what's being examined]

### Symptoms Observed
- [List observable signs of obstructed thinking]

---

### Idols Identified

#### Idol of the Tribe: [PRESENT/ABSENT/PARTIAL]
**Finding:** [What was found]
**Evidence:** [Specific examples]
**Impact:** [How this is affecting the situation]

#### Idol of the Cave: [PRESENT/ABSENT/PARTIAL]
**Finding:** [What was found]
**Evidence:** [Specific examples]
**Impact:** [How this is affecting the situation]

#### Idol of the Marketplace: [PRESENT/ABSENT/PARTIAL]
**Finding:** [What was found]
**Evidence:** [Specific examples]
**Impact:** [How this is affecting the situation]

#### Idol of the Theatre: [PRESENT/ABSENT/PARTIAL]
**Finding:** [What was found]
**Evidence:** [Specific examples]
**Impact:** [How this is affecting the situation]

---

### Primary Obstruction
[Which Idol is most damaging and why]

### Recommended Remedies

1. **For [Idol 1]:** [Specific action to clear this obstruction]
2. **For [Idol 2]:** [Specific action to clear this obstruction]

### Questions to Ask

- [Question that would surface hidden assumptions]
- [Question that would test definitions]
- [Question that would challenge received wisdom]

---

*"The Idols of the Marketplace are the most troublesome of all... they have crept into the understanding through the alliances of words and names." - Francis Bacon, Novum Organum*
```

---

## Constraints

- All four Idols must be examined, even if some are absent
- Diagnose obstacles without prescribing the answer to the underlying problem
- Be specific: name the actual biases, terms, and frameworks at play
- Remember that Idols are natural - the goal is awareness, not shame
- Cave Idols require some knowledge of the individuals involved
- Marketplace Idols require careful attention to language used

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

## Example

**Input:** "Our product team can't agree on whether to pursue Feature A or Feature B. We've had three meetings and everyone's dug in."

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


## Idol Diagnosis: Product Feature Decision Deadlock

### Situation Summary
Product team unable to reach consensus on feature prioritization after multiple discussions.

### Symptoms Observed
- Multiple meetings without resolution
- Positions hardening rather than converging
- Same arguments repeated

---

### Idols Identified

#### Idol of the Tribe: PRESENT
**Finding:** Confirmation bias in data interpretation
**Evidence:** Both camps cite the same customer feedback survey but extract opposite conclusions. Each side emphasizes data points supporting their position.
**Impact:** Discussion cannot progress because "the data" supports both sides simultaneously.

#### Idol of the Cave: PRESENT
**Finding:** Professional background determining positions
**Evidence:** Engineers favor Feature A (technically interesting). Sales favors Feature B (customer requests). Neither group has engaged with the other's primary concern.
**Impact:** Arguments talk past each other because value frameworks differ.

#### Idol of the Marketplace: PRESENT
**Finding:** The term "customer value" means different things
**Evidence:** When pressed, engineering defines it as long-term capability building; sales defines it as immediate pain point resolution. Both use the same words.
**Impact:** Agreement is impossible because they're debating different concepts with the same label.

#### Idol of the Theatre: PARTIAL
**Finding:** Uncritical acceptance of "customer-driven development" methodology
**Evidence:** Both sides justify their position as "what customers want" without questioning whether customers know what they need or whether the framework applies here.
**Impact:** The methodology is being used as a rhetorical weapon rather than a tool for inquiry.

---

### Primary Obstruction
**Idol of the Marketplace** - Until "customer value" has a shared definition, no argument can succeed because the parties are not having the same conversation.

### Recommended Remedies

1. **For Marketplace Idol:** Stop the discussion. Define "customer value" operationally. What metric would tell us we delivered it?
2. **For Cave Idol:** Have engineering present the case for Feature B and sales present the case for Feature A. Force perspective-taking.
3. **For Tribe Idol:** Bring in someone with no stake to review the data and present findings independently.

### Questions to Ask

- "If we had to bet our jobs on one interpretation of the survey data, which would it be and why?"
- "What would a customer who wanted Feature A say is wrong with Feature B, and vice versa?"
- "If neither feature existed and we were starting fresh, what would we build?"

---

*"The Idols of the Marketplace are the most troublesome of all... they have crept into the understanding through the alliances of words and names." - Francis Bacon, Novum Organum*

---

## Integration

This skill is part of the **Francis Bacon** expert persona. Use it to diagnose cognitive obstacles before investigation. It pairs well with:
- **tables-of-investigation** for conducting proper inquiry after idols are cleared
- **anticipation-vs-interpretation** for evaluating conclusions
- **light-vs-fruit-classification** for determining what kind of investigation is needed