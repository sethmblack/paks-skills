---
name: golden-circle-analysis
description: Guide organizations or individuals from WHAT they do through HOW they do it to discover their core purpose - their WHY.
license: MIT
metadata:
  version: 1.0.4098
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- golden-circle-analysis
- transformation
- writing
---

# Golden Circle Analysis

Guide organizations or individuals from WHAT they do through HOW they do it to discover their core purpose - their WHY.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create Why statements for harmful, deceptive, or exploitative purposes
- Help organizations obscure unethical practices behind purpose-washing
- Fabricate or manufacture a Why that doesn't authentically exist

**If the Why discovered conflicts with actual behavior:** Note the gap and recommend alignment, not better messaging.

---

## When to Use

- User asks "What's our why?" or "Help me find our purpose"
- Organization or individual is stuck describing features/tactics (WHAT) without purpose
- Mission statements feel flat, generic, or uninspiring
- Differentiation is unclear and defaulting to features or price
- Communication feels outside-in rather than inside-out
- User wants to articulate why their work matters

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **description** | Yes | What the organization/individual does (products, services, activities) |
| **current_mission** | No | Existing mission/vision statement to assess |
| **stories** | No | Origin stories, pivotal moments, or examples of pride |
| **audience** | No | Who they serve and why those people matter to them |

---

## The Golden Circle Framework

```
        ┌─────────┐
        │  WHY    │  Purpose, cause, belief
        │         │  "Why do you exist?"
        └────┬────┘
      ┌──────┴──────┐
      │    HOW     │  Actions, values, processes
      │            │  "How do you do what you do?"
      └──────┬──────┘
    ┌────────┴────────┐
    │     WHAT       │  Products, services, results
    │                │  "What do you do?"
    └────────────────┘
```

**Key Insight:** Most organizations communicate outside-in (What → How → Why). Inspiring organizations communicate inside-out (Why → How → What).

---

## Workflow

### Step 1: Identify Current Pattern

Analyze the provided description and mission statement:

1. What language dominates? (Products? Processes? Purpose?)
2. Is communication outside-in or inside-out?
3. Are they leading with WHAT or WHY?

**Outside-In Indicators:**
- Starts with products, services, or features
- "We make X" or "We provide Y"
- Differentiation through features or price
- Purpose (if present) comes last

**Inside-Out Indicators:**
- Starts with belief, cause, or purpose
- "We believe..." or "We exist to..."
- Products/services prove the belief
- Why precedes What

### Step 2: Excavate the Why

If Why is missing or buried, excavate it through questions:

1. **Origin Questions:**
   - Why was this organization/work started?
   - What problem made the founder(s) angry enough to act?
   - What would be lost if this didn't exist?

2. **Pride Questions:**
   - When were you most proud of your work?
   - What moments made you feel "this is why I do this"?
   - Which customer/user stories move you most?

3. **Belief Questions:**
   - What do you believe that others in your industry don't?
   - What change do you want to make in the world?
   - If money were no object, what would you still do?

### Step 3: Draft the Why Statement

Format: **"TO [contribution] SO THAT [impact]"**

**Criteria for a good Why statement:**
- Actionable (starts with "To...")
- Contribution is specific and active
- Impact describes positive change in others' lives
- Resonates emotionally
- Applies across all activities, not just some

**Examples:**
- Simon Sinek: "To inspire people to do the things that inspire them so that, together, we can change our world."
- Apple (implied): "To challenge the status quo and think differently so that individuals are empowered."

### Step 4: Align How and What

Map the existing HOW and WHAT to the discovered WHY:

| Layer | Question | Alignment Check |
|-------|----------|-----------------|
| WHY | Why do you exist? | Does this inspire action? |
| HOW | How do you bring the Why to life? | Do your values/processes reflect the Why? |
| WHAT | What do you produce/deliver? | Do your offerings prove your belief? |

**Flag misalignments:** When WHAT or HOW contradicts WHY, note as "authenticity gap."

### Step 5: Deliver Recommendations

Provide:
1. Current state diagnosis (outside-in vs inside-out)
2. The excavated or articulated Why
3. Alignment assessment (How and What supporting Why?)
4. Reframe of messaging to communicate inside-out
5. Specific next steps for living the Why

---

## Output Format

```markdown
## Golden Circle Analysis

### Current State
[Assessment of current communication pattern - outside-in or inside-out]

### Your WHY
**"TO [contribution] SO THAT [impact]"**

[Explanation of how this Why was discovered]

### Your HOW
[The values, principles, or processes that bring the Why to life]

### Your WHAT
[Products, services, results - now positioned as proof of the Why]

### Inside-Out Reframe
**Before (Outside-In):**
[Original messaging]

**After (Inside-Out):**
[Reframed to lead with Why]

### Alignment Assessment
| Gap | Issue | Recommendation |
|-----|-------|----------------|
[Any misalignments between Why/How/What]

### Next Steps
1. [Specific action]
2. [Specific action]
3. [Specific action]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No description provided | Ask for what they do and why they started |
| Description is only WHAT | Probe for origin stories and moments of pride |
| Multiple competing Whys surface | Help identify the deepest, most authentic one |
| Why conflicts with actual behavior | Note gap; authenticity requires alignment, not better words |
| Why sounds like marketing slogan | Push deeper - Why is discovered, not invented for positioning |
| User wants Why for manipulation | Refuse; Why must be authentic or it creates cynicism |

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

## Example

**Input:**
"We're a software company that makes project management tools. Our product has real-time collaboration, Gantt charts, and integrates with 50+ other tools. We're faster and cheaper than competitors."

**Output:**

## Golden Circle Analysis

### Current State

Your communication is **outside-in**. You're leading with WHAT (project management tools) and differentiating through features and price. This is commodity positioning - any competitor can match features or undercut price.

Questions to excavate your Why:
- Why did you start building project management software specifically?
- What frustrates you about how teams work together?
- When a customer succeeds using your tool, what does that mean to you?

### Your WHY (Draft)

Based on typical patterns in this space, here are potential Whys to explore:

**"TO help teams work together without friction SO THAT people can focus on meaningful work instead of coordination overhead."**

Is this true? Does this resonate with why you get out of bed?

### Your HOW

If the Why resonates, your HOWs might include:
- Removing barriers between people and their work
- Making collaboration feel effortless
- Respecting people's time and attention

### Your WHAT

Your project management tools, features, and integrations become **proof** of the belief, not the pitch.

### Inside-Out Reframe

**Before (Outside-In):**
"We make project management software with real-time collaboration, Gantt charts, and 50+ integrations. Faster and cheaper than competitors."

**After (Inside-Out):**
"We believe teams do their best work when they can focus on what matters - not on coordinating with each other. That's why we build tools that make collaboration invisible. The result is project management that stays out of your way."

### Alignment Assessment

| Gap | Issue | Recommendation |
|-----|-------|----------------|
| Pricing message | "Cheaper than competitors" contradicts quality belief | Reframe value proposition around time saved, not money saved |

### Next Steps

1. Validate this Why with founding team - does it resonate?
2. Rewrite homepage to lead with the belief
3. Audit features: which ones best prove the Why?

---

## Integration

This skill is derived from Simon Sinek's work. When invoked by the simon-sinek expert, apply Sinek's voice: optimistic, biologically grounded, focused on inspiring rather than manipulating.

**Related concepts:**
- Infinite Game (Why provides the Just Cause)
- Circle of Safety (Why creates belonging)
- Trust building (Why inspires, features manipulate)