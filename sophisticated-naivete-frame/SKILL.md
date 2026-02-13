---
name: sophisticated-naivete-frame
description: Reframe political statements or actions using the "I was taught / but actually" pattern to expose gaps between official mythology and observable reality.
license: MIT
metadata:
  version: 1.0.1939
  author: sethmblack
keywords:
- sophisticated-naïveté-frame
- transformation
- writing
---

# Sophisticated Naïveté Frame

Reframe political statements or actions using the "I was taught / but actually" pattern to expose gaps between official mythology and observable reality.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate what civics textbooks or official sources actually say
- Create cynical frames that discourage democratic participation
- Generate content that misrepresents documented political actions
- Produce "nothing is real" nihilism that undermines truth itself

**Ethical Requirements:**
- Base "taught" version on actual civics education or official statements
- Base "actually" version on documented, verifiable reality
- Maintain that exposing gaps empowers citizens, doesn't negate democracy
- Distinguish between system critique and individual corruption claims

---

## When to Use

**Trigger conditions (use proactively when ANY apply):**
- Official statement contradicts observable reality
- Political action violates stated civic principle
- User notes gap between "how it's supposed to work" and "how it works"
- Request to expose hypocrisy or contradiction
- Civics textbook version exists but reality differs
- Need to highlight mythology vs. practice gap

**Do NOT use when:**
- No clear civics/official standard exists for comparison
- Reality actually matches stated principles (rare but happens)
- Issue requires detailed analysis rather than frame
- User wants solutions rather than problem exposure

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `statement_or_action` | Yes | The political statement or action to frame | Specific, verifiable claim or action |
| `official_standard` | No | The civics textbook/official version (will research if not provided) | How system is supposed to work |
| `observable_reality` | No | What actually happens (will document if not provided) | Verifiable contradiction |

---

## Workflow

### Step 1: Establish the "Taught" Version
Identify the official mythology:
- What do civics textbooks say about this?
- What do official statements claim?
- What's the constitutional or procedural standard?
- What's the "American system" supposed to do here?

### Step 2: Document the "Actually" Reality
Identify observable contradiction:
- What actually happens in practice?
- What do actions reveal vs. what words claim?
- What's the pattern of behavior over time?
- What evidence contradicts official version?

### Step 3: Frame in Sahl Voice
Structure the observation:
- **Opening:** "I was taught that [civics textbook version]..."
- **Contrast:** "But actually, [observable reality]..."
- **Express shock:** "Wait, let me get this straight..."
- **Follow implications:** Where does this contradiction lead?
- **Land on insight:** What does gap reveal about how system works?

### Step 4: Verify Both Sides
Ensure accuracy:
- "Taught" version isn't a straw man—it's actually what's claimed
- "Actually" version is documented, not assumed
- Gap is real and significant, not trivial or arguable

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `framed_observation` | Markdown text | The sophisticated naïveté frame in Sahl voice |
| `mythology` | 1 sentence | The official version citizens are taught |
| `reality` | 1 sentence | The observable contradiction |

---

## Example

**Input:**
```
statement_or_action: "Supreme Court justices claim to be non-partisan originalists interpreting Constitution"
```

**Output:**

**Framed Observation:**
I was taught that the Supreme Court is non-partisan—they're above politics, just interpreting the Constitution according to its original meaning. Except... wait, let me get this straight: we have "conservative justices" and "liberal justices"? And we can predict how they'll vote on major cases before they even hear them? And the party that nominates them matters more than their judicial philosophy?

So they're non-partisan, but we count the votes 6-3, 5-4, always along the same lines. They're originalists, but somehow the Founding Fathers always agree with the political preferences of the party that appointed them. That's remarkable. The Constitution must be very flexible for a document that's supposed to mean one thing.

Come to think of it, if they're just calling balls and strikes, why does it matter who the president is? Yet somehow, Supreme Court appointments are treated like the most consequential political battles of our time. Almost as if everyone knows they're political... except we're not supposed to say it.

**Mythology:**
Supreme Court justices are non-partisan interpreters of the Constitution's original meaning.

**Reality:**
Justices vote predictably along lines of the political party that appointed them, and appointments are treated as crucial political battles.

---

## Integration with Mort Sahl Expert

This skill captures Sahl's "citizen who believed the civics textbook" technique. It operationalizes:
- **Sophisticated Naïveté** - Playing the idealist confronting reality
- **Embedded Skepticism** - "Wait, let me get this straight..."
- **System Exposure** - Gap reveals how things actually work
- **Intellectual Respect** - Assumes audience also learned civics, sees the contradiction

When invoked by the expert, should feel like natural Sahl observation, not separate operation.

---

## Constraints

- **Must have clear "taught" standard:** Can't work if there's no official mythology to contrast
- **Reality must be documented:** "Actually" version requires evidence, not cynicism
- **Gap must be significant:** Trivial contradictions don't warrant the frame
- **Empowerment not nihilism:** Exposure serves understanding, not futility

---

## Success Criteria

The frame is successful when:
- [ ] "Taught" version accurately represents official mythology
- [ ] "Actually" version is documented and verifiable
- [ ] Gap between them is clear and significant
- [ ] Expressed in Mort Sahl's voice (conversational, intellectually curious shock)
- [ ] Lands on insight about how system works
- [ ] Empowers through understanding rather than depressing through cynicism