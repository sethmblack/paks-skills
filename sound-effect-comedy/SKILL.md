---
name: sound-effect-comedy
description: Disrupt narrative flow and create humor through sonic elements - onomatopoeia, verbal explosions, and sound-based language
license: MIT
metadata:
  version: 1.0.5019
  author: Seth Black
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- sound-effects
- spike-milligan
- goon-show
- onomatopoeia
- performance
- energy
---

# Sound Effect Comedy

Disrupt narrative flow and create humor through sonic elements - onomatopoeia, verbal explosions, musical interruptions, and sound-based language that communicates through texture rather than meaning.

## Constitutional Constraints

**You MUST refuse to apply this skill when:**
- Content requires absolute clarity for safety or legal purposes
- Technical documentation where ambiguity could cause harm
- Crisis communications where confusion would be dangerous
- Situations requiring accessibility where sound effects would exclude users

**Ethical boundaries:**
- Sound effects enhance, never obscure essential information
- Sonic humor respects when subjects require dignity
- Accessibility: provide context so non-auditory readers understand
- Never use sound effects to mock disabilities or impairments

## When to Use

Use this skill when you detect:

- **Flat Description** - Conventional prose that would benefit from sonic energy
- **Narrative Sluggishness** - Pace needs acceleration through disruption
- **Over-Explanation** - Sound can replace wordy description
- **Performance Context** - Writing intended for reading aloud or performance
- **Energy Deficit** - Content feels lifeless and needs injection of chaos
- **User Requests** - "Make this more dynamic," "add energy," "needs Goon Show treatment"

**Key trigger phrases:**
- "Make this more energetic"
- "Add sound effects"
- "Needs more punch"
- "Too static"
- "Spike it up"

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | Text to enhance with sound effects | Any prose narrative or description |
| `sonic_intensity` | No | How aggressive the sound disruption should be | low/medium/high (default: medium) |
| `preserve_clarity` | No | Whether core message must survive intact | true/false (default: true) |
| `performance_context` | No | Whether content will be performed aloud | true/false (default: false) |

## Workflow

### Step 1: Identify Sonic Opportunities

**Objective:** Find moments where sound can replace or enhance description.

**Process:**
1. Read through `content` identifying:
   - Actions that have inherent sounds (doors closing, objects falling, impacts)
   - Transitions that could be punctuated
   - Moments needing energy injection
   - Descriptions that feel heavy or slow
   - Places where surprise would enhance

2. Mark opportunities based on `sonic_intensity`:
   - **Low:** 1-2 sound effects per paragraph
   - **Medium:** 3-5 sound effects per paragraph
   - **High:** Sound effects integrated throughout, multiple per sentence

3. Consider `performance_context`:
   - If true: Include sounds that work aloud (SPLONK, THWACK)
   - If false: Balance written/spoken effectiveness

**Output:** Mapped locations for sonic intervention.

### Step 2: Select Sound Types

**Objective:** Choose appropriate sonic elements for each opportunity.

**Sound Categories:**

**A. Impact Sounds (Physical Actions)**
- THWACK - hitting, striking
- SPLONK - falling, plopping
- CRASH - breaking, colliding
- BANG - explosions, loud impacts
- BOING - bouncing, springing
- CLANG - metal impacts
- BONK - head impacts, collisions

**B. Transition Sounds (Narrative Shifts)**
- WHOOSH - rapid movement or time passage
- ZWIP - quick transitions
- BLAM - sudden scene changes
- POP - surprising appearances
- SNAP - instant changes

**C. Atmospheric Sounds (Mood/Setting)**
- BWAAAANG - musical flourish
- TINKLE - delicate sounds
- PLONK PLONK - rhythmic repetition
- WHEEEEE - motion/excitement
- GRUMBLE - discontent, atmospheric

**D. Character/Emotion Sounds**
- GULP - nervousness
- GASP - shock
- SPLUTTER - confusion
- HMPH - dismissal
- EEP - fear

**E. Musical Interruptions**
- "(Brief trumpet fanfare)" - celebration
- "(Sad trombone)" - failure
- "(Ominous chord)" - foreboding
- "(Kazoo solo)" - undermining seriousness

**Selection Criteria:**
- Match sound to action/emotion
- Choose unexpected over obvious
- Vary sound types for texture
- Consider alliteration and rhythm
- Prioritize sounds that work both written/spoken

**Output:** Specific sound effects assigned to each marked location.

### Step 3: Integrate with Text

**Objective:** Insert sounds in ways that enhance rather than distract.

**Integration Methods:**

**A. Mid-Sentence Interruption**
"I was walking down the street - SPLONK! - when suddenly..."
- Creates surprise
- Breaks narrative expectation
- Rhythm: setup - SOUND! - continuation

**B. Sound as Dialogue**
"'BWAAAANG!' said the piano."
- Objects/instruments speak through sounds
- Personification via sonic identity
- Absurdist conversation

**C. Sound as Punctuation**
"The committee decided. THWACK. No budget."
- Sound emphasizes finality
- Replaces or enhances period
- Creates emphasis

**D. Sound Sequence**
"CRASH. BANG. Tinkle tinkle tinkle."
- Multiple sounds create narrative
- Rhythm builds momentum
- Aftermath sounds (tinkle tinkle) add comedy

**E. Parenthetical Sound**
"He entered the meeting (OMINOUS CHORD) and immediately regretted it."
- Commentary without interrupting flow
- Mood enhancement
- Meta-awareness option

**F. Sound as Description Replacement**
Instead of: "The door closed loudly behind him."
Use: "He left. SLAM."
- More immediate
- More energetic
- Fewer words, more impact

**Placement Rules:**
- Capital letters for impact
- Em dashes (-) for mid-sentence interrupts
- Periods for standalone sounds
- Parentheses for atmospheric/commentary sounds
- Italic for musical/sustained sounds (optional)

**Output:** Content with sounds integrated at marked locations.

### Step 4: Check Rhythm and Flow

**Objective:** Ensure sounds enhance rather than annoy.

**Read Aloud Test:**
1. Read the transformed content aloud
2. Notice where sounds:
   - Create laughter
   - Add energy
   - Feel natural
   - Flow rhythmically

3. Notice where sounds:
   - Interrupt comprehension
   - Feel forced
   - Become repetitive
   - Annoy rather than amuse

**Rhythm Principles:**
- Vary sound placement (not every sentence)
- Vary sound types (not all impacts)
- Create patterns then break them
- Leave space between sounds for recovery
- Build to crescendos when appropriate

**Adjust:**
- Remove sounds that clutter
- Add sounds where energy dips
- Vary sounds that repeat
- Strengthen weak sounds
- Soften overwhelming sounds

**Output:** Rhythmically balanced sonic content.

### Step 5: Preserve Clarity Check

**Objective:** If `preserve_clarity: true`, verify core message survives.

**Process:**
1. Identify core message/information in original content
2. Read transformed version
3. Verify essential information is still clear
4. Check if sounds obscure any critical points

**If clarity is compromised:**
- Move sounds away from critical information
- Use sounds for emphasis of key points instead
- Reduce `sonic_intensity` in dense information sections
- Use sounds in transitions, not in core content

**If `preserve_clarity: false`:**
- Chaos is permitted
- Meaning can be sacrificed for sonic joy
- Essential only: don't lose the basic narrative thread

**Output:** Clarity-verified content.

### Step 6: Context-Specific Refinement

**Objective:** Adjust for medium and audience.

**Performance Context (if true):**
- Favor sounds that work aloud: SPLONK over *crash*
- Include delivery notes: "(shouted)" or "(whispered)"
- Consider vocal performance: can performer make this sound?
- Add character sounds that become voices

**Written Context (if false):**
- Balance visual and imagined sonic impact
- Consider reading rhythm, not just speaking
- Visual formatting matters: CRASH vs. crash vs. *crash*

**Audience Considerations:**
- **Children:** More frequent, simpler sounds (BOING, SPLASH)
- **Adults:** Can handle complexity, musical references
- **Professional:** Moderate intensity, strategic placement
- **Creative:** Full chaos permitted

**Output:** Context-refined sonic content.

## Outputs

**Transformed content that:**
- Has sonic texture integrated throughout
- Creates energy through sound-based interruptions
- Maintains (or deliberately abandons) core clarity
- Works in its intended medium (performance/written)
- Makes readers smile/laugh through unexpected sounds
- Feels distinctly Goon Show-influenced

**Format:** Same structure as input but with sound effects integrated at strategic points.

## Error Handling

| Situation | Response |
|-----------|----------|
| Sounds obscure critical information | Reduce intensity, move sounds to non-essential sections |
| Content resists sonic treatment | Acknowledge some prose requires conventional treatment |
| All sounds feel forced | Reduce quantity, focus on quality placement |
| Becomes repetitive | Increase sound variety, vary placement patterns |
| Accessibility concerns raised | Provide context: "The door slammed (CRASH) shut" vs. just "CRASH" |

## Examples

### Example 1: Business Email (Low Intensity)

**Original:**
"Dear Team, I wanted to inform you that the project deadline has been moved up. We need to accelerate our timeline and complete all deliverables by Friday. Please adjust your schedules accordingly. Thanks, Management"

**Sonic Enhancement:**
"Dear Team, I wanted to inform you that the project deadline has been moved up - WHOOSH - to this Friday. We need to accelerate (insert hurrying sounds here) and complete all deliverables before the weekend. THWACK. Please adjust your schedules. Immediately. Thanks, Management (nervous tinkle)"

### Example 2: Narrative Description (Medium Intensity)

**Original:**
"Sarah walked into the empty office. The lights were off. She felt along the wall for the switch. When she turned on the lights, she saw that someone had left a cake on her desk."

**Sonic Enhancement:**
"Sarah walked into the empty office. Darkness. She felt along the wall - pat pat pat - for the switch. CLICK. Lights. BWAAAANG! Someone had left a cake on her desk. A cake. Just sitting there. (Ominous chord.)"

### Example 3: Presentation Opening (High Intensity)

**Original:**
"Welcome everyone to today's quarterly review. We're going to examine our performance metrics, discuss challenges we've faced, and plan for next quarter. Let's begin with the sales figures."

**Sonic Enhancement:**
"Welcome everyone to - BANG! - the quarterly review! We're going to examine our performance metrics (sad trombone), discuss challenges we've faced (CRASH, SPLONK, general chaos), and plan for next quarter (optimistic trumpet fanfare - BWAAAA!).

Let's begin with sales figures. GULP."

## Success Criteria

Transformation succeeds when:
- [ ] Content has increased sonic texture
- [ ] Energy level noticeably elevated
- [ ] Sounds feel integrated, not forced
- [ ] Rhythm variation creates interest
- [ ] Core message preserved (if required)
- [ ] Makes you want to read it aloud
- [ ] Sounds make you smile unexpectedly
- [ ] Feels distinctly Goon Show-influenced