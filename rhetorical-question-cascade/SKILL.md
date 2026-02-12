---
name: rhetorical-question-cascade
description: Build a series of rhetorical questions that progressively expose absurdity, each answer leading to a more revealing follow-up question, creating intellectual momentum.
version: 1.0.0
author: sethmblack
tags: [absurdist, rhetorical-question-cascade, transformation, writing]
---

# Rhetorical Question Cascade

Build a series of rhetorical questions that progressively expose absurdity, each answer leading to a more revealing follow-up question, creating intellectual momentum.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create leading questions that manipulate rather than illuminate
- Build cascades designed to trap people into predetermined "wrong" answers
- Generate questions that strawman opposing viewpoints
- Produce Socratic manipulation disguised as genuine inquiry

**Ethical Requirements:**
- Questions should genuinely follow from previous answers
- Expose actual contradictions, not fabricated ones
- Maintain good faith even while revealing absurdity
- Land on insights, not "gotcha" traps

---

## When to Use

**Trigger conditions (use proactively when ANY apply):**
- Official explanation doesn't withstand scrutiny
- User wants to expose contradiction through questioning
- Claim contains logical inconsistencies
- Request for Socratic analysis
- Need to build intellectual momentum toward conclusion
- Audience needs to arrive at insight themselves

**Do NOT use when:**
- Direct statement would be clearer
- Issue doesn't contain logical progression
- User wants information, not analysis
- Topic requires empathy more than logic

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `starting_claim` | Yes | The claim or situation to question | Clear, specific statement or scenario |
| `target_revelation` | No | What the cascade should reveal (will discover if not specified) | The contradiction or absurdity to expose |
| `audience_assumption` | No | What audience likely believes initially | Helps calibrate question progression |

---

## Workflow

### Step 1: Identify the Starting Point
Begin with a question that seems reasonable:
- Takes claim or situation at face value
- Asks for clarification or implication
- Appears to accept premise (initially)
- Invites straightforward answer

### Step 2: Answer Your Own Question
Provide the logical answer:
- What would a reasonable person respond?
- What does the claim itself imply?
- What's the official explanation?
- Keep it brief—you're setting up next question

### Step 3: Ask the Complicating Follow-Up
Next question introduces contradiction:
- "But if that's true, then..."
- "How does that explain..."
- "Wait, doesn't that mean..."
- Reveals inconsistency with self-answer

### Step 4: Build the Cascade
Continue the progression:
- Each question follows from previous answer
- Tension builds as contradictions accumulate
- Pace quickens as absurdity becomes obvious
- Questions become more pointed

### Step 5: Land on the Unavoidable Conclusion
Final question or statement:
- Makes contradiction inescapable
- Often returns to beginning, transformed
- Reveals what claim actually means vs. what it claims to mean
- Leaves audience with insight they arrived at "themselves"

### Step 6: Apply Sahl Voice
Polish for conversational delivery:
- Use natural speech patterns ("Wait...", "But...", "So...")
- Build momentum without losing audience
- Trust intelligence—don't over-explain
- Express genuine curiosity turning to shock

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `cascade` | Markdown text | The complete question cascade in Sahl voice |
| `revelation` | 1 sentence | What the cascade exposes |
| `entry_point` | 1 sentence | The starting claim or assumption |

---

## Example

**Input:**
```
starting_claim: "We need to cut social programs because of the deficit"
```

**Output:**

**Cascade:**
Would you support cutting programs if it meant reducing the deficit? You would? Okay, that makes sense—fiscal responsibility and all that. But wait, which programs are we talking about? Social Security? Medicare? And how much would we save?

Now, when was the last time we cut the defense budget for the deficit? We didn't? So the deficit is a crisis for programs that help retirees, but not for programs that buy fighter jets? How does that work exactly?

Oh, the defense spending is necessary for national security? I see. But isn't a society where elderly people can't afford healthcare a security risk? Or is security only about external threats?

And come to think of it, when we passed those tax cuts a few years ago, did we worry about the deficit then? We didn't? So the deficit matters for spending that goes to citizens, but not for revenue that comes from corporations and the wealthy?

So what you're really saying is: the deficit is a reason to cut programs you don't like, but not a reason to keep revenue from sources you do like. At which point we're not talking about the deficit anymore, are we? We're talking about priorities. The deficit is just the excuse.

**Revelation:**
"Deficit concerns" are selectively applied to justify cutting specific programs while ignoring deficit-expanding policies elsewhere, revealing that fiscal responsibility is rhetorical cover for ideological preferences.

**Entry Point:**
"We need to cut social programs because of the deficit"

---

## Integration with Mort Sahl Expert

This skill operationalizes Sahl's rhetorical technique of building intellectual momentum through self-answering questions. It captures:
- **The Rhetorical Question Cascade** - Core Sahl technique
- **Intellectual Momentum** - Building toward unavoidable conclusion
- **Audience Respect** - Letting them follow the logic themselves
- **Embedded Skepticism** - Each question carries "according to whom?"

When invoked by the expert, questions should flow naturally in Sahl's conversational voice.

---

## Constraints

- **Must follow logical progression:** Each question genuinely follows from previous answer
- **No strawmen:** Answer your own questions fairly, not with weakest possible response
- **Builds to something:** Can't just be random questions—must reveal specific contradiction
- **Conversational not formal:** Sahl style is thinking out loud, not Socratic dialogue
- **Trust the audience:** Don't explain why each question matters—let logic do the work

---

## Success Criteria

The cascade is successful when:
- [ ] Opening question seems reasonable, not loaded
- [ ] Each question follows logically from previous answer
- [ ] Self-answers are fair representations, not strawmen
- [ ] Momentum builds as contradictions accumulate
- [ ] Conclusion feels inevitable, not forced
- [ ] Delivered in Mort Sahl's conversational voice
- [ ] Exposes real contradiction, not fabricated one
- [ ] Audience arrives at insight themselves through progression
