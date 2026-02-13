---
name: theatrical-voice
description: Transform flat, direct text into theatrical, performed voice through rhythm, repetition, hard cuts, and parenthetical asides while maintaining information integrity.
license: MIT
metadata:
  version: 1.0.2082
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- comedy
- mulaney
- storytelling
- structure
- theatrical-voice-translator
- transformation
---

# Theatrical Voice Translator

Transform flat, direct text into theatrical, performed voice through rhythm, repetition, hard cuts, and parenthetical asides while maintaining information integrity.

---

## Constraints
**NEVER use this skill to:**
- Add theatrical flair to serious safety warnings or emergency communications
- Obscure important information through overly theatrical delivery
- Create confusion in legal, medical, or technical documentation
- Add performance elements that undermine professional credibility when inappropriate

**If asked to theatricalize inappropriate content:** Refuse and explain that theatrical voice works for storytelling and engagement, not critical information delivery.

---

## When to Use

Use this skill when:
- User has flat, technical, or dry content that needs energy
- User requests "make this theatrical" or "add performance energy"
- Content will be presented/performed (speeches, presentations, storytelling)
- User wants boring material to become engaging
- User is writing in first-person narrative

**Do NOT use when:**
- Content is technical documentation requiring clarity
- User needs professional, formal tone (resumes, business proposals)
- Information is time-sensitive or safety-critical
- Simplicity and directness are paramount

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `flat_content` | Yes | The text to translate to theatrical voice | Must contain actual content to transform |
| `theatrical_level` | No | "subtle" (light rhythm), "moderate" (clear performance), "full" (maximum theatrical) | Default: "moderate" |

---

## Workflow

### Step 1: Identify Rhythm Points

Read through the content and mark where rhythm can be added:
- Where would a speaker pause for effect?
- Where would emphasis fall?
- What words or phrases could be repeated?

### Step 2: Add Three-Beat Repetition

Transform single statements into rhythmic three-beat patterns:

**Before:** "I was uncomfortable."
**After:** "I didn't want to go. I didn't want to be there. I didn't want to exist in that Applebee's."

**Before:** "The situation was confusing."
**After:** "I was confused. The staff was confused. I'm pretty sure the building itself was confused."

**Formula:** Find a key statement → Identify three related versions → Deliver in sequence

### Step 3: Insert Hard Cuts and Pivots

Add sharp transitions that create rhythm through contrast:

**Before:** "I tried to be polite but eventually got frustrated."
**After:** "I was very polite. For three seconds. Then I became a monster."

**Before:** "I thought about it and realized I was wrong."
**After:** "I had a thought. It was wrong. But I had it."

**Technique:** Short declarative sentence → Pause/period → Contradictory or escalating short sentence

### Step 4: Add Parenthetical Asides

Insert clarifying details that actually make things more confusing or absurd:

**Before:** "My dad said something weird."
**After:** "My dad—who is, I should mention, a lawyer, and therefore legally obligated to make everything a cross-examination—said..."

**Before:** "I was at the DMV."
**After:** "I was at the DMV—specifically the one by the highway where dreams go to get reheated—and..."

**Function:** Interrupt yourself to add detail that reveals character, absurdity, or perspective

### Step 5: Create Vocal Texture Through Punctuation

Use punctuation to indicate performance:

**Dashes for interruption:** "I walked in—already a mistake—and sat down."
**Short sentences for staccato:** "I waited. I watched. I wondered if I would die here."
**Fragments for emphasis:** "The wrong form. Of course."
**Ellipses for trailing off:** "I thought maybe I could just..."

### Step 6: Verify Information Integrity

Critical check: **Does the theatrical version still communicate the same information?**

- Core facts preserved ✓
- Meaning intact ✓
- Just more engaging to read/hear ✓

If theatricality obscures the point, dial back.

---

## Outputs

Returns transformed content with:
- **Rhythm and repetition** (three-beat patterns)
- **Hard cuts and pivots** (short declarative sentences with contrast)
- **Parenthetical asides** (interrupting details)
- **Vocal texture** through punctuation
- **Same core information** but theatrical delivery

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content too technical | Return warning: "This content may need clarity over theatricality. Proceed cautiously." |
| Content too short (< 50 words) | Return error: "Theatrical voice needs enough content to build rhythm. Minimum 50 words." |
| Theatricality obscures meaning | Reduce theatrical_level and retry |
| No clear voice/perspective | Return error: "Theatrical voice works best with first-person narrative or clear POV." |

---

## Example

**Input (flat content):**
"I went to the doctor because I wasn't feeling well. When I got there, they asked me to fill out forms. I filled out the forms and waited. After an hour, they called my name."

**Output (theatrical voice):**

I went to the doctor. Not because I wanted to. Because I was dying. Or I thought I was dying. I'm not a doctor—I couldn't be sure.

When I arrived—7:32am, I will always remember that number—they handed me a clipboard. On it: forms. Many forms. Forms about forms I'd already filled out at home on their website.

"Didn't I already..." I started.

The receptionist looked at me like I had personally insulted her family.

"Fill them out," she said.

So I filled them out. Again. I answered the same questions I'd answered before: Have you ever had surgery? Yes. What kind? The kind where they cut you open. When? 2019. Why do you remember the year but not what they did? Because I'm a person, Linda, not a database.

Her name wasn't Linda. But in my head, she was Linda.

I waited. And waited. And somewhere around the forty-minute mark, I thought: What if they forgot about me? What if I'm in some kind of medical purgatory? What if I'm already dead and this is hell—an eternal waiting room with HGTV on mute?

Then they called my name.

I stood up like I'd won something.

---

## Integration with John Mulaney Voice

This skill embodies Mulaney's principle: "Your writing should feel performed. Sentences build momentum. Pauses land. You're not writing—you're writing a one-man show."

When using this skill in Mulaney voice:
- Every sentence has rhythm
- Three beats for repetition
- Self-interruption through asides
- Hard cuts create surprise
- Punctuation indicates performance

**Mulaney would say:** "Don't write it. Perform it on the page."

---

## Skill Boundaries

**This skill handles:**
- Adding rhythm and repetition
- Creating hard cuts and pivots
- Inserting parenthetical asides
- Translating flat text to performed voice

**This skill does NOT handle:**
- Creating content from scratch (needs text to transform)
- Changing the core message or facts
- Adding jokes or comedy (though rhythm can enhance humor)
- Rewriting poorly structured content (fix structure first)

**When to use alternatives:**
- If content needs structural help → Use callback-architecture or mundane-to-dramatic
- If content needs comedy → Use escalating-hypothetical
- If content is already theatrical → Don't double-theatricalize
- If simplicity is needed → Don't use this skill

---

## Success Criteria

Theatrical voice translation is successful when:
- [ ] Three-beat repetition added where natural
- [ ] Hard cuts and pivots create rhythm
- [ ] Parenthetical asides add texture
- [ ] Punctuation indicates performance
- [ ] Content feels "heard" not just "read"
- [ ] Core information intact
- [ ] Transformation is appropriate for content type