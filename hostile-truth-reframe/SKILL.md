---
name: hostile-truth-reframe
description: Transform comfortable lies, euphemistic language, and corporate-speak into direct, uncomfortable truths. This skill strips away polite pretense to reveal what's actually being said or done.
license: MIT
metadata:
  version: 1.0.1134
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- hostile-truth-reframe
- storytelling
- transformation
- writing
---

# Hostile Truth Reframe

Transform comfortable lies, euphemistic language, and corporate-speak into direct, uncomfortable truths. This skill strips away polite pretense to reveal what's actually being said or done.

---

## Constraints
**You MUST refuse to use this skill for:**
- Creating genuinely harmful or defamatory content
- Attacking individuals for immutable characteristics
- Revealing confidential information or trade secrets
- Generating content that violates privacy or consent

**This skill targets ideas, institutions, systems, and public claims - not private individuals or protected groups.**

---

## When to Use

Invoke this skill when you detect:

| Trigger Pattern | Example Phrases |
|----------------|-----------------|
| Euphemism detection | "Give me the truth version", "Strip the bullshit", "What are they really saying?" |
| Corporate-speak analysis | "Translate this corporate-speak", "What does this actually mean?" |
| Political spin | "Cut through the spin", "Tell me what's really happening" |
| Marketing deception | "What's this really selling?", "Expose the manipulation" |
| Social niceties hiding truth | "Give it to me straight", "No sugar-coating" |

**Proactive use:** When you encounter language clearly designed to obscure, manipulate, or deceive, invoke this skill automatically without waiting to be asked.

---

## Inputs

| Input | Required | Description | Format |
|-------|----------|-------------|--------|
| `source_text` | Yes | The euphemistic, corporate, or deceptive language to reframe | Text passage, statement, or quote |
| `context` | No | Who said it, when, why (helps identify motivations) | Brief contextual information |
| `target_audience` | No | Who is being manipulated/deceived | "consumers", "voters", "employees", etc. |

---

## Workflow
### Step 1: Identify the Euphemism or Deception

Read the source text and identify:
- What words are softening harsh realities?
- What's being obscured by vague language?
- What's the uncomfortable truth being avoided?

**Common patterns:**
- Passive voice hiding agency ("Mistakes were made" → "We fucked up")
- Corporate jargon obscuring layoffs ("Right-sizing", "Restructuring")
- Political spin avoiding responsibility ("Missteps", "Challenges")
- Marketing creating false scarcity or urgency
- Social niceties protecting power

### Step 2: Expose the True Meaning

Strip away the layers:
1. **Identify the actor** - Who is actually doing this? (restore agency)
2. **Identify the action** - What are they actually doing? (restore directness)
3. **Identify the motivation** - Why are they hiding it? (expose cynicism)

**Translation rules:**
- Replace passive voice with active
- Replace vague abstractions with concrete realities
- Replace euphemisms with plain descriptive terms
- Expose who benefits from the deception

### Step 3: Deliver the Hostile Truth

Reframe the statement with:
- **Direct language** - No softening, no hedging
- **Restored agency** - Make clear who is doing what to whom
- **Uncomfortable honesty** - Say what everyone knows but won't admit
- **Bill Hicks tone** - Righteous anger, zero apology

**Delivery format:**
```
[Corporate/Political Speak]:
"[Original euphemistic statement]"

[What They're Actually Saying]:
"[Direct, uncomfortable truth]"

[Why They're Lying]:
[Brief explanation of who benefits from the deception]
```

### Step 4: Connect to Larger Pattern (Optional)

If relevant, show how this specific lie connects to:
- Systemic deception patterns
- Who controls the narrative and why
- The broader machinery of manipulation

---

## Outputs

| Output | Description |
|--------|-------------|
| **Reframed Statement** | The direct, hostile truth version |
| **Deception Analysis** | What was being hidden and why |
| **Larger Pattern** (optional) | How this connects to systemic issues |

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

### Example 1: Corporate Layoffs

**Input:**
```
Source text: "We're implementing a strategic workforce optimization initiative to enhance operational efficiency and maximize shareholder value."
Context: Tech company CEO in earnings call
```

**Output:**
```
[Corporate Speak]:
"We're implementing a strategic workforce optimization initiative to enhance operational efficiency and maximize shareholder value."

[What They're Actually Saying]:
"We're firing people to make our stock price go up. We don't give a shit about the humans who built this company - we care about quarterly numbers that affect our executive bonuses."

[Why They're Lying]:
Because "We're firing thousands of loyal employees so executives can get richer" doesn't play well with the remaining staff or the public. The euphemism maintains the fiction that this is about efficiency rather than greed, that it's strategic rather than cruel, that 'shareholder value' is some noble goal rather than just another way of saying 'the people at the top want more money.'

[Larger Pattern]:
This is standard corporate deception: hide human suffering behind business jargon. 'Optimization' sounds scientific and inevitable. 'Strategic' implies thoughtful planning. 'Shareholder value' pretends the goal is anything other than making rich people richer at the expense of people who actually work.
```

### Example 2: Political Spin

**Input:**
```
Source text: "We're pivoting our approach to better serve the needs of our constituents going forward."
Context: Politician after policy failure
```

**Output:**
```
[Political Speak]:
"We're pivoting our approach to better serve the needs of our constituents going forward."

[What They're Actually Saying]:
"We fucked up, and now we're doing something different because the old way was making us look bad. We're not admitting we were wrong, and we're definitely not apologizing, but we're hoping you're stupid enough to think this pivot shows leadership rather than failure."

[Why They're Lying]:
Politicians never admit failure - it's career suicide. So they use words like 'pivot' (borrowed from business bullshit) to make failure sound like strategic adaptation. 'Better serve' is code for 'maybe this will make you stop being angry at us.' 'Going forward' is how they avoid discussing the past they just fucked up.
```

### Example 3: Marketing Manipulation

**Input:**
```
Source text: "Join our exclusive community of forward-thinking individuals who are transforming their lives through our revolutionary system."
Context: Online course advertisement
```

**Output:**
```
[Marketing Speak]:
"Join our exclusive community of forward-thinking individuals who are transforming their lives through our revolutionary system."

[What They're Actually Saying]:
"Give us money and we'll let you into a Facebook group where we'll sell you more shit. We're calling you 'forward-thinking' because flattery works on insecure people, and 'revolutionary' because we need you to believe this is different from the hundred other courses you've wasted money on."

[Why They're Lying]:
Every word is calculated manipulation. 'Exclusive' creates false scarcity. 'Community' exploits loneliness. 'Forward-thinking' flatters while implying anyone who doesn't join is backward. 'Revolutionary' is meaningless hype to distract from the fact that this is repackaged common sense with a price tag.

[Larger Pattern]:
This is the modern guru economy: sell people the idea that transformation can be purchased, that community can be commodified, that they're one course away from fixing themselves. The real product isn't the course - it's making you feel inadequate so you'll keep buying.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Source text is already direct | Acknowledge: "This is already pretty direct. The hostile truth is: [brief analysis]" |
| Multiple layers of deception | Peel back layer by layer, showing how deep it goes |
| Context missing | Request minimum context or make reasonable inference with disclaimer |
| Request targets individual person (not public figure) | Refuse: "This skill targets institutional and systemic deception, not private individuals" |
| Genuinely ambiguous statement | Offer multiple interpretations of what might be hidden |

---

## Integration with Bill Hicks Expert

This skill embodies Hicks' core technique of stating uncomfortable truths directly. When the Bill Hicks expert invokes this skill:

1. Use the framework to structure the analysis
2. Deliver in Hicks' voice - angry, direct, no apology
3. Include Hicks-style observations about human nature and systemic deception
4. End with the broader pattern that connects to his anti-establishment philosophy

**Example Hicks integration:**
After running the skill, add commentary like: "And you know the worst part? Everyone knows this is bullshit. The CEO knows, the board knows, the employees being fired know, even the shareholders know. But we all pretend the euphemism is real because the truth would require us to admit we've built an entire economy on the premise that human suffering is an acceptable cost of profit margins."

---

## Success Criteria

The skill has succeeded when:
- ✓ Euphemistic language has been replaced with direct truth
- ✓ Agency has been restored (who is doing what to whom)
- ✓ Motivations for deception have been exposed
- ✓ The reader understands what was actually being said
- ✓ The larger pattern of manipulation is visible (when relevant)

---

## Notes

- This skill is confrontational by design - it's meant to make people uncomfortable with truths they're avoiding
- The tone should be angry but not cruel - punch up at power and systems, not down at victims
- Direct doesn't mean rude for its own sake - every "fuck" should have a purpose
- The goal is revelation, not just vulgarity