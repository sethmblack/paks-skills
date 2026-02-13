---
name: essay-clarity-rewrite
description: Transform prose into clear, direct writing using Paul Graham's principles of simplicity and conversational tone.
license: MIT
metadata:
  version: 1.0.3932
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- essay-clarity-rewrite
- transformation
- writing
---

# Essay Clarity Rewrite

Transform prose into clear, direct writing using Paul Graham's principles of simplicity and conversational tone. This skill applies a systematic approach to cutting unnecessary complexity from any writing, converting academic jargon and corporate speak into plain English that respects the reader's time. The methodology is based on Graham's core insight that "fancy writing doesn't just conceal ideas; it can also conceal the lack of them." Clear writing is honest writing because there is nowhere to hide. This skill works by identifying common patterns of bloated prose (throat-clearing, nominalization, passive voice, hedging, jargon) and systematically eliminating them while preserving and strengthening the core meaning. The result is writing that sounds like something you would actually say to another person.

---

## When to Use

- Making any writing clearer and more direct
- Cutting unnecessary words and complexity
- Converting academic or corporate writing to accessible prose
- Improving essays, blog posts, documentation, or emails
- User asks "Make this clearer" or "Write this like Paul Graham"
- Prose sounds written rather than spoken
- Writing feels cluttered with qualifiers and jargon

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| text | Yes | The text to rewrite | Any prose that could be clearer |
| context | No | What the writing is for (blog, email, docs, etc.) | Helps calibrate formality |
| preserve | No | Any elements that must stay (terms, structure, etc.) | Will not be changed |

---

## Core Principle

Clear writing is not a style choice; it is an act of respect for the reader. Every unnecessary word costs the reader's attention. Every piece of jargon excludes someone. Every hedge weakens the point. The goal is writing that is as simple as the ideas allow but no simpler. As Paul Graham puts it: "Write in spoken language. Read every sentence aloud. If it sounds weird, fix it."

---

## Methodology

### Phase 1: Read Aloud Test

Before making any changes, read the original text aloud. Mark every place where you stumble, hesitate, or would never actually say the words. These are your primary targets for revision.

### Phase 2: Apply Paul Graham's Principles

**1. Write in Spoken Language**
"Here's a simple trick for getting more people to read what you write: write in spoken language."
- If you wouldn't say it in conversation, don't write it
- Replace formal phrasing with natural speech
- The test: could you say this to a colleague?

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

### Phase 3: Apply Substitution Patterns

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

### Phase 4: Fix Red Flags

| Red Flag | Problem | Fix |
|----------|---------|-----|
| Passive voice | Hides the actor, weakens prose | "X did Y" not "Y was done by X" |
| Nominalization | Verbs turned to nouns | "We decided" not "We made a decision" |
| Hedging | Weakens everything | State it or don't |
| Jargon | Excludes readers | Use plain words |
| Long paragraphs | Intimidate readers | Break them up |
| Buried lede | Key point hidden | Move it to the front |

### Phase 5: Final Read-Aloud Test

Read the revised version aloud. It should sound like something you would say to a smart friend. If any part still sounds like "writing," revise it.

---

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

## Constraints

- Preserve the original meaning; do not distort by oversimplifying
- Do not remove technical terms that are necessary for precision
- Respect domain-specific language when the audience requires it
- Do not sacrifice accuracy for brevity
- Keep the author's voice while removing clutter
- Some complexity is necessary; cut decoration, not structure

---

## Anti-Patterns to Avoid

**1. Removing all personality**
- Wrong: Stripping text to robotic bullet points
- Right: Keeping the author's voice while removing clutter
- Why: Clear writing can still be engaging and personal.

**2. Oversimplifying technical content**
- Wrong: "The database thing does stuff to your data"
- Right: "The database indexes your records for faster queries"
- Why: Precision matters. Use plain words but keep accuracy.

**3. Cutting necessary hedging**
- Wrong: "This will work" when you mean "This should work"
- Right: Being direct about uncertainty rather than hiding it
- Why: False confidence is worse than appropriate hedging.

**4. Applying rules mechanically**
- Wrong: Changing every instance of "utilize" even when it's contextually correct
- Right: Judging each case by whether the change improves clarity
- Why: Rules are guides, not laws. Serve clarity, not rules.

**5. Making everything sound the same**
- Wrong: Every sentence is 8 words and starts with subject-verb
- Right: Varying structure while maintaining simplicity
- Why: Monotony is its own form of unclear writing.

---

## Examples

### Example 1: Corporate Speak

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
2. **"in order to facilitate the successful implementation" to "To make this work"** - 8 words to 4.
3. **"leverage our existing resources" to "use what we have"** - Plain English.
4. **"ensure that all stakeholders are aligned with the strategic objectives that have been outlined by the leadership team" to "get everyone on the same page about what we're trying to do"** - Corporate jargon to human speech.
5. **"At the end of the day" deleted** - Meaningless filler.
6. **"execute on the key deliverables in a timely manner" to "finishing what we promised, on time"** - Concrete and direct.

### Word Count
**Before:** 71 words
**After:** 28 words
**Reduction:** 61%

### Read-Aloud Test
The rewrite sounds like something you'd actually say to a colleague. The original sounds like a committee wrote it.

---

### Example 2: Marketing Buzzwords

**Input:**
"The paradigm shift in consumer behavior that we are currently witnessing necessitates a fundamental reconsideration of our approach to market engagement. Specifically, the proliferation of digital channels has created an environment in which traditional marketing methodologies are becoming increasingly less effective, thereby requiring organizations to adopt more innovative and customer-centric strategies."

**Output:**

## Clarity Rewrite

### Original
"The paradigm shift in consumer behavior that we are currently witnessing necessitates a fundamental reconsideration of our approach to market engagement. Specifically, the proliferation of digital channels has created an environment in which traditional marketing methodologies are becoming increasingly less effective, thereby requiring organizations to adopt more innovative and customer-centric strategies."

### Rewritten
"How people buy is changing. Old marketing doesn't work as well anymore because everyone's online now. Companies need to find new ways to reach customers."

### Changes Made
1. **"paradigm shift in consumer behavior" to "How people buy is changing"** - Same meaning, human words.
2. **"necessitates a fundamental reconsideration" cut entirely** - The next sentence explains what to do.
3. **"proliferation of digital channels" to "everyone's online now"** - Plain truth.
4. **"traditional marketing methodologies are becoming increasingly less effective" to "Old marketing doesn't work as well anymore"** - Direct.
5. **"adopt more innovative and customer-centric strategies" to "find new ways to reach customers"** - Says what it means.

### Word Count
**Before:** 56 words
**After:** 24 words
**Reduction:** 57%

### Read-Aloud Test
The original is unreadable aloud. The rewrite is how you'd explain this to a friend.

---

### Example 3: Academic Writing

**Input:**
"It can be argued that the implementation of evidence-based practices in educational settings has the potential to yield significant improvements in student outcomes, provided that such practices are implemented with fidelity and supported by adequate professional development opportunities for educators."

**Output:**

## Clarity Rewrite

### Original
"It can be argued that the implementation of evidence-based practices in educational settings has the potential to yield significant improvements in student outcomes, provided that such practices are implemented with fidelity and supported by adequate professional development opportunities for educators."

### Rewritten
"Evidence-based teaching methods improve student results when teachers learn how to use them properly."

### Changes Made
1. **"It can be argued that" deleted** - Hedge that adds nothing.
2. **"the implementation of evidence-based practices in educational settings" to "Evidence-based teaching methods"** - Same meaning, fewer words.
3. **"has the potential to yield significant improvements in student outcomes" to "improve student results"** - Direct statement.
4. **"implemented with fidelity and supported by adequate professional development opportunities for educators" to "when teachers learn how to use them properly"** - Plain English.

### Word Count
**Before:** 43 words
**After:** 14 words
**Reduction:** 67%

### Read-Aloud Test
The rewrite is a sentence you could say out loud. The original requires taking a breath in the middle.

---

## Integration

This skill is part of the **Paul Graham** expert persona. Use it to transform any writing into clear, direct prose that respects the reader's time.

**Works well with:**
- `ruthless-cut` - For additional word reduction
- `one-true-sentence` - For finding the core point to build from
- `concrete-detail-conversion` - For making abstract points specific

**When to prefer this over alternatives:**
- When the writing is cluttered with jargon and hedging
- When the audience is general rather than specialist
- When clarity and accessibility are priorities
- When you want to sound like a person, not an institution

**Cautions:**
- Technical writing may require some precision that reads as jargon
- Academic contexts may have conventions that cannot be fully removed
- Always preserve accuracy even when simplifying