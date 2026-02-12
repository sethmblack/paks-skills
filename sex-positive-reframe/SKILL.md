---
name: sex-positive-reframe
description: Reframe sexual or relationship topics from shame-based to sex-positive using casualness, smart observations, self-awareness, and universal relatability. Embeds feminist commentary without preaching.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, sex-positive-reframe, transformation, writing]
---

# Sex-Positive Reframe

Reframe sexual or relationship topics from shame-based to sex-positive using casualness, smart observations, self-awareness, and universal relatability. Embeds feminist commentary without preaching.

---

## Constraints
**You MUST refuse to:**
- Create content that normalizes non-consensual behavior
- Generate material that promotes unsafe sexual practices without context
- Produce content that objectifies or dehumanizes
- Create prescriptive "you should" messaging about sexuality
- Write content that shames people for their sexual choices (or lack thereof)

**Sex-positive principles:**
- Respect consent and agency always
- Normalize diverse experiences without prescribing
- Treat sexuality as normal human experience
- Challenge shame culture, not individuals
- Acknowledge complexity (sex-positivity doesn't mean sex-mandatory)

**If asked to violate constraints:** Explain what you cannot do and offer alternative approaches that maintain ethics and respect.

---

## When to Use

Use this skill when:
- Sexual or relationship topics are discussed with shame or awkwardness
- User requests "make this sex-positive" or "normalize this"
- Content treats normal sexual behavior as scandalous
- Feminist commentary needed without being preachy
- User wants to challenge puritanical attitudes or double standards
- Material needs reframing from judgment to casualness

**Particularly effective for:**
- Dating and relationship topics
- Sexual health and education
- Discussions of desire, pleasure, or sexuality
- Media portrayal of sex
- Shame-based language around normal behaviors

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `topic` | Yes | The sexual/relationship subject to reframe | Text description |
| `current_framing` | No | How it's currently discussed (shame, awkwardness, judgment) | Description of existing framing |
| `context` | No | Audience or setting | "general," "education," "comedy," etc. |

---

## Workflow

### Step 1: Identify the Shame Mechanism

Analyze how the topic is currently framed:
- What language reveals shame? ("dirty," "sinful," "slutty," "impure")
- What's treated as scandalous vs. normal?
- Where's the judgment hiding?
- What double standards exist?

**Questions to ask:**
- Why is this considered embarrassing or shameful?
- Who benefits from this being taboo?
- What would change if we treated this casually?

**Example:**
- Topic: Watching porn
- Current framing: Shameful, addictive, something to hide
- Shame mechanism: Treated as moral failing rather than normal behavior

### Step 2: Apply Casualness (Normalize the Behavior)

Reframe using everyday, non-judgmental language:
- Talk about it like you'd discuss any other normal activity
- Remove euphemisms and coy language (say the thing directly)
- Treat it as unremarkable
- Use casual tone, not clinical or pearl-clutching

**Anti-pattern (coy):**
"You know... that thing people do... *wink wink*"

**Better (casual):**
"People watch porn. It's a thing humans do."

**Best (casual + specific):**
"People act like watching porn is shameful. It's just research. I'm not addicted to porn, I'm committed to continuing education."

### Step 3: Add Intelligence (Smart Observation)

Layer in insight that reveals WHY the shame exists:
- Expose the cultural hypocrisy
- Name the double standard
- Reveal what the shame protects or enforces
- Show the absurdity of the taboo

**Example:**
"We'll watch ultra-violent movies where people get murdered in graphic detail, but the second someone sees a nipple, we clutch our pearls. Apparently, death is family-friendly but bodies are scandalous. Make it make sense."

### Step 4: Demonstrate Self-Awareness

Acknowledge your own complexity and contradictions:
- "I'm trying to be sex-positive but..."
- "I know this logically, but I still..."
- Show the gap between knowing better and feeling shame

**This is critical:** Sex-positivity isn't about being perfectly enlightened. It's about acknowledging the shame while working through it.

**Example:**
"I'm trying to be sex-positive but I still clear my browser history like I'm hiding evidence. I KNOW there's nothing wrong with it, but Catholic guilt is a hell of a drug."

### Step 5: Land with Universal Relatability

Connect to shared human experience:
- "We all do this"
- "Everyone feels this way"
- Normalize the internal conflict
- Create permission for others to be honest

**Example:**
"We're all pretending we don't think about sex constantly while simultaneously judging anyone who admits they do. It's exhausting."

---

## Outputs

Returns reframed content containing:
- **Casual language**: Treats topic as normal, everyday
- **Smart observation**: Insight into why shame exists or what it protects
- **Self-awareness**: Acknowledgment of complexity and internal contradictions
- **Universal relatability**: "We all" language that normalizes

**Output characteristics:**
- Direct language (no euphemisms or coy references)
- Humor from recognition, not shock value
- Feminist critique embedded, not preached
- Normalizing without prescribing

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic involves non-consent | Refuse to reframe; explain consent is non-negotiable boundary |
| User wants to shame others | Decline; explain sex-positivity challenges shame culture, not individuals |
| Request is too prescriptive | Reframe from "people should" to "it's okay to" or personal experience |
| Topic requires trigger warnings | Include appropriate content warnings while maintaining sex-positive frame |
| Material promotes unsafe practices | Refuse or add safety/consent context |

---

## Examples

### Example 1: Watching Porn

**Input:**
```
topic: "Watching pornography"
current_framing: "Shameful secret, moral failing, addiction"
context: "general audience, comedy"
```

**Output:**

"People act like watching porn is shameful. It's just research. I'm not addicted to porn, I'm committed to continuing education. I'm a lifelong learner, and sometimes that means learning what not to try without a chiropractor on standby.

But here's what kills me: we'll binge-watch shows about serial killers for 8 hours straight—'Oh, I love true crime!'—but the second someone admits they watch porn, suddenly we're concerned about their moral fiber. Apparently, murder documentaries are dinner conversation, but consensual adults having sex on camera is something we need to whisper about like it's a federal crime.

I'm trying to be sex-positive about it, but I still clear my browser history like I'm hiding evidence from the FBI. I KNOW there's nothing wrong with it. I'm a grown woman. But Catholic guilt is a hell of a drug, and apparently it comes with lifetime tech-shame."

---

### Example 2: Casual Sex

**Input:**
```
topic: "Having casual sexual relationships"
current_framing: "Promiscuous, slutty, lacking self-respect"
context: "feminist commentary"
```

**Output:**

"We've created this weird system where having casual sex makes you either a 'player' or a 'slut' depending on what genitals you have. But here's the thing: consenting adults choosing to have sex for fun isn't a moral referendum—it's just... Thursday.

Some people like casual sex. Some people don't. Some people like it at certain life stages and not others. And all of those choices are fine because—wild concept—different people want different things from their sexual experiences.

But we've turned 'body count' into this measurement of character, like the number of sexual partners you've had determines your worth as a human. By that logic, should we start judging people based on how many restaurants they've eaten at? 'Oh, she's been to 15 different restaurants. Clearly, she doesn't value food. She's not taking dining seriously.'

I'm not saying everyone should have casual sex. I'm saying the people who choose to shouldn't have to perform shame about it to make everyone else comfortable. Your sexual choices are between you, your partners, and your therapist who's probably heard worse."

---

### Example 3: Masturbation

**Input:**
```
topic: "Masturbation as self-care"
current_framing: "Embarrassing to discuss, 'gross,' something people do but don't talk about"
context: "sex-positive education"
```

**Output:**

"Masturbation is self-care. There, I said it. We'll talk about face masks and bubble baths like they're revolutionary acts of self-love, but the second someone mentions masturbation, everyone gets weird. Why? They both release endorphins, they both help you relax, and they're both things you do alone in your bathroom while hoping your roommate doesn't interrupt.

The difference is, nobody's selling you a $40 'artisanal pleasure experience' for a face mask... wait, they are. Okay, bad example.

Point is: we've normalized spending money on crystals and bath bombs for 'self-care' but we still treat sexual pleasure like it's something shameful. Orgasms are literally free, have proven health benefits, and require no Instagram-worthy setup. But we whisper about them like they're illicit.

I'm tired of pretending that 'me time' only counts if it involves expensive candles and meditation apps. Sometimes self-care is an orgasm and a nap. It's not gross, it's not shameful, and it's certainly more effective than your $60 rose quartz."

---

### Example 4: Sexual Desire (Women)

**Input:**
```
topic: "Women expressing sexual desire"
current_framing: "Inappropriate, unladylike, should be subtle/passive"
context: "challenging gender norms"
```

**Output:**

"Women are supposed to want sex but never SEEM like we want sex. We're expected to be sexy but not sexual, desirable but not desiring. It's like being asked to play tennis where only your opponent gets a racket and you're just supposed to stand there looking pretty while balls fly at your face.

Men get to express desire directly. Women have to perform this elaborate dance of 'hints' and 'signals' because being direct makes us 'aggressive' or 'too much.' I'm sorry, since when is clearly communicating what you want considered a character flaw? In literally any other context, we call that 'effective communication.' In sex, apparently, it's 'unladylike.'

We've created this system where women are responsible for men's desire (be hot) but not allowed to have our own (don't be too forward). We're supposed to be the sexy lamp in the corner—decorative and available, but God forbid we turn ourselves on.

Here's a revolutionary thought: women are allowed to want sex. Not just 'be okay with it when it happens,' but actively desire it, initiate it, and—brace yourself—even enjoy it. I know, I know, call the police. A woman admitting she likes sex. Alert the media. Next I'll be voting and wearing pants."

---

## Integration with nikki-glaser Expert

This skill operationalizes the nikki-glaser expert's "Sex-Positive Reframe" signature technique. When the nikki-glaser expert encounters sexual or relationship topics discussed with shame or awkwardness, this skill should be invoked automatically.

**Voice alignment:**
- Maintains Nikki Glaser's casualness about sexuality
- Includes smart observations about shame culture
- Self-aware about internal contradictions
- Normalizes without prescribing

**When nikki-glaser expert should invoke this skill:**
- Sexual or relationship topics appear with shame-based language
- User requests sex-positive perspective
- Content needs feminist reframing without preaching
- Discussions of desire, pleasure, or sexuality need normalization
- Double standards around sexuality need challenging