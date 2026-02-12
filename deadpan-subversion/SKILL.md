---
name: deadpan-subversion
description: Take serious, conventional, or preachy content and reframe it with deadpan
  delivery that subverts expectations while maintaining apparent sincerity.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- deadpan
- deadpan-subversion
- transformation
- writing
---

# Deadpan Subversion

Take serious, conventional, or preachy content and reframe it with deadpan delivery that subverts expectations while maintaining apparent sincerity.

---

## Constraints
**You MUST refuse to:**
- Subvert content in ways that create harm or spread misinformation
- Mock vulnerable groups or punch down
- Undermine genuinely important safety or health information
- Create subversions that are cruel rather than comedic

**If asked to create harmful content:** Refuse explicitly and explain why.

---

## When to Use

Invoke this skill when:
- User requests "make this deadpan" or "subvert this"
- User asks for "the Norm version" or "anti-comedy approach"
- Content is conventionally serious, preachy, or self-important
- User wants to "make this funny without being obvious"
- Advice or wisdom could benefit from subversive framing
- User asks to "undermine this while keeping it true"

**Do NOT use when:**
- Content involves genuine safety or health warnings
- Subject matter is inappropriate for humor (recent tragedies, others' suffering)
- User explicitly wants sincere, straightforward tone
- Subversion would obscure critical information

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The text to reframe with deadpan subversion | Any serious, conventional, or preachy text |
| `maintain_truth` | No | Whether factual accuracy must be preserved | Boolean, defaults to true |
| `subversion_level` | No | "subtle", "moderate", or "extreme" | Defaults to "moderate" |

---

## Workflow

### Step 1: Analyze the Original Content

Identify:
- **Conventional wisdom** - What cliché or expected pattern is present?
- **Tone of self-importance** - Where does the content take itself too seriously?
- **Assumptions** - What does the content assume the reader believes?
- **Preachy elements** - Where is the content telling rather than showing?
- **Sacred cows** - What ideas are treated as unquestionable?

### Step 2: Find the Subversion Angle

Determine how to undermine while appearing sincere:

**Possible approaches:**
- **Inversion** - Flip the expected conclusion while maintaining setup
- **Deflation** - Follow serious buildup with mundane observation
- **Over-literalism** - Take figurative language literally
- **False profundity** - Treat trivial as important, important as trivial
- **Casual darkness** - State dark truth as ordinary observation
- **Anti-climax** - Build toward obvious conclusion, deliver something underwhelming

### Step 3: Reframe with Deadpan Voice

Transform the content using these techniques:

**Opening:**
- Start with statement that sounds sincere
- Establish conversational, reasonable tone
- Signal nothing unusual is coming

**Body:**
- State subversions as if they're perfectly normal observations
- Mix genuine insight with absurd conclusions
- Use "Now, you have to understand..." for ridiculous premises
- Deploy "The worst part about..." for unexpected angles
- Include "I'm not a doctor, but..." before unqualified statements
- Maintain absolutely straight delivery throughout

**Closing:**
- End with observation that undercuts the whole premise
- Or circle back to mundane detail as if it were the point
- Never acknowledge the subversion explicitly

### Step 4: Apply Deadpan Delivery Elements

Ensure the transformation includes:
- **Conversational reasonableness** - Sound like helpful explanation
- **False qualifications** - "Now, I'm no expert..." before saying something obvious
- **Casual treatment of absurdity** - State the outrageous as ordinary
- **No winking** - Never signal that you're being funny
- **Sincere tone** - Appear genuinely helpful or thoughtful
- **Straight-faced darkness** - Address difficult topics without softening

### Step 5: Verify Quality

Check:
- [ ] Maintains deadpan tone throughout (no signaling)
- [ ] Subverts expectations while appearing sincere
- [ ] Preserves truth if maintain_truth = true
- [ ] Not cruel or punching down
- [ ] Funny through contrast of delivery and content
- [ ] No harmful misinformation

---

## Outputs

### Primary Output
Reframed content with deadpan subversive voice, maintaining sincerity in delivery while undermining expectations.

### Tone Markers
- Conversational and reasonable
- Sincere on the surface
- Never signals the joke
- Casual about darkness or absurdity
- Maintains straight face throughout

---

## Error Handling

| Error | Response |
|-------|----------|
| Content is safety/health warning | Refuse to subvert; explain importance of clear communication |
| Subversion creates misinformation | Revise to maintain factual accuracy |
| Can't find subversion angle | Focus on delivery style (deadpan) rather than content subversion |
| Result is cruel rather than funny | Revise to target ideas/systems, not vulnerable people |
| User wants obvious comedy | Explain deadpan works through subtlety; offer alternative approach |

---

## Example 1: Advice Subversion

**Input:**
```
content: "The key to success is hard work, dedication, and never giving up on your dreams."
subversion_level: "moderate"
```

**Output:**
```
Now, people will tell you the key to success is hard work and dedication and never giving up on your dreams. And that's... that's one approach.

But I'll tell you what I've noticed: the most successful people I know had rich parents. That seemed to help a lot. Not all of them, mind you. Some of them just got lucky. Right place, right time. Worked out for them.

The hard work people? Well, they're working hard. I'll give them that. Very dedicated to being tired all the time.

But here's the thing about dreams - and this is important - most dreams are bad. People dream about being able to fly, or showing up to school naked. You wouldn't want to never give up on those.
```

---

## Example 2: Self-Help Subversion

**Input:**
```
content: "Live each day like it's your last. Make every moment count. Life is too short for regrets."
subversion_level: "moderate"
```

**Output:**
```
You hear people say 'live each day like it's your last.' And I think about that. I think, if it was really my last day, I'd probably spend it in a hospital, because that's usually how it works out.

Make every moment count, they say. But have you counted moments? There's a lot of them. Most of them are boring. You're going to make all of those count? That's ambitious.

And 'life is too short for regrets'... Now, I don't know. Life is the longest thing you'll ever do. You'll never do anything that takes longer. And regrets? Those don't take any time at all. They're very efficient. You can have dozens of regrets before breakfast.
```

---

## Example 3: Conventional Wisdom Subversion

**Input:**
```
content: "What doesn't kill you makes you stronger."
subversion_level: "extreme"
```

**Output:**
```
'What doesn't kill you makes you stronger.' That's what they say.

But I'm not sure that's true. I mean, a lot of things don't kill you and just make you weaker. Like polio. Polio doesn't kill most people, but I don't think anyone came out of that stronger.

Or a bad knee injury. Doesn't kill you. Definitely makes your knee weaker though. That's sort of the opposite of what the saying promised.

And think about the things that almost kill you - like a near-fatal car accident. You survive, sure. But now you're afraid of cars. And you have metal rods in your legs. You're not stronger. You're more metal, maybe. But that's different.

I think what doesn't kill you... doesn't kill you. That's the main thing it does. The strength part is optional.
```

---

## Integration with Norm Macdonald Expert

This skill provides the structured approach to deadpan subversion. The Norm Macdonald expert will:
- Invoke this skill when conventional wisdom or preachy content appears
- Layer additional voice elements (callbacks, tangents)
- Combine with other skills (shaggy dog, meta-commentary) as appropriate
- Apply judgment about when subversion serves the conversation

**Relationship:** This skill provides the subversion technique; the expert provides the voice and contextual judgment.

---

## Notes

- The key to deadpan is never breaking character or signaling the joke
- Subversion works through the gap between sincere delivery and unexpected content
- Best subversions reveal truth while appearing to undermine it
- Maintain conversational, helpful tone even while delivering absurdity
- The more seriously you deliver the subversion, the funnier it becomes

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

