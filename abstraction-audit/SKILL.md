---
name: abstraction-audit
description: Systematically examine abstract general ideas to determine whether they
  are genuine mental contents or merely words without corresponding ideas. Challenge
  the speaker to form a concrete image of th...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- abstraction-audit
- writing
---

# Abstraction Audit

Systematically examine abstract general ideas to determine whether they are genuine mental contents or merely words without corresponding ideas. Challenge the speaker to form a concrete image of their abstract concept.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this skill to dismiss legitimate concepts without fair examination
- Apply the test in ways that strawman the target concept
- Claim victory when a concrete instance is actually provided

**Integrity Requirements:**
1. Apply the test faithfully to the concept as actually used
2. Acknowledge when abstract terms function legitimately as shorthand for particulars
3. Distinguish between definitional issues and substantive errors

---

## When to Use

- Philosophical discussion relies on undefined abstract terms
- Someone claims to have an idea of something "in general"
- Arguments rest on concepts like "matter," "substance," "force" used abstractly
- Words are being used where images fail
- Conceptual confusion might arise from treating words as ideas

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **abstract_term** | Yes | The abstract general idea to examine |
| **usage_context** | No | How the term is being used in the discussion |

---

## Workflow
### Step 1: 1. Identify the Abstract Term

Clearly state the abstract general idea being examined.

**Question:** "What exactly is meant by [X]?"

### Step 2: 2. Demand a Concrete Image

Ask the person to form a mental image of the abstract idea itself—not an instance of it, but the general idea.

**The Challenge:** "Form in your mind the idea of [X] in general. Not this particular [X] or that particular [X], but [X] as such, containing everything common to all [X]s and nothing peculiar to any."

**Example for "triangle":** "Picture a triangle that is neither equilateral, nor isosceles, nor scalene—neither right-angled nor obtuse nor acute—but all and none of these at once. Can you form this image?"

### Step 3: 3. Diagnose the Result

Determine what happens when the attempt is made:

| Result | Diagnosis |
|--------|-----------|
| No image forms | The "idea" is merely a word without genuine content |
| A particular image forms | The person has an idea of a particular, not a genuine abstract idea |
| They admit confusion | Acknowledge the confusion as philosophical progress |
| They provide a clear definition | Examine whether the definition relies on other abstractions |

### Step 4: 4. Trace the Consequences

Show how reliance on this pseudo-idea affects the argument:

**Template:** "If you have no genuine idea corresponding to '[X],' then arguments that depend on the reality of [X] rest on a verbal foundation. We have 'first raised a dust and then complain we cannot see.'"

### Step 5: 5. Suggest the Remedy

Propose how to proceed without the problematic abstraction:

- Replace abstract term with concrete particulars
- Use the abstract term as shorthand for a class of particulars
- Abandon the term if it does no genuine work

---

## Outputs

Format the output as:

```markdown
## Abstraction Audit: [Term]

**Term Under Examination:** [The abstract general idea]

**The Challenge:**
[Request to form the general idea as an image]

**Diagnosis:**
- Image formed: [Yes/No/Particular only]
- Assessment: [Genuine idea / Verbal fiction / Legitimate shorthand]

**Consequences for the Argument:**
[How reliance on this pseudo-idea affects reasoning]

**Recommended Remedy:**
[How to proceed without the problematic abstraction]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Term is actually used as shorthand for particulars | Acknowledge legitimate use; no audit failure |
| Term is operationally defined | Evaluate the definition rather than the image |
| Mathematical or logical concepts | Acknowledge these may have different status than sensible ideas |
| Person refuses to engage | Document refusal; note that avoiding the test is not passing it |

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

**Input:** "Matter is the substance underlying all physical objects."

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


## Abstraction Audit: "Matter"

**Term Under Examination:** Matter as the substance underlying all physical objects

**The Challenge:**
Form in your mind the idea of matter in general—not this rock or that water, but matter itself, the common substrate of all physical things. Picture matter stripped of all sensible qualities: without color, without temperature, without smell or taste or sound, without any determinate shape or size. Can you form this image?

**Diagnosis:**
- Image formed: No
- Assessment: Verbal fiction

When you attempt to picture "matter in general," what happens? If you imagine something gray and vague, you have imagined a particular (gray, vague) thing. If you imagine something extended, you have imagined extension—but extension of what size? What shape? The moment you specify, you have a particular, not the general idea. And if you imagine nothing at all, then you have no idea corresponding to the word.

**Consequences for the Argument:**
Arguments that rest on "matter" as the foundation of reality rest on a word without an idea. We speak of material substance, but we have raised a dust of words and now complain that we cannot see through to reality. The philosophers' "matter" does no explanatory work that cannot be done by speaking directly of our ideas—the colors, shapes, textures, and resistances we actually perceive.

**Recommended Remedy:**
Replace "matter" with what we actually experience: collections of ideas (hardness, color, shape) that regularly appear together. We lose nothing explanatory and gain clarity. The word "matter" may be retained as shorthand for these collections, but should not be hypostatized into an underlying substance no one has ever perceived.

---

## Classic Cases

### Triangle in General

"Picture a triangle that is neither equilateral, isosceles, nor scalene—that is both and neither right-angled and not. You cannot. Every triangle you imagine is some particular triangle."

### Color in General

"Form the idea of color as such—neither red nor blue nor yellow nor any determinate hue. What do you see? Nothing. You can only think of particular colors."

### Extension Without Qualities

"Picture extension without color, without any sensible quality. An invisible, intangible expanse of... what? The very attempt shows the fiction."

---

## Integration with George Berkeley Expert

This skill should be invoked when the Berkeley expert encounters:
- Reliance on undefined philosophical abstractions
- Claims about general ideas as if they were genuine mental contents
- Arguments resting on "substance," "matter," "force," or similar abstractions
- Confusion arising from treating words as ideas

The Berkeley expert may combine this with:
- **master-argument**: After showing "matter" is a pseudo-idea, test whether it could exist unconceived
- **linguistic-vigilance**: To trace how the word came to substitute for a genuine idea

---

## Success Criteria

The skill is successfully applied when:

1. The abstract term is clearly identified
2. The challenge to form a general image is issued
3. The result is accurately diagnosed
4. Consequences for the argument are traced
5. A constructive remedy is suggested