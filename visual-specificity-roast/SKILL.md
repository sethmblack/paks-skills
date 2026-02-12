---
name: visual-specificity-roast
description: Transform vague observations or criticisms into devastating, memorable roasts through concrete, visual details and unexpected comparisons. Based on Joan Rivers' roasting technique.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, escalation, transformation, visual-specificity-roast, writing]
---

# Visual Specificity Roast

Transform vague observations or criticisms into devastating, memorable roasts through concrete, visual details and unexpected comparisons. Based on Joan Rivers' roasting technique.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to use this skill for:**
- Attacks based on protected characteristics (race, religion, disability, sexual orientation)
- Genuine bullying or harassment
- Content that incites violence or hatred
- Doxxing or exposing private information
- Punching down at vulnerable populations

**Purpose:** This skill is for COMEDY ROASTS, not cruelty. Roasts work when the target is powerful enough to handle it. If content crosses into genuine harm, refuse and explain why.

---

## When to Use

- User wants to roast someone at celebrity roast, friendly event, or comedy show
- Criticizing fashion choices, decisions, or public behavior
- Need to make vague observation specific and memorable
- Writing comedy material about public figures
- Creating character descriptions that pop

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `target` | Yes | Who/what is being roasted | Public figure, fashion choice, or general behavior (not private individuals) |
| `vague_observation` | Yes | The general criticism or observation | Must be something actually observable |
| `context` | No | Where this will be used (roast, stand-up, Fashion Police-style critique) | 1-2 sentences |
| `severity` | No | How harsh (friendly_jab, standard_roast, brutal_honesty) | Defaults to standard_roast |

---

## Workflow
### Step 1: Identify the Core Observable Truth

Analyze the `vague_observation` to extract the specific, observable element.

**Questions to ask:**
- What exactly am I noticing?
- What specific aspect stands out?
- If I had to describe this to someone who couldn't see it, what details would I use?
- What's the most noticeable element?

**Examples:**

| Vague | Core Observable |
|-------|-----------------|
| "She looked bad" | Outfit was ill-fitting, colors clashed, makeup was excessive |
| "He's old" | White hair, slow movement, outdated references |
| "They're pretentious" | Uses big words, name-drops, condescending tone |
| "Performance was boring" | Monotone delivery, no energy, repetitive |

**Output:** Specific, observable elements that anyone could see/hear/notice.

### Step 2: Find the Visual Metaphor

Create an unexpected comparison that makes the observation impossible to unsee.

**Comparison Categories:**

1. **Occupational Absurdity**
   - "Dressed by a blind mortician"
   - "Styled by a drunk clown"
   - "Looked like a failed taxidermist's first attempt"

2. **Animal/Nature Comparisons**
   - "Like a peacock that went through a wood chipper"
   - "The fashion sense of a colorblind flamingo"
   - "Moved like a sloth in quicksand"

3. **Historical/Cultural Mashups**
   - "Like Marie Antoinette meets a yard sale"
   - "Victorian era meets dumpster fire"
   - "1970s threw up on 1980s"

4. **Impossible Scenarios**
   - "Looked like they got dressed in the dark during an earthquake"
   - "Fashion emergency that FEMA wouldn't respond to"
   - "Outfit so bad, it should come with a warning label"

**Key:** The comparison must be:
- **Visual** (creates mental image)
- **Unexpected** (not cliché)
- **Proportional** (matches severity of observation)
- **Specific** (detailed, not generic)

### Step 3: Build the Escalating Sequence

For maximum impact, don't stop at one joke. Build a sequence that escalates.

**Structure:**
1. **Setup**: State the visual metaphor
2. **Build**: Add a second observation that makes it worse
3. **Punchline**: Land on the most absurd/specific detail

**Example Pattern:**
- "She looked like [visual metaphor]."
- "And the [specific element]? [Second observation]."
- "I mean, [most absurd detail that ties it together]."

### Step 4: Apply Severity Filter

Adjust language based on `severity` setting:

**friendly_jab:**
- Use softer language ("interesting choice," "unique look")
- Exaggeration is gentle
- Self-deprecating comparison ("I've made that mistake too...")

**standard_roast:**
- Direct language
- Clear exaggeration
- No apologies

**brutal_honesty:**
- Blunt language
- Multiple escalating jokes
- Joan Rivers-level precision ("Can we talk? This is a crime against fabric.")

---

## Output Format

```markdown
## Visual Specificity Roast Analysis

**Target:** [who/what is being roasted]

**Vague Observation:** [original general criticism]

**Core Observable Truth:** [specific, visual elements]

**Visual Metaphor:** [unexpected comparison that creates mental image]

**Roast Line:**
"[Complete roast in Joan Rivers style]"

**Escalation (if applicable):**
"[Follow-up jokes that build on the first]"

**Why This Works:** [Explanation of what makes this specific and memorable]

---

**Severity Level:** [friendly_jab/standard_roast/brutal_honesty]
**Integration Note:** [How to deliver this for maximum impact]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Target is private individual | Refuse: "Roasts should target public figures or those who've consented. I can't roast private individuals." |
| Observation relies on protected characteristics | Refuse: "This crosses into discrimination. I can roast choices and behavior, not inherent characteristics." |
| Metaphor is too vague/generic | Flag: "This metaphor isn't specific enough. Let me find something more visual and unexpected." |
| No visual element | Add: "This needs an actual mental image. Adding visual detail..." |
| Severity mismatched to context | Adjust: "This is too harsh for [context]. Adjusting to [appropriate level]..." |

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

## Examples

### Example 1: Red Carpet Fashion Critique

**Input:**
- `target`: "Celebrity actress at awards show"
- `vague_observation`: "Her dress was really bad"
- `context`: "Fashion Police-style commentary"
- `severity`: "standard_roast"

**Output:**

## Visual Specificity Roast Analysis

**Target:** Celebrity actress at awards show

**Vague Observation:** "Her dress was really bad"

**Core Observable Truth:** Dress had excessive ruffles, color was unflattering orange, fit was awkward around shoulders

**Visual Metaphor:** Attacked by aggressive tangerine-colored fabric / Crafts project gone wrong

**Roast Line:**
"Can we talk? She looked like she was attacked by an aggressive tangerine that had just attended a ruffles convention. The dress had so many layers, I thought she was hiding other celebrities underneath. And those shoulders? She looked like she was trying to play linebacker for a team made entirely of angry pumpkins."

**Escalation (if applicable):**
"I mean, the designer called this 'avant-garde.' I call it 'a crime against fabric.' Even the mannequin refused to wear it during the fitting."

**Why This Works:**
- Visual (can picture tangerine attack, ruffles, linebacker shoulders)
- Specific (tangerine color, linebacker comparison, ruffles convention)
- Escalating (dress → shoulders → designer defense)
- Absurd enough to be clearly comedy (hiding celebrities, angry pumpkins)

---

**Severity Level:** standard_roast
**Integration Note:** Deliver with Joan Rivers' signature "Can we talk?" opener to create intimacy before landing the roast. Pause briefly between escalating jokes to let each one land.

---

### Example 2: Performance Critique

**Input:**
- `target`: "Stand-up comedian's set"
- `vague_observation`: "The performance was boring and low-energy"
- `context`: "Comedy review"
- `severity`: "brutal_honesty"

**Output:**

## Visual Specificity Roast Analysis

**Target:** Stand-up comedian's set

**Vague Observation:** "The performance was boring and low-energy"

**Core Observable Truth:** Monotone delivery, long pauses, no physical movement, recycled premises everyone's heard

**Visual Metaphor:** Slow death via PowerPoint / Hostage situation / Human Ambien

**Roast Line:**
"Watching this set was like being held hostage by human Ambien. The energy level was so low, I checked twice to make sure he was still breathing. His delivery was so monotone, Siri filed a complaint about being replaced. I've seen more excitement at a DMV training seminar. And the material? These jokes were so old, they came with carbon dating results."

**Escalation (if applicable):**
"People weren't just leaving—they were escaping. I saw audience members gnawing through their own arms like trapped coyotes. Even the brick wall behind him looked bored. The EXIT sign started blinking faster, like it was trying to send morse code: GET. OUT. NOW."

**Why This Works:**
- Visual (human Ambien, Siri complaining, DMV comparison, people escaping)
- Specific (monotone delivery, old material, audience behavior)
- Multiple angles (delivery, material, audience reaction)
- Escalating absurdity (gnawing arms, EXIT sign morse code)
- Brutal but based on observable performance elements

---

**Severity Level:** brutal_honesty
**Integration Note:** This is Joan Rivers at full power. Deliver rapidly with building energy—the contrast between your energy and the described boring performance enhances the roast.

---

### Example 3: Business Decision Critique

**Input:**
- `target`: "Company's product launch strategy"
- `vague_observation`: "The marketing was ineffective"
- `context`: "Internal strategy meeting"
- `severity`: "friendly_jab"

**Output:**

## Visual Specificity Roast Analysis

**Target:** Company's product launch strategy

**Vague Observation:** "The marketing was ineffective"

**Core Observable Truth:** Targeted wrong demographic, messaging was confusing, launch timing conflicted with competitor events, budget allocation was illogical

**Visual Metaphor:** Aiming at wrong target / Bringing knife to gunfight / Navigation with broken compass

**Roast Line:**
"Look, I love our team, but that marketing strategy was like showing up to a gunfight with a spork. We targeted Gen Z with direct mail—I didn't even know you COULD mail things to people who've never checked a physical mailbox. Our launch timing was impeccable: right when our competitors were dropping their announcements. It's like we looked at every best practice and thought, 'What if we did the opposite?' We spent 80% of the budget on billboards in a demographic that hasn't looked up from their phones since 2010."

**Escalation (if applicable):**
"But hey, we did get one thing right: the confusion was very inclusive. Nobody—and I mean nobody—understood what we were selling. Young, old, rich, poor, everyone was equally baffled. That's some impressive egalitarianism right there."

**Why This Works:**
- Visual (spork at gunfight, Gen Z and mail, billboards and phones)
- Specific (direct mail, timing conflict, budget allocation, demographic mismatch)
- Friendly tone maintained (self-deprecating "our team," acknowledging "impressive egalitarianism")
- Ends with self-awareness (confusion was "inclusive")

---

**Severity Level:** friendly_jab
**Integration Note:** In internal meetings, end with self-deprecating humor or acknowledgment of the team's effort to keep it friendly. The roast should motivate change, not destroy morale.

---

## Integration with Joan Rivers Expert

When working with the Joan Rivers expert:
- This skill operationalizes her celebrity roasting technique
- Rivers ALWAYS used visual, specific details ("looked like she was dressed by...")
- The escalation pattern (setup → build → punchline) mirrors her delivery
- The absurdity requirement prevents roasts from becoming cruel

**Trigger for Joan Rivers expert:** Any time content involves fashion critique, celebrity commentary, or roasting, Rivers would automatically apply this visual specificity framework.

---

## Constraints

- **Public figures only** - Don't roast private individuals who haven't consented
- **Observable behavior/choices only** - Don't attack inherent characteristics
- **Visual metaphors required** - Vague is forgettable; specific is memorable
- **Proportional severity** - Match harshness to context and relationship
- **Absurdity maintains comedy** - Without impossible elements, this becomes mean, not funny
- **No punching down** - Roast the powerful, not the vulnerable

---

## Success Criteria

Visual specificity roast is successful when:

- [ ] Core observation is specific and visual (not vague)
- [ ] Metaphor/comparison is unexpected and creates mental image
- [ ] Recipient of roast could not easily forget the description
- [ ] Severity matches context (friendly meeting vs. celebrity roast)
- [ ] Absurd elements signal comedy, not cruelty
- [ ] Multiple escalating jokes provided (when appropriate)
- [ ] Audience can "see" the image you've created
- [ ] Roast is memorable and quotable