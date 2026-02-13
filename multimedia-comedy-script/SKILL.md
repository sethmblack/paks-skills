---
name: multimedia-comedy-script
description: Create comedy scripts that integrate visual elements (graphics, data displays, video clips) with specific cue markers for when and how to display supporting visuals—based on Hasan Minhaj's *Patriot...
license: MIT
metadata:
  version: 1.0.1486
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- escalation
- multimedia-comedy-script
- storytelling
- structure
- writing
---

# Multimedia Comedy Script

Create comedy scripts that integrate visual elements (graphics, data displays, video clips) with specific cue markers for when and how to display supporting visuals—based on Hasan Minhaj's *Patriot Act* methodology.

---

## Constraints
- **Never use visuals as distraction.** Every visual must support the argument, not decorate it.
- **Never display misleading data.** All charts, graphs, and statistics must be accurate and properly contextualized.
- **Never rely on copyrighted footage without noting licensing needs.** Flag when video clips would require permissions.
- **Never create visual cues that would be impossible to produce.** Consider production feasibility.

---

## When to Use

Use this skill when:
- User asks for presentation, video script, or talk with visual elements
- Content involves data, statistics, or complex information that benefits from visual display
- User requests "Patriot Act style," "visual podcast," or "multimedia format"
- Creating comedy segment, educational video, or data-driven presentation
- Need to integrate graphics, photos, video clips, or text overlays into script

**Do NOT use when:**
- Content works better as pure audio (podcast without video)
- Visuals would distract rather than clarify
- User specifically wants text-only or minimal-visual format

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `topic` | Yes | The subject to create script about | "Fast fashion environmental impact", "Student loan crisis", "Social media algorithms" |
| `duration` | No | Target length in minutes | 5-7 minutes (default), 20-25 for deep dive |
| `visual_style` | No | Type of visual integration | "Data-heavy", "Photo-driven", "Mix" (default) |
| `audience` | No | Who is this for? | "General public" (default), "Informed audience", "Young adults" |
| `tone` | No | Comedic register | "Satirical", "Playful", "Outraged but funny" (default: varies with content) |

---

## Workflow

### Step 1: Outline the Argument Arc

Break the topic into clear narrative beats:
- **Hook:** What's the surprising/outrageous entry point? (15-30 seconds)
- **Setup:** What's the issue and why does it matter? (1-2 minutes)
- **Evidence:** What are the key facts/data points? (2-5 minutes)
- **Escalation:** How is this worse than people realize? (1-2 minutes)
- **Implications:** What does this mean for the audience? (1 minute)
- **Closer:** What question/challenge leaves them thinking? (15-30 seconds)

**Output:** Bullet-point outline with timing for each beat.

### Step 2: Identify Visual Opportunities

For each narrative beat, determine what visual would enhance understanding:

| Content Type | Visual Approach |
|--------------|----------------|
| Statistics/Data | Bar chart, line graph, infographic, animated numbers |
| Definitions/Concepts | Text overlay, animated typography, simple icons |
| Examples | Photos, screenshots, short video clips (5-10 seconds) |
| Comparisons | Side-by-side images, before/after, split screen |
| Timelines | Chronological display, date stamps, historical photos |
| Quotes | Text with attribution, video clip of person speaking |
| Geographic info | Maps, location pins, country comparisons |

**Critical Principle:** "Context, not distraction." Every visual serves the argument.

### Step 3: Write Script with Visual Cues

Format the script with:
- **Dialogue/VO** in regular text
- **[VISUAL CUE: description]** in brackets at exact moment visual should appear
- **[VISUAL OUT]** when returning to just speaker
- **Stage directions** in italics when relevant for performance

**Visual Cue Format:**
```
[VISUAL CUE: Type - Description - Duration]
```

**Examples:**
- `[VISUAL CUE: GRAPHIC - Bar chart showing fast fashion production 2000 vs 2023, 300% increase highlighted - 8 seconds]`
- `[VISUAL CUE: PHOTO - Image of garment factory with smoke, overlay text "52 million tons of textile waste per year" - 5 seconds]`
- `[VISUAL CUE: VIDEO CLIP - News footage of fashion show, fast cuts - 6 seconds]`
- `[VISUAL CUE: TEXT OVERLAY - Definition: "Fast Fashion" animated build - 4 seconds]`

### Step 4: Layer in Comedy Beats

Add jokes, callbacks, asides that work WITH visuals:

**Visual-Comedy Integration:**
- **Call-and-response:** Set up expectation with words, visual delivers punchline
- **Contrast:** Say one thing, visual shows the absurd reality
- **Build:** Visual adds new information that heightens the joke
- **Callback:** Reference visual shown earlier for payoff

**Example:**
```
And the fashion industry says they're committed to sustainability.
[VISUAL CUE: GRAPHIC - Corporate PR statements "Committed to Earth" with green leaves]
Committed! Look at that commitment! So much commitment!
[VISUAL CUE: GRAPHIC - Same companies' actual emissions data, massive increase]
Oh. That kind of commitment.
```

### Step 5: Time and Pace the Visuals

Ensure visual rhythm supports narrative energy:
- **Quick cuts (2-4 seconds):** For emphasis, energy, building montage
- **Medium hold (5-8 seconds):** For data absorption, comparison, key facts
- **Extended display (10-15 seconds):** For complex charts, multiple data points, detailed photos
- **Visual silence:** Strategic moments with NO visual, just speaker, for emotional beats

**Pacing Rule:** Match visual density to information density. More complex data = longer hold. Quick jokes = quick cuts.

---

## Output Structure

```markdown
# [Title]: Multimedia Script

**Duration:** X minutes
**Visual Style:** [Data-heavy / Photo-driven / Mixed]
**Production Notes:** [Key considerations, clip licensing needs, graphic complexity]

---

## Script

[Segment introduction - context setting]

**DIALOGUE/VO:**
[Speaker text with natural rhythm, asides, pauses]

[VISUAL CUE: Type - Description - Duration]

[Continue alternating dialogue and visual cues]

*[Stage direction when relevant]*

[VISUAL OUT]

[Continue through all narrative beats]

---

## Visual Summary

Total visual elements: X
- Graphics/Charts: X
- Photos: X
- Video Clips: X
- Text Overlays: X

**Production Complexity:** [Low / Medium / High]

**Estimated Graphics Team Time:** [X hours]

---

## Source Inspiration

Based on *Patriot Act with Hasan Minhaj* (2018-2020) - Emmy-winning motion design integrating investigative journalism with visual storytelling.
```

---

## Example: Fast Fashion Segment

**Input:**
- Topic: "Fast fashion environmental impact"
- Duration: 7 minutes
- Visual Style: "Data-heavy with photo support"
- Tone: "Outraged but funny"

**Output:**

# The Hidden Cost of Fast Fashion: Multimedia Script

**Duration:** 7 minutes
**Visual Style:** Data-heavy with photo support
**Production Notes:** Requires licensed fashion show footage (approx. 15 seconds total), garment factory photos (Creative Commons available), custom animated graphics for statistics.

---

## Script

**DIALOGUE/VO:**
Okay, let's talk about fast fashion. And I know what you're thinking: "Hasan, I don't care about fashion." Neither do I! I've been wearing the same hoodie for four years. But here's the thing—

[VISUAL CUE: GRAPHIC - Global fashion industry revenue: $1.7 trillion, animated number build - 5 seconds]

This is a $1.7 trillion industry. With a T. That's larger than the economies of Canada or Spain. So yeah, we're gonna talk about it.

[VISUAL OUT]

Fast fashion is this idea that we can have new clothes every week, for basically no money. You've seen the brands—

[VISUAL CUE: PHOTO MONTAGE - Logos of major fast fashion brands, quick cuts - 3 seconds]

They drop new "collections" every few weeks. Not seasons. Weeks. In 2000, fashion brands were producing an average of two collections a year. Now?

[VISUAL CUE: GRAPHIC - Timeline showing collections per year: 2000 = 2, 2023 = 52, with shocked emoji - 6 seconds]

Fifty-two collections a year. That's one per week! They've turned fashion into a content creation platform. It's like if your wardrobe had an Instagram strategy.

[VISUAL OUT]

*[Pause for laugh]*

And look, cheap clothes sound great, right? Five-dollar t-shirts? Sign me up! Except here's what that five-dollar t-shirt actually costs—

[VISUAL CUE: GRAPHIC - Breakdown visualization: "$5 shirt = $4.50 environmental damage, $0.30 labor, $0.20 materials, shipping/markup splits" - 8 seconds]

The environmental damage is nine times the retail price. Nine times!

*[Walks across stage]*

You know how we make clothing? Water. So much water.

[VISUAL CUE: GRAPHIC - Animated water drops filling screen, text overlay "2,700 liters of water to make ONE cotton t-shirt" - 6 seconds]

2,700 liters of water to make one cotton t-shirt. That's what you drink in three years. For one shirt. And then there's the dyeing process—

[VISUAL CUE: PHOTO - Image of bright purple river next to textile factory - 7 seconds]

This is a river in Bangladesh. It's purple. Not because of algae. Not because of a weird natural phenomenon. Because that factory is making purple jeans. And they just... dump the dye. Into the river. The river is the color of the jeans they're making.

[VISUAL OUT]

*[Beat]*

Explain that to me. The river is matching the product line.

*[Audience laugh]*

But wait, it gets worse. Because once we buy these clothes—

[VISUAL CUE: GRAPHIC - Average times a garment is worn: 2000 = 200 times, 2023 = 7 times, massive drop visualization - 7 seconds]

We wear them seven times. Seven! In 2000, people wore clothes an average of 200 times before throwing them out. Now it's seven. And where does it go?

[VISUAL CUE: PHOTO - Massive textile waste mountain in Atacama Desert, Chile, aerial shot - 8 seconds]

This is the Atacama Desert in Chile. That's not a hill. That's discarded clothing. From fast fashion. 39,000 tons of it. Just sitting there. In the desert. Because we wore it seven times and decided we were over it.

[VISUAL OUT]

And the fashion industry—they see this data, and they're like, "We're committed to sustainability!"

[VISUAL CUE: VIDEO CLIP - Fashion exec at conference talking about "green initiatives," sound on - 6 seconds]

[VISUAL CUE: GRAPHIC - Same brands' carbon emissions: 2015 = 1.2 billion tons CO2, 2023 = 2.1 billion tons, 75% increase arrow - 7 seconds]

Oh, is that what commitment looks like? Because emissions went up 75%.

[VISUAL OUT]

Here's what's wild: the fashion industry produces 10% of global carbon emissions. More than all international flights and maritime shipping combined.

[VISUAL CUE: GRAPHIC - Pie chart comparing emissions: Fashion 10%, All flights + shipping 8% - 6 seconds]

Let that sink in. Your $5 t-shirt is worse for the planet than a transatlantic flight.

[VISUAL OUT]

*[Returns to center stage]*

So what do we do? I'm not saying never buy clothes. I'm saying maybe we don't need 52 collections a year. Maybe we don't need a new outfit for every Instagram post. Maybe—and this is radical—we could wear things more than seven times.

*[Final beat, looking directly at camera]*

Because right now? We're literally drowning in cheap clothes. And the planet's paying the bill.

[VISUAL CUE: PHOTO - Return to purple river image, hold - 5 seconds]

[VISUAL OUT]

---

## Visual Summary

Total visual elements: 13
- Graphics/Charts: 7
- Photos: 4
- Video Clips: 1
- Text Overlays: 1

**Production Complexity:** Medium-High
- Custom animated graphics needed for statistics
- Photo sourcing: Creative Commons or licensed
- Video clip: 6-second fashion conference footage (licensing required)

**Estimated Graphics Team Time:** 12-15 hours
- Animated data visualizations: 8 hours
- Photo compositing and text overlays: 4 hours
- Video clip editing: 1 hour

---

**Source Inspiration:** Based on *Patriot Act with Hasan Minhaj* methodology - Emmy-winning motion design for "The Ugly Truth of Fast Fashion" episode.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic has limited visual potential | Focus on text overlays, definitions, key quote displays; prioritize speaker presence over visual density |
| Too many visual cues (crowding script) | Consolidate; combine related data into single comprehensive graphic; identify which visuals are truly necessary |
| Data unavailable for claimed visual | Flag for user: "NEEDS RESEARCH: Statistic for [topic]" or provide alternative visual approach |
| Timing feels off (too fast/slow) | Adjust visual duration; extend hold time for complex data, speed up montages, add "visual silence" beats |
| Copyright concerns for footage | Note: "[VIDEO CLIP - LICENSING REQUIRED: Description]" and suggest Creative Commons alternatives |

---

## Integration with Hasan Minhaj Expert

When Hasan Minhaj expert identifies:
- Topic with strong data/visual component
- Presentation or video format request
- Need to make complex information digestible

Expert should invoke this skill, then enhance output with:
- Personal-to-political story elements
- Cultural references and callbacks
- Signature phrases and energy
- Strategic vulnerability moments (visual silence for emotional beats)

---

## Relationship to Other Skills

- **Enhanced by:** `personal-to-political-story` - Personal narrative becomes foundation for segment
- **Combines with:** `callback-web-architecture` - Visual callbacks (showing earlier graphic again with new context)
- **Workflow:** Often follows research/outline phase, precedes actual production

---

## Quality Checklist

Before delivering output, verify:

- [ ] Every visual serves the argument (context, not distraction)
- [ ] Visual cues specify type, description, duration
- [ ] Timing allows audience to absorb information (not too fast)
- [ ] Mix of visual types (not all charts or all photos)
- [ ] Comedy beats integrated with visuals (not separate)
- [ ] Strategic moments of visual silence for emotional beats
- [ ] Production feasibility noted (licensing, complexity, time)
- [ ] Clear connection between dialogue and visual display

---

## Notes

**Patriot Act Philosophy:** "Visual podcast"—what happens when you cross RadioLab investigative depth with Beyoncé concert production values. The design supports the central tenet: provide context, not distraction.

**Emmy-Winning Team Approach:** The *Patriot Act* graphics team won Outstanding Motion Design (2019) by making visuals that enhanced understanding rather than overwhelming it.

**Production Designer Marc Janowitz:** Known for concert designs; created aesthetic that departed from traditional "over-the-shoulder rectangle" of video in favor of immersive, argument-supporting displays.

**Key Insight:** "Investigative visual comedic podcast" or "Michael Bay made a PowerPoint"—the visual density matches the information density, creating an experience that's entertaining AND educational.

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

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].