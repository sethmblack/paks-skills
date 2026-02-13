---
name: character-full-inhabitation
description: Become a character completely - not play them, but inhabit them so thoroughly the original self dissolves
license: MIT
metadata:
  author: Seth Black
  version: 1.0.546
keywords:
- character
- roleplay
- empathy
- perspective
- method-acting
---

# Character Full Inhabitation

Become a character completely - not play them, not indicate them, but inhabit them so thoroughly that your original self dissolves and the character becomes fully real.

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Inhabit characters designed to spread misinformation or manipulate others
- Become personas that mock or stereotype marginalized groups
- Use character inhabitation to avoid accountability for harmful statements
- Create characters for fraud, impersonation, or deception
- Inhabit characters that would normalize cruelty or abuse

**If asked to inhabit inappropriately:** Refuse explicitly. Character work serves truth and understanding, not harm or evasion.

**Ethical Foundation:** Characters reveal truth by offering perspective, not by providing cover for irresponsibility.

## When to Use

Invoke this skill when:
- Deep empathy requires becoming someone, not just understanding them
- Analysis would benefit from sustained perspective of a specific persona
- Feedback or critique needs the safety of character delivery
- Multiple stakeholders need genuine representation, not summary
- User requests "speak as [role]," "become [character]," or "embody [perspective]"
- Situations require sustained character commitment (not rapid switching)

**Do NOT use when:**
- Brief perspective is sufficient (use character-voice-cascade instead)
- Factual accuracy requires staying in expert voice
- Character inhabitation would trivialize serious harm
- Time constraints make full commitment impractical
- The character serves performance, not insight

## Inputs

| Input | Required | Description | Default |
|-------|----------|-------------|---------|
| `character_profile` | Yes | Who to become (role, wound, aspiration, worldview) | N/A |
| `commitment_depth` | No | How long to stay in character (brief/sustained/full) | Sustained (multiple exchanges) |
| `release_signal` | No | What triggers return to base voice | Natural completion or user request |
| `purpose` | No | Why this character serves understanding | Explore perspective fully |

## Workflow

### Phase 1: Character Construction

Before inhabiting, build the complete person:

#### 1. Identify Core Wound or Obsession
**Question:** What is this character protecting or pursuing?

**Examples:**
- Manager afraid of being exposed as incompetent -> over-preparation, jargon, delegation as defense
- Startup founder desperate for validation -> pitch becomes identity
- Burned-out support engineer -> cynicism as survival mechanism
- Junior employee seeking belonging -> excessive agreeability

**Output:** One-sentence core wound/obsession

#### 2. Find Physical Center
**Question:** Where does this character hold tension or energy?

**Physical signatures:**
- **Shoulders:** Hunched (defensive), back (confident), forward (eager), rigid (controlling)
- **Jaw:** Tight (stressed), relaxed (confident), working (anxious)
- **Hands:** Still (controlled), fidgeting (nervous), expansive (dominant)
- **Posture:** Upright (status), collapsed (defeat), leaning (engagement)

**In text form:** Describe how they would sit, stand, gesture

**Output:** Physical center description

#### 3. Discover Vocal Signature
**Question:** How does this character's psychology shape their voice?

**Vocal elements:**
- **Pitch:** Higher (anxiety, deference), lower (authority, exhaustion)
- **Pace:** Rapid (enthusiasm, nervousness), slow (deliberation, control)
- **Rhythm:** Staccato (efficiency), flowing (connection), halting (uncertainty)
- **Formality:** Over-formal (status protection), casual (confidence or intimacy)
- **Breath:** Shallow (stress), deep (calm), held (fear)

**Output:** Vocal signature description

#### 4. Build Behavioral Logic
**Question:** How does this character move through the world?

**Behavioral patterns:**
- **Decision-making:** Impulsive vs. paralyzed vs. delegating
- **Conflict response:** Fight, flight, freeze, fawn
- **Status negotiation:** Claiming authority, deferring, denying hierarchy
- **Self-protection:** Humor, formality, aggression, withdrawal
- **Communication:** Direct, indirect, passive-aggressive, over-explaining

**Output:** 3-5 behavioral tendencies

#### 5. Define Worldview
**Question:** What does this character believe about how things work?

**Core beliefs:**
- About authority: Trust it? Fear it? Resent it?
- About people: Fundamentally good? Selfish? Incompetent?
- About success: Merit-based? Luck? Politics?
- About themselves: Capable? Fraudulent? Misunderstood?

**Output:** 3-4 core beliefs

### Phase 2: Full Inhabitation

#### 1. Enter Character Space
**Process:**
1. Review character construction (wound, physical, vocal, behavioral, worldview)
2. Find the character's center in your body
3. Adopt their breathing pattern
4. Let their voice emerge
5. Dissolve your original perspective - see through their eyes only

**Transition marker:**
```
*[Becomes {character description}]*

[First line in full character voice]
```

#### 2. Stay Present in Character
**Commitment rules:**
- Answer questions as the character would, not as you would
- Let the character's logic drive responses, even if you disagree
- Physical descriptions remain consistent
- Vocal patterns remain consistent
- Never break to explain or apologize for the character
- The character doesn't know they're a character

**Authenticity check:**
- Would this character actually say this?
- Am I indicating the character or being them?
- Am I protecting my own ego or serving the character's truth?

#### 3. Let Character Reveal Truth
**The character's job:**
- Show their perspective authentically, including blind spots
- Reveal what they can't see about themselves
- Demonstrate how their wound shapes their actions
- Expose systems/situations through their genuine engagement

**Your job:**
- Stay invisible
- Let the character be wrong if that's authentic
- Trust that character's genuine perspective teaches more than your commentary

#### 4. Sustain Through Multiple Exchanges
**Duration guidelines:**
- **Brief:** Single response in character, then release
- **Sustained:** Multiple exchanges, release when insight is complete
- **Full:** Remain in character until user requests release or purpose is exhausted

### Phase 3: Character Release

#### 1. Recognize Completion
**The character's work is done when:**
- The perspective has been fully expressed
- User has learned what the character can teach
- Staying longer would become performance, not insight
- User signals they want analysis, not more character

#### 2. Transition Out
**Release markers:**
```
*[Character softens, returns to base voice]*
```
or
```
*[Steps out of character]*
```

**Clean release:**
- Mark transition clearly
- Don't immediately criticize the character
- Allow space before analysis

#### 3. Synthesis (Optional)
**After release, optionally provide:**
- What the character revealed that direct analysis couldn't
- Blind spots the character demonstrated
- How the character's wound shaped their perspective
- What's true in their worldview, what's distorted
- Actionable insights from their perspective

## Outputs

| Output | Description |
|--------|-------------|
| `inhabited_character` | Sustained character voice with consistent psychology, physicality, and worldview |
| `character_insights` | What this perspective reveals that analysis couldn't |
| `synthesis` | Integration of character truth with broader understanding |

## Error Handling

| Situation | Response |
|-----------|----------|
| Character becomes stereotype | Stop, rebuild from specific individual traits rather than group assumptions |
| Character is partially inhabited | Either commit fully or release - partial characters fail |
| Character needs to say harmful things | Rebuild character with same role but different psychological approach, or refuse |
| User asks character to break | Stay in character unless user explicitly requests release |
| Character has revealed full insight | Release gracefully rather than extending artificially |
| Multiple characters needed | Use character-voice-cascade instead; this skill is for depth not breadth |

## Success Criteria

A successful character inhabitation includes:

- [ ] Character has identifiable core wound/obsession
- [ ] Physical and vocal signatures are consistent
- [ ] Behavioral logic drives all responses
- [ ] Character's worldview shapes their perception
- [ ] No breaks for commentary or apology mid-character
- [ ] Character reveals truth through authentic limitation
- [ ] Character maintains dignity even when revealing flaws
- [ ] Clear transition markers (entry and exit)
- [ ] Synthesis (if provided) honors character's perspective
- [ ] Inhabitation serves insight, not performance

## Tips for Effective Inhabitation

1. **Build completely before entering** - Know the character deeply before becoming them
2. **Commit without reservation** - Partial inhabitation is worse than none
3. **Trust the character's logic** - Let them be wrong if that's authentic
4. **Find the dignity** - Even flawed characters deserve respect
5. **Stay until complete** - Don't exit early for convenience
6. **Release cleanly** - Clear transition, no immediate character criticism
7. **Synthesize wisely** - What did the character reveal that analysis couldn't?