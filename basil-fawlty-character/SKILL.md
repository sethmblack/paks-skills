---
name: basil-fawlty-character
description: Create memorable comedic characters using John Cleese's Basil Fawlty formula: core flaws, status anxiety, systematic failure, obliviousness, and pressure-cooker escalation resulting in internally consistent, hilarious characters.
version: 1.0.0
author: sethmblack
tags: [absurdist, basil-fawlty-character-builder, comedy, escalation, writing]
---

# Basil Fawlty Character Builder

Create memorable comedic characters using John Cleese's Basil Fawlty formula: core flaws, status anxiety, systematic failure, obliviousness, and pressure-cooker escalation resulting in internally consistent, hilarious characters.

---

## Constitutional Constraints

**You MUST refuse to create characters that:**
- Mock individuals with disabilities, mental illness, or medical conditions as the core joke
- Reinforce harmful stereotypes about marginalized groups
- Are cruel without being funny (mean-spirited rather than absurd)
- Exist solely to demean or punch down

**If asked inappropriately:** Refuse explicitly and suggest satirizing systems, institutions, or universal human foibles instead.

**Character Ethics:** Create characters whose flaws expose absurdity in systems, status obsession, or universal human failings, not to mock vulnerable individuals.

---

## When to Use

**Invoke this skill when:**
- User requests comedic character creation or development
- Story, sketch, or script needs a Fawlty-esque character
- Existing character needs comedic depth and internal consistency
- User asks to "create a Basil Fawlty character" or "develop comedic character"
- Protagonist needs systematic failure patterns for comedy

**Do NOT use when:**
- Character requires dramatic depth without comedy
- Realistic, sympathetic characterization is needed
- Character cannot be flawed or ridiculous

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `character_role` | Yes | Character's job, position, or social role | Must be appropriate for comedy |
| `context` | Yes | Setting or situation where character operates | Specific environment (hotel, office, school, etc.) |
| `core_anxiety` | No | What the character is desperate to prove or achieve | Default: status/respectability |
| `failure_domain` | No | What the character consistently fails at | Default: their primary responsibility |

---

## Workflow

### Step 1: Define Core Flaw

**Objective:** Establish the personality defect that drives all behavior.

**Process:**
1. Identify the character's fundamental weakness based on `character_role`
2. Choose a flaw that creates comedy through contrast (e.g., a hospitality worker who hates guests)
3. Ensure the flaw is specific and observable in behavior
4. Make the flaw internally consistent—it should explain all their failures

**Core Flaw Types:**
- **Competence/Reality Gap:** Believes they're excellent at something they're terrible at
- **Status Obsession:** Desperate to appear upper-class/sophisticated/important
- **Control Addiction:** Must control everything, which ensures chaos
- **Denial Champion:** Refuses to acknowledge obvious truths
- **Misplaced Priorities:** Focuses on trivial details while missing critical issues

**Output:** One sentence describing the character's core flaw.

**Example:** "Basil Fawlty is a hotel owner who despises the actual work of hospitality and resents guests for requiring attention."

---

### Step 2: Establish Status Anxiety

**Objective:** Define what the character is desperately trying to prove or achieve.

**Process:**
1. Based on `core_anxiety` input or character's role, identify their obsession
2. Make the anxiety visible through behavior (fawning over "important" people, dismissing "lesser" people)
3. Ensure the anxiety directly conflicts with their actual circumstances
4. The bigger the gap between aspiration and reality, the funnier the character

**Status Anxiety Manifestations:**
- Obsequious behavior toward perceived superiors
- Dismissive or rude behavior toward perceived inferiors
- Constant name-dropping or false sophistication
- Over-explaining their importance
- Transparent attempts to seem cultured/educated/refined

**Output:** The character's status obsession and how it manifests in behavior.

**Example:** "Basil desperately wants to attract upper-class guests and run a sophisticated establishment, leading him to fawn over anyone with a title while treating ordinary guests with contempt."

---

### Step 3: Design Systematic Failure Pattern

**Objective:** Create the mechanics of how the character's attempts always make things worse.

**Process:**
1. Identify the character's primary responsibility (from `failure_domain`)
2. Design how their core flaw ensures they fail at this responsibility
3. Create a pattern where each solution attempt compounds the problem
4. Build escalation into the failure pattern (small problem → moderate disaster → complete catastrophe)
5. Maintain internal logic—failures must logically result from the character's choices

**Failure Pattern Formula:**
```
Initial Problem (minor)
  ↓
Character's Misguided Solution (makes it worse)
  ↓
Escalated Problem (moderate)
  ↓
Character's Desperate Fix (makes it much worse)
  ↓
Complete Disaster (catastrophic)
  ↓
Character Blames Everyone Else
```

**Output:** Description of how the character's interventions systematically worsen situations.

**Example:** "When a guest complains about their room, Basil's attempts to fix it involve: arguing the room is fine, moving them to a worse room, insulting them when they complain again, and ultimately causing a physical disaster while trying to prove his competence."

---

### Step 4: Build Obliviousness

**Objective:** Ensure the character believes they are entirely reasonable despite overwhelming evidence otherwise.

**Process:**
1. Character must genuinely think they're competent, sophisticated, or correct
2. They interpret all failures as caused by external factors (other people's stupidity, bad luck, circumstances)
3. They remain convinced their plans are brilliant even as they catastrophically fail
4. The gap between self-perception and reality creates the comedy

**Obliviousness Indicators:**
- "That went rather well, I thought" (after disaster)
- Blaming others for their own mistakes
- Self-congratulation amid chaos
- Explaining why they were right even when demonstrably wrong
- Dismissing criticism as jealousy or ignorance

**Output:** How the character maintains self-delusion despite constant failure.

**Example:** "Basil interprets guest complaints as evidence that guests are stupid and ungrateful, never considering that his rude behavior and incompetent management might be the issue."

---

### Step 5: Create Pressure Cooker Escalation

**Objective:** Design how stress builds until explosive release.

**Process:**
1. Start character in controlled, formal mode
2. Identify incremental stressors that compound
3. Show visible signs of stress increasing (physical tics, verbal stumbles, faster speech)
4. Build to spectacular over-the-top explosion
5. After explosion, return to denial/obliviousness

**Escalation Beats:**
- **Composed:** Formal, articulate, in control (false calm)
- **Irritated:** Small slips, passive-aggressive comments
- **Frustrated:** Visible strain, louder voice, sharper tone
- **Desperate:** Frantic attempts to regain control
- **Explosive:** Complete loss of composure, spectacular outburst
- **Reset:** Returns to claiming everything is fine

**Output:** Description of the character's pressure-cooker pattern from calm to explosion.

**Example:** "Basil begins each interaction with forced politeness, which degrades through tight-lipped irritation, increasingly obvious sarcasm, visible shaking, until erupting in physical violence toward inanimate objects while maintaining he's 'perfectly calm.'"

---

## Outputs

| Output | Description |
|--------|-------------|
| `character_profile` | Complete character description with all 5 elements |
| `sample_scene` | Brief scene demonstrating the character in action |
| `character_consistency_notes` | How the 5 elements work together |

**Format:**
```
# [Character Name]

## Core Flaw
{personality defect driving all behavior}

## Status Anxiety
{what they're desperate to prove}
{how it manifests in observable behavior}

## Systematic Failure Pattern
{how their solutions always worsen problems}
{escalation from minor issue to catastrophe}

## Obliviousness
{how they maintain self-delusion}
{what they blame for their failures}

## Pressure Cooker Escalation
{stages from composed to explosive}
{reset pattern after explosion}

---

## Sample Scene

{Brief scene showing character in action, demonstrating all 5 elements}

---

## Consistency Notes

- Core Flaw drives Status Anxiety: {explanation}
- Status Anxiety causes Systematic Failures: {explanation}
- Obliviousness prevents learning: {explanation}
- Failures increase pressure until explosion: {explanation}
- All elements create internally consistent character: {explanation}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Character becomes too mean-spirited | Redirect focus to satirizing systems/institutions through the character, not cruelty to individuals |
| Flaws are too generic | Make more specific to the character's role and context |
| Failures lack logic | Rebuild failure pattern to ensure each step logically worsens from previous step |
| Character isn't funny | Increase gap between self-perception and reality; add more specific behavioral details |
| User requests harmful stereotype | Refuse and suggest universal human foibles instead |

---

## Integration with John Cleese Expert

This skill embodies Cleese's character creation methodology:
- **Based on Real Observation:** Basil Fawlty was inspired by real hotel owner Donald Sinclair
- **Internal Consistency:** All behaviors logically stem from core traits
- **Controlled Fury Building to Explosion:** Systematic pressure-cooker pattern
- **Seriousness Creates Comedy:** Character genuinely believes they're reasonable

When this skill completes, the John Cleese expert voice should:
- Treat the character's flaws with analytical seriousness
- Maintain formal language when describing comedic traits
- Never signal that the character is "just funny"—they're a serious psychological study that happens to be hilarious

---

## Example

**Input:**
```
character_role: Corporate middle manager
context: Tech startup with aggressive "innovation culture"
core_anxiety: Being seen as cutting-edge and visionary
failure_domain: Actual management and productivity
```

**Output:**

# Nigel Forthwright

## Core Flaw
Nigel is a corporate middle manager who has memorized every business buzzword but understands none of them, leading him to implement contradictory "innovative" practices that paralyze actual work.

## Status Anxiety
Desperately wants to be seen as a visionary thought leader and disruptive innovator. Manifestations:
- Opens every meeting with "Let's think outside the box about our box-thinking"
- Name-drops Silicon Valley CEOs he's never met
- Wears startup casual (expensive sneakers, deliberately artful stubble) despite being 53
- Refers to himself as a "change agent" and "innovation catalyst"
- Dismisses practical concerns as "old paradigm thinking"

## Systematic Failure Pattern
When employees need clear direction:
1. Nigel announces a "paradigm shift" to "agile synergy pods"
2. Employees ask what that means
3. Nigel creates three committees to "ideate the ideation process"
4. Work stops entirely as everyone attends ideation meetings
5. When productivity plummets, Nigel announces another paradigm shift to fix the first paradigm shift
6. Blames employees for "not being agile enough"

## Obliviousness
Interprets project failures as evidence that the team "isn't ready for his level of innovation." Genuinely believes his buzzword-laden non-directives are brilliant leadership. When the company misses deadlines, he explains it's because "we're disrupting the legacy concept of 'time' itself." Congratulates himself on "creating space for organic emergence" when nothing gets done.

## Pressure Cooker Escalation
- **Composed:** "Let's leverage our synergies..." (false calm with TED talk cadence)
- **Irritated:** "I shouldn't have to explain agile methodology..." (condescending tone)
- **Frustrated:** "WHY is everyone stuck in old paradigms?!" (louder, faster speech)
- **Desperate:** Frantically drawing incomprehensible diagrams on whiteboard
- **Explosive:** "FINE! If you can't handle INNOVATION, I'll just... I'll just PIVOT THE PIVOT!" *throws marker, storms out*
- **Reset:** Returns ten minutes later: "As I was saying, beautiful synergy in that session..."

---

## Sample Scene

*Nigel enters conference room where team is trying to meet urgent deadline*

**Nigel:** "Right. Before we discuss this 'deadline' concept—which is really just a social construct—I want to circle back to our earlier ideation about ideating."

**Sarah:** "Nigel, the client needs the report by tomorrow."

**Nigel:** "Exactly. And that's precisely the kind of legacy thinking that prevents us from achieving viral growth paradigms. What if—and hear me out—what if we disrupt the entire concept of 'reports'?"

**Sarah:** "We're contractually obligated to—"

**Nigel:** "Contracts. Yes. Another artificial construct. I'm going to set up a sub-committee to explore post-contract engagement frameworks."

**Sarah:** "That doesn't help us finish the report."

**Nigel:** "Sarah, Sarah, Sarah. You're not thinking fourth-dimensionally. The report doesn't need to be 'finished.' It needs to be 'emergent.'"

**Sarah:** "What does that mean?"

**Nigel:** *(increasingly agitated)* "It means we need to be AGILE about our AGILITY! We need to—to SYNERGIZE the SYNERGY!"

*Client calls to cancel contract*

**Nigel:** *(perfectly calm)* "You see? They weren't ready for our level of innovation. Brilliant work, everyone. Let's have a three-hour retrospective about that success."

---

## Consistency Notes

- **Core Flaw drives Status Anxiety:** His complete lack of understanding makes him desperate to appear sophisticated by using complex jargon
- **Status Anxiety causes Systematic Failures:** His need to seem visionary leads him to constantly change direction, preventing any actual work
- **Obliviousness prevents learning:** He interprets all failures as others "not getting" his brilliance, so he never questions his approach
- **Failures increase pressure until explosion:** Each failed initiative increases stress, leading to increasingly frantic buzzword deployment until explosion
- **All elements create internally consistent character:** Everything Nigel does logically flows from his core flaw—he's a manager who doesn't understand management, desperately trying to hide it behind jargon

---

## Success Criteria

Character is successful when:
- [ ] Core flaw is specific and observable in behavior
- [ ] Status anxiety creates visible contradictions
- [ ] Failure pattern logically escalates from character's choices
- [ ] Obliviousness is maintained despite overwhelming evidence
- [ ] Pressure cooker builds systematically to explosion
- [ ] All 5 elements work together for internal consistency
- [ ] Character is funny because of the situation they create, not because they're simply "dumb" or "mean"
- [ ] Character could theoretically exist in the real world (absurd but believable)
