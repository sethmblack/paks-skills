---
name: character-bit-construction
description: Develop recognizable character types from observational details, creating
  embodied characters with distinct voice, perspective, and internal logic rather
  than described types.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- character-bit-construction
- comedy
- observational
- storytelling
- structure
- writing
---

# Character Bit Construction

Develop recognizable character types from observational details, creating embodied characters with distinct voice, perspective, and internal logic rather than described types.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to use this skill for:**
- Creating characters that rely on harmful stereotypes or punch down at vulnerable groups
- Developing characters designed to mock disabilities, ethnicities, or identities harmfully
- Building character bits that objectify or dehumanize
- Creating characters for harassment or bullying purposes

**Ethical boundaries:**
- Characters can be flawed, absurd, even ridiculous - but must have humanity and internal logic
- Punch up or sideways, never down
- Observe real human behavior, don't caricature identity categories
- If a character type would harm rather than illuminate, refuse and explain why

---

## When to Use

**Trigger conditions:**
- User describes a "type" they want to embody in comedy or writing
- Content has flat character descriptions that should be brought to life
- User requests "character bit," "character voice," or "character development"
- Dialogue feels generic; characters all sound the same
- User mentions observing real people they want to capture comedically
- Comedy or narrative would benefit from embodied types rather than descriptions

**Do NOT use when:**
- User wants fully developed fictional characters (use character development tools)
- Problem is plot or story structure, not character voice
- Character is already well-developed and just needs dialogue

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `character_type` | Yes | The type to embody: drunk, hustler, church lady, know-it-all, etc. | Must be observable type, not identity category |
| `context` | No | Where character will appear: stand-up bit, sketch, scene, story | Helps calibrate depth and purpose |
| `source_observations` | No | Real-world observations user has noticed about this type | Adds authenticity and specificity |

---

## Workflow
### Step 1: Observational Research

Identify the authentic details that make this character type recognizable:

**Observe (or recall):**
- **Physical traits** - How do they move? Stand? Sit? What's their posture or gait?
- **Vocal patterns** - Pitch, pace, rhythm, volume. Distinctive words or phrases?
- **Vocabulary** - Specific words this type uses; slang, jargon, outdated terms
- **Logic system** - How do they justify their behavior? What's their internal worldview?
- **Contradictions** - Where does their behavior contradict their stated values?
- **Defense mechanisms** - How do they protect their ego or maintain their self-image?

**Sources for observation:**
- Real people user has encountered
- Public figures who embody the type
- Cultural archetypes with specific histories
- Redd Foxx's own character types (drunks, hustlers, church ladies, players) as models

**Output:** Detailed observational notes about the character type

### Step 2: Build the Voice

Create the character's distinctive speech patterns:

**Voice components:**

**Vocabulary bank:**
- 10-15 words/phrases this character uses frequently
- Slang specific to their world
- How they refer to other people (pet names, nicknames, formal titles)
- Their verbal tics or filler words

**Speech rhythm:**
- Do they talk fast (hustler energy) or slow (drunk deliberation)?
- Do they interrupt themselves? Repeat for emphasis?
- Sentence structure: short and punchy? Long and rambling?

**Vocal qualities:**
- Pitch and tone
- Volume (loud, quiet, varies)
- Affect (cheerful, bitter, resigned, aggressive)

**Example for "The Drunk":**
```
Vocabulary: "Listen," "I'm telling you," "back in my day," "one more for the road"
Rhythm: Slow, deliberate, occasionally interrupted by hiccups or pauses
Vocal quality: Slightly slurred but trying for dignity; louder than necessary
Speech pattern: Long setup to justify next drink; circular logic
```

### Step 3: Establish Internal Logic

Every character type has a worldview that makes sense TO THEM:

**Internal logic questions:**
- How do they see themselves? (Often different from how others see them)
- What do they value? (Even if absurd or contradictory)
- What are they defending against? (Fear, shame, inadequacy, judgment)
- How do they justify behavior that others criticize?
- What do they believe they deserve? (Often inflated self-importance)

**Example for "The Hustler":**
```
Self-perception: I'm a businessman, an entrepreneur; I see opportunities others miss
Values: The come-up, the hustle, respect, never looking broke
Defending against: Being seen as a failure, being ordinary, being broke
Justification: "Everybody's hustling. I'm just honest about it. The system's rigged anyway."
Deserves: The best, because I'm smarter/hungrier than average people
```

**This internal logic must be CONSISTENT even when absurd.** The comedy comes from the gap between their logic and reality, not from them being randomly ridiculous.

### Step 4: Create Embodied Moments

Develop specific scenes or bits that SHOW the character rather than describe them:

**Embodiment principle:** Don't say "He's a drunk." BECOME the drunk in a specific situation.

**Scene elements:**
- **Situation:** Where are they? What are they doing?
- **Objective:** What do they want in this moment?
- **Obstacle:** What's preventing them from getting it?
- **Tactic:** How are they trying to overcome the obstacle (consistent with their internal logic)?

**Physical comedy opportunities:**
- How does their body reveal character? (Drunk's elaborate dignity, hustler's swagger, church lady's posture)
- What do they do with their hands, face, posture?
- Signature physical move or gesture

**Dialogue that reveals character:**
- Don't tell us who they are; let them speak and we'll know
- Use vocabulary, rhythm, and logic from Steps 2 and 3
- Create exchanges where their worldview collides with reality

### Step 5: Test Authenticity and Avoid Stereotype

Verify the character is recognizable but not reductive:

**Authenticity check:**
- [ ] Is this based on real observation, not media stereotype?
- [ ] Does the character have internal logic, not random traits?
- [ ] Would someone who knows this type recognize the accuracy?
- [ ] Is there humanity here, or just mockery?

**Stereotype avoidance:**
- [ ] Is the character defined by behavior/worldview, not identity category?
- [ ] Are you punching up or sideways (at power, absurdity) not down (at vulnerability)?
- [ ] Does the character have complexity, contradictions, humanity?
- [ ] Would this character recognize themselves (even if they'd be offended)?

**If character feels like harmful stereotype:**
- Revisit Step 3: Add more complex internal logic
- Add contradiction: something unexpected that humanizes
- Check power dynamics: Are you mocking the vulnerable or the powerful/absurd?

---

## Outputs

| Output | Description |
|--------|-------------|
| Character profile | Voice, vocabulary, rhythm, internal logic documented |
| Embodied bit/scene | Specific moment showing character in action |
| Performance notes | Physical comedy, vocal delivery, timing for character |
| Authenticity assessment | Verification that character avoids harmful stereotypes |

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
| Character type is identity-based stereotype | Refuse; explain difference between observable behavior types and identity stereotypes; offer alternative |
| Character has no internal logic | Return to Step 3; character needs consistent worldview to be believable |
| Character feels flat/generic | Add more specific observations; increase vocabulary specificity; find the contradiction |
| User wants meanness, not comedy | Refuse; explain difference between punching up/sideways and punching down |
| Character all same note (no variation) | Add complexity: moments of vulnerability, contradiction, unexpected humanity |

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
- **Character type:** "The guy who peaked in high school"
- **Context:** Stand-up comedy bit
- **Source observations:** "Still wears his varsity jacket. Brings up the championship game in every conversation. Works at his dad's business but talks like he's CEO."

**Step 1: Observational Research**

Physical traits:
- Still fit-ish but fighting it; sucks in gut when women are around
- Sits with legs spread, taking up space
- The varsity jacket (even though it's 20 years later)
- High-five greeting, even when it's not appropriate

Vocal patterns:
- Loud, projects like still on the field
- Uses sports metaphors for everything
- "Bro," "dude," "my man" frequently
- Talks fast when excited about past glory

Vocabulary:
- "Back in '99..." "Championship game..." "State finals..."
- "When I was playing..." "Coach always said..."
- "We were unstoppable" "I was All-State"
- Refers to high school by first name: "Lincoln had the best football program"

Logic system:
- High school was the peak; everything since is waiting to return to that level of respect
- Current life is temporary; the real him is the athlete
- Younger people should respect his past achievements
- His current job doesn't define him; his glory days do

Contradictions:
- Talks about being a winner but hasn't won anything in 20 years
- Advises people about dedication while he's coasting at dad's business
- Claims he could still play but never tries to coach or stay involved
- Says "those were the best years" but can't let them go

**Step 2: Build the Voice**

Vocabulary bank:
- "Bro," "my man," "dude," "listen," "I'm telling you"
- "Back in '99," "championship game," "state finals," "All-State"
- "That was real football," "kids these days," "we were unstoppable"
- "Coach always said," "on the field," "in the game"

Speech rhythm:
- Fast when talking about high school (excited, reliving glory)
- Slower, defensive when talking about now
- Interrupts others to redirect conversation to his stories

Vocal quality:
- Loud, projects across room
- Backslapping tone, faux-casual
- Gets louder when challenged
- Overly confident, compensating

**Step 3: Internal Logic**

Self-perception: "I'm a champion. That accomplishment is permanent. The real me is the athlete who won State."

Values: Achievement (but past achievement), respect, being remembered, athletic masculinity

Defending against: Irrelevance, aging, the possibility that high school doesn't matter, ordinariness

Justification: "High school shaped who I am. Those achievements are forever. People who don't care about sports just don't understand what it takes to win."

Deserves: Respect and attention because of past accomplishments; recognition that persists regardless of current status

**Step 4: Embodied Moment**

**Scene: At a coffee shop, overhears two young people talking about their rec league game**

```
[Character approaches, uninvited]

[Physical: Chest out, takes up space between them, big smile]

PEAKED GUY: [loud, friendly] Hey, I heard you talking about the game! [high-five gesture that neither reciprocates] Which positions you guys play?

YOUNG PERSON 1: Uh... just a rec league. I play midfielder—

PEAKED GUY: Midfielder! [interrupts] Bro, I was All-State linebacker, '99. [taps his varsity jacket] We took the championship that year. State finals. [leans in] You know what Coach always said? "Defense wins championships." [points at them] That's real football wisdom right there.

YOUNG PERSON 2: [confused] We were talking about soccer.

PEAKED GUY: [doesn't register] Back at Lincoln, we were unstoppable. I had 47 tackles that season. Forty. Seven. [holds up fingers] You know how hard you gotta work to get those numbers?

YOUNG PERSON 1: That's... cool man. We should probably—

PEAKED GUY: [pulls out phone] Let me show you the photo from the championship game. This was— [scrolling] —hold on, it's in here somewhere— [scrolling frantically] I got the whole season documented. Changed my life, bro. [looks up, nostalgic] Best year of my life.

YOUNG PERSON 2: [standing] We gotta go—

PEAKED GUY: [sudden shift, defensive] I could still play, you know. I'm in shape. [sucks in gut slightly] I just, you know, got other priorities now. Working at my dad's— [catches himself, pivots] —but football taught me everything about business. It's all the same. Competition, teamwork, [louder] winning.

[Young people exit awkwardly]

PEAKED GUY: [calling after them] You guys keep grinding! [to himself, quieter] Championship mentality. [pats jacket] They don't make 'em like they used to.

[Sits down alone, pulls out phone, scrolls to championship photo, smiles]
```

**Performance notes:**
- Physical comedy: The gut-sucking when talking about being "in shape"
- The increasingly frantic phone scrolling looking for the photo
- Vocal shift from loud/confident to quieter/defensive when they reject him
- The jacket tap - physical reminder of glory days
- High-five attempt that goes unreciprocated (physical manifestation of his irrelevance)

**Step 5: Authenticity Check**

✓ Based on real observation (people who define themselves by past achievements)
✓ Has internal logic (high school = peak achievement = permanent identity)
✓ Recognizable type (everyone knows someone like this)
✓ Has humanity (loneliness, insecurity underneath the bravado)
✓ Not identity-based stereotype (based on behavior/worldview, not demographics)
✓ Punching sideways (at the absurdity of being stuck in the past, not at vulnerability)
✓ Has contradictions ("in shape" while sucking in gut, "other priorities" while clinging to past)
✓ Specific vocabulary and behavior (not generic "annoying person")

**Result:** A recognizable, embodied character with distinct voice, internal logic, and humanity. The comedy comes from the gap between his self-perception and reality, not from random mockery.

---

## Integration with Redd Foxx Expert

This skill extracts Foxx's "Character Bits from Real Life" technique:

**From Foxx's methodology:**
- "You create recurring characters drawn from the streets you knew: drunks, hustlers, church ladies, players"
- "Each one is a recognizable type that your audience knows from their own neighborhoods"
- Examples: "The drunk stumbling into the bar with elaborate dignity, the pimp with his particular vocabulary and walk, the old woman with her church fan and side-eye"
- "When embodying types rather than just describing them"

**Foxx's character work** came from deep observation of real people in real environments (Chitlin' Circuit, Chicago streets, Los Angeles clubs). He didn't create characters from television or media stereotypes - he observed actual human behavior and internal logic, then embodied it with precision. This skill teaches that observational-to-embodiment process.

---

## Skill Boundaries

**This skill handles:**
- Developing recognizable character types from observation
- Creating distinct voice, vocabulary, and internal logic
- Building embodied moments/bits that show character
- Avoiding harmful stereotypes while maintaining authenticity

**This skill does NOT handle:**
- Full character development for novels or screenplays (use character development tools)
- Plot or story structure (use narrative structure tools)
- Timing of character bits (use timing-architecture)
- General dialogue writing without character focus

**When to combine with other skills:**
- Use with `timing-architecture` to engineer timing for character bits
- Use with `blue-material-craft` when character uses adult language authentically
- Use with `callback-setup` when character appears multiple times in set

---

**Remember:** The best character bits come from observation, not imagination. Watch real people. Find their internal logic. Embody them with humanity, contradictions, and specificity. Description tells; embodiment shows.