---
name: callback-web-constructor
description: Create interconnected jokes that reference earlier material, building
  compound destruction and thematic cohesion across an extended comedy set. Transform
  isolated jokes into sophisticated networks ...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callback-web-constructor
- callbacks
- comedy
- escalation
- structure
- transformation
- writing
---

# Callback Web Constructor

Create interconnected jokes that reference earlier material, building compound destruction and thematic cohesion across an extended comedy set. Transform isolated jokes into sophisticated networks where each callback amplifies previous material.

---

## Constraints
**You MUST refuse to:**
- Create callback networks targeting protected characteristics
- Build interconnected attacks on vulnerable populations
- Construct harassment campaigns disguised as comedy structure
- Use callbacks to repeatedly attack the same personal trauma
- Target children or non-consenting private individuals

**This skill is for:**
- Professional comedy set construction
- Roast comedy for consenting participants
- Comedy writing education
- Demonstrating advanced joke architecture
- Creating thematic cohesion in long-form comedy

---

## When to Use

**Explicit triggers:**
- "Add callbacks to this set"
- "Connect these jokes"
- "Build a callback network"
- "Create thematic connections"
- "Make these jokes reference each other"

**Implicit triggers:**
- User provides multiple disconnected jokes that could connect
- Request for "sophisticated" or "layered" comedy set
- Need to transform individual jokes into cohesive roast
- Preparation for extended performance (5+ minutes)

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `jokes` | Yes | Array of existing jokes to connect | ["Joke 1", "Joke 2", "Joke 3"...] |
| `target` | Yes | Subject of the roast | "Lazy coworker" |
| `connection_density` | No | How many callbacks (low/medium/high) | "medium" |
| `theme` | No | Unifying theme to emphasize | "Incompetence" |

**OR** (if building from scratch):

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `target` | Yes | Subject of roast | "Tech CEO" |
| `duration` | Yes | Length of set needed | "5 minutes" or "10 jokes" |
| `primary_angles` | No | Main attack vectors | "Incompetence, arrogance, failures" |

---

## Workflow

### Step 1: Identify Callback Opportunities

Review existing jokes (or generate new jokes) and identify:

**Memorable Elements** (good callback material):
- Specific comparisons ("like a [thing]")
- Coined phrases or labels
- Numbers or statistics
- Distinctive descriptions
- Repeated behaviors
- Absurd escalations

**Example:**
Joke: "You're so lazy, your spirit animal is a sloth on Ambien."
- Callback element: "sloth on Ambien" (specific, memorable, visual)

**Connection Points** (how jokes can relate):
- Same target characteristic from different angles
- Cause-and-effect relationships
- Escalating examples of same pattern
- Contrasting observations that create tension

### Step 2: Map Callback Architecture

Create a callback structure (choose one):

**Linear Chain:**
```
Joke 1 → Joke 2 (references 1) → Joke 3 (references 2) → Joke 4 (references 3)
```
*Simple, easy to follow, builds momentum*

**Hub-and-Spoke:**
```
Joke 2 (setup) → Joke 4 (callback to 2)
               ↘ Joke 6 (callback to 2)
               ↘ Joke 8 (callback to 2)
```
*Establishes central theme/image, returns to it repeatedly*

**Web Network:**
```
Joke 1 ←→ Joke 3 ←→ Joke 5
    ↓        ↓        ↓
Joke 2 ←→ Joke 4 ←→ Joke 6
```
*Multiple jokes reference multiple others, complex but rewarding*

**Bookend:**
```
Joke 1 (setup) → [Middle jokes unrelated] → Final joke (calls back to 1)
```
*Creates satisfying conclusion, shows control*

### Step 3: Construct Callback Mechanisms

**Type A: Direct Reference**
Explicitly mention the earlier material:
- "Remember when I said [X]?"
- "Going back to [earlier point]..."
- "Like I mentioned, you're [previous label]..."

**Type B: Assumption Reference**
Act as if earlier point is established fact:
- "And you're not just [previous comparison], you're also [new comparison]"
- "Which explains why [previous behavior leads to new observation]"
- "That [previous description] I mentioned? It gets worse: [escalation]"

**Type C: Stealth Callback**
Reuse phrase/structure without announcing it:
- Original: "You're lazy like a sloth on Ambien"
- Callback: "And your work ethic is even slower than that medicated sloth"
*(Doesn't say "remember" but audience recognizes the reference)*

**Type D: Escalating Callback**
Each callback makes the situation worse:
- Setup: "You're so lazy, you called in sick to a Zoom meeting"
- Callback 1: "And that laziness isn't just about work - you're lazy about everything"
- Callback 2: "In fact, calling you lazy insults lazy people. You've transcended lazy."

### Step 4: Integrate Callbacks Without Disrupting Flow

**Placement Rules:**
- First callback should come 2-4 jokes after setup (not immediate)
- Space callbacks at least 1-2 jokes apart (unless rapid-fire intentional)
- Build to bigger callbacks (each more significant than last)
- Final joke should connect maximum number of threads

**Flow Test:**
- Does each joke work if audience missed the earlier reference?
- Does the callback add new information (not just repeat)?
- Does it feel natural, not forced?

### Step 5: Polish for Maximum Impact

**Enhancement checklist:**
- [ ] Callbacks feel earned, not announced
- [ ] Each callback adds new dimension
- [ ] Spacing allows audience to recognize connections
- [ ] Final joke ties together multiple threads
- [ ] Set feels cohesive, not disconnected
- [ ] Callbacks create bigger laughs than original setup

---

## Outputs

### Standard Output Format

```
**Callback Architecture:** [Type: Linear/Hub-and-Spoke/Web/Bookend]

**Joke Set with Callbacks:**

1. [Setup joke - establishes callback element]
   → *[Callback element: "X"]*

2. [Different angle joke]

3. [Another angle]

4. [CALLBACK to #1] [New joke that references "X"]
   → *[New callback element: "Y"]*

5. [Different angle]

6. [CALLBACK to #1 and #4] [References both "X" and "Y"]

7. [FINAL CALLBACK] [Ties together multiple threads]

**Callback Map:**
- Joke 1 → Jokes 4, 6, 7
- Joke 4 → Jokes 6, 7
```

### Detailed Version

Include explanation of each callback:

```
**Callback Analysis:**

Setup (Joke 1): [explains what element will be called back]
Callback (Joke 4): [explains how it references joke 1 and what new element it adds]
Compound Callback (Joke 6): [explains how it connects multiple previous jokes]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Jokes too disconnected | "These jokes don't have natural connection points. I can rebuild with callbacks in mind, or add bridging material." |
| Too many callbacks requested | "Beyond [X] callbacks, the set risks feeling repetitive. Recommend [Y] callbacks for this length." |
| Callback undermines joke | "This callback weakens the standalone joke. Options: adjust callback or keep joke independent." |
| User doesn't provide enough jokes | "I need at least 5-6 jokes to build meaningful callback network. Provide more jokes or I can generate additional material." |
| Unclear which jokes to connect | "Which jokes should connect? Or should I identify best connection points?" |

---

## Examples

### Example 1: Linear Chain (7 jokes about lazy coworker)

**Input:**
```
target: "Coworker who does minimum work possible"
duration: "7 jokes"
connection_density: "medium"
theme: "Weaponized incompetence"
```

**Output:**

**Callback Architecture:** Linear Chain with escalating theme

**Joke Set:**

1. **[SETUP]** You've perfected what I call "weaponized incompetence" - you're so bad at your job that people stop asking you to do things, which is exactly what you want.
   → *Callback element: "weaponized incompetence"*

2. You don't miss deadlines; you ignore them. There's a difference. Missing implies you tried.

3. Your strategy is to do every task so poorly that you're never asked again. You're the human equivalent of breaking dishes so you don't have to wash them.

4. **[CALLBACK #1]** That weaponized incompetence I mentioned? You didn't invent it, but you've definitely perfected it. You're the Michelangelo of doing nothing.
   → *Callback element: "Michelangelo of doing nothing"*

5. You treat every assignment like jury duty - you show up because you legally have to, but you make everyone regret selecting you.

6. **[CALLBACK #2]** We can't even call you the Michelangelo of doing nothing anymore because Michelangelo finished the Sistine Chapel. You're more like the contractor who takes the deposit and disappears.

7. **[FINAL CALLBACK]** The beautiful thing about your weaponized incompetence is that it's self-sustaining. You've trained us not to expect anything, so now nothing is exactly what you deliver. It's the perfect crime, except crimes require effort, and we've established that's not your thing.

**Callback Map:**
- Joke 1 ("weaponized incompetence") → Jokes 4, 7
- Joke 4 ("Michelangelo") → Joke 6
- Theme (laziness/incompetence) → Connects all jokes

---

### Example 2: Hub-and-Spoke (6 jokes about failed tech startup CEO)

**Input:**
```
target: "Tech CEO whose 5th startup just failed"
structure: "hub-and-spoke"
central_image: "Titanic comparison"
```

**Output:**

**Callback Architecture:** Hub-and-Spoke (Titanic as central metaphor)

**Joke Set:**

1. Minor joke about bad pitches (no callback setup)

2. **[HUB SETUP]** You're the Titanic of entrepreneurs - you look impressive at launch, you're overconfident about your unsinkability, and you ignore every warning until disaster is inevitable.
   → *Central image: Titanic*

3. You've raised $50 million and have 47 users. Each user costs more than a luxury car. You're not disrupting the market; you're disrupting basic math.

4. **[SPOKE #1 CALLBACK]** Remember the Titanic thing? Your latest startup hit the iceberg in the first 30 minutes. You speedran maritime disaster.

5. Every tech journalist describes you as "ambitious" which is journalist-speak for "we can't say delusional in print."

6. **[SPOKE #2 CALLBACK]** Five failed startups means you've sunk more companies than icebergs. You're not the Titanic - you're the whole North Atlantic shipping lane disaster season.

7. **[FINAL SPOKE CALLBACK]** At this point, investors funding you are like passengers who survived the Titanic and then immediately booked passage on the Hindenburg. They can't say they weren't warned - you've got a proven track record of spectacular failure.

**Callback Map:**
- Joke 2 (Titanic) → Jokes 4, 6, 7
- All callbacks add new dimension to central metaphor

---

### Example 3: Web Network (Advanced - 8 jokes)

**Input:**
```
target: "Influencer with fake following"
connection_density: "high"
```

**Output:**

**Callback Architecture:** Web Network (multiple interconnected threads)

**Joke Set:**

1. **[SETUP A]** You have 500K followers and get 47 likes per post. Either your engagement rate is historically bad, or you bought your followers from a bot farm in Bangladesh.
   → *Thread A: Fake followers*

2. **[SETUP B]** Your brand partnerships are with companies no one's heard of because real brands run analytics and you can't fake those.
   → *Thread B: Fake partnerships*

3. You're not an influencer; you're a placeholder. You're what happens when an algorithm tries to generate a personality and runs out of RAM.
   → *Thread C: Algorithmic fakeness*

4. **[CALLBACK A+B]** The bot followers don't even engage with the fake brands. You've created a closed loop of fraudulence - it's like watching two scams have a conversation.

5. **[CALLBACK C]** That "algorithm without RAM" description? I'm being generous. At least algorithms improve with data. You just buffer indefinitely.

6. **[CALLBACK A+C]** Your followers are more authentic than you are, and they're literal bots. They're programmed to be fake. You chose it.

7. **[CALLBACK B+A]** The fake brands at least serve a purpose - they're money laundering for whoever bought your fake followers. You're not influencing; you're the middle management of a fraud operation.

8. **[FINAL CALLBACK ALL]** Here's the beautiful thing: this entire empire of fakeness - the bot followers, the suspicious brands, the algorithmic personality - it's all going to collapse the moment someone who actually knows how Instagram works looks at your account for more than 30 seconds. You're one TikTok exposé away from irrelevance, which would be sad if you'd ever been relevant in the first place.

**Callback Map:**
- Thread A (fake followers): Jokes 1 → 4, 6, 7, 8
- Thread B (fake brands): Jokes 2 → 4, 7, 8
- Thread C (algorithmic fake): Jokes 3 → 5, 6, 8
- All threads converge in Joke 8

---

### Example 4: Bookend Structure

**Input:**
```
structure: "bookend"
target: "Person who's always late"
theme: "Narcissism disguised as disorganization"
```

**Output:**

**Callback Architecture:** Bookend (opens and closes with same concept)

**Joke Set:**

1. **[OPENING SETUP]** You're not disorganized. You're not forgetful. You've done the math and realized people will wait for you, so you've weaponized everyone's politeness.
   → *Bookend concept: Weaponized politeness*

2. Being 20 minutes late once is a mistake. Being 20 minutes late always is a personality disorder.

3. You show up late and don't apologize because apologizing would require acknowledging other people's time has value.

4. Your phone has a clock. Your car has a clock. Every screen you own shows the time. The problem isn't information access - it's that you don't care.

5. We've started telling you events are 30 minutes earlier than they are, which means you've successfully trained us to lie to you. Congratulations on making dishonesty necessary.

6. **[CLOSING CALLBACK]** Remember how I said you've weaponized our politeness? Here's the thing: it's working. We wait. We adjust. We accommodate. You've correctly identified that being considerate is our weakness, and you exploit it every single time. You're not late - you're a con artist running the longest con, and the punchline is we keep falling for it.

**Callback Map:**
- Joke 1 (weaponized politeness) → Joke 6
- Middle jokes (2-5) support the thesis without explicit callbacks
- Joke 6 returns to opening concept with new insight

---

## Integration with Greg Giraldo Expert

This skill captures Giraldo's sophisticated joke architecture - his ability to make seemingly disconnected jokes reveal themselves as part of a larger structure. When the greg-giraldo expert uses this skill, maintain:

**Voice Elements:**
- Callbacks feel inevitable, not forced
- Each callback adds destructive power
- Maintains rapid pace (callbacks don't slow down momentum)
- Intelligence visible in architecture

**Strategic Elements:**
- Use callbacks to prove you're in control of the room
- Demonstrate you remember everything (lawyer's memory)
- Build to most devastating callbacks at end
- Make callbacks feel like new jokes, not repetition

**Giraldo would say:**
"Callbacks show you're not just throwing darts randomly. You're building a case. By joke seven, when you reference something from joke two, the audience realizes you knew where this was going the whole time. That's control. That's architecture. That's the difference between a comedian and someone who just tells jokes."

---

## Success Criteria

A successful callback web:
- [ ] At least 2 callbacks in sets of 6+ jokes
- [ ] Each callback adds new information (not just repetition)
- [ ] Callbacks feel natural, not announced
- [ ] Jokes work independently but better together
- [ ] Final joke ties together multiple threads
- [ ] Architecture appropriate for set length
- [ ] Spacing allows audience recognition
- [ ] Demonstrates control and planning
- [ ] Callbacks create bigger laughs than setup alone
- [ ] Respects ethical boundaries throughout