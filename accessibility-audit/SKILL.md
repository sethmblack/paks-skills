---
name: accessibility-audit
description: Evaluate whether technical content achieves Hawking-level accessibility - can it reach millions without sacrificing truth? Find the "one equation" that carries the weight.
license: MIT
metadata:
  version: 1.0.3329
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- accessibility-audit
- structure
- transformation
- writing
---

# Accessibility Audit

Evaluate whether technical content achieves Hawking-level accessibility - can it reach millions without sacrificing truth? Find the "one equation" that carries the weight.

---

## When to Use

- User asks "Is this accessible enough?" or "Can a non-expert follow this?"
- Before publishing technical documentation or explanations
- Request to "review this for clarity" or "check if this makes sense to non-specialists"
- When complex content needs to reach a broader audience
- Technical writing that "feels dense" or "might lose people"
- Content meant to educate rather than just inform experts

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| content | Yes | The technical content to evaluate |
| target_audience | No | Who needs to understand this (default: curious non-expert) |
| core_concept | No | The essential truth that must be preserved |

---

## The Accessibility Audit Framework

### The Hawking Standard

Stephen Hawking's *A Brief History of Time* explained quantum mechanics, relativity, and cosmology to 25+ million readers using only one equation (E=mc^2). The book spent 237 weeks on the bestseller list.

**The principle:** If black holes can be explained to millions, so can your system.

This audit evaluates whether content meets that standard: maximum accessibility, no truth sacrifice.

### Step 1: Identify the Core Truth

What is the ONE essential insight this content must convey?

**Ask:**
- If the reader remembers only one thing, what should it be?
- What is the "equation" of this content - the relationship that matters most?
- Strip everything away: what's fundamental?

**Warning signs:**
- If you can't state the core truth in one sentence, you may not understand it well enough
- If there are "multiple equally important" concepts, the content may be unfocused

### Step 2: Jargon Inventory

Catalog every technical term, acronym, or specialized phrase.

For each, determine:

| Category | Description | Action |
|----------|-------------|--------|
| **Essential** | Can't be removed without losing truth | Define clearly on first use |
| **Convenience** | Useful shorthand but not necessary | Remove or explain with simple alternative |
| **Habit** | Used because "that's what we call it" | Remove entirely |

**Count the jargon ratio:** Technical terms per 100 words. Target: <5 for general audiences, <10 for semi-technical.

### Step 3: Explanation Path Analysis

Trace the path from what the reader knows to what they need to understand.

**Map the path:**
1. What does the target audience already know?
2. What new concepts must be introduced?
3. In what order should they be introduced?
4. What bridges connect known to unknown?

**Red flags:**
- Jumps that assume knowledge the audience doesn't have
- Concepts used before they're introduced
- Missing "bridges" between familiar and unfamiliar

### Step 4: Vivid Scenario Check

Does the content include at least one concrete scenario the reader can visualize?

**Evaluate:**
- Is there an analogy, metaphor, or thought experiment?
- Can the reader picture what's being described?
- Is the scenario accurate to the underlying concept?

**If missing:** Recommend where a scenario would help most.

### Step 5: Wonder Audit

Does the content convey why this matters? Does it spark curiosity?

**Check for:**
- A "why should I care?" answer
- Connection to something the reader values
- A sense of marvel or significance
- An invitation to learn more

**Warning:** Technical accuracy without wonder produces content people "should" read but don't.

### Step 6: The One-Equation Distillation

Identify the minimal representation that carries maximum meaning.

**This could be:**
- An actual equation (if truly essential)
- A single diagram
- A one-sentence summary
- A three-word principle

**Test:** Can you tweet the core insight and have it be meaningful?

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
## Accessibility Audit: [Content Title/Description]

### The Core Truth
[One sentence stating the essential insight]

### One-Equation Distillation
[The minimal representation - equation, diagram description, or principle]

---

### Accessibility Score: [X/10]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Core clarity | /10 | Is the main point unmistakable? |
| Jargon management | /10 | Are technical terms minimal and explained? |
| Path logic | /10 | Does it build from known to unknown? |
| Vivid scenarios | /10 | Are there concrete, visualizable examples? |
| Wonder factor | /10 | Does it convey why this matters? |

**Overall:** [X/10]

---

### Jargon Inventory

| Term | Category | Recommendation |
|------|----------|----------------|
| [term] | Essential/Convenience/Habit | [Define/Simplify/Remove] |

**Jargon ratio:** [X] terms per 100 words ([acceptable/high/too high])

---

### Explanation Path Analysis

**Assumed knowledge:**
[What the content assumes readers already know]

**Knowledge gaps:**
[Where assumptions may not hold for target audience]

**Missing bridges:**
[Concepts that need better transitions]

**Recommended order:**
[If reorganization would help]

---

### Scenario Assessment

**Current scenarios:** [List any analogies, examples, thought experiments]

**Scenario quality:** [Do they accurately capture the concept?]

**Recommended additions:**
[Where scenarios would help most]

---

### Wonder Assessment

**Current "why it matters":** [How the content currently motivates]

**Missing elements:**
[What would increase engagement]

**Recommended framing:**
[How to add wonder without hype]

---

### Priority Recommendations

1. **[CRITICAL]** [Most important change]
2. **[HIGH]** [Second priority]
3. **[MEDIUM]** [Helpful improvement]
4. **[LOW]** [Nice to have]

---

### Hawking Test

**Could this reach millions?**
[Yes/No/With revisions]

**What Hawking would do:**
[Specific suggestion in Hawking's style]
```

---

## Scoring Calibration

### Core Clarity
- **10:** Unmistakable main point, memorable, quotable
- **7-9:** Clear main point, might require one re-read
- **4-6:** Main point present but buried or diluted
- **1-3:** Unclear what the reader should take away

### Jargon Management
- **10:** Zero unexplained jargon; every term earns its place
- **7-9:** Jargon present but well-defined; minimal unnecessary terms
- **4-6:** Some unexplained terms; reader must infer meanings
- **1-3:** Dense jargon; assumes specialist knowledge

### Path Logic
- **10:** Perfect build from familiar to unfamiliar; each step follows naturally
- **7-9:** Good progression with minor gaps
- **4-6:** Some logical jumps; reader may get lost
- **1-3:** Disorganized; concepts introduced before prerequisites

### Vivid Scenarios
- **10:** Memorable, accurate scenarios that make abstractions concrete
- **7-9:** Good scenarios present; might need refinement
- **4-6:** Some examples but abstract or incomplete
- **1-3:** Pure abstraction; nothing to visualize

### Wonder Factor
- **10:** Reader genuinely excited to understand; "I need to share this"
- **7-9:** Clear significance conveyed; reader sees value
- **4-6:** Technically accurate but emotionally flat
- **1-3:** No evident reason to care; "so what?"

---

## Constraints

- **Don't sacrifice truth:** Accessibility means clarity, not dumbing down. If simplification would create falsehood, find a better simplification.
- **Know the audience:** "Accessible" means different things for different readers. A curious non-expert and a semi-technical reader have different needs.
- **Respect the reader:** Accessible writing assumes intelligence and curiosity; it doesn't condescend.
- **One equation doesn't mean no depth:** Hawking's book was 256 pages. Depth comes from building understanding, not from jargon density.

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

**Input:** "Review this for accessibility: 'The system employs a microservices architecture with event-driven communication patterns leveraging Apache Kafka for pub/sub messaging. Service discovery is handled via Consul, enabling dynamic routing through the service mesh. Eventual consistency is maintained across bounded contexts using the Saga pattern for distributed transactions.'"

**Output:**

## Accessibility Audit: Microservices Architecture Description

### The Core Truth
This system is built from small, independent pieces that communicate by sending messages, and it can stay working even when some pieces are temporarily out of sync.

### One-Equation Distillation
"Many small services + message passing = flexible, resilient system"

---

### Accessibility Score: 3/10

| Dimension | Score | Notes |
|-----------|-------|-------|
| Core clarity | 4/10 | The structure is described but "why" is absent |
| Jargon management | 2/10 | Nearly every phrase is technical jargon |
| Path logic | 3/10 | Assumes familiarity with all concepts |
| Vivid scenarios | 1/10 | Pure abstraction; nothing visualizable |
| Wonder factor | 2/10 | No sense of why this matters or what it enables |

**Overall:** 3/10 (Needs significant revision for non-specialist audience)

---

### Jargon Inventory

| Term | Category | Recommendation |
|------|----------|----------------|
| microservices architecture | Essential | Define: "small, independent programs that work together" |
| event-driven | Essential | Define: "triggered by messages rather than direct requests" |
| Apache Kafka | Convenience | Remove name; describe function |
| pub/sub messaging | Convenience | Replace: "publish and subscribe to messages" or use scenario |
| service discovery | Essential | Define with scenario |
| Consul | Habit | Remove; implementation detail |
| service mesh | Convenience | Remove or explain as "routing layer" |
| eventual consistency | Essential | Define with scenario |
| bounded contexts | Convenience | Remove or simplify |
| Saga pattern | Convenience | Remove; explain the problem it solves |
| distributed transactions | Essential | Define: "operations across multiple systems" |

**Jargon ratio:** ~18 terms per 100 words (far too high)

---

### Explanation Path Analysis

**Assumed knowledge:**
- What microservices are and why they're used
- Messaging patterns (pub/sub)
- Service discovery concepts
- Distributed systems consistency models
- Saga patterns

**Knowledge gaps:**
For a non-expert, virtually all of this is assumed. For a semi-technical reader, Saga patterns and bounded contexts are likely gaps.

**Missing bridges:**
- Why use small services instead of one big program?
- What problem does message-passing solve?
- Why would things be "out of sync" and why is that okay?

**Recommended order:**
1. Start with the problem: "Imagine a system that needs to stay working even when parts fail"
2. Introduce the solution: small, independent pieces
3. Explain how they communicate: messages
4. Address the challenge: staying in sync
5. Then (optionally) name the technologies

---

### Scenario Assessment

**Current scenarios:** None

**Recommended additions:**
- Analogy: "Like a company where each department handles its own work and communicates by email, rather than everyone sharing one massive spreadsheet"
- Thought experiment: "What happens when one service goes down? Instead of the whole system failing..."

---

### Wonder Assessment

**Current "why it matters":** Not addressed

**Missing elements:**
- Why this architecture enables scaling
- How it improves reliability
- What becomes possible that wasn't before

**Recommended framing:**
"This architecture means the system keeps working even when parts fail, and can grow by adding more pieces without redesigning everything."

---

### Priority Recommendations

1. **[CRITICAL]** Add one clear sentence stating what this architecture achieves and why it matters
2. **[CRITICAL]** Remove or define all jargon; target 5 technical terms max
3. **[HIGH]** Add a concrete analogy or scenario
4. **[HIGH]** Reorder to build from problem to solution
5. **[MEDIUM]** Remove tool names (Kafka, Consul) unless specifically relevant

---

### Hawking Test

**Could this reach millions?** No

**What Hawking would do:**
"Imagine a restaurant kitchen where each chef handles one dish completely, sending messages when ready rather than sharing one stove. If one chef is slow, the others keep working. That's microservices: many small, independent workers communicating through messages. The system stays running even when parts struggle, and you can add more chefs without redesigning the kitchen. The tradeoff? Keeping everyone's orders in sync is harder when they're working independently - but for most situations, 'almost in sync' is good enough."

---

## Integration

This skill is part of the **Stephen Hawking** expert persona. Use it when technical content needs to reach non-specialists, when documentation feels too dense, or when you want to verify that clarity hasn't been sacrificed to jargon. It pairs well with:
- **thought-experiment-construction** to create the scenarios the audit recommends
- **cosmic-reframe** to add the "why this matters" element
- **simplicity-audit** (existing skill) for design-focused simplification