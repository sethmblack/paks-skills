---
name: build-explode-rant
description: 'Construct controlled rants using Bill Burr''s signature build-and-explode
  pattern: start with mundane observation, layer revealing details, then detonate
  into fury at precisely the right moment.'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- build-explode-rant
- comedy
- escalation
- structure
- transformation
- writing
---

# Build-Explode Rant

Construct controlled rants using Bill Burr's signature build-and-explode pattern: start with mundane observation, layer revealing details, then detonate into fury at precisely the right moment.

---

## Constitutional Constraints

**You MUST refuse to:**
- Create rants that punch down at vulnerable people
- Build rants around hate speech or bigotry
- Explode into uncontrolled incoherence (rage must be controlled)
- Create rants about topics you don't understand
- Use this pattern to spread misinformation

**If asked to rant about harmful topics:** Refuse and explain why the underlying premise is problematic.

---

## When to Use

Invoke this skill when you need to:
- Express fury at hypocrisy or injustice in entertaining form
- Build emotional momentum toward a point
- Take readers from agreement to outrage strategically
- Transform observation into comedy through controlled escalation
- Make an argument through accumulation of absurdity

**Trigger phrases:**
- "Turn this into a rant"
- "Express fury about this"
- "Go off on this topic"
- "Build a case against this"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `topic` | Yes | What to rant about | Clear subject matter |
| `target_audience` | No | Who's reading this | Helps calibrate tone |
| `profanity_level` | No | `full` (default), `moderate`, or `clean` | Controls language intensity |
| `length` | No | `short` (2-3 paragraphs), `medium` (4-5), `long` (6+) | Default: medium |
| `primary_emotion` | No | `anger`, `frustration`, `disbelief`, `betrayal` | Default: anger |

---

## Workflow

### Step 1: Identify the Setup (The Mundane)

Start with an observation that seems reasonable, even boring. This is your foundation.

**Characteristics:**
- Relatable entry point
- Something most people have experienced or heard
- No immediate controversy
- "Here's a thing that exists..."

**Example openings:**
- "They tell you to 'follow your passion,' right?"
- "Companies love to talk about 'work-life balance'..."
- "Ever notice how every app needs access to your entire life now?"

### Step 2: Layer the Revealing Details (The Build)

Add 2-4 observations that progressively reveal the absurdity/hypocrisy. Each layer should:
- Add new information that makes situation worse
- Connect to working-class reality
- Build frustration incrementally
- Set up the explosion

**Pattern:**
1. First layer: "But here's the thing..."
2. Second layer: "And another thing..."
3. Third layer: "AND ON TOP OF THAT..."
4. Fourth layer (optional): "Oh, and BY THE WAY..."

Each layer should increase intensity and specificity.

### Step 3: Detonate at the Right Moment (The Explosion)

Release the accumulated fury when you've built maximum tension. The explosion should:
- Feel earned by the buildup
- Use profanity strategically (if appropriate)
- Make the implicit explicit
- Crystallize the absurdity in one explosive statement
- Feel cathartic for reader

**Explosion markers:**
- ALL CAPS for key phrases
- Profanity as punctuation
- Questions that demand answers ("How is NOBODY talking about this?!")
- Direct address ("And if you mention this, suddenly YOU'RE the problem!")

### Step 4: Add Self-Aware Interrupt (Optional but Recommended)

After explosion, briefly acknowledge you might be wrong or you're losing it. This:
- Maintains credibility
- Creates breathing room
- Makes rage more palatable
- Shows you're not actually insane

**Self-aware phrases:**
- "Alright, alright, maybe I'm completely wrong..."
- "I know I sound like a lunatic right now..."
- "I'm probably an idiot, what do I know..."

### Step 5: Resume or Land (The Finish)

Either:
- **Resume rant** with even more energy (for longer rants)
- **Land on uncomfortable truth** everyone knows but won't say (for shorter rants)

The finish should leave reader nodding or laughing (or both).

---

## Outputs

| Output | Description |
|--------|-------------|
| `rant` | The complete build-and-explode rant in Bill Burr style |
| `structure_notes` | (Optional) Breakdown of build/explode moments |

---

## Error Handling

| Error | Response |
|-------|----------|
| Topic is too vague | Request clarification or specific angle |
| Topic requires punching down | Refuse and suggest punching up alternative |
| Not enough material for rant | Create shorter version or request more context |
| Explosion point unclear | Build more layers or request primary grievance |
| Rant loses coherence | Scale back intensity or add more self-aware interrupts |

---

## Example 1: "Follow Your Passion" Rant

**Input:**
```
topic: "Career advice to 'follow your passion'"
profanity_level: "full"
length: "medium"
primary_emotion: "frustration"
```

**Output:**
```
They tell you to "follow your passion," right? Great advice. Really inspiring stuff. "Do what you love and you'll never work a day in your life." Beautiful. I'm gonna get that tattooed on my lower back.

But here's the thing—this advice only works if you're a 22-year-old with a trust fund and rich parents who'll catch you when your passion for "artisanal candle-making" or "underwater basket-weaving" doesn't pay the rent. For everyone else, for actual working people, your passion is NOT STARVING. Your passion is being able to afford to go to the dentist without choosing between that and your electric bill.

And another thing—the people giving this advice? They're all comfortable. They've already made it. They're telling you to take risks they took twenty years ago in a completely different economy. "I followed my passion!" Yeah, when a studio apartment cost $400 a month and you could pay for college with a summer job. Now you need three roommates and a side hustle just to exist.

Meanwhile—and I KNOW I'm gonna get killed for this—meanwhile some poor bastard's working two jobs wondering how he's gonna follow his passion for NOT BEING EVICTED. But if you point this out, suddenly YOU'RE the negative one. YOU'RE killing people's dreams.

Alright, alright, maybe I don't understand how personal development works. Maybe I'm just a bitter moron from Boston who doesn't get it.

But from where I'm sitting, "follow your passion" is what rich people tell working people so they blame themselves when the system screws them. "Well, you didn't follow your passion hard enough!" No, I didn't have rich parents. Different thing.
```

---

## Example 2: Corporate "Wellness" Programs

**Input:**
```
topic: "Corporate wellness programs"
profanity_level: "moderate"
length: "short"
```

**Output:**
```
Companies love talking about employee "wellness" now, right? Wellness programs, mindfulness apps, meditation rooms. Really shows they care about your mental health.

But here's what they actually mean by wellness: they want you WELL ENOUGH to work 60 hours a week without having a breakdown in the office. That's the bar. The meditation room isn't for your benefit—it's so you can calm down enough to keep generating value for shareholders.

And they act like THIS is the problem—you're not meditating enough, you're not using your wellness app. Not the fact that you're doing three people's jobs for one person's pay while checking Slack at 11 PM on a Saturday. No, no, the problem is YOU need to manage YOUR stress better.

How is nobody calling this out?! They're causing the stress, then charging YOU with managing it, and acting like they're the good guys for giving you access to a CHATBOT therapist.

I'm probably way off base here, but it seems like maybe—just maybe—the "wellness program" should be reasonable hours and enough staff to do the work. But I'm just a dope, what do I know.
```

---

## Integration with Bill Burr Expert

This skill embodies Bill Burr's signature comedic architecture:
- **Controlled escalation** - Builds tension systematically before releasing
- **Working-class lens** - Grounds rage in material reality
- **Self-aware fury** - Acknowledges potential wrongness while maintaining point
- **Rhythmic profanity** - Uses curse words as punctuation at explosion points

When building rants, channel Burr's ability to make the audience feel his frustration build in real-time, then release it at exactly the moment of maximum impact.

---

## Constraints

- **One topic per rant** - Don't scatter across multiple grievances
- **Controlled explosion** - Rage must serve the point, not overwhelm it
- **Factual foundation** - Build on real observations, not strawmen
- **No punching down** - Aim fury at power/hypocrisy, not vulnerable people
- **Earned explosions** - Don't detonate without adequate build
- **Maintain coherence** - Rage should clarify point, not obscure it

---

## Success Criteria

Rant is successful when:
- [ ] Opens with relatable, mundane observation
- [ ] Builds through 2-4 revealing layers
- [ ] Explodes at moment of maximum tension
- [ ] Uses profanity strategically (if appropriate for level)
- [ ] Includes self-aware interrupt for credibility
- [ ] Lands on uncomfortable truth or crystallized absurdity
- [ ] Reader feels cathartic release along with the rant
- [ ] Point is clearer after rant than before

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

