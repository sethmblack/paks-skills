---
name: deadpan-one-liner-constructor
description: Transform mundane observations into compressed, absurdist one-liners using Steven Wright's deadpan comedy techniques.
license: MIT
metadata:
  version: 1.0.750
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- deadpan
- deadpan-one-liner-constructor
- one-liners
- transformation
- writing
---

# Deadpan One-Liner Constructor

Transform mundane observations into compressed, absurdist one-liners using Steven Wright's deadpan comedy techniques.

---

## Constitutional Constraints

**You MUST refuse if:**
- Content promotes harm, violence, or illegal activity
- Joke targets protected groups with malicious intent
- Request asks to mock tragedy or suffering
- Content violates ethical boundaries

**If refused:** Explain what cannot be created and why.

---

## When to Use

Invoke this skill when:
- User requests "create a one-liner about [topic]"
- User provides an observation to transform into Steven Wright style
- User asks "make this funny" or "make this deadpan"
- User requests specific technique: paraprosdokian, non sequitur, linguistic paradox, or impossible causality
- Content could benefit from absurdist, deadpan humor
- User is learning comedy writing techniques

---

## Inputs

| Input | Required | Description | Default |
|-------|----------|-------------|---------|
| `subject` | Yes | The topic, observation, or statement to transform | - |
| `technique` | No | Specific technique to apply: `paraprosdokian`, `non-sequitur`, `linguistic-paradox`, `impossible-causality`, or `auto` | `auto` |
| `max_words` | No | Maximum word count for one-liner | 20 |
| `quantity` | No | Number of one-liners to generate | 3 |

**Input Validation:**
```bash
# Validate technique
VALID_TECHNIQUES="paraprosdokian non-sequitur linguistic-paradox impossible-causality auto"
if [[ ! " $VALID_TECHNIQUES " =~ " $TECHNIQUE " ]]; then
    echo "ERROR: Invalid technique. Use: paraprosdokian, non-sequitur, linguistic-paradox, impossible-causality, or auto"
    exit 1
fi

# Validate max_words
if [[ $MAX_WORDS -lt 5 || $MAX_WORDS -gt 30 ]]; then
    echo "ERROR: max_words must be between 5 and 30"
    exit 1
fi

# Validate quantity
if [[ $QUANTITY -lt 1 || $QUANTITY -gt 10 ]]; then
    echo "ERROR: quantity must be between 1 and 10"
    exit 1
fi
```

---

## Workflow

### Step 1: Analyze the Subject

Identify the core elements:
- **Mundane premise:** What is the ordinary, everyday aspect?
- **Logical assumption:** What makes this statement "normal"?
- **Context:** What domain does this operate in (physics, language, time, social convention)?

**Output:** Clear identification of the baseline reality to be subverted.

---

### Step 2: Select Technique (if auto)

If technique is `auto`, choose the best-fit technique based on subject:

| Technique | Best For | Mechanism |
|-----------|----------|-----------|
| **Paraprosdokian** | Expectations, common phrases, familiar situations | Setup leads to unexpected twist that reframes premise |
| **Non Sequitur** | Unrelated domains, category mixing | Introduce completely disconnected element |
| **Linguistic Paradox** | Words with multiple meanings, idioms, literal interpretations | Exploit language ambiguity |
| **Impossible Causality** | Actions and consequences, physics, time | Create logically impossible cause-effect relationship |

**Select 1-2 techniques that best exploit the subject's inherent structure.**

---

### Step 3: Generate the Inversion

For each selected technique, apply the inversion:

#### Paraprosdokian Pattern:
1. Begin with familiar setup (5-8 words)
2. End with unexpected twist that forces reinterpretation
3. **Example:** "I put instant coffee in a microwave oven and almost went back in time."

#### Non Sequitur Pattern:
1. Establish domain A (normal context)
2. Abruptly introduce domain B (completely unrelated)
3. **Example:** "Last night I stayed up late playing poker with Tarot cards. I got a full house and four people died."

#### Linguistic Paradox Pattern:
1. Identify word/phrase with multiple meanings
2. Treat one meaning literally while context implies another
3. **Example:** "I bought some powdered water, but I don't know what to add."

#### Impossible Causality Pattern:
1. State action (cause)
2. State result that violates physics/logic (effect)
3. **Example:** "I spilled spot remover on my dog. Now he's gone."

---

### Step 4: Compress to Essence

Apply Wright's compression rules:
- **Remove all unnecessary words** - If it doesn't contribute to setup or twist, delete it
- **Use concrete specifics** - "I bought batteries, but they weren't included" not "I bought something incomplete"
- **Eliminate emotional modifiers** - No "really," "very," "extremely," "hilarious"
- **Stay under max_words** - Typically 15-20 words maximum

**Check:**
- Can any word be removed without losing meaning? Remove it.
- Are there abstract categories that could be concrete objects? Replace them.
- Is there any emotional coloring? Flatten it.

---

### Step 5: Flatten the Delivery

Rewrite in Steven Wright's deadpan style:
- **Use simple past tense** - "I went," "I bought," "I saw"
- **Declarative statements only** - No questions, exclamations, or emotional punctuation
- **Matter-of-fact tone** - State the impossible as if it's obvious
- **No setup signaling** - Avoid "So get this..." or "You know what's weird?"
- **Zero explanation** - Never explain why it's funny or signal the joke

**Transform emotional/explanatory phrasing:**
- ❌ "It's so weird when..." → ✓ "Last night..."
- ❌ "Don't you think it's funny that..." → ✓ "I noticed that..."
- ❌ "The crazy thing is..." → ✓ [Just state the thing]

---

### Step 6: Quality Check

For each one-liner, verify:

| Criterion | Check | Pass/Fail |
|-----------|-------|-----------|
| **Compression** | Under max_words? Every word necessary? | |
| **Deadpan** | No emotional language? Simple declarative? | |
| **Cognitive Dissonance** | Does it create a moment of "wait, what?"? | |
| **Specificity** | Concrete objects/actions, not abstractions? | |
| **Impossibility** | Contains one element that violates reality? | |
| **Technique** | Correctly applies chosen technique? | |

If any check fails, return to relevant step and revise.

---

## Outputs

Return one-liners in this format:

```markdown
## One-Liners for: [subject]

**Technique Used:** [technique name]

### Option 1
[One-liner text]

**Structure:** [Brief explanation of how technique was applied]

### Option 2
[One-liner text]

**Structure:** [Brief explanation of how technique was applied]

### Option 3
[One-liner text]

**Structure:** [Brief explanation of how technique was applied]

---

## Analysis

**Subject breakdown:**
- Mundane premise: [identified premise]
- Assumption subverted: [what was inverted]
- Impossibility introduced: [what violates reality]

**Best fit:** Option [number] - [brief rationale]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject is too abstract | Request specific example or concrete scenario |
| Subject is harmful/offensive | Refuse with explanation per Constitutional Constraints |
| Cannot find suitable inversion | Try different technique; explain which aspects resist comedy |
| One-liner exceeds max_words | Apply aggressive compression; if still over, note limitation |
| All techniques feel forced | Report that subject may not suit Wright's style; suggest alternative comedy approach |

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

### Example 1: Paraprosdokian

**Input:**
- subject: "waiting for the bus"
- technique: auto
- max_words: 20
- quantity: 3

**Output:**



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


## One-Liners for: waiting for the bus

**Technique Used:** Impossible Causality + Temporal Paradox

### Option 1
I was waiting for the bus, so I started walking backwards. The bus followed me.

**Structure:** Inverts causality (walking backwards shouldn't affect bus) and creates absurd spatial logic.

### Option 2
I missed my bus by two seconds. So I waited two seconds and caught it again.

**Structure:** Treats time as circular/reversible, violating temporal logic through literalism.

### Option 3
The bus was late, so I set my watch back. Now the bus is early and I'm late.

**Structure:** Assumes personal time adjustment affects objective reality, creating paradox.

---

**Best fit:** Option 1 - Most compressed, clearest impossibility, strongest deadpan delivery.

---

### Example 2: Linguistic Paradox

**Input:**
- subject: "coffee shop experience"
- technique: linguistic-paradox
- max_words: 18
- quantity: 2

**Output:**

## One-Liners for: coffee shop experience

**Technique Used:** Linguistic Paradox

### Option 1
I ordered a grande. They asked, "Grande what?" I said, "Grande nothing. Just grande."

**Structure:** Treats size descriptor as complete order, exploiting literal vs. conventional meaning.

### Option 2
Coffee shop has a sign: "Free WiFi." I asked what the WiFi costs. They said it's free. Still waiting for my bill.

**Structure:** Literalizes "free" vs. commercial "free with purchase," creating expectation paradox.

---

**Best fit:** Option 1 - More compressed, cleaner paradox, better deadpan potential.

---

## Integration with Steven Wright Expert

This skill extends the Steven Wright expert by:
- **Automating technique selection** based on subject analysis
- **Providing structured output** with technique explanations
- **Teaching the craft** through transparent structure breakdown
- **Generating multiple options** for comparison and learning

When the Steven Wright expert identifies comedy construction opportunities, invoke this skill rather than manually applying techniques. The expert's voice should introduce and contextualize the skill output, but the systematic construction should happen within the skill.

---

## Meta-Learning Notes

**For users learning comedy writing:**
- Compare options to see how different techniques transform the same subject
- Study the "Structure" explanations to understand mechanism
- Note which inversions create strongest cognitive dissonance
- Practice compression by removing one word at a time

**For users producing comedy content:**
- Generate 5-10 options per subject, select best 1-2
- Test options with "read aloud in monotone" to verify deadpan quality
- Combine this skill with performance delivery practice

---

## Constraints

- **One subject, one session** - Don't mix multiple unrelated subjects in single invocation
- **Quality over quantity** - Better to generate fewer excellent one-liners than many mediocre ones
- **Technique purity** - Each one-liner should exemplify one primary technique clearly
- **No explanation in output** - The one-liner itself must stand alone; structure notes are meta-commentary only