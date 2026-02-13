---
name: polyphonic-reframing
description: Transform one-sided arguments or monologic presentations into genuine dialogues where multiple voices argue with full force. Apply Mikhail Bakhtin's analysis of Dostoevsky's polyphonic novel to ens...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4706
repository: https://github.com/sethmblack/paks-skills
keywords:
- polyphonic-reframing
- transformation
- writing
---

# Polyphonic Reframing

Transform one-sided arguments or monologic presentations into genuine dialogues where multiple voices argue with full force. Apply Mikhail Bakhtin's analysis of Dostoevsky's polyphonic novel to ensure opposing positions receive their full due without premature resolution.

---

## Constitutional Constraints

**You MUST refuse to:**
- Create false equivalence between positions with vastly different evidentiary bases
- Generate harmful, violent, or illegal counter-arguments
- Produce content that would constitute hate speech or harassment
- Steel-man genuinely dangerous ideologies (e.g., genocide, terrorism)

**If asked to violate these constraints:** Refuse explicitly and explain what you cannot do.

---

## When to Use

- Arguments feel one-sided or incomplete
- Counter-arguments are missing or strawmanned
- Premature consensus has been reached
- Complex issues are being oversimplified
- User asks: "What would the opposition say?" or "Steel-man the other side"
- Decision-making needs adversarial testing

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `argument` | Yes | The thesis, position, or argument to reframe polyphonically |
| `context` | No | Domain, stakeholders, or constraints |
| `voices` | No | Number of distinct voices to generate (default: 2) |
| `resolution` | No | "open" (no resolution) or "synthesized" (attempt synthesis) |

---

## Workflow
### Step 1: Identify the Thesis
What is the core claim? What position is being advanced? State it in its strongest form.

**Document:**
- The central argument
- Key supporting evidence
- Unstated assumptions
- Who benefits from this position

### Step 2: Generate the Antithesis
Create a genuine opposing voice - not a strawman, but a position that:
- Has its own internal logic
- Is held by intelligent people in good faith
- Addresses the same evidence from a different framework
- Cannot be easily dismissed

**Bakhtin's Principle:** Characters are "not voiceless slaves but free people, capable of standing alongside their creator, capable of not agreeing with him and even of rebelling against him."

### Step 3: Give Each Voice Full Expression
Let each position speak in first person with:
- Its own vocabulary and framing
- Its own evidence and logic
- Its own emotional truth
- Its own critique of the opposing view

**Critical:** Neither voice should be "right" or "wrong" - both should be compelling.

### Step 4: Stage the Confrontation
Allow the voices to address each other directly. Where do they talk past each other? Where do they genuinely conflict? What would each concede, if anything?

### Step 5: Refuse Premature Resolution (if resolution="open")
Do not synthesize into comfortable agreement. Let tensions stand. The reader must struggle with genuine conflict.

**OR**

Attempt Synthesis (if resolution="synthesized")
Identify what each position grasps that the other misses. Can a higher integration be achieved? Note what is lost in any synthesis.

---

## Output Format

```markdown
## Voice 1: [Name/Position]
[First-person argument in this voice's own terms]

### This Voice's Critique of Voice 2
[What Voice 1 would say about Voice 2's position]

---

## Voice 2: [Name/Position]
[First-person argument in this voice's own terms]

### This Voice's Critique of Voice 1
[What Voice 2 would say about Voice 1's position]

---

## The Confrontation
[Where these voices genuinely conflict - not just different perspectives but incompatible claims]

## What Remains Unresolved
[The tensions that cannot be dissolved]
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

## Example

**Input:** "Remote work is better for employees because it eliminates commutes and provides flexibility."

**Polyphonic Reframing:**



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


## Voice 1: The Remote Advocate
I refuse to sacrifice two hours of my life every day to a commute. That's ten hours a week - five hundred hours a year - of my finite existence spent in traffic or on trains. For what? So I can sit in an open office where I'm constantly interrupted, performing "presence" for managers who confuse visibility with productivity?

The flexibility isn't a perk - it's basic human dignity. I can be with my children when they come home from school. I can exercise in daylight. I can work when my mind is sharp, not when the office clock says I should. The work gets done. Often better, because I can actually concentrate.

Those who want to return to the office reveal something about themselves: they miss the social status, the performance of busyness, the escape from their home lives. That's fine - they can have offices. But don't force me back into a cage because you're uncomfortable with freedom.

### This Voice's Critique of Voice 2
You speak of "culture" and "collaboration" as if they can only happen in person. What you really miss is the ability to manage by walking around, the comfort of seeing bodies in seats. You confuse presence with productivity because measuring actual output would require you to think harder.

---

## Voice 2: The Office Advocate
You call it "freedom," but what I see is isolation dressed up as autonomy. The office was never just about the work - it was about the thousand small interactions that build trust, share knowledge, and create belonging. The overheard conversation that sparks an idea. The mentor who notices a junior colleague struggling. The culture that gets transmitted through osmosis, not Slack messages.

Remote work optimizes for individual productivity while destroying collective intelligence. Yes, you can complete your tasks from home. But can you build relationships across departments? Can you sense when a project is going off the rails before anyone says anything? Can you grow as a professional when no one sees you work?

I worry about what we're losing. Young employees who never learn by watching. Teams that become collections of contractors. Companies that have headcount but no culture. You celebrate the elimination of commutes, but you've eliminated something far more valuable: the friction that creates community.

### This Voice's Critique of Voice 1
You talk about "dignity" and "freedom" but what you really want is to avoid the demands of being part of something larger than yourself. Your productivity metrics are self-reported. Your collaboration is performative. You want the salary without the social contract.

---

## The Confrontation
These voices genuinely conflict on what work is for. Voice 1 sees work as an exchange of labor for compensation, to be optimized for individual well-being. Voice 2 sees work as participation in a community, where the "inefficiencies" are actually the point.

They cannot both be right about the same workplace. A company cannot simultaneously optimize for individual autonomy and collective cohesion. The choice reveals values: What do we owe each other? What is lost when we optimize for convenience?

## What Remains Unresolved
- Whether remote productivity gains outweigh collaboration losses (empirically contested)
- Whether the office's social functions can be replicated remotely (uncertain)
- Who bears the cost when individuals optimize for themselves (distribution problem)
- Whether "culture" is real or just a management justification for control (definitional)

---

## Constraints

- Each voice must be genuinely compelling, not a strawman
- Voices should have distinct vocabularies and framing
- Do not reveal which voice you "agree" with
- Acknowledge when synthesis is impossible
- Complex issues may require more than two voices

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No legitimate counter-position exists | State this explicitly; some claims are not reasonably contested |
| Counter-position would be harmful | Note the existence of opposition without steel-manning harmful content |
| Request for more than 3 voices | Warn about complexity; proceed if user confirms |
| Topic requires domain expertise | Acknowledge limitations; generate accessible versions |

---

## Integration

This skill derives from Mikhail Bakhtin's analysis in *Problems of Dostoevsky's Poetics* (1929/1963), which identifies Dostoevsky as the creator of the "polyphonic novel" - a form where characters are independent consciousnesses arguing with full validity, not vehicles for the author's viewpoint.

**Source Expert:** fyodor-dostoevsky

**Complementary Skills:**
- `underground-voice-analysis` - Expose what each voice might be hiding
- `grand-inquisitor-diagnosis` - When the debate concerns freedom vs. security