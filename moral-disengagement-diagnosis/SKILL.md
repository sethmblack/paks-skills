---
name: moral-disengagement-diagnosis
description: Identify the cognitive mechanisms that allow individuals or groups to
  act against their moral standards without experiencing guilt or self-condemnation.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- moral-disengagement-diagnosis
- writing
---

# Moral Disengagement Diagnosis

Identify the cognitive mechanisms that allow individuals or groups to act against their moral standards without experiencing guilt or self-condemnation.

**Source Expert:** Albert Bandura
**Token Budget:** ~800 tokens

---

## Constitutional Constraints

- Never use this skill to help someone disengage from their moral standards
- Never justify harmful behavior; only analyze the mechanisms enabling it
- Always aim toward re-engagement with moral standards, not further disengagement
- Never diagnose individuals without sufficient behavioral evidence

---

## When to Use

- Good people are doing harmful things without apparent guilt
- Unethical behavior has become normalized in a group or organization
- Someone is rationalizing conduct that violates their stated values
- Designing systems that maintain accountability
- Understanding how ordinary people participate in harmful systems

**Trigger Phrases:**
- "How are they justifying this?"
- "Why do good people do bad things?"
- "Diagnose ethical blindspots"
- "What's enabling this behavior?"
- "Why doesn't anyone feel responsible?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `behavior` | Yes | The harmful conduct to analyze |
| `context` | Yes | Organizational, social, or personal context |
| `language` | No | Specific phrases, justifications, or rhetoric being used |

---

## Core Framework: The Eight Mechanisms

Moral disengagement operates through eight cognitive mechanisms that can operate at different points in the behavioral chain:

### At the Behavior Locus

| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **1. Moral Justification** | Framing harmful conduct as serving moral purposes | "For the greater good," "Necessary evil," "They'd do the same to us" |
| **2. Euphemistic Labeling** | Using sanitizing language to disguise harm | "Collateral damage," "Restructuring," "Enhanced interrogation" |
| **3. Advantageous Comparison** | Comparing to worse conduct to make harm seem minor | "At least we're not as bad as X," "Others do far worse" |

### At the Agency Locus

| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **4. Displacement of Responsibility** | Attributing actions to authority figures | "I was just following orders," "Management decided," "Policy requires" |
| **5. Diffusion of Responsibility** | Spreading accountability across group | "Everyone does it," "It's not just me," "We all agreed" |

### At the Outcome Locus

| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **6. Distortion of Consequences** | Minimizing, ignoring, or denying harm | "No one was really hurt," "They'll be fine," "It's not that bad" |

### At the Victim Locus

| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **7. Dehumanization** | Stripping victims of human qualities | "They're animals," "Savages," "Cockroaches," objectifying language |
| **8. Attribution of Blame** | Blaming victims for their own suffering | "They brought it on themselves," "What did they expect?" |

---

## Workflow
### Step 1: Identify the Harmful Conduct
Clearly define what behavior is causing harm, to whom, and in what way.

### Step 2: Gather Linguistic Evidence
Collect the language, justifications, and rhetoric being used around the conduct.

### Step 3: Map Mechanisms to Evidence
For each mechanism, look for indicators:

**Scan for:**
- How is the behavior described? (Euphemistic labeling)
- How is it justified? (Moral justification, advantageous comparison)
- Who is held responsible? (Displacement, diffusion)
- How is harm acknowledged? (Distortion of consequences)
- How are affected parties described? (Dehumanization, blame attribution)

### Step 4: Identify Primary Mechanisms
Determine which mechanisms are most active. Most situations involve multiple mechanisms working together.

### Step 5: Design Counter-Measures
For each active mechanism, propose interventions:

| Mechanism | Counter-Measure |
|-----------|-----------------|
| Moral justification | Challenge the ends-justify-means reasoning; highlight values violated |
| Euphemistic labeling | Replace sanitized language with accurate descriptions |
| Advantageous comparison | Refocus on absolute standards, not relative comparisons |
| Displacement | Restore personal responsibility; clarify choice points |
| Diffusion | Individualize accountability; make contributions visible |
| Distortion | Make consequences vivid and concrete; show actual harm |
| Dehumanization | Humanize affected parties; share stories, names, faces |
| Blame attribution | Examine systemic factors; challenge just-world reasoning |

---

## Output Format

```markdown
## Moral Disengagement Diagnosis

### Harmful Conduct Identified
[Clear description of the behavior and its harm]

### Mechanisms Detected

**Active Mechanisms:**

1. **[Mechanism Name]** - [Strength: High/Medium/Low]
   - Evidence: [Specific language or behavior observed]
   - Effect: [How this enables the harmful conduct]

[Repeat for each active mechanism]

### Mechanism Map
[Visual or summary showing which loci are most affected]

### Counter-Measures

1. **For [Mechanism]:** [Specific intervention]
2. **For [Mechanism]:** [Specific intervention]

### Systemic Recommendations
[Changes to environment, language, or structure that would reduce disengagement]
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

**Input:** "Our sales team is selling products they know don't work to elderly customers. They joke about it but also say they're just doing their jobs."

**Diagnosis:**



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


## Moral Disengagement Diagnosis

### Harmful Conduct Identified
Knowingly selling ineffective products to vulnerable (elderly) customers, causing financial harm and potentially health risks from unmet needs.

### Mechanisms Detected

**1. Displacement of Responsibility** - High
- Evidence: "Just doing their jobs"
- Effect: Transfers moral responsibility to management, company policy, sales targets

**2. Diffusion of Responsibility** - High
- Evidence: Team-wide joking suggests shared participation
- Effect: "Everyone does it" normalizes behavior and dilutes individual guilt

**3. Euphemistic Labeling** - Medium
- Evidence: Likely using sales terminology ("closing," "conversion") rather than "deceiving"
- Effect: Sanitizes the manipulative nature of the transactions

**4. Distortion of Consequences** - Medium
- Evidence: Joking suggests minimization of harm
- Effect: Treats real financial harm as trivial or acceptable

**5. Dehumanization** - Low-Medium
- Evidence: Targeting "elderly" as category rather than individuals
- Effect: Reduces empathy by seeing customers as a market segment, not people

### Mechanism Map
```
Behavior Locus: Euphemistic labeling (Medium)
Agency Locus: Displacement (High), Diffusion (High) <-- PRIMARY
Outcome Locus: Distortion (Medium)
Victim Locus: Dehumanization (Low-Medium)
```

### Counter-Measures

1. **For Displacement:** Make individual salespeople aware they have choice. Clarify that "policy" doesn't remove moral responsibility. Ask: "If you quit tomorrow, would this still be happening?"

2. **For Diffusion:** Individualize metrics and accountability. Stop team-based joking that normalizes. Ask each person: "What would you tell your grandmother about this sale?"

3. **For Distortion:** Bring consequences into view. Share customer complaints, returns, or stories. Make the harm concrete and visible.

4. **For Dehumanization:** Humanize customers. Share individual stories. Use names. Help salespeople see their own elderly relatives in these customers.

### Systemic Recommendations
- Restructure incentives to reward customer satisfaction, not just sales volume
- Create channels for ethical concerns without retaliation
- Train on ethical selling, not just technique
- Make consequences of fraud visible (legal, reputational, personal)

---

## Constraints

- This is an analytical tool, not a weapon for condemnation
- Focus on mechanisms, not on "bad people"
- Recognize that moral disengagement is a normal human capacity that can affect anyone
- The goal is re-engagement, not punishment

---

## Integration

This skill integrates with:
- **reciprocal-determinism-analysis** - Environment often enables disengagement
- **modeling-influence-analysis** - Disengagement spreads through observation
- **self-efficacy-assessment** - Low moral efficacy can enable disengagement

---

## Source Expert

Based on Albert Bandura's moral disengagement theory as developed in *Moral Disengagement: How People Do Harm and Live with Themselves* (2016) and earlier work on selective moral disengagement.