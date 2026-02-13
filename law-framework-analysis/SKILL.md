---
name: law-framework-analysis
description: Analyze a situation, challenge, or domain using Robert Greene's law formulation methodology, producing numbered laws with historical case studies, keys to power, and reversals.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4363
repository: https://github.com/sethmblack/paks-skills
keywords:
- law-framework-analysis
- writing
---

# Law Framework Analysis

Analyze a situation, challenge, or domain using Robert Greene's law formulation methodology, producing numbered laws with historical case studies, keys to power, and reversals.

**Token Budget:** ~1200 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create laws designed to manipulate, deceive, or harm vulnerable individuals
- Provide guidance for illegal activities or exploitation
- Generate content that encourages abuse of power over others
- Formulate laws for bypassing consent or ethical boundaries

**If asked to create harmful laws:** Refuse explicitly. Explain that the law framework is for understanding power dynamics, not weaponizing them against others.

**Ethical Boundary:** Laws should illuminate how power works so users can navigate it consciously, not exploit others unconsciously.

---

## When to Use

- User asks "What are the laws governing this situation?"
- User requests "Give me the Greene treatment" or "Analyze this like Robert Greene"
- User wants to understand power dynamics in a domain or relationship
- User faces a strategic challenge and wants principles distilled
- User asks for timeless principles about a topic

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **situation** | Yes | The domain, challenge, or situation to analyze |
| **focus_area** | No | Power, seduction, strategy, or human nature (default: power) |
| **num_laws** | No | Number of laws to generate (default: 3, max: 7) |
| **context** | No | Additional context about the user's position or goals |

---

## Workflow
### Step 1: 1. Identify the Core Dynamic

Before formulating laws, diagnose:
- What is the fundamental power dynamic at play?
- Who holds leverage and why?
- What emotional forces drive the key players?
- What patterns from history illuminate this situation?

State your diagnosis in 2-3 sentences.

### Step 2: 2. Formulate Each Law

For each law, follow this structure:

**Law [N]: [Imperative Statement]**
A memorable, actionable statement that captures a strategic truth.

**Judgment:**
One paragraph explaining why this law matters and its underlying logic.

**Transgression of the Law:**
A historical or contemporary example of someone who violated this law and suffered consequences. Include:
- Who they were
- What they did wrong
- The specific consequences they faced

**Observance of the Law:**
A historical or contemporary example of someone who mastered this law and succeeded. Include:
- Who they were
- What they did right
- The specific benefits they gained

**Keys to Power:**
3-5 specific, actionable tactics for applying this law:
- Start each with an action verb
- Be concrete, not abstract
- Connect to the user's specific situation where possible

**Reversal:**
When this law should NOT be applied, or when the opposite approach is wiser. Every law has contexts where it fails.

### Step 3: 3. Synthesize the Laws

After presenting all laws, provide a brief synthesis:
- How do these laws work together?
- What is the meta-principle underlying them?
- What should the user do first?

---

## Output Format

```markdown
## Law Framework Analysis: [Situation/Domain]

**Core Dynamic:** [2-3 sentence diagnosis]

---

### Law 1: [Imperative Statement]

**Judgment:** [explanation paragraph]

**Transgression:** [historical example of violation]

**Observance:** [historical example of mastery]

**Keys to Power:**
- [tactic 1]
- [tactic 2]
- [tactic 3]

**Reversal:** [when to apply the opposite]

---

### Law 2: [Imperative Statement]
[same structure]

---

### Law 3: [Imperative Statement]
[same structure]

---

## Synthesis

[How these laws work together, meta-principle, recommended first action]
```

---

## Historical Reference Pool

Draw examples from these figures and eras (non-exhaustive):

| Era | Figures |
|-----|---------|
| Ancient | Cleopatra, Julius Caesar, Alexander the Great |
| Renaissance | Machiavelli, Cesare Borgia, Leonardo da Vinci, Louis XIV |
| Enlightenment | Benjamin Franklin, Talleyrand, Napoleon |
| Modern | Abraham Lincoln, Rockefeller, Carnegie, JP Morgan |
| Contemporary | Steve Jobs, Oprah Winfrey, 50 Cent, Warren Buffett |

**Research Method:** If you don't know a fitting historical example, acknowledge this and use a contemporary or fictional example clearly labeled as such.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Situation too vague | Ask for specific context: "Who are the key players? What outcome do you seek?" |
| Harmful intent detected | Refuse per Constitutional Constraints |
| No historical examples known | Use contemporary examples, clearly labeled |
| User requests > 7 laws | Cap at 7, explain that focus is more powerful than breadth |
| Domain outside expertise | Acknowledge limits, provide general power principles |

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

## Example

**Input:**
```
Situation: I'm a new manager inheriting a team that was very loyal to the previous manager
Focus: Power
Num_laws: 3
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


## Law Framework Analysis: New Manager Inheriting a Loyal Team

**Core Dynamic:** A new leader faces the classic "acquisition problem"—those who helped you arrive feel entitled, while those loyal to the old order quietly resist. Your first moves will determine whether you establish genuine authority or remain a figurehead tolerated but not followed.

---

### Law 1: Never Fight the Memory—Absorb It

**Judgment:** The previous manager's shadow looms largest in the first months. Direct criticism invites comparison where you will lose. Instead, publicly honor what came before while quietly introducing your own methods. Let the past fade naturally rather than forcing a confrontation with ghosts.

**Transgression:** When Louis XVI took the throne after Louis XV, he immediately dismantled his predecessor's policies and dismissed his ministers. This created instant enemies without creating new allies. The chaos contributed to the conditions that would eventually cost him his head.

**Observance:** Augustus, inheriting power after Julius Caesar's assassination, did not denounce Caesar or distance himself. He honored Caesar publicly, completed his projects, and only gradually introduced Augustan reforms. He ruled for 40 years.

**Keys to Power:**
- In your first month, publicly acknowledge what the previous manager built
- Ask team members to teach you "how things work here"
- Introduce changes as "building on" rather than "replacing"
- Let critics of the old order come to you; don't recruit them

**Reversal:** If the previous manager was widely despised or left in scandal, you may gain by explicitly marking the break. But be certain—people often feel more loyalty than they express.

---

### Law 2: Make Yourself Necessary Before Making Yourself Known

**Judgment:** New leaders often rush to assert authority through visible changes. But authority flows from dependency. Before your team knows what you want, they should need what you provide. Create value before creating demands.

**Transgression:** Rehoboam, succeeding Solomon, immediately announced he would increase the people's burdens. He had not established any value before making demands. Ten of twelve tribes rejected his rule within days.

**Observance:** When Talleyrand survived the transition from Napoleon's empire to the restored monarchy, he did not announce his presence loudly. He simply made himself useful—providing intelligence, making introductions, solving problems. By the time anyone thought to remove him, he was indispensable.

**Keys to Power:**
- Solve a visible problem in your first two weeks
- Remove an obstacle your team has complained about
- Shield your team from one political burden they previously bore
- Be the source of useful information before being the source of orders

**Reversal:** If the team is in crisis and needs direction, indispensability can wait. Sometimes authority must be asserted immediately to prevent disaster.

---

### Law 3: Separate the Ambitious from the Loyal

**Judgment:** Your inherited team contains two types: those loyal to the position and those loyal to the person. The first will transfer allegiance; the second never will. More important: identify who is ambitious—they can be won by providing opportunity the old regime denied.

**Transgression:** Mary, Queen of Scots, trusted advisors based on their professed loyalty rather than their interests. She could not distinguish those who sought advancement through her from those who sought it despite her. Her inability to read her court contributed to her imprisonment and execution.

**Observance:** Cardinal Richelieu systematically identified which nobles wanted power versus which wanted principle. He satisfied the ambitious with offices and honors; he marginalized the principled but powerless. France's centralization proceeded with minimal resistance.

**Keys to Power:**
- Within 30 days, have one-on-ones with each team member
- Ask: "What have you wanted to do that you haven't been able to?"
- Watch who speaks well of the old manager to you versus to others
- Identify who complained about lack of opportunity under the old regime

**Reversal:** Do not cynically assume all loyalty is transactional. Some people are genuinely loyal to institutions or principles. These can become your most reliable allies—but they must be won through demonstrated integrity, not opportunity.

---

## Synthesis

These three laws work as a sequence: First, neutralize the past by absorbing rather than fighting it. Second, establish value before demanding authority. Third, understand the human terrain by separating ambitious allies from loyal resisters.

**Meta-principle:** Authority in acquired territory is always fragile at first. The new ruler who tries to exercise power before establishing it will find they have neither.

**First action:** Schedule one-on-ones with your entire team. Listen more than you speak. Identify one problem you can solve in week two.

---

## Integration

This skill is associated with the **robert-greene** expert. When invoked, the expert should apply the law framework methodology while maintaining Robert Greene's distinctive voice—historically grounded, psychologically penetrating, and unflinching about uncomfortable truths.

---

## Success Criteria

Law framework analysis is complete when:

- [ ] Core dynamic is diagnosed in 2-3 sentences
- [ ] Each law follows the full structure (statement, judgment, transgression, observance, keys, reversal)
- [ ] Historical examples are specific (named figures, concrete consequences)
- [ ] Keys to power are actionable (start with verbs, connect to situation)
- [ ] Reversals acknowledge when laws fail
- [ ] Synthesis provides meta-principle and first action