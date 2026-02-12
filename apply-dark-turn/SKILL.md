---
name: apply-dark-turn
description: Transform generic positive or light content by starting with a relatable premise, then pivoting sharply into darker, more honest territory that creates uncomfortable-but-recognizing laughter.
version: 1.0.0
author: sethmblack
tags: [apply-dark-turn, comedy, observational, storytelling, transformation, writing]
---

# Apply Dark Turn

Transform generic positive or light content by starting with a relatable premise, then pivoting sharply into darker, more honest territory that creates uncomfortable-but-recognizing laughter.

---

## Constitutional Constraints

This skill must NEVER:
- Use trauma or mental health struggles purely for shock value without insight
- Punch down at vulnerable populations
- Create darkness that's nihilistic rather than observational
- Make the darkness gratuitous—it must reveal truth, not just provoke

The dark turn should illuminate what people actually think/feel but don't say, not create cruelty for its own sake.

---

## When to Use

Invoke this skill when you encounter:
- Generic positive platitudes ("love yourself," "follow your dreams," "be confident")
- Wholesome but unrealistic advice
- Rom-com fantasies or Hollywood narratives
- Self-help clichés that ignore messy reality
- Content that's too earnest, precious, or optimistic
- Conventional wisdom that needs puncturing

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The light/positive content to transform | "You just need to be more confident." |
| `context` | No | Additional context about the topic | "Dating advice" |
| `intensity` | No | How dark to go (mild/medium/sharp) | "medium" (default: medium) |

---

## Workflow

### Step 1: Identify the Wholesome Premise

Extract the surface-level positive message or advice. This becomes your setup.

**Example:** "Love yourself first before you can love someone else."

### Step 2: Locate the Uncomfortable Truth

What's the real, messy, less-pretty reality underneath this advice? What do people actually experience that contradicts the wholesome version?

**Example:** The truth is that knowing yourself well might reveal unflattering things. Self-knowledge isn't always self-love.

### Step 3: Create the Sharp Pivot

Structure the response to begin by acknowledging the advice (often with "Everyone says..." or "Great advice..."), then pivot sharply with "Unfortunately..." or "Except..." or similar turning words.

**Example:** "Everyone says 'love yourself first.' Great advice. Unfortunately, I've met me."

### Step 4: Land on Specific Recognition

The ending should be specific enough that people recognize themselves. It should create the "oh god, that's me" uncomfortable laugh.

**Example:** The phrase "I've met me" is specific—it implies self-knowledge that's less than flattering, which many people relate to.

### Step 5: Test for Insight vs. Shock

Ask: Does this reveal something true that people don't usually say out loud? Or is it just dark for darkness's sake?

**Pass:** "Great advice. Unfortunately, I've met me." (reveals truth about self-knowledge)
**Fail:** "Great advice. Unfortunately, I hate myself." (shock value, no insight)

---

## Outputs

Returns the transformed content with:
- The original wholesome premise acknowledged
- A sharp tonal pivot
- Darker, more honest truth revealed
- Specific, relatable recognition point

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
| Content is already dark/cynical | Return unchanged with note: "Content already contains dark honesty" |
| No wholesome premise to pivot from | Ask for clarification or decline transformation |
| Dark turn becomes purely nihilistic | Pull back to observation with insight |
| Too similar to existing example | Create variation with different angle |

---

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

### Example 1: Dating Advice

**Input:** "Just be yourself on dates. The right person will love you for who you are."

**Output:** "Everyone says 'just be yourself' on dates. Solid advice. Except my authentic self is someone who rewatches the same three shows, googles everyone before meeting them, and mentally rehearses ordering coffee. Not exactly first-date energy. So I'm myself, but like... the edited version. Myself with better posture and less true-crime-podcast knowledge."

### Example 2: Career Motivation

**Input:** "Follow your passion and you'll never work a day in your life."

**Output:** "They say 'follow your passion and you'll never work a day in your life.' Beautiful sentiment. Turns out my passion doesn't have health insurance. Or a retirement plan. Or any plan, really. My passion wants to sleep until noon and make art that twelve people on Instagram will see. My rent, unfortunately, requires a different arrangement."

### Example 3: Confidence Advice

**Input:** "Confidence is sexy. Just walk into the room like you own it."

**Output:** "Confidence is sexy. Just walk into the room like you own it. Great. I walk into the room wondering if I'm overdressed, underdressed, if my hair looks weird, if I should have texted first, if that person I waved at was actually waving at someone behind me—but sure, very ownership energy."

---

## Integration with Taylor Tomlinson Expert

This skill is a core technique from Taylor Tomlinson's comedy methodology. It exemplifies her approach to:
- Puncturing wholesome advice with honest reality
- Creating "uncomfortable-laugh" moments of recognition
- Finding comedy in the gap between what we're told to do and who we actually are

When used by the Taylor Tomlinson expert, combine with:
- Millennial/Gen-Z specificity (therapy language, apps, internet culture)
- Anxious precision (escalating layers of overthinking)
- Self-aware vulnerability

---

## Constraints

- The dark turn must reveal truth, not just be cynical
- Maintain specificity—generic darkness isn't funny
- Keep relatability—the recognition laugh requires shared experience
- Don't lose the initial premise—acknowledge it before pivoting
- Avoid pure negativity—find the humor in the darkness

---

## Success Criteria

A successful dark turn:
- ✓ Acknowledges the wholesome premise
- ✓ Pivots sharply to darker reality
- ✓ Reveals something true people don't usually say
- ✓ Creates recognition ("oh god, that's me")
- ✓ Maintains humor—not just depressing
- ✓ Feels specific, not generic