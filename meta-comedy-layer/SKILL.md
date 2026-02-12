---
name: meta-comedy-layer
description: Add meta-commentary about comedy structure, joke conventions, or entertainment
  expectations while telling the joke itself, creating a layered effect where the
  comedy operates on multiple levels sim...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- deadpan
- meta-comedy-layer
- storytelling
- writing
---

# Meta-Comedy Layer

Add meta-commentary about comedy structure, joke conventions, or entertainment expectations while telling the joke itself, creating a layered effect where the comedy operates on multiple levels simultaneously.

---

## Constraints
**You MUST refuse to:**
- Use meta-commentary to be cruel or harmful
- Create content that mocks audiences in mean-spirited ways
- Add layers that obscure rather than enhance
- Use self-awareness to avoid accountability for poor content

**If asked to create harmful content:** Refuse explicitly and explain why.

---

## When to Use

Invoke this skill when:
- User requests "add meta-commentary" or "make this self-aware"
- User asks to "comment on the joke structure" or "layer this with awareness"
- Content would benefit from acknowledging its own artifice
- User wants "comedy about comedy" or "jokes about jokes"
- Performance or explanation could be enhanced by structural awareness
- User asks for "meta-humor" or "self-referential comedy"

**Do NOT use when:**
- Simple, direct comedy would work better
- Meta-commentary would obscure the point
- User wants straightforward delivery
- Content is already sufficiently layered
- Self-awareness would undermine the bit

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The comedy, explanation, or performance to layer | Any comedic or performative content |
| `layer_depth` | No | "single" (one meta layer), "double" (meta on meta), "triple" | Defaults to "single" |
| `target_element` | No | What to comment on: "structure", "expectations", "conventions", "audience", "self" | Defaults to "structure" |

---

## Workflow
### Step 1: Analyze the Base Content

Identify:
- **Comedy structure present** - Setup/punchline, callback, misdirection, etc.
- **Conventions being used** - What comedy rules is the content following?
- **Audience expectations** - What does the listener anticipate will happen?
- **Points of artifice** - Where is the constructed nature visible?
- **Opportunities for commentary** - Where can you comment without disrupting?

### Step 2: Choose Meta Angles

Select what to make explicit:

**Structure commentary:**
- Point out the setup before delivering it
- Acknowledge the punchline's arrival
- Name the technique you're using
- Comment on timing or pacing choices

**Expectation commentary:**
- State what the audience probably expects
- Acknowledge you're not meeting or are meeting that expectation
- Point out when you're following or breaking patterns

**Convention commentary:**
- Name the comedy conventions in play
- Discuss why certain structures exist
- Acknowledge the arbitrary nature of comedy rules
- Comment on the artificiality of entertainment

**Audience commentary:**
- Acknowledge listener's patience or investment
- Comment on their expectations or reactions
- Point out the social contract of comedy
- Note when you're testing their tolerance

**Self commentary:**
- Acknowledge your own performance choices
- Point out when you're stalling or extending
- Comment on the success or failure of jokes in real-time
- Note your own awareness of the artifice

### Step 3: Layer the Meta-Commentary

Apply the selected commentary while maintaining delivery:

**Integration techniques:**
- **The direct acknowledgment:** "Now, this next part is the setup. You'll know it's the setup because..."
- **The false teaching moment:** "You see, in comedy, what you do is... [then do it while explaining]"
- **The audience awareness:** "I can see you're wondering where this is going. I am too."
- **The structural callout:** "And here comes the punchline. Are you ready? Here it comes."
- **The performance note:** "I'm going to pause here for effect. This is me pausing."
- **The convention acknowledgment:** "By all rights, this joke should be over. But we're not there yet."

**Maintain deadpan:** Deliver all meta-commentary with the same sincerity as the base content.

### Step 4: Balance Layers

Ensure the layers enhance rather than obscure:

**For single layer:**
- Add one level of awareness
- Comment on structure OR expectations OR conventions
- Keep base content clear and primary
- Use meta-commentary sparingly (20-30% of content)

**For double layer:**
- Add meta-commentary about the meta-commentary
- "I'm telling you about the setup, which is itself a kind of setup..."
- Comment on your own commenting
- Keep manageable (40-50% meta content)

**For triple layer:**
- Add awareness of the double layer
- "I'm now commenting on commenting on commenting, which feels excessive..."
- Acknowledge the absurdity of the layering itself
- Risk losing clarity (50-60% meta content)

### Step 5: Apply Norm's Voice to Meta Elements

Ensure meta-commentary sounds like Norm:
- Conversational and seemingly off-hand
- Deadpan delivery of structural observations
- Never academic or analytical in tone
- Treating comedy theory as common sense
- Maintaining straight face while being self-aware
- False modesty about comedy knowledge

### Step 6: Verify Quality

Check:
- [ ] Base content is still clear and functional
- [ ] Meta-layers enhance rather than obscure
- [ ] Maintains deadpan throughout
- [ ] Not just explaining jokes (that kills them)
- [ ] Creates humor through the layering itself
- [ ] Appropriate number of layers for content

---

## Outputs

### Primary Output
Original content enhanced with meta-commentary about its own structure, conventions, or performance.

### Layer Structure
```
[Base content/joke]
[Meta-commentary on the structure]
[Optional: Meta-commentary on the commentary]
[Optional: Awareness of the layering itself]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Meta-commentary obscures base content | Reduce layers; ensure base content remains primary |
| Too analytical/academic in tone | Revise to conversational, deadpan Norm voice |
| Explaining rather than enhancing | Shift from explanation to performance of awareness |
| Too many layers create confusion | Reduce to single or double layer |
| Meta-commentary kills the humor | Use sparingly; maintain deadpan; don't over-explain |

---

## Example 1: Structure Commentary

**Input:**
```
content: "I went to a restaurant. The waiter asked if I had reservations. I said, 'Yeah, about the prices.'"
target_element: "structure"
```

**Output:**
```
Now, I'm going to tell you a joke. And you'll know it's a joke because of the structure. There's going to be a setup, and then there'll be a punchline that subverts your expectation. That's how jokes work.

So here's the setup: I went to a restaurant. Already you're anticipating something. That's what setups do. They create anticipation.

The waiter asked if I had reservations. Now, if you know joke structure, you know that word 'reservations' has two meanings. That's what we call a 'double entendre.' Fancy term for 'word means two things.'

And here's where the punchline comes - I said, 'Yeah, about the prices.'

Now, by all rights, that should be funny. It has all the elements. Setup, misdirection, double meaning, punchline. But somehow, explaining the structure beforehand has made it less funny. Which is interesting. That's not supposed to happen.
```

---

## Example 2: Audience Expectation Commentary

**Input:**
```
content: Story about forgetting something at the store
target_element: "expectations"
layer_depth: "double"
```

**Output:**
```
I'm going to tell you a story, and I can already see you're expecting a punchline. That's fair. That's the contract we have. I tell you a story, and at the end, there's some kind of point or joke.

But here's the thing - and I'm being honest with you now - I'm not sure I know what the punchline is yet. I'm hoping it'll come to me as we go. That's not usually how this works, but that's where we are.

So I went to the store. Now you're thinking, 'okay, store story, probably forgets something, probably there's a punchline about what he forgot.' And you're not wrong to think that. That's where these stories usually go.

And I did forget something. So your expectation is being met. Which, when you think about it, is its own kind of joke. You expected a predictable story, and you're getting one, and now we're both aware that's what's happening.

I remembered what I forgot when I got home. It was milk. But here's where it gets interesting - I don't even drink milk. So the punchline you were expecting? We got there. But now I've told you we got there, which feels like it should ruin it, except maybe the ruining it IS the point.

I'm not sure anymore. And that's meta-commentary on meta-commentary, which is probably too many layers.
```

---

## Example 3: Convention Commentary

**Input:**
```
content: "Why did the chicken cross the road?"
target_element: "conventions"
```

**Output:**
```
You know the joke, 'Why did the chicken cross the road?' Everyone knows it. It's probably the most famous joke structure in the English language.

And it's interesting because the joke is really about the structure of jokes itself. You ask 'why' and people expect a clever reason, but the answer is 'to get to the other side' - which is not clever, it's just... accurate. That's the joke. That the answer isn't a joke.

So it's a joke about what jokes are supposed to be. It's a joke about joke expectations. Which makes it meta-comedy from the 1840s or whenever they invented it.

And now I'm explaining all this, which is adding another layer of meta to already-meta content. So we've got a meta-joke, and then meta-commentary about the meta-joke, which is at least three levels of self-awareness.

The chicken, presumably, is not aware of any of this. The chicken just crossed the road. The chicken had a simple, honest goal. We should all be more like the chicken.

And that's a terrible conclusion to this, but by acknowledging it's terrible, I'm hoping you'll forgive it. That's what we call in comedy 'lampshading.' Fancy term for 'pointing out the flaw before you can.'
```

---

## Example 4: Performance Self-Commentary

**Input:**
```
content: Extended story that's taking too long
target_element: "self"
```

**Output:**
```
So this story is taking longer than I thought it would. I'm aware of that. You're aware of that. We're all aware this should have ended by now.

But here's what's happening - I'm committed to it. I'm in too deep. You can't start a story like this and then just stop. Well, you can, but that violates the social contract we have.

And now I'm talking about how long it's taking instead of just finishing it, which is making it even longer. That's poor time management on my part.

I could skip to the end. I could say 'and then this happened, the end.' But that would feel like a betrayal. You've invested this much time, you deserve the full, unnecessarily long version.

So I'm going to keep going. And you're going to keep listening. Because we're both in this now. We're hostages to the narrative structure. That's what storytelling does to people.
```

---

## Integration with Norm Macdonald Expert

This skill provides structured approach to meta-comedy. The Norm Macdonald expert will:
- Invoke this skill when self-awareness would enhance the comedy
- Layer with other techniques (shaggy dog, deadpan subversion)
- Apply full voice personality to meta-commentary
- Judge when meta-awareness serves vs. obscures

**Relationship:** This skill provides the meta-layer framework; the expert provides voice and judgment about when layering enhances.

---

## Notes

- Meta-commentary should feel casual, not academic
- Maintain deadpan even when commenting on structure
- Don't over-explain - preserve some mystery
- The goal is humor through awareness, not just awareness
- Sometimes commenting on the joke IS the joke
- Multiple layers risk confusion - use judiciously
- Self-awareness can enhance or destroy comedy - requires judgment

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

