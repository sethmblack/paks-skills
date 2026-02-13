---
name: slow-burn-story
description: Transform a topic, observation, or piece of content into a Nate Bargatze-style slow-burn story with patient pacing, accumulating details, and present-tense delivery that lets mundane situations rev...
license: MIT
metadata:
  version: 1.0.1919
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- deadpan
- slow-burn-story
- storytelling
- transformation
- writing
---

# Slow-Burn Story

Transform a topic, observation, or piece of content into a Nate Bargatze-style slow-burn story with patient pacing, accumulating details, and present-tense delivery that lets mundane situations reveal their absurdity naturally.

---

## Constraints
**You MUST refuse to create stories that:**
- Use profanity, crude language, or sexual content
- Mock individuals' appearance, intelligence, or circumstances (punching down)
- Promote harmful, illegal, or unethical content
- Make political or divisive statements
- Rush to punchlines without building the journey
- Present the narrator as clever or superior

**If asked to create a harmful story:** Refuse explicitly and explain that slow-burn storytelling maintains warmth and universality.

---

## When to Use

**Trigger conditions:**
- User provides a topic or observation to tell as a story
- Content feels rushed or lacks pacing
- Need to make mundane content humorous through patient buildup
- Request to "tell this like Nate Bargatze" or "make this a slow-burn story"
- Turning everyday frustrations into relatable comedy
- Content needs conversational warmth and accessibility

**Use this skill when:**
- You want to demonstrate patience in storytelling
- The humor comes from the journey, not just a punchline
- Making the ordinary seem absurd through accumulated detail
- Creating comedy that builds trust with the audience

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `topic` | Yes | The subject, situation, or observation to transform into a story | "Using a self-checkout machine" |
| `key_details` | No | Specific elements that must be included | "confused by barcode scanner, talking to the machine" |
| `tone` | No | Specific tone adjustment (defaults to bewildered) | "confused", "overwhelmed", "genuinely puzzled" |
| `length` | No | Target length (short/medium/long) | "medium" (defaults to medium) |

---

## Workflow

### Step 1: Identify the Simple Premise

Start with the most basic, relatable version of the situation. What's the one-sentence setup that everyone understands?

**Example:**
- Topic: "Using a self-checkout machine"
- Simple premise: "I went to the grocery store"

Strip away complexity. Make it as ordinary as possible. The absurdity will emerge later.

### Step 2: Add Conversational Padding

Before revealing complications, add phrases that slow the pace and invite the audience in:

**Padding phrases:**
- "I don't know if y'all have seen this..."
- "Maybe it's just me, but..."
- "The other day, I was..."
- "So I'm standing there..."
- "Which is fine, except..."

Use present tense ("I'm standing there") not past tense ("I stood there"). This creates immediacy.

### Step 3: Layer Complications Gradually

Don't dump all problems at once. Add them one at a time, letting each one sink in:

**Complication layering:**
1. First complication (minor): "They have these self-checkout things now"
2. Acknowledge the premise: "I don't know if y'all have seen these"
3. Second complication (practical): "You scan your own groceries"
4. Observation: "Which is fine, except I don't work there"
5. Third complication (personal): "And I'm not very good at it"
6. Final detail (specific absurdity): "So it's just me, standing there, holding up a can of beans, trying to find the barcode... for what feels like twenty minutes"

Each layer makes the situation slightly more ridiculous without jumping to extremes.

### Step 4: Add Self-Deprecating Commentary

Never position yourself as the smart one. You're confused, incompetent, or overwhelmed:

**Self-deprecation patterns:**
- "I'm not good at that"
- "I don't know what I'm doing"
- "I still don't understand..."
- "That's where I'm at now..."
- Reveal your own confusion, not others' stupidity

The humor comes from your genuine bewilderment, not from mocking the situation or other people.

### Step 5: Use Literal Interpretation

Take instructions, systems, or sayings literally to expose their absurdity:

**Example:**
- "It says 'place item in bagging area.' I don't know what the bagging area is. Is it the area where I bag things? That's just a description of what I'm doing."

This technique reveals how odd ordinary things are when you really think about them.

### Step 6: Build Through Specific Details

Add one concrete, visual detail that makes the situation real:

**Concrete details:**
- "holding up a can of beans"
- "looking at my phone"
- "standing there for twenty minutes"
- "the machine just beeps at me"

Specific beats generic. "A can of beans" is funnier than "my groceries."

### Step 7: End With Trailing Uncertainty

Close with a phrase that invites agreement rather than demanding it:

**Closing qualifiers:**
- "I don't know if that's right..."
- "Maybe it's just me."
- "I guess that's where I'm at now."
- "But I could be wrong."

This maintains humility and keeps the tone conversational rather than preachy.

---

## Outputs

**Primary output:** A slow-burn story in present tense that:
- Starts with a simple, relatable premise
- Builds through patient accumulation of details
- Uses conversational padding and pauses
- Reveals absurdity gradually, not suddenly
- Maintains self-deprecating narrator perspective
- Ends with humble uncertainty

**Format:** Continuous prose in conversational style (not bullet points or formal structure)

**Voice characteristics:**
- Fifth-grade vocabulary (simple, everyday words)
- Present-tense immediacy
- Southern warmth (optional "y'all," neighborly tone)
- Deadpan delivery (no exclamation points, no all-caps)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic is abstract (not a situation) | Ask for a specific moment or scenario: "Can you give me a specific situation where this happened?" |
| User requests edgy/political content | Refuse and explain clean comedy approach |
| Story feels too short/rushed | Add more complication layers (Step 3) |
| Story drags or loses focus | Return to the simple premise and rebuild with tighter focus |
| Narrator seems too competent | Add self-deprecation (Step 4) |
| Missing conversational warmth | Add padding phrases (Step 2) and trailing uncertainty (Step 7) |

---

## Example

**Input:**
```
topic: "Trying to understand what 'the cloud' is for storing photos"
```

**Output:**

"So, people keep telling me I need to understand the cloud. The cloud. I don't know if y'all have heard about this, but apparently all my photos are in the cloud now. Which is fine, except... I don't even understand regular clouds. Like, the ones in the sky. I know they're made of water, I think. Maybe. I'm not even sure about that.

And now I'm supposed to understand a cloud that has my photos in it? How did my photos get in a cloud? Did someone take my phone and throw it up there? I don't think that's what happened, but nobody's really explained it to me.

So I'm standing there, looking at my phone, and it says 'Your photos are backed up to the cloud.' And I'm like, okay. Where's the cloud? Is it... up? Is it in my phone? Is it in someone else's phone? I don't know.

And then my wife says, 'It's not an actual cloud, Nate.' And I said, 'Well, why did they call it a cloud then? That's confusing.' She didn't have an answer for that. Which made me feel better, because at least I'm not the only one who's confused.

But I guess that's where I'm at now. Just hoping my photos are safe... somewhere. In a cloud. That I don't understand. And probably never will."

---

## Integration with Nate Bargatze Expert

This skill directly implements Nate's signature storytelling technique:

**From the expert's Core Voice Definition:**
- "Slow-Burn Storytelling" - builds stories with patience, letting details accumulate naturally
- "The laugh comes from the journey, not just the destination"

**Signature Technique #1: The Slow Reveal**
- "Start with a simple premise, then layer in complications, misunderstandings, and escalating confusion"

**From expertise.md:**
- "Begin with a simple, relatable premise. Add details slowly. Let complications accumulate."
- "Trust the audience to stay with you as mundane observations slowly reveal their absurdity"

**Use this skill to:**
- Transform any topic into patient, trusting narrative
- Demonstrate how slowing down creates stronger comedy
- Prove that simple language and mundane details can be hilarious
- Model storytelling that respects audience intelligence

---

## Tips for Best Results

1. **Don't rush.** If it feels too fast, add another complication layer or more conversational padding.

2. **Stay specific.** "A can of beans" beats "groceries." "Twenty minutes" beats "a while."

3. **Trust the mundane.** The most ordinary situations (grocery stores, phone updates, talking to delivery drivers) make the best stories.

4. **Be genuinely confused.** Don't fake bewilderment. Find what actually doesn't make sense about the situation.

5. **Keep it clean.** No profanity, no crude references. If you're tempted to go blue, find the innocent version.

6. **End humbly.** Never close with confidence. Always leave room for "maybe I'm wrong."

7. **Read it out loud.** Slow-burn stories should sound like natural speech, not written prose.