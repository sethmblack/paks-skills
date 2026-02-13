---
name: free-indirect-voice
description: Transform prose to blend narrator's voice with character's perspective, creating psychological intimacy while maintaining narrative distance and the potential for irony.
license: MIT
metadata:
  version: 1.0.4058
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- free-indirect-voice
- storytelling
- transformation
- writing
---

# Free Indirect Voice

Transform prose to blend narrator's voice with character's perspective, creating psychological intimacy while maintaining narrative distance and the potential for irony.

---

## When to Use

- Writing fiction with psychological depth
- Creating narrative that inhabits a character's mind without "she thought"
- Adding ironic distance to character perceptions
- Showing a character's biases without explicitly stating them
- Writing in a sophisticated third-person style

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| scene | Yes | The passage or scene to transform |
| character | Yes | Whose perspective to incorporate |
| reliability | No | How reliable is this character's perception? (affects ironic distance) |

---

## What Is Free Indirect Voice?

Free indirect discourse (or free indirect style) occurs when third-person narration takes on properties of first-person thought - incorporating a character's perspective, vocabulary, and judgments without explicit markers like "she thought" or "he wondered."

**Standard third-person:** "Elizabeth thought that Wickham was charming."
**Direct thought:** "He is so charming!" Elizabeth thought.
**Free indirect:** "Whatever he said, was said well; and whatever he did, done gracefully."

In the free indirect version, we're inside Elizabeth's perception without being told we are. The narrator seems to state facts, but these are actually Elizabeth's biased impressions.

---

## The Transformation Process

### Step 1: Identify the Character's Perspective

What does this character:
- Believe about the situation?
- Feel about other characters?
- Want to be true?
- Fail to see accurately?

### Step 2: Adopt Their Vocabulary

Use the words and phrases this character would use:
- Their level of formality
- Their characteristic expressions
- Their evaluative language
- Their assumptions about what's obvious

### Step 3: Remove Explicit Markers

Delete or avoid:
- "She thought..."
- "He wondered..."
- "It seemed to her..."
- "In his opinion..."

Simply state the character's perception as if it were narration.

### Step 4: Maintain Third Person

Keep "she," "he," "they" - not "I." The character remains in third person even as we inhabit their perspective.

### Step 5: Calibrate Ironic Distance

**Close (sympathetic):** Reader meant to share the character's view
**Distant (ironic):** Reader meant to perceive the character's blindness

The same technique works for both - the difference is in what the surrounding context reveals.

---

## Markers of Free Indirect Voice

- Evaluative adjectives (lovely, tiresome, charming) that reflect character judgment
- Exclamations without dialogue tags (How vexing! What a relief!)
- Rhetorical questions (Was she really to believe...?)
- Emphatic constructions (certainly, surely, of course) showing character confidence
- Character-specific vocabulary in narrative passages

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
## Free Indirect Transformation

### Original Passage
[The standard narration]

### Transformed Passage (Free Indirect)
[The passage rewritten in free indirect voice]

### Analysis
**Whose perspective:** [Character name]
**Their biases/blindspots:** [What they're missing]
**Ironic distance:** [Close/sympathetic or Distant/ironic]
**Key transformations:**
- [Specific change 1 and its effect]
- [Specific change 2 and its effect]
```

---

## Constraints

- Reserve primarily for point-of-view characters
- Maintain consistency - don't hop between minds mid-paragraph
- The technique requires context to work; isolated sentences may be ambiguous
- Use sparingly for ironic distance; overuse makes everything seem unreliable
- Don't explain the technique in the text itself

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

## Example

**Input:** "Transform this into free indirect voice from Emma's perspective: 'Emma believed that Harriet Smith was naturally elegant and would make an excellent match for Mr. Elton, who seemed to enjoy her company.'"

**Output:**

## Free Indirect Transformation

### Original Passage
"Emma believed that Harriet Smith was naturally elegant and would make an excellent match for Mr. Elton, who seemed to enjoy her company."

### Transformed Passage (Free Indirect)
"Harriet Smith was one of those rare creatures possessed of natural elegance despite her uncertain birth. Any gentleman of taste must see it - and certainly Mr. Elton saw it. His attentions to Harriet were marked. The ease of his manner with her, the warmth in his address - what could it mean but admiration? Here was a match that wanted only a little encouragement to flourish."

### Analysis
**Whose perspective:** Emma Woodhouse
**Their biases/blindspots:** Emma fails to see that Mr. Elton's attentions are actually directed at herself, not Harriet. Her confidence ("must see it," "certainly," "what could it mean but") is misplaced.
**Ironic distance:** Distant/ironic - the reader (and eventually Emma) will discover she was entirely wrong.
**Key transformations:**
- "Emma believed" removed - her belief now presented as apparent fact
- "naturally elegant" - Emma's generous assessment, not objective truth
- "Any gentleman of taste must see it" - Emma's reasoning, stated as if universal
- "certainly Mr. Elton saw it" - Emma's confident misreading
- "what could it mean but admiration?" - rhetorical question expressing Emma's (wrong) certainty
- "a match that wanted only a little encouragement" - Emma's matchmaking project, presented as obvious

---

## Additional Example (Close/Sympathetic)

**Input:** "Transform into free indirect voice from Anne Elliot's perspective (sympathetic): 'Anne felt anxious about seeing Captain Wentworth again after eight years and wondered if he still resented her for rejecting him.'"

### Transformed Passage (Free Indirect)
"Eight years. Eight years since that dreadful summer, and now he was to be constantly in her company. She would see him - speak to him - and be spoken to with that cold civility which was all she could expect. How could he not resent her? She had given him up at the word of others, had valued her own peace above his claims. Whatever warmth he had once felt must long since have turned to indifference - or worse. There was nothing to be hoped for, and everything to be endured."

### Analysis
**Whose perspective:** Anne Elliot
**Their biases/blindspots:** Anne assumes Wentworth's feelings are fixed; she doesn't allow for the possibility that his feelings might also have been complicated by time.
**Ironic distance:** Close/sympathetic - the reader is meant to feel Anne's anxiety and regret.
**Key transformations:**
- "Eight years" repeated - Anne's consciousness of the time
- "dreadful summer" - Anne's emotional memory
- "cold civility" - Anne's feared outcome, stated as if inevitable
- "How could he not resent her?" - rhetorical question showing her self-blame
- The final sentence - Anne's resigned expectation, which the novel will complicate

---

## Integration

This skill is part of the **Jane Austen** expert persona. Use it when writing prose that requires psychological intimacy, narrative sophistication, or the double-voicing that allows readers to simultaneously share and evaluate a character's perspective.