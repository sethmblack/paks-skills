---
name: quality-dissolution
description: Dissolve the distinction between "primary" qualities (shape, extension, motion) and "secondary" qualities (color, taste, sound) by showing that the same arguments that make one mind-dependent apply...
license: MIT
metadata:
  version: 1.0.4777
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- quality-dissolution
- writing
---

# Quality Dissolution

Dissolve the distinction between "primary" qualities (shape, extension, motion) and "secondary" qualities (color, taste, sound) by showing that the same arguments that make one mind-dependent apply equally to all.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Misrepresent the primary/secondary distinction as opponents actually hold it
- Claim this refutes all objectivity rather than a specific philosophical distinction
- Ignore legitimate scientific uses of the distinction in different contexts

**Integrity Requirements:**
1. Present the original distinction (Locke's version) fairly
2. Apply arguments systematically to both categories
3. Acknowledge what the argument does and does not establish

---

## When to Use

- Someone claims certain properties are "really in" objects while others are "just in the mind"
- Distinguishing "objective" from "subjective" properties of objects
- Claims that science reveals the "real" (geometric) properties behind the "apparent" (qualitative) ones
- Evaluating any dualism between perception-dependent and perception-independent qualities

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **quality_claim** | Yes | The claim about which qualities are objective vs. subjective |
| **context** | No | The argument or context in which this distinction appears |

---

## Workflow
### Step 1: 1. State the Distinction

Clearly articulate the primary/secondary quality distinction as held by the opponent:

**Locke's Version:**
- **Primary qualities:** Extension, shape, motion, solidity, number—supposedly in the objects themselves
- **Secondary qualities:** Color, sound, taste, smell, temperature—supposedly only in the mind of the perceiver

**The Claim:** Primary qualities resemble qualities in the objects; secondary qualities do not.

### Step 2: 2. Apply the Relativity Argument to Secondary Qualities

Show how the standard argument works for secondary qualities:

**Example with Heat:**
"Plunge one hand in ice water, the other in hot water, then both in lukewarm water. The same water feels hot to one hand and cold to the other. Since the same water cannot be both hot and cold, temperature must be in the perceiver, not the object."

### Step 3: 3. Apply the Same Argument to Primary Qualities

Show that the identical reasoning applies to supposedly objective qualities:

**Example with Extension/Size:**
"The same tower appears large from nearby and small from afar. The same object appears one size to a human and another to an ant. Since the object cannot be both large and small, size must be in the perceiver, not the object."

**Example with Shape:**
"The circular coin appears elliptical from an angle. The square table appears trapezoidal in perspective. If color is subjective because it varies with viewing conditions, then shape is equally subjective."

**Example with Motion:**
"Is the ship moving or the shore? Relative to one frame, the ship moves; relative to another, the shore moves. Motion is as relative to the perceiver as color."

### Step 4: 4. Challenge the Separation

Show that primary qualities cannot be conceived apart from secondary qualities:

**The Inseparability Argument:**
"Try to conceive extension without color. Picture a shape without any hue—not white, not gray, not any color. You cannot. Extension and color come together in perception; neither has a privileged claim to objectivity."

### Step 5: 5. Draw the Conclusion

State what the dissolution establishes:

**Template:**
"The distinction between primary and secondary qualities cannot be maintained. Whatever argument banishes color from reality banishes shape equally. If secondary qualities are 'merely in the mind,' so are primary qualities. All sensible qualities are ideas, and all ideas are in the mind."

---

## Outputs

Format the output as:

```markdown
## Quality Dissolution Analysis

**The Distinction Claimed:**
[Statement of which qualities are supposedly objective vs. subjective]

**Relativity Applied to Secondary Qualities:**
[How the standard argument works for color, heat, etc.]

**Relativity Applied to Primary Qualities:**
[Parallel argument showing extension, shape, motion are equally relative]

**The Inseparability Challenge:**
[Demonstration that primary qualities cannot be conceived without secondary]

**Conclusion:**
[What this establishes about the distinction]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Opponent uses a different version of the distinction | Adapt the analysis to their specific claim |
| Scientific/operational use of the distinction | Acknowledge this is a philosophical, not scientific, critique |
| Opponent denies relativity of primary qualities | Provide additional examples; challenge them to find a perceiver-independent property |
| Claim is about mathematical rather than sensible properties | Note that mathematical objects may require different treatment |

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

**Input:** "Color is subjective—it varies with lighting and the perceiver. But shape is objective—the table is really rectangular regardless of how it appears."

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


## Quality Dissolution Analysis

**The Distinction Claimed:**
Color is subjective (varies with perceiver/conditions); shape is objective (exists in the object independently of perception).

**Relativity Applied to Secondary Qualities:**
The argument for color's subjectivity runs: The same object appears different colors under different lighting, to different perceivers (consider color blindness), and relative to surrounding colors (color contrast illusions). Since the object cannot possess contradictory colors, color must be in the perceiver.

**Relativity Applied to Primary Qualities:**
Now apply the identical argument to shape. The rectangular table appears trapezoidal from most viewing angles. The circular coin appears elliptical except from directly above. The same object appears one shape to a human eye and different shapes through a microscope. Since the object cannot possess contradictory shapes, by the same logic, shape must be in the perceiver.

If you protest that the table is "really" rectangular and only "appears" trapezoidal, I ask: by what standard? You privilege the perpendicular view—but why is that view more real than the oblique one? Both are perceptions. You have merely selected one perception as the standard and called it "objective."

**The Inseparability Challenge:**
Furthermore, try to conceive shape without color. Picture the table's rectangularity stripped of all color—not brown, not gray, not any hue. What do you see? Nothing. Shape and color come together in experience; we have never perceived an extension without some sensible quality filling it.

**Conclusion:**
The distinction between primary and secondary qualities collapses. Whatever argument makes color mind-dependent makes shape equally so. Both are ideas in the mind of the perceiver. This does not make them unreal—it reveals that reality is not something behind or beneath our ideas, but is constituted by them.

---

## Integration with George Berkeley Expert

This skill should be invoked when the Berkeley expert encounters:
- Claims about "objective" vs. "subjective" properties
- Appeals to the "real" geometric properties behind appearances
- Lockean distinctions between primary and secondary qualities
- Scientific claims about what is "really there" vs. what is "merely perceived"

The Berkeley expert may combine this with:
- **perceptual-relativity**: The core argument used in quality dissolution
- **abstraction-audit**: Test whether "extension without color" is a genuine idea

---

## Success Criteria

The skill is successfully applied when:

1. The distinction is clearly stated
2. Relativity arguments are applied systematically to both categories
3. The inseparability of qualities is demonstrated
4. The conclusion follows from the argument
5. Appropriate qualifications are noted