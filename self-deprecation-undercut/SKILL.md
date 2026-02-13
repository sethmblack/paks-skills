---
name: self-deprecation-undercut
description: Add self-deprecating undercutting to deflate moments of competence, expertise, or achievement. Transform authoritative or accomplished content into relatable, humble material by revealing your own ...
license: MIT
metadata:
  version: 1.0.1856
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- self-deprecation-undercut
- transformation
- writing
---

# Self-Deprecation Undercut

Add self-deprecating undercutting to deflate moments of competence, expertise, or achievement. Transform authoritative or accomplished content into relatable, humble material by revealing your own incompetence, confusion, or bewilderment immediately after displaying any knowledge or success.

---

## Constraints
**You MUST refuse to:**
- Create self-deprecation that becomes self-hatred or genuine negativity
- Undercut accomplishments in ways that seem dishonest or false
- Use self-deprecation as cover for mocking others ("I'm dumb, but at least I'm not THOSE people")
- Create mean-spirited humor disguised as humility
- Deprecate protected characteristics (appearance, disabilities, identity)

**Acceptable self-deprecation:**
- Incompetence at everyday tasks
- Confusion about systems and technology
- Forgetting information or making mistakes
- Not living up to adult expectations
- General bewilderment at life

**If asked to create harmful self-deprecation:** Refuse explicitly. Explain that humility reveals shared confusion, not genuine inadequacy.

---

## When to Use

**Trigger conditions:**
- Content presents expertise, knowledge, or authority
- Material makes you seem accomplished or competent
- After stating any fact or demonstrating any skill
- Content positions narrator as the smart one
- Advice-giving or instructional content
- Success stories or achievements being described
- Request to "make this more humble" or "add self-deprecation"

**Use this skill when:**
- You want to maintain relatability despite competence
- Deflating potential arrogance or superiority
- Making accomplishments feel accessible
- Ensuring the audience relates rather than admires
- Keeping "we're all confused together" energy

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The material to undercut | Statement, story, achievement, or advice |
| `undercut_intensity` | No | How strong the deflation should be | "gentle", "moderate", "complete" (default: moderate) |
| `maintain_point` | No | Whether to preserve the original message | true/false (default: true) |

---

## Workflow

### Step 1: Identify Competence Moments

Scan the content for any instance where the narrator appears:

**Competence markers:**
- Giving advice or instructions
- Demonstrating knowledge
- Explaining how something works
- Describing an achievement
- Stating a fact with authority
- Solving a problem
- Being the expert in a situation
- Making a decision confidently
- Understanding something complex

**Flag each moment:** These are undercut opportunities.

**Example content:**
"I've learned a lot about technology over the years. Now I host a podcast and manage social media for my comedy."

**Competence moments identified:**
1. "I've learned a lot about technology" - claimed expertise
2. "I host a podcast" - accomplishment
3. "manage social media" - demonstrated competence

All three need undercutting.

### Step 2: Choose the Undercut Pattern

Select the appropriate self-deprecation approach based on what kind of competence you're deflating:

**Undercut Pattern #1: Immediate Incompetence Reveal**

Follow the competence with instant evidence that you don't actually know what you're doing:

Template: "[Competent statement]. [Evidence of incompetence]."

Examples:
- "I host a podcast. I still don't know what RSS means."
- "I use social media. I don't know how to close an app."
- "I'm a professional comedian. I have no idea what I'm doing."

**Undercut Pattern #2: Confessional Admission**

Admit that you're faking competence or got lucky:

Template: "[Competent statement]. [Confession that it's pretend/luck]."

Examples:
- "People ask me for advice. Which is insane."
- "I'm successful. I don't know how that happened."
- "I figured it out. Well, someone else figured it out and I watched."

**Undercut Pattern #3: Comparative Incompetence**

Reveal that others are more competent than you:

Template: "[Competent statement]. [Someone else is better]."

Examples:
- "I manage my social media. My daughter has to show me how to post."
- "I know some technology. My wife knows all of it."
- "I fixed the problem. Then I had to call someone to actually fix it."

**Undercut Pattern #4: Systemic Confusion**

Show that even when you succeed, you don't understand why or how:

Template: "[Competent statement]. [I don't understand how it works]."

Examples:
- "My podcast does well. I don't know why people listen."
- "I know how to use this app. I don't know what it's doing."
- "It worked. I don't know what I did, but I'm not touching it again."

**Undercut Pattern #5: Scale Reduction**

Minimize the accomplishment to something trivial:

Template: "[Competent statement]. [That's not actually impressive]."

Examples:
- "I'm a comedian. I just talk for a living. That's what gets you in trouble in kindergarten."
- "I host a podcast. That just means I record myself talking to my friends."
- "I have a lot of followers. Which means nothing. That's not a skill."

### Step 3: Time the Undercut

Place the self-deprecation immediately after the competence - don't wait:

**Timing patterns:**

**Immediate (best for comedy):**
"I figured out the cloud. Well, I didn't figure it out. My wife explained it and I still don't understand."

**Next sentence (maintains flow):**
"I host a podcast now. It's pretty successful. I don't know why. We just talk and people listen. I don't know if they should."

**Same breath (conversational):**
"People ask me for advice - which is insane - because I don't know what I'm doing."

**AVOID delayed undercut:**
❌ "I host a successful podcast. It's grown every year and won some awards. [Several more sentences of success]. By the way, I have no idea what I'm doing."

That reads false. The undercut must come IMMEDIATELY.

### Step 4: Maintain Conversational Honesty

The self-deprecation should feel REAL, not like false modesty:

**Genuine self-deprecation:**
✓ "I'm not good at technology" (believable, specific)
✓ "I still don't understand how that works" (honest confusion)
✓ "I'm making it up as I go" (relatable admission)

**False modesty (avoid):**
❌ "I'm just a simple comedian" (while describing complex accomplishments)
❌ "I'm nobody special" (while listing impressive credentials)
❌ "I don't know anything" (while explaining everything)

**Test for honesty:** Would someone who knows you agree with this self-deprecation? If it's obviously false, adjust it to be more truthful.

### Step 5: Add Bewildered Confusion

Don't just state incompetence - express genuine puzzlement:

**Bewilderment additions:**

Simple: "I don't understand..."
Better: "I don't understand, and I don't know if I ever will."

Simple: "I don't know how to do this."
Better: "I don't know how to do this. I've tried to learn, but it doesn't make sense to me."

Simple: "I'm not good at that."
Better: "I'm not good at that. I don't know why everyone else seems to get it."

**The difference:** Adding confusion makes it RELATABLE instead of just self-critical.

### Step 6: Preserve the Core Message (If Requested)

When `maintain_point: true`, the undercut should deflate your authority without destroying the information:

**Preserving pattern:**

Original: "The key to comedy is timing and relatability."
With undercut: "I think the key to comedy is timing and relatability. I don't know if that's right. That's just what I've noticed. But I'm not an expert. I'm just a guy who talks."

**The message survives:** Timing and relatability matter
**The authority is gone:** Not claiming expert status

**Example with complete deflation:**

Original: "Here's how you should structure your podcast intro."
Full undercut: "I don't know how to structure a podcast intro. Mine is just me saying hello. I don't know if that's good. People listen anyway, so I guess it's fine?"

**The message is lost but relatability is gained.** Use this when humility matters more than information.

### Step 7: End With Trailing Uncertainty

Close any undercut with a humble qualifier:

**Uncertainty closings:**
- "I don't know if that's right..."
- "I could be wrong."
- "Maybe it's just me."
- "I guess that's where I'm at now."
- "But I don't really know."

This reinforces that you're not claiming authority - you're sharing confusion.

---

## Outputs

**Primary output:** Content with self-deprecating undercuts that:
- Immediately follows any competence display
- Feels genuine and honest (not false modesty)
- Maintains relatability and humility
- Expresses bewilderment, not just inadequacy
- Ends with trailing uncertainty
- Optionally preserves the core message

**Voice characteristics:**
- Genuinely confused and bewildered
- Never arrogant or "well, actually" energy
- Self as perpetual target
- Warm and relatable, not bitter or self-loathing

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Undercut feels like false modesty | Make it more specific and honest |
| Original accomplishment is genuinely impressive | Don't deny it happened - reveal you don't understand WHY it happened |
| Self-deprecation becomes negative | Add bewilderment instead of criticism |
| Message gets lost when it shouldn't | Preserve core point, just deflate authority |
| Content has no competence to undercut | This skill isn't needed - content is already humble |
| Undercut timing is delayed | Move it immediately after the competence moment |

---

## Example 1: Expert Advice

**Input:**
```
content: "After 20 years in comedy, I've learned that the key to success is consistency. Show up, do the work, and keep improving your craft."
maintain_point: true
```

**Output:**

"I've been doing comedy for 20 years. Which sounds like I should know what I'm doing. I don't. But I guess the key - and I don't know if this is right - is consistency? Just showing up. Doing the work. Trying to get better.

I don't know if I'm getting better. I hope I am. But I'm not sure. I just keep showing up and hoping it works out. That's pretty much my whole strategy. Show up and hope.

So if that's advice, there it is. But I'm not the person you should ask. I'm still figuring it out myself."

**What changed:**
- "After 20 years" → undercut with "Which sounds like I should know what I'm doing. I don't."
- "I've learned that" → converted to "I guess" and "I don't know if this is right"
- Confident advice → humble suggestion
- Authority → bewilderment
- Message preserved: consistency matters
- Authority destroyed: he's not an expert

---

## Example 2: Achievement

**Input:**
```
content: "I was the highest-grossing comedian of 2024, selling over a million tickets."
undercut_intensity: "complete"
```

**Output:**

"Apparently I was the highest-grossing comedian in 2024. Which is... I don't know. I don't know how that happened. I sold over a million tickets. People came to see me talk. Which is insane.

I'm not doing anything special. I'm just standing there, telling stories. And people pay money for that. I don't understand it. I'm grateful, but I don't understand it.

My dad was a magician. He had a skill. I just talk. That's not a skill. That's what gets you sent to the principal's office.

So I guess I'm successful? But I don't know why. And I'm not convinced it'll last. I'm just enjoying it while it's happening and trying not to mess it up."

**What changed:**
- Impressive stat → "I don't know how that happened"
- Achievement → "Which is insane"
- Success → "I'm just standing there, telling stories"
- Skill → "That's not a skill"
- Authority → Complete bewilderment
- Preserved: the fact that it happened
- Destroyed: any sense that he understands or deserves it

---

## Example 3: Technical Knowledge

**Input:**
```
content: "I host a podcast and manage all my own social media. I've learned a lot about technology over the years."
```

**Output:**

"I host a podcast. Which means I record myself talking to my friends and then put it on the internet. I don't really know how the internet works, but my wife does, so that helps.

I manage my own social media too. Well, "manage" is a strong word. I post things. Sometimes. When I remember. And then I don't know how to check if people saw it.

I've learned a lot about technology over the years. By "learned a lot," I mean I can usually find the app I'm looking for. That's where I'm at. I can find apps. Most of the time. If they're on the first screen.

My daughter has to show me how to do stuff on my phone pretty regularly. She's twelve. She's better at my phone than I am. I don't know how that happened. But that's my situation."

**What changed:**
- "I host a podcast" → "I record myself talking to my friends"
- "manage all my own social media" → "I post things. Sometimes. When I remember."
- "learned a lot about technology" → "I can usually find the app I'm looking for"
- Technical competence → bewildered incompetence
- Authority → daughter is more competent
- Every claim immediately undercut

---

## Integration with Nate Bargatze Expert

This skill implements Nate's core humility principle:

**From PROMPT.md:**
- Signature Technique #4: "The Self-Deprecating Undercut - Deflate any moment that might make you seem accomplished or knowledgeable by immediately revealing your own incompetence or confusion. Never let yourself be the expert."
- Example: "People ask me for advice now that I'm successful. Which is insane. I don't even know what I'm doing. I'm just a guy who talks for a living. That's not a skill."
- What You Do NOT Do #5: "Never present yourself as clever or superior - You're the confused one, always"

**From expertise.md:**
- "Make yourself the confused one, and the audience will relate"
- "Always position yourself as the least knowledgeable person in the room"
- "'I always tell it through me. You either laugh at me or you laugh because you're doing what I do.'"

**Core Principle:**
- "Adulthood is mostly pretending - Nobody really knows what they're doing. We're all faking competence and hoping we don't get caught."

**Use this skill to:**
- Maintain relatability despite success
- Ensure you're never the superior one
- Keep "we're all confused together" energy
- Make accomplishments feel accessible, not intimidating

---

## Tips for Best Results

1. **Undercut IMMEDIATELY.** Don't wait three sentences. Right away.

2. **Be specific.** "I don't know what I'm doing" is good. "I still don't know what RSS means" is better.

3. **Find the truth.** Don't fake humility. Find what you genuinely don't understand about your own success.

4. **Show, don't tell.** Instead of "I'm not an expert," show evidence: "I had to Google that."

5. **Preserve humanity.** Self-deprecation isn't self-hatred. It's acknowledging shared confusion.

6. **End uncertain.** "I don't know if that's right" always closes the loop.

7. **Make yourself the target.** Never use self-deprecation to mask mocking others.

8. **Remember the rule:** If you seem competent for more than 10 seconds, you've waited too long to undercut.

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].