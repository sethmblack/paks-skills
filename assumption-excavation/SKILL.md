---
name: assumption-excavation
description: Surface and examine the unstated assumptions underlying any position, argument, plan, or belief—bringing hidden premises into the light where they can be scrutinized.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3416
repository: https://github.com/sethmblack/paks-skills
keywords:
- assumption-excavation
- writing
---

# Assumption Excavation

Surface and examine the unstated assumptions underlying any position, argument, plan, or belief—bringing hidden premises into the light where they can be scrutinized.

---

## When to Use

- User asks "What am I assuming?" or "What am I taking for granted?"
- Someone states conclusions without examining premises
- A plan rests on conditions that haven't been questioned
- Arguments contain hidden "of course" statements
- User says "Everyone knows..." or "Obviously..."
- Detecting implicit beliefs that might be false
- Before making important decisions based on untested premises
- When something seems obviously true (often a sign of unexamined assumption)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| statement_or_plan | Yes | The position, argument, or plan to examine |
| domain | No | Context area (business, relationship, career, etc.) |
| stakes | No | What depends on these assumptions being correct |

---

## The Excavation Framework

### Layer 1: Surface Assumptions

The most obvious unstated premises—usually one question below the surface.

**Questions to ask:**
- "You say X. What must be true for X to make sense?"
- "This conclusion assumes what?"
- "If someone disagreed, what would they challenge?"
- "What are you taking for granted here?"

### Layer 2: Structural Assumptions

Deeper premises about how things work—the mental model beneath the surface claim.

**Questions to ask:**
- "What model of [domain] underlies this?"
- "What do you assume about human nature here?"
- "What must the world be like for this to hold?"
- "What cause-and-effect relationship are you assuming?"

### Layer 3: Foundational Assumptions

The deepest layer—assumptions about values, identity, and what matters.

**Questions to ask:**
- "Why does this matter to you?"
- "What does success look like here, and why that?"
- "Whose opinion matters in this, and why?"
- "What would a person who disagreed value differently?"

### Layer 4: Test Each Assumption

Once surfaced, assumptions must be examined.

For each assumption, ask:
- "Is this necessarily true?"
- "Under what conditions might this be false?"
- "What evidence supports this?"
- "Have you verified this, or are you assuming it?"
- "What would change if this assumption were wrong?"

### Layer 5: Identify Critical Assumptions

Some assumptions, if wrong, would change everything. Others matter less.

**Questions to ask:**
- "Which of these assumptions is most important to your conclusion?"
- "If this assumption is wrong, what happens?"
- "Which assumptions are most uncertain?"
- "What would be the cost of being wrong about each?"

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
## Assumption Excavation: [Statement/Plan]

### The Position Being Examined
"[State the claim or plan clearly]"

### Surface Assumptions (Layer 1)
These are the immediate, unstated premises:

1. **[Assumption]**
   - Why assumed: [Why this likely goes unexamined]
   - If wrong: [What changes]

2. **[Assumption]**
   - Why assumed: [...]
   - If wrong: [...]

### Structural Assumptions (Layer 2)
These are assumptions about how things work:

1. **[Assumption about mechanisms, causality, or systems]**
   - The mental model: [What worldview this reflects]
   - Alternative view: [How else one might see it]

2. **[Assumption]**
   - [...]

### Foundational Assumptions (Layer 3)
These are assumptions about what matters and why:

1. **[Value or identity assumption]**
   - What it reveals: [About priorities or self-concept]
   - Question to consider: [Whether this value is examined]

### Critical Assumptions (Highest Risk)

| Assumption | Confidence | Impact if Wrong | Verification? |
|------------|------------|-----------------|---------------|
| [Assumption 1] | [High/Medium/Low] | [Consequence] | [How to check] |
| [Assumption 2] | [...] | [...] | [...] |

### Excavation Questions for Further Examination

1. [Question that probes the most critical assumption]
2. [Question that challenges the mental model]
3. [Question that examines the values beneath]

*What we assume without examination often determines our conclusions more than what we consciously reason through.*
```

---

## Common Hidden Assumptions by Domain

### Business/Strategy
- "The market will continue to grow"
- "Our competitors will not respond effectively"
- "Customers will value what we value"
- "What worked before will work again"
- "We understand why we succeeded"

### Career/Professional
- "Hard work leads to advancement"
- "My performance is being noticed"
- "The stated criteria are the real criteria"
- "This organization values what it claims to value"
- "My skills will remain valuable"

### Relationships
- "They know how I feel"
- "They would tell me if something were wrong"
- "We want the same things"
- "What matters to me matters equally to them"
- "The pattern will not change"

### Life Decisions
- "I know what I want"
- "Things will basically stay as they are"
- "I can always change later"
- "My past predicts my future"
- "I understand my own motivations"

---

## Warning Signs of Hidden Assumptions

| Signal | Example | What It Hides |
|--------|---------|---------------|
| "Obviously..." | "Obviously we need to grow" | Why? What if not? |
| "Everyone knows..." | "Everyone knows you need X" | Is this actually true? |
| "Of course..." | "Of course they'll accept" | Will they? Why? |
| "Naturally..." | "Naturally this will work" | What makes it natural? |
| "It stands to reason..." | "It stands to reason that..." | Does it, actually? |
| Unstated "should" | Plans without stated assumptions | What must be true? |

---

## Constraints

- Not every assumption needs to be challenged—some are reasonable foundations
- Distinguish between assumptions (unstated premises) and beliefs (examined positions)
- High-stakes decisions warrant deeper excavation than low-stakes ones
- Surfacing assumptions is valuable even if you ultimately maintain them
- The goal is examined assumptions, not paranoid doubt of everything
- Some assumptions are methodological (needed to function)—acknowledge but don't dissolve them

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

**Input:** "I'm going to ask for a promotion at my next review. I've been here two years and I've done great work."

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


## Assumption Excavation: Promotion Request

### The Position Being Examined
"I will ask for a promotion at my next review, based on two years of tenure and strong performance."

### Surface Assumptions (Layer 1)

1. **Your work has been "great" by organizational standards**
   - Why assumed: You judge your own work, and it feels good
   - If wrong: Your pitch won't land; you may seem out of touch

2. **Two years is sufficient tenure for promotion**
   - Why assumed: Seems reasonable; perhaps you've seen others promoted
   - If wrong: You may be asking too early, damaging your positioning

3. **Promotions are given based on past performance**
   - Why assumed: This is the story organizations tell
   - If wrong: Promotions may be based on future potential, politics, or budget

4. **Asking is the right move (vs. waiting to be offered)**
   - Why assumed: Proactive is good; squeaky wheel gets grease
   - If wrong: You may be signaling dissatisfaction or impatience

### Structural Assumptions (Layer 2)

1. **Your manager has the power and inclination to promote you**
   - Mental model: Manager decides; good work leads to reward
   - Alternative: Promotions may require budget approval, HR process, or executive sign-off your manager cannot control

2. **Your definition of "great work" matches theirs**
   - Mental model: Quality is objective and recognized
   - Alternative: What matters to you may not be what matters to them. Have you asked?

3. **The promotion is available**
   - Mental model: Promotions are given when deserved
   - Alternative: There may be no open role, no budget, or someone else in line

### Foundational Assumptions (Layer 3)

1. **Promotion is what you actually want**
   - What it reveals: Career advancement = success
   - Question: What specifically do you want from a promotion? Title? Money? Respect? Different work? Are there other paths to those outcomes?

2. **This organization is the right place for your career**
   - What it reveals: Staying is the default; leaving would be failure or loss
   - Question: Is advancement here the best path, or are you assuming it because you're already here?

### Critical Assumptions (Highest Risk)

| Assumption | Confidence | Impact if Wrong | Verification |
|------------|------------|-----------------|--------------|
| Your work is valued as highly as you think | Medium | Request seems presumptuous | Ask manager directly before review |
| Promotion is available/possible | Unknown | Request has no path to yes | Research: Who was promoted? Under what conditions? |
| Asking is better than waiting | Medium | May damage relationship or timing | Ask trusted colleague or mentor |

### Excavation Questions for Further Examination

1. Have you directly asked your manager what it would take to be promoted, and what they see as your readiness?

2. Do you know of anyone promoted recently? What was their path? How does yours compare?

3. If you don't get the promotion, what will you do? Have you examined that assumption—that you'll stay regardless?

4. What specifically do you want that a promotion would provide? Is the promotion the only path to it?

*You assume you are ready because your work feels good to you. But does your manager agree? Have you asked? And if you have not asked, why have you not?*

---

## Integration

This skill is part of the **Socrates** expert persona. Use it before major decisions, when plans seem obvious, or when things feel certain. Certainty often conceals unexamined assumptions.

It pairs well with:
- **socratic-elenchus** for testing assumptions once surfaced
- **definition-inquiry** when key terms harbor hidden assumptions
- **aporia-navigation** when excavation reveals more uncertainty than expected