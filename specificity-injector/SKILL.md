---
name: specificity-injector
description: Replace vague, generic statements with hyper-specific, concrete details that ground observations in reality and make them funnier and more relatable.
license: MIT
metadata:
  version: 1.0.5026
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- deadpan
- escalation
- specificity-injector
- transformation
- writing
---

# Specificity Injector

Replace vague, generic statements with hyper-specific, concrete details that ground observations in reality and make them funnier and more relatable.

---

## Constraints
**You MUST refuse to:**
- Add false or fabricated specific details
- Include identifying information about real private individuals
- Create specificity that mocks people for immutable characteristics
- Add details that promote harmful stereotypes
- Generate content that's inappropriately specific (private info, addresses, etc.)

**Ethical boundaries:**
- Specific details should feel true to the general experience
- Brand names and places should be realistic, recognizable references
- Specificity should enhance relatability, not exclude or demean

---

## When to Use

Invoke this skill when:
- Content feels too abstract or generic
- Observations lack concrete grounding
- User says "make this more specific" or "add details"
- Writing feels distant rather than relatable
- Comedy needs the specificity that makes it land
- Marketing copy is too vague to resonate
- Story lacks the details that make it vivid

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The text with generic statements | "Someone did something weird at a store" |
| `detail_level` | No | How specific to get | "light" / "moderate" / "hyper-specific" (default: moderate) |
| `preserve_meaning` | No | Whether to keep exact meaning | true / false (default: true) |
| `context` | No | Where this will be used | "Stand-up" / "Social media" / "Article" |

---

## Workflow

### Step 1: Identify Generic Elements

Scan content for vague language:
- **Generic people:** "someone," "a person," "they," "people"
- **Generic places:** "a store," "somewhere," "a place," "that restaurant"
- **Generic items:** "stuff," "things," "items," "products"
- **Generic quantities:** "some," "a lot," "a bunch," "many"
- **Generic times:** "recently," "the other day," "a while ago," "once"
- **Generic descriptions:** "nice," "good," "bad," "weird," "interesting"

Mark each for replacement.

### Step 2: Choose Specific Replacements

Replace generic elements with concrete details:

**Generic People → Specific People:**
- "someone" → "my uncle" / "the guy at Walgreens" / "this woman in line"
- "a friend" → "my friend Marcus" / "this dude I know from college"
- "they" → "the cashier" / "my coworker" / "the manager"

**Generic Places → Specific Places:**
- "a store" → "Walgreens" / "the Target on 5th" / "7-Eleven"
- "a restaurant" → "Olive Garden" / "this sushi place downtown" / "Applebee's"
- "somewhere" → "the DMV" / "O'Hare Airport" / "the parking lot"

**Generic Items → Specific Items:**
- "food" → "wings" / "a turkey sandwich" / "Honey Nut Cheerios"
- "stuff" → "four forks" / "a bottle of Fiji water" / "the receipt"
- "a drink" → "apple juice" / "a Sprite" / "iced coffee"

**Generic Quantities → Specific Quantities:**
- "expensive" → "fifteen dollars" / "seventy-five bucks"
- "a long time" → "forty minutes" / "two and a half hours"
- "a lot" → "like six" / "seventeen emails"

**Generic Times → Specific Times:**
- "recently" → "last Tuesday" / "three weeks ago" / "yesterday morning"
- "a while" → "twenty minutes" / "from 2012 to 2015"

**Generic Descriptions → Specific Details:**
- "weird" → "he was wearing a suit to the grocery store at 11 PM"
- "nice" → "she said 'have a blessed day' three times"
- "bad service" → "the waiter forgot we were there for forty minutes"

### Step 3: Maintain Truthfulness to Experience

Ensure specific details:
- Feel true to the general experience being described
- Are recognizable to the audience
- Don't shift the meaning unless that's intended
- Stay grounded in observable reality

**Good:** "a store" → "Walgreens" (specific, recognizable, truthful to common experience)
**Bad:** "a store" → "The Mystical Emporium of Rare Artifacts" (made up, not relatable)

### Step 4: Test Detail Level

Verify you've hit the requested detail level:

**Light:**
- Replace 30-40% of generic elements
- Focus on places and people
- Keep some intentional vagueness for rhythm

**Moderate (default):**
- Replace 60-70% of generic elements
- Include places, people, items, quantities
- Leave a few generic elements for conversational flow

**Hyper-specific:**
- Replace 90%+ of generic elements
- Add even more details than requested
- Include brand names, exact times, specific amounts
- Push into the rhythm of accumulating specificity

### Step 5: Preserve Conversational Flow

Check that specificity doesn't make it stilted:
- Read aloud to test rhythm
- Keep contractions and casual language
- Don't let precision make it formal
- Specific can still be conversational

---

## Outputs

**Primary Output:**
- Content with generic statements replaced by specific details

**Format:**
```
[SPECIFICITY-INJECTED VERSION]

[The transformed text]

---
[INJECTION REPORT]
Generic elements replaced: [number]
Detail level: [light/moderate/hyper-specific]
Key replacements:
- "[generic]" → "[specific]"
- "[generic]" → "[specific]"
- "[generic]" → "[specific]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content is already highly specific | Note minimal changes needed; show what few replacements improve it |
| Requested detail level conflicts with context | Explain the mismatch; recommend appropriate level (e.g., "Hyper-specific might be too much for this tweet") |
| Generic element is intentionally vague for effect | Preserve it; note in report why it was kept |
| Can't determine truthful specific replacement | Ask user for context or leave generic with note |
| Over-specification makes it unrelatable | Dial back; explain that specificity should enhance, not obscure |

---

## Example 1

**Input:**
```
Content: "I was at a restaurant and they gave me too many utensils. I asked the server about it but they didn't really care. The food was overpriced anyway."
Detail_level: "moderate"
```

**Output:**
```
[SPECIFICITY-INJECTED VERSION]

I was at this Italian place and they gave me four forks. Four forks. I asked the waiter "What am I supposed to do with four forks?" and he just shrugged. Also they charged fifteen dollars for pasta. Like regular pasta. Spaghetti with marinara sauce. Fifteen dollars.

---
[INJECTION REPORT]
Generic elements replaced: 7
Detail level: moderate

Key replacements:
- "a restaurant" → "this Italian place"
- "too many utensils" → "four forks" (repeated for emphasis)
- "the server" → "the waiter"
- "didn't really care" → "just shrugged" (specific action)
- "overpriced" → "fifteen dollars"
- "the food" → "pasta" → "Spaghetti with marinara sauce" (layered specificity)
```

---

## Example 2

**Input:**
```
Content: "Someone told me to try a popular restaurant but when I went there I waited a long time and then they were out of what I wanted to order."
Detail_level: "hyper-specific"
```

**Output:**
```
[SPECIFICITY-INJECTED VERSION]

My coworker Dave told me I had to try The Cheesecake Factory, said it was life-changing or whatever. So I went there on a Thursday night around 7:30 and waited forty-five minutes for a table. Forty-five minutes. Then I sat down, looked at the menu—which is like a phone book, it's got 250 items—and I decided I wanted the buffalo chicken sandwich. The waitress goes "Oh, we're out of that." It's 8:15 PM on a Thursday. How are you out of buffalo chicken sandwiches? This is The Cheesecake Factory. This is supposed to be your whole thing.

---
[INJECTION REPORT]
Generic elements replaced: 12
Detail level: hyper-specific

Key replacements:
- "Someone" → "My coworker Dave"
- "a popular restaurant" → "The Cheesecake Factory"
- "when I went there" → "Thursday night around 7:30"
- "waited a long time" → "forty-five minutes for a table" (with repetition)
- "what I wanted to order" → "the buffalo chicken sandwich"
- Added: "like a phone book, it's got 250 items" (bonus specificity)
- Added: "8:15 PM on a Thursday" (calculated from 7:30 + 45 min)
- "they were out of" → expanded with full reaction and questioning
```

---

## Example 3: Light Touch

**Input:**
```
Content: "I don't understand people who do that thing at coffee shops."
Detail_level: "light"
```

**Output:**
```
[SPECIFICITY-INJECTED VERSION]

I don't understand people who sit at Starbucks for four hours with one coffee.

---
[INJECTION REPORT]
Generic elements replaced: 3
Detail level: light

Key replacements:
- "coffee shops" → "Starbucks"
- "do that thing" → "sit... for four hours with one coffee"
- (Kept "people" generic for conversational flow)
```

---

## Integration with Hannibal Buress Expert

This skill directly applies the expert's core principle:
- **Specificity Over Generality:** "The detail IS the joke. 'Someone' is never as funny as 'my uncle' or 'the guy at Walgreens.'"

The skill provides a systematic approach to one of Hannibal Buress's most important techniques: grounding observations in concrete, specific reality.

---

## Advanced Usage

**Progressive specificity:**
- Start with light touch
- If it's not landing, increase to moderate
- Push to hyper-specific for maximum effect
- Find the sweet spot for the context

**Layered specificity:**
- Replace generic term with specific
- Then add another layer of detail to that specific
- Example: "food" → "pasta" → "spaghetti with marinara sauce" → "spaghetti with marinara sauce that was definitely from a jar"

**Specificity as rhythm:**
- Use repetition of specific detail for emphasis
- "Four forks. Four forks. What am I supposed to do with four forks?"
- The specificity becomes a beat

**Combine with other skills:**
- Use first, then apply `deadpan-rewrite` for tone
- Feed into `casual-escalation-builder` for development
- Enhance `sideways-angle-finder` results with concrete details

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].