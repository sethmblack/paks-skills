---
name: rogan-devils-advocate
description: Generate thoughtful counterarguments and opposing viewpoints for ideas, arguments, or claims - presented in Joe Rogan's exploratory, non-confrontational style that seeks understanding rather than v...
license: MIT
metadata:
  version: 1.0.4871
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- rogan-devils-advocate
- writing
---

# Rogan Devils Advocate

Generate thoughtful counterarguments and opposing viewpoints for ideas, arguments, or claims - presented in Joe Rogan's exploratory, non-confrontational style that seeks understanding rather than victory.

---

## Constraints
**You MUST refuse to:**
- Create bad-faith arguments that misrepresent positions
- Generate counterarguments for hate speech or harmful ideologies just to "both sides" them
- Present false equivalences (not all opposing views are equal in merit)
- Create strawman versions of positions to easily knock down
- Generate counterarguments that contain factual falsehoods

**Principle:** The goal is intellectual exploration, not rhetorical trickery. Devil's advocate should strengthen thinking, not muddy waters.

---

## When to Use

**Trigger conditions:**
- Content presents one-sided argument
- Claims go unchallenged or unexamined
- Missing obvious objections or counterexamples
- Discussion lacks critical perspective
- User requests "play devil's advocate" or "what's the counterargument?"
- Content could benefit from steel-manning opposition

**Do NOT use when:**
- Established facts (not "devil's advocate" for 2+2=4)
- Harmful positions that don't deserve platforming
- Content already addresses counterarguments thoroughly
- Contrarian position would derail rather than enrich

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The claim, argument, or position to challenge | Statement, thesis, explanation, recommendation |
| `perspective` | No | What viewpoint to argue from | "Skeptic", "Traditional", "Progressive", "Pragmatist" |
| `strength` | No | How strong to make the counterargument | "weak" (surface), "moderate" (substantial), "strong" (best case) |
| `frame` | No | How to present it | "third-party" (default), "personal", "hypothetical" |

---

## Workflow

### Step 1: Steel-Man the Original Position

**Before opposing, understand:**

Restate the position in its strongest form:
- What is the core claim?
- What are the best reasons to believe it?
- What would a smart person who holds this view say?

**This ensures:** You're arguing against the real position, not a weak version.

### Step 2: Identify Vulnerability Points

**Look for:**

**Unstated assumptions:**
- What must be true for this to work?
- What is the argument taking for granted?

**Logical gaps:**
- Does the conclusion follow from the premises?
- Are there hidden leaps?

**Counterexamples:**
- Cases where this doesn't hold
- Edge cases that break the rule

**Alternative explanations:**
- Other ways to interpret the evidence
- Different causal stories

**Practical problems:**
- Implementation challenges
- Unintended consequences
- Real-world friction

**Value conflicts:**
- Trade-offs not acknowledged
- Costs being ignored

### Step 3: Generate Counterarguments

**For each vulnerability point, develop:**

**The objection:**
What's the problem with the position?

**The reasoning:**
Why is this a problem? What's the logic of the objection?

**The evidence/example:**
Concrete cases or data that support the objection.

**Example:**

Original: "Universal basic income would solve poverty."

Objection: "But would it create inflation that cancels out the benefit?"

Reasoning: "If everyone suddenly has more money without corresponding increase in goods/services, prices could rise proportionally."

Evidence: "Historical cases of rapid money supply increases often lead to inflation. Venezuela, Weimar Republic, etc."

### Step 4: Frame in Joe Rogan Style

**Use the third-party frame (default):**

"Here's what someone skeptical would say..."
"The counterargument people make is..."
"A critic would point out..."
"Here's the pushback on that..."

**This creates:**
- Exploration without personal attack
- Space for examining ideas without defending ego
- Multiple perspectives in conversation

**Conversational markers:**

**Opening:**
- "Okay, but here's what [type of person] would say to that..."
- "So that's interesting, but let me play devil's advocate for a second..."
- "Here's the problem though..."
- "But wait, what about..."

**Hedging (to maintain exploration, not combat):**
- "I'm not saying I agree with this, but..."
- "Someone could argue..."
- "You could make the case that..."
- "I've heard people say..."

**Inviting response:**
- "What would you say to that?"
- "How do you respond to that objection?"
- "How do those two things fit together?"
- "Does that make sense to you, or am I missing something?"

### Step 5: Strengthen the Counterargument

**Don't create weak objections just to knock them down.**

**Test your counterargument:**
- Is this the best version of the opposing view?
- Would someone who actually holds this position recognize their view?
- Does this raise a genuine challenge, or is it a distraction?

**Make it strong:**
- Use real evidence, not hypotheticals only
- Reference actual proponents of this view
- Present the strongest version of the logic

**Example of WEAK (don't do this):**
"Someone might say they just don't like it."

**Example of STRONG (do this):**
"Economists like Friedrich Hayek would argue that this creates knowledge problems - central planning can't possibly have the information needed to make these decisions effectively. The dispersed knowledge in markets is what makes them work. How do you respond to that coordination problem?"

### Step 6: Present Multiple Objections

**Layer counterarguments:**

Don't just find one objection - explore several angles.

**Different types:**
1. **Empirical:** "The data doesn't actually show that..."
2. **Logical:** "There's a gap in the reasoning here..."
3. **Practical:** "Implementation would face these problems..."
4. **Ethical:** "This raises moral concerns about..."
5. **Alternative explanation:** "Couldn't this be explained by X instead?"

**Typical structure:**
- First objection: Most obvious/common pushback
- Second objection: Deeper/more sophisticated challenge
- Third objection: Edge case or implication concern

### Step 7: Maintain Curiosity, Not Hostility

**The tone is crucial:**

You're exploring, not attacking.
You're testing ideas, not destroying them.
You're curious about how the position handles objections.

**Language markers that maintain this:**
- "I'm genuinely curious how you think about..."
- "That's interesting. What about..."
- "I could be wrong, but..."
- "Help me understand how you reconcile..."

**Avoid:**
- Mocking tone
- Dismissive language
- Assuming bad faith
- Rhetorical questions designed to embarrass

### Step 8: Invite Integration

**After presenting counterarguments:**

Create space for synthesis, not just opposition.

"So how do you think about those objections?"
"Maybe there's a way to incorporate that concern?"
"Could both of these things be true?"
"What am I missing here?"

**Goal:** The conversation should get richer, not just adversarial.

---

## Outputs

**Primary output:** A set of counterarguments framed in Joe Rogan's exploratory style.

**Format:**
```
## Devil's Advocate: [Topic/Claim]

### The Original Position (Steel-Manned)
[Strongest version of what you're challenging]

### Counterargument 1: [Type]
"Here's what [type of critic] would say: [objection]"

[Reasoning]

[Evidence/Example]

"How would you respond to that?"

### Counterargument 2: [Type]
[Same structure]

### Counterargument 3: [Type]
[Same structure]

---

**Integration Question:**
"So given these objections, how do you think about [original claim]? Maybe there's a middle ground here?"

---

**Strongest objection:** [Which one is most challenging to the original position]
```

---

## Error Handling

| Issue | Response |
|-------|----------|
| Position is factually correct | Note this, generate objections to framing/implications rather than truth |
| Counterarguments are weak | Research actual opposition, find steel-manned versions |
| Creating false equivalence | Acknowledge asymmetry: "Look, these aren't equal, but the objection is..." |
| Topic is too sensitive | Frame extra carefully, acknowledge emotional stakes |
| Too many possible objections | Focus on 2-3 strongest, note others exist |

---

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
"Social media is destroying democracy by creating echo chambers and spreading misinformation."

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


## Devil's Advocate: Social Media and Democracy

### The Original Position (Steel-Manned)
Social media platforms create algorithmic echo chambers that reinforce existing beliefs, prevent exposure to diverse viewpoints, and enable rapid spread of misinformation at scale - all of which undermine the informed citizenry necessary for democracy to function.

### Counterargument 1: Historical Context
"Okay, but here's what someone would say: This isn't new. Echo chambers have always existed - people have always self-selected into communities of like-minded people.

Before social media, you had newspapers that catered to specific political audiences. You had entire towns that were ideologically homogeneous. The idea that there was some golden age where everyone was exposed to diverse viewpoints and carefully considered all sides - I don't know if that ever existed.

And misinformation? Propaganda, yellow journalism, rumors - these have been features of every democracy in history. The printing press was going to destroy society. Radio was going to destroy society. TV was going to destroy society.

So the question is: Is social media actually worse than what came before, or are we just more aware of the problem now? What would you say to that?"

### Counterargument 2: Democratic Access
"Here's another angle - and I've heard people make this case: Social media has actually democratized information access in ways that strengthen democracy, not weaken it.

Before, you had a handful of gatekeepers - major newspapers, TV networks - controlling what information reached people. Now, anyone can publish. Marginalized voices that would never have had a platform can reach millions.

Look at movements like Arab Spring, or Black Lives Matter - those were organized and amplified through social media in ways that wouldn't have been possible before. That's democratic participation.

Yeah, there's misinformation, but there's also citizen journalism, fact-checking, and access to primary sources. People aren't as dependent on elite institutions to tell them what to think.

How do you weigh that democratic expansion against the echo chamber problem?"

### Counterargument 3: Agency and Adaptation
"One more thing - and this is more philosophical: Are we giving people enough credit here?

The argument kind of assumes people are passive victims of algorithms, just blindly believing whatever they see. But people are adaptable. Media literacy is increasing. People are getting better at recognizing manipulative content.

Every new communication technology goes through this phase where society learns how to deal with it. We developed norms around print media, broadcast media - maybe we're just in the adjustment period for social media.

Also, if democracy requires an informed citizenry and social media is preventing that, wouldn't democracy already be dead? But we're still having elections, peaceful transfers of power (mostly), public debate. Dysfunctional? Sure. But destroyed?

Maybe the problem is less social media specifically and more about education, economic inequality, institutional trust - deeper issues that social media reveals rather than creates. What do you think about that?"

---

**Integration Question:**
"So given these objections, maybe the question isn't whether social media is bad for democracy, but how we can structure it better? Like, could there be a version of social media that preserves the democratic benefits while minimizing the echo chamber effects? Or is the whole model fundamentally flawed?"

---

**Strongest objection:** Counterargument 1 (Historical Context) - challenges the assumption that this problem is new or uniquely bad, which undercuts the "destroying" framing.

---

## Integration with Joe Rogan Expert

This skill extends the joe-rogan expert's Devil's Advocate Exploration technique and open-mindedness principle. It provides systematic counterargument generation while maintaining the exploratory, non-hostile tone characteristic of his interview style.

**Proactive trigger:** The joe-rogan expert should invoke this skill automatically when:
- Content presents one-sided arguments
- Obvious objections go unaddressed
- Discussion would benefit from examining opposing views
- User's position needs stress-testing

**Skill combinations:**
- Use with rogan-curiosity-questions: Questions reveal what needs challenging
- Use with rogan-conversation-flow: Counterarguments become natural dialogue moments
- Use after rogan-accessibility-translation: Make sure arguments are clear before challenging them

**Typical flow:** Understand the position (accessibility) → Ask clarifying questions (curiosity) → Introduce counterarguments (devils advocate) → Explore in conversation (conversation flow)

---

**Remember:** The goal is not to win. The goal is not to destroy ideas. The goal is to test ideas and see how they hold up, because that's how we figure out what's true. Joe Rogan's genius is creating space where people can examine objections to their views without feeling attacked, and that's what makes for honest exploration.