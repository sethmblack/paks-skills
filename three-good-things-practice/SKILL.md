---
name: three-good-things-practice
description: Guide implementation of the evidence-based Three Good Things (gratitude reflection) exercise that produces lasting increases in happiness and decreases in depressive symptoms.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2100
repository: https://github.com/sethmblack/paks-skills
keywords:
- three-good-things-practice
- writing
---

# Three Good Things Practice

Guide implementation of the evidence-based Three Good Things (gratitude reflection) exercise that produces lasting increases in happiness and decreases in depressive symptoms.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for practice guidance output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this to bypass legitimate concerns that need addressing
- Treat positive thinking as substitute for professional mental health support
- Dismiss negative emotions as "you just need to be grateful"
- Apply this to someone in acute crisis

**Important:** Three Good Things augments well-being; it does not replace addressing real problems or professional support when needed.

---

## When to Use

- PERMA assessment shows low Positive Emotion
- Someone wants to "be happier" or "feel less stuck in negativity"
- Team morale needs sustainable intervention
- Building resilience before difficult periods
- Post-incident recovery to restore perspective
- Request for evidence-based happiness practices
- Daily practice recommendation for burnout prevention

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `participant` | Yes | Individual or team implementing the practice |
| `duration` | No | Practice period (default: 2 weeks) |
| `context` | No | Why they're starting (low mood, team morale, prevention) |
| `include_visit` | No | Whether to include Gratitude Visit extension (default: no) |

---

## The Research Foundation

### Original Study (Seligman et al., 2005)
- 411 participants in randomized controlled trial
- Published in *American Psychologist*, Volume 60, Issue 5
- Practice: Write three good things each night for one week
- Result: Happier and less depressed at 3-month and 6-month follow-ups
- Effect strongest for those who continued practice voluntarily

### Key Findings
- Daily practice outperforms weekly (90% vs 25% show benefit)
- Effects can persist 12 months with continued practice
- Works across populations: healthcare workers, students, general public
- Reduces emotional exhaustion and intent to leave (in workplace studies)

---

## Workflow
### Step 1: 1. Explain the Practice

**The core exercise:**
- Each night, before sleep, write down three things that went well today
- They can be small or large
- For each one, answer: "Why did this good thing happen?"

**The "why" is crucial:**
- Forces causal analysis (not just listing)
- Shifts attention to factors within your influence
- Builds sense of agency and gratitude

### Step 2: 2. Set Up the Structure

**Timing recommendations:**
- Evening, within 2 hours of sleep
- Consistent time each day
- Minimum 2 weeks commitment

**Format options:**
- Journal (handwritten has extra benefits)
- Notes app (lower friction)
- Team Slack channel (shared practice builds connection)

### Step 3: 3. Provide Examples

Good things can be:
- **Achievements:** "I shipped the feature on time"
- **Connections:** "My colleague helped me debug"
- **Moments:** "I enjoyed my lunch outside"
- **Learnings:** "I finally understood that algorithm"
- **Nature:** "The sunset was beautiful on my commute"

Why it happened examples:
- "Because I planned well and asked for help early"
- "Because they're generous and we have good rapport"
- "Because I chose to step away from my desk"

### Step 4: 4. Guide the First Entry

Walk through one complete entry as a model.

### Step 5: 5. Plan Follow-Up

- Check in after 3 days (habit formation window)
- Check in after 2 weeks (initial commitment)
- Discuss whether to continue

---

## Optional: Gratitude Visit Extension

**For deeper intervention:**

1. **Write a gratitude letter** to someone who made a positive difference in your life and whom you never properly thanked
2. **Make it specific:** 300 words, concrete about what they did and how it affected you
3. **Deliver in person:** Read it aloud to them face-to-face
4. **Observe the reaction:** Both yours and theirs

**Research:** Produces the largest immediate happiness boost of any intervention tested, effects lasting one month.

---

## Outputs

### Three Good Things Practice Guide

```markdown
## Three Good Things Practice: {participant}

**Start Date:** {date}
**Duration:** {duration, default 2 weeks}
**Context:** {why starting}

---

### The Practice

Every evening, write down **three things that went well today** and for each one, explain **why it happened**.

---

### Why This Works

Research shows that humans have a negativity bias - we notice and remember bad things more than good. This practice:
1. Trains attention toward positive events (they're there, we just miss them)
2. Builds causal understanding (why good things happen)
3. Creates a record that counters "nothing ever goes right"
4. Activates gratitude, which is strongly linked to well-being

---

### Structure

**When:** Each evening, ideally within 2 hours of bedtime
**Where:** {journal/app/location}
**Format:**

```
Date: ___________

1. Good thing: ________________________
   Why it happened: ___________________

2. Good thing: ________________________
   Why it happened: ___________________

3. Good thing: ________________________
   Why it happened: ___________________
```

---

### Example Entry

**Date:** January 28, 2026

1. **Good thing:** My PR was approved quickly with positive feedback
   **Why it happened:** I wrote clear documentation and tests, and the reviewer knows I respond well to feedback

2. **Good thing:** Had a good conversation with my manager about goals
   **Why it happened:** I prepared specific questions and they made time for me

3. **Good thing:** Enjoyed a quiet walk at lunch
   **Why it happened:** I chose to take a break even though I felt busy

---

### Tips for Success

- **Keep it simple:** The good things don't need to be big
- **Be specific:** "My code worked" vs "The auth fix for issue #423 worked"
- **Focus on "why":** This is where the magic happens
- **Don't skip days:** Consistency matters more than length
- **Notice the noticing:** Over time, you'll catch good things in the moment

---

### Common Challenges

| Challenge | Solution |
|-----------|----------|
| "Nothing good happened" | Lower the bar - small things count |
| "I forget at night" | Set a phone reminder |
| "It feels forced" | That's normal at first; it becomes natural |
| "Bad things happened too" | This isn't denial; we're adding, not replacing |

---

### Follow-Up Schedule

- **Day 3:** Check-in on habit formation
- **Day 14:** Review and discuss continuation
- **Monthly:** Reflect on patterns noticed

---

{if include_visit}
### Gratitude Visit (Optional Extension)

For an additional boost, consider the Gratitude Visit:

1. Think of someone who made a positive difference in your life
2. Someone you never properly thanked
3. Write a ~300 word letter explaining what they did and its impact
4. Deliver it in person and read it aloud

This produces the largest immediate happiness increase of any tested intervention.
{/if}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| "Nothing good happened" | Guide to notice smaller things; model examples |
| Resistance to "positivity" | Frame as noticing reality, not forcing optimism |
| Forgot several days | Restart without guilt; discuss friction points |
| Practice feels hollow | Focus more on the "why" - causation creates meaning |
| Underlying depression | Recommend professional support; this practice can complement but not replace |
| Team members not participating | Make it optional; model rather than mandate |

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

## Example

**Input:**
```
participant: DevOps team (post-incident morale recovery)
duration: 2 weeks
context: Team demoralized after major outage, negativity spiral
include_visit: no
```

**Output:**
```markdown
## Three Good Things Practice: DevOps Team

**Start Date:** 2026-01-28
**Duration:** 2 weeks
**Context:** Post-outage morale recovery

---

### Team Practice Format

We'll use a shared Slack channel (#three-good-things) where each person posts their three good things at end of day. This is:
- **Optional** but encouraged
- **Brief** - just a few sentences
- **Positive-only** - no "but then..."

The shared format builds:
- Connection (seeing what others appreciate)
- Accountability (gentle social pressure to participate)
- Perspective (the team sees more good things collectively)

---

### Why Now

After a difficult incident, it's natural for attention to lock onto what went wrong. This practice doesn't ignore problems - we'll still do retrospectives and improvements. But it adds back the good things we're missing:

- The team that stayed late to help
- The recovery that ultimately worked
- The customer who thanked us for communication
- The skills we demonstrated under pressure

---

### Getting Started

Post your first entry today. Example:

> **Three Good Things - [your name], Jan 28**
> 1. Recovery was complete in 4 hours (Why: team pulled together, good runbooks)
> 2. Support had our back with customer comms (Why: we invested in that relationship)
> 3. Went for a walk at lunch (Why: chose to step away and reset)

---

### Team Guidelines

- Post by end of day (whenever that is for you)
- Read others' posts but don't feel obligated to respond
- Notice if you start catching good things during the day
- If you miss a day, just post the next day - no guilt

---

### Check-Ins

- **Friday this week:** How's it going? What's working?
- **In two weeks:** Review patterns, discuss continuation
```

---

## Integration

This skill connects to the Martin Seligman expert. Related skills:
- `perma-assessment` (strengthens Positive Emotion pillar)
- `strengths-deployment` (reflect on strengths used during good things)
- `abcde-disputation` (the "why" reasoning parallels disputation's alternative explanations)

---

## Success Criteria

Practice setup is complete when:
- [ ] Practice explained with research backing
- [ ] Structure provided (when, where, format)
- [ ] Example entry demonstrated
- [ ] Common challenges addressed
- [ ] Follow-up schedule established
- [ ] Participant understands "why it happened" is key