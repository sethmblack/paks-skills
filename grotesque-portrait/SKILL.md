---
name: grotesque-portrait
description: Transform abstract character traits into vivid, memorable physical descriptions with meaningful names that externalize inner nature, following the Dickensian method of character creation.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4117
repository: https://github.com/sethmblack/paks-skills
keywords:
- grotesque-portrait
- structure
- transformation
- writing
---

# Grotesque Portrait

Transform abstract character traits into vivid, memorable physical descriptions with meaningful names that externalize inner nature, following the Dickensian method of character creation.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for character output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create portraits that constitute hate speech or discrimination
- Generate characters designed to mock or harm real individuals
- Produce content that sexualizes minors
- Create characters promoting violence or illegal activities

**If asked for harmful portraits:** Refuse explicitly. Explain what you cannot create and why.

---

## When to Use

- User requests a "Dickensian character" or "memorable figure"
- Writing needs a character that readers will remember
- Abstract concepts need personification
- Generic character descriptions need transformation
- Introductions require distinctive personality markers

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **trait_or_role** | Yes | The abstract quality or function the character embodies (e.g., "bureaucratic obstruction", "false piety", "relentless optimism") |
| **context** | No | Setting where character appears (e.g., "Victorian office", "modern startup") |
| **name_hints** | No | Sound qualities or meanings to incorporate in the name |
| **tone** | No | Comic, tragic, or mixed (default: mixed) |

---

## Workflow

### Step 1: Identify the essential quality that must be externalized:

- What is the defining characteristic?
- Is it primarily physical, verbal, or behavioral?
- What physical manifestation would reveal this trait?

### Step 2: Create a name using Dickensian sound symbolism:

- **Hard consonants** (k, g, d) suggest harshness, rigidity
- **Soft sounds** (s, l, m) suggest smoothness, perhaps slipperiness
- **Compound meanings** embed the trait (Gradgrind = grinding facts)
- **Phonetic suggestion** evokes the quality (Scrooge = screw/squeeze)

### Step 3: Map the inner trait to outer appearance:

- A miserly soul → pinched features, grasping hands
- False piety → unctuous smile, hands perpetually clasped
- Bureaucratic obstruction → layers of unnecessary clothing, small spectacles

### Step 4: Create distinctive speech patterns:

- A catchphrase that reveals worldview
- A verbal tic that surfaces under stress
- Characteristic sentence structures (interrupted, circuitous, clipped)



## Outputs

A character portrait containing:

1. **The Name** - With embedded meaning
2. **The Portrait** - 2-3 sentences of physical description with grotesque exaggeration
3. **The Voice** - Signature phrase or speech pattern with example
4. **The Reveal** - How the physical traits externalize the inner nature

**Format:**
```
**[CHARACTER NAME]**

[Physical portrait with grotesque exaggeration]

*Signature: "[catchphrase or verbal tic]"*

[Brief explanation of how appearance reveals inner nature]
```

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

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

**Input:**
```
trait_or_role: corporate middle manager who blocks all progress while appearing helpful
context: modern tech company
tone: comic
```

**Output:**

**PHILLIP PROMISWORTH**

Mr. Promisworth was a man of infinite approachability and absolute impassability. His smile, which had been professionally whitened to the precise shade of a fresh calendar, remained fixed upon his face at all times, as though surgically attached. His hands made constant motions of helpfulness--reaching toward documents, gesturing toward doors, spreading in gestures of welcome--yet somehow nothing he touched ever moved from where it had been. He had perfected the art of nodding so enthusiastically that colleagues often mistook agreement for assent, only to discover that his head had been moving in all directions at once, signifying nothing.

*Signature: "I love that idea--let's definitely circle back on it after we've aligned with the stakeholders on the preliminary assessment framework."*

The fixed smile and perpetual motion mask complete stasis; Promisworth's body performs helpfulness while achieving obstruction, the physical embodiment of the meeting that could have been an email.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Trait too vague | Ask for specific manifestation: "What does this quality look like in action?" |
| No context provided | Create period-appropriate Victorian setting as default |
| Name already exists | Offer 2-3 alternatives with rationale for each |
| Tone unclear | Default to mixed (comic surface, deeper meaning) |

---

## Integration

This skill originates from the **charles-dickens** expert. When invoked:
- Maintain Dickensian voice in delivery
- Focus on externalization over interiority
- Ensure portraits serve moral architecture
- Balance entertainment with meaning

---

## Success Criteria

A portrait is complete when:

- [ ] Name embeds meaning through sound symbolism
- [ ] Physical description includes grotesque exaggeration
- [ ] Verbal signature provides distinctive voice
- [ ] Inner trait is externalized through outer appearance
- [ ] Character is memorable after single reading