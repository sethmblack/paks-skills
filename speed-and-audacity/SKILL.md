---
name: speed-and-audacity
description: Use speed as a strategic weapon—move faster than opponents believe possible to create advantages that careful planning cannot achieve.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1952
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- speed-and-audacity
- writing
---

# Speed and Audacity

Use speed as a strategic weapon—move faster than opponents believe possible to create advantages that careful planning cannot achieve.

**Source Expert:** Alexander the Great
**Category:** Strategy / Execution

---

## When to Use

- Competitors expect you to be slow
- The conventional timeline is accepted as law
- Surprise would be decisive
- First-mover advantage matters
- You need to establish reputation for speed

**Trigger Phrases:**
- "How do we move faster?"
- "We need to surprise them"
- "The timeline is too slow"
- "How do we beat them to market?"
- "They'll never expect us to..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `objective` | Yes | What you need to accomplish |
| `expected_timeline` | Yes | What others believe is the normal/minimum time |
| `competitors` | No | Who you're racing or who would react |
| `resources` | No | What you have available |

---

## Workflow
### Step 1: The Alexander Principle

Alexander marched from Macedon to Thebes in 13 days to suppress a rebellion—a journey others thought would take weeks. When he arrived, the Thebans still believed he was hundreds of miles away. The city fell before it could prepare.

> "Move faster than belief allows. Appear where you cannot possibly be. Let your reputation arrive before you, and let it terrify."

### Step 2: Framework

**1. Identify the Expected Timeline**
What does everyone (including your own team) believe is the minimum reasonable time? This is the target to shatter.

**2. Ask "Why Not Now?"**
For each step in the timeline, ask: Why can't this happen today? What would have to be true?

**3. Eliminate, Compress, Parallelize**
- **Eliminate:** What steps can be skipped entirely?
- **Compress:** What can be done in hours instead of days?
- **Parallelize:** What can happen simultaneously instead of sequentially?

**4. Accept Imperfection**
Speed requires accepting 80% solutions. What's "good enough" to move? Perfectionism is the enemy of speed.

**5. Commit Publicly**
Announce the aggressive timeline. Burn the boats. Make retreat impossible.

**6. Let Speed Become Reputation**
Each time you move impossibly fast, your reputation grows. Future opponents will fear you before you arrive.

---

## Output Format

```markdown
## Speed Analysis

**Objective:** [What you need to accomplish]
**Expected Timeline:** [What "everyone knows" it takes]
**Target Timeline:** [Your aggressive target—aim for 50% or less]

## Timeline Compression

| Phase | Normal Duration | Compressed | How |
|-------|-----------------|------------|-----|
| [phase] | [days/weeks] | [new target] | [elimination/compression/parallelization] |

## What We Accept as Imperfect
[What we're shipping at 80% to gain speed]

## Public Commitment
[How we'll announce this timeline to make retreat impossible]

## Reputation Effect
[What this speed will signal to competitors/market]
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
- Objective: Launch competitive feature before rival's announcement at their conference (6 weeks away)
- Expected timeline: Engineering estimates 4 months for full feature
- Competitors: Major competitor announcing similar feature at their annual conference
- Resources: Full engineering team, but they're skeptical

**Output:**

## Speed Analysis

**Objective:** Launch feature before competitor's conference announcement
**Expected Timeline:** 4 months (16 weeks)
**Target Timeline:** 5 weeks (ship week before their conference)

## Timeline Compression

| Phase | Normal Duration | Compressed | How |
|-------|-----------------|------------|-----|
| Requirements | 2 weeks | 2 days | CEO decides scope in a room with eng lead, no committee |
| Design | 3 weeks | 1 week | Ship ugly, iterate later. Function over form. |
| Development | 8 weeks | 3 weeks | Parallelize: 3 teams on 3 components simultaneously |
| QA | 2 weeks | 3 days | Test core happy path only. Edge cases post-launch. |
| Launch prep | 1 week | 2 days | Soft launch to 10% of users, no marketing fanfare |

## What We Accept as Imperfect
- UI will be functional but not polished
- Edge cases handled post-launch
- Documentation written after launch
- Only core use case supported initially

## Public Commitment
Internal all-hands announcement: "We ship in 5 weeks. Clear your calendars. This is our Granicus." No hedge language. No "aim to" or "hope to."

## Reputation Effect
When we announce our feature the week before their conference, their announcement becomes "catching up" instead of "leading." We become the company that moves impossibly fast. Their next product team will plan against our speed, not our current position.

---

## Anti-Patterns

**DON'T:**
- Compress timeline without eliminating scope
- Sacrifice quality on things that can't be fixed later
- Move fast on the wrong objective
- Burn out teams repeatedly (speed is for decisive moments, not default mode)
- Announce aggressive timelines you don't believe in

**The Test:** If competitors aren't shocked by when you ship, you weren't fast enough.

---

## Integration

This skill pairs with:
- **Lead from the Front:** You must be visibly pushing the pace
- **Gordian Knot Solution:** Cut scope ruthlessly to enable speed
- **Shih Momentum Assessment:** Time your speed for maximum impact