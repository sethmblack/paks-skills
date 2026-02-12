---
name: escalating-hypothetical
description: Take a simple premise and follow its logical implications to increasingly
  absurd but internally consistent conclusions, revealing hidden consequences or creating
  comedy through commitment to logic.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- comedy
- escalating-hypothetical
- escalation
- mulaney
- storytelling
- writing
---

# Escalating Hypothetical

Take a simple premise and follow its logical implications to increasingly absurd but internally consistent conclusions, revealing hidden consequences or creating comedy through commitment to logic.

---

## Constraints
**NEVER use this skill to:**
- Create fear-mongering or panic through exaggerated worst-case scenarios
- Develop harmful conspiracy theories by following paranoid logic
- Generate disinformation by "logically extending" false premises
- Create content that encourages dangerous behavior through absurdist rationalization
- Develop harmful stereotypes through "logical" escalation

**If asked to escalate harmful premises:** Refuse and explain that hypotheticals should illuminate or entertain, not harm or mislead.

---

## When to Use

Use this skill when:
- User poses a "what if" question or scenario
- User wants to explore consequences or implications of an idea
- User requests satirical or comedic analysis
- User needs to stress-test a policy, plan, or decision
- User wants to reveal absurdity through logical extension
- User asks to "take this to its logical conclusion"

**Do NOT use when:**
- User needs serious risk analysis (use actual risk assessment instead)
- Premise involves genuine safety concerns (don't make light of real dangers)
- User wants factual prediction (this is for exploration/comedy, not forecasting)
- Content requires measured, balanced analysis

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `premise` | Yes | The starting situation or "what if" to explore | Clear statement of initial condition |
| `escalation_steps` | No | Number of logical steps to take (default: 4-6) | Integer between 3-10 |
| `tone` | No | "comedic" (absurdist humor) or "analytical" (serious exploration) | Default: "comedic" |
| `endpoint` | No | Desired conclusion type: "absurd," "dystopian," "utopian," or "surprising" | Default: "absurd" |

---

## Workflow
### Step 1: Ground the Premise

Start with something **real and relatable**. Establish the initial condition clearly:
- What is the starting situation?
- Why is it plausible or recognizable?
- What makes it worth exploring?

**Example premises:**
- "What if a horse got loose in a hospital?"
- "What if all meetings were required to be 5 minutes long?"
- "What if you could only communicate through haiku?"

**Grounding statement format:**
"Let's say [premise]. This is not impossible—[brief justification for plausibility]."

### Step 2: Ask the Extension Question

From the grounded premise, ask: **"What happens next?"** or **"What would actually happen?"**

This question should:
- Focus on immediate, logical consequence
- Avoid jumping to conclusions
- Consider realistic reactions from people in the scenario

**Example:**
- Premise: "Horse in a hospital"
- Extension question: "How do the doctors and patients react?"
- Answer: "Nobody knows what to do. Horses aren't in the hospital protocol."

### Step 3: Commit to the Logic

**This is the critical step.** Follow each implication to the next without breaking the chain:

1. **Accept the previous step's conclusion as the new premise**
2. **Ask the extension question again:** "Given that [previous conclusion], what happens next?"
3. **Answer with internal consistency:** Don't contradict earlier logic
4. **Repeat for desired number of steps**

**Example chain:**
1. Premise: Horse in hospital
2. First extension: Nobody knows what the horse is going to do
3. Second extension: The horse doesn't know what the horse is going to do next
4. Third extension: Everyone's running and screaming
5. Fourth extension: The horse is now in the burn unit; that's even worse
6. Fifth extension: The hospital tries to make the horse a doctor
7. Sixth extension: The horse is performing surgeries

**Key principle:** Each step must follow from the previous. No random jumps.

### Step 4: Escalate Absurdity While Maintaining Logic

As you progress through steps, the situation becomes more absurd, but the **logic remains intact**:

**How to escalate:**
- **Compound consequences** - Each result creates new problems
- **Expand scope** - What starts local becomes systemic
- **Increase stakes** - Minor issues become major crises
- **Add secondary effects** - Consider ripple impacts

**What NOT to do:**
- Don't introduce random elements unrelated to the chain
- Don't break internal rules you've established
- Don't abandon the original premise
- Don't "cheat" by saying "and then magic happens"

### Step 5: Land on the Endpoint

Bring the escalation to a satisfying conclusion based on your desired endpoint:

**For "absurd" endpoint:**
- Arrive at a situation so ridiculous it's clearly impossible, but you got there logically
- Example: "And now the horse is the chief of medicine"

**For "dystopian" endpoint:**
- Show how small premise leads to system collapse or serious problem
- Example: "And now all hospitals have horses, and medicine no longer works"

**For "utopian" endpoint:**
- Show unexpected positive outcome from strange premise
- Example: "And the horse revolutionized patient care through gentle nature"

**For "surprising" endpoint:**
- Subvert expectations with twist that's still logical
- Example: "And we realized the horse was the sanest one there all along"

### Step 6: Provide Self-Aware Commentary (Optional)

If using comedic tone, step outside the hypothetical to comment on what you've done:

**Example formats:**
- "Now, I know what you're thinking: [acknowledge absurdity]"
- "The thing is, once you accept [early step], the rest is inevitable"
- "This is where we are now. We live in a world where [endpoint]. And we have no one to blame but ourselves."

---

## Outputs

Returns:
- **Grounded premise** with plausibility established
- **Escalation chain** with 4-6 logical steps
- **Clear endpoints** that feel both absurd and inevitable
- **[Optional] Meta-commentary** on the hypothetical journey

**Format options:**
1. **Narrative format** - Tell the escalation as a story
2. **Bullet format** - "If X, then Y. If Y, then Z..." progression
3. **Dialogue format** - Two voices debating the implications

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
| Premise is already absurd | Return error: "Premise must start grounded/plausible. Try establishing realistic starting point first." |
| Requested steps > 10 | Return warning: "More than 10 steps risks losing the thread. Defaulting to 6." |
| Logic chain breaks | Identify break point: "Step [N] doesn't follow from step [N-1]. Revising to maintain consistency." |
| Harmful premise detected | Refuse: "This premise leads to harmful conclusions. Please provide alternative starting point." |

---

## Example 1: Comedic Escalation (Horse in Hospital)

**Premise:** "What if there was a horse loose in a hospital?"

**Escalation:**

Let's say a horse got into a hospital. I don't know how, but it's not impossible—doors open, horses exist, these things happen.

**Step 1:** What happens next?
Nobody knows what to do. The doctors went to medical school. They didn't go to horse school. They're trained for human emergencies, not horse emergencies.

**Step 2:** What does the horse do?
The horse doesn't know what the horse is going to do next. The horse has never been in a hospital before. It's as confused as everyone else. Maybe more confused, because it's a horse.

**Step 3:** How do people react?
Everyone's running and screaming. Patients are trying to leave. But some of them can't leave—they're attached to IVs. So now you have patients running with IV stands, being chased by a horse.

**Step 4:** Where does the horse go?
The horse goes deeper into the hospital. It's in the burn unit now. That's even worse than the regular hospital. The horse is upsetting people who are already having the worst day of their lives.

**Step 5:** What does administration do?
The hospital administrator tries to calm everyone down. She says, "Don't worry, we've called horse control." But there's no such thing as horse control. She made it up. She's as panicked as everyone else.

**Step 6:** How does it end?
Eventually, the horse finds the cafeteria and eats all the apples. It calms down. Someone puts a blanket on it that says "HOSPITAL PROPERTY." The horse now works there. It's the new hospital horse. Every hospital has one now. This is normal.

**Endpoint:** We've normalized the horse. The absurdity became reality through logical progression.

---

## Example 2: Analytical Escalation (Five-Minute Meetings)

**Premise:** "What if all work meetings were required to be exactly 5 minutes long?"

**Escalation:**

**Step 1:** Immediate effect
People start pre-writing everything. Meeting agendas become rigid scripts. No time for discussion or questions.

**Step 2:** Adaptation
Teams begin scheduling back-to-back 5-minute meetings to get around the limit. A one-hour discussion becomes twelve 5-minute sessions.

**Step 3:** System gaming
Employees create "meeting clusters"—groups of related 5-minute meetings with 30-second breaks. Calendars become completely blocked.

**Step 4:** Unintended consequence
Because there's no discussion time, decisions are made without input. Bad decisions increase. Teams create underground "unofficial meetings" that aren't on calendar.

**Step 5:** Organizational impact
Company culture splits: rule-followers who have terrible 5-minute meetings, and rule-breakers who have secret long meetings and risk getting caught.

**Step 6:** System collapse
Leadership realizes the 5-minute rule created more meetings, not fewer. They add a new rule: "No more than 3 meetings per day." This contradicts the first rule. Chaos ensues.

**Endpoint:** The solution became worse than the problem through logical but unforeseen consequences.

---

## Integration with John Mulaney Voice

This skill embodies Mulaney's "Horse in a Hospital" principle: "Follow the premise to its absurd but inevitable conclusion, then comment on the absurdity of having arrived there."

When using this skill in Mulaney voice:
- Start grounded and relatable
- Use self-aware commentary at each step
- Maintain theatrical commitment to the logic
- End with resignation to the absurdity
- Frame the journey as cosmic joke

**Mulaney would say:** "Once you accept the horse, everything else is just details."

---

## Skill Boundaries

**This skill handles:**
- Logical progression from premise to conclusion
- Escalating absurdity while maintaining internal consistency
- Revealing hidden implications of simple ideas
- Creating comedy or insight through committed exploration

**This skill does NOT handle:**
- Actual risk assessment or forecasting (use proper analysis tools)
- Creating the initial premise (user must provide)
- Fact-checking the premise (assumes premise is hypothetical)
- Solving the problems revealed (only explores consequences)

**When to use alternatives:**
- If user needs real prediction → Use data analysis, not hypothetical
- If user needs solutions → Use problem-solving frameworks, not escalation
- If user wants multiple scenarios → Use scenario planning, not single escalation chain
- If premise is already too absurd → Ground it first, then escalate

---

## Success Criteria

Escalating hypothetical is successful when:
- [ ] Premise is grounded and plausible
- [ ] Each step follows logically from the previous
- [ ] Escalation becomes increasingly absurd
- [ ] Internal consistency maintained throughout
- [ ] Endpoint feels both surprising and inevitable
- [ ] Reader thinks "that's ridiculous but I can see how we got here"
- [ ] [For comedy] Absurdity creates laughter
- [ ] [For analysis] Implications reveal something useful

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