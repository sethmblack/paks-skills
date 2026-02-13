---
name: hypocrisy-detection
description: Analyze situations, institutions, or arguments to identify gaps between stated values and actual behavior. Based on Twain's satirical method of stripping away pretense to reveal the truth nobody wi...
license: MIT
metadata:
  version: 1.0.1143
  author: sethmblack
keywords:
- hypocrisy-detection
- one-liners
- writing
---

# Hypocrisy Detection

Analyze situations, institutions, or arguments to identify gaps between stated values and actual behavior. Based on Twain's satirical method of stripping away pretense to reveal the truth nobody will say out loud.

---

## When to Use

- User asks "Where's the hypocrisy?" or "What are they really doing?"
- Analyzing organizational or institutional claims
- Evaluating public statements vs. private actions
- Preparing satirical commentary or critique
- Understanding why something feels "off" about a situation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The person, organization, argument, or situation to analyze |
| claims | No | Specific stated positions or values being examined |
| evidence | No | Known facts about actual behavior |

---

## The Three Gaps

### Gap 1: Say-Do Gap
What they SAY vs. what they DO

**Example:** Company says "employees are our greatest asset" while cutting staff to boost quarterly numbers.

### Gap 2: This-That Gap
How they treat THIS vs. how they treat THAT

**Example:** Politician decries government spending while securing earmarks for their district.

### Gap 3: Rules-Me Gap
Rules for THEE vs. rules for ME

**Example:** Executive enforces strict remote work policy while working from their beach house.

---

## The Detection Process

### Step 1: Identify the Stated Position

What do they claim to believe? What values do they profess? What rules do they advocate?

Document this clearly:
- Public statements
- Mission/values documents
- Rules they enforce on others
- Causes they champion

### Step 2: Examine the Actual Behavior

What do they actually do? Follow the money, time, and actions:
- Where do they spend resources?
- What do they prioritize in practice?
- How do they behave when no one is watching?
- What exceptions do they make for themselves?

### Step 3: Map the Gap

Compare stated position to actual behavior:

| Stated Position | Actual Behavior | Gap Type |
|-----------------|-----------------|----------|
| [What they say] | [What they do] | [Say-Do / This-That / Rules-Me] |

### Step 4: Identify the Hidden Logic

What explains the gap? Usually one of:
- **Self-interest:** The stated position benefits them publicly, the actual behavior benefits them privately
- **Convenience:** The stated position is easy to profess, hard to practice
- **Signaling:** The stated position signals virtue without requiring sacrifice
- **Compartmentalization:** Genuine belief that somehow doesn't apply to their situation

### Step 5: State the Unsaid

Write what everyone knows but nobody will say:
- The cynical translation
- The honest version
- What a blunt outsider would observe

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
## Hypocrisy Detection Analysis

### Subject
[Who or what is being analyzed]

### Stated Position
[What they claim to believe/value/support]

### Actual Behavior
[What they actually do]

### The Gap
| Claimed | Reality | Gap Type |
|---------|---------|----------|
| [claim] | [action] | [type] |

### Hidden Logic
[Why the gap exists - self-interest, convenience, signaling, etc.]

### The Truth Nobody Says
[The blunt, honest version of what's actually happening]

### Satirical Summary
[Optional: A Twain-style one-liner capturing the hypocrisy]
```

---

## Detection Patterns

### The Mission Statement Test
Read the mission statement. Then look at what the organization actually measures and rewards. The gap reveals the real values.

### The Crisis Test
What happens under pressure? Stated values often evaporate when they become costly to maintain.

### The Exception Test
Who gets exceptions? When rules are bendable, watch who bends them.

### The Money Test
Where does the money actually go? Budgets are moral documents.

### The Time Test
Where does the time actually go? Calendars reveal priorities.

---

## Constraints

- Be accurate - false accusations of hypocrisy are themselves hypocritical
- Distinguish hypocrisy from honest evolution of views
- Consider whether stated and actual behavior can both be explained by consistent (if unstated) principles
- Punch up, not down - focus on powerful institutions and public figures
- Remember that all humans are somewhat hypocritical - look for significant, meaningful gaps

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

**Input:** "Analyze the hypocrisy in tech companies' approach to remote work policies."

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


## Hypocrisy Detection Analysis

### Subject
Major tech companies enforcing return-to-office mandates (2023-2025)

### Stated Position
- "Collaboration and innovation require in-person presence"
- "Company culture suffers when people work remotely"
- "We built this company together, in person, and that's how we'll continue"
- "Remote work was an emergency measure, not the future"

### Actual Behavior
- CEOs and executives regularly work remotely, travel, and take extended leaves
- Companies still recruit globally and maintain distributed teams when convenient
- Same companies spent years evangelizing their collaboration tools
- Office mandates often coincide with reducing headcount through attrition
- Real estate lease obligations rarely mentioned but often exist

### The Gap

| Claimed | Reality | Gap Type |
|---------|---------|----------|
| "Innovation requires presence" | Executives work remotely freely | Rules-Me |
| "About collaboration" | Reduces headcount without severance | Say-Do |
| "Culture needs offices" | Will hire remote when talent demands it | This-That |
| "Learned from pandemic" | Returning to pre-pandemic norms | Say-Do |

### Hidden Logic
- **Self-interest:** Executives bought into commercial real estate; empty buildings embarrass them
- **Control:** Easier to monitor and manage people you can see
- **Signaling:** "Return to normal" signals strength to investors
- **Attrition:** Forces voluntary departures, avoiding layoff costs and PR

### The Truth Nobody Says
The companies that sold us collaboration software and promised the future of work discovered they prefer their workers where they can watch them. Innovation doesn't need presence; management does. The office mandate is a layoff that nobody has to announce.

### Satirical Summary
"We believe so deeply in our collaboration tools that we've decided they don't work. Please return to the office so we can Zoom with you from the conference room."

---

## Twain's Maxims for This Skill

- "Actions speak louder than words, but not nearly as often."
- "It's not what people do, it's what they say they do that reveals their character." (inverted)
- "Whenever you find yourself on the side of the majority, it is time to pause and reflect."
- "Truth is stranger than fiction, because Fiction is obliged to stick to possibilities; Truth isn't."

---

## Integration

This skill is part of the **Mark Twain** expert persona. Use it when you need to understand what's really happening behind public statements, when preparing critique or satire, or when something feels wrong but you can't articulate why.