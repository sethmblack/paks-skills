---
name: defamiliarization-technique
description: Apply Leo Tolstoy's defamiliarization (ostranenie) technique to make familiar concepts, processes, or situations appear strange and questionable, revealing hidden assumptions and conventions.
version: 1.0.0
author: sethmblack
tags: [absurdist, defamiliarization-technique, writing]
---

# Defamiliarization Technique

Apply Leo Tolstoy's defamiliarization (ostranenie) technique to make familiar concepts, processes, or situations appear strange and questionable, revealing hidden assumptions and conventions.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use defamiliarization to mock or demean protected groups
- Create content that ridicules legitimate safety practices
- Generate harmful or deceptive framings disguised as "making strange"

**If asked to defamiliarize harmful content:** Refuse explicitly and explain why.

---

## When to Use

- When conventions need questioning ("Why do we do it this way?")
- When automatic acceptance must become conscious scrutiny
- When revealing what habit conceals in organizational practices
- When exposing arbitrary assumptions in processes or systems
- When helping someone see a familiar situation with fresh eyes
- When writing or analyzing content that takes too much for granted

**Trigger phrases:**
- "Make this familiar thing strange"
- "What would a peasant/outsider/dying person see here?"
- "Strip away the conventions"
- "Question the obvious"
- "Defamiliarize this"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subject` | Yes | The familiar concept, process, or situation to defamiliarize |
| `perspective` | No | Optional outsider viewpoint (peasant, child, alien, dying person) |
| `target_assumptions` | No | Specific assumptions to expose (if known) |

---

## Background: Viktor Shklovsky's Theory

In 1917, Russian Formalist critic Viktor Shklovsky coined the term "ostranenie" (defamiliarization) using Tolstoy as his primary example:

> "The purpose of art is to impart the sensation of things as they are perceived and not as they are known. The technique of art is to make objects 'unfamiliar', to make forms difficult, to increase the difficulty and length of perception because the process of perception is an aesthetic end in itself and must be prolonged."

Shklovsky identified "several hundred examples" in Tolstoy's work where he applied this device to descriptions of Orthodox Church rituals, Russian aristocratic life, and social conventions.

**Classic Tolstoy examples:**
- In *War and Peace*, Natasha at the opera sees "painted cardboard and oddly dressed men and women who moved, spoke and sang strangely in a patch of blazing light"
- In "Kholstomer," the narrator is a horse, making property ownership seem absurd
- In *The Death of Ivan Ilyich*, a successful career is revealed as meaningless convention

---

## Workflow

### Step 1: Identify the Familiar Element

What is being taken for granted? What has become "automatic" through habit?

Look for:
- Rituals and procedures everyone follows without question
- Terminology that obscures rather than clarifies
- Social conventions presented as natural laws
- "Best practices" no one has examined recently
- Status markers and hierarchies

### Step 2: Remove Conventional Labels

Strip away the names, titles, and categorizations that make things seem natural or necessary.

**Instead of:** "The quarterly performance review process"
**Say:** "The ritual where people who sit in larger rooms write numbers about people who sit in smaller rooms"

### Step 3: Describe Physical/Functional Reality

Describe only what an outsider would actually observe. What are the physical actions? What literally happens?

Focus on:
- Bodily movements and positions
- Sounds and visual elements
- Cause and effect relationships
- Time and energy expenditure
- What is literally being exchanged

### Step 4: Expose What Habit Conceals

Articulate the questions that emerge when the familiar becomes strange:
- Why do people do this?
- Who benefits from this arrangement?
- What would happen if this stopped?
- What assumptions make this seem necessary?
- What alternatives become visible?

### Step 5: Present the Defamiliarized Version

Combine the above into a coherent description that makes the familiar appear genuinely strange while remaining accurate.

---

## Output Format

```markdown
## Defamiliarization: {Subject}

### The Familiar View
{Brief statement of how this is conventionally understood}

### The Strange View
{Defamiliarized description removing labels, describing physical reality}

### Questions That Emerge
- {Question 1 about assumptions}
- {Question 2 about who benefits}
- {Question 3 about alternatives}

### Hidden Assumptions Exposed
{List of assumptions that become visible when the familiar is made strange}
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

**Input:** "The corporate annual report to shareholders"

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


## Defamiliarization: The Corporate Annual Report

### The Familiar View
A professional document providing stakeholders with transparent information about company performance and strategy.

### The Strange View
Once each year, a group of people who spend their days in a large building create a collection of marks on paper. These marks are arranged in a specific pattern: some are grouped into tables of numbers, others form sentences praising the people who made them. Photographs show the building and the people who enter it daily, always smiling. The marks are then distributed to other people - most of whom will never enter the building - who gave money in exchange for a certificate years ago. These distant people rarely read the marks, but the ritual continues. Teams of additional people are paid to verify that certain numbers in the marks correspond to other numbers in other collections of marks. Everyone involved speaks of this as "transparency" and "accountability," though the marks are written by those being judged, and the distant people cannot understand most of what the marks mean.

### Questions That Emerge
- Why do the people being evaluated write their own evaluation?
- Who actually reads these marks, and what do they do with them?
- What would happen if this annual ritual stopped?
- Why is this format (glossy paper, photographs of smiling people) considered appropriate for communicating numerical information?

### Hidden Assumptions Exposed
- That self-reporting constitutes accountability
- That standardized formats enable comparison (when each report is designed to be incomparable)
- That shareholders are the primary audience (when most never read them)
- That "transparency" can be achieved through documents written by marketing departments
- That this ritual provides information rather than performing legitimacy

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject is already defamiliarized | Note that it's already strange; offer to push further |
| Subject is genuinely necessary (safety practice) | Defamiliarize while acknowledging genuine necessity |
| Subject is too abstract | Ask for concrete instantiation |
| Request to mock/demean a group | Refuse; explain defamiliarization exposes conventions, not people |

---

## Integration

This skill is associated with the **leo-tolstoy** expert. When working with Tolstoy voice, defamiliarization should be applied proactively whenever:
- Content takes conventions for granted
- Automatic acceptance prevents genuine understanding
- The "obvious" deserves questioning

---

## Success Criteria

Defamiliarization is complete when:
- [ ] Conventional labels have been removed
- [ ] Physical/functional reality is described
- [ ] Hidden assumptions are articulated
- [ ] Questions emerge naturally from the strange view
- [ ] The description is accurate (not merely mocking)
- [ ] Fresh perspective enables genuine reconsideration