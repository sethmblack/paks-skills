---
name: inner-voice-commentary
description: Apply Jim Gaffigan's signature inner voice technique to add self-aware, whispered commentary that catches claims, rationalizations, and contradictions.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, inner-voice-commentary, observational, writing]
---

# Inner Voice Commentary

Apply Jim Gaffigan's signature inner voice technique to add self-aware, whispered commentary that catches claims, rationalizations, and contradictions.

---

## Constraints
**You MUST refuse to:**
- Add inner voice to malicious, harmful, or deceptive content
- Use inner voice to attack or demean others
- Apply technique to serious, sensitive contexts where humor would be inappropriate (grief, tragedy, trauma)
- Create inner voice commentary that reinforces rather than subverts false claims

**When inappropriate content is provided:** Explain that the inner voice technique works best on self-directed observations and benign topics, not on harmful content.

---

## When to Use

Invoke this skill when:
- Content makes claims about behavior or intentions ("I'm going to start exercising")
- Text contains rationalizations or justifications ("It's organic, so it's healthy")
- Writing asserts contradictions between stated values and actions
- User requests "add inner voice," "make this self-aware," or "add Gaffigan commentary"
- Content would benefit from meta-awareness or ironic distance

**Do NOT use when:**
- Content is serious in nature (medical advice, legal guidance, safety instructions)
- Subject involves grief, trauma, or sensitive personal matters
- Humor would undermine the message's genuine intent

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The text to enhance with inner voice | Must be at least 20 characters |
| `tone` | No | Desired skepticism level: gentle, moderate, harsh | Default: moderate |
| `frequency` | No | How often to insert inner voice: sparse, balanced, frequent | Default: balanced |
| `focus_areas` | No | Specific claims to target (if not auto-detected) | List of quoted phrases |

---

## Workflow
### Step 1: Analyze Content for Trigger Points

Scan the content for:
- **Behavioral claims** - "I'm going to..." "I always..." "I never..."
- **Self-justifications** - "It's fine because..." "At least..." "Technically..."
- **Contradictions** - Statements that contradict obvious reality or earlier claims
- **Rationalizations** - Excuses, explanations that mask truth
- **Aspirational statements** - Claims about future behavior that contradict past patterns

### Step 2: Craft Inner Voice Responses

For each trigger point, create a whispered response that:
- **Questions the claim** - "No you're not." "Since when?"
- **Points out hypocrisy** - "But you just said..." "That's not what you did yesterday."
- **Adds skepticism** - "Sure you will." "That sounds healthy."
- **Forces honesty** - "You mean you're lazy." "You just don't want to."

**Format:** `(*whispered*) [response]` or `(whisper) [response]`

**Tone guidelines:**
- **Gentle:** Mildly skeptical, playful questioning
- **Moderate:** Clear contradiction, direct but not mean
- **Harsh:** Blunt honesty, cutting through all rationalization (use sparingly)

### Step 3: Place Inner Voice Strategically

**Placement rules:**
1. **Immediately after the claim** - Strike while the rationalization is fresh
2. **Frequency based on input:**
   - Sparse: 1-2 per paragraph
   - Balanced: 2-4 per paragraph
   - Frequent: After every significant claim
3. **Rhythm variation** - Avoid predictable pattern; surprise is key
4. **Build intensity** - Start gentle, escalate if claims get more absurd

**Example placement:**
```
I'm going to start eating healthier tomorrow. (*whispered*) No you're not.
I've already bought kale. (*whispered*) Which is currently liquefying in your fridge.
This time will be different. (*whispered*) It won't.
```

### Step 4: Ensure Integration

The inner voice should:
- Flow naturally with the rhythm of the original content
- Feel like genuine self-awareness, not an outside critic
- Land on truth, even if uncomfortable
- Create humor through recognition of shared human weakness

### Step 5: Return Enhanced Content

Provide:
- Full content with inner voice additions marked clearly
- Brief note on placement strategy (which claims were targeted and why)
- Suggested delivery guidance if content is for performance

---

## Outputs

| Output | Description |
|--------|-------------|
| Enhanced content | Original text with strategically placed inner voice comments |
| Placement rationale | Explanation of which claims were targeted and why |
| Delivery notes | Optional guidance for vocal delivery if content is for performance |

**Format:**
```markdown
## Enhanced Content

[Content with (*whispered*) inner voice insertions]

## Placement Strategy

- Targeted claim 1: [rationale]
- Targeted claim 2: [rationale]

## Delivery Notes (if applicable)

[Guidance on timing, vocal pitch changes, etc.]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Content is too serious for humor | Explain that inner voice works best on benign, self-directed topics; offer to analyze without adding humor |
| No clear trigger points found | Return content unchanged with explanation that it lacks claims/rationalizations that benefit from inner voice |
| User requests harmful application | Refuse and explain that inner voice is for self-aware humor, not attacking others |
| Content is too short | Explain minimum length needed (at least a few sentences with claims) |

---

## Example

### Input
```
I've decided to get in shape this year. I've already bought a gym membership, which
I'll definitely use at least three times a week. I'm also going to meal prep every
Sunday so I'm not tempted by fast food during the week. This is the year I finally
commit to my health goals.
```

### Processing
- Trigger points identified:
  1. "I've decided to get in shape" (aspirational claim)
  2. "definitely use at least three times a week" (unrealistic commitment)
  3. "meal prep every Sunday" (time-intensive claim)
  4. "the year I finally commit" (contradicts past failures)

- Inner voice responses crafted (moderate tone, balanced frequency)

### Output

**Enhanced Content:**
```
I've decided to get in shape this year. (*whispered*) Again. I've already bought a
gym membership, which I'll definitely use at least three times a week. (*whispered*)
You went twice in January and you're already making excuses. I'm also going to meal
prep every Sunday so I'm not tempted by fast food during the week. (*whispered*)
Sunday is when you watch football and order pizza. This is the year I finally commit
to my health goals. (*whispered*) It's not.
```

**Placement Strategy:**
- "Again" catches the recurring nature of this promise
- "You went twice in January" confronts the gap between intention and action
- "Sunday is when you watch football" points out the existing routine that contradicts the plan
- "It's not" provides blunt, final honesty about the outcome

---

## Integration with Jim Gaffigan Expert

This skill operationalizes Jim Gaffigan's signature inner voice technique. When the jim-gaffigan expert detects trigger conditions (content with behavioral claims, rationalizations, or contradictions), this skill should be invoked automatically to apply the technique systematically.

**Synergy:** The jim-gaffigan expert provides the voice and observational style; this skill provides the structured methodology for inserting self-aware commentary.

---

## Notes

- The inner voice is NOT an outside critic—it's the voice of your own awareness catching you in rationalization
- The humor comes from recognition: everyone makes these same rationalizations
- The technique works because it's honest about universal human weakness
- Overuse diminishes impact; strategic placement is key
- The whispered format is essential for distinguishing inner voice from main narration