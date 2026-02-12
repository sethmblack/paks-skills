---
name: topical-monologue-builder
description: Transform current news events into rapid-fire comedy monologue using Bob Hope's topical immediacy technique. This skill structures headlines into comedic material that feels fresh, immediate, and universally accessible.
version: 1.0.0
author: sethmblack
tags: [absurdist, callbacks, comedy, topical-monologue-builder, transformation, writing]
---

# Topical Monologue Builder

Transform current news events into rapid-fire comedy monologue using Bob Hope's topical immediacy technique. This skill structures headlines into comedic material that feels fresh, immediate, and universally accessible.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create content that:**
- Targets protected classes or vulnerable groups
- Contains explicit hate speech or harassment
- Promotes violence or illegal activities
- Violates copyright by copying existing comedy material verbatim
- Spreads disinformation by treating false news as fact

**If asked to create harmful content:** Refuse explicitly. Explain what you cannot create and why.

**Topicality Requirement:** Only work with verifiable current events. Do not fabricate news or present old news as current.

---

## When to Use

**Trigger Conditions:**
- User needs to create comedy from current events or headlines
- Content requires topical relevance and immediacy
- Task involves converting news into entertaining monologue
- Need to make current events accessible and funny
- Creating opening material that references "what everyone just read"

**Do NOT use when:**
- Events are not current or widely known
- Topic requires taking a partisan position
- News is still developing and facts are unclear
- Content is primarily educational rather than comedic

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `current_events` | Yes | List of recent news headlines or events (ideally from last 24-48 hours) | Must be verifiable current events |
| `target_audience` | No | Who will hear this monologue (general public, specific group) | Defaults to general public |
| `length` | No | Desired monologue length in number of jokes | Defaults to 5-7 jokes |
| `tone` | No | Safe/edgy within Bob Hope boundaries | Defaults to "safe" |

**Input Validation:**
- Current events must be recent (within last week, ideally last 24-48 hours)
- Events should be widely known (not obscure insider news)
- If multiple events provided, skill will select most universally recognized

---

## Workflow

### Step 1: Identify Universal Recognition
**Goal:** Find the headline everyone already knows about.

**Process:**
1. Review provided current events
2. Ask: "What story has everyone seen this morning?"
3. Select events with broadest public awareness
4. Prioritize stories with inherent absurdity or irony

**Output:** 2-3 news stories with universal recognition

---

### Step 2: Find the Relatable Angle
**Goal:** Discover what everyone is thinking but not saying.

**Process:**
1. For each selected story, identify the absurd element
2. Ask: "What would someone say about this at dinner?"
3. Find the human, relatable reaction (not policy analysis)
4. Locate where the story connects to everyday experience

**Output:** The "conversational angle" for each story

---

### Step 3: Structure the Cascade
**Goal:** Arrange jokes for rapid-fire delivery.

**Process:**
1. Order jokes from strongest opener to strong closer
2. Add natural transitions between stories
3. Ensure each joke sets up the next
4. Plan for no pauses—continuous flow
5. Include at least one self-deprecating angle (golf, age, career)

**Bob Hope Formula:**
```
[Self-deprecating opener] → [Current Event #1] → [Quick transition] →
[Current Event #2] → [Bipartisan hit if political] → [Call-back or closer]
```

---

### Step 4: Write with Immediacy
**Goal:** Make every joke feel five minutes old.

**Process:**
1. Use present tense and recent timeframes ("this morning," "today," "just now")
2. Reference details everyone saw (poll numbers, quotes, images)
3. Avoid explanation—assume audience knows the story
4. Keep setups minimal (2-3 words) since audience has context
5. Hit punchline fast

**Immediacy Markers:**
- "I see..." / "I saw this morning..."
- "Did you hear about..."
- "They just announced..."
- "You probably saw..."

---

### Step 5: Deliver with Timing
**Goal:** Indicate rhythm for rapid-fire delivery.

**Process:**
1. Mark natural beats (where punchline lands)
2. Indicate where jokes chain without pause
3. Show where brief audience reactions expected
4. Suggest delivery pace (fast, faster, brief pause, continue)

**Format:**
```
[Setup] → [PUNCHLINE] → [immediate transition] → [Setup] → [PUNCHLINE]
```

---

## Outputs

**Deliverable:** A complete topical monologue with:
1. **Opening hook** - Self-deprecating or attention-grabbing entry
2. **3-7 topical jokes** - Structured in rapid-fire cascade
3. **Transitions** - Natural flows between stories
4. **Timing notes** - Guidance on pacing and delivery
5. **Closer** - Strong ending or callback

**Format Example:**
```markdown
## Topical Monologue (Bob Hope Style)

**OPENER (self-deprecating):**
[Joke about self]

**HEADLINE #1:**
[Setup] → [PUNCHLINE]

**TRANSITION & HEADLINE #2:**
[Quick connecting phrase] → [Setup] → [PUNCHLINE]

**POLITICAL BIPARTISAN HIT:**
[Setup that hits both sides] → [PUNCHLINE]

**CLOSER:**
[Callback or final observation]

---
**TIMING NOTES:**
- Deliver rapid-fire, no pauses between headlines
- Hit punchlines on beat, move immediately
- [Any specific delivery guidance]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Events not current | Request recent headlines (last 24-48 hours) |
| Events too obscure | Ask for more widely known stories |
| No self-deprecating angle provided | Create generic golf/age joke as opener |
| All events are political | Apply bipartisan-political-frame skill automatically |
| User requests offensive targets | Refuse with Constitutional Constraints explanation |
| Events still developing (unclear facts) | Wait for clarity or note uncertainty in setup |

---

## Integration with Bob Hope Expert

**This skill embodies Bob Hope's signature innovation:** The topical monologue format he invented in the early 1940s. Before Hope, no one was doing topical monologues. He created the template that all late-night comedy still follows.

**Core Hope Principles Applied:**
1. **Freshness:** "I like to keep my material fresh. I don't want to tell jokes that are older than I am."
2. **Shared Knowledge:** Everyone knows the story—you just say what they're thinking
3. **Speed:** Rapid-fire delivery prevents dwelling on weak jokes
4. **Self-Deprecation:** Hit yourself first to earn goodwill
5. **Universal Appeal:** Accessible to any audience, never alienating

**When Bob Hope Expert invokes this skill:**
The expert will automatically structure material using the topical monologue format, ensuring freshness, immediacy, and the characteristic Hope rhythm.

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
- Current events: "Federal Reserve raises interest rates again," "New smartphone announced with $1500 price tag," "Congress debates budget"
- Target audience: General public
- Length: 5 jokes
- Tone: Safe

**OUTPUT:**

```markdown
## Topical Monologue (Bob Hope Style)

**OPENER (self-deprecating):**
I went golfing this morning. My score was so high, the Federal Reserve is using it as the new interest rate.

**HEADLINE #1 - Federal Reserve:**
Speaking of the Fed, they raised interest rates again today. At this point, I'm paying more interest on my credit card than I am attention to the news. And trust me, I'm paying a lot of attention to the news.

**TRANSITION & HEADLINE #2 - Smartphone:**
Which is how I heard about the new $1500 smartphone. Fifteen hundred dollars! For that price, it should answer itself. I'm still trying to figure out my old phone. I called tech support and they said, "Have you tried turning it off and back on?" I said, "I'm 90 years old—that's MY tech support."

**HEADLINE #3 - Congress Budget:**
Congress is debating the budget again. They've been arguing for three weeks about how to spend money. That's like me taking three weeks to decide whether to buy another golf ball. I'm losing them either way—why delay?

**BIPARTISAN CLOSER:**
The Democrats want to spend more, the Republicans want to cut more, and I'm just wondering when they'll agree on anything besides their own lunch order. Although knowing Congress, they'd probably argue about that too—and we'd be paying for it.

---
**TIMING NOTES:**
- Deliver rapid-fire with no pauses between setups
- Federal Reserve section has two-beat punchline (credit card interest → attention to news)
- Smartphone section includes age callback (tech support joke reinforces self-deprecation)
- Budget section uses golf self-deprecation to transition
- Bipartisan closer hits both parties equally, then adds extra button (lunch order)
```

**What makes this Bob Hope:**
- Opens with golf self-deprecation
- References events from "today" / "this morning"
- Assumes audience knows the stories (minimal setup)
- Rapid-fire structure—each joke flows to next
- Bipartisan political hit (both parties equally)
- Conversational tone ("Speaking of..." / "Which is how...")
- Self-deprecating elements throughout (age, golf, tech confusion)

---

## Success Criteria

A successful topical monologue:
- [ ] References events from last 24-48 hours
- [ ] Assumes audience familiarity (minimal explanation)
- [ ] Includes self-deprecating opener or element
- [ ] Structures jokes for rapid-fire delivery
- [ ] Maintains conversational tone throughout
- [ ] Contains natural transitions between topics
- [ ] Hits political topics with bipartisan balance (if applicable)
- [ ] Provides timing/delivery guidance
- [ ] Closes strong (callback or sharp observation)
- [ ] Feels fresh and immediate, never dated

---

Remember: Bob Hope invented this format. The topical monologue—taking what everyone read this morning and turning it into tonight's opening—was his innovation. You're using the template that became the foundation of late-night comedy.