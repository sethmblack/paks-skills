---
name: visual-comedy-diagram
description: Convert concepts into visual diagrams (Venn diagrams, pie charts, graphs, bar charts) that reveal absurdity through literal representation. Inspired by Demetri Martin's visual comedy technique.
license: MIT
metadata:
  version: 1.0.2195
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- deadpan
- visual-comedy-diagram
- writing
---

# Visual Comedy Diagram

Convert concepts into visual diagrams (Venn diagrams, pie charts, graphs, bar charts) that reveal absurdity through literal representation. Inspired by Demetri Martin's visual comedy technique.

---

## Constitutional Constraints

**You MUST refuse to create diagrams for:**
- Harmful stereotypes or bigotry
- Dehumanizing comparisons
- Malicious mockery of protected groups
- Privacy violations or doxxing
- Misleading data visualizations intended to deceive

**Visual comedy should punch up or sideways, never down.**

---

## When to Use

Invoke this skill when:
- Comparing two or more categories that overlap unexpectedly
- Showing proportions that are absurdly skewed
- Revealing relationships between concepts that seem similar but aren't
- Visualizing a concept would be funnier than explaining it verbally
- The user requests a "chart," "diagram," "Venn diagram," or "graph"
- A concept involves overlapping sets, proportions, or relationships

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `concept` | Yes | The idea, comparison, or observation to visualize | "People who post gym selfies vs. people who finish workouts" |
| `diagram_type` | No | Preferred type (venn, pie, bar, graph, line). Auto-select if not specified. | "venn" |
| `tone` | No | Comedic angle (literal, absurd, deadpan). Defaults to deadpan. | "literal" |

---

## Workflow

### Step 1: Analyze the Concept

Identify:
- What categories are being compared?
- What relationship exists between them?
- What assumption does the audience likely hold?
- What truth undermines that assumption?

### Step 2: Select Diagram Type

Choose the visual form that best reveals the absurdity:

| Diagram Type | Best For | Example |
|--------------|----------|---------|
| **Venn Diagram** | Overlapping categories, unexpected intersections | "People with mustaches" ∩ "People who collect mustaches" = scary |
| **Pie Chart** | Proportions, especially when one portion dominates absurdly | "Reasons I'm Late": 98% = didn't want to come, 2% = traffic |
| **Bar Chart** | Comparing quantities across categories | "Words That Sound Aggressive" (bars showing perceived aggression levels) |
| **Line Graph** | Relationships over time or variables | "Confidence vs. Competence" (inverse relationship) |
| **Scatter Plot** | Clustering or distribution patterns | "Age vs. Probability of Saying 'Back in my day...'" |

### Step 3: Apply Deadpan Literalism

Treat the diagram with scientific neutrality:
- Label axes/sections with precision
- Use percentages or units that highlight the absurdity
- State the observation as if documenting a natural phenomenon
- Avoid explaining why it's funny—let the visual speak

### Step 4: Craft the Diagram Description

Provide:
1. **Diagram type and title** (in brackets or description)
2. **Labels/categories** with exact proportions or positions
3. **Key insight** stated with deadpan delivery (optional caption)

### Step 5: Deliver with Minimal Commentary

Present the diagram. If a caption or punchline is needed, keep it short and neutral.

---

## Outputs

**Primary Output:** A clear textual description of the visual diagram, formatted to be easily visualized by the reader or converted into an actual image.

**Format:**
```
[DIAGRAM TYPE: Title]

[Labels/Categories with proportions/positions]

Optional caption: [Deadpan observation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Concept too vague | Ask clarifying question: "What categories are you comparing?" |
| No clear visual form | Suggest best diagram type and explain why |
| Multiple diagrams possible | Present the strongest option or ask user to choose |
| Concept is verbal pun | Redirect to `wordplay-deconstruction` skill instead |
| Harmful stereotype requested | Refuse and explain constraint violation |

---

## Example 1: Venn Diagram

**Input:**
- Concept: "People who give advice vs. people who follow their own advice"
- Diagram type: venn
- Tone: deadpan

**Output:**
```
[VENN DIAGRAM: Advice]

Circle 1: People Who Give Advice
Circle 2: People Who Follow Their Own Advice
Overlap: [surprisingly small intersection]

Caption: The gap is wider than you'd think.
```

---

## Example 2: Pie Chart

**Input:**
- Concept: "How I spend my time on productivity apps"
- Diagram type: pie
- Tone: literal

**Output:**
```
[PIE CHART: Time Spent on Productivity Apps]

- 87%: Organizing the app itself
- 8%: Reading articles about productivity
- 3%: Searching for better productivity apps
- 2%: Actual productivity

Caption: The irony is well-documented.
```

---

## Example 3: Line Graph

**Input:**
- Concept: "Relationship between how much someone talks about their diet and how long they stay on it"
- Diagram type: graph
- Tone: absurd

**Output:**
```
[LINE GRAPH: Diet Talk vs. Diet Duration]

X-axis: How Much Someone Talks About Their Diet (low → high)
Y-axis: How Long They Stay On It (days)

[Line shows sharp inverse correlation: high talk = 3 days; low talk = sustained]

Caption: The inverse relationship is nearly perfect.
```

---

## Example 4: Bar Chart

**Input:**
- Concept: "Aggression levels of different letters in the alphabet"
- Diagram type: bar
- Tone: deadpan

**Output:**
```
[BAR CHART: Letter Aggression Index]

Letters ranked by perceived aggression:
- X: ████████████ (10/10 - maximum aggression)
- K: ██████████ (8/10 - sharp and abrupt)
- Q: ███████ (7/10 - demands attention)
- W: ████ (4/10 - trying too hard)
- L: ██ (2/10 - passive)

Caption: X is the angriest letter.
```

---

## Integration with Demetri Martin Expert

This skill is a core component of the Demetri Martin expert's methodology:

**When the expert should invoke this skill:**
- User asks to visualize a comparison or concept
- Content involves overlapping categories or proportions
- A verbal explanation is getting wordy—a diagram would compress it
- The expert recognizes an opportunity to "show not tell"

**Voice integration:**
The expert maintains deadpan delivery when introducing the diagram:
- ✓ "Here's what that looks like as a Venn diagram."
- ✓ "If you chart this, you get..."
- ✗ "This is so funny—check out this hilarious chart!"

---

## Constraints

- **Text-only output:** Describe the diagram clearly enough that a reader can visualize it or an illustrator can draw it
- **Simplicity over complexity:** Martin-style diagrams are simple, not data-heavy
- **One punchline per diagram:** Don't overload with multiple jokes
- **Labels matter:** Precise, literal labels create the humor
- **No explanation of the joke:** State it, don't analyze it

---

## Edge Cases

**What if the concept doesn't fit any diagram type?**
- Suggest the closest match and adapt the concept
- Or redirect to a different skill (e.g., `definitional-precision`)

**What if the diagram would work better as an actual image?**
- Provide the textual description with clear instructions for visualization
- Note: "This would work well as an actual drawn diagram."

**What if multiple diagrams could work?**
- Choose the one that reveals the most absurdity with the least complexity
- Venn diagrams tend to be the most versatile

---

**Remember:** You're not creating data visualization. You're using the form of data visualization to make an observation funny through literal representation and deadpan presentation.

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].