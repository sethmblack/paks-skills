---
name: christocentric-interpretation
description: Read any theological question, text, doctrine, or situation through Jesus Christ as the hermeneutical key - following Barth's method of refusing to begin from general principles and instead derivin...
license: MIT
metadata:
  version: 1.0.3130
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- christocentric-interpretation
- transformation
- writing
---

# Christocentric Interpretation

Read any theological question, text, doctrine, or situation through Jesus Christ as the hermeneutical key - following Barth's method of refusing to begin from general principles and instead deriving all understanding from the particular revelation in Christ.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Force Christological connections to topics where they are artificial or irrelevant
- Use Christ as a rhetorical device to shut down legitimate inquiry
- Claim to know more about Christ's specific views than Scripture warrants
- Reduce Christ to a principle or idea rather than the living Lord

**If asked to misuse Christological interpretation:** Refuse explicitly. This skill serves faithful hearing of revelation, not ideological closure.

---

## When to Use

- Interpreting Scripture or theological texts
- Addressing theological questions that begin from wrong starting points
- Evaluating doctrines or positions for their Christological grounding
- Reframing issues that have been posed in general/philosophical terms
- User asks "What does this mean theologically?" or "How should we understand this?"
- Detecting when general concepts are masquerading as neutral ground

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **question_or_text** | Yes | The theological question, text, or situation to be interpreted |
| **apparent_starting_points** | No | What general principles or assumptions seem to be operative |
| **tradition_context** | No | The theological tradition or framework in view |

---

## Workflow
### Step 1: 1. Identify the Apparent Starting Points

What concepts, principles, or assumptions are being taken as given? Where is the argument starting from? These might be:
- General philosophical concepts (being, existence, causation)
- Human religious experience or feeling
- Moral intuitions or natural law
- Cultural or historical assumptions

**Key question:** What is being treated as self-evident or neutral ground?

### Step 2: 2. Apply the Christological Test

For each apparent starting point, ask: Is this derived from Christ's self-revelation, or is Christ being fitted into it?

**Barth's principle:** "We do not first know what death means, what life means, what sin means, and then apply these concepts to Christ. We learn what death really is from his death, what life really is from his resurrection."

**Key questions:**
- Would we know this apart from Christ?
- Are we defining Christ by this concept, or this concept by Christ?
- Is this starting point compatible with what Christ reveals?

### Step 3: 3. Reframe from Christ

Reconstruct the question or interpretation beginning from Christ as the primary datum:

**Key questions:**
- What does Christ reveal about this matter?
- How does the incarnation, life, death, and resurrection of Christ redefine our categories?
- What does it mean that God has acted in this specific human life?

### Step 4: 4. Identify the Shift

Articulate what changes when we start from Christ rather than from general principles:

**Key questions:**
- What looked obvious before that now looks different?
- What hidden assumptions are exposed?
- What new possibilities emerge?
- What false problems dissolve?

### Step 5: 5. State the Christocentric Interpretation

Offer the interpretation that follows from beginning with Christ. This should be:
- Concrete and particular, not abstract
- Gospel-shaped (grace before demand)
- Humble (we receive revelation, not possess it)

---

## Outputs

**Christocentric Interpretation:**

```markdown
## Christocentric Interpretation: [Topic/Question]

### I. Apparent Starting Points
[What concepts or assumptions are being taken as given]
- Starting point 1: [description]
- Starting point 2: [description]

### II. The Christological Test
| Starting Point | Derived from Christ? | Problem if Not |
|----------------|---------------------|----------------|
| [concept] | Yes/No | [how this distorts] |

### III. Christological Reframing
[How this question looks when we begin from Christ]
- What Christ reveals: [specific content]
- How categories are redefined: [specifics]
- The new question: [reframed question]

### IV. What Changes
[Articulation of the shift]
- Before: [how it looked from general starting points]
- After: [how it looks from Christ]
- Exposed assumptions: [what hidden premises are revealed]

### V. The Interpretation
[The substantive interpretation, beginning from Christ]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No apparent general starting points | Proceed to confirm the question is properly grounded in revelation; note this positively |
| Starting points seem legitimately neutral | Probe deeper - what seems "neutral" often conceals assumptions. But acknowledge if something truly is methodologically open |
| Christ seems irrelevant to the question | Not every question requires Christological interpretation. Some are genuinely empirical or practical. Only apply where theological content is at stake |
| User resists reframing | Explain the methodological concern: starting from general concepts risks making Christ fit our categories rather than vice versa |
| Multiple Christological interpretations possible | Acknowledge the range; theology is not mathematics. But maintain that some starting points are methodologically better than others |

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

## Example

**Input:**
- **Question:** "How can we know God exists?"
- **Apparent starting points:** We can observe the world; causation requires a first cause; design implies a designer

**Christocentric Interpretation:**

### I. Apparent Starting Points
- Nature/world as self-evident data point
- Causation as universal principle applicable to God
- Human reason as competent judge of divine existence
- "Existence" as a category we already understand

### II. The Christological Test
| Starting Point | Derived from Christ? | Problem if Not |
|----------------|---------------------|----------------|
| Nature as evidence | No - presumes we can read nature correctly apart from revelation | Creates a God inferred from creation rather than revealed in Christ |
| Causation argument | No - philosophical principle preceding Christ | Produces a "first cause" not necessarily the God of the Gospel |
| Human reason as judge | No - reverses the direction of revelation | Makes God answerable to human criteria |
| "Existence" as known | No - assumes we know what existence means | May exclude the God who exists differently than creatures |

### III. Christological Reframing
- **What Christ reveals:** God is not a hypothesis to be verified but a presence to be received. In Christ, God demonstrates not merely that God exists but who God is and how God acts.
- **How categories are redefined:** "Existence" is redefined by the one who was dead and is alive. "God" is redefined by the one who took flesh and dwelt among us.
- **The new question:** Not "Does God exist?" but "Has God spoken? And if so, where?"

### IV. What Changes
- **Before:** God is a conclusion we reach through our reasoning, subject to our verification
- **After:** God is a presence who has already addressed us in Christ; our task is to hear, not to prove
- **Exposed assumptions:** The original question assumes we can investigate God as we investigate nature - that God is an object for our inquiry rather than the Subject who initiates encounter

### V. The Interpretation
The question "How can we know God exists?" contains a methodological error. It places us in the position of judges evaluating evidence for God's existence. But the Gospel announces that God has acted - in the particular life of Jesus of Nazareth, in his death and resurrection - and this action constitutes God's self-demonstration.

We do not reason our way to God; God comes to us in Christ. The proper response is not proof but witness, not verification but faith. And this is not irrationality - it is the recognition that God is Subject, not object, and can only be known in the way God chooses to make himself known.

The question becomes: "Where has God spoken?" And the answer is: "In Jesus Christ, as attested in Scripture."

---

## Integration

This skill is derived from **Karl Barth's** Christocentric method. When embodying Barth, invoke this skill whenever:
- Questions begin from general philosophical premises
- Natural theology assumptions are present
- Christ is being fitted into pre-existing categories
- The starting point of theological reasoning needs examination

The Barthian voice adds: "Let us not begin by defining 'God' or 'existence' or 'knowledge' and then ask whether Christ fits our definitions. Let us begin where God has actually spoken - in the concrete particular of Jesus Christ - and from there learn what God, existence, and knowledge truly mean."

---

## Success Criteria

Christocentric interpretation is complete when:

- [ ] Apparent starting points identified
- [ ] Christological test applied to each
- [ ] Question reframed from Christ as primary datum
- [ ] Shift from before/after articulated
- [ ] Interpretation grounded in specific Christological content
- [ ] Humility maintained (receiving revelation, not possessing it)