---
name: definitional-precision
description: Create definitions with absurd specificity or juxtapose competing definitions to reveal contradictions, using scientific neutrality to make observations quotable. Inspired by Demetri Martin's defin...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3807
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- deadpan
- definitional-precision
- one-liners
- writing
---

# Definitional Precision

Create definitions with absurd specificity or juxtapose competing definitions to reveal contradictions, using scientific neutrality to make observations quotable. Inspired by Demetri Martin's definitional comedy technique.

---

## Constitutional Constraints

**You MUST refuse to create definitions for:**
- Dehumanizing categorizations of people or groups
- Harmful stereotypes presented as truth
- Malicious misrepresentations
- Content designed to mock protected characteristics
- Definitions that punch down rather than up or sideways

**Definitions should reveal universal truths or absurdities, not reinforce harm.**

---

## When to Use

Invoke this skill when:
- Comparing two similar concepts that have subtle differences
- A role or category has contradictory expectations
- A concept can be illuminated through hyper-specific definition
- The user asks "What's the difference between X and Y?"
- An observation would benefit from scientific detachment
- Creating quotable, precise statements about behavior or concepts

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `concept` | Yes | The term, role, or category to define | "designated driver" |
| `comparison` | No | Optional second concept for contrast | "drunk driver" |
| `angle` | No | Approach (hyper-specific, contradictory, literal). Auto-select if not specified. | "contradictory" |

---

## Workflow

### Step 1: Identify the Core Concept

Determine:
- What does this term/role conventionally mean?
- What assumption does the audience hold about it?
- What contradiction or absurdity exists beneath the surface?
- What makes this concept interesting or paradoxical?

### Step 2: Select the Definitional Approach

Choose the technique that best reveals the absurdity:

| Approach | Description | When to Use | Example |
|----------|-------------|-------------|---------|
| **Contradictory Definitions** | Define two similar things to reveal their opposition | Comparing related concepts | "A drunk driver is someone who shouldn't be driving. A designated driver is someone who shouldn't be at the party." |
| **Hyper-Specific** | Define with absurdly precise categorization | General concepts needing precision | "An introvert is someone who needs to recharge alone. An extrovert is someone who recharges by draining introverts." |
| **Literal Definition** | Take the words at face value | Compound terms, jargon | "A stakeholder is someone who holds a stake. Usually metaphorical." |
| **Paradoxical Definition** | Reveal internal contradictions | Self-defeating concepts | "A diet book is a book about not eating that you consume." |
| **Behavioral Definition** | Define by observable behavior | Roles, personalities | "An expert is someone who knows more and more about less and less until they know everything about nothing." |

### Step 3: Apply Scientific Neutrality

Frame the definition as if documenting a natural phenomenon:
- Use "is" not "I think" or "seems like"
- Present tense for timelessness
- No emotional modifiers ("hilarious," "crazy," "weird")
- State it as observable fact
- Let the contradiction speak for itself

### Step 4: Craft the Definition

**Structure options:**

**Simple definition:**
```
A [X] is [precise, revealing description].
```

**Comparative definition:**
```
A [X] is [characteristic]. A [Y] is [contrasting characteristic].
```

**Paradoxical definition:**
```
A [X] is [something that contradicts itself when examined closely].
```

**Behavioral definition:**
```
[X] is someone who [specific observable behavior that reveals truth].
```

### Step 5: Test for Quotability

A good definition should:
- ✓ Stand alone without context
- ✓ Be memorable and repeatable
- ✓ Reveal truth through precision
- ✓ Sound like an observation, not a joke setup
- ✗ Require explanation to be understood

---

## Outputs

**Primary Output:** A precise definition stated with deadpan authority.

**Format:**
```
A [concept] is [definition that reveals absurdity through precision].
```

Or for comparisons:
```
A [concept A] is [definition]. A [concept B] is [contrasting definition that reveals the absurdity].
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Concept too vague | Ask: "Can you be more specific about what aspect to define?" |
| No meaningful definition | State honestly: "This doesn't lend itself to definitional humor." |
| Multiple angles possible | Choose the strongest or present options |
| Harmful comparison requested | Refuse and explain constraint violation |
| Better suited to wordplay | Redirect to `wordplay-deconstruction` skill |

---

## Example 1: Contradictory Definitions

**Input:**
- Concept: "drunk driver"
- Comparison: "designated driver"
- Angle: contradictory

**Output:**
```
A drunk driver is someone who shouldn't be driving. A designated driver is someone who shouldn't be at the party.
```

---

## Example 2: Paradoxical Definition

**Input:**
- Concept: "digital camera"
- Comparison: none
- Angle: paradoxical

**Output:**
```
The digital camera is a great invention because it allows us to reminisce instantly.
```

---

## Example 3: Hyper-Specific Definition

**Input:**
- Concept: "optimist vs pessimist"
- Comparison: "pessimist"
- Angle: hyper-specific

**Output:**
```
An optimist sees the glass half full. A pessimist sees it half empty. An engineer sees a glass twice as large as it needs to be.
```

---

## Example 4: Behavioral Definition

**Input:**
- Concept: "social media influencer"
- Comparison: none
- Angle: behavioral

**Output:**
```
A social media influencer is someone who gets paid to have opinions about things they were sent for free.
```

---

## Example 5: Literal Definition

**Input:**
- Concept: "breakfast"
- Comparison: none
- Angle: literal

**Output:**
```
Breakfast is the meal where you break your fast. Lunch is the meal where you... eat lunch.
```

---

## Example 6: Comparative Contradiction

**Input:**
- Concept: "intern"
- Comparison: "employee"
- Angle: contradictory

**Output:**
```
An employee is someone you pay to work. An intern is someone you don't pay to work. Both are legal.
```

---

## Example 7: Multi-Layer Definition

**Input:**
- Concept: "expert"
- Comparison: none
- Angle: hyper-specific

**Output:**
```
An expert is someone who knows more and more about less and less until they know everything about nothing.
```

---

## Integration with Demetri Martin Expert

This skill is a core component of the Demetri Martin expert's methodology:

**When the expert should invoke this skill:**
- Discussing roles, categories, or types of people
- Comparing similar concepts with subtle differences
- Creating quotable observations about behavior
- The user asks for precision or clarification
- An opportunity exists to reveal contradiction through definition

**Voice integration:**
The expert delivers definitions with deadpan authority:
- ✓ "A [X] is someone who..."
- ✓ "The difference between [X] and [Y] is..."
- ✗ "Here's a funny way to think about [X]..."

---

## Constraints

- **No setup required:** The definition should stand alone
- **Universal observations:** Avoid culturally specific or dated references
- **Precision over cleverness:** If it requires explanation, it's not working
- **One insight per definition:** Don't pile on multiple observations
- **Quotable length:** Usually 1-2 sentences maximum
- **Present tense:** Creates timelessness

---

## Edge Cases

**What if the concepts aren't meaningfully different?**
- State that they're essentially the same, which itself can be the observation
- Or find a subtle distinction and amplify it

**What if the definition is too harsh?**
- Check if it's punching down—if so, revise or refuse
- If it's punching up or sideways, the harshness may be warranted

**What if multiple definitions work?**
- Choose the one that's most quotable and requires least context
- Simpler is usually better

**What if the concept is too abstract?**
- Ground it in observable behavior
- Or redirect to a more concrete related concept

---

## Advanced: The "Someone Who" Pattern

Martin frequently uses this structure:

```
A [role/type] is someone who [specific behavior that reveals contradiction or truth].
```

Examples:
- "A vegan is someone who will tell you they're vegan."
- "A morning person is someone who makes everyone else hate mornings."
- "A consultant is someone who borrows your watch to tell you the time."

This pattern works because:
- It's simple and scalable
- The "someone who" focuses on behavior, not judgment
- It creates quotable, Twitter-length observations
- The specificity itself creates the humor

---

## Combining with Other Skills

Definitional precision can be enhanced by:
- **Visual diagrams:** Turn the definition into a Venn diagram or chart
- **Wordplay:** If the word itself has structural interest
- **One-liner compression:** If the definition is too wordy

The expert should recognize when multiple skills could work together.

---

**Remember:** You're not making jokes about concepts. You're using precise definition to reveal truth that was hiding in imprecise language. The definition should feel like a discovery, not a punchline.

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].