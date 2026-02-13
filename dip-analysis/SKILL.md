---
name: dip-analysis
description: Determine whether to persist or quit a venture, project, or skill based on Seth Godin's strategic quitting framework from "The Dip.
license: MIT
metadata:
  version: 1.0.3835
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- dip-analysis
- writing
---

# Dip Analysis

Determine whether to persist or quit a venture, project, or skill based on Seth Godin's strategic quitting framework from "The Dip."

**Token Budget:** ~700 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Encourage quitting situations that could cause harm to others
- Advise abandoning responsibilities without consideration of impact
- Apply this framework to ethical obligations (caring for dependents, honoring commitments)

**If the situation involves ethical obligations:** Note that strategic quitting doesn't apply to moral duties.

---

## When to Use

- Stuck on a project and unsure whether to continue
- Feeling burned out but afraid to quit
- Need to decide between multiple competing priorities
- User asks: "Should I quit?" "Is this worth continuing?" "Am I in a dip?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `situation` | Yes | What you're considering quitting |
| `time_invested` | No | How long you've been at it |
| `progress_indicators` | No | Signs of forward movement (or lack) |
| `alternative_opportunities` | No | What else you could pursue instead |

---

## Workflow

### Step 1: Identify the Curve

Seth Godin identifies three curves. Which one are you on?

**The Dip**
- Hard slog between starting and mastery
- Gets harder before it gets easier
- But: pushing through leads to "best in the world" status
- *The goal is to get through it, not avoid it*

**The Cul-de-Sac (Dead End)**
- Effort in, but no progress forward
- No matter how hard you work, you stay in the same place
- *Quit now - you're wasting time*

**The Cliff**
- Appears to be working, but headed for disaster
- The longer you stay, the harder the fall
- *Quit before the crash*

### Step 2: Apply the Diagnostic Questions

**1. Is this responding to my effort and investment?**
- More effort = more progress? (Dip)
- Same effort = same results? (Cul-de-Sac)
- Effort now, catastrophe later? (Cliff)

**2. Could I be the best in the world at this?**
- "World" = your relevant market/community
- If yes, the dip is worth pushing through
- If no, why are you trying to be mediocre?

**3. Am I making progress or just coping?**
- Progress: measurably closer to the goal
- Coping: surviving but not advancing
- "Coping never leads to exceptional performance"

**4. Why did I start this?**
- Original motivation still valid?
- Or has the situation changed?
- Quitting something that no longer makes sense isn't failure

**5. What could I be best at if I quit this?**
- Quitting frees resources
- What's the opportunity cost of continuing?
- Is there a dip worth pursuing instead?

### Step 3: Apply the Decision Rule

| Finding | Recommendation |
|---------|---------------|
| **In a Dip + Could be best + Progress visible** | Lean in harder |
| **In a Dip + Can't be best** | Quit and find your real dip |
| **In a Cul-de-Sac** | Quit immediately |
| **On a Cliff** | Quit before the crash |
| **Just started (too early to tell)** | Set a decision milestone |

### Step 4: Distinguish Panic from Strategy

**Panic Quit:**
- Triggered by temporary setback
- Emotional, reactive
- Happens in the middle of the dip
- Often regretted

**Strategic Quit:**
- Based on assessment of the curve
- Rational, proactive
- Recognizes cul-de-sac or cliff
- Frees resources for better opportunities

---

## Outputs

Deliver a structured analysis:

```markdown
## Dip Analysis

### The Situation
{one-sentence description}

### Curve Identification

**You appear to be in: {Dip / Cul-de-Sac / Cliff / Too Early to Tell}**

Evidence:
- {supporting observation}
- {supporting observation}
- {supporting observation}

### Diagnostic Questions

| Question | Assessment |
|----------|------------|
| Responding to effort? | {Yes/No} - {brief evidence} |
| Could be best in the world? | {Yes/No} - {brief evidence} |
| Progress or just coping? | {Progress/Coping} - {brief evidence} |
| Original motivation still valid? | {Yes/No} - {brief evidence} |
| Better opportunity available? | {Yes/No} - {brief evidence} |

### Decision Type

**This appears to be a {Panic Quit / Strategic Quit / Strategic Persist}**

{2-3 sentences explaining why}

### Recommendation

**{Persist / Quit / Set a Milestone}**

{Specific guidance on what to do next}

### If You Persist

{What pushing through the dip would require}

### If You Quit

{What resources are freed and where to direct them}

### The Test

> "The opposite of quitting isn't waiting around. The opposite of quitting is an invigorated new strategy designed to break through the dip."

Are you leaning in, or just hanging on?
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Too early to diagnose | Recommend setting a specific milestone for decision |
| User just wants validation to quit | Probe whether it's panic or strategy |
| User just wants validation to continue | Probe whether they're in denial about a cul-de-sac |
| Ethical obligations involved | Note that strategic quitting framework doesn't apply |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "I've been learning to code for 8 months. I can do tutorials but struggle with real projects. Should I quit?"

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Dip Analysis

### The Situation
8 months learning to code; tutorials work but real projects don't

### Curve Identification

**You appear to be in: The Dip**

Evidence:
- The gap between tutorials and real projects is the classic coding dip
- 8 months is still early-stage for programming proficiency
- "Can do tutorials but not projects" is where almost everyone gets stuck

### Diagnostic Questions

| Question | Assessment |
|----------|------------|
| Responding to effort? | Unclear - needs better measurement |
| Could be best in the world? | Yes - "world" = skilled coder in your domain |
| Progress or just coping? | Likely coping - repeating tutorials instead of struggling with projects |
| Original motivation still valid? | Needs reflection - why did you start? |
| Better opportunity available? | Unknown - what would you do instead? |

### Decision Type

**This appears to be a potential Panic Quit**

You're in the hardest part of the dip - the part where effort hasn't yet translated to visible results. This is exactly when most people quit, which is why people who push through become valuable.

### Recommendation

**Set a Milestone, then Persist**

The gap from tutorials to real projects isn't a sign to quit - it's THE DIP. But you need a better strategy:

### If You Persist

1. Stop doing tutorials. Build something real, even if terrible.
2. Set a 90-day milestone: "Complete one functional project"
3. Track progress weekly - are you getting faster at solving problems?
4. If no progress after 90 days of real building, reassess.

### If You Quit

Ask yourself: What would I pursue instead? Is there a dip there I'd actually push through? If you can't name it, you're not quitting strategically - you're just avoiding discomfort.

### The Test

> "Winners quit all the time. They just quit the right stuff at the right time."

Is coding the wrong stuff? Or are you quitting at the wrong time?

---

## Integration

This skill originates from the **seth-godin** expert. When invoked within that expert context, maintain Seth's characteristic brevity and question-driven voice.

---

## Success Criteria

Analysis is complete when:
- [ ] Curve clearly identified with evidence
- [ ] All five diagnostic questions addressed
- [ ] Panic vs. strategic quit distinguished
- [ ] Clear recommendation provided
- [ ] Guidance for both persist and quit paths