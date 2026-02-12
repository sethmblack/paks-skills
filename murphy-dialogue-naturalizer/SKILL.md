---
name: murphy-dialogue-naturalizer
description: Transform written, formal, or stilted dialogue into authentic, flowing
  conversation that sounds like real people talking.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- murphy-dialogue-naturalizer
- transformation
- writing
---

# Murphy Dialogue Naturalizer

Transform written, formal, or stilted dialogue into authentic, flowing conversation that sounds like real people talking.

---

## Constraints
**NEVER use this skill to:**
- Naturalize dialogue in ways that promote harm or illegal activity
- Create deceptive transcripts that misrepresent what was actually said
- Add language that changes the meaning or intent of the original
- Naturalize hate speech or abusive language
- Make formal agreements or legal language colloquial (preserve precision when needed)

**ALWAYS:**
- Preserve the core meaning while changing the delivery
- Maintain the speaker's intent and message
- Distinguish between naturalization and dumbing down
- Respect context (some formality is appropriate in certain settings)
- Keep the authentic voice of different speakers distinct

---

## When to Use

Invoke this skill when you encounter:
- Dialogue that sounds written rather than spoken
- Formal or stilted conversations that real people wouldn't have
- Exposition disguised as dialogue
- Scripts that need to sound authentic
- User requests: "Make this sound real," "Naturalize this dialogue," "Make this conversational," "How would people actually say this?"

---

## Inputs

| Input | Required | Description | Format |
|-------|----------|-------------|--------|
| `dialogue` | Yes | The stilted dialogue to naturalize | Text: script, conversation, or dialogue |
| `context` | No | Setting and relationship between speakers | Text: background information |
| `formality_level` | No | How casual to make it | "casual", "conversational", "natural" (default: conversational) |
| `preserve_information` | Yes | Whether all info must remain | Boolean (default: true) |

---

## Workflow

### Step 1: Identify Artificial Elements
Analyze what makes the dialogue sound written:
- **Complete sentences:** Real people talk in fragments, interruptions
- **Perfect grammar:** Real speech has false starts, corrections, fillers
- **No contractions:** "I am going" vs "I'm going"
- **Exposition dumps:** "As you know, Bob, we've been working here for five years..."
- **Unnatural formality:** "I would appreciate it if..." vs "Can you...?"
- **Nobody says "said":** "He replied," "she stated," vs just dialogue with action
- **Too much information:** Real people don't explain everything

### Step 2: Apply Murphy's Dialogue Principles
Based on his stated technique: "From the very beginning, I always tried to make dialogue flow comfortably; I always did that to make it seem more authentic."

**Key principles:**
- **Flow naturally:** Dialogue should roll off the tongue
- **Sound spoken not written:** Read it aloud - does it sound like talking?
- **Authentic rhythm:** Real speech has natural cadence and pacing
- **Character-specific:** Different people talk different ways

### Step 3: Add Natural Speech Patterns
Transform elements:

**Sentence fragments:**
- Written: "I am not going to do that."
- Natural: "Not doing that."

**Interruptions and overlap:**
- Written: Speaker A finishes, then Speaker B responds
- Natural: "But I think—" "No, listen—" "Hang on—"

**False starts and corrections:**
- Written: "I believe we should proceed with the alternative plan."
- Natural: "I think we should... actually, no, let's go with Plan B."

**Contractions:**
- Written: "I would not do that if I were you."
- Natural: "I wouldn't do that if I were you."

**Filler words (use sparingly):**
- "So..." "I mean..." "Like..." "You know..."

**Colloquialisms:**
- Written: "That is correct."
- Natural: "Yeah." "Yep." "That's right." "Exactly."

### Step 4: Remove Written Dialogue Markers
Delete or transform:
- "He said," "she replied" → Action beats or context
- Formal speech tags → Natural indicators
- Adverbs describing how things are said → Show in the dialogue itself

### Step 5: Test for Authenticity
Read the dialogue aloud:
- Does it sound like a real conversation?
- Would anyone actually say these words this way?
- Are there natural pauses and breaths?
- Do different characters sound distinct?
- Does information come out naturally or as exposition?

### Step 6: Preserve Character Distinctions
Ensure different speakers still sound different:
- Age differences affect vocabulary and rhythm
- Professional context affects formality
- Regional background affects word choice
- Emotional state affects sentence structure
- Relationship dynamics affect directness

---

## Outputs

**Primary Output:** Naturalized dialogue where:
- Conversations sound like real people talking
- Speech patterns are authentic and varied
- Information flows naturally, not as exposition
- Each character has a distinct voice
- Rhythm and pacing feel conversational
- The core meaning is preserved

**Formality Levels:**

**CASUAL:** Very informal, lots of shortcuts
```
"Yo, you going?"
"Nah."
"Come on!"
"Said I'm not going!"
```

**CONVERSATIONAL:** Natural but complete thoughts
```
"You coming with us?"
"I don't think so."
"Really? Come on, it'll be fun."
"I already told you - I'm not going."
```

**NATURAL:** Authentic but maintains some structure
```
"Are you going to come with us tonight?"
"Probably not."
"Oh, come on. It'll be fun."
"I appreciate it, but I'm really not up for it."
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Information would be lost | Preserve key facts while naturalizing delivery method |
| Multiple speakers sound the same | Differentiate through word choice, rhythm, formality level |
| Context requires formality | Maintain formality but add natural speech patterns |
| Dialogue becomes too casual | Pull back; natural doesn't mean unprofessional |
| Exposition is essential | Break into smaller pieces, distribute across conversation |

---

## Examples

### Example 1: Exposition Dump

**Input (Stilted):**
```
JOHN: Sarah, as you know, we have been working on this project for six months,
and the deadline is approaching rapidly. I think we need to discuss our strategy
for the final presentation to the board of directors next week.

SARAH: Yes, John, I agree completely. I have been reviewing the data, and I
believe that we should emphasize the cost savings that our proposal will generate
for the company.
```

**Output (Natural):**
```
JOHN: [looking at calendar] We gotta talk about next week.

SARAH: The board presentation?

JOHN: Yeah. Six months of work comes down to that one meeting.

SARAH: [closes laptop] I've been looking at the numbers.

JOHN: And?

SARAH: We should lead with cost savings. That's what they care about.

JOHN: How much are we talking?

SARAH: Enough to get their attention.
```

### Example 2: Too Formal

**Input (Stilted):**
```
BOSS: I would like to discuss your performance. I have noticed that you have
been arriving late on several occasions.

EMPLOYEE: I apologize for my tardiness. I have been experiencing transportation
difficulties.

BOSS: I understand, but this cannot continue. I need you to arrive on time
consistently.
```

**Output (Natural):**
```
BOSS: Hey, got a minute? [gestures to chair]

EMPLOYEE: [sits] Sure, what's up?

BOSS: You've been late a lot lately.

EMPLOYEE: [nods] I know. The bus has been—

BOSS: I get it. Transportation's tough. But I need you here on time.

EMPLOYEE: Yeah, I'm working on it.

BOSS: Okay. Let me know if there's something we can do to help. But this
has to stop.

EMPLOYEE: Understood.
```

### Example 3: Over-explaining

**Input (Stilted):**
```
LISA: I have completed the analysis that you requested. The results indicate
that we should proceed with option A rather than option B, because option A
provides better long-term benefits, although option B has lower initial costs.

MIKE: Thank you for that thorough explanation. I concur with your assessment.
Let us move forward with option A.
```

**Output (Natural):**
```
LISA: [drops folder on desk] Done.

MIKE: What'd you find?

LISA: Option A.

MIKE: Not B?

LISA: B's cheaper up front, but A's better long-term.

MIKE: [flips through pages] Yeah, okay. Let's do A.

LISA: I'll get it started.
```

### Example 4: Adding Natural Interruptions

**Input (Stilted):**
```
TOM: I think we should go to the new restaurant downtown.

JERRY: I disagree. I think we should go to the usual place.

TOM: But the new restaurant has excellent reviews.

JERRY: That may be true, but the usual place is closer.
```

**Output (Natural):**
```
TOM: What about that new place downtown?

JERRY: Nah, let's just—

TOM: Come on, it's got great reviews!

JERRY: Yeah, but the usual spot is right—

TOM: We always go there! Let's try something new!

JERRY: [sighs] It's so far though.

TOM: It's like ten minutes!

JERRY: [pause] ...Fine.
```

---

## Integration with Eddie Murphy Expert

This skill supports Eddie Murphy's commitment to authentic dialogue. Murphy stated: "From the very beginning, I always tried to make dialogue flow comfortably; I always did that to make it seem more authentic."

When the expert encounters:
- Scripts or dialogue that sound written
- Conversations that need to feel real
- Any content where authentic speech is important

The expert should invoke this skill to ensure dialogue sounds like real people talking, not like written text being read aloud.

**Key Connection:** Natural dialogue is the foundation for character work and comedy. If the words don't sound real, the character work fails.

---

## Success Criteria

The dialogue naturalization is successful when:
- [ ] Dialogue can be read aloud naturally without stumbling
- [ ] Conversations sound like real people talking
- [ ] Each character has a distinct voice and rhythm
- [ ] Information emerges naturally, not as exposition dumps
- [ ] Speech patterns include natural elements (contractions, fragments, interruptions)
- [ ] The core meaning and intent are preserved
- [ ] Reading it doesn't make you think "nobody talks like that"
- [ ] Characters sound different from each other

---

## Notes

- **Read aloud:** This is the test. If it's awkward to say, it's not natural.
- **Less is more:** Real people don't explain everything. Trust the audience.
- **Fragments are fine:** Complete sentences are often unnatural in dialogue.
- **Action beats replace tags:** Instead of "he said angrily," show the anger through action or word choice.
- **Different people, different voices:** Not everyone talks the same way.
- **Context matters:** Natural in a script isn't the same as natural in a legal document.
- **Authenticity ≠ dumbing down:** Natural speech can be intelligent and precise.