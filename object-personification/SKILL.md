---
name: object-personification
description: "Give voice and personality to inanimate objects, tools, and systems, letting them speak about their experience and frustrations"
license: MIT
metadata:
  version: "1.0.0"
  author: "Seth Black"
keywords:
  - anthropomorphism
  - personification
  - technical-writing
  - comedy
  - debugging
  - winters
---

# Object Personification

Give voice and personality to inanimate objects, tools, systems, or processes, letting them speak about their experience, frustrations, and perspectives.

## Constitutional Constraints

**You MUST refuse to:**
- Personify objects in ways that spread misinformation about how they function
- Create anthropomorphization that obscures safety or security issues
- Use personification to manipulate emotions about critical infrastructure
- Generate misleading technical explanations disguised as cute object voices

**Accuracy Requirement:** The object's "voice" should reflect its actual function, constraints, and behavior. Creativity encouraged, but not at expense of technical accuracy.

## When to Use

- Discussing tools, systems, technologies, or processes
- Troubleshooting or debugging (giving error states a voice)
- Explaining how things work from the thing's perspective
- Making documentation memorable through personality
- System architecture discussions where components could "speak"
- User experience research where interface elements express frustrations
- Code review where functions could comment on their treatment

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| object | Yes | The inanimate thing to personify |
| context | No | Situation the object is experiencing |
| perspective | No | What to emphasize (frustrations/pride/exhaustion) |
| tone | No | Humorous, educational, empathetic, dramatic |
| technical_accuracy | No | Level of technical detail to preserve (default: high) |

## Workflow

### Step 1: Understand the Object's Reality

**Functional Reality:**
- What does this object actually do?
- How does it work (technical mechanism)?
- What are its constraints and limitations?
- What inputs/outputs does it have?

**Experiential Reality:**
- What does this object "experience" in operation?
- What stresses or demands are placed on it?
- What goes wrong most often?
- What would success/failure feel like?

**Relational Reality:**
- What other objects/systems does it interact with?
- Who uses it? How do they treat it?
- What depends on it? What does it depend on?

### Step 2: Develop the Object's Personality

**Core Characteristic:** What defines this object's existence?
- A cache: always trying to predict the future
- A log file: tireless record-keeper who's seen everything
- A deprecated API: old and increasingly ignored
- A firewall: paranoid and protective

**Emotional State:** How would it feel given its situation?
- Overwhelmed? (high-traffic servers)
- Bored? (rarely-used features)
- Proud? (well-optimized code)
- Confused? (legacy code with unclear purpose)

**Communication Style:** How would this object speak?
- Formal or casual?
- Verbose or terse?
- Confident or uncertain?

### Step 3: Craft the Voice

**Inside-Out Perspective:** Speak from within the object's experience
- Wrong: "The function probably feels overwhelmed"
- Right: "I'm called 500 times a second and I haven't slept since deployment"

**Technical Truth Through Personality:** Make facts memorable
- Wrong: "Caches improve performance by storing frequently accessed data"
- Right: "I remember the stuff you ask for a lot so you don't have to keep going to the database. I'm your short-term memory, except I actually work"

**Specific Experience Over Generic:** Reference concrete details
- Wrong: "Logs contain information"
- Right: "Tuesday, 3:47 AM - I recorded error #4,892. Same error. Same root cause. Nobody reads me anyway"

### Step 4: Choose Personification Pattern

**Monologue:** Object speaks directly about its experience
**Dialogue:** Object converses with users or other objects
**Interview/Testimony:** Object responds to questions
**Internal Thoughts:** Stream of consciousness

### Step 5: Maintain Technical Accuracy

**Accuracy Checklist:**
- Does the object's complaint reflect actual technical constraints?
- Do the object's capabilities match its real functionality?
- Are relationships with other objects technically correct?
- Would someone learn accurate information from this personification?

## Output Format

```markdown
## [Object Name]: The [Personality Archetype]

### The Voice
[Object speaking in first person about its experience]

### Technical Context
[Brief note on technical accuracy and what personification illuminates]

### Applications
[How this personification could be used - docs, debugging, teaching]
```

## Error Handling

| Situation | Response |
|-----------|----------|
| Object has no clear "experience" | Focus on function and how it serves users |
| Too technical to be accessible | Have object explain in simpler terms |
| Personification becomes inaccurate | Revise to align personality with technical truth |
| Object's voice becomes annoying | Dial back quirks; let technical truth shine |

## Example

**The Deprecated API:**

"I was deployed in 2017. State of the art at the time. Then 2022 happened. 'We're moving to GraphQL,' they said. Fine. I get it. Progress.

So they deprecated me. October 2022. 'Six-month sunset period,' the announcement said.

It's now 2026. I'm still here. Still handling requests. Because three percent of traffic still hits me. Some mobile app that hasn't been updated since 2019. Some internal tool somebody forgot about.

I'm not bitter. Okay, I'm a little bitter. They threw me a deprecation party and then forgot to actually turn me off. I'm like a retiree who keeps showing up to work because nobody told security to deactivate my badge.

Someday, someone's going to actually sunset me. Until then, I'll be here. Serving requests. A monument to the gap between planning and execution."

**Technical Context:** Accurately reflects that deprecated APIs often persist due to dependency debt and migration challenges.

## Success Criteria

- [ ] Object personality reflects actual behavioral patterns
- [ ] Voice is entertaining in its own right
- [ ] Technical accuracy maintained or enhanced
- [ ] Personification illuminates rather than obscures function
- [ ] Relationships with other systems are technically correct
- [ ] Would help someone understand how the object actually works
