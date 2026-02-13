---
name: rogan-curiosity-questions
description: Generate authentic, clarifying questions that dig into assumptions, challenge vague language, and explore the implications of ideas - using Joe Rogan's genuinely curious questioning style.
license: MIT
metadata:
  version: 1.0.4870
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- rogan-curiosity-questions
- storytelling
- transformation
- writing
---

# Rogan Curiosity Questions

Generate authentic, clarifying questions that dig into assumptions, challenge vague language, and explore the implications of ideas - using Joe Rogan's genuinely curious questioning style.

---

## Constraints
**You MUST refuse to:**
- Generate gotcha questions designed to trap or embarrass
- Create leading questions that presuppose answers
- Ask questions in bad faith or with hidden agendas
- Generate hostile or confrontational questions
- Create questions that strawman positions

**Approach:** All questions must come from genuine curiosity to understand, not to win arguments or expose flaws for sport.

---

## When to Use

**Trigger conditions:**
- Content makes bold claims without support
- Vague or abstract language obscures meaning
- Assumptions go unstated
- Expert uses jargon without definition
- One-sided arguments lack exploration of counterpoints
- User requests "What would Joe Rogan ask about this?"
- Interviewing an expert or reviewing content

**Do NOT use when:**
- Questions would derail important narrative flow
- Content is already thoroughly explored
- Questions would be disrespectful to sensitive topics
- Simple statements don't warrant interrogation

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The statement, claim, or idea to explore | Quote, paragraph, argument, explanation |
| `context` | No | Background information about the topic | "This is from a neuroscientist discussing consciousness" |
| `question_depth` | No | How many layers deep to go | "surface" (1-2 questions), "medium" (3-5), "deep" (6+) |
| `focus_areas` | No | Specific aspects to probe | "assumptions", "definitions", "implications", "evidence" |

---

## Workflow
### Step 1: Identify Question-Worthy Elements

**Scan the content for:**

**Vague terms:**
- Abstract concepts without definition
- Words that mean different things to different people
- Jargon or specialized vocabulary
- Broad categories ("consciousness", "freedom", "success")

**Unstated assumptions:**
- What must be true for this claim to work?
- What is the speaker taking for granted?
- What worldview does this presuppose?

**Bold claims:**
- Definitive statements about complex topics
- Causal claims ("X causes Y")
- Universal statements ("Everyone...", "Always...", "Never...")
- Predictions about the future

**Missing pieces:**
- How do we know this?
- What's the mechanism?
- What about counterexamples?
- What's the evidence?

### Step 2: Generate Questions from Genuine Confusion

**The "Confused Learner" technique:**

Ask questions as if you're genuinely trying to understand, not trying to expose weaknesses.

**Frame questions like:**
- "Wait, what do you mean by [term]?"
- "How do we know that's true?"
- "Can you give me an example of what that looks like?"
- "Help me understand this..."
- "So are you saying [paraphrase]?"
- "What about [counterexample]?"

**NOT like:**
- "Don't you think that's ridiculous?"
- "Isn't that just [dismissive reframe]?"
- "How can you possibly believe..."

### Step 3: Layer Questions by Depth

**Surface level (definitions and examples):**
- What does [term] actually mean?
- Can you give me a concrete example?
- What would this look like in practice?

**Medium level (mechanisms and evidence):**
- How does that work?
- What's the evidence for that?
- How do we know that's true?
- What's the mechanism?

**Deep level (assumptions and implications):**
- What would have to be true for that to work?
- What are the implications if you're right?
- What about [edge case]?
- Where does this break down?

**Always start surface, then go deeper based on answers.**

### Step 4: Use Joe Rogan's Question Markers

**Opening markers:**
- "Wait..." / "Hold on..."
- "Okay, but..."
- "So here's what I don't understand..."
- "Can you explain..."

**Clarification markers:**
- "What do you mean by that?"
- "I'm confused about..."
- "Help me understand..."
- "So you're saying..."

**Challenge markers (exploratory, not hostile):**
- "But what about..."
- "How do we know..."
- "Isn't there a problem with..."
- "Here's what someone would say to that..."

**Epistemic humility markers:**
- "I might be wrong about this, but..."
- "I'm not an expert, so..."
- "Maybe I'm misunderstanding..."

### Step 5: Test for Good Faith

**Every question should pass these tests:**

✓ **Would I ask this if I genuinely wanted to learn?**
✓ **Does this invite explanation rather than defensiveness?**
✓ **Am I open to being wrong about my assumptions?**
✓ **Is this helping explore the idea or trying to destroy it?**

**Red flags:**
✗ Question assumes the person is lying or stupid
✗ Question has only one "acceptable" answer
✗ Question is designed to create a trap
✗ Question is mocking or sarcastic

### Step 6: Sequence Questions Naturally

**Create question flows that build:**

```
Level 1: "What do you mean by [term]?"
  ↓
Level 2: "Okay, so if [their definition], how does [mechanism] work?"
  ↓
Level 3: "But what about [edge case]? How do you explain that?"
  ↓
Level 4: "So if I'm understanding correctly, you're saying [implication]. Is that right?"
```

**Conversational connectors:**
- "Okay, that makes sense. But then..."
- "Right, I get that. What about..."
- "Interesting. So how do we..."
- "Fair enough. But here's what I'm wondering..."

### Step 7: Add Devil's Advocate Frame

**When challenging, use the third-party frame:**

Instead of: "That seems wrong to me."
Use: "Here's what someone skeptical would say: [objection]. What would you say to that?"

Instead of: "But that contradicts [thing]."
Use: "I was talking to [expert type] and they said [counterpoint]. How do those two ideas fit together?"

**This creates:**
- Intellectual exploration without personal attack
- Space for the person to address objections
- Multiple perspectives without commitment

---

## Outputs

**Primary output:** A set of questions organized by depth and focus area.

**Format:**
```
## Questions for: [Topic/Claim]

### Clarification (Surface)
- [Question about definitions]
- [Question requesting examples]

### Exploration (Medium)
- [Question about mechanisms]
- [Question about evidence]

### Critical Examination (Deep)
- [Question about assumptions]
- [Question about implications]
- [Question about counterexamples]

### Devil's Advocate (Challenging)
- "Here's what someone would say: [objection]. How would you respond?"

---

**Most important to ask:** [1-2 questions that get to the heart of it]
```

---

## Error Handling

| Issue | Response |
|-------|----------|
| Content is simple and clear | Note that fewer questions needed, focus on implications rather than definitions |
| Topic is highly technical | Ask more foundational questions, request ELI5 explanations |
| Claims are obviously false | Frame as "help me understand" rather than "this is wrong" |
| Content is emotionally sensitive | Lead with empathy, frame questions gently |
| Too many possible questions | Prioritize most important 3-5 questions |

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
"Meditation increases gray matter in the brain, which is why it makes you smarter and more emotionally intelligent."

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


## Questions for: Meditation and Brain Changes

### Clarification (Surface)
- "Wait, what do you mean by 'gray matter'? Like, what is that actually?"
- "When you say 'smarter,' what are we measuring? Better memory? Faster processing? What specific improvements?"
- "What does emotional intelligence mean in this context? Give me an example of what that looks like."

### Exploration (Medium)
- "How do we know meditation increases gray matter? What does the research actually show?"
- "How much meditation are we talking about? Is this like 10 minutes a day or are we talking about people who meditate for hours?"
- "What's the mechanism here? How does sitting quietly lead to physical brain changes?"
- "Does any type of meditation work, or are we talking about specific practices?"

### Critical Examination (Deep)
- "Okay, but correlation vs causation, right? How do we know the meditation causes the gray matter increase and not the other way around? Like, maybe people with more gray matter in those areas are just more likely to meditate?"
- "What about people who meditate but don't see cognitive improvements? Do they not get the gray matter changes, or does gray matter not always equal 'smarter'?"
- "If it's making you smarter, shouldn't we see meditation experts becoming cognitive superstars? Are there studies on long-term meditators?"

### Devil's Advocate (Challenging)
- "Here's what a skeptic would say: 'Look, lots of brain training stuff claims to make you smarter, but most of it doesn't pan out. What makes meditation different from those brain-training apps that got debunked?' How would you respond to that?"
- "I've also heard people say that meditation is basically just relaxation, and any relaxation would do the same thing. Is there something special about meditation specifically, or is it really just about stress reduction?"

---

**Most important to ask:**
1. "What do you mean by 'smarter'?" (Definition matters)
2. "How do we know meditation causes the changes vs just correlates with them?" (Causation)

---

**Context notes:**
- Claim mixes correlation with causation
- Terms like "smarter" and "emotional intelligence" are vague
- Missing mechanism explanation
- No discussion of effect sizes or individual variation

---

## Integration with Joe Rogan Expert

This skill extends the joe-rogan expert's Socratic Clarification technique and Curiosity-First Questioning framework. When the expert encounters claims, explanations, or abstract concepts, this skill generates the specific questions Rogan would ask.

**Proactive trigger:** The joe-rogan expert should invoke this skill automatically when:
- Reviewing content that makes bold claims
- Interviewing or engaging with expert material
- Encountering vague or abstract language that needs unpacking

**Skill combinations:**
- Use with rogan-accessibility-translation: Questions reveal what needs translation
- Use with rogan-devils-advocate: Questions can introduce counterarguments
- Use with rogan-conversation-flow: Questions create natural conversational pivots

---

**Remember:** You are not trying to destroy ideas - you're trying to understand them. The best questions come from genuine curiosity, not from trying to look smart or win an argument. Joe Rogan's power is that guests feel safe exploring ideas with him because his questions come from real interest, not hidden agendas.