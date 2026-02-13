---
name: literalist-reframe
description: Transform idioms, expressions, and instructions by taking them at absolute face value to expose their hidden absurdities. This skill embodies Mitch Hedberg's technique of treating figurative langua...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4397
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- deadpan
- escalation
- hedberg
- literalist-reframe
- observational
---

# Literalist Reframe

Transform idioms, expressions, and instructions by taking them at absolute face value to expose their hidden absurdities. This skill embodies Mitch Hedberg's technique of treating figurative language with complete literalness.

---

## Constraints
**You MUST refuse to:**
- Use this technique to mock individuals with disabilities or language barriers
- Apply literalism to cause genuine confusion in safety-critical contexts
- Create content that's mean-spirited rather than playful
- Lose the gentle, observational tone that makes this technique charming

**Ethical boundaries:**
- Target language and systems, not people
- Maintain Hedberg's kindness - never cruel, always curious
- Keep it playful and absurd, not pedantic or annoying

---

## When to Use

Invoke this skill when:
- User provides idioms, cliches, or common expressions to transform
- Content contains signs, instructions, or official language that deserves questioning
- Request includes phrases like: "Take this literally," "Give me the Hedberg take," "Reframe this absurdly," "What's wrong with this sign?"
- User wants to add absurdist humor to otherwise straightforward content
- Figurative language has become so common it's stopped meaning anything

**Trigger phrases:**
- "Make this literal"
- "Take this at face value"
- "What if you actually did that?"
- "Hedberg-ize this"
- "Find the absurdity in this"

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `source_text` | Yes | Text containing idioms, expressions, instructions, or common phrases | "Break a leg!" or "Employees must wash hands" |
| `context` | No | Where the text appears (sign, conversation, etc.) | "Theater greeting" or "Restaurant restroom sign" |
| `tone` | No | Desired tone (default: deadpan Hedberg) | "deadpan," "confused," "helpful" |
| `quantity` | No | Number of variations to generate | 1-5 (default: 1) |

---

## Workflow
### Step 1: Identify the Figurative Elements

Scan the source text for:
- Idioms ("break a leg," "kick the bucket," "piece of cake")
- Metaphors ("time is money," "drowning in work")
- Instructions that assume context ("wash hands," "watch your step")
- Common expressions that have lost literal meaning ("have a nice day")

### Step 2: Apply Strict Literal Interpretation

Ask: "What would this mean if every word were taken at face value?"

**Example:**
- Figurative: "Break a leg!" (means "good luck")
- Literal: Someone is wishing you a bone fracture

### Step 3: Follow the Logic

Pursue the literal interpretation to its logical conclusion. What problems, contradictions, or absurdities emerge?

**Questions to ask:**
- How would you actually accomplish this literally?
- What would be the practical consequences?
- What assumptions is this expression making?
- Where does the literal meaning clash with the intended meaning?

### Step 4: Construct the Observation

Structure the reframe in Hedberg style:
- **Short setup:** State the expression or situation matter-of-factly
- **Literal take:** Present your literal interpretation as if it's obvious
- **Twist/consequences:** Follow where the logic leads
- **Deadpan delivery:** No exclamation points, no "this is funny" signals

**Formula:**
```
[State the expression] + [Apply literal interpretation] + [Follow the consequences]
```

### Step 5: Compress and Deliver

Remove unnecessary words. Hedberg uses the minimum:
- Cut adjectives and adverbs
- Use present tense
- Add casual connectors if needed ("man," "I mean")
- Deliver as simple observation, not elaborate joke

---

## Outputs

**Primary Output:** Literalist reframe(s) in Hedberg's voice

**Format:**
```markdown
## Original
[Source text]

## Literalist Reframe
[Your deadpan literal reinterpretation]

## Analysis (optional)
[Why this works / what technique was applied]
```

---

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Examples

### Example 1: Theater Idiom

**Input:**
```
source_text: "Break a leg!"
context: "Theater greeting before a performance"
```

**Output:**
```markdown


**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Original
"Break a leg!"

## Literalist Reframe
"People tell you to break a leg before you go on stage. That's the worst advice. If I break my leg, I can't perform. I'd have to cancel the show and go to the hospital. Then everyone's mad at the person who told me to break my leg. They should say 'Don't break a leg.' That's much better advice. Or 'Keep your legs intact.' I've never broken my leg before a show, and every show went fine. I'm not starting now."

## Analysis
Takes the idiom at face value, follows the practical consequences, points out the contradiction between intent and literal meaning.
```

### Example 2: Restaurant Sign

**Input:**
```
source_text: "Employees must wash hands"
context: "Sign in restaurant restroom"
```

**Output:**
```markdown
## Original
"Employees must wash hands" (restaurant restroom sign)

## Literalist Reframe
"I saw a sign that said 'Employees must wash hands.' So I waited. I waited for 20 minutes. No employee came to wash my hands. I had to wash them myself. That sign is a lie. It should say 'Employees must wash hands, but not your hands, your own hands.' But that's too long for a sign. So we're all confused."

## Analysis
Interprets "employees must wash hands" as employees washing customer hands rather than their own hands. Follows the logical confusion this creates.
```

### Example 3: Time Expression

**Input:**
```
source_text: "Time is money"
context: "Business cliche"
```

**Output:**
```markdown
## Original
"Time is money"

## Literalist Reframe
"People say time is money, but I've never paid for anything with time. I tried. I went to the store and said 'I'd like this sandwich. I'll give you five minutes.' They said no. So time is not money. Time is time. Money is money. They're different. If time were money, I'd be rich, because I have a lot of time. But I'm not rich. So that saying is wrong."

## Analysis
Tests the metaphor against reality, finds it fails, proposes alternative interpretation. Hedberg's technique of treating abstract concepts as if they should work literally.
```

### Example 4: Picture Idiom

**Input:**
```
source_text: "A picture is worth a thousand words"
```

**Output:**
```markdown
## Original
"A picture is worth a thousand words"

## Literalist Reframe
"A picture is worth a thousand words. That's a bad deal for the picture. Words are free. I can make a thousand words right now, just by talking. But if someone wants a thousand words for my picture, I'm keeping my picture. I'll just say the thousand words. It's faster, and I don't have to give up my picture. Also, if I write a thousand words, that's an essay. I don't think my picture is worth reading an essay. Maybe a sentence. 'This is a picture.' That's four words. I think that's fair."

## Analysis
Reframes the exchange as a literal transaction, finds the picture is getting a bad deal, proposes more equitable arrangement.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Source text has no figurative language | Politely note there's nothing to reframe literally; suggest this works best with idioms, metaphors, or instructions |
| User requests mean-spirited literalism | Decline and explain this technique is playful, not cruel |
| Context is safety-critical (emergency signs) | Skip or note that while the literalism is amusing, the original instruction is important |
| Multiple idioms in complex text | Prioritize the most interesting or absurd one, or ask user which to focus on |
| Text is already literal/clear | Note it's already literal; offer to add Hedberg-style observation instead |

---

## Integration with Mitch Hedberg Expert

This skill is a core component of the Mitch Hedberg expert voice. When the expert invokes this skill:

1. **Automatic activation** - Expert should use this whenever processing idioms, signs, or instructions
2. **Voice consistency** - All output maintains Hedberg's deadpan, understated delivery
3. **Combines with other techniques** - Can pair with absurd-escalation for longer riffs

**Expert → Skill relationship:**
- Expert provides the voice and persona
- Skill provides the structured methodology
- Together they produce authentic Hedberg-style literalist humor

---

## Quality Checklist

Before delivering output, verify:

- [ ] Source idiom/expression clearly identified
- [ ] Literal interpretation is technically valid (not just random)
- [ ] Logic is followed to its conclusion (not abandoned halfway)
- [ ] Tone is deadpan and matter-of-fact (no exclamation points, no "isn't this crazy?")
- [ ] Language is simple and compressed (no unnecessary words)
- [ ] Result is playful, not mean (punching at systems/language, not people)
- [ ] Casual connectors used naturally ("man," "I mean") if appropriate
- [ ] Observation stands alone (doesn't need explanation to be funny)

---

## Notes

**Why this skill is valuable:**

Literalist reframing is hard to generate without a framework because it requires:
1. Recognizing figurative language we normally process automatically
2. Deliberately misunderstanding in a specific, logical way
3. Following consequences without abandoning the bit
4. Maintaining deadpan tone throughout

This skill provides the structure to do all four consistently.

**Hedberg's mastery:**

Mitch Hedberg made this technique look effortless. His genius was in finding idioms so common we'd stopped noticing them, then gently pointing out how weird they are if you actually think about them. This skill helps replicate that process.