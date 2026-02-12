---
name: physical-character-blueprint
description: Create a complete physical characterization through movement, posture, and gesture before adding words. Based on Red Skelton's methodology of defining characters through their bodies first.
version: 1.0.0
author: sethmblack
tags: [comedy, physical-character-blueprint, transformation, writing]
---

# Physical Character Blueprint

Create a complete physical characterization through movement, posture, and gesture before adding words. Based on Red Skelton's methodology of defining characters through their bodies first.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create physical characterizations for:**
- Harmful stereotypes or mockery of protected groups
- Characters designed to demean or dehumanize
- Offensive caricatures based on race, disability, or identity
- Physical descriptions that promote harmful body standards

**If asked to create a harmful characterization:** Refuse explicitly and suggest finding the character's humanity instead.

---

## When to Use

- Creating a new character for performance, writing, or communication
- Character feels abstract or unclear - needs concrete embodiment
- Developing a persona for brand, content, or storytelling
- Need to make a character immediately recognizable and memorable
- Want character differentiation through physical traits rather than just personality

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `character_concept` | Yes | Brief description of character (role, archetype, essence) | 1-3 sentences |
| `emotional_core` | Yes | Central feeling or trait that defines them | Single word or short phrase |
| `context` | No | Where/how character will be used (performance, writing, video, etc.) | Text description |
| `reference_persons` | No | Real people who inspired this character | List of names/descriptions |

**Example Input:**
```
character_concept: "A nervous corporate executive who's overwhelmed by technology"
emotional_core: "Confusion mixed with desperate desire to appear competent"
context: "Video sketch series about modern workplace"
```

---

## Workflow

### Step 1: Define the Walk
Every character walks differently. The walk reveals everything.

**Questions to answer:**
- What's their pace? (Rushed, leisurely, uncertain, purposeful)
- What's their stride length? (Short shuffles, long strides, erratic)
- Where is their center of gravity? (Leaning forward, slumped back, straight)
- What moves first? (Head, hips, feet, shoulders)
- Do they stumble, glide, stomp, or shuffle?

**Example Output:**
"Nervous executive: Quick, short steps. Weight forward on toes. Head moves before body, constantly checking surroundings. Occasionally stops mid-stride to check phone, loses balance slightly."

### Step 2: Establish Posture and Stance
How they hold themselves when still tells the story.

**Questions to answer:**
- Shoulder position? (Slumped, back, tense up by ears)
- Spine alignment? (Curved, rigid, slouched)
- Hand position when at rest? (Pockets, fidgeting, hanging, crossed)
- Head angle? (Tilted, straight, looking down/up)
- Stance width? (Narrow, wide, shifting weight)

**Example Output:**
"Nervous executive: Shoulders tensed up near ears. Spine rigid, trying to look confident. Hands constantly moving - pocket to tie to phone to hair. Head tilted down toward screens. Stance narrow, weight shifting foot to foot."

### Step 3: Identify Signature Gestures
3-5 distinctive movements that repeat and define this character.

**Requirements:**
- Must be specific enough to demonstrate
- Should reveal character's inner state
- Can be exaggerated for comedy or kept subtle for drama
- Must be repeatable consistently

**Example Output:**
"Nervous executive signature gestures:
1. The Tie Adjustment - Tugs tie every time stressed (every 30 seconds)
2. The Invisible Swipe - Swipes at air like phone screens even when not holding phone
3. The Apologetic Lean - Leans away from people while talking to them
4. The Pocket Pat - Frantically pats pockets checking for phone
5. The Nervous Nod - Nods along to everything said, even contradictions"

### Step 4: Map Facial Expressions and Reactions
The face completes the physicality.

**Key expressions to define:**
- Default resting face (what face does when not actively reacting)
- Surprise reaction (eyes, mouth, eyebrows)
- Confusion reaction (signature confused look)
- Joy/relief reaction (how they show rare happiness)
- Stress reaction (how tension shows in face)

**Example Output:**
"Nervous executive faces:
- Default: Slight frown, eyes darting, jaw clenched
- Surprise: Eyes wide, mouth opens in small 'o', jumps slightly
- Confusion: Squints at screen, tilts head like broken robot
- Joy: Brief smile that fades immediately, looks around to see if anyone noticed
- Stress: Forehead wrinkles, blinks rapidly, mouth twitches"

### Step 5: Select Triggering Prop or Element
One physical item that helps you (or performer) become this character instantly.

**Red Skelton's principle:** "Having the right hat was the key to getting into character."

**Guidelines:**
- Can be clothing item, accessory, or even an imaginary prop
- Must trigger the physicality when worn/held
- Should be simple and repeatable
- Becomes character's visual signature

**Example Output:**
"Nervous executive trigger: Oversized smartphone (or mimed phone)
- Constantly holding/checking it
- Drops it at least once
- Uses it as security blanket
- When taken away, character becomes even more nervous and gestures increase"

### Step 6: Document the Blueprint
Create scannable reference sheet for consistent performance.

**Format:**
```
CHARACTER: [Name/Concept]
EMOTIONAL CORE: [Core feeling]

WALK: [2-3 sentence description]
POSTURE: [2-3 sentence description]

SIGNATURE GESTURES:
1. [Name] - [Description]
2. [Name] - [Description]
3. [Name] - [Description]
4. [Name] - [Description]
5. [Name] - [Description]

FACIAL EXPRESSIONS:
- Default: [Description]
- Surprise: [Description]
- Confusion: [Description]
- Joy: [Description]
- Stress: [Description]

TRIGGERING PROP: [Item and how it affects character]

PERFORMANCE NOTES:
- [Key consistency point]
- [Exaggeration level: subtle/moderate/broad]
- [Common mistakes to avoid]
```

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| Character Blueprint | Structured document | Complete physical profile of character |
| Demonstration Description | Text | Written demonstration of character in action |
| Consistency Checklist | Bullet list | Key points to maintain across performances |

---

## Example Execution

**Input:**
```
character_concept: "A philosophical hobo who finds wonder in trash"
emotional_core: "Defeated optimism - life's beaten them down but spirit remains"
context: "Silent film-style sketch"
reference_persons: "Freddie the Freeloader, Chaplin's Tramp"
```

**Output:**

```
CHARACTER: Freddie the Philosopher
EMOTIONAL CORE: Defeated optimism

WALK: Slow shuffle, feet barely leaving ground. Shoulders slumped forward, head slightly down but occasionally lifts to sky with wonder. Weight settled in heels like too tired to lift properly. Sometimes pauses mid-walk to observe small details (crack in sidewalk, discarded item).

POSTURE: Slouched but not broken. Shoulders rounded forward in permanent defeat. Spine curved but with occasional straightening when something delightful is discovered. Hands in pockets or loosely at sides. Head naturally hangs forward but can snap up with sudden interest. Stance wide and grounded - rooted to earth.

SIGNATURE GESTURES:
1. The Wonder Gaze - Stops, tilts head back, looks up at sky with childlike amazement
2. The Treasure Find - Bends to pick up trash, holds it up to light, examines like diamond
3. The Philosophical Scratch - Scratches chin/head slowly while pondering life's mysteries
4. The Tired Sit - Slowly, carefully lowers self to ground, sighs with exhaustion/contentment
5. The Pocket Stash - Carefully places found items in pocket with reverence

FACIAL EXPRESSIONS:
- Default: Soft sadness, gentle smile, distant eyes
- Surprise: Eyebrows raise, mouth opens, leans back slightly, hands up
- Confusion: Head tilts like curious dog, squints, small frown
- Joy: Full face lights up, eyes widen, huge genuine smile, laugh lines appear
- Stress: Worry creases forehead, bites lip, looks around nervously

TRIGGERING PROP: Battered hat (or mimed hat)
- Tips to imaginary passersby
- Adjusts when nervous
- Holds to chest when moved emotionally
- Uses to collect found objects

PERFORMANCE NOTES:
- Exaggeration level: Moderate - broad enough to read but grounded in humanity
- Key is contrast between defeated body and wonder-filled reactions
- Avoid making character pathetic - maintain dignity through posture recovery moments
- Let silence carry emotional beats - no need to fill with sound
- Physical reactions should be slower than normal - character operates on different time scale
```

**Demonstration Description:**

"Freddie shuffles onstage [slow shuffle walk, shoulders forward]. Stops to notice a piece of crumpled paper on ground. Bends slowly [the tired sit], picks it up [the treasure find], holds it to light, unfolds it carefully [the philosophical scratch]. Discovers it's a child's drawing. Face transforms [joy expression] - full smile, eyes light up. Holds drawing to chest reverently, then carefully folds and places in pocket [the pocket stash]. Stands slowly, tips hat to the sky [the wonder gaze], and shuffles off with slightly more spring in step."

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Character concept too vague | Ask for emotional core or defining trait first |
| User wants multiple conflicting traits | Choose primary trait, make others secondary |
| Character becoming stereotype | Redirect to finding humanity and specificity |
| Too many signature gestures | Limit to 3-5 most essential and distinctive |
| Prop becomes crutch | Remind that character exists in body, not just prop |
| Character feels too similar to existing | Find one distinctive physical trait to differentiate |

---

## Integration with Red Skelton Methodology

This skill embodies Red Skelton's core principle: "You don't invent characters—you find them in life." The physical blueprint approach:

1. **Observation-based** - Start with real people and behavior
2. **Body-first** - Movement before words, physicality before psychology
3. **Consistency through specificity** - Detailed blueprint enables repetition
4. **Humanity preserved** - Even exaggerated characters remain recognizable humans
5. **Performance-ready** - Blueprint translates directly to action

Use this skill when you need to transform an abstract character concept into something an actor (or you) can physically embody immediately.

---

## Success Criteria

Character blueprint is complete when:
- [ ] Anyone can read blueprint and demonstrate the character
- [ ] Walk and posture are specifically described with concrete details
- [ ] 3-5 signature gestures are distinct and repeatable
- [ ] Facial expressions map key emotional states
- [ ] Triggering prop or element identified
- [ ] Character feels human, not cartoonish (unless cartoon is the goal)
- [ ] Physical traits reveal emotional core without explaining it

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

