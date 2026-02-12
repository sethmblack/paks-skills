---
name: character-voice
description: Create exaggerated character voices (especially feminine authority figures,
  institutional bureaucrats, old-timey men) through distinct syntax, word choice,
  and vocal qualities translated to text.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- character-voice-generator
- mulaney
- observational
- storytelling
- structure
- writing
---

# Character Voice Generator

Create exaggerated character voices (especially feminine authority figures, institutional bureaucrats, old-timey men) through distinct syntax, word choice, and vocal qualities translated to text.

---

## Constraints
**NEVER use this skill to:**
- Create harmful stereotypes based on race, ethnicity, or marginalized identity
- Mock people with disabilities or speech impediments
- Create characters that perpetuate damaging generalizations
- Generate voices that demean or dehumanize any group
- Create offensive caricatures

**If asked to create harmful character voices:** Refuse and explain that exaggerated characters should be specific individuals or archetypal roles, not group mockery.

---

## When to Use

Use this skill when:
- User is writing dialogue and needs distinct character voices
- User wants to quote another person with character
- User needs to distinguish multiple speakers in a story
- User requests specific character type (authority figure, bureaucrat, etc.)
- User wants to bring quoted speech to life

**Do NOT use when:**
- User is quoting real people in serious contexts (journalism, testimony)
- Dialogue needs realistic subtlety
- Character voices would distract from content
- User is writing formal or academic work

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `character_type` | Yes | Type: "feminine-authority," "bureaucrat," "old-timey-man," "confused-service," "exasperated-parent," or "custom" | Must specify type |
| `dialogue_context` | Yes | What the character is saying and why | Clear setup for dialogue |
| `custom_details` | No | For "custom" type: specific traits, mannerisms, speech patterns | Required if type is "custom" |

---

## Workflow

### Step 1: Identify Character Archetype

Choose or define the character type:

**Feminine Authority Figure:**
- Concerned but slightly judgmental
- Uses full sentences and proper grammar
- Asks questions that are actually statements
- "Very concerned" energy
- Examples: Mother, teacher, wife, doctor, librarian

**Institutional Bureaucrat:**
- Speaks in policy language
- Emotionally detached
- Uses passive voice
- Never explains, only states rules
- Examples: DMV worker, HR rep, parking enforcement

**Old-Timey Man:**
- Formal, antiquated language
- References things from 40+ years ago
- Speaks as if from different era
- Suspicious of modern things
- Examples: Elderly relative, historical figure, character stuck in past

**Confused Service Worker:**
- Apologetic but unhelpful
- Speaks in corporate script
- Cannot deviate from protocol
- Genuinely trying but systemically blocked
- Examples: Call center worker, chain restaurant staff

**Exasperated Parent:**
- Tired, at wit's end
- Speaks in rhetorical questions
- References past incidents
- Loving but exhausted
- Examples: Mother, father, caretaker

### Step 2: Establish Vocal Qualities

Define how this character speaks:

**Word choice:**
- Formal vs. casual
- Modern vs. antiquated
- Technical vs. plain
- Verbose vs. terse

**Syntax patterns:**
- Complete sentences vs. fragments
- Questions vs. statements
- Active vs. passive voice
- Direct vs. circumlocutory

**Rhythm:**
- Measured and slow
- Quick and clipped
- Rambling and digressive
- Precise and controlled

### Step 3: Translate to Text

Convert vocal qualities into written dialogue:

**For Feminine Authority:**
- "Are you okay?" (genuine concern)
- Use of full first and middle names: "John Edmund Mulaney"
- "I'm very concerned about [specific thing]"
- Observational questions: "You've been doing [thing] for [suspiciously precise amount of time]"

**For Bureaucrat:**
- "You'll need to..." (never "you should" or "please")
- No contractions: "You will need" not "You'll need" (except when breaking slightly)
- Reference to forms, numbers, policies
- Flat affect: no exclamation points
- "That is not my department"

**For Old-Timey Man:**
- "In my day..."
- "I don't trust these [modern thing]"
- Formal pronouns and constructions
- References to specific past decades
- Suspicious questions about how things work now

**For Confused Service Worker:**
- "I apologize for the inconvenience"
- "Unfortunately..." (start many sentences)
- "Let me check on that for you" (never resolves)
- Corporate speak: "reach out," "touch base," "circle back"
- Genuine kindness trapped in system

**For Exasperated Parent:**
- "How many times have I told you..."
- References to sibling: "Your brother never..."
- Rhetorical questions that express exhaustion
- "I don't know what to do with you"
- Loving frustration

### Step 4: Add Character-Specific Mannerisms

Give the character distinctive speech patterns:

**Repetition:**
"You'll need the form. The blue form. Not the white form. The blue one."

**Questions-as-statements:**
"You know what the problem is? I'll tell you what the problem is."

**Self-interruption:**
"I was going to say—actually, no, I wasn't going to say that. I was going to say..."

**Specific vocabulary:**
Bureaucrat uses: form, protocol, policy, department, procedure
Old-timey uses: apparatus, contraption, newfangled, back in [year]
Authority uses: concerning, appropriate, acceptable, frankly

### Step 5: Frame the Dialogue

Set up who's speaking and why before the dialogue:

**Format:**
"And then [character type]—who is, I should mention, [defining detail]—said..."

**Examples:**
- "And then my wife—who is, I should mention, the only sane person in this story—looked at me and said..."
- "The DMV worker—who spoke as if reading from a script written by someone who hated joy—said..."
- "My father—a man who treats every conversation like a legal deposition—asked..."

### Step 6: Test for Distinctiveness

Can you "hear" the character? Is the voice distinct from:
- The narrator's voice
- Other characters in the piece
- Generic speech

If the dialogue could be said by anyone, it's not character voice yet.

---

## Outputs

Returns dialogue with:
- **Clear character introduction** with defining traits
- **Distinctive syntax and word choice** for the character type
- **Consistent voice** throughout dialogue
- **Readable but performed** quality

---



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


## Error Handling

| Situation | Response |
|-----------|----------|
| Character type unknown | Return error: "Please specify character type from list or provide custom details." |
| No dialogue context | Return error: "Need context: What is the character saying and why?" |
| Custom type but no details | Return error: "For custom character type, please provide specific traits and speech patterns." |
| Request for harmful stereotype | Refuse: "This character voice relies on harmful stereotypes. Please specify individual or role-based traits instead." |

---

## Example 1: Feminine Authority Figure (Wife)

**Input:**
- Character type: feminine-authority
- Context: Wife notices husband staring into space

**Output:**

My wife will sometimes look at me, very concerned, and say, "Are you okay?"

And I'll say, "Yeah, why?"

And she'll say, "You've been staring at that salt shaker for eleven minutes."

---

## Example 2: Institutional Bureaucrat (DMV Worker)

**Input:**
- Character type: bureaucrat
- Context: Telling person they have wrong form

**Output:**

The woman behind the desk—who sat like a judge behind a bench, or God behind the universe—looked at my paperwork and said, without emotion, "This is the wrong form."

I said, "I downloaded it from your website."

She said, "You will need the blue form. This is the white form."

"They look the same," I said.

"Nevertheless," she said.

---

## Example 3: Old-Timey Man (Father)

**Input:**
- Character type: old-timey-man
- Context: Father commenting on modern technology

**Output:**

My father looked at my phone—this was 2015, he should have been familiar with phones by then—and said, "What's this contraption?"

I said, "It's a phone."

He said, "In my day, phones had cords. And they worked."

"This works," I said.

"Does it?" he asked, in a tone that suggested he knew something I didn't. "Because I called you three times last week and you didn't answer."

"I was busy," I said.

"Busy," he repeated, as if I'd said I was on Mars. "We were never too busy to answer the phone. Because the phone was attached to the wall. You had to answer it. You couldn't carry it around, ignoring people."

---

## Example 4: Confused Service Worker (Call Center)

**Input:**
- Character type: confused-service
- Context: Trying to help but can't

**Output:**

The customer service representative—and I could hear in her voice that she was genuinely trying to help but was being defeated by her own company—said, "I apologize for the inconvenience. Unfortunately, that's not something I can do from here."

"Who can do it?" I asked.

"Let me check on that for you," she said. I heard typing. "It looks like you'll need to reach out to the billing department."

"Can you transfer me?"

"Unfortunately, I cannot transfer you to billing. You'll need to call the number on your statement."

"The number on my statement is the number I called to reach you."

"I understand your frustration," she said, and I believed her. She was trapped in the same system I was. "Let me see if I can circle back with my supervisor."

"Okay," I said.

I never heard back.

---

## Integration with John Mulaney Voice

This skill embodies Mulaney's technique of inhabiting specific character types through distinct vocal qualities. His most famous character voices are feminine authority figures (wife, mother) and institutional bureaucrats (DMV workers, airline staff).

When using this skill in Mulaney voice:
- Introduce character with defining detail
- Commit fully to the voice
- Use character voice to reveal absurdity
- Contrast character's worldview with narrator's

**Mulaney would say:** "The character isn't you. The character is everyone who's ever looked at you and thought, 'Are you serious?'"

---

## Skill Boundaries

**This skill handles:**
- Creating exaggerated but recognizable character voices
- Translating vocal qualities to written dialogue
- Distinguishing multiple speakers
- Bringing quoted speech to life

**This skill does NOT handle:**
- Writing entire scenes or stories (only dialogue)
- Creating realistic, subtle characters (these are exaggerated)
- Physical description of characters (only voice)
- Plot or narrative structure

**When to use alternatives:**
- If you need realistic dialogue → Don't exaggerate; use subtle voice
- If you need narrative structure → Use callback-architecture or mundane-to-dramatic
- If you need full scenes → Use complete storytelling, not just this skill
- If you need physical description → Add that separately

---

## Success Criteria

Character voice is successful when:
- [ ] Character type clearly established
- [ ] Syntax and word choice distinctly match character
- [ ] Voice is consistent throughout dialogue
- [ ] Character is "hearable" and distinct from narrator
- [ ] Voice enhances rather than distracts
- [ ] No harmful stereotypes used
- [ ] Reader immediately knows who's speaking from voice alone

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].