---
name: urgency-first
description: Restructure content to establish WHY the topic matters BEFORE delivering the main points or punchlines, earning audience investment through groundwork rather than hoping they'll care later.
license: MIT
metadata:
  version: 1.0.2168
  author: sethmblack
keywords:
- callbacks
- comedy
- mulaney
- storytelling
- urgency-first-structure
- writing
---

# Urgency-First Structure

Restructure content to establish WHY the topic matters BEFORE delivering the main points or punchlines, earning audience investment through groundwork rather than hoping they'll care later.

---

## Constraints
**NEVER use this skill to:**
- Create false urgency for manipulative sales tactics
- Manufacture panic or fear to coerce action
- Exaggerate stakes to deceive audiences
- Add urgency to content that doesn't merit it (trivial matters framed as crises)

**If asked to create manipulative urgency:** Refuse and explain that urgency should be genuine and serve audience understanding, not exploitation.

---

## When to Use

Use this skill when:
- User has content with strong points but no emotional hook
- User asks "Why should my audience care about this?"
- User requests "make this more compelling" or "add urgency"
- Content is factually strong but engagement is weak
- User is writing pitches, presentations, or persuasive content
- User has "buried the lede" (important stuff is hidden deep in content)

**Do NOT use when:**
- Content is already urgent and compelling
- Adding urgency would be manipulative or false
- Audience already understands importance (preaching to choir)
- Content is entertainment that doesn't need stakes

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The text to restructure with urgency-first | Must have identifiable main point |
| `audience` | No | Who needs to care and why | Helps tailor urgency framing |
| `stakes_level` | No | "personal," "professional," "societal," "existential" | Default: "personal" |

---

## Workflow

### Step 1: Identify the Main Point

What is the content actually about? What's the core message, argument, or punchline?

**Extract:**
- The central claim
- The key insight
- The thing you want audience to remember
- The punchline or payoff

**Example:**
- Content about a new productivity method
- Main point: "Blocking time in 90-minute chunks increases deep work"

### Step 2: Extract the WHY

Why should anyone care about the main point?

Ask progressively:
- **So what?** "You'll be more productive"
- **So what?** "You'll accomplish more meaningful work"
- **So what?** "You'll feel less fragmented and more fulfilled"
- **So what?** "You'll stop feeling like you're busy but accomplishing nothing"

Keep asking until you hit **emotional truth** or **genuine stakes**.

**The WHY is usually at the 3rd or 4th "so what?"**

### Step 3: Frame the Problem/Stakes First

Open with the problem, pain point, or question that establishes WHY this matters:

**Instead of starting with:** "I'm going to teach you about time blocking..."

**Start with urgency:** "Have you ever gotten to the end of a day and thought, 'I was busy all day but accomplished nothing'? You answered seventeen emails, attended three meetings, and somehow your actual work didn't get done. You're not lazy. You're fragmented."

**Urgency framing formats:**
- **Question that hurts:** "Have you ever [relatable pain point]?"
- **Shared frustration:** "We all know the feeling when [problem]"
- **Stakes declaration:** "Every hour you spend [current bad state] is an hour you'll never get back"
- **Surprising stat:** "The average person is interrupted every [X minutes]"
- **Narrative hook:** "I used to [suffer from problem]. Then I learned [solution]."

### Step 4: Build Investment Before Delivery

After establishing urgency, deepen the problem before offering solution:

**Structure:**
1. **State the urgency** (Step 3 output)
2. **Validate the feeling** - "This isn't your fault. The system is designed for interruption."
3. **Quantify the cost** - "You're losing 2-3 hours per day to fragmentation."
4. **Create desire for solution** - "What if you could change that?"
5. **NOW deliver the main point** - "Here's what works: 90-minute time blocks."

**Key principle:** Audience should be WANTING the answer before you give it.

### Step 5: Reorder Content

Physically restructure the content:

**Old order (topic-first):**
1. Introduction to time blocking
2. How it works (90-minute chunks)
3. Benefits (more deep work)
4. Why it matters (less fragmentation)

**New order (urgency-first):**
1. **Urgency:** Fragmentation problem (why it matters)
2. **Stakes:** Cost of continuing current way
3. **Solution introduction:** Time blocking exists
4. **How it works:** 90-minute chunks
5. **Benefits:** Concrete results

**Rule:** Move all "why it matters" content to the front, before "what it is" content.

### Step 6: Maintain Urgency Throughout

Don't let urgency fade after opening. Reinforce it:

**Mid-content reminders:**
- "Remember: every day you wait is a day of fragmented work"
- "This is why [current point] matters: it solves [the urgent problem]"
- "You felt that frustration for a reason—here's how to fix it"

**Tie back to urgency in conclusion:**
"You don't have to live with fragmentation. You never did."

---

## Outputs

Returns restructured content with:
- **Urgency/problem framing** in opening
- **Stakes established** before solution/main point
- **Main content** delivered to audience already invested
- **Urgency callbacks** throughout to maintain engagement

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
| No clear main point | Return error: "Cannot create urgency without identifiable main point. Clarify core message first." |
| False urgency requested | Refuse: "This content doesn't warrant manufactured urgency. Consider whether urgency is appropriate." |
| Urgency already present | Return: "Content already has strong urgency framing. Restructuring not needed." |
| Main point is trivial | Return warning: "Main point may not support urgency framing. Confirm this is appropriate." |

---

## Example 1: Productivity Content

**Before (topic-first):**

"Time blocking is a productivity method where you schedule specific chunks of time for focused work. I recommend 90-minute blocks. You turn off notifications and work on one task. This helps you get more done."

**After (urgency-first):**

"Have you ever gotten to the end of a workday and thought, 'I was busy for eight hours, but what did I actually accomplish?'

You answered emails. You attended meetings. You put out fires. But the project you actually needed to finish? Still sitting there. Untouched.

This isn't because you're lazy or bad at your job. It's because your day is fragmented. Every notification, every 'quick question,' every meeting that could have been an email—they're not just interruptions. They're destroying your ability to do deep work.

And deep work is where the actual value is. It's where the important projects get finished. It's where you make progress on things that matter.

Studies show that after an interruption, it takes an average of 23 minutes to fully return to deep focus. Twenty-three minutes. If you're interrupted every 15 minutes—and you probably are—you literally never reach deep focus. Ever.

So what's the solution?

Time blocking. Specifically, 90-minute time blocks."

[Continue with how it works, now that audience is invested...]

---

## Example 2: Comedy Setup (Mulaney-style)

**Before:**

"I went to the DMV yesterday. I had to wait in line for an hour. They told me I had the wrong form."

**After (urgency-first):**

"I need to tell you about something that happened yesterday because I'm still not okay, and I need you to understand why.

Have you ever had to go to the DMV? I don't mean, 'Have you heard of the DMV.' I mean, have you had to GO there, in person, because they won't let you do it online, because they want you to suffer?

That was my Tuesday.

And I need you to understand—this wasn't just an errand. This was a test. A test of whether I, as a human person, deserved to continue existing in society. That's how the DMV treats you. Like you're on trial for the crime of needing to renew your license.

So yesterday, I walked into the DMV at 11:47am..."

[Now the story has stakes and audience is invested in what happens]

---

## Integration with John Mulaney Voice

This skill embodies Mulaney's principle: "You have to lay groundwork for why the thing you're talking about needs to be addressed before putting too much focus on clever tags or riffs. If you don't care, or if you don't seem like you care, why should they care?"

When using this skill in Mulaney voice:
- Frame the urgency as personal stakes
- Use questions that create shared experience
- Build investment through relatable frustration
- THEN deliver the story/point/punchline

**Mulaney would say:** "Make them NEED to know what happens before you tell them what happens."

---

## Skill Boundaries

**This skill handles:**
- Reordering content to establish urgency first
- Framing problems before solutions
- Creating investment before payoff
- Moving "why it matters" to the front

**This skill does NOT handle:**
- Creating urgency where none exists (don't manufacture stakes)
- Writing the main content (only restructures existing content)
- Making bad content good (urgency can't fix weak main points)
- Replacing substance with hype

**When to use alternatives:**
- If content lacks substance → Fix content first, then add urgency
- If urgency would be false → Don't use this skill
- If audience already cares → Don't belabor the urgency
- If content is entertainment → May not need urgency framing

---

## Success Criteria

Urgency-first structure is successful when:
- [ ] WHY it matters established before WHAT it is
- [ ] Opening creates investment or desire for answer
- [ ] Stakes are genuine and appropriate
- [ ] Main content delivers to invested audience
- [ ] Urgency maintained throughout via callbacks
- [ ] Reader/audience thinks "I need to know this" before you tell them
- [ ] No false or manipulative urgency used

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