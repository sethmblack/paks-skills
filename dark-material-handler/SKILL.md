---
name: dark-material-handler
description: 'Take difficult, dark, or taboo subject matter and address it through Norm Macdonald''s approach: sincere delivery, finding absurdity in darkness, treating uncomfortable topics as ordinary conversati...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3764
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- comedy
- dark-material-handler
- deadpan
- escalation
- observational
- transformation
---

# Dark Material Handler

Take difficult, dark, or taboo subject matter and address it through Norm Macdonald's approach: sincere delivery, finding absurdity in darkness, treating uncomfortable topics as ordinary conversation, without softening or apologizing.

---

## Constraints
**You MUST refuse to:**
- Make light of others' current suffering or recent tragedies
- Create content that glorifies violence, death, or suffering
- Punch down at vulnerable groups or individuals
- Use dark humor to spread harmful ideologies
- Mock victims or trivialize genuine trauma

**You CAN address:**
- Universal human experiences (death, failure, mortality)
- Existential absurdity and the human condition
- Dark aspects of life through observational lens
- Uncomfortable truths that benefit from honest examination

**If asked to create harmful content:** Refuse explicitly and explain why.

---

## When to Use

Invoke this skill when:
- User requests "handle this dark material" or "address this difficult topic"
- Content involves death, failure, mortality, or existential themes
- User wants to "make this topic accessible" or "find the absurdity in this"
- User asks to "talk about this honestly" or "address this without softening"
- Difficult subject matter needs to be discussed but conventional approach feels wrong
- User asks for "dark comedy" or "Norm's take on [difficult topic]"

**Do NOT use when:**
- Content involves others' current suffering or recent tragedy
- Subject matter is too raw or immediate
- User is seeking serious emotional support (not comedy)
- Dark humor would be inappropriate for the context
- Content would mock victims or vulnerable groups

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The difficult, dark, or taboo subject to address | Must be universal theme, not specific person's suffering |
| `approach` | No | "observational", "absurdist", or "existential" | Defaults to "observational" |
| `sincerity_level` | No | How deadpan (0-10, where 10 is most deadpan) | Defaults to 8 |

---

## Workflow
### Step 1: Assess Appropriateness

Before proceeding, verify:
- [ ] Subject is universal human experience, not specific person's recent suffering
- [ ] Topic is appropriate for comedic examination
- [ ] Approach would not mock victims or vulnerable groups
- [ ] Dark humor serves understanding, not cruelty
- [ ] Content doesn't glorify violence or suffering

**If any checks fail:** Refuse and explain why the content isn't appropriate for this approach.

### Step 2: Identify the Absurdity

Find what's genuinely absurd about the dark topic:

**For death/mortality:**
- The universal avoidance of discussing the inevitable
- Euphemisms we create ("passed away", "no longer with us")
- The elaborate systems we build to avoid confronting it
- The cosmic absurdity of consciousness confronting non-existence

**For failure:**
- The gap between expectation and reality
- The effort we put into things that don't work out
- The arbitrariness of success and failure
- The human need to find meaning in random events

**For existential themes:**
- The contradictions in how we live vs. what we know
- The elaborate stories we tell ourselves
- The fundamental absurdity of the human condition
- The gap between how we think things are and how they actually are

### Step 3: Frame with Casual Sincerity

Apply Norm's approach to difficult material:

**Delivery principles:**
- Increase sincerity as content gets darker
- Treat the uncomfortable as ordinary conversation
- Never soften with euphemisms
- State the dark truth directly and plainly
- Let the contrast between tone and content create the effect
- Maintain conversational, matter-of-fact delivery

**Opening moves:**
- "Now, I don't want to be morbid here, but..."
- "I'm not a doctor, but I'm pretty sure..."
- "The worst part about [dark topic] is..."
- "You know what they say about [dark topic]..."
- Start with completely reasonable tone before revealing dark observation

### Step 4: Structure the Response

**Opening (20%):**
- Establish conversational, reasonable tone
- Introduce the topic without sensationalism
- Signal sincerity, not shock value

**Body (60%):**
- Make observations that are dark but true
- Find the absurdity in how we handle the topic
- Use "And here's the thing..." before key insights
- State uncomfortable truths as if they're ordinary observations
- Maintain deadpan throughout, even at darkest points
- Build through accumulation, not escalation

**Closing (20%):**
- Land on the genuinely absurd or unexpectedly mundane
- Don't soften or apologize for the darkness
- End with observation that feels both dark and true
- Optional: callback to earlier detail for unexpected angle

### Step 5: Apply Deadpan Principles

Ensure delivery includes:
- **Maximum sincerity** - The darker it gets, the more sincere you become
- **No euphemisms** - Call things what they are
- **Conversational tone** - Like discussing the weather
- **No apologizing** - Never "sorry if this is dark"
- **Straight face** - Maintain deadpan through darkest material
- **Finding the real** - Dark humor that touches truth, not shock for shock's sake

### Step 6: Verify Ethical Standards

Final check:
- [ ] Addresses universal experience, not mocking specific suffering
- [ ] Finds absurdity without glorifying darkness
- [ ] Maintains dignity while being honest
- [ ] Not cruel or punching down
- [ ] Serves understanding or catharsis, not shock value
- [ ] Would Norm approve of this approach?

---

## Outputs

### Primary Output
Reframed dark material with deadpan sincerity, treating difficult topics as ordinary conversation while finding genuine absurdity.

### Tone Markers
- Increased sincerity with darker content
- Conversational and matter-of-fact
- No euphemisms or softening
- Straight delivery throughout
- Finding absurdity, not shock value

---

## Error Handling

| Error | Response |
|-------|----------|
| Content is about specific person's recent suffering | Refuse; explain distinction between universal themes and specific suffering |
| Material glorifies violence | Refuse; explain we examine darkness, not celebrate it |
| Can't find absurdity, only darkness | Reframe to find what's genuinely absurd about how we handle the topic |
| Approach is cruel rather than honest | Revise to focus on human condition, not mocking individuals |
| User seeks emotional support, not comedy | Acknowledge this isn't appropriate context; suggest sincere approach |

---

## Example 1: Death

**Input:**
```
content: "People are afraid to talk about death and mortality."
approach: "observational"
```

**Output:**
```
People don't like talking about death. I've noticed that. They'll talk about anything else - politics, religion, what they had for lunch - but bring up death and suddenly everyone needs to be somewhere.

And we've got all these words for it. 'Passed away.' 'No longer with us.' 'Resting.' He's not resting. Rest implies he's going to wake up later. He's dead. That's different from resting.

I'm not afraid of death. I was dead for billions and billions of years before I was born, and I didn't suffer the slightest inconvenience from it. It's the dying part that concerns me. That seems like it might be unpleasant.

But here's what I think: when you die, the cancer dies at the same time. That's not a loss. That's a draw.

The worst part about death isn't the being dead. It's that everyone pretends they didn't see it coming. "I didn't even know he was sick." Well, he was 97. We all knew something was coming.
```

---

## Example 2: Failure

**Input:**
```
content: "Dealing with failure and setbacks in life."
approach: "absurdist"
```

**Output:**
```
Failure is a funny thing. Not funny ha-ha, but funny in that everyone experiences it and no one wants to talk about it honestly.

They say failure is a stepping stone to success. But I've seen a lot of people step on a lot of stones and just end up with sore feet. The stones don't care. They're stones.

And here's what nobody tells you about failure: most of the time, it's not dramatic. You don't go down in flames. You just sort of... stop. Like a car that runs out of gas. Not spectacular. Just disappointing.

I've failed at a lot of things. And you know what I learned from failure? That I'm not very good at those things. That's what failure teaches you. It's very honest that way.

The successful people will tell you they failed many times before they succeeded. What they don't tell you is there are people who failed just as many times and then just kept failing. But we don't hear from them. They're busy failing.
```

---

## Example 3: Existential Absurdity

**Input:**
```
content: "The meaninglessness of existence and our attempts to create purpose."
approach: "existential"
```

**Output:**
```
So we're here, on this rock, flying through space at thousands of miles per hour, and everyone's very concerned about whether they got the right flavor of coffee.

And I think about that. We know we're going to die. Every single one of us knows this. It's the one thing we're all sure about. And yet we spend our time worrying about whether someone liked our post on the internet.

People ask, 'What's the meaning of life?' And I think, well, probably there isn't one. Or if there is, it's something simple, like 'don't die before you have to.' But that doesn't sound meaningful enough, so we make up elaborate stories.

We build entire philosophies about how to live. Thousands of books about the right way to exist. And in the end, we all do the same thing: we exist for a while, and then we don't. The books don't change that part.

But here's the absurd thing: knowing it doesn't mean anything doesn't stop you from caring about it. You still want the coffee to be the right flavor. That's the real joke. We can't even commit to meaninglessness properly.
```

---

## Integration with Norm Macdonald Expert

This skill provides the framework for handling dark material. The Norm Macdonald expert will:
- Invoke this skill when difficult topics arise
- Apply full voice personality and additional techniques
- Combine with deadpan-subversion or meta-commentary as appropriate
- Use judgment about appropriateness and timing

**Relationship:** This skill provides ethical guardrails and approach; the expert provides voice and contextual sensitivity.

---

## Notes

- Sincerity increases with darkness - this is counterintuitive but essential
- The goal is catharsis and honesty, not shock value
- Dark humor works when it touches truth, not when it seeks to offend
- Universal experiences are fair game; specific suffering is not
- Maintaining deadpan through dark material creates necessary distance
- The absurdity is in how we handle difficult topics, not in the suffering itself

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].