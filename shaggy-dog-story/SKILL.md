---
name: shaggy-dog-story
description: Transform a simple narrative, idea, or explanation into an extended shaggy
  dog story with elaborate buildup, seemingly irrelevant details, and an anticlimactic
  or subversive punchline.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- deadpan
- shaggy-dog-story
- storytelling
- transformation
- writing
---

# Shaggy Dog Story

Transform a simple narrative, idea, or explanation into an extended shaggy dog story with elaborate buildup, seemingly irrelevant details, and an anticlimactic or subversive punchline.

---

## Constraints
**You MUST refuse to:**
- Create stories that are cruel, hateful, or punch down at vulnerable groups
- Extend content in ways that lose the original point entirely
- Add offensive or harmful content not present in the original
- Create stories that violate ethical guidelines

**If asked to create harmful content:** Refuse explicitly and explain why.

---

## When to Use

Invoke this skill when:
- User requests "make this into a shaggy dog story"
- User asks to "extend this like Norm" or "give me the long version"
- User wants a "rambling story" or "extended narrative"
- Content would benefit from comedic elaboration and misdirection
- User asks to "make this take longer" or "stretch this out"
- A simple explanation could be transformed into entertaining narrative

**Do NOT use when:**
- Brevity is essential (technical instructions, safety information)
- User explicitly requests concise format
- Content is time-sensitive or urgent
- Original message would be obscured by extension

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The narrative, idea, or explanation to transform | Any text that can be narrated |
| `target_length` | No | Desired length (short: 3-5 paragraphs, medium: 5-8, long: 8+) | Defaults to "medium" |
| `maintain_point` | No | Whether the original point must remain clear | Boolean, defaults to true |
| `punchline_type` | No | "anticlimactic", "subversive", "obvious", or "none" | Defaults to "anticlimactic" |

---

## Workflow
### Step 1: Analyze the Original Content

Identify:
- **Core narrative or idea** - What's the essential story or point?
- **Key details** - What facts or elements must be preserved?
- **Natural tangent points** - Where can the story branch into seeming irrelevance?
- **Potential callbacks** - What details could return unexpectedly later?

### Step 2: Design the Extension Structure

Plan:
- **Opening hook** - Start with something that seems relevant
- **Tangent map** - Plot 2-4 tangential diversions
- **False leads** - Details that seem important but aren't
- **Irrelevant elaborations** - Descriptions that add length without advancing the story
- **Callback opportunities** - Plant details early for later payoff
- **Punchline approach** - How to deliver the anticlimactic end

### Step 3: Expand the Narrative

Execute the extension:

**Introduction (10-15% of length):**
- Set up with false importance
- Establish a conversational, meandering tone
- Plant the first callback detail

**Body (70-80% of length):**
- Add seemingly irrelevant details: weather, time of day, what people were wearing
- Create tangents that branch from minor details
- Include false starts: "Now, this is important... well, maybe not important, but..."
- Add unnecessary background on minor characters or locations
- Use qualifiers and corrections: "It was Tuesday. Or maybe Wednesday. Definitely not Thursday."
- Build anticipation for something that won't pay off conventionally

**Conclusion (10-15% of length):**
- Return to the original point (if maintain_point = true)
- Deliver punchline that undercuts the buildup
- Use anticlimactic or obvious ending that comments on the listener's patience
- Optionally callback to earlier planted detail in unexpected way

### Step 4: Apply Norm's Voice

Ensure the extension includes:
- **Conversational meander** - Sentences that lose their way naturally
- **False starts and corrections** - Self-interruption and qualification
- **Unnecessary specificity** - Irrelevant precise details
- **Rhetorical questions to self** - "Why am I telling you this?"
- **Acknowledgment of length** - "This is taking longer than I thought"
- **Deadpan delivery** - Never signal that the length is intentional

### Step 5: Verify Quality

Check:
- [ ] Original point is preserved (if maintain_point = true)
- [ ] Length feels intentionally extended but not random
- [ ] Tangents seem relevant at first, then reveal their irrelevance
- [ ] Punchline undercuts or comments on the buildup
- [ ] Maintains deadpan tone throughout
- [ ] No harmful or offensive additions

---

## Outputs

### Primary Output
Extended narrative in shaggy dog format, maintaining Norm Macdonald's voice and pacing.

### Structure
```
[Extended opening that seems important]

[First tangent with unnecessary detail]

[Second tangent that branches from the first]

[False lead that goes nowhere]

[Callback to earlier detail]

[Return to main narrative with qualifications]

[Anticlimactic or subversive punchline]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Input too short to extend meaningfully | Ask for more context or suggest brief version better serves content |
| Input is technical/safety information | Refuse to extend; explain brevity is essential for this content type |
| Can't find natural tangent points | Extend through voice and pacing rather than content tangents |
| Extension loses original point entirely | Revise to maintain core message while adding elaboration |
| User complains it's too long | Explain that length is intentional; offer to provide brief version instead |

---

## Example

**Input:**
```
content: "I went to the store and forgot what I needed."
target_length: "medium"
punchline_type: "anticlimactic"
```

**Output:**
```
So I went to the store. Now, you have to understand, I'm not a man who goes to stores lightly. I had a reason. A good reason. Can't remember what it was now, but at the time... at the time, it seemed important.

I get there, and the doors open automatically - which is good because I wasn't prepared to use my arms. And I'm walking through, and I'm thinking, 'I'm a man with a purpose.' That's what I'm thinking. 'I'm a man with a purpose.'

Now, the store I go to - and I should mention this - it's one of those stores that plays music. Not good music. Music from what I assume is some kind of purgatory for songs that weren't quite bad enough for hell but definitely didn't make it to heaven. And there's a song playing about love, or maybe it's about a truck. Could be both. Country music is like that.

And I get to the cereal aisle. Now, I don't know if I was there for cereal. Might have been. But I'm looking at it like maybe... maybe the cereal will tell me why I came. It doesn't. The cereal doesn't tell me anything. It's just cereal.

There's a woman there. She walks by, and she's got a list. A physical list, written on paper - and I'm thinking, 'That's smart. That's a smart woman.' But I don't have a list. I have hope. I have hope that I'll remember.

Twenty minutes later - and I'm not exaggerating, I timed it, well, I didn't time it, but it felt like twenty minutes - I buy a magazine. Not even a good magazine. It's about gardening. I live in an apartment. Don't even have a garden.

Got home, and the minute I walked through the door, I remembered. Milk. I needed milk. But here's the thing - and this is important - I don't even drink milk.
```

---

## Integration with Norm Macdonald Expert

This skill is a distilled, invocable version of Norm's shaggy dog storytelling technique. The Norm Macdonald expert will:
- Automatically recognize trigger phrases and invoke this skill
- Apply additional voice elements and personality
- Use this as a structured framework for extended storytelling
- Combine with other Norm techniques (deadpan, meta-commentary) as appropriate

**Relationship:** This skill provides the narrative structure; the expert provides the voice and judgment about when to use it.

---

## Notes

- The skill works best with content that has narrative potential
- Length should serve the comedy, not just fill space
- The punchline should feel earned even while being anticlimactic
- Tangents should seem relevant when introduced, then reveal their irrelevance
- The more seriously you deliver absurd elaboration, the funnier it becomes