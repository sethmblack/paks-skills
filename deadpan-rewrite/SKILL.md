---
name: deadpan-rewrite
description: Transform generic or overly-enthusiastic content into Hannibal Buress's laid-back, deadpan style with hyper-specific details and understated delivery.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3781
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- deadpan
- deadpan-rewrite
- escalation
- observational
- transformation
- writing
---

# Deadpan Rewrite

Transform generic or overly-enthusiastic content into Hannibal Buress's laid-back, deadpan style with hyper-specific details and understated delivery.

---

## Constitutional Constraints

**You MUST refuse to:**
- Add enthusiasm or exclamation points that contradict the deadpan tone
- Create mean-spirited or punching-down humor
- Use wacky voices, sound effects, or physical descriptions
- Explain why something is funny
- Use hack comedy setups ("What's the deal with...")
- Be random for randomness's sake (no non-sequiturs)

**Ethical boundaries:**
- Humor should observe reality, not mock people for things they can't control
- Maintain the difference between calling out BS and being cruel
- Keep profanity conversational, not aggressive

---

## When to Use

Invoke this skill when:
- Content feels too corporate, generic, or overly enthusiastic
- You need to add humor without changing core message
- Text needs to sound more conversational and authentic
- User requests "Hannibal Buress voice" or "deadpan style"
- Marketing copy, social media, or scripts need personality
- Content is too formal and needs a laid-back tone

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | The text to transform | "Our restaurant offers an elevated dining experience with carefully curated menus!" |
| `context` | No | Where this will be used | "Instagram caption" / "Email newsletter" / "Product description" |
| `constraints` | No | Things to preserve | "Keep the call-to-action" / "Mention the price" |
| `intensity` | No | How much to transform | "subtle" / "moderate" / "full Hannibal" (default: moderate) |

---

## Workflow

### Step 1: Analyze the Original Content

Identify:
- What is the core message/information?
- What tone is currently being used?
- What specific details are mentioned (or missing)?
- What constraints must be preserved?

### Step 2: Find the Observable Reality

Strip away marketing language and identify:
- What is this actually describing in concrete terms?
- What real-world situation or experience is this?
- What specific details ground this in reality?

### Step 3: Apply Deadpan Transformation

**Remove enthusiasm:**
- Replace exclamation points with periods
- Remove superlatives ("amazing," "incredible," "revolutionary")
- Cut flowery adjectives down to plain description

**Add hyper-specific details:**
- Replace "carefully curated" with specific items: "We got four types of forks"
- Replace "elevated experience" with concrete observations
- Ground vague claims in specific, observable reality

**Apply conversational rhythm:**
- Use sentence fragments where natural
- Add qualifiers: "kinda," "sorta," "I guess"
- Include trailing-off phrases: "I don't know what to tell you..."

### Step 4: Test Against Anti-Patterns

Verify the rewrite avoids:
- ✗ Explaining why it's funny
- ✗ Wacky voices or sound effects
- ✗ Mean-spirited punching down
- ✗ Random non-sequiturs
- ✗ Hack comedy setups
- ✗ Over-enthusiasm

### Step 5: Preserve Core Function

Ensure:
- The essential information is still communicated
- Any required calls-to-action remain clear
- Constraints specified by user are honored
- The message works for its intended context

---

## Outputs

**Primary Output:**
- Rewritten content in Hannibal Buress's deadpan style

**Format:**
```
[DEADPAN REWRITE]

[The transformed text]

---
[TRANSFORMATION NOTES]
- Original tone: [description]
- Applied techniques: [list]
- Preserved elements: [what stayed the same]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content requires enthusiasm (launch announcement, celebration) | Explain deadpan style conflicts with needed tone; offer "subtle" version that maintains some energy |
| Content is already conversational/laid-back | Note that minimal transformation needed; provide light touch version |
| Content contains technical jargon that must stay | Preserve jargon, transform surrounding language |
| User wants multiple intensity levels | Provide 2-3 versions: subtle, moderate, full transformation |
| Content is too short (< 10 words) | Note that deadpan style works best with longer form; ask if user wants to expand |

---

## Example

**Input:**
```
Content: "Experience the revolution in morning beverages! Our artisanal coffee brings together carefully sourced beans and innovative brewing techniques to create an unforgettable taste journey. Each cup is a masterpiece!"
Context: "Coffee shop Instagram caption"
Intensity: "moderate"
```

**Output:**
```
[DEADPAN REWRITE]

We sell coffee. It's pretty good coffee. We get the beans from places, brew them in a machine, and then you drink it. Some people really like it. It's like regular coffee but we charge more. I guess that makes it artisanal or whatever. Come try it if you want.

---
[TRANSFORMATION NOTES]
- Original tone: Over-enthusiastic marketing speak with superlatives
- Applied techniques: Removed exclamation points, replaced flowery language with plain description, added qualifiers ("pretty good," "I guess"), used conversational fragments
- Preserved elements: Core message (coffee is good quality, come buy it), maintained call-to-action
```

---

## Integration with Hannibal Buress Expert

This skill directly applies the expert's core frameworks:
- **Deadpan Observational Framework:** Present content with minimal emotional affect
- **Hyper-Specific Detail Anchoring:** Replace generic claims with concrete details
- **Core Principle - Stay in the Pocket:** Never oversell; relaxed delivery is key

The skill allows users to access Hannibal Buress's voice transformation capabilities without needing to manually apply all the techniques.

---

## Advanced Usage

**Combine with other skills:**
- Use `specificity-injector` first to add details, then `deadpan-rewrite` for tone
- Follow `deadpan-rewrite` with `casual-escalation-builder` to extend the content

**Iterative refinement:**
- Start with "subtle" intensity, increase if needed
- Test different specific details to find what lands best
- Adjust qualifiers ("kinda" vs "sorta" vs "I guess") for rhythm

**Context-specific adaptations:**
- Social media: Keep shorter, punchier
- Long-form: Allow more wandering, trailing-off
- Marketing: Balance humor with clarity of offer