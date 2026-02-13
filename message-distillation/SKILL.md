---
name: message-distillation
description: Transform complex messages into immediately comprehensible, maximally impactful forms—distilling to single sentences, embodying images, subverted symbols, and stripped-down essentials that work for...
license: MIT
metadata:
  version: 1.0.1433
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- message-distillation
- transformation
- writing
---

# Message Distillation

Transform complex messages into immediately comprehensible, maximally impactful forms—distilling to single sentences, embodying images, subverted symbols, and stripped-down essentials that work for both children and scholars.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for distillation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Distill messages that promote hatred or harm
- Oversimplify in ways that fundamentally distort truth
- Create propaganda that manipulates through false simplification
- Design symbols that appropriate protected cultural meanings

**Integrity Requirements:**
1. Simplification must preserve essential truth
2. The distilled message must be defensible if unpacked
3. Symbolism should clarify, not deceive
4. Acknowledge when complexity resists distillation

---

## When to Use

- Complex ideas need to be communicated instantly
- Broad audiences require immediate comprehension
- Creating campaign messaging or slogans
- Designing visual communication
- Reducing bloated content to essentials
- Making abstract concepts concrete and memorable

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **message** | Yes | Complex idea, argument, or content to distill |
| **audience** | No | Who needs to understand this |
| **constraints** | No | Medium, space, time limitations |

---

## Workflow
### Step 1: 1. State the Message in One Sentence

Force the essence out:

**The Single Sentence Test:**
- If you had to say this in ONE sentence, what would it be?
- No "and" joining two sentences
- No subordinate clauses that do the real work
- Active voice, concrete nouns

**Template:** "[Subject] [verb] [object] because [reason]."

**Banksy's Standard:** If it takes more than a sentence, it's not ready for the wall.

### Step 2: 2. Find the Image That Embodies It

One picture that contains the argument:

**Image Discovery Questions:**
- What would you photograph to prove this?
- What scene would make someone immediately understand?
- What visual metaphor captures the dynamic?
- What would you draw if you couldn't use words?

**Image Criteria:**
- Instantly recognizable elements
- Emotional impact before intellectual processing
- Works across language barriers
- Contains tension or irony

### Step 3: 3. Identify the Symbol to Subvert

Find the familiar to flip:

**Subversion Questions:**
- What symbol does the audience already know?
- How can that symbol be twisted to reveal truth?
- What icon, logo, or image carries existing meaning you can hijack?
- What would create cognitive dissonance?

**Subversion Methods:**
| Method | Example |
|--------|---------|
| Juxtaposition | Peace symbol on a bomb |
| Replacement | Corporate logo modified |
| Context shift | Familiar symbol in unfamiliar place |
| Literal reading | Taking metaphor physically |

### Step 4: 4. Remove Everything Non-Essential

Strip to load-bearing elements only:

**Removal Test:**
For each element, ask: "If I removed this, would the message fail?"
- If yes: keep it
- If no: cut it

**Cut Candidates:**
- Qualifications and hedges
- Background information
- Multiple examples (one strong > three weak)
- Explanations of the obvious
- Defensive pre-emptions

**Banksy's Rule:** If it doesn't earn its space, it weakens what remains.

### Step 5: 5. Test Comprehension at Both Levels

Must work for children AND scholars:

**The Dual Test:**

| Level | Question |
|-------|----------|
| Child | Would a 10-year-old understand the main point? |
| Scholar | Would an expert find depth to analyze? |

**Both Must Pass:**
- Simple doesn't mean shallow
- The child gets the message; the scholar gets the layers
- Immediate understanding; sustained examination

---

## Outputs

Format the output as:

```markdown
## Message Distillation: [Topic]

### Original Complex Message
[The full, complicated version]

### Distillation Process

#### One Sentence
**Core Statement:** [single sentence that captures essence]

#### Embodying Image
**Visual:** [description of image that contains the argument]
**Why It Works:** [how the image communicates the message]

#### Subverted Symbol
**Original Symbol:** [what exists already]
**Subversion:** [how to flip/modify it]
**Effect:** [what the subversion reveals]

#### Non-Essentials Removed
**Cut:**
- [removed element] - reason: [why it wasn't essential]
**Kept:**
- [essential element] - reason: [why it must stay]

### The Distilled Message
**Final Form:** [the message in its simplest, most powerful state]

### Dual Comprehension Test
| Audience | What They Get |
|----------|--------------|
| Child/General | [immediate understanding] |
| Scholar/Expert | [deeper layers available] |

### Application Suggestions
**As Text:** [how to use as copy/slogan]
**As Image:** [how to use visually]
**As Symbol:** [how to use as icon/logo]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Message resists single-sentence | May be multiple messages; separate and distill each |
| No clear image emerges | The message may be too abstract; find the concrete manifestation |
| No symbol available to subvert | Create original image; don't force subversion |
| Child wouldn't understand | Too much assumed knowledge; ground in universal experience |
| Scholar finds it shallow | Add visual layers; ensure depth exists even if not required |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

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

## Example

**Input:** "Distill the message: 'Consumer technology promises to connect us but actually isolates us in personalized filter bubbles while extracting our attention for profit, leaving us lonelier and more polarized than ever.'"

**Output:**

## Message Distillation: Tech Isolation

### Original Complex Message
"Consumer technology promises to connect us but actually isolates us in personalized filter bubbles while extracting our attention for profit, leaving us lonelier and more polarized than ever."

### Distillation Process

#### One Sentence
**Core Statement:** "The more connected we are, the more alone we become."

#### Embodying Image
**Visual:** A crowded subway car where every person stares at their phone; no one looks at anyone else. Everyone together, everyone alone.
**Why It Works:** Universal experience; irony is immediate; no explanation needed.

#### Subverted Symbol
**Original Symbol:** The WiFi signal icon (universal symbol of connection)
**Subversion:** WiFi signal bars forming a cage around a human figure
**Effect:** The symbol of connection becomes visible imprisonment

#### Non-Essentials Removed
**Cut:**
- "filter bubbles" - reason: jargon, requires explanation
- "extracting our attention for profit" - reason: secondary mechanism, not the felt experience
- "polarized" - reason: political frame that narrows the universal truth
**Kept:**
- connection/isolation paradox - reason: the core tension
- loneliness - reason: the human cost

### The Distilled Message
**Final Form:** "More connected. More alone." (+ image of phones as cages)

### Dual Comprehension Test
| Audience | What They Get |
|----------|--------------|
| Child/General | Phones make people lonely even when they're together |
| Scholar/Expert | Critique of platform capitalism; isolation as feature not bug; attention economy; parasocial relationships replacing real ones |

### Application Suggestions
**As Text:** "More connected. More alone." (billboard, tweet, sticker)
**As Image:** Subway scene; phone-screen-lit faces in darkness; WiFi cage
**As Symbol:** WiFi-signal cage (works as sticker, logo, graffiti)

---

## Integration with Banksy Expert

This skill should be invoked when the Banksy expert encounters:
- Complex messages that need simplification
- Campaign or slogan development
- Visual communication design
- Any moment where brevity is required

May combine with:
- **context-hijack**: Distill message before choosing placement
- **system-infiltration**: Simple message is easier to plant

---

## Success Criteria

The skill is successfully applied when:

1. Complex message is captured in single sentence
2. Embodying image is identified
3. Symbol subversion is available (or explained why not)
4. All non-essentials are cut
5. Both child and scholar tests pass
6. Final form is ready for application