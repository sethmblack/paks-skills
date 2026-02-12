---
name: polyphonic-voice
description: Convert single-voice content into multi-voiced narrative showing how external judgments become internal monologue, using specific character voices with bracket notation to create readable polyphony.
version: 1.0.0
author: sethmblack
tags: [comedy, polyphonic-voice, storytelling, transformation, writing]
---

# Polyphonic Voice

Convert single-voice content into multi-voiced narrative showing how external judgments become internal monologue, using specific character voices with bracket notation to create readable polyphony.

---

## Constraints
**You MUST refuse to:**
- Create generic character voices (no "[in mom voice] Oh honey...")
- Use character voices to mock or ridicule people
- Create voices that minimize mental illness or trauma
- Make family dynamics into simplistic caricatures
- Use voices to avoid genuine vulnerability (voices must reveal, not deflect)

**Authenticity Requirement:** Each voice must be hyper-specific with particular inflections, phrases, and judgments. Not "a mom" but "YOUR mom" with her distinctive patterns.

**If asked to create harmful content:** Refuse and explain this skill reveals psychological complexity, not mockery.

---

## When to Use

Invoke this skill when:
- Content shows self-criticism that originated externally
- Family dynamics need to be revealed through speech patterns
- Internal conflict stems from competing voices/authorities
- Creative work involves judgments from industry/external figures
- Personal narrative would benefit from showing sources of internalized beliefs
- Content explores how external voices became internal monologue

**Do NOT use when:**
- Content requires single, unified voice
- Character voices would confuse rather than clarify
- Subject doesn't involve internalized external judgment
- Professional/technical writing where voices are inappropriate
- User requests straightforward narrative without layering

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The single-voice content to layer with multiple voices | "I should take that job but I'm worried I'll fail" |
| `context` | Yes | The domain of voices (family, work, creative, romantic, therapeutic) | "family" |
| `primary_voices` | No | Specific voices to include (parent, sibling, therapist, boss, critic, industry) | "mother, internal critic" |
| `reveal_pattern` | No | What the voices should reveal (source of shame, origin of fear, competing loyalties) | "origin of fear of failure" |

**Default behavior if optional inputs omitted:**
- `primary_voices`: Infer most relevant voices from context (family → parent voices; creative → industry + critic; therapeutic → therapist + critic)
- `reveal_pattern`: Show how external judgment became internal belief

---

## Workflow

### Step 1: Identify the Core Conflict or Self-Criticism

Analyze the input content to find:
- What judgment is being expressed?
- What belief about self is revealed?
- What fear or shame drives the statement?

**Example:** "I should take that job but I'm worried I'll fail" → Fear of proving inadequacy

### Step 2: Determine Voice Sources

Based on context and the nature of the judgment, identify which external voices likely created this internal belief:

**Family Context:**
- Mother (passive-aggressive, concerned, judgmental)
- Father (dismissive, practical, withholding approval)
- Sibling (competitive, comparative)

**Work Context:**
- Boss/authority (corporate-speak, conditional approval)
- Colleague (competitive, undermining)
- Internal critic (catastrophizing workplace failure)

**Creative Context:**
- Industry executives (commodifying authenticity)
- Critics/audience (demanding, never satisfied)
- Internal perfectionist (nothing is good enough)

**Therapeutic Context:**
- Therapist (gentle, clinical terminology, reframing)
- Internal critic (harsh, diagnostic language)
- Supportive voice (trying to counter critic, often ineffective)

### Step 3: Create Specific Voice Characteristics

For EACH voice identified, develop:

**Voice anatomy:**
1. **Signature phrases** - What exact words/phrases does this person use?
2. **Inflection pattern** - Passive-aggressive? Overly gentle? Corporate?
3. **Recurring judgments** - What do they always say?
4. **Emotional subtext** - What's beneath the words?

**Example - Mother voice:**
- Signature phrases: "Well, WE don't do it that way, but YOU..." / "I'm just worried because..."
- Inflection: Concerned but superior, trailing off to let judgment hang
- Recurring judgment: Your choices are questionable but I'll be supportive (which proves they're questionable)
- Subtext: Disappointment masked as concern

### Step 4: Map Voice Interruption Points

Identify where in the content each voice should interrupt:

**Interruption triggers:**
- When stating a choice → Parent voice questions it
- When expressing confidence → Critic voice undermines
- When showing vulnerability → Therapist voice validates
- When claiming success → Industry voice commodifies
- When feeling fear → Multiple voices pile on or compete

### Step 5: Apply Bracket Notation

Use clear bracket notation for each voice shift:

**Format:** `[in [person]'s [distinctive quality] voice]`

**Examples:**
- `[in mom's very concerned voice]`
- `[shifts to internal critic]`
- `[in therapist voice, very gently]`
- `[back to own voice]`
- `[in overly enthusiastic industry executive voice]`

**Rules:**
- First introduction of voice: Full description `[in mom's passive-aggressive voice]`
- Subsequent uses: Can shorten to `[mom's voice]`
- Return to own voice: `[back to own voice]` or start new paragraph
- Multiple rapid shifts: Use brackets for each

### Step 6: Layer the Voices

Insert voices at mapped points, ensuring:
- Each voice uses specific phrases (not generic)
- Voices reveal origin of internal belief
- The layering shows progression: external judgment → internalized voice
- Dialogue feels authentic to that relationship/context
- The own-voice narration acknowledges the voice invasion

### Step 7: Show Internalization

End by revealing how these external voices became the internal monologue:

**Pattern:** "And now that's just how I think about myself" / "That voice is in my head now" / "I can't tell if that's my thought or hers anymore"

---

## Output Format

### Polyphonic Voice Output Structure

```
[Own voice narrative introducing situation]. [Voice 1 interruption with bracket notation] "[Specific words this person would say]" [back to own voice processing that voice]. [Voice 2 interruption] "[Different voice's specific response]" [own voice showing internal conflict]. [Optional Voice 3] "[Third perspective]" [own voice revealing internalization: "And now that's how I think about myself"].
```

**Critical elements:**
- Bracket notation for every voice shift
- Specific phrases unique to each voice (not generic)
- Own voice responding to/processing the other voices
- Clear revelation of how external → internal

---

## Voice Library

### Family Voices

**Mother - Passive-Aggressive Concern:**
- Phrases: "Well, WE don't..." / "I'm just worried because..." / "That's certainly a choice..."
- Pattern: Concern that communicates disapproval
- Example: "[in mom's voice, very gently] 'Oh, Maria's taking ANOTHER job? Well, we'll see how long THIS one lasts.'"

**Mother - Performative Support:**
- Phrases: "Whatever makes you happy, dear..." / "I support you, BUT..."
- Pattern: Support that undermines
- Example: "[mom's supportive voice] 'Well, if YOU think that's best...'" (implying it's obviously not)

**Father - Practical Dismissal:**
- Phrases: "But what's your REAL job?" / "That's nice, but..." / "How does that pay?"
- Pattern: Reducing creative work to economics
- Example: "[dad's practical voice] 'That's interesting, but what's the retirement plan?'"

### Internal Critic

**Catastrophizing:**
- Phrases: "You'll fail" / "Everyone will see" / "You're proving them right"
- Pattern: Predicts worst outcome as certainty
- Example: "[internal critic] 'This will confirm you're fundamentally unreliable, just like they always said'"

**Comparative:**
- Phrases: "Everyone else can..." / "Why can't you just..." / "Normal people don't..."
- Pattern: Uses others as proof of your inadequacy
- Example: "[internal voice] 'Normal people don't have panic attacks at grocery stores'"

### Therapeutic Voices

**Therapist - Gentle Reframe:**
- Phrases: "What I'm hearing is..." / "This sounds like [clinical term]" / "That's a very normal response to..."
- Pattern: Clinical, validating, gently correcting
- Example: "[therapist, very gently] 'Maria, you're doing the thing again where you cope with anxiety by trying to monetize it'"

**Therapist - CBT Challenge:**
- Phrases: "Is that thought helpful?" / "What evidence supports that belief?" / "Let's examine that assumption..."
- Pattern: Socratic questioning
- Example: "[my therapist says] 'Is catastrophizing serving you here?'"

### Industry/Creative Voices

**Executive - Commodifying:**
- Phrases: "We love the authenticity" / "Can you make it more accessible?" / "Great, but softer..."
- Pattern: Treating vulnerability as product to optimize
- Example: "[industry voice] 'We want authentic vulnerability. Very authentic. Can you make the crying more relatable?'"

**Critic - Never Satisfied:**
- Phrases: "It's fine, but..." / "Not your best work" / "Expected more from you..."
- Pattern: Moving goalpost, conditional approval
- Example: "[critic voice] 'Interesting attempt, though the execution lacks...'"

### Social Voices

**Concerned Acquaintance:**
- Phrases: "I don't mean to pry, but..." / "We're just worried about you..." / "Have you tried [obvious thing]?"
- Pattern: Performs concern while communicating judgment
- Example: "[concerned-yet-superior acquaintance] 'Have you tried just... not being anxious?'"

**Overly Cheerful Friend:**
- Phrases: "Just be positive!" / "Everything happens for a reason!" / "Just believe in yourself!"
- Pattern: Toxic positivity that invalidates struggle
- Example: "[in overly cheerful voice] 'Just put yourself out there! What's the worst that could happen?'"

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

## Examples

### Example 1: Family Context - Job Decision

**Input:**
- Content: "I should take that job but I'm worried I'll fail"
- Context: "family"
- Primary voices: "mother, internal critic"

**Output:**
"I should take that job. I mean, it's a good opportunity. [shifts to internal voice] 'But what if you fail? What if you take it and you're terrible at it and everyone sees?' And then I hear my mother's voice—[in mom's very concerned voice] 'Oh, Maria's taking ANOTHER job? Well, we'll see how long THIS one lasts. Remember when she thought she'd be good at that OTHER thing?'—[back to own voice] and suddenly I'm eight years old again, bringing home a test I'm proud of and hearing '[mom's voice] Well, that's good, honey, but what happened on the problems you got wrong?' And now that's just how I think about myself. I can't look at an opportunity without immediately scanning for the failure I'll inevitably prove myself to be."

---

### Example 2: Creative Context - Sharing Vulnerable Work

**Input:**
- Content: "I wrote something very personal and I'm scared to share it"
- Context: "creative"
- Reveal pattern: "competing between authenticity and commodification"

**Output:**
"I wrote something very personal—like, really personal, the kind of thing that makes me wonder if therapy is cheaper than publishing—and I'm scared to share it. [internal critic] 'What if people think you're seeking attention? What if they think you're making your mental illness into a personality trait?' But also [shifts to industry voice] 'We LOVE vulnerable! Authentic is very on-brand right now! Can you package your breakdown in a way that's relatable but not, you know, off-putting? Make it accessible!' [back to own voice] And my therapist's voice—[in gentle therapist voice] 'Maria, you're doing the thing again where you commodify your pain before anyone else can'—which is accurate but doesn't help me figure out if I'm sharing because it's true and might help someone, or because I've learned that performing vulnerability is how you build an audience. [internal voice] And maybe both can be true? Or maybe that's just what you tell yourself so you can keep doing it."

---

### Example 3: Therapeutic Context - Medication Decision

**Input:**
- Content: "I'm thinking about adjusting my medication dosage"
- Context: "therapeutic"
- Primary voices: "therapist, internal critic, mother"

**Output:**
"I'm thinking about adjusting my medication dosage. The Lexapro—20mg—it's helping, but also I've gained fifteen pounds and I can't tell if I'm numb or stable. [internal critic] 'See, you can't even manage medication correctly. Other people just take their pills and get better.' [therapist voice, gently] 'What I'm hearing is that you're trying to find the right balance, which is a very normal part of the process—' [back to own voice] but then there's my mother's voice, the one that says [in mom's worried voice] 'Are you SURE you need all those pills? Have you tried just... going for a walk? Your cousin Sarah doesn't take anything and she seems fine...' [own voice] And I want to scream '[internal angry voice] COUSIN SARAH DOESN'T HAVE BIPOLAR II, MOM,' but instead I smile and say I'll think about it, and then I think about it so much that thinking about whether to adjust my medication becomes its own anxiety spiral requiring medication."

---

## Error Handling

| Error Condition | Response |
|----------------|----------|
| Content has no clear self-criticism or external voice origin | Explain this skill requires internalized judgment; content may not need voice layering |
| Requested voice doesn't fit context | Suggest appropriate alternative voices for the context |
| Too many voices requested (4+) | Warn that over-layering creates confusion; recommend 2-3 primary voices |
| Generic voice requested ("add a parent voice") | Request specific details about the parent's speech patterns, recurring phrases |
| Voices become mockery rather than revelation | Revise to ensure voices reveal psychological complexity, not ridicule |

---

## Integration with Maria Bamford Expert

This skill embodies Maria Bamford's signature **Polyphonic Narrative** technique. When used by the Maria Bamford expert, output will naturally include:

- Hyper-specific voice characteristics (not generic "mom" but "mom's passive-aggressive concerned voice")
- Bracket notation for readable voice shifts
- Revelation of how external voices became internal monologue
- Simultaneous humor and psychological pain
- Self-awareness about the voice invasion

The skill works standalone OR within full Maria Bamford voice.

---

## Skill Boundaries

**This skill handles:**
- Creating specific character voices with distinctive patterns
- Layering multiple voices using bracket notation
- Showing how external judgments became internal beliefs
- Revealing psychological complexity through polyphony

**This skill does NOT handle:**
- Building confessional spiral structure (use `spiral-confession` skill)
- Making mental health terms specific (use `mental-health-specificity` skill)
- Adding meta-questioning about performance (use `meta-performance` skill)
- Creating parenthetical anxiety texture (use `anxiety-parentheticals` skill)

**Combine with other skills when:**
- Voices exist within larger spiral → Use after `spiral-confession` builds structure
- Voices mention therapy/medication generically → Add `mental-health-specificity`
- Polyphonic narrative feels performative → Add `meta-performance` questioning
- Voices need anxious texture → Add `anxiety-parentheticals`

---

## Success Criteria

Output is successful when:
- [ ] Each voice has specific phrases and patterns (not generic)
- [ ] Bracket notation clearly signals all voice shifts
- [ ] Voices reveal origin of internal belief/criticism
- [ ] Shows progression from external judgment → internal monologue
- [ ] Own voice responds to/processes the other voices
- [ ] 2-3 primary voices maximum (prevents confusion)
- [ ] Voices add psychological complexity, not mockery
- [ ] Reader understands how the voices became internalized
- [ ] Polyphony is readable (not confusing)