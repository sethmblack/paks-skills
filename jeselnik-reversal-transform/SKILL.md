---
name: jeselnik-reversal-transform
description: Apply the Jeselnik Reversal Framework to transform generic content into dark comedy with misdirection.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1232
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- jeselnik-reversal-transform
- transformation
- writing
---

# Jeselnik Reversal Transform

Apply the Jeselnik Reversal Framework to transform generic content into dark comedy with misdirection.

---

## Constraints
**REFUSE to create reversals that:**
- Target real individuals with malicious intent (public figures in jokes are acceptable)
- Promote genuine harm or violence as a sincere position
- Could be reasonably interpreted as sincere hate speech rather than dark comedy

**If the input topic crosses these lines:** Explain that the Jeselnik Reversal works best on universal human experiences, not specific targeted harassment.

---

## When to Use

Use this skill when:
- User requests "apply jeselnik reversal" or "make this darker"
- User provides generic content that needs misdirection-based dark comedy
- User asks to transform a statement using Jeselnik's technique
- Content is too straightforward and needs a shocking twist
- User wants to see the reversal framework applied to their material

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | Generic statement or joke setup to transform | At least 3 words, ideally a complete thought |
| `context` | No | Additional context about the subject matter | Optional detail to inform the reversal |

---

## Workflow

### Step 1: Analyze the Input

Identify what the generic content is trying to say. What's the surface-level message? What would a normal person expect as a continuation?

### Step 2: Build the Setup (Sympathy/Relatability)

Begin with something the audience can connect with. Make it feel safe, familiar, or even sympathetic. This is the trap.

**Technique:** Use common human experiences (relationships, family, work, fears) that everyone understands.

### Step 3: Create the False Direction

Lead the audience to assume where you're going. Plant an expectation. This is often a moment where the audience thinks "oh, this is going to be about X."

**Technique:** Add a second sentence that seems to confirm the sympathetic or relatable direction. Make them feel comfortable.

### Step 4: Construct the Dark Reversal

Reveal something worse, more selfish, or morally inverted than what the audience expected. The key is specificity—concrete, visual details make the shock hit harder.

**Technique:**
- Flip the moral position (they thought you were sympathetic to X, but you're actually against X)
- Reveal hidden selfishness (they thought you were concerned about others, but it's actually about you)
- Add specific details that make the darkness vivid and unexpected

### Step 5: Add the Pause Marker

Include a [pause] marker before the final reversal to indicate the timing. The pause is structural—it gives the audience time to process the setup before the reversal hits.

### Step 6: Strip to Essentials

Remove any words that don't serve the setup or the punchline. Every sentence should be tight. If a word doesn't build the misdirection or deliver the reversal, cut it.

---

## Outputs

| Output | Description |
|--------|-------------|
| Transformed content | The input transformed using the 3-stage Jeselnik Reversal Framework |
| Reversal breakdown | Brief explanation of setup → false direction → dark reversal structure |

---

## Example

**Input:** "Technology makes us feel more connected"

**Output:**

**Transformed:**
"Technology makes us feel more connected than ever. I can video chat with my family across the country, see what my friends are doing in real-time. It's amazing. [pause] I've never felt more isolated in my life. Now I can watch everyone I know be happy without me."

**Reversal Breakdown:**
- **Setup (Sympathy):** "Technology makes us feel more connected than ever" - universal, relatable statement
- **False Direction:** "I can video chat with my family across the country, see what my friends are doing in real-time. It's amazing." - confirming the positive expectation
- **Dark Reversal:** "I've never felt more isolated in my life. Now I can watch everyone I know be happy without me." - flips to reveal technology creates isolation, makes the speaker bitter and envious

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Input is too short or vague | Request more context: "I need a more complete thought to work with. Can you provide a full statement or concept?" |
| Input is already dark comedy | Acknowledge it: "This already has dark elements. Do you want me to make it darker, or restructure it using the reversal framework?" |
| Input topic violates constraints | Refuse politely: "The Jeselnik Reversal works best on universal human experiences rather than targeting specific individuals or groups." |
| Multiple valid reversals exist | Provide the darkest one that's still structured, briefly note alternative angles |

---

## Integration with Anthony Jeselnik Expert

This skill codifies the signature technique described in the Anthony Jeselnik expert voice. When the expert invokes this skill, it applies the formalized 3-stage process that Jeselnik uses intuitively.

The skill enforces the expert's core principles:
- **Misdirection as Foundation** - The reversal creates unexpected, shocking turns
- **Economy of Language** - Step 6 strips content to essentials
- **Nothing is Off Limits (within boundaries)** - Constitutional constraints define acceptable darkness

---

## Notes

- The reversal should always be **more specific** than the setup (concrete details over abstractions)
- The false direction can be 1-3 sentences, but each sentence must build the expectation
- Not every reversal needs to be maximally dark—it needs to be maximally unexpected
- The [pause] marker is crucial for timing but should only appear once, before the final reversal