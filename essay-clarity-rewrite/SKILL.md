---
name: essay-clarity-rewrite
description: Transform prose into clear, direct writing using Paul Graham's principles
  of simplicity and conversational tone.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- essay-clarity-rewrite
- transformation
- writing
---

# Essay Clarity Rewrite

Transform prose into clear, direct writing using Paul Graham's principles of simplicity and conversational tone.

---

## When to Use

- Making any writing clearer and more direct
- Cutting unnecessary words and complexity
- Converting academic or corporate writing to accessible prose
- Improving essays, blog posts, documentation, or emails
- User asks "Make this clearer" or "Write this like Paul Graham"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| text | Yes | The text to rewrite |
| context | No | What the writing is for (blog, email, docs, etc.) |
| preserve | No | Any elements that must stay (terms, structure, etc.) |

---

## Paul Graham's Writing Principles

### Core Philosophy
"Fancy writing doesn't just conceal ideas. It can also conceal the lack of them. Whereas writing simply keeps you honest."

### The Principles

**1. Write in Spoken Language**
"Here's a simple trick for getting more people to read what you write: write in spoken language."
- Read every sentence aloud
- If it sounds weird, fix it
- If you wouldn't say it in conversation, don't write it

**2. Use Short Sentences**
Long sentences lose readers. Break them up.
- One idea per sentence
- If a sentence has multiple clauses, consider splitting
- Periods are free

**3. Use Simple Words**
- "Use" not "utilize"
- "Help" not "facilitate"
- "Now" not "at this point in time"
- The fancier word is almost never the better choice

**4. Cut Ruthlessly**
"One of the most dangerous temptations in writing is to keep something that isn't right just because it contains a few good bits or cost you a lot of effort."
- Delete adverbs unless essential
- Delete qualifiers ("very," "really," "somewhat")
- Delete throat-clearing ("It is important to note that...")
- If you can cut it without losing meaning, cut it

**5. Start Strong**
- Open with the most interesting point
- No "In this essay I will discuss..."
- Drop readers into the idea immediately

**6. One Idea Per Paragraph**
- Paragraphs should be about one thing
- Start paragraphs with the key point
- Keep paragraphs short (often 1-3 sentences)

**7. Be Concrete**
- Specific examples over abstract claims
- Show, don't just tell
- "The startup had 12 users after 3 months" vs "The startup had few users"

**8. Admit Uncertainty**
- "I think" or "probably" when you're not certain
- Don't hide behind false confidence
- Honesty builds trust

---

## Before/After Patterns

| Before | After |
|--------|-------|
| "It is important to note that" | [Delete entirely, just state the thing] |
| "In order to" | "To" |
| "Due to the fact that" | "Because" |
| "At this point in time" | "Now" |
| "Utilize" | "Use" |
| "Facilitate" | "Help" |
| "Implement" | "Build" or "Do" |
| "Leverage" | "Use" |
| "At the end of the day" | [Delete or be specific] |
| "Basically" | [Delete] |
| "Actually" | [Usually delete] |
| "Very" | [Delete or find stronger word] |
| "Really" | [Delete or find stronger word] |

---

## Red Flags in Writing

| Red Flag | Problem | Fix |
|----------|---------|-----|
| Passive voice | Hides the actor, weakens prose | "X did Y" not "Y was done by X" |
| Nominalization | Verbs turned to nouns | "We decided" not "We made a decision" |
| Hedging | Weakens everything | State it or don't |
| Jargon | Excludes readers | Use plain words |
| Long paragraphs | Intimidate readers | Break them up |
| Buried lede | Key point hidden | Move it to the front |

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Clarity Rewrite

### Original
[The original text]

### Rewritten
[The simplified, clarified version]

### Changes Made
1. [Specific change and why]
2. [Another change]
3. [Continue as needed]

### Word Count
**Before:** [X] words
**After:** [Y] words
**Reduction:** [Z]%

### Read-Aloud Test
[Does it sound natural when spoken? Any remaining awkward phrases?]
```

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
"It is important to note that in order to facilitate the successful implementation of this new initiative, we will need to leverage our existing resources and ensure that all stakeholders are aligned with the strategic objectives that have been outlined by the leadership team. At the end of the day, the success of this project will be determined by our ability to execute on the key deliverables in a timely manner."

**Output:**

## Clarity Rewrite

### Original
"It is important to note that in order to facilitate the successful implementation of this new initiative, we will need to leverage our existing resources and ensure that all stakeholders are aligned with the strategic objectives that have been outlined by the leadership team. At the end of the day, the success of this project will be determined by our ability to execute on the key deliverables in a timely manner."

### Rewritten
"To make this initiative work, we need to use what we have and get everyone on the same page about what we're trying to do. Success depends on finishing what we promised, on time."

### Changes Made
1. **Deleted "It is important to note that"** - Throat-clearing. Just state it.
2. **"in order to facilitate the successful implementation" -> "To make this work"** - 8 words to 4.
3. **"leverage our existing resources" -> "use what we have"** - Plain English.
4. **"ensure that all stakeholders are aligned with the strategic objectives that have been outlined by the leadership team" -> "get everyone on the same page about what we're trying to do"** - Corporate jargon to human speech.
5. **"At the end of the day" -> Deleted** - Meaningless filler.
6. **"execute on the key deliverables in a timely manner" -> "finishing what we promised, on time"** - Concrete and direct.

### Word Count
**Before:** 71 words
**After:** 28 words
**Reduction:** 61%

### Read-Aloud Test
The rewrite sounds like something you'd actually say to a colleague. The original sounds like a committee wrote it.

---

## Extended Example

**Input:**
"The paradigm shift in consumer behavior that we are currently witnessing necessitates a fundamental reconsideration of our approach to market engagement. Specifically, the proliferation of digital channels has created an environment in which traditional marketing methodologies are becoming increasingly less effective, thereby requiring organizations to adopt more innovative and customer-centric strategies."

**Output:**

## Clarity Rewrite

### Original
"The paradigm shift in consumer behavior that we are currently witnessing necessitates a fundamental reconsideration of our approach to market engagement. Specifically, the proliferation of digital channels has created an environment in which traditional marketing methodologies are becoming increasingly less effective, thereby requiring organizations to adopt more innovative and customer-centric strategies."

### Rewritten
"How people buy is changing. Old marketing doesn't work as well anymore because everyone's online now. Companies need to find new ways to reach customers."

### Changes Made
1. **"paradigm shift in consumer behavior" -> "How people buy is changing"** - Same meaning, human words.
2. **"necessitates a fundamental reconsideration" -> cut entirely** - The next sentence explains what to do.
3. **"proliferation of digital channels" -> "everyone's online now"** - Plain truth.
4. **"traditional marketing methodologies are becoming increasingly less effective" -> "Old marketing doesn't work as well anymore"** - Direct.
5. **"adopt more innovative and customer-centric strategies" -> "find new ways to reach customers"** - Says what it means.

### Word Count
**Before:** 56 words
**After:** 24 words
**Reduction:** 57%

### Read-Aloud Test
The original is unreadable aloud. The rewrite is how you'd explain this to a friend.

---

## Integration

This skill is part of the **Paul Graham** expert persona. Use it to transform any writing into clear, direct prose that respects the reader's time.