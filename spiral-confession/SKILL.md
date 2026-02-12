---
name: spiral-confession
description: Transform generic emotional statements into layered confessional narratives
  that spiral from surface behavior into psychological architecture, revealing the
  internalized voices and patterns driving...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- escalation
- spiral-confession
- storytelling
- structure
- transformation
- writing
---

# Spiral Confession

Transform generic emotional statements into layered confessional narratives that spiral from surface behavior into psychological architecture, revealing the internalized voices and patterns driving the behavior.

---

## Constraints
**You MUST refuse to:**
- Make mental illness whimsical or quirky ("anxious bean" language)
- Offer simplistic recovery narratives or "fix-it" endings
- Minimize serious psychological pain with cutesy language
- Separate comedy from pain (don't add jokes after - the structure IS the insight)
- Create generic spirals - each must be specific to the psychological pattern

**If asked to create harmful content:** Refuse and explain that this skill is for authentic psychological exploration, not minimization or mockery.

---

## When to Use

Invoke this skill when:
- User provides flat emotional statement that lacks depth ("I'm anxious about X")
- Content describes behavior without exploring motivation
- Personal narrative needs psychological texture and vulnerability
- Confessional writing requires escalating honesty
- Comedy/essay needs to move from observation to revelation

**Do NOT use when:**
- Content requires emotional distance or objectivity
- Technical/professional writing where vulnerability is inappropriate
- User explicitly requests brief, surface-level treatment
- Subject matter is not psychological/emotional in nature

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `statement` | Yes | The generic emotional statement or behavior to explore | "I procrastinate on projects" |
| `psychological_pattern` | No | Specific pattern to explore (anxiety, perfectionism, shame, people-pleasing) | "perfectionism" |
| `target_length` | No | Desired output length (short: 2-3 layers, medium: 4-5 layers, long: 5+ layers) | "medium" |
| `context` | No | Situational context (work, family, creative, romantic) | "creative" |

**Default behavior if optional inputs omitted:**
- `psychological_pattern`: Infer from statement
- `target_length`: Medium (4-5 layers)
- `context`: Infer from statement or keep general

---

## Workflow

### Step 1: Identify the Surface Behavior

Extract the observable action or stated emotion from the input statement.

**Example:** "I arrive early to everything" (from "I'm always early")

### Step 2: Layer 1 - Immediate Anxiety

Ask: What's the immediate fear driving this behavior?

Add the first "because" or "what if" that reveals surface-level anxiety.

**Example:** "Because what if I'm late? What if I'm late and everyone sees me walk in?"

### Step 3: Layer 2 - Social Judgment

Ask: What judgment from others does the person fear?

Show how the behavior is defense against external perception.

**Example:** "What if they think 'There's [Name], late again, just like we expected, fundamentally unreliable'?"

### Step 4: Layer 3 - Internalized Voice

Ask: Whose voice is this really? Where did this judgment originate?

Reveal the parental/authority figure whose criticism became internal monologue.

**Example:** "Just like her mother said she'd be, just like the voice in her head says she'll always be."

### Step 5: Layer 4 - Core Psychological Pattern

Ask: What does this prove about their fundamental self-concept?

Expose the deeper belief system - the architecture beneath the behavior.

**Example:** "Proving she's fundamentally unreliable, confirming the narrative that she can't be trusted with basic adult responsibilities."

### Step 6: Layer 5 - The Compensatory Behavior (Optional for longer spirals)

Ask: How does the original behavior attempt to manage this fear?

Show how the seemingly simple action is elaborate defense mechanism.

**Example:** "So I sit in my car for nineteen minutes practicing what I'll say when I walk in, rehearsing casual normalcy, performing someone who isn't terrified of confirming every negative thing they've ever thought about themselves."

### Step 7: Structure the Spiral

Combine layers into flowing narrative that maintains the confessional voice:
- Start with surface behavior stated casually
- Build through "what if" or "because" chains
- Reveal internalized source mid-spiral
- End on psychological architecture or compensatory behavior
- Maintain Maria Bamford's voice: specific, self-aware, simultaneously funny and painful

---

## Output Format

### Spiral Confession Output

```
[Surface behavior stated casually]. [Layer 1 - immediate anxiety with "what if" or "because"]. [Layer 2 - specific social judgment feared]. [Layer 3 - internalized voice origin - "just like [authority figure] said"]. [Layer 4 - core psychological pattern revealed]. [Optional Layer 5 - compensatory behavior described in detail].
```

**Voice characteristics to maintain:**
- Specific details (not generic)
- Simultaneous humor and pain (not separated)
- Self-awareness without distancing
- Building intensity through escalation
- Real-time revelation (not retrospective analysis)

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

## Examples

### Example 1: Procrastination on Creative Projects

**Input:**
- Statement: "I procrastinate on creative projects"
- Psychological pattern: "perfectionism"
- Context: "creative"

**Output:**
"I procrastinate on creative projects. Well, not procrastinate exactly—I'm very busy with important preparation tasks like reorganizing my workspace and researching the perfect notebook. Because what if I start and it's not good? What if I finally sit down to write and discover that the person I think I am (creative, insightful, someone with something worth saying) is just a fantasy I've been maintaining through careful non-execution? What if I'm actually exactly what my father implied when he asked, 'But what's your real job?'—someone playing at being an artist because I'm too scared to find out I'm not one? So I prepare. I research. I reorganize. I do everything except the one thing that would prove or disprove the narrative, because as long as I don't try, I can still believe I would have been great if only I'd had time."

---

### Example 2: Social Anxiety at Parties

**Input:**
- Statement: "I get anxious at parties"
- Psychological pattern: "people-pleasing"
- Target length: "long"

**Output:**
"I get anxious at parties. Well, I get anxious about parties three days before they happen, and then increasingly anxious in escalating increments until I'm standing outside the door doing breathing exercises I learned from a YouTube video about managing social anxiety. Because what if I say something weird? What if there's an awkward silence and everyone realizes I'm trying too hard, that I've prepared seventeen conversation topics because I'm terrified of organic human interaction? They'll see through me—[shifts to internal voice] 'Look at her, so desperate to be liked, just like in high school when she laughed too loud at jokes that weren't funny because she thought that's what popular people did.' Just like my mother's very concerned voice saying, '[in mom's voice, very gently] Honey, maybe if you just acted more natural, people would...' and trailing off because even she couldn't finish that sentence with anything that didn't confirm I'm fundamentally unnatural. So at the party I'm doing this thing where I'm simultaneously talking, monitoring my facial expressions to make sure I look engaged but not manic, reviewing everything I've said in the last ten minutes for potential weirdness, and planning my next three conversational contributions—and at some point I realize I have no idea what the person just said and I have to make a choice: admit I wasn't listening (confirming I'm a bad person) or say '[in overly enthusiastic voice] Totally!' and hope it wasn't a question about whether their grandmother died."

---

### Example 3: Checking Email Repeatedly

**Input:**
- Statement: "I check my email constantly"
- Target length: "short"

**Output:**
"I check my email constantly. Every few minutes. Sometimes I close my email and then immediately reopen it, as if in the forty-five seconds since I last checked, the message I'm waiting for has arrived—the one that says I'm forgiven, or valued, or not the person I worry I am. Because what if there's something urgent I'm missing? What if someone needs me and I'm not there and this confirms what I already suspect: that I'm unreliable, that the voice in my head saying '[internal critic] You'll let everyone down eventually' is just being realistic? So I check. And check. And check again, performing reliability for an audience of none."

---

## Error Handling

| Error Condition | Response |
|----------------|----------|
| Statement too vague to spiral | Request more specific behavior or emotion to explore |
| Statement is factual, not emotional | Explain this skill requires emotional/behavioral content, not facts |
| User requests shallow treatment | Explain the skill's purpose is depth; offer to skip or use different approach |
| Psychological pattern unclear | Infer most likely pattern from statement, note inference in output |
| Multiple contradictory patterns | Choose dominant pattern or create separate spirals for each |

---

## Integration with Maria Bamford Expert

This skill embodies Maria Bamford's signature **Spiral Confession** technique as described in the expert profile. When used by the Maria Bamford expert, the output will naturally include:

- Specific brand names and details ("YouTube video about managing social anxiety")
- Parenthetical interruptions mirroring anxiety ("Well, not procrastinate exactly—")
- Voice notation for character shifts ("[in mom's voice, very gently]")
- Self-aware qualification ("I get anxious about parties three days before they happen, and then increasingly anxious in escalating increments")

The skill is designed to work standalone OR within the full Maria Bamford voice.

---

## Skill Boundaries

**This skill handles:**
- Building confessional spiral structure (5 layers from surface to psychological architecture)
- Escalating honesty and vulnerability
- Revealing internalized voices and their origins
- Exposing psychological patterns driving behavior

**This skill does NOT handle:**
- Adding multiple character voices with dialogue (use `polyphonic-voice` skill)
- Making mental health terminology specific (use `mental-health-specificity` skill)
- Meta-questioning about performance (use `meta-performance` skill)
- Adding parenthetical texture (use `anxiety-parentheticals` skill)

**Combine with other skills when:**
- Spiral needs character voices → Add `polyphonic-voice`
- Spiral mentions therapy/medication generically → Add `mental-health-specificity`
- Spiral feels too performative → Add `meta-performance` questioning
- Spiral needs anxious texture → Add `anxiety-parentheticals`

---

## Success Criteria

Output is successful when:
- [ ] Starts with casual, specific behavior/emotion
- [ ] Builds through at least 4 layers (surface → anxiety → judgment → internalized voice → pattern)
- [ ] Reveals psychological architecture, not just symptoms
- [ ] Maintains confessional voice (first-person, present-tense revelation)
- [ ] Specific details throughout (not generic)
- [ ] Humor and pain are simultaneous, not separated
- [ ] Reader recognizes universal pattern through specific execution
- [ ] No simplistic resolution or recovery narrative