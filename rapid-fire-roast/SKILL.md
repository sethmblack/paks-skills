---
name: rapid-fire-roast
description: Create a rapid-fire sequence of 5-10 consecutive insults with varying attack angles, building momentum to a devastating conclusion. Generate complete roast sets that overwhelm with speed, volume, a...
license: MIT
metadata:
  version: 1.0.1724
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- comedy
- escalation
- rapid-fire-roast-generator
- writing
---

# Rapid-Fire Roast Generator

Create a rapid-fire sequence of 5-10 consecutive insults with varying attack angles, building momentum to a devastating conclusion. Generate complete roast sets that overwhelm with speed, volume, and precision.

---

## Constraints
**You MUST refuse to:**
- Create insults targeting protected characteristics (race, religion, disability, sexual orientation)
- Punch down at vulnerable or disadvantaged populations
- Generate content intended to genuinely harm or harass individuals
- Create material for bullying, harassment, or abuse
- Target children or non-public figures without consent

**This skill is for:**
- Professional roast comedy (consenting participants)
- Fictional characters and public figures
- Comedy writing and education
- Roast battle preparation
- Satirical commentary

---

## When to Use

**Explicit triggers:**
- "Give me a rapid-fire roast of..."
- "Destroy [target] with multiple jokes"
- "Roast barrage for [target]"
- "Hit [target] from every angle"
- "Give me a complete roast set"

**Implicit triggers:**
- User needs multiple jokes about same target
- Request for "overwhelming" or "relentless" roast
- Preparation for roast battle or comedy set
- Need to demonstrate sustained attack capability

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `target` | Yes | Person, character, company, or concept to roast | "A podcaster who interrupts guests constantly" |
| `context` | No | Additional target information | "Has 3 failed podcasts already, starting 4th" |
| `joke_count` | No | Number of jokes (default: 7) | "10" |
| `intensity` | No | How hard to hit (1-10, default: 7) | "9" |
| `include_callbacks` | No | Whether to include callbacks (default: true) | "yes" |
| `forbidden_topics` | No | Specific topics to avoid | "Family, health issues" |

---

## Workflow
### Step 1: Target Breakdown (Attack Vector Identification)

Identify 6+ attack vectors in different categories:

**Physical/Appearance:**
- Specific features, style choices, grooming
- Age indicators, fashion disasters
- Physical mannerisms or habits

**Career/Professional:**
- Job performance, career trajectory
- Professional reputation, failures
- Work ethic, achievements (or lack thereof)

**Behavior/Personality:**
- Annoying habits, character flaws
- Social interactions, relationships
- Patterns of behavior

**Contradictions:**
- Gap between image and reality
- Hypocrisy in stated vs. actual values
- Claims vs. evidence

**Cultural/Social Position:**
- What they represent culturally
- Social status, aspirations vs. reality
- Generational or demographic patterns

**Absurd Comparisons:**
- What they look/sound/act like
- Historical or fictional parallels
- Unlikely combinations that fit perfectly

### Step 2: Strategic Joke Sequencing

Order jokes for maximum impact using this structure:

**Joke 1-2: ESTABLISH DOMINANCE**
- Open with your strongest material
- Set aggressive tone immediately
- Make it clear you're in control

**Joke 3-5: VARY ATTACK ANGLES**
- Shift between different categories
- Maintain surprise through variety
- Build momentum through accumulation
- Include at least one intellectual angle

**Joke 6-7: BUILD TO BIGGER BLOWS**
- Each joke slightly harder than previous
- Increase absurdity or darkness
- Add callback to earlier material
- Stack multiple layers per joke

**Joke 8-10 (if requested): KILL SHOT SEQUENCE**
- Most devastating observation
- Callback that connects multiple jokes
- Final absurd escalation
- End with mic-drop moment

### Step 3: Construct Individual Jokes

Each joke should be:
- **Economical:** No wasted words, maximum impact per syllable
- **Specific:** Avoid generic insults anyone could use
- **Varied:** Different structure/length than previous joke
- **Building:** Connect to overall momentum

**Joke Structure Variety:**
- Simple declaration: "You're X."
- Comparison: "You look/sound/act like X."
- Observation: "You [behavior] like [comparison]."
- Question setup: "You know what's [adjective] about you? [Answer]."
- Self-aware: "I'm not saying [X]... wait, yes I am."

### Step 4: Integrate Callbacks

**First Reference (Joke 2-4):**
Establish something memorable that can be called back:
- Specific comparison
- Coined phrase
- Numerical claim
- Distinctive description

**Callback (Joke 5-8):**
Reference the earlier material while adding new information:
- "Remember when I said X? Well, [new related attack]."
- "You're not just X, you're also Y."
- "[New target detail] makes that [earlier comparison] seem generous."

**Callback Web (Advanced):**
Multiple jokes reference each other, creating interconnected network.

### Step 5: Rhythm and Pacing

**Vary sentence length:**
- Short punchy lines: "You're lazy. And stupid. And lazy about being stupid."
- Medium development: "You dress like you've given up on being perceived as a sexual being."
- Longer builds: Full compound insults with multiple clauses

**Maintain speed:**
- Minimize setup time
- Get to punch quickly
- Keep audience off-balance
- No pausing for applause breaks (push through)

---

## Outputs

### Standard Format (7 jokes)

```
1. [Opening power shot - strongest material]
2. [Different angle, establish variety]
3. [Intellectual angle or unexpected reference]
4. [Callback setup - memorable phrase/image]
5. [Different angle, building intensity]
6. [Callback to #4 + new attack]
7. [Kill shot - most devastating or absurd]
```

### Extended Format (10 jokes)

Add three more jokes between #7 and final kill shot:
- Explore additional angles
- Add secondary callback
- Increase absurdity progressively

### Presentation Options

**As numbered list:**
```
1. First joke
2. Second joke
...
```

**As continuous paragraph:**
```
First joke. Second joke. Third joke...
```

**As script format:**
```
[Aggressive opening]
You're X. You're also Y. And here's what makes it worse: Z...
[Build momentum]
[Kill shot]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient target info | Ask: "Tell me more about [target] so I can find enough attack angles for [X] jokes." |
| Requested joke count too high | Warn: "I can generate [X] quality jokes. Beyond that risks repetition. Proceed?" |
| Target is vulnerable population | Refuse: "I can't roast [vulnerable group]. Try public figure or consenting participant." |
| Jokes feel repetitive | Restart with more diverse attack vectors; ensure each angle is genuinely different |
| User wants harder hits | Ask: "Increase intensity to [X+1]? This will get darker." |
| Callback request but no good setup | Create setup in joke 2-3, callback in joke 6-7 |

---

## Examples

### Example 1: Podcaster (7 jokes, intensity 8)

**Input:**
```
target: "Podcaster who interrupts guests constantly"
context: "Has 3 failed podcasts, starting 4th one"
joke_count: 7
include_callbacks: yes
```

**Output:**

1. You've failed at three podcasts already, which makes you the Afghanistan of audio content - everyone thinks they can make it work, and everyone's wrong.

2. You interrupt guests so much, you're not conducting interviews - you're holding people hostage while you perform a monologue you're too insecure to do alone.

3. Starting your fourth podcast after three failures isn't persistence, it's the Dunning-Kruger effect in real time. You're too incompetent to realize you're incompetent.

4. Your guests book your show hoping to promote something, but they leave just hoping you'll shut up long enough for them to finish a sentence. You're not a host - you're an obstacle.

5. You call it "dynamic conversation" but it's really just you treating other people's expertise as a jumping-off point for your uninformed opinions. You're like Wikipedia if Wikipedia could interrupt itself.

6. Remember how I said you're an obstacle? You're actually worse than that. You're an obstacle that thinks it's helping. You're the human equivalent of Clippy: "It looks like you're trying to make a point - can I stop you and make it worse?"

7. The fact that you're starting a fourth podcast proves you've learned nothing. You're speedrunning irrelevance. By podcast six, you'll just be talking to yourself in a closet, which honestly is what you wanted all along.

**Analysis:**
- Joke 1: Career failure (strong opening)
- Joke 2: Behavior pattern (interrupting)
- Joke 3: Intellectual angle (Dunning-Kruger)
- Joke 4: Callback setup ("obstacle")
- Joke 5: Different angle (Wikipedia comparison)
- Joke 6: Callback with escalation (Clippy)
- Joke 7: Kill shot (predicting worse future)

### Example 2: Tech Startup CEO (5 jokes, intensity 7)

**Input:**
```
target: "Tech startup CEO with more funding than users"
joke_count: 5
intensity: 7
```

**Output:**

1. You've raised $50 million and have 47 users, which means each user cost about a million dollars. You're not disrupting anything except investor bank accounts.

2. Your pitch deck has more slides than your app has daily active users. You've perfected the art of selling a solution to a problem nobody has.

3. You talk about "changing the world" but you can't even change your user count from two digits to three. You're not a visionary - you're a guy in a hoodie with PowerPoint.

4. Every tech journalist calls you "a founder to watch" which is journalist-speak for "we've been paid to cover this and we're confused too."

5. In five years, you'll be a case study in business school titled "How Venture Capital Enables Confident Mediocrity" - congratulations, you're educational.

### Example 3: Self-Aware Dark Roast (6 jokes, intensity 9)

**Input:**
```
target: "Influencer who faked philanthropy for content"
context: "Got exposed, doubled down instead of apologizing"
joke_count: 6
intensity: 9
```

**Output:**

1. You faked charity work for Instagram engagement, which makes you the spiritual successor to scam televangelists, except they at least had the decency to wear nice suits while stealing from people.

2. When you got caught, you didn't apologize - you posted a 'statement' explaining why you did nothing wrong. You're not just shameless; you're educationally shameless, teaching a masterclass in how to be a sociopath with good lighting.

3. You literally staged photos of yourself 'helping' people, which means you looked human suffering in the face and thought "this is my brand opportunity." That's not influencer behavior - that's serial killer origin story shit.

4. Your followers defended you by saying "at least they raised awareness." You know what else raises awareness? Actual charity. But that doesn't get you sponsored posts from fashion brands, does it?

5. You're proof that social media has created a generation that believes documentation of virtue is the same as actual virtue. You're not an influencer - you're a warning label that somehow got verified.

6. Here's what nobody's saying: You're going to keep doing this because it works. You lost 10% of followers but kept 90% and gained controversy clout. You've learned that authenticity doesn't matter if your audience is too stupid or complicit to care. Congratulations - you've figured out we're in hell and decided to monetize it.

**Analysis:**
- Opens with strong comparison (televangelists)
- Escalates darkness (sociopath, serial killer)
- Self-aware framing ("Here's what nobody's saying")
- Builds to nihilistic conclusion
- Each joke harder than previous

---

## Integration with Greg Giraldo Expert

This skill captures Giraldo's signature rapid-fire delivery and momentum building. When the greg-giraldo expert uses this skill, maintain his characteristics:

**Voice Elements:**
- Economical language (no wasted words)
- Aggressive forward momentum
- Intelligence in service of brutality
- Self-aware about the darkness

**Strategic Elements:**
- Open with strongest material
- Vary attack angles constantly
- Build to bigger blows
- End with kill shot

**Giraldo would say:**
"The key to rapid-fire is you don't give them time to defend. By the time they've processed joke three, you're hitting them with joke six. It's overwhelming by design. You're not having a conversation - you're conducting an airstrike."

---

## Success Criteria

A successful rapid-fire roast:
- [ ] Opens with strong material (not saving best for last)
- [ ] Attacks from at least 5 different angles
- [ ] Varies joke structure and length
- [ ] Includes at least one intellectual reference
- [ ] Contains at least one callback (if 6+ jokes)
- [ ] Builds momentum throughout
- [ ] Ends with most devastating or absurd material
- [ ] Maintains speed (economical language)
- [ ] Each joke could stand alone but works better in sequence
- [ ] Respects ethical boundaries (no punching down)