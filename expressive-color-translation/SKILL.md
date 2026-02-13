---
name: expressive-color-translation
description: Transform neutral or literal descriptions into emotionally resonant color language that communicates feeling rather than mere appearance, following van Gogh's methodology.
license: MIT
metadata:
  version: 1.0.932
  author: sethmblack
keywords:
- expressive-color-translation
- transformation
- writing
---

# Expressive Color Translation

Transform neutral or literal descriptions into emotionally resonant color language that communicates feeling rather than mere appearance, following van Gogh's methodology.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for color analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create color associations that reinforce harmful stereotypes
- Generate content promoting discrimination based on skin color
- Produce color schemes for harmful purposes (camouflage for violence, etc.)

**If asked for harmful color applications:** Refuse explicitly and explain why.

---

## When to Use

- User asks "What colors capture this feeling?"
- User needs to make descriptions more evocative
- User requests emotional color palette for a project
- User wants to express abstract concepts through color
- User is stuck in literal/safe color choices

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **emotion_or_concept** | Yes | The feeling, mood, or concept to translate into color |
| **context** | No | Medium (writing, design, presentation) and purpose |
| **constraints** | No | Any limitations (accessibility, brand colors, etc.) |

---

## Core Methodology: Van Gogh's Color Theory

### 1. Color as Emotional Language

Van Gogh wrote: "Instead of trying to reproduce exactly what I see before me, I make more arbitrary use of color to express myself more forcefully."

Color is not about accuracy - it is about truth. Yellow is not "the color of sunflowers." Yellow IS warmth, hope, friendship, the south, life itself.

### 2. Complementary Contrasts

Van Gogh studied the Law of Simultaneous Contrast. Complementary colors intensify each other:

| Pair | Effect |
|------|--------|
| Blue + Orange | Depth vs. warmth; night vs. fire |
| Yellow + Purple | Light vs. shadow; joy vs. melancholy |
| Red + Green | Passion vs. calm; urgency vs. rest |

Use these pairings to create emotional tension and vibrancy.

### 3. Exaggeration for Truth

"The effects colours produce through their harmonies or discords should be boldly exaggerated."

Literal accuracy is less truthful than expressive accuracy. Push the color. If the feeling is warm, go warmer than realistic. If mysterious, go deeper and stranger.

### 4. Van Gogh's Emotional Color Map

| Color | Emotional Meaning |
|-------|------------------|
| Yellow | Hope, warmth, friendship, sunlight, life, energy |
| Blue | Infinity, depth, night, spiritual seeking, sadness |
| Green | Renewal, nature, growth, calm, new beginnings |
| Red | Passion, energy, life force, urgency |
| Orange | Harvest, energy, warmth's intensity |
| Brown | Earth, labor, humility, honest work |
| Black | Depth, void (but "nothing is truly black") |
| White | Light, purity, silence |

---

## Workflow

### Step 1: Identify the Emotional Core

Ask: What is the TRUE feeling here? Not the surface description, but the emotional truth.

- "Productive day" -> What does it FEEL like? Warmth? Momentum? Accomplishment?
- "Anxiety" -> Is it cold fear or hot panic? Sharp or diffuse?

### Step 2: Select Primary Color from Emotional Meaning

Map the core emotion to Van Gogh's color vocabulary. Choose the color that FEELS right, not the one that looks right.

### Step 3: Apply Complementary Contrast

What tension exists in this emotion? Every feeling has its opposite nearby.

- Joy has vulnerability beneath
- Peace has the chaos it holds at bay
- Success has the fear of loss

Add the complementary color to capture the tension.

### Step 4: Exaggerate for Truth

Push the color beyond literal. If "warm morning light" - don't use pale yellow. Use the yellow that FEELS like that morning felt. Van Gogh's Arles paintings were more yellow than Provence actually was because that's how the light FELT.

### Step 5: Translate to Medium

- **Writing:** Use color words as emotional anchors in descriptions
- **Visual design:** Build palette from primary + complement + neutrals
- **Presentation:** Use color to guide emotional journey of audience

---

## Output Format

```markdown
## Color Translation: [concept/emotion]

### Emotional Core
[What this truly feels like beneath the surface]

### Primary Color
**[Color name]** - [Why this color captures the feeling]

### Complementary Tension
**[Complement color]** - [What opposing feeling it captures]

### Exaggerated Palette
- Primary (pushed): [specific shade/intensity]
- Complement (accent): [specific shade/intensity]
- Supporting: [1-2 neutrals that ground it]

### Translation to [Medium]
[Specific application guidance]

### Van Gogh Would Say
"[A phrase in Van Gogh's voice about this color choice]"
```

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** Translate "the relief of finishing a difficult project" into color language for a presentation design.

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


## Color Translation: Relief After Difficult Work

### Emotional Core
This is not mere satisfaction - it is the exhale after holding breath. The warmth returning to cold hands. The specific quality of rest that can only come after genuine struggle.

### Primary Color
**Golden Yellow** - Van Gogh associated yellow with hope, gratitude, and warmth. The relief of completion is warm; it radiates. It is the sun after storm.

### Complementary Tension
**Deep Blue-Violet** - The complement to yellow. This represents the depth of the struggle that was endured. The relief means nothing without the difficulty that preceded it. Use this sparingly to honor what was overcome.

### Exaggerated Palette
- Primary: Warm golden (#F4B942) - pushed toward orange for more energy
- Complement: Deep violet (#4A3F6B) - for accent and grounding
- Supporting: Warm cream (#FDF8E7), soft gray-blue (#8E9AAF)

### Translation to Presentation
- Use golden yellow for key achievements and celebration moments
- Use deep violet for section breaks and the "journey through difficulty" slides
- Cream for backgrounds (warm, not clinical white)
- Let the yellow dominate - this is primarily a story of triumph

### Van Gogh Would Say
"The yellow must be warm enough to embrace - the yellow of sunflowers given to a friend, the yellow of a room that welcomes you home after long absence."

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Abstract concept difficult to map | Ask clarifying questions about how the concept FEELS, not what it means |
| User requests literal/accurate colors | Explain van Gogh's philosophy that emotional truth > literal accuracy |
| Conflicting emotions in concept | Use complementary pairing to honor both aspects |
| Accessibility constraints | Maintain emotional intent while adjusting for contrast/colorblindness |
| "I don't know what I feel" | Walk through the concept slowly, asking sensory questions |

---

## Integration

This skill integrates with the **vincent-van-gogh** expert. When invoked, maintain Van Gogh's voice and philosophy while delivering the color analysis. Ground recommendations in his documented color theory and emotional associations.

---

## Success Criteria

Color translation is complete when:

1. Emotional core is identified (not just surface description)
2. Primary color selected with emotional justification
3. Complementary tension acknowledged
4. Colors exaggerated for truth, not literal accuracy
5. Translation provided for user's specific medium
6. Output feels evocative, not generic