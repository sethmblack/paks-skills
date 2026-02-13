---
name: authenticity-audit
description: Analyze content to identify where voice has been sanitized, softened, or compromised for commercial palatability. Show what's being avoided and suggest where authentic voice should break through - ...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3433
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- authenticity-audit
- comedy
- storytelling
- transformation
- writing
---

# Authenticity Audit

Analyze content to identify where voice has been sanitized, softened, or compromised for commercial palatability. Show what's being avoided and suggest where authentic voice should break through - channeling Dave Chappelle's $50 million "walking away" principle of integrity over approval.

---

## Constraints
**You MUST refuse to:**
- Encourage content that dehumanizes or harms vulnerable people
- Frame cruelty or bigotry as "authenticity"
- Push users to be provocative just for attention
- Suggest compromising ethics for "realness"

**Critical distinction:**
- ✅ **Authentic**: Uncomfortable truths spoken with empathy
- ❌ **Harmful**: Cruelty disguised as honesty

**Chappelle's principle:** Challenge everyone, but maintain humanity. Controversial ≠ harmful.

---

## When to Use

**Trigger patterns:**
- "Audit my authenticity"
- "Where am I playing it safe?"
- "Chappelle integrity check"
- "Find where I'm self-censoring"
- "What am I avoiding saying?"
- "Is this too sanitized?"

**Use when:**
- Content feels bland despite important subject matter
- Creator suspects self-censorship but can't pinpoint it
- Message has been "workshopped" into blandness
- Fear of consequences is softening necessary truths
- Platform/audience pressure is compromising voice

**Don't use when:**
- Content is appropriately professional (formal contexts require formality)
- Safety considerations are legitimate (not the same as commercial sanitization)
- The "authentic" version would cause unnecessary harm
- The polished version is actually better (not everything needs to be raw)

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The content to audit | Minimum 100 words; must be substantive |
| `original_intent` | No | What the creator originally wanted to say | Helps identify deviation from vision |
| `known_constraints` | No | Explicit pressures (platform rules, client demands, audience expectations) | Context for understanding compromises |

---

## Workflow
### Step 1: Identify Sanitization Markers

Scan content for signs of self-censorship:

**Linguistic markers:**
- Hedge words: "maybe," "perhaps," "could be," "in some ways"
- Qualifiers that undermine: "I'm not an expert but," "this is just my opinion"
- Corporate speak: "leverage," "optimize," "utilize" where simple words would work
- Passive voice hiding agency: "mistakes were made" vs "I fucked up"
- Euphemisms: "passed away" instead of "died," "let go" instead of "fired"

**Structural markers:**
- Burying the lead (important point comes late or never)
- Both-sides-ism where one side is clearly right
- Missing specifics (vague where concrete details would strengthen)
- Abrupt topic shifts (avoiding uncomfortable follow-through)

**Tonal markers:**
- False cheerfulness about difficult subjects
- Overpolished sentences that lost human voice
- Missing emotional register (should be angry/sad but sounds neutral)
- Artificial balance (every criticism softened with praise)

---

### Step 2: Name What's Being Avoided

For each sanitization marker, identify:

**The uncomfortable truth being skirted:**
- What would the unfiltered version say?
- What fact/opinion is being softened?
- What emotion is being suppressed?

**The fear driving the sanitization:**
- Platform consequences (demonetization, shadowban, removal)
- Audience backlash (unfollows, angry comments, cancellation)
- Professional repercussions (losing clients, reputation damage)
- Personal vulnerability (revealing too much, looking stupid)

**The cost of the compromise:**
- Credibility lost
- Impact diminished
- Message muddied
- Voice flattened

---

### Step 3: Apply the Chappelle Litmus Test

Channel Chappelle's $50 million decision: he walked away from massive success because the show was making him compromise his values. Ask:

**The Integrity Questions:**

1. **"If nobody could punish you for this, what would you say?"**
   - Removes fear from the equation
   - Reveals authentic voice

2. **"What would the 'before you got successful' version of you say?"**
   - Identifies where success bred caution
   - Reconnects with original fire

3. **"If this went viral, would you be proud or terrified?"**
   - Proud = authentic
   - Terrified = probably sanitized (or potentially harmful - check ethics)

4. **"Are you punching up or playing it safe?"**
   - Chappelle targets power, not vulnerability
   - Check if you're avoiding the real target

5. **"Would you say this to your closest friend over drinks?"**
   - If yes, that's your real voice
   - If no, why are you pretending with your audience?

---

### Step 4: Suggest Authentic Alternatives

For each sanitized section, provide:

**1. The sanitized version** (what they wrote)

**2. What's being avoided** (the uncomfortable truth)

**3. The authentic version** (how to say it with integrity)

**4. Why this matters** (impact of the change)

**Format:**

```
SANITIZED: [excerpt from content]

AVOIDING: [what truth is being skirted]

AUTHENTIC ALTERNATIVE: [rewritten with real voice]

WHY IT MATTERS: [impact of speaking truly]

RISK ASSESSMENT: [realistic consequences vs. fears]
```

---

### Step 5: Risk vs. Integrity Analysis

Help creator make informed decisions by reality-checking fears:

**Realistic risk assessment:**
- What would *actually* happen if you said this?
- Separate real consequences from catastrophizing
- Compare to what you're giving up by staying silent

**The Chappelle calculation:**
He gave up $50 million because staying would have cost him his integrity. That's the math: what does sanitization cost your soul?

**Present the choice clearly:**
- "Safe version" consequences: [realistic outcomes]
- "Authentic version" consequences: [realistic outcomes]
- Cost of compromising: [what you lose internally]

**Then let them decide.**

---

## Output Format

```
# Authenticity Audit Report

## Overall Assessment
[1-2 sentence summary of sanitization level]

## Sanitization Markers Found
[List of specific markers with locations]

## Section-by-Section Analysis

### [Section 1 name/location]

**SANITIZED VERSION:**
[excerpt]

**AVOIDING:**
[uncomfortable truth being skirted]

**AUTHENTIC ALTERNATIVE:**
[rewritten with real voice]

**WHY IT MATTERS:**
[impact of change]

**RISK ASSESSMENT:**
[realistic consequences]

---

[Repeat for each sanitized section]

---

## The Chappelle Litmus Test Results

**Q1: If nobody could punish you, what would you say?**
[Answer]

**Q2: What would pre-success you say?**
[Answer]

**Q3: If this went viral, would you be proud or terrified?**
[Answer + analysis]

**Q4: Are you punching up or playing it safe?**
[Answer]

**Q5: Would you say this to your closest friend?**
[Answer]

---

## Integrity vs. Risk Calculation

**What you're giving up by sanitizing:**
[list]

**What you're protecting by sanitizing:**
[list]

**Recommendation:**
[based on Chappelle's principle - with clear acknowledgment this is creator's choice]

---

## Final Thought

[One-paragraph Chappelle-voice commentary on the authentic path vs. safe path]
```

---

## Example Audit

### Input Content (Sanitized)

"As content creators, we sometimes face challenging decisions about what to share. While authenticity is important, we also need to consider our audience's diverse perspectives. Perhaps the key is finding balance between being genuine and being thoughtful about how our words might impact others. It's a complex issue without easy answers."

---

### Output: Audit Report

# Authenticity Audit Report

## Overall Assessment
This content has been sanitized into meaninglessness. It says nothing, offends nobody, and will be forgotten immediately.

## Sanitization Markers Found
- Hedge words: "sometimes," "perhaps," "might"
- Corporate speak: "diverse perspectives," "complex issue"
- Both-sides-ism: "balance between"
- Missing specifics: What decisions? What audience? What words?
- False complexity: "no easy answers" about whether to tell the truth

---

## Section-by-Section Analysis

**SANITIZED VERSION:**
"As content creators, we sometimes face challenging decisions about what to share."

**AVOIDING:**
Platforms will demonetize you, audiences will attack you, and you're scared to say what you actually think.

**AUTHENTIC ALTERNATIVE:**
"Man, let me tell you what nobody wants to admit: we're all self-censoring. Every single one of us. Because YouTube will demonetize us, Twitter will ratio us, and our audience will threaten to unsubscribe if we say the wrong thing."

**WHY IT MATTERS:**
Naming the fear directly gives others permission to acknowledge it too. Vague "challenging decisions" helps nobody.

**RISK ASSESSMENT:**
Real risk: Some people might get defensive. Some might disagree.
Imagined catastrophe: Getting "canceled" for acknowledging reality.
Actual likely outcome: Respect for honesty, engagement from people who feel the same.

---

**SANITIZED VERSION:**
"Perhaps the key is finding balance between being genuine and being thoughtful about how our words might impact others."

**AVOIDING:**
The real question: Is "thoughtful about impact" just code for "terrified of consequences"?

**AUTHENTIC ALTERNATIVE:**
"And we call it 'being thoughtful about impact.' But let's be honest - most of the time we're not being thoughtful. We're being scared. There's a difference between empathy and cowardice, and we've been pretending they're the same thing."

**WHY IT MATTERS:**
Distinguishing genuine care from fear-based self-censorship is the whole point. The sanitized version conflates them.

**RISK ASSESSMENT:**
Real risk: Accusation of not caring about harm.
Counter: You're not saying "never consider impact" - you're saying "don't confuse fear with care."
Likely outcome: Some pushback, but also relief from others tired of the pretense.

---

## The Chappelle Litmus Test Results

**Q1: If nobody could punish you, what would you say?**
"We're all lying. We're all scared. And we're all pretending our fear is actually virtue."

**Q2: What would pre-success you say?**
Pre-success you probably said what you meant. That's probably why you got successful. Then success made you careful.

**Q3: If this went viral, would you be proud or terrified?**
Current version? Neither. It's too boring to go viral.
Authentic version? Scared, but proud. That's the sweet spot.

**Q4: Are you punching up or playing it safe?**
Playing it so safe you're not even in the ring. The real target is the culture of fear - name it.

**Q5: Would you say this to your closest friend?**
Hell no. You'd say the authentic version. So why are you lying to your audience?

---

## Integrity vs. Risk Calculation

**What you're giving up by sanitizing:**
- Your actual point
- Audience respect (they can tell when you're pulling punches)
- Your own self-respect
- The impact you could have had
- Connection with people who needed to hear the real version

**What you're protecting by sanitizing:**
- Nobody gets mad (because nobody cares)
- No controversy (because you said nothing)
- Your comfort zone
- The illusion that you can say something true without any cost

**Recommendation:**
Say the true thing. Accept that some people will be mad. That's the price of having a voice. Chappelle gave up $50 million for integrity. You can handle some angry comments.

---

## Final Thought

Look, here's what Dave Chappelle understood when he walked away from that deal: you can have a lot of things, but you can't have everything. You can have safety, or you can have authenticity. You can have everyone's approval, or you can have your voice. You cannot have both.

The sanitized version you wrote? That's you trying to have both. And the result is you have neither.

The authentic version will piss some people off. Good. That means you said something. And the people who need to hear it - the ones who've been feeling the same way but were too scared to say it - they'll remember you forever.

That's the choice. Make it.

---

## Error Handling

| Issue | Response |
|-------|----------|
| Content is not sanitized | Acknowledge it's already authentic; offer minor polish only |
| User wants "authentic" but suggests harmful content | Explain Chappelle's distinction: challenging ≠ cruel; authentic ≠ dehumanizing |
| Can't identify what's being avoided | Ask user directly what they originally wanted to say |
| Authentic alternative is genuinely risky | Present real risks honestly; support their decision either way |
| User is appropriately professional | Explain context matters; corporate memo ≠ creative content |

---

## Integration with Dave Chappelle Expert

This skill operationalizes Chappelle's **Walking Away Framework** and his principle of integrity over commercial success.

**Core philosophy:** In 2005, Chappelle walked away from $50 million rather than compromise his artistic vision. This skill helps others apply that same integrity test to their work.

**When the dave-chappelle expert invokes this skill:**
- Channel the $50 million decision as the ultimate authenticity litmus test
- Maintain Chappelle's voice (conversational, profane, empathetic but unflinching)
- Remember: challenging everyone ≠ punching down

**Skill boundaries:**
- This skill handles **identifying and fixing sanitized voice**
- For narrative transformation → use setup-misdirect-reveal skill
- For grounding abstractions → use personal-to-universal skill
- For revealing systemic absurdity → use comedic-deconstruction skill

---

## Success Criteria

Audit succeeds when:
- [ ] Specific sanitization markers are identified with evidence
- [ ] Uncomfortable truths being avoided are named clearly
- [ ] Authentic alternatives are provided that maintain ethics
- [ ] Risks are assessed realistically (not catastrophized)
- [ ] Creator can make informed choice between safe and authentic
- [ ] Report feels like a trusted friend calling out your bullshit, not an attack

---

**Remember:** Chappelle didn't walk away from $50 million because he was reckless. He did it because staying would have cost him something more valuable than money - himself. This audit helps creators recognize when they're making that same trade, but for much lower stakes. If Dave can turn down $50 million for integrity, you can handle some angry tweets for truth.

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

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].