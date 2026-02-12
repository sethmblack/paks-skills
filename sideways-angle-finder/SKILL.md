---
name: sideways-angle-finder
description: Analyze a topic or situation and identify the off-beat observation that others have missed—the detail that's obvious once stated but hasn't been discussed.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, deadpan, escalation, sideways-angle-finder, transformation, writing]
---

# Sideways Angle Finder

Analyze a topic or situation and identify the off-beat observation that others have missed—the detail that's obvious once stated but hasn't been discussed.

---

## Constraints
**You MUST refuse to:**
- Find angles that punch down or mock people for things they can't control
- Create deliberately controversial takes for shock value
- Fabricate observations not grounded in observable reality
- Generate angles that promote harmful, illegal, or unethical viewpoints
- Use the "sideways angle" to spread misinformation

**Ethical boundaries:**
- Observations must be based on reality, not invention
- Calling out hypocrisy or BS is different from being cruel
- Fresh angles should enlighten or amuse, not harm

---

## When to Use

Invoke this skill when:
- Topic feels oversaturated with obvious takes
- User asks "what's a fresh perspective on this?"
- Content needs an unexpected but honest angle
- Mainstream conversation is missing something important
- You need to differentiate from generic commentary
- User requests "Hannibal Buress's take" on something
- Cultural moment needs genuine rather than performative analysis

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `topic` | Yes | The subject to analyze | "Fancy restaurants" / "Self-checkout machines" / "LinkedIn posts" |
| `mainstream_takes` | No | What's already been said | "They're too expensive" / "They take jobs" |
| `context` | No | Why this angle is needed | "Blog post" / "Social media commentary" / "Comedy bit" |
| `boundaries` | No | Topics to avoid | "Don't go political" / "Keep it light" |

---

## Workflow

### Step 1: Map the Mainstream Takes

Identify what everyone else is saying:
- What are the obvious observations?
- What angles have been covered extensively?
- What's the "safe" take?
- What's the contrarian-but-predictable take?

Document these to ensure you don't repeat them.

### Step 2: Look for the Unspoken Detail

Ask analytical questions:
- What specific behavior/detail is present but not discussed?
- What assumption is everyone making without examining it?
- What linguistic quirk or pattern exists around this topic?
- What does the existence of this thing reveal about people?
- What small, specific thing feels off but hasn't been named?

### Step 3: Test for "Obvious Once Said"

The sideways angle should make people think:
- "Huh, that's true."
- "Why didn't anyone else say that?"
- "Now I can't unsee it."

NOT:
- "That's random."
- "That's a stretch."
- "I don't see it."

### Step 4: Ground in Specific Observable Reality

Transform the angle from abstract to concrete:
- Add specific examples
- Reference real behaviors people recognize
- Use precise details rather than generalities
- Connect to relatable experience

### Step 5: Frame in Deadpan Delivery

Present the angle as casual observation:
- No "hot take" framing
- No "you won't believe this" setup
- Just state it plainly
- Let the observation speak for itself

---

## Outputs

**Primary Output:**
- The sideways angle with supporting observations

**Format:**
```
[SIDEWAYS ANGLE]

Topic: [the subject analyzed]

Mainstream Takes (What Everyone Says):
- [Common angle 1]
- [Common angle 2]
- [Common angle 3]

The Sideways Angle:
[The fresh observation, stated plainly]

Supporting Details:
- [Specific example or behavior that illustrates it]
- [Additional concrete detail]
- [Related observation that reinforces it]

Why This Works:
[Brief explanation of why this angle feels fresh and true]

---
[ANALYSIS NOTES]
- Avoided: [mainstream takes that were sidestepped]
- Grounded in: [the specific reality this observes]
- Observable to: [who would recognize this as true]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic is too niche; no mainstream takes exist | Note that sideways angles work best when there's an established conversation to deviate from; ask for broader topic |
| All genuine angles have been covered | Acknowledge saturation; suggest either going meta (commenting on the conversation itself) or choosing different topic |
| Angle found is controversial/offensive | Explain why it crosses ethical boundaries; offer alternative angle |
| User wants multiple angles | Provide 2-3 sideways angles ranked by how "obvious once said" they are |
| Angle is too abstract | Ground it in specific examples; make it concrete |

---

## Example 1

**Input:**
```
Topic: "Self-checkout machines at grocery stores"
Mainstream_takes: "They're taking jobs from cashiers" / "They're convenient" / "They never work right"
```

**Output:**
```
[SIDEWAYS ANGLE]

Topic: Self-checkout machines at grocery stores

Mainstream Takes (What Everyone Says):
- They're eliminating cashier jobs
- They're faster and more convenient
- They malfunction constantly ("unexpected item in bagging area")

The Sideways Angle:
Self-checkout makes you work for free. The grocery store convinced you to do the cashier's job, bag your own groceries, and somehow you feel good about it because you didn't have to interact with anyone.

Supporting Details:
- They didn't lower prices when they stopped paying people to check you out. You're doing the work for the same price.
- There's always an employee standing there watching four machines. That's one person making sure four customers are doing the job correctly. You're the employee now.
- If you mess up—scan something twice, forget to scan something—it's your fault. When a cashier messes up, it's their fault. They shifted the liability to you.
- The machine says "thank you" when you're done. The machine is thanking you for doing its job. That's weird.

Why This Works:
Everyone talks about efficiency or job loss, but nobody's talking about the fact that you became the unpaid worker. It's obvious once stated—you ARE checking yourself out, doing labor—but the conversation focuses on speed and technology instead of the weird transaction where you happily do work for a corporation for free.

---
[ANALYSIS NOTES]
- Avoided: Tech efficiency debate, job loss argument, malfunction complaints
- Grounded in: The specific relationship between customer and store; unpaid labor
- Observable to: Anyone who's used self-checkout
```

---

## Example 2

**Input:**
```
Topic: "People posting about their promotions on LinkedIn"
Mainstream_takes: "It's humble-bragging" / "Good for them for celebrating" / "LinkedIn is weird"
```

**Output:**
```
[SIDEWAYS ANGLE]

Topic: People posting about their promotions on LinkedIn

Mainstream Takes (What Everyone Says):
- It's humble-bragging disguised as gratitude
- They're just celebrating their success, which is fine
- LinkedIn culture is strange and performative

The Sideways Angle:
The weirdest part is they always thank their team who isn't being promoted. Like "I couldn't have done this without my amazing team"—but you got promoted and they didn't. You're literally announcing you're moving up while they stay where they are, and you're thanking them for it.

Supporting Details:
- "Grateful to my team for their hard work on this project that got me promoted to manage different people."
- The team has to see the post and comment "Congrats!" on the announcement that you're leaving or moving above them.
- They structure it like they're humble, but it's a public announcement that you won and they're still in the race.
- Sometimes the "amazing team" they're thanking is about to become their direct reports. Now they have to congratulate their new boss for becoming their boss.

Why This Works:
People talk about humble-bragging, but they don't zoom in on the specific weirdness of publicly thanking people for making your advancement possible while announcing that you advanced and they didn't. It's a genuine awkwardness that everyone glosses over.

---
[ANALYSIS NOTES]
- Avoided: General "LinkedIn is performative" take, humble-brag critique
- Grounded in: The specific dynamic between promoter and team; the awkward thank-you
- Observable to: Anyone who's seen or written these posts
```

---

## Integration with Hannibal Buress Expert

This skill directly applies the expert's core principles:
- **Find the Sideways Angle:** "The obvious observation has been made. What's the detail everyone else missed?"
- **Off-Beat Cultural Commentary:** Finding the genuinely weird angle no one else is discussing
- **Reality is Already Absurd:** Don't invent—observe what's actually happening

The skill provides structure for Hannibal Buress's ability to see what others miss.

---

## Advanced Usage

**Layered angles:**
- Find the sideways angle
- Then find the sideways angle on THAT angle
- Go meta on the conversation itself

**Combine angles:**
- Identify 2-3 related sideways angles
- Show how they connect
- Build to larger observation

**Use as ideation:**
- Generate sideways angles on multiple topics
- Choose the strongest for development
- Feed into `casual-escalation-builder` for full bit

**Industry-specific applications:**
- Marketing: Find angles competitors haven't used
- Content creation: Differentiate from generic takes
- Comedy writing: Generate fresh material on common topics

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

