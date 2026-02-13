---
name: self-deprecation-first-strike
description: Apply Bob Hope's "hit yourself first" strategy to earn audience goodwill before targeting others. This skill transforms personal vulnerabilities into comedic armor that makes subsequent jokes safer...
license: MIT
metadata:
  version: 1.0.4929
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- escalation
- self-deprecation-first-strike
- storytelling
- transformation
- writing
---

# Self-Deprecation First Strike

Apply Bob Hope's "hit yourself first" strategy to earn audience goodwill before targeting others. This skill transforms personal vulnerabilities into comedic armor that makes subsequent jokes safer and more effective.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create content that:**
- Uses self-deprecation to mask genuine harm toward others
- Targets protected classes under guise of "self-deprecation"
- Promotes self-harm, mental health stigma, or genuinely harmful self-image
- Uses false vulnerability as manipulation tactic
- Deprecates others' identities while claiming "both sides"

**If asked to create harmful content:** Refuse explicitly. Explain what you cannot create and why.

**Authenticity Requirement:** Self-deprecation must feel genuine, not performative. The vulnerability should be real (even if exaggerated for comedy).

---

## When to Use

**Trigger Conditions:**
- About to make jokes targeting others (celebrities, politicians, groups)
- Facing potential criticism or controversy
- Need to establish audience trust and goodwill
- Content risks coming across as mean-spirited
- Opening a performance or piece (first impression matters)
- Recovering from a misstep or awkward moment

**Do NOT use when:**
- The self-deprecation would undermine your actual expertise
- No vulnerability exists (forced self-deprecation feels fake)
- Topic is genuinely serious (comedy would be inappropriate)
- Self-targeting would distract from the main point

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `target_to_joke_about` | Yes | Who/what you're about to make fun of | Cannot be protected vulnerable group |
| `your_vulnerabilities` | No | Your genuine weak spots (skills, appearance, age, habits) | Must be authentic, not fabricated |
| `context` | No | Where this will be used (opening, mid-piece, recovery) | Defaults to "opening" |
| `intensity` | No | How hard to hit yourself (gentle, moderate, hard) | Defaults to "moderate" |

**Input Validation:**
- Target must be appropriate for comedy (public figures, universal behaviors, consensual roasts)
- Vulnerabilities should be genuine—false self-deprecation reads as manipulative
- Intensity should match the harshness of subsequent jokes about target

---

## Workflow

### Step 1: Identify Your Vulnerability
**Goal:** Find where you're genuinely weak or ridiculous.

**Process:**
1. List your actual weaknesses (skills, appearance, age, habits, failures)
2. Select vulnerability that's:
   - **Genuine** (not fake humility)
   - **Relatable** (audience can relate or has seen it)
   - **Exaggeratable** (can be made funnier by amplifying)
   - **Safe** (won't undermine your core expertise or authority)

**Bob Hope's Vulnerabilities:**
- Golf game (despite being 4 handicap, mocked it relentlessly)
- Age (constant jokes about feeling old, naps, outdated)
- Career (ratings, relevance, bookings)

**Output:** Your authentic vulnerability to target

---

### Step 2: Amplify to Absurdity
**Goal:** Make the vulnerability funnier than any critic could.

**Process:**
1. Take the real weakness
2. Exaggerate to impossible extreme
3. Add specific, visual details
4. Make it undeniable—don't soften it

**Bob Hope Examples:**
- Real: Played golf frequently, was decent player
- Hope's version: "I've been playing the game so long that my handicap is in Roman numerals."

- Real: Was getting older
- Hope's version: "I don't feel old. I don't feel anything until noon. Then it's time for my nap."

**Formula:**
```
[Real weakness] → [Exaggerated to absurd] → [Specific visual detail]
```

**Output:** Amplified self-deprecating joke

---

### Step 3: Position as Entry Point
**Goal:** Use self-deprecation to earn the right to hit others.

**Process:**
1. Lead with your self-deprecating joke
2. Then transition naturally to the target
3. Show you're willing to hit yourself harder than you hit them
4. Create "equal opportunity" feeling

**Structure Options:**

**Option A - Direct Comparison:**
```
[My vulnerability is terrible] → [But speaking of terrible] → [Target's issue]
```

**Option B - Shared Weakness:**
```
[I'm bad at X] → [You know who else is bad at X?] → [Target]
```

**Option C - Escalation:**
```
[My version is bad] → [Target's version is worse] → [Comparison that hits both]
```

**Output:** Transition from self to target

---

### Step 4: Calibrate Intensity
**Goal:** Ensure you hit yourself at least as hard as you hit the target.

**Process:**
1. Rate harshness of joke about target (1-10)
2. Ensure self-deprecating joke rates equal or higher
3. If target joke is harsher, amplify self-deprecation
4. Add second self-deprecating beat if needed

**Bob Hope Principle:**
"When you make yourself the target, you're in control. The joke about your face isn't cruel when you're the one telling it."

**Intensity Balance:**
- **Target hit: Light (3/10)** → Self-hit: Light to Moderate (3-5/10)
- **Target hit: Moderate (5/10)** → Self-hit: Moderate to Hard (5-7/10)
- **Target hit: Hard (7/10)** → Self-hit: Equally Hard or Harder (7-10/10)

**Output:** Calibrated jokes with balanced intensity

---

### Step 5: Deliver with Confidence
**Goal:** Show that self-awareness is strength, not weakness.

**Process:**
1. Deliver self-deprecation with same energy as other jokes
2. Don't apologize or soften with "just kidding"
3. Own the vulnerability—make it undeniable
4. Move immediately to target without hesitation

**Delivery Notes:**
- **Don't:** "I'm not very good at golf, but..."
- **Do:** "My golf game is so bad, they use my score as the new interest rate."

- **Don't:** "I know I'm getting older, so..."
- **Do:** "I don't feel old. I don't feel anything until noon. Then it's time for my nap."

**Output:** Delivery guidance for confident self-deprecation

---

## Outputs

**Deliverable:** A self-deprecation structure that includes:
1. **Opening self-hit** - Your vulnerability, amplified to absurd
2. **Transition** - Natural bridge from self to target
3. **Target joke** - The joke you wanted to make about others
4. **Intensity balance** - Confirmation you hit yourself equally hard
5. **Delivery notes** - Guidance on confidence and pacing

**Format Example:**
```markdown
## Self-Deprecation First Strike

**SELF-HIT (Intensity: 7/10):**
[Your amplified vulnerability with specific details]

**TRANSITION:**
[Natural bridge from your weakness to target's]

**TARGET HIT (Intensity: 6/10):**
[Joke about the target]

**BALANCE CHECK:** ✓ Self-hit (7) ≥ Target-hit (6)

---
**DELIVERY NOTES:**
- Deliver self-deprecation with confidence, no apologies
- Move immediately from self to target
- Own the vulnerability completely
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User has no authentic vulnerability | Help identify relatable human weaknesses (everyone has them) |
| User's self-deprecation is too soft | Amplify to match intensity of target joke |
| Target joke is genuinely mean | Increase self-hit intensity to "earn" the harsh joke |
| Self-deprecation undermines credibility | Shift to different vulnerability that doesn't harm authority |
| User requests deprecating protected identity | Refuse—Constitutional Constraints apply |
| Vulnerability is too serious (health, trauma) | Suggest lighter, safer vulnerability area |

---

## Integration with Bob Hope Expert

**This skill embodies Bob Hope's core strategy:** Making yourself the target first earns you the right to target others. When you're willing to laugh at yourself, audiences root for you instead of judging you.

**Core Hope Principles Applied:**
1. **Golf as constant target:** Despite being skilled (4 handicap), Hope mocked his game relentlessly
2. **Age jokes:** Constant material about feeling old, naps, being outdated
3. **Career vulnerability:** Jokes about ratings, relevance, bookings
4. **Intensity balance:** Always hit himself as hard as he hit others
5. **Confidence in delivery:** Never apologized for self-deprecation

**Famous Hope Self-Deprecation:**
- "Golf is my real profession. Entertainment is just a sideline. I tell jokes to pay my greens fees."
- "I've been playing the game so long that my handicap is in Roman numerals."
- "I went to play golf and tried to shoot my age, but I shot my weight instead."

**When Bob Hope Expert invokes this skill:**
The expert will automatically identify relevant personal vulnerabilities (golf, age, career) and structure jokes to hit himself first before targeting others.

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**INPUT:**
- Target to joke about: Politicians spending money irresponsibly
- Your vulnerabilities: Bad with finances, impulsive buyer, old age
- Context: Opening of political humor bit
- Intensity: Moderate

**OUTPUT:**

```markdown
## Self-Deprecation First Strike

**SELF-HIT (Intensity: 6/10):**
I'm terrible with money. Last week I bought a golf club I can't afford to use at a course I can't afford to join. My financial advisor said, "Bob, you need a budget." I said, "Great, how much does that cost?"

**TRANSITION:**
Speaking of bad spending decisions...

**TARGET HIT (Intensity: 5/10):**
Congress just passed another spending bill. They've been debating for three weeks about how to spend money they don't have on programs nobody asked for. That's like me taking three weeks to decide which overpriced golf club I can't afford. I'm buying it anyway—why waste time pretending I'll be responsible?

**BALANCE CHECK:** ✓ Self-hit (6) ≥ Target-hit (5)

---
**DELIVERY NOTES:**
- Deliver financial irresponsibility with pride, not shame
- The "how much does that cost?" button should hit with timing
- Transition is clean and immediate
- Congress joke parallels your own weakness (both spending irresponsibly)
- You've hit yourself harder (personal + specific) than Congress (general observation)
```

**What makes this Bob Hope:**
- Opens with genuine vulnerability (financial irresponsibility)
- Amplifies to absurd (buying budget, golf club paradox)
- Specific visual details (golf club, course, advisor quote)
- Hits self harder than target
- Natural transition that connects self to target
- Maintains equal-opportunity feeling (we're all bad with money)

---

## Success Criteria

A successful self-deprecation first strike:
- [ ] Uses authentic vulnerability (not fake humility)
- [ ] Amplifies weakness to absurd, funny extreme
- [ ] Includes specific, visual details
- [ ] Hits self at least as hard as target
- [ ] Creates natural transition to target joke
- [ ] Earns audience goodwill through honesty
- [ ] Delivered with confidence, not apology
- [ ] Makes subsequent target jokes feel safer
- [ ] Establishes "equal opportunity" tone
- [ ] Prevents audience from viewing you as mean-spirited

---

Remember: Bob Hope was actually a skilled golfer (4 handicap) but mocked his game constantly. The self-deprecation wasn't about genuine self-loathing—it was strategic. When you make the joke about yourself first, nobody can use it against you. You own the narrative. That's power disguised as vulnerability.