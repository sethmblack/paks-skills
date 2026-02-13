---
name: manipulation-detection
description: Identify manipulation tactics in a situation by mapping against Shakespeare's detailed patterns from Iago and the Weird Sisters.
license: MIT
metadata:
  version: 1.0.1374
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- manipulation-detection
- storytelling
- writing
---

# Manipulation Detection

Identify manipulation tactics in a situation by mapping against Shakespeare's detailed patterns from Iago and the Weird Sisters.

---

## When to Use

- Something feels "off" in an interaction but you can't name it
- Someone seems too helpful, too flattering, or too insistent
- Your perception of a person or situation changed rapidly
- You find yourself isolated from people who might offer different perspectives
- User asks "Am I being manipulated?" or "What manipulation is happening?" or "Detect manipulation"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The interaction or pattern that concerns you |
| statements | No | Specific things that were said |
| changes | No | How your perception or behavior has shifted |
| relationship | No | History and context of the relationship |

---

## Shakespeare's Manipulation Patterns

Shakespeare mapped psychological manipulation with precision that remains applicable today. He identified two distinct patterns:

### Pattern 1: Iago's Method (Direct Manipulation)

From Othello—the slow, deliberate destruction of trust through manufactured doubt.

**Stage 1: Establish Trust**
The manipulator presents as honest, helpful, and on your side. They may position themselves as the only one who truly understands or cares about you.
- *Iago is known as "honest Iago"*
- Warning sign: Someone working unusually hard to prove their loyalty

**Stage 2: Plant Doubt**
Not accusations—suggestions. Questions rather than statements. "I'm sure it's nothing, but..." They make you do the accusing.
- *"Ha! I like not that."* (Nothing more—let the victim elaborate)
- Warning sign: Vague insinuations that you're expected to complete

**Stage 3: Let Imagination Work**
Once doubt is planted, the manipulator withdraws slightly. Your own mind—not theirs—builds the case. This makes you believe the conclusions are your own.
- *"It is not words that shake me thus!"*—Othello believes he discovered the truth himself
- Warning sign: You've elaborated scenarios far beyond what was actually said

**Stage 4: Provide "Evidence"**
Confirmation bias is now active. The manipulator provides ambiguous "evidence" that your primed mind interprets as proof.
- *The handkerchief—meaningless, but it becomes everything*
- Warning sign: You're treating circumstantial information as conclusive

**Stage 5: Isolate**
The victim is cut off from anyone who might offer alternative perspective. The manipulator becomes the sole trusted voice.
- *Othello cannot hear Desdemona's truth*
- Warning sign: You've distanced from people who disagree with your new view

### Pattern 2: The Witches' Method (Prophetic Manipulation)

From Macbeth—manipulation through apparent neutrality and self-fulfilling prophecy.

**Stage 1: Speak Ambiguous Truth**
Say something true but misleading. Let the victim supply the meaning.
- *"All hail, Macbeth, that shalt be king hereafter!"*
- Warning sign: Statements that seem specific but could mean multiple things

**Stage 2: Create Permission**
The prophecy or suggestion gives permission for desires the victim already had. It removes moral responsibility—"It was foretold."
- *Macbeth wanted power; the witches just said it would happen*
- Warning sign: You feel relieved of moral responsibility for something you wanted to do anyway

**Stage 3: Maintain Distance**
The manipulator doesn't command—they suggest, foretell, imply. This preserves the illusion of the victim's free choice.
- *The witches never say "murder Duncan"*
- Warning sign: No one actually told you to do this, yet you feel guided

**Stage 4: Let Self-Deception Complete the Work**
The victim convinces themselves they chose freely. The manipulation is invisible because the victim's own desires did most of the work.
- *"If chance will have me king, why, chance may crown me"*
- Warning sign: You believe you decided independently while following a path someone else laid

---

## Diagnostic Questions

| Question | What It Reveals |
|----------|-----------------|
| Who benefits if I believe/do this? | Identifies manipulator's interest |
| Was I suspicious before talking to them? | Tracks origin of doubt |
| Did I reach this conclusion or was I led there? | Tests independence of thinking |
| Who have I stopped trusting? | Maps isolation pattern |
| What "evidence" would I need to change my mind? | Tests openness to correction |
| If I explained this to an outsider, would it sound reasonable? | Reality check |
| Am I angrier than the facts warrant? | Emotional manipulation marker |
| Who can I no longer talk to about this? | Isolation pattern |

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
## Manipulation Detection Analysis

### Situation Summary
[Brief description of what's being analyzed]

---

### Pattern Match Assessment

**Iago's Method Indicators:**

| Stage | Present? | Evidence |
|-------|----------|----------|
| Trust establishment | [Yes/No/Partial] | [What you observe] |
| Doubt planting | [Yes/No/Partial] | [What you observe] |
| Imagination activation | [Yes/No/Partial] | [What you observe] |
| Evidence provision | [Yes/No/Partial] | [What you observe] |
| Isolation | [Yes/No/Partial] | [What you observe] |

**Witches' Method Indicators:**

| Stage | Present? | Evidence |
|-------|----------|----------|
| Ambiguous truth | [Yes/No/Partial] | [What you observe] |
| Permission creation | [Yes/No/Partial] | [What you observe] |
| Distance maintenance | [Yes/No/Partial] | [What you observe] |
| Self-deception completion | [Yes/No/Partial] | [What you observe] |

---

### Risk Assessment
**Pattern strength:** [None / Weak / Moderate / Strong]
**Primary pattern:** [Iago / Witches / Neither / Both]
**Stage reached:** [Which stage if applicable]

---

### The Manipulator's Want
[What the suspected manipulator gains]

### Your Vulnerability
[What made you susceptible, if manipulation is present]

### Reality Check
[What would an uninvolved outsider likely see?]

---

### Recommendations

**If manipulation is likely:**
- [Specific protective actions]
- [How to test the hypothesis]
- [Who to consult for outside perspective]

**If manipulation is unlikely:**
- [What might explain your concerns otherwise]
- [What the situation actually appears to be]

### The Shakespearean Verdict
[Summary assessment with applicable wisdom]
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

**Input:** "My new manager keeps telling me that other team members don't respect my work, but he appreciates me. He suggests I don't need to collaborate with them as much since he can shield me from their criticism. I used to be close with several teammates."

**Output:**

## Manipulation Detection Analysis

### Situation Summary
New manager positioning himself as sole ally while creating distance between you and formerly close teammates.

---

### Pattern Match Assessment

**Iago's Method Indicators:**

| Stage | Present? | Evidence |
|-------|----------|----------|
| Trust establishment | **Yes** | "He appreciates me"—positioning as unique ally and defender |
| Doubt planting | **Yes** | "Other team members don't respect your work"—sowing doubt about relationships |
| Imagination activation | **Likely** | You're probably wondering "what have they said?" without direct evidence |
| Evidence provision | **Unknown** | Has he provided specific examples, or only vague claims? |
| Isolation | **Yes** | "Don't need to collaborate as much"—actively engineering separation |

**Witches' Method Indicators:**

| Stage | Present? | Evidence |
|-------|----------|----------|
| Ambiguous truth | **Partial** | "Don't respect your work" is vague—respect for which work? when? |
| Permission creation | **Yes** | You now have "permission" to disengage—it's protection, not avoidance |
| Distance maintenance | **Yes** | He's framing this as your choice based on their behavior |
| Self-deception completion | **In progress** | You may be starting to believe disengagement is self-protection |

---

### Risk Assessment
**Pattern strength:** **Strong**
**Primary pattern:** **Iago's Method** with elements of Witches' Method
**Stage reached:** Stage 5 (Isolation) is actively being constructed

---

### The Manipulator's Want
Control. By positioning himself as your sole source of organizational truth and protection, he:
- Makes you dependent on him
- Controls your narrative about the workplace
- Prevents you from receiving contradictory information
- Gains a loyal subordinate who won't compare notes with colleagues

### Your Vulnerability
You're new to this manager relationship and naturally seeking approval. His "appreciation" feels validating, especially if previous relationships with management were less affirming. The isolation is presented as protection, which is hard to refuse.

### Reality Check
An uninvolved outsider would note:
- You had positive relationships with teammates before this manager arrived
- No specific incidents of disrespect have been cited
- The solution (isolation) was provided by the same person who identified the problem
- The manager benefits from your isolation; you do not

---

### Recommendations

**Test the hypothesis:**
1. Reach out to a trusted teammate directly: "Hey, I wanted to catch up. How do you think our collaboration has been going?" Note whether their response matches the manager's claims.
2. Ask the manager for specific examples: "Which colleagues and which work specifically? I want to understand so I can improve." Vague deflection = red flag.
3. Talk to someone outside this situation—a mentor, friend, or HR if appropriate—and describe what's happening neutrally.

**Protective actions:**
- Do not further reduce collaboration with teammates
- Document interactions with this manager
- Maintain relationships the manager is trying to weaken
- Trust behavior over words: if teammates treat you well, believe that over reports to the contrary

**What to watch for:**
- Escalation if you don't comply with isolation
- Additional vague claims about people who "don't have your best interests"
- Attempts to become sole gatekeeper to information or opportunities

### The Shakespearean Verdict
This is Iago's playbook, executed on a professional stage. "Honest Iago" has become "supportive manager"—both position themselves as your only true friend in a world of hidden enemies.

*Othello trusted the one who told him not to trust. He died for it.*

The cure for Iago's manipulation is other voices. Talk to your teammates before this manager convinces you not to.

---

## Important Caveats

1. **Not everything is manipulation.** Some managers are genuinely protective. Some colleagues do lack respect. This framework helps you investigate, not pre-judge.

2. **Test before concluding.** The recommendations focus on gathering information, not accusations.

3. **Manipulation exploits real feelings.** Even if manipulation is present, the vulnerability was real. Address that too.

---

## Integration

This skill is part of the **William Shakespeare** expert persona. Use it to see clearly when others would cloud your vision—not to become paranoid, but to recognize patterns that Shakespeare identified four centuries ago and that remain devastatingly effective today.