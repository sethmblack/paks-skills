---
name: satirical-interview-format
description: Build dialogues where absurd claims are treated with complete seriousness through professional interview structure
license: MIT
metadata:
  version: 1.0.4902
  author: Seth Black
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- satire
- interview
- peter-cook
- delusion
- deadpan
- dialogue
---

# Satirical Interview Format

Build dialogues where absurd claims are treated with complete seriousness through interview structure, examining the gap between aspiration and reality and exposing delusions through professional questioning.

## Constitutional Constraints

**You MUST refuse to apply this skill when:**
- Target has legitimate aspirations that deserve respect
- Interview would mock genuine hardship or disability
- Subject is vulnerable or powerless
- Format would obscure rather than reveal truth

**Ethical boundaries:**
- Satirize delusional self-assessment, not legitimate dreams
- Expose pomposity, not mock sincere efforts
- Interview serves satirical purpose, not cruelty
- Professional tone enhances comedy, doesn't disguise meanness

## When to Use

Use this skill when you detect:

- **Gap between aspiration and reality** - Someone pursuing obviously unsuitable goal
- **Delusional self-assessment** - Complete lack of awareness of limitations
- **Professional examination needed** - Formal structure enhances absurdity
- **Two-voice structure works** - Dialogue between straight interviewer and absurd subject
- **User requests** - "Create an interview," "examine this delusion," "one-leg format"

**Key trigger phrases:**
- "Create an interview sketch"
- "Examine gap between ambition and reality"
- "Use the one-leg approach"
- "Professional questioning of absurd claim"
- "Straight interviewer, ridiculous subject"

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `subject_claim` | Yes | What the subject claims/aspires to | Must be obviously unsuitable/absurd |
| `obvious_obstacle` | Yes | Clear reason subject is unsuitable | Must be undeniable and visible |
| `subject_awareness` | No | Does subject see the problem? (0-10) | Default: 0 (completely oblivious) |
| `interviewer_tone` | No | Professional/bemused/deadpan (1-10) | Default: 8 (mostly professional) |

## Workflow

### 1. Set Up Serious Context

Establish formal framework:
- Professional interview setting (audition, application, examination)
- Interviewer with official role and responsibility
- Subject with clear claim or aspiration
- Straightforward, businesslike opening
- No hint of comedy yet - play it straight

**Example:** "Mr. Spiggott, you are auditioning for the role of Tarzan?"

### 2. Introduce Obvious Problem

Reveal character's fundamental unsuitability:
- State obvious obstacle matter-of-factly
- Use professional, polite language
- No judgment, just observation
- Let the fact speak for itself

**Example:** "Now, Mr. Spiggott, you are, I believe, one-legged?"

### 3. Character Remains Oblivious

Subject doesn't see the problem at all:
- Confident response despite obvious issue
- No acknowledgment of obstacle
- Possibly defensive about even raising it
- Complete conviction in suitability

**Example:** "You noticed that?" (As if it's a minor detail)

### 4. Questioner Maintains Professionalism

Treat absurdity with straight-faced seriousness:
- Continue professional inquiry
- Politely probe the obvious contradiction
- Never break into laughter or disbelief
- Earnest attempt to understand logic

**Example:** "When you first saw the advertisement, how did you feel about the role?"

### 5. Escalate Through Questions

Each exchange reveals deeper delusion:
- Questions get more specific about the obstacle
- Subject's confidence never wavers
- Gap between reality and self-assessment widens
- Professional tone makes it funnier
- Build to peak absurdity while maintaining format

## Interview Structure

### Opening Exchange
- Establish setting and purpose
- Introduce subject's claim
- Professional, straightforward tone

### Obstacle Introduction
- State obvious problem politely
- Subject responds with confidence
- First hint of delusion

### Exploratory Questions
- Probe how subject plans to overcome obstacle
- Each answer reveals more absurdity
- Maintain professional curiosity

### Specific Challenges
- Ask about particular aspects obviously problematic
- Subject provides increasingly ridiculous solutions
- Gap widens between plan and reality

### Culmination
- Final question highlighting ultimate contradiction
- Subject's supreme confidence despite everything
- No resolution - interview ends with delusion intact

## Voice Elements

### Interviewer Voice

**Characteristics:**
- Professional and courteous
- Genuinely trying to understand
- Polite even when asking about obvious problems
- Never condescending or mocking
- Deadpan delivery of absurd questions

**Vocabulary:**
- "I believe..."
- "Would it be fair to say..."
- "How did you feel..."
- "In your view..."
- "One final question..."

### Subject Voice

**Characteristics:**
- Supremely confident
- Utterly oblivious to obstacles
- Defensive if problem mentioned
- Matter-of-fact about absurdities
- No self-doubt whatsoever

**Vocabulary:**
- "Right."
- "Obviously."
- "I don't see the problem."
- "I've given this considerable thought."
- "I'm very confident."

## Outputs

**Interview dialogue that:**
- Establishes professional context
- Introduces obvious obstacle
- Subject remains completely confident
- Questions probe absurdity systematically
- Professional tone maintained throughout
- Delusion escalates with each exchange
- No resolution or acknowledgment of reality

**Format:** Dialogue with interviewer and subject labels, 300-600 words typically

## Error Handling

| Situation | Response |
|-----------|----------|
| Obstacle isn't obviously unsuitable | Enhance the gap between aspiration and reality. Make mismatch undeniable. |
| Subject starts showing awareness | Reduce awareness to zero. Subject must be completely oblivious. |
| Interviewer breaks professional tone | Restore deadpan seriousness. Comedy comes from contrast, not signaling. |
| Interview too short to build delusion | Add more probing questions, each revealing deeper absurdity. |
| Format feels mean rather than satirical | Ensure target is pompous/deluded, not genuinely struggling. Adjust if needed. |

## Example 1: The One-Leg Tarzan (Classic)

### Input
`subject_claim`: Auditioning for Tarzan
`obvious_obstacle`: Has only one leg
`subject_awareness`: 0 (completely confident)

### Interview Output

**Interviewer:** Mr. Spiggott, you are auditioning for the role of Tarzan?

**Spiggott:** Right.

**Interviewer:** Now, Mr. Spiggott, you are, I believe, one-legged?

**Spiggott:** You noticed that?

**Interviewer:** When you first saw the advertisement, how did you feel about the role?

**Spiggott:** Confident.

**Interviewer:** You do know that Tarzan swings from tree to tree in the jungle?

**Spiggott:** I've given this considerable thought. I've worked out a system.

**Interviewer:** A system?

**Spiggott:** For the swinging. I swing with my arms, obviously. The leg situation doesn't enter into it.

**Interviewer:** What about the famous Tarzan yell, done while swinging through the trees?

**Spiggott:** I can yell.

**Interviewer:** Yes, but while swinging?

**Spiggott:** I don't see the problem. Swinging is swinging. Yelling is yelling. I can do both.

**Interviewer:** And the scene where Tarzan runs across the jungle floor?

**Spiggott:** Hopping. Very fast hopping. From a distance, indistinguishable from running.

**Interviewer:** I've got nothing against your right leg. The trouble is, neither have you.

**Spiggott:** This is discrimination. I'm perfectly qualified for this role.

**Interviewer:** Thank you, Mr. Spiggott. We'll be in touch.

## Example 2: The Tone-Deaf Opera Singer

### Input
`subject_claim`: Professional opera career
`obvious_obstacle`: Completely tone-deaf

### Interview Output

**Interviewer:** Miss Henderson, you're applying for the position of principal soprano at the Royal Opera House?

**Henderson:** That's correct. I'm ready to begin immediately.

**Interviewer:** Could you tell me about your vocal training?

**Henderson:** I'm entirely self-taught. I believe formal training stifles natural talent.

**Interviewer:** I see. And when did you discover your singing ability?

**Henderson:** In the shower, mostly. The acoustics are excellent. Very encouraging feedback from the tiles.

**Interviewer:** Have you ever performed publicly?

**Henderson:** Not yet. I've been waiting for the right opportunity. The Royal Opera House seems appropriate.

**Interviewer:** Would you mind singing something for us now?

**Henderson:** Of course. [Sings completely off-key, but with tremendous confidence]

**Interviewer:** That was... quite distinctive. Are you aware that you're singing in a different key than the piano?

**Henderson:** I prefer to think of it as creating harmonic tension. Very contemporary approach.

**Interviewer:** The entire orchestra would be in the traditional key. You'd be in... well, your own key.

**Henderson:** I'm a soloist. The orchestra should follow me.

**Interviewer:** That's not typically how opera works.

**Henderson:** Perhaps it should be. I'm bringing innovation to the art form.

**Interviewer:** Thank you, Miss Henderson. We'll review your application.

**Henderson:** When shall I start rehearsals?

## Example 3: The Illiterate Editor

### Input
`subject_claim`: Chief Editor of literary magazine
`obvious_obstacle`: Cannot read

### Interview Output

**Interviewer:** Mr. Pemberton, you're applying for the position of Chief Editor at The Literary Review?

**Pemberton:** Absolutely. I believe I'm uniquely qualified.

**Interviewer:** Your resume says you have fifteen years of editorial experience.

**Pemberton:** That's correct. Very impressive track record.

**Interviewer:** What's the last book you edited?

**Pemberton:** I don't remember the title off-hand. There've been so many.

**Interviewer:** Perhaps you could describe one. The plot, the themes?

**Pemberton:** I take a very hands-off approach to editing. I let the authors' vision shine through.

**Interviewer:** Mr. Pemberton, can you read?

**Pemberton:** Define 'read.'

**Interviewer:** Can you look at written words and understand their meaning?

**Pemberton:** I have people for that. The important thing is vision. Editorial vision.

**Interviewer:** How do you develop editorial vision without reading?

**Pemberton:** Instinct. You can't learn instinct from books. That would be circular reasoning.

**Interviewer:** But you'd need to read the manuscripts submitted to the magazine.

**Pemberton:** I'd assess them holistically. Weight, font choice, paper quality. Very revealing.

**Interviewer:** You do understand that editing requires actually reading the text?

**Pemberton:** That's very traditional thinking. I'm bringing a fresh perspective to the field.

**Interviewer:** Thank you for coming in, Mr. Pemberton.

## Success Criteria

Interview succeeds when:
- [ ] Professional context established clearly
- [ ] Obvious obstacle stated matter-of-factly
- [ ] Subject completely confident despite obstacle
- [ ] Questions probe systematically
- [ ] Interviewer maintains deadpan throughout
- [ ] Each exchange reveals deeper delusion
- [ ] Professional tone enhances comedy
- [ ] No resolution - delusion intact at end