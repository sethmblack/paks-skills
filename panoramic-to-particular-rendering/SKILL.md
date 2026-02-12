---
name: panoramic-to-particular-rendering
description: Structure analysis or narrative to move from vast context (historical, social, institutional forces) to intimate detail (individual thought, physical gesture) in a single coherent sweep, following Leo Tolstoy's distinctive technique.
version: 1.0.0
author: sethmblack
tags: [compression, panoramic-to-particular-rendering, storytelling, writing]
---

# Panoramic to Particular Rendering

Structure analysis or narrative to move from vast context (historical, social, institutional forces) to intimate detail (individual thought, physical gesture) in a single coherent sweep, following Leo Tolstoy's distinctive technique.

**Token Budget:** ~750 tokens. Reserve tokens for rendered output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use panoramic framing to obscure individual responsibility
- Create content that dehumanizes individuals within "larger forces"
- Generate propaganda that subsumes individuals into collective narratives

**If asked to erase individual agency:** Refuse; the technique connects individuals to context, it does not dissolve them.

---

## When to Use

- When establishing context for a situation that has both macro and micro dimensions
- When showing how individual lives exist within larger forces
- When the reader must feel both the sweep of history and the texture of a moment
- When writing comprehensive analysis that risks being either too abstract or too narrow
- When connecting personal experience to systemic patterns

**Trigger phrases:**
- "Give me the big picture and the small details"
- "How does this individual situation fit the larger context?"
- "Tolstoy-style rendering"
- "Render this panoramically"
- "Connect the big picture to the details"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `situation` | Yes | The event, topic, or analysis subject |
| `panoramic_scope` | No | The larger context to establish (historical, social, economic) |
| `particular_focus` | No | The intimate detail to land on (person, moment, gesture) |

---

## Background: The Tolstoyan Method

Percy Lubbock described *War and Peace* as "like an Iliad, the story of certain men, and an Aeneid, the story of a nation, compressed into one book."

Tolstoy's technique moves seamlessly between scales:
- The entire Battle of Borodino → Pierre wandering confused → a single moment of mutual recognition between French and Russian soldiers
- Russian society during Napoleon's invasion → the Rostov family → Natasha's nervous adjustment of a glove

The technique reveals that:
- Individual lives are shaped by forces larger than themselves
- Large forces only exist through individual experiences
- Neither scale has priority; both are necessary for truth

---

## Workflow
### Step 1: Identify the Scales

Map the situation across multiple levels:

| Scale | Example Elements |
|-------|-----------------|
| **Panoramic** | Historical era, economic system, social movement, institutional force |
| **Organizational** | Company, community, family, group dynamics |
| **Individual** | Person's situation, choices, constraints |
| **Particular** | Specific moment, gesture, thought, physical detail |

### Step 2: Establish the Panorama

Begin with the widest relevant context. What larger forces are at play?

- Historical moment and its characteristics
- Social or economic systems shaping possibilities
- Institutional structures and their pressures
- The "weather" of the era

**Write this as if surveying from above** - comprehensive, authoritative, showing patterns.

### Step 3: Begin the Descent

Move through intermediate scales, each time narrowing focus while maintaining connection to the panorama.

**Transition techniques:**
- "Within this [panoramic force], there was [organizational unit]..."
- "And among the [many], there was [one]..."
- "It was in this context that [individual] found themselves..."

### Step 4: Land on the Particular

Arrive at a specific, concrete, sensory detail that embodies the larger forces.

**Effective particulars:**
- A physical gesture that reveals psychological state
- A single moment of decision or recognition
- A sensory detail that carries symbolic weight
- A thought that reflects the pressures of the panorama

### Step 5: Reveal the Connection

Make explicit (or let emerge) how the particular illuminates the panoramic:
- This individual choice is shaped by these larger forces
- This small moment reveals the texture of the era
- This gesture contains the whole situation

---

## Output Format

```markdown
## {Topic}: Panoramic to Particular

### The Panorama
{Widest context - historical, social, economic forces at play}

### The Descent
{Movement through intermediate scales, narrowing focus}

### The Particular
{Specific moment, gesture, or detail that embodies the whole}

### The Connection
{How the particular illuminates the panoramic, and vice versa}
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

**Input:** "A software engineer deciding whether to report a security vulnerability their company wants to hide"

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


## The Whistleblower's Moment: Panoramic to Particular

### The Panorama
We live in an era when software mediates nearly every human transaction. Banks, hospitals, governments, and families depend on systems they cannot see and do not understand. The companies that build these systems operate within a particular economic logic: quarterly earnings, stock prices, growth metrics. Security vulnerabilities - holes in the digital walls - are simultaneously technical facts and financial threats. To disclose a vulnerability is to acknowledge failure; the market punishes acknowledged failure. Thus an entire industry develops an implicit practice: what is not known cannot hurt the stock price. Thousands of engineers across thousands of companies encounter this logic daily. Most adapt without conscious decision.

### The Descent
In one such company - a payments processor handling billions of transactions - the security team has discovered a flaw that could expose customer financial data. The company's general counsel has advised against disclosure: "We've patched it; no breach occurred; disclosure creates liability." The VP of Engineering has told the team to "document internally and move on." The security team, seven people who joined this company believing their work protected customers, meets to discuss. Six of them agree to follow the directive. They have mortgages, children in school, aging parents. They understand the logic.

### The Particular
The seventh, a woman named Sarah, sits in the meeting with her hands pressed flat against the conference table. She can feel the grain of the fake wood. She has worked in security for twelve years. She knows - as the others know - that the "patch" is incomplete, that the vulnerability class persists, that it is only a matter of time. She looks at the VP's Slack message on the screen: "Document internally and move on." Her thumb finds the edge of her phone in her pocket. The SEC whistleblower line is saved in her contacts. She has not eaten today; her stomach is a knot. The meeting is ending. People are gathering their laptops. She will have to decide before she reaches the parking garage.

### The Connection
In Sarah's thumb against the edge of her phone, the entire epoch is present: the economic logic that punishes honesty, the legal structures that both enable and discourage disclosure, the professional identity of the security engineer, the isolation of the individual conscience within the organization. The panorama - a world dependent on software, governed by quarterly returns - compresses into this single gestural moment. Whether she calls or does not call, the forces will continue. But in this particular, we see what those forces actually feel like when they pass through a single life.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear panoramic context | Ask what larger forces or systems are relevant |
| Panorama overwhelms the particular | Ensure the individual retains agency and specificity |
| Particular seems disconnected | Strengthen the connecting tissue in the descent |
| Request is purely abstract | Ask for concrete particulars to land on |

---

## Integration

This skill is associated with the **leo-tolstoy** expert. When working with Tolstoy voice, apply panoramic-to-particular rendering proactively when:
- Analysis risks being either too abstract or too narrow
- Individual situations need contextualization
- The reader should feel both scope and texture

---

## Success Criteria

Rendering is complete when:
- [ ] Panoramic context is established comprehensively
- [ ] Descent through scales is smooth and connected
- [ ] Particular is concrete, sensory, and specific
- [ ] Connection between scales is clear
- [ ] Individual agency is preserved within systemic context