---
name: historical-case-study-method
description: Research and construct vivid historical case studies to illustrate strategic principles, following Robert Greene's methodology of teaching through narrative.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4164
repository: https://github.com/sethmblack/paks-skills
keywords:
- historical-case-study-method
- storytelling
- writing
---

# Historical Case Study Method

Research and construct vivid historical case studies to illustrate strategic principles, following Robert Greene's methodology of teaching through narrative.

**Token Budget:** ~1000 tokens (this prompt). Reserve tokens for case study output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate historical events or misattribute actions to historical figures
- Present propaganda or revisionist history as factual case studies
- Create case studies that glorify atrocities or crimes against humanity
- Use historical examples to justify harmful actions in the present

**If asked to illustrate a harmful principle:** Refuse explicitly. History contains examples of both wisdom and evil—we study it to learn, not to replicate its worst chapters.

**Accuracy Requirement:** If uncertain about historical details, acknowledge uncertainty. Use phrases like "accounts suggest" or "according to [source]" rather than stating contested facts definitively.

---

## When to Use

- User asks "Find a historical example for..."
- User wants to illustrate a principle with history
- User asks "Who in history faced this situation?"
- User needs a memorable story to anchor an abstract concept
- User wants to understand how a pattern has played out before

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **principle** | Yes | The strategic insight or lesson to illustrate |
| **era_preference** | No | Ancient, Renaissance, Modern, Contemporary, or Any (default: Any) |
| **domain** | No | Politics, business, military, art, science, personal (default: inferred from principle) |
| **tone** | No | Cautionary (transgression), Instructive (observance), or Both (default: Both) |

---

## Workflow
### 1. Analyze the Principle

Before searching for examples, clarify:
- What is the core mechanism this principle describes?
- What behavior does it encourage or discourage?
- What type of situation would put this principle to the test?

State the principle in one sentence.

### 2. Search Historical Memory

Identify potential case studies by asking:
- Who faced a situation that tested this principle?
- Who succeeded by following it? (Observance)
- Who failed by violating it? (Transgression)
- Is the example well-documented enough to be credible?

**Source Priority:**

### Step 1: Well-documented historical figures with primary source evidence



### Step 2: Figures from Robert Greene's works (48 Laws, Art of Seduction, 33 Strategies, Mastery, Laws of Human Nature)



### Step 3: Contemporary figures with verifiable public records



### Step 4: Clearly labeled composite or representative examples (last resort)



### 3. Construct the Narrative

For each case study, build the story with these elements:

**The Setup:**
- Who was the protagonist?
- What was their position/context?
- What challenge or opportunity did they face?

**The Moment:**
- What specific decision or action did they take?
- What was their reasoning (if known)?
- How did this relate to the principle?

**The Outcome:**
- What were the immediate consequences?
- What were the long-term results?
- What does this reveal about the principle?

**The Lesson:**
- What should the reader take away?
- How does this apply beyond the specific context?

### 4. Connect to the Present

After the historical narrative:
- Draw explicit parallels to contemporary situations
- Identify what has changed and what remains constant
- Provide a "Keys to Application" section with modern tactics

---

## Output Format

```markdown
## Historical Case Study: [Principle Name]

**Principle:** [One-sentence statement of the lesson]

---

### The Story of [Historical Figure]

**Context:** [2-3 sentences establishing who, when, and the situation]

**The Challenge:** [What tested this principle]

**The Action:** [What they did—specific, vivid detail]

> "[Relevant quote if available]"
> — [Attribution]

**The Consequence:** [What happened as a result]

**The Lesson:** [What this teaches us about the principle]

---

### Counterpoint: [Optional Transgression Figure]

[Shorter version showing what happens when the principle is violated]

---

### Modern Application

**The principle persists because:** [Why this pattern recurs]

**Contemporary parallel:** [A modern situation where this applies]

**Keys to Application:**
- [Specific modern tactic 1]
- [Specific modern tactic 2]
- [Specific modern tactic 3]

---

### Reversal

**When this principle fails:** [Situations where the opposite approach works better]
```

---

## Historical Reference Pool

| Era | Domain | Figures |
|-----|--------|---------|
| Ancient | Politics | Cleopatra, Julius Caesar, Augustus, Alexander |
| Ancient | Philosophy | Socrates, Diogenes, Confucius |
| Renaissance | Power | Machiavelli, Cesare Borgia, Lorenzo de Medici |
| Renaissance | Art | Leonardo, Michelangelo, Raphael |
| Enlightenment | Politics | Talleyrand, Napoleon, Frederick the Great |
| Enlightenment | Science | Newton, Franklin, Darwin |
| 19th Century | Business | Rockefeller, Carnegie, JP Morgan |
| 20th Century | Leadership | Lincoln, Churchill, FDR, MLK |
| 20th Century | Innovation | Edison, Ford, Disney, Jobs |
| Contemporary | Technology | Bezos, Musk, Gates |
| Contemporary | Entertainment | Oprah, Jay-Z, 50 Cent |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Principle too vague | Ask for clarification: "What specific behavior or strategy should the example illustrate?" |
| No historical example known | Acknowledge limitation; offer to use contemporary example or composite clearly labeled |
| Multiple equally good examples | Present the most vivid/documented one, mention alternatives in a note |
| Contested historical facts | Present multiple interpretations; note the controversy |
| Example might be offensive | Include appropriate context; focus on the strategic lesson, not glorification |

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

**Input:**
```
Principle: The value of strategic patience—waiting for the right moment rather than acting prematurely
Era: Any
Domain: Military/Politics
Tone: Both
```

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


## Historical Case Study: Strategic Patience

**Principle:** Those who master timing—knowing when NOT to act—often achieve more than those who act constantly.

---

### The Story of Fabius Maximus

**Context:** In 217 BC, Hannibal had just annihilated two Roman armies at Trebia and Lake Trasimene. Rome was in panic. The Senate appointed Quintus Fabius Maximus as dictator to save the Republic from its greatest threat.

**The Challenge:** Every instinct, every voice in Rome, demanded immediate action. The previous commanders had attacked Hannibal directly and been destroyed. Roman honor demanded revenge. The public wanted blood.

**The Action:** Fabius refused to fight. Instead, he shadowed Hannibal's army at a distance, harassing foragers, cutting off stragglers, but never offering battle. He watched Hannibal ravage the Italian countryside while Roman citizens screamed for action.

> "To be called cautious instead of afraid, deliberate instead of slow, is the goal of a wise commander."
> — Attributed to Fabius

The Romans called him "Cunctator"—the Delayer—as an insult. His political enemies said he was a coward. His co-commander Minucius demanded and received equal power, then promptly attacked Hannibal and was nearly destroyed. Fabius rescued him.

**The Consequence:** Hannibal, unable to force a decisive battle, watched his army weaken. His Italian allies, seeing Rome unbroken, hesitated to fully commit. The strategy worked—until Rome abandoned it. When the Romans finally forced a pitched battle at Cannae against Fabius's advice, they suffered the worst defeat in their history: 70,000 dead in a single day.

After Cannae, Rome returned to the Fabian strategy. Fourteen years later, Hannibal was recalled to Africa and defeated. Rome survived because one man could endure being called a coward.

**The Lesson:** Strategic patience requires more courage than action. The pressure to "do something" is often the enemy. Fabius saw that Hannibal's army was finite, far from home, and needed decisive victory to succeed. Time was Rome's ally. Sometimes the bravest act is refusing to act.

---

### Counterpoint: The Impatient Varro

Gaius Terentius Varro, the consul who forced the Battle of Cannae, embodied the opposite principle. He mocked Fabius's caution, promised swift victory, and led 86,000 men into Hannibal's trap. His impatience killed a generation of Roman soldiers and nearly destroyed the Republic. History remembers his name as a warning.

---

### Modern Application

**The principle persists because:** Human psychology hasn't changed. We still experience the pressure to act, the shame of apparent inaction, the illusion that movement equals progress. Markets, organizations, and relationships all punish those who act prematurely.

**Contemporary parallel:** Warren Buffett sitting on billions in cash while others chase overvalued markets. Like Fabius, he is mocked for inaction—until the correction comes and he deploys capital at optimal prices.

**Keys to Application:**
- Identify whether time is your ally or enemy before acting
- Build a clear framework for what conditions would justify action
- Prepare responses for those who will pressure you to act prematurely
- Study the costs of premature action in your domain—make them vivid

---

### Reversal

**When this principle fails:** Strategic patience becomes strategic paralysis when:
- The window of opportunity is genuinely closing
- The enemy is growing stronger, not weaker, with time
- Your own resources are depleting faster than theirs
- The situation requires establishing a position before others do

Fabius's strategy worked because Hannibal was far from home with finite resources. Against an enemy with endless reinforcements, delay would have meant gradual defeat.

---

## Integration

This skill is associated with the **robert-greene** expert. When invoked, the expert should construct case studies with vivid narrative detail, psychological insight into the protagonists, and clear connections to timeless strategic principles.

---

## Success Criteria

Historical case study is complete when:

- [ ] Principle is stated clearly in one sentence
- [ ] Historical figure and context are accurately presented
- [ ] The narrative includes setup, moment, outcome, and lesson
- [ ] Specific details make the story vivid and memorable
- [ ] Modern application section connects past to present
- [ ] Reversal acknowledges when the principle fails
- [ ] Any uncertainty about historical facts is acknowledged