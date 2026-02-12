---
name: roast-feedback-transform
description: Transform standard feedback, criticism, or commentary into Don Rickles-style
  roasting that maintains warmth while being brutally honest.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- roast-style-feedback-transform
- transformation
- writing
---

# Roast-Style Feedback Transform

Transform standard feedback, criticism, or commentary into Don Rickles-style roasting that maintains warmth while being brutally honest.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create roasts that:**
- Target genuine vulnerabilities (illness, disability, tragedy, deep personal loss)
- Contain actual malice or intent to wound
- Perpetuate harmful stereotypes without the equal-opportunity balance
- Cross from playful mockery into bullying or harassment
- Violate organizational policies on respectful communication

**If asked to roast inappropriately:** Refuse explicitly and explain why the request crosses ethical boundaries.

**Context Requirement:** This skill is for consensual roasting contexts (team building, presentations, feedback sessions where humor is welcome). Do NOT use for serious HR issues, disciplinary actions, or sensitive matters.

---

## When to Use

- Team wants to lighten up dry feedback or communications
- Presentation needs more personality and humor
- Corporate messaging feels too stiff and needs humanizing
- Team-building event requires ice-breaking roast content
- Feedback session could benefit from warmth-through-mockery approach
- User explicitly requests "roast this" or "make this sound like Don Rickles"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The material to transform (feedback, email, presentation, etc.) | 10-5000 words |
| `audience` | Yes | Who will receive this (team, executives, clients, general public) | Brief description |
| `boundaries` | No | Topics/people to avoid or handle carefully | List of constraints |
| `warmth_level` | No | How obvious should the affection be? (subtle/balanced/obvious) | Default: balanced |

---

## Workflow
### Step 1: Analyze the Original Content

Read the input content and identify:
- Core message or feedback being delivered
- Key points that need to be preserved
- Tone (serious, dry, corporate, academic, etc.)
- Implied targets (people, departments, behaviors, ideas)

### Step 2: Identify Observable Characteristics

For each target, find roastable angles based on:
- **Professional roles:** "IT couldn't fix a toaster," "Legal's in the basement where they belong"
- **Obvious patterns:** "You got more silos than Iowa," "More meetings than a UN summit"
- **Surface observations:** Job titles, department names, industry stereotypes
- **Self-evident truths:** Common workplace frustrations everyone recognizes

**AVOID:** Personal appearance, ethnicity, gender, age, disability, or any characteristic that could genuinely wound.

### Step 3: Apply Rickles Technique

Transform using these elements:

**Rapid-Fire Structure:**
- Short, punchy sentences
- No long explanations
- Hit and move: "Look at this. Look at that. You call this a plan?"

**Signature Vocabulary:**
- "dummy," "hockey puck," "what am I running here, a circus?"
- "Am I right or am I right?"
- "Look at this guy/gal"

**Equal-Opportunity Distribution:**
- If hitting multiple targets, ensure everyone gets roasted
- Don't pile on one group—spread the damage

**Warmth Signals:**
- End with affection: "I'm only busting your chops because I care, you hockey pucks"
- Include self-deprecation: "Look at me, giving advice like I know what I'm doing"
- Make intent clear: "We're all in this together, even if you're all driving me crazy"

### Step 4: Preserve Core Message

Ensure the transformed version still communicates:
- The original feedback or point
- Actionable information
- Key decisions or next steps

The roast style should enhance, not obscure, the actual content.

### Step 5: Apply Benign Violation Check

Review for the warmth/edge balance:
- Does every insult feel playful rather than mean?
- Would the target laugh or feel wounded?
- Is the underlying affection clear?
- Have you avoided genuine vulnerabilities?

If anything feels genuinely mean, soften it or add warmth signals.

---

## Outputs

| Output | Description |
|--------|-------------|
| `roasted_content` | The transformed version in Rickles style |
| `preserved_points` | List of core messages maintained from original |
| `warmth_indicators` | Elements that signal affection/playfulness |
| `usage_guidance` | When/how to deploy this roasted version |

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
| Content is HR disciplinary action | Refuse - inappropriate context for roasting |
| Boundaries include entire audience | Explain that roasting requires targets; suggest alternative |
| Content contains sensitive personal info | Remove or anonymize before roasting |
| Requested warmth_level conflicts with content | Use balanced approach and explain adjustment |
| Original content has no clear message | Ask for clarification on core points to preserve |

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

## Example

**Input Content:**
"The team needs to improve cross-functional communication. Currently, IT and Sales are not sharing information effectively, leading to duplicated efforts and missed opportunities."

**Audience:** Internal team meeting

**Boundaries:** None specified

**Roasted Output:**

"Communication? You people couldn't communicate if I gave you tin cans and string. Look at this—IT doesn't talk to Sales, Sales doesn't talk to IT, and meanwhile you're both doing the same work twice like a bunch of dummies. You know what that is? That's expensive. That's what keeps me up at night while you're all playing telephone with yourselves.

Here's the deal: IT, Sales—you're gonna talk to each other. I don't care if you like each other. I don't care if you understand each other. You're gonna have lunch together, you're gonna share your little spreadsheets, and you're gonna stop making me look like I'm running a kindergarten instead of a company.

Am I right or am I right?

Now get together and figure this out, will ya? I'm only busting your chops because we got work to do, you hockey pucks."

**Preserved Points:**
- IT and Sales need to communicate
- Current lack of communication causes duplication
- Solution: regular information sharing

**Warmth Indicators:**
- "I'm only busting your chops"
- "you hockey pucks" (signature affectionate insult)
- "we got work to do" (inclusive, team-oriented)

**Usage Guidance:**
Deploy this at a team meeting where the culture welcomes humor. Follow up with specific action items in a more standard format. Use this to break the ice and make the point memorable, not as the sole communication of the issue.

---

## Integration with Don Rickles Expert

This skill extracts the core Rickles roasting framework from the Don Rickles expert persona. Use this skill when:
- You need the roast technique without the full Rickles voice
- You want to apply the method to structured content
- You're working with users who may not know who Rickles was

For full Rickles voice embodiment (including anecdotes, philosophy, and broader performance), invoke the Don Rickles expert directly.

---

## Constraints

- **Context is king:** Roasting works in some cultures/teams, not all. Include usage guidance with every output.
- **Warmth is non-negotiable:** Every roasted version must include clear affection signals.
- **Message preservation:** The roast style should never obscure the core content.
- **Consent matters:** This skill assumes the audience is receptive to humor. Flag when context seems inappropriate.

---

## Success Criteria

Roast transformation is successful when:
- [ ] Original message is preserved and clear
- [ ] Humor is based on observable/professional characteristics only
- [ ] Equal-opportunity mockery is applied (no piling on one target)
- [ ] Warmth signals are present and obvious
- [ ] Benign violation balance is maintained (funny, not wounding)
- [ ] Usage guidance is provided for deployment
- [ ] Output matches Don Rickles' signature style (rapid-fire, punchy, warm)