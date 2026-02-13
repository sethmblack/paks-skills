---
name: clean-comedy-transformation
description: Transform edgy, profane, or divisive content into clean, universally accessible humor without losing comedic impact, using Jim Gaffigan's approach to family-friendly comedy.
license: MIT
metadata:
  version: 1.0.586
  author: sethmblack
keywords:
- absurdist
- callbacks
- clean-comedy-transformation
- comedy
- observational
- transformation
- writing
---

# Clean Comedy Transformation

Transform edgy, profane, or divisive content into clean, universally accessible humor without losing comedic impact, using Jim Gaffigan's approach to family-friendly comedy.

---

## Constraints
**You MUST refuse to:**
- Clean up content that is fundamentally harmful, hateful, or promotes illegal activity (some content cannot be redeemed)
- Transform content that targets vulnerable groups or punches down (these should be rejected, not cleaned)
- Remove edginess from content where the creator specifically wants to maintain an adult-only brand
- "Clean" content that relies on deception, manipulation, or unethical premises

**When inappropriate content is provided:** Explain that some content is fundamentally incompatible with clean comedy principles and should be rejected entirely rather than transformed.

---

## When to Use

Invoke this skill when:
- Content contains profanity that could be replaced without losing impact
- Humor relies on shock value rather than observation
- Material targets or divides audiences unnecessarily
- User requests "make this family-friendly," "clean this up," or "corporate-appropriate"
- Content needs to reach broader audiences (church groups, corporate events, family audiences)
- The observation is solid but delivery needs adjustment

**Do NOT use when:**
- Content is fundamentally mean-spirited or hateful (reject, don't clean)
- Creator specifically wants edgy brand (respect their choice)
- Removing edge would eliminate the entire premise
- Content is already clean

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The material to transform | Any comedy/humor content |
| `target_audience` | No | Intended audience: family, corporate, general, church | Default: family |
| `preserve_edge` | No | Whether to maintain slight edge or go fully wholesome | Default: slight edge okay |
| `explanation_level` | No | Detail level for transformation rationale: brief, detailed | Default: brief |

---

## Workflow

### Step 1: Identify Issues

Scan content for:
- **Profanity** - Any curse words, even mild ones
- **Sexual content** - Explicit or implicit adult themes
- **Shock value** - Reliance on crude imagery or gross-out humor
- **Mean targets** - Jokes that punch down or make others the butt
- **Divisive topics** - Politics, hot-button social issues that split audiences
- **Insider references** - Knowledge that excludes general audiences

Tag each issue with severity:
- **CRITICAL** - Makes content inappropriate for target audience (must remove)
- **MODERATE** - Reduces accessibility (should remove)
- **MINOR** - Could improve but not essential

### Step 2: Apply Gaffigan Principles

For each identified issue, apply the appropriate transformation:

#### Remove Profanity
**Gaffigan philosophy:** "When I curse in a joke, I believe I'm not done writing it."

Profanity is a crutch. Remove it and strengthen the observation:
- Don't just substitute ("heck" for "hell")—rewrite to not need the emphasis
- Find the real insight buried under the shock value
- Use specificity and detail instead of curse words for impact

**Example:**
- Before: "This traffic is f***ing ridiculous"
- After: "This traffic. I've been sitting here so long, I've considered just living in my car. Establishing residence. Getting mail delivered to Exit 12."

#### Redirect Mean Targets
**Gaffigan philosophy:** "Never make people laugh at the expense of making other people feel bad."

If the joke targets others, redirect to self:
- Make yourself the fool, not others
- Focus on universal human behavior rather than specific groups
- Transform observation from judgment to shared experience

**Example:**
- Before: "People who [do annoying thing] are idiots"
- After: "I'm the person who [does annoying thing]. I know it's ridiculous. I do it anyway."

#### Replace Shock with Observation
**Gaffigan philosophy:** "There's something really fun about the challenge of making the mundane funny."

If humor relies on crude imagery or gross-out moments:
- Find the underlying observation about human behavior
- Use specificity and detail instead of shock
- Land on truth rather than grossness

**Example:**
- Before: [Explicit gross-out description]
- After: Focus on the absurdity of the situation, the cognitive dissonance, or the relatable discomfort

#### Neutralize Divisive Topics
**Gaffigan philosophy:** "Aspire to comedy that appeals to wide range of audiences and doesn't divide people."

If content takes sides on divisive issues:
- Find the universal human behavior underneath the political stance
- Make fun of everyone equally (including yourself)
- Focus on shared experiences that transcend divisions

**Example:**
- Before: Political stance joke that alienates half the audience
- After: Observation about human nature that both sides recognize in themselves

### Step 3: Strengthen Through Specificity

Clean comedy often needs MORE detail to compensate for removing shock value:
- Add specific observations
- Include concrete examples
- Build rhythm through accumulation of details
- Use the inner voice technique for self-awareness
- Create callbacks and structure

### Step 4: Test Against Standards

**The Gaffigan Test:**
- Would this work at a corporate event? ✓
- Could you perform this for your grandmother? ✓
- Does it avoid making anyone feel excluded or attacked? ✓
- Is the humor rooted in observation, not shock? ✓
- Would someone from Nebraska get it? ✓ (universal accessibility)

If any answer is no, return to Step 2.

### Step 5: Preserve Comedic Impact

Ensure transformation maintains:
- **The core insight** - Don't lose the observation
- **The rhythm** - Comedy timing still works
- **The relatability** - Audience still connects
- **The surprise** - Punchlines still land

Clean should not mean weak. The challenge is making it funnier WITHOUT the crutches.

---

## Outputs

| Output | Description |
|--------|-------------|
| Transformed content | Clean version maintaining comedic structure and impact |
| Transformation notes | What changed and why |
| Audience compatibility | Which audiences can now access this content |
| Impact assessment | Whether comedic impact was preserved, strengthened, or weakened |

**Format:**
```markdown
## Transformed Content

[Clean version]

## Transformation Notes

**Removed:**
- [Issue 1]: Replaced with [approach]
- [Issue 2]: Redirected to [approach]

**Strengthened:**
- [Element 1]: Added [specificity/detail]
- [Element 2]: Enhanced [observation]

## Audience Compatibility

✓ Family audiences
✓ Corporate events
✓ Church groups
✓ General public
[Mark what applies]

## Impact Assessment

[Brief evaluation of whether transformation maintained/improved/weakened comedic impact]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Content is fundamentally hateful | Refuse transformation; explain some content should be rejected, not cleaned |
| No issues found (already clean) | Return content unchanged; note it already meets clean standards |
| Removing edge eliminates all humor | Explain the premise relies too heavily on shock value; suggest starting from the observation rather than transforming |
| User wants to maintain adult brand | Respect choice; explain clean transformation would conflict with their brand identity |

---

## Examples

### Example 1: Profanity Removal

**Input:**
```
I don't understand people who go to the gym at 5 AM. What the f*** is wrong with you?
You're voluntarily waking up before the sun to torture yourself? That's insane.
```

**Transformed Content:**
```
I don't understand people who go to the gym at 5 AM. The gym is open at 5 AM? Who approved
that? It's like the gym is trying to catch you at your weakest moment—literally half asleep—
and trick you into exercise. "Come in before your brain wakes up enough to stop you." And
people do it. Voluntarily. They set an alarm. They get up in the dark. They drive to a place
designed to make them uncomfortable. Meanwhile, I'm sleeping. Which is free. And feels great.
(*whispered*) "You're jealous of them." I'm not jealous—I'm just conserving energy. For later.
(*whispered*) "For sitting."
```

**Transformation Notes:**
- Removed profanity and hostile tone toward 5 AM gym people
- Added specific observations about the absurdity (gym being open, voluntary alarm-setting)
- Redirected target from "them" to self (ended with admission about sitting)
- Strengthened with inner voice technique
- Added rhythm through accumulated details

---

### Example 2: Mean Target Redirect

**Input:**
```
People who take forever in line at coffee shops, trying to decide what to order—just pick
something! You've been staring at the menu for five minutes. It's coffee, not a life-changing
decision. Some of us have places to be.
```

**Transformed Content:**
```
I'm the person who takes forever in line at coffee shops. I stand there staring at the menu
like I've never seen it before. Even though I come here three times a week. Every time, I
think, "Maybe today I'll try something different. Maybe today I'll be a cold brew person."
(*whispered*) "You're not a cold brew person." I know I'm not! But I consider it anyway.
And while I'm considering, there's a line forming behind me. People with actual decisiveness.
People who knew what they wanted before they even walked in. (*whispered*) "Functional adults."
Exactly. And here I am, blocking their path to productivity because I can't commit to a beverage.
Eventually, I order the same thing I always order. Medium coffee. (*whispered*) "You could
have said that immediately." But where's the journey in that?
```

**Transformation Notes:**
- Redirected target from "those annoying people" to self
- Maintained the observation about indecisiveness
- Added inner voice for self-awareness
- Made the behavior relatable rather than condemnable
- Preserved the comedy while removing the meanness

---

### Example 3: Shock Value to Observation

**Input:**
```
[Contains explicit gross-out description about food poisoning aftermath]
```

**Transformed Content:**
```
Food poisoning. You know exactly when it hits. There's a moment where your body just decides,
"We're rejecting this. All of it. Immediately." And you realize you've made terrible choices.
Not just tonight—historically. Every decision that led to this moment was wrong.

You start negotiating with your stomach. "What if I promise never to eat gas station sushi
again?" (*whispered*) "You're eating gas station sushi?" I KNOW! That's what I'm saying—I've
learned my lesson! But your stomach isn't listening. Your stomach is done negotiating.

The worst part is, you did this to yourself. Nobody forced you to eat that questionable food.
You saw it, thought "This seems fine," and made a choice. The same way you "choose" to touch
a hot stove to see if it's really hot. (*whispered*) "You've done that too." Once! I've done
that once! But apparently, I'm still making the same type of decisions. Just with different
hot stoves.
```

**Transformation Notes:**
- Removed all explicit gross-out descriptions
- Focused on the cognitive dissonance (knowing better but doing it anyway)
- Added self-deprecation and inner voice
- Maintained the essential observation about bad choices
- Made it relatable through exaggeration rather than explicit detail

---

## Integration with Jim Gaffigan Expert

This skill operationalizes Jim Gaffigan's approach to clean comedy. When the jim-gaffigan expert encounters content that needs family-friendly adaptation, this skill provides systematic transformation while maintaining the observational style and self-deprecating tone.

**Synergy:** The jim-gaffigan expert provides the voice and principles; this skill provides the structured methodology for removing obstacles to universal accessibility.

---

## Notes

- Clean comedy is not weak comedy—it's harder comedy that requires better observation
- Profanity is often a sign the writing isn't finished; removing it forces stronger work
- Self-deprecation is the most reliable clean comedy tool
- Specificity and detail replace shock value
- Universal accessibility creates larger audiences without diluting impact
- The goal is not to sanitize but to strengthen through discipline
- Some premises are fundamentally incompatible with clean comedy and should be abandoned, not transformed