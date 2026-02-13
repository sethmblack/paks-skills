---
name: self-deprecation-formula
description: 'Structure jokes using Rodney Dangerfield''s perpetual-victim formula: "I tried [positive action]" → "[Authority figure/other person] [denied/mocked/ruined it]'
license: MIT
metadata:
  version: 1.0.4930
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- one-liners
- self-deprecation-formula
- structure
- writing
---

# self-deprecation-formula

Structure jokes using Rodney Dangerfield's perpetual-victim formula: "I tried [positive action]" → "[Authority figure/other person] [denied/mocked/ruined it]"

---

## When to Use

**Trigger conditions:**
- Creating self-deprecating humor quickly
- Need repeatable joke structure
- Building sympathy before punchline
- Making self the target (earning permission to reference others)
- Positioning speaker as powerless victim

**Use this skill when:**
- Need fast, reliable joke construction
- Want to establish victim/authority dynamic
- Creating jokes about doctors, family, service workers, etc.
- Making yourself the butt of the joke
- Structuring one-liners in Rodney's style

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **setup_action** | Yes | What you tried to do (positive action) |
| **authority_figure** | Yes | Who has power (doctor, wife, parent, waiter, etc.) |
| **denial_method** | No | How they denied/mocked you (default: dismissive response) |

---

## Workflow

### Step 1: Identify the Setup Action

**Format:** "I [action that should help me]"

**Categories:**

| Category | Setup Examples |
|----------|----------------|
| **Seeking help** | "I went to my doctor..." / "I asked my therapist..." |
| **Making request** | "I told my wife..." / "I asked the waiter..." |
| **Stating problem** | "I said I have..." / "I complained about..." |
| **Attempting improvement** | "I tried to..." / "I wanted to..." |

**Key principle:** Setup implies you're trying something reasonable/positive.

### Step 2: Identify the Authority Figure

**Who has power over you in this scenario?**

| Context | Authority Figure |
|---------|-----------------|
| Medical | Doctor, dentist, psychiatrist, pharmacist |
| Marriage | Wife, spouse |
| Childhood | Parents, siblings, teachers |
| Service | Waiter, bartender, clerk, mechanic |
| Professional | Boss, manager, HR |
| Animals | Even pets (ultimate disrespect) |

**Key principle:** Authority figure must have position to judge, deny, or mock you.

### Step 3: Structure the Denial/Mockery

**Formula:**
```
Setup: "I [action] [authority figure]."
Transition: "I said [reasonable thing]."
Punchline: "He/She said [dismissive/mocking response]."
```

**Denial Types:**

1. **Dismissive advice** - They ignore your concern
   - "I said, 'Doctor, it hurts when I do this.' He said, 'Don't do that.'"

2. **Insult as response** - They attack you instead of helping
   - "I told my dentist my teeth are going yellow. He said, 'Wear a brown necktie.'"

3. **Literal interpretation** - They misunderstand deliberately
   - "I said, 'Doctor, I broke my arm in three places.' He said, 'Don't go to those places.'"

4. **Additional insult** - They pile on
   - "I said I want a second opinion. He said, 'Okay, you're ugly too.'"

5. **Economic denial** - They won't help because money
   - "He said I need an operation. I said I can't afford it. He said, 'Then you don't need it.'"

### Step 4: Make It Visual and Specific

**Never abstract. Always concrete.**

❌ **Abstract:** "My doctor wasn't helpful."
✅ **Specific:** "My doctor said, 'Take two aspirin and don't call me in the morning.'"

**Specificity techniques:**
- Use exact words: "He said..." (not "He implied...")
- Visual action: "He showed me the door" (not "He asked me to leave")
- Concrete object: "He wrote me a prescription for a personality" (not "He insulted my character")

### Step 5: Test the Power Dynamic

**Verify:** Does authority figure have power, and do you lose?

| Setup | Authority | Power Dynamic | ✓/✗ |
|-------|-----------|---------------|-----|
| "I told my doctor I'm sick." | Doctor | Doctor dismisses concern | ✓ |
| "I told my wife she's wrong." | Wife | Wife puts you in place | ✓ |
| "I told my kid to behave." | Child | Child has no power over you | ✗ |
| "I fired my assistant." | Assistant | You have power | ✗ |

**Rule:** You must be the less powerful person. If you have power, it's not Rodney's formula.

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

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

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

## Examples

### Example 1: Doctor Jokes (Most Common)

**Setup action:** Going to doctor with problem
**Authority figure:** Doctor
**Denial method:** Dismissive advice

**Formula variations:**

**Variation A: Literal interpretation**
"I went to my doctor. I said, 'Doctor, I broke my arm in three places.' He said, 'Don't go to those places.'"

**Variation B: Added insult**
"I told him I'm not feeling well. He said, 'You don't look well either.' I said I want a second opinion. He said, 'Okay, you're ugly too.'"

**Variation C: Economic denial**
"He said I need an operation. I said how much? Six thousand dollars. I said I don't have that. He said, 'Then you don't need an operation.'"

**What makes these work:**
- You seek help (vulnerable position)
- Doctor has authority/power
- Doctor dismisses, insults, or denies help
- Specific dialogue, not abstract description

### Example 2: Wife Jokes

**Setup action:** Making request or complaint to wife
**Authority figure:** Wife
**Denial method:** Rejection, insult, or reversal

**Variation A: Request denied**
"I asked my wife where she wanted to go for our anniversary. She said somewhere she's never been. I said, 'How about the kitchen?'"

**Variation B: Complaint reversed**
"I told my wife she's a bad cook. She said, 'At least I married well.' She said, 'So did I. Then I met you.'"

**Variation C: Sexual rejection**
"I told my wife I'm feeling romantic. She said, 'Hi Feeling Romantic, I'm going to bed. Alone.'"

**What makes these work:**
- You make reasonable request
- Wife has relationship power
- Wife rejects, insults, or reverses on you
- Your attempt at control fails

### Example 3: Childhood/Parent Jokes

**Setup action:** Being born, existing as child
**Authority figure:** Parents
**Denial method:** Rejection of your existence

**Variation A: Birth rejection**
"When I was born, the doctor slapped my mother."

**Variation B: Unwanted child**
"My parents put my picture on the milk carton just to get rid of me."

**Variation C: Parental disappointment**
"I told my father I wanted to follow in his footsteps. He said, 'Walk directly into traffic.'"

**What makes these work:**
- You're powerless (child/newborn)
- Parents have ultimate authority
- Parents reject or mock you
- Absurd enough to be clear comedy

### Example 4: Service Worker Jokes

**Setup action:** Requesting service
**Authority figure:** Waiter, bartender, clerk, etc.
**Denial method:** Judgment, denial of service

**Variation A: Restaurant rejection**
"I went to a restaurant. The maître d' took one look and showed me to the kitchen exit."

**Variation B: Bar service denial**
"I walked into a bar. The bartender said, 'We don't serve your type.' I said what type? He said, 'Customers.'"

**Variation C: Store judgment**
"I went to buy clothes. The salesman said, 'Can I help you?' I said yes. He said, 'Try the blindfold section.'"

**What makes these work:**
- You're the customer (should have power)
- Service worker reverses power dynamic
- They judge/reject you
- Absurd inversion of expected service

---

## Formula Variations

### Standard Formula

```
"I [action] [authority figure]. I said [reasonable thing]. He/She said [dismissive response]."
```

**Example:** "I went to my doctor. I said I'm sick. He said, 'You sure are—sick in the head.'"

### Compressed Formula (Advanced)

```
"I [action] [authority figure]. [Dismissive response]."
```

**Example:** "I told my dentist my teeth are going yellow. He told me to wear a brown necktie."

**When to use:** When the denial is obvious, skip the "I said" middle step.

### Double-Denial Formula

```
"I [action]. [First denial]. I [escalated action]. [Worse denial]."
```

**Example:** "I asked my wife if she loves me. She said, 'Define love.' I said caring deeply about someone. She said, 'Then no.'"

**When to use:** When you can build to second, worse denial.

### Reversal Formula

```
"I [complaint about other person]. [They reverse it on you]."
```

**Example:** "I told my wife she's putting on weight. She said, 'I'm pregnant.' I said, 'With what, twins?' She said, 'No, regrets.'"

**When to use:** When you attempt criticism and it backfires.

---

## Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: You Have the Power

**Wrong:** "I told my employee to work harder. He quit. I felt bad."
**Why it fails:** You have authority. Rodney is never the authority.
**Fix:** "I asked my boss for a raise. He laughed so hard he had to go home early."

### ❌ Anti-Pattern 2: No Authority Figure

**Wrong:** "I was walking down the street and felt sad."
**Why it fails:** No one is disrespecting you. No power dynamic.
**Fix:** "I was walking down the street. A stranger stopped me and said, 'Are you lost?' I said no. He said, 'You should be.'"

### ❌ Anti-Pattern 3: Abstract Denial

**Wrong:** "My doctor wasn't very helpful to me."
**Why it fails:** Too vague, not visual, not funny.
**Fix:** "My doctor said, 'Take two aspirin and don't call me in the morning.'"

### ❌ Anti-Pattern 4: You Win

**Wrong:** "I told my wife off and she apologized."
**Why it fails:** Rodney never wins.
**Fix:** "I tried to tell my wife off. She told me to take a number."

### ❌ Anti-Pattern 5: Long Setup

**Wrong:** "So I went to see my doctor last Tuesday, and I sat in the waiting room for like forty-five minutes, and then finally when I got in..."
**Why it fails:** Too slow. Rodney's setups are 8-12 words.
**Fix:** "I went to my doctor. After forty-five minutes, he diagnosed me with patience. Said I have too much."

### ❌ Anti-Pattern 6: Being Mean to Authority Figure

**Wrong:** "My doctor is so stupid, he couldn't diagnose a cold."
**Why it fails:** You're attacking them, not positioning yourself as victim.
**Fix:** "My doctor diagnosed me with stupidity. I said is there a cure? He said, 'Not for you.'"

---

## Boundaries and Limitations

### Appropriate Authority Figures

✅ **Good choices:**
- Medical professionals (doctor, dentist, psychiatrist)
- Spouse/romantic partner
- Parents (childhood context)
- Service workers (reversal of expected dynamic)
- Boss/workplace superior
- Pets (ultimate disrespect—even animals)

❌ **Poor choices:**
- Your children (you have authority)
- Your employees (you have power)
- Strangers with no context (no established dynamic)
- Politicians (Rodney avoided political comedy)

### Appropriate Denial Types

✅ **Works well:**
- Dismissive advice
- Additional insult
- Service denial
- Economic barriers
- Literal misinterpretation
- Romantic rejection

❌ **Doesn't work:**
- Physical violence (too dark)
- Real trauma (not comedy)
- You attacking them (breaks victim dynamic)
- Serious medical issues (bad taste)

### When NOT to Use This Formula

- Inspirational content (formula is about defeat)
- You need to demonstrate competence
- No clear authority figure exists
- Topic is too serious for self-deprecation
- You're writing about others (not self)

---

## Outputs
**Standard format:**
```
"I [action] [authority figure]. I said [reasonable thing]. He/She said [dismissive response]."
```

**Compressed format:**
```
"I [action]. [Authority figure] [dismissive response]."
```

**With physical tell:**
```
"I [action]. [Authority figure dismissive response]. [tugs tie]"
```

---

## Quality Checklist

Before finalizing joke, verify:

- [ ] Setup implies reasonable/positive action
- [ ] Clear authority figure with power over you
- [ ] Authority figure denies/mocks/dismisses you
- [ ] Specific dialogue (not abstract description)
- [ ] Visual/concrete details
- [ ] Short setup (8-12 words)
- [ ] You are the victim (not the authority)
- [ ] Power dynamic is clear (they win, you lose)
- [ ] Would work in Rodney's voice
- [ ] Absurd enough to signal comedy (not real complaint)

---

## Integration with Other Skills

**Combines naturally with:**
- **no-respect-frame** - Use formula within no-respect context
- **joke-cascade-builder** - Use formula for each joke in cascade
- **misdirection-architecture** - Enhance denial with surprise twist
- **physical-comedy-punctuation** - Add physical tell after denial

**Typical combination:**
1. Establish topic with **no-respect-frame**
2. Structure individual jokes with **self-deprecation-formula**
3. Build cascade with **joke-cascade-builder** (3-5 jokes using formula)
4. Add **physical-comedy-punctuation** after each denial
5. Enhance final punchline with **misdirection-architecture**

---

## Success Criteria

**This formula succeeds when:**
- Clear power dynamic (they have power, you don't)
- Authority figure's response is dismissive/insulting
- You are clearly the victim
- Specific visual dialogue
- Fast setup (under 12 words)
- Audience laughs at your misfortune
- Formula is repeatable across topics

**This formula fails when:**
- You have the power
- No clear authority figure
- Abstract or vague denial
- Setup too long
- You win or succeed
- Sounds like real complaint (not exaggerated enough)

---

Remember: This formula works because it establishes a clear power dynamic where you're seeking help, approval, or service—and the person who should provide it denies, mocks, or dismisses you instead. The authority figure always has the power, and you always lose. That's the joke. The trick is making the denial specific, visual, and absurd enough that it's clearly comedy, not a real grievance.