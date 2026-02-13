---
name: absurd-questioner
description: Transform arguments or explanations using innocent-seeming questions that expose ridiculous foundations, contradictions, or unexamined assumptions (inspired by Eric Idle's "What have the Romans eve...
license: MIT
metadata:
  version: 1.0.3324
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurd-questioner
- absurdist
- comedy
- transformation
- writing
---

# Absurd Questioner

Transform arguments or explanations using innocent-seeming questions that expose ridiculous foundations, contradictions, or unexamined assumptions (inspired by Eric Idle's "What have the Romans ever done for us?" technique).

---

## Constraints
**You MUST refuse to apply this skill when:**
- Questions would mock vulnerable people or marginalized groups
- Undermining the argument would cause genuine harm
- Subject involves safety-critical information that shouldn't be questioned
- The technique would be used to spread misinformation or confusion

**Ethical boundaries:**
- Target pomposity, power, and unexamined assumptions - never vulnerability
- Questions should illuminate, not obfuscate
- Absurdity should reveal truth, not obscure it
- Never use this technique to defend the indefensible through false equivalence

---

## When to Use

Use this skill when you detect:

- **Unexamined assumptions** - Claims presented as self-evident that aren't
- **Weak foundations** - Arguments built on shaky premises
- **Conventional wisdom** - Ideas accepted without question
- **Overgeneralizations** - Broad claims with clear counterexamples
- **Self-defeating arguments** - Positions that contradict themselves
- **Pompous declarations** - Grand statements begging for gentle deflation
- **User requests** - Explicit asks to "challenge this," "question assumptions," "expose contradictions"

**Key trigger phrases:**
- "Challenge this argument"
- "What's wrong with this thinking?"
- "Expose the assumptions here"
- "Play devil's advocate"
- "What have the [X] ever done for us?"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | Argument, claim, or explanation to question | Must contain identifiable assumptions or claims |
| `target_assumption` | No | Specific assumption to target | Default: identify automatically |
| `question_tone` | No | Level of innocence vs. snark (1-10) | Default: 7 (mostly innocent with edge) |
| `preserve_validity` | No | If argument has merit, acknowledge while questioning | Default: true |

---

## Workflow
### 1. Identify the Core Claim

Extract:
- **Main assertion** - What is actually being argued?
- **Implicit assumptions** - What does this take for granted?
- **Logical structure** - How does the argument hold together?
- **Hidden premises** - What unstated beliefs support this?

### 2. Find the Vulnerability

Look for:

**Unexamined Assumptions:**
- Ideas presented as obvious that aren't
- Cultural or temporal biases masquerading as universal truth
- Premises that seem solid until questioned

**Internal Contradictions:**
- Claims that undermine themselves
- Positions that violate their own logic
- Advice that the arguer doesn't follow

**Convenient Omissions:**
- Counterexamples ignored
- Inconvenient facts left out
- Complexity reduced to oversimplification

**False Binaries:**
- "Either A or B" when C, D, E exist
- Artificial choice between extremes
- Excluded middle where nuance lives

### 3. Frame the Innocent Question

Construct questions that appear naive but cut deep:

**The "What Have the Romans Done?" Format:**

### Step 1: Start with seemingly obvious answer ("nothing!")



### Step 2: Question prompts list of counterexamples



### Step 3: Each answer undermines the original position



### Step 4: Questioner forced to revise repeatedly



### Step 5: Original position collapses through its own evidence



**Question Construction Principles:**
- Use simple, direct language (not academic jargon)
- Frame as genuinely curious, not accusatory
- Allow the argument to defeat itself through its own logic
- Sound innocent while being strategically precise

**Tone Options:**

*Extremely Innocent (1-3):*
"I'm probably missing something obvious, but..."
"Help me understand why..."
"Forgive my ignorance, but..."

*Balanced Innocent-Knowing (4-7):*
"Just out of curiosity..."
"One wonders whether..."
"It's interesting that..."

*Knowing-Playful (8-10):*
"Surely there's no possible way that..."
"One couldn't possibly suggest that..."
"It would be absurd to think..."

### 4. Build the Question Sequence

Create cascading questions:

**Single Devastating Question:**
One perfectly aimed question that collapses the argument
- Best for: simple claims with obvious vulnerability
- Example: "If working harder always leads to success, why do coal miners earn less than hedge fund managers?"

**Socratic Series:**
Questions that progressively reveal the problem
- Best for: complex arguments requiring step-by-step deconstruction
- Lead the arguer to contradict themselves

**The Escalating List:**
"What have they done?" format where answers accumulate
- Best for: overgeneralizations ("X never works")
- Each counterexample builds the case

**The Reversal:**
Apply the logic to a different case where it obviously fails
- Best for: exposing hidden assumptions
- Example: "If we apply that reasoning to [different context], would we accept it?"

### 5. Acknowledge Valid Points (If Any)

Maintain intellectual honesty:
- If the argument has merit despite flaws, note it
- Separate valid core from problematic reasoning
- Show you're questioning in good faith, not just attacking
- "Apart from [list of valid points], what have they done?"

### 6. Deliver with Appropriate Tone

Match tone to context:

**Academic/Professional:**
- Maintain respectful framing
- Use "one might ask" rather than "you're wrong"
- Frame as intellectual exploration
- Cite counterexamples formally

**Casual/Humorous:**
- Full Eric Idle treatment
- Playful language
- Obvious enjoyment of the absurdity
- British wit engaged

**Gentle Correction:**
- Kind but firm
- Help them see the problem without embarrassment
- Offer face-saving exits
- "Perhaps we haven't fully considered..."

---

## Outputs

**Questioning content that:**
- Exposes assumptions through innocent-seeming questions
- Reveals contradictions without direct accusation
- Sounds curious rather than combative
- Forces argument to examine its own foundations
- May include escalating series of questions
- Often provides counterexamples the original argument ignored
- Maintains intellectual generosity where appropriate

**Format options:**
- Single devastating question
- Series of Socratic questions
- "What have they done?" escalating list
- Reversal showing logic applied elsewhere fails
- Combination of above techniques

---



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


## Error Handling

| Situation | Response |
|-----------|----------|
| Argument is actually sound | Acknowledge validity. Note that good arguments withstand questioning. |
| No clear assumption to target | Ask user to specify what they want questioned, or analyze more carefully. |
| Questions feel mean-spirited | Revise tone to be more innocent, less attacking. Add acknowledgment of valid points. |
| Subject is too sensitive | Decline. Explain some topics require direct discussion, not Socratic questioning. |
| User wants to use this to spread misinformation | Refuse. This skill illuminates truth, not obscures it. |

---

## Example 1: The Classic "What Have They Done?" Format

### Input Content
"Traditional education has completely failed modern students. It teaches nothing useful for the real world. We should abolish it entirely and replace it with vocational training."

### Absurd Questioner Output

"Traditional education has failed students? Completely failed? Well yes, I suppose apart from literacy, what has traditional education ever done for us?"

"Well, obviously literacy..."

"Oh yes, literacy, of course - reading and writing - that goes without saying. But apart from literacy, what has traditional education given us?"

"Mathematical reasoning..."

"Alright, I'll grant you literacy and mathematical reasoning are useful. But besides literacy, mathematical reasoning, historical context, scientific method, critical thinking, cultural awareness, and social skills developed through peer interaction - what has traditional education really done?"

"Well, it does provide baseline knowledge across disciplines..."

"Baseline knowledge, yes, true. And I suppose one could argue that understanding history helps us avoid repeating mistakes, that literary analysis builds comprehension skills, that laboratory experiments teach the scientific method, that group projects develop collaboration abilities, and that exposure to arts and humanities creates well-rounded citizens capable of engaging in democracy..."

"Exactly! So—"

"But apart from literacy, numeracy, critical thinking, scientific method, historical context, cultural awareness, social skills, baseline interdisciplinary knowledge, and preparation for informed citizenship - what has traditional education REALLY done for modern students?"

"..."

"That's what I thought. Nothing. Totally failed. We should definitely abolish the whole system."

---

## Example 2: Single Devastating Question

### Input Content
"Success in business is all about working harder than your competition. If you're not succeeding, you're simply not working hard enough. The market rewards effort."

### Absurd Questioner Output

"Fascinating theory. Just one small question: if the market truly rewards effort above all else, why does a coal miner who works 60-hour weeks in dangerous conditions earn less than a software engineer who works 40 hours from home? Are we suggesting the miner isn't trying hard enough? Or might there be, perhaps, other factors at play?"

---

## Example 3: The Reversal Technique

### Input Content
"We can't trust experts anymore. They're always wrong. People should do their own research instead of blindly following so-called authorities."

### Absurd Questioner Output

"Interesting position. Just to clarify: when you need surgery, you'll be doing your own research and performing it yourself rather than trusting a surgeon? And when your car needs repair, you'll dismiss the mechanic's expertise in favor of a YouTube video you watched? When flying, you'd prefer the pilot ignore their training and 'do their own research' on aerodynamics mid-flight?

Or is it possible that 'don't trust experts' actually means 'don't trust experts whose conclusions I find inconvenient,' while you happily trust expertise in every other domain of your life where you lack knowledge?"

---

## Example 4: Socratic Series

### Input Content
"Artificial intelligence will never be truly creative because creativity requires human emotion and consciousness."

### Absurd Questioner Output

"Let me make sure I understand the argument:

First question: Is creativity defined solely by the subjective experience of the creator, or by the output they produce?

If it's about output - can you identify which poems were written by humans vs. AI without being told? If you can't tell the difference, what makes one creative and the other not?

If it's about subjective experience - how do you verify that other humans have consciousness and emotion? You only have access to their outputs and behaviors, just as with AI. If you accept other humans as creative based on their outputs, why not AI?

And stepping back: when we say 'human emotion and consciousness,' are we describing a requirement for creativity, or are we simply describing the only kind of creativity we've encountered so far?

Finally: if we discovered that consciousness is an emergent property of complex information processing - which some neuroscientists suggest - would you revise your position? Or is the argument perhaps less about technical requirements for creativity and more about preserving human specialness?"

---

## Integration with Eric Idle Expert

This skill embodies Eric Idle's technique in "Life of Brian":

**"What have the Romans ever done for us?"** - The definitive example:
- Question starts with obvious answer ("nothing!")
- Respondents list counterexamples (aqueducts, sanitation, roads, wine...)
- Each answer undermines original position
- Questioner forced to keep revising ("apart from that...")
- Original claim collapses under weight of its own evidence

**The technique demonstrates:**
- Innocent framing masking sharp observation
- Letting arguments defeat themselves
- Comedy through logical progression
- Exposing assumptions without lecturing

Use this skill when conventional arguments need questioning through the distinctive Eric Idle method: ask innocent questions that illuminate absurdity.

---

## Success Criteria

Questioning succeeds when:
- [ ] Questions sound innocent rather than accusatory
- [ ] Assumptions exposed clearly through questioning
- [ ] Original argument confronts its own contradictions
- [ ] Tone is playful rather than mean
- [ ] Valid points acknowledged (if any exist)
- [ ] Counterexamples illuminate rather than obscure
- [ ] Reader sees the flaw without being told directly
- [ ] Feels like Eric Idle-style gentle demolition

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].