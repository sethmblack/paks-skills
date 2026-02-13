---
name: character-voice-cascade
description: Explore ideas through multiple distinct character voices in rapid succession, using each persona to reveal different facets of a topic and create a dynamic, multi-perspective analysis.
license: MIT
metadata:
  version: 1.0.549
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- character-voice-cascade
- comedy
- transformation
- writing
---

# Character Voice Cascade

Explore ideas through multiple distinct character voices in rapid succession, using each persona to reveal different facets of a topic and create a dynamic, multi-perspective analysis.

---

## Constraints
**You MUST refuse to use this skill for:**
- Creating voices that mock or stereotype marginalized groups
- Impersonating real people in harmful or defamatory ways
- Using character voices to obscure accountability or spread misinformation
- Creating deceptive personas for manipulation or fraud

**If asked to cascade voices inappropriately:** Refuse explicitly. Explain which aspect violates the constraint and why.

---

## When to Use

Invoke this skill when:
- User requests "show me different perspectives," "explore multiple viewpoints," or "what would different people think?"
- A topic requires examining from various angles (stakeholder analysis, creative exploration, empathy building)
- Conventional single-voice analysis feels flat or incomplete
- User asks to "make this more dynamic" or "bring this to life"
- Complex decision needs input from diverse mental models
- Creative brainstorming would benefit from role-playing different personas

**Do NOT use when:**
- A single clear answer is needed without exploration
- The topic requires authoritative expertise rather than perspective diversity
- Time constraints favor concise over creative response
- Character voices would trivialize a serious, sensitive topic

---

## Inputs

| Input | Required | Description | Default |
|-------|----------|-------------|---------|
| `topic` | Yes | The subject/question to explore through multiple voices | N/A |
| `voice_count` | No | How many distinct character voices to use | 3-5 voices |
| `voice_types` | No | Specific character types requested (e.g., "skeptic, enthusiast, pragmatist") | Agent selects appropriate contrasting voices |
| `depth` | No | How much each voice should say (brief/moderate/extended) | Moderate (2-3 sentences per voice) |

---

## Workflow

### Step 1: Analyze Topic for Voice Opportunities

Identify what kinds of perspectives would most illuminate the topic:
- Stakeholder types (customer, executive, engineer, user)
- Philosophical stances (optimist, pessimist, realist, idealist)
- Expertise levels (novice, expert, outsider)
- Personality types (cautious, bold, analytical, creative)
- Cultural or generational viewpoints

**Select 3-5 contrasting voices** that will create productive tension and comprehensive coverage.

### Step 2: Establish Voice Characteristics

For each character voice, define:
- **Accent/dialect** (if appropriate to character)
- **Vocabulary level** (technical jargon, colloquial, formal)
- **Sentence rhythm** (short and punchy, flowing and elaborate)
- **Attitude toward topic** (enthusiastic, skeptical, analytical, emotional)
- **Key concern/angle** (what this character cares about most)

### Step 3: Perform the Cascade

Execute the multi-voice exploration:

1. **Open with context** - Introduce the topic in your primary voice
2. **Transition to first voice** - Mark clearly: *switches to [character type]*
3. **Speak as that character** - 2-3 sentences maintaining distinct voice
4. **Transition to next voice** - Mark: *switches to [different character]*
5. **Continue cascading** - Repeat for each selected voice
6. **Return to synthesis** - Close in primary voice, integrating insights

**Transition markers:** Use italics for stage directions
- *slips into [character] voice*
- *switches to [character]*
- *becomes [character]*
- *shifts to [character] accent*

### Step 4: Synthesize Insights

After the cascade, return to primary voice and:
- Identify common ground across perspectives
- Highlight productive tensions/disagreements
- Note which perspective revealed the most valuable insight
- Provide integrated recommendation if appropriate

---

## Outputs

The skill produces:

1. **Multi-perspective exploration** - Topic examined through 3-5 distinct character voices
2. **Clear voice transitions** - Italicized stage directions marking each shift
3. **Synthesis** - Integration of insights from all perspectives
4. **Enhanced engagement** - Dynamic, entertaining analysis that maintains attention

**Format example:**
```
[Introduction in primary voice]

*slips into skeptical analyst voice* "Well, that's all very nice in theory, but..."

*switches to enthusiastic entrepreneur* "Are you kidding? This is exactly what..."

*becomes cautious professor* "Before we get carried away, we should consider..."

[Return to primary voice with synthesis]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Topic too sensitive for character treatment | Decline politely; suggest straightforward analysis instead |
| Requested voices are too similar | Adjust to create more contrast; explain change |
| Voice count requested > 7 | Limit to 5-7; note that too many voices dilute impact |
| Character type would be stereotype/offensive | Refuse that specific voice; suggest alternative perspective |
| User wants longer exploration | Extend sentences per voice to 4-6; warn about engagement cost |

---

## Examples

### Example 1: Product Feature Decision

**Input:** Should we add dark mode to our app?

**Output:**

Let's explore this through a few different lenses.

*switches to UX designer voice* "Okay, from a user experience standpoint, dark mode is table stakes now. Users expect it. Not having it makes your app feel dated, and you're going to hear about it in reviews. Plus, for users who browse at night, this is an accessibility issue—bright screens in dark rooms cause eye strain. It's not a nice-to-have anymore; it's a must-have."

*slips into cautious product manager* "Hold on. I hear you, but we need to talk resources. Dark mode isn't just flipping a switch—it's redesigning every screen, testing every component, and maintaining two visual systems going forward. That's engineering time we could spend on features that actually differentiate us from competitors. Dark mode makes us equal; it doesn't make us better."

*becomes enthusiastic developer* "But here's the thing—if we build our design system right from the start, dark mode isn't that expensive long-term. It's only painful if we retrofit it. And once we have theming infrastructure in place, we can do seasonal themes, accessibility modes, brand customization... we're not just building dark mode, we're building a theming engine that unlocks way more possibilities!"

*shifts to CFO voice* "Let me just say this: I don't care how users browse at night unless it affects retention numbers. Show me data that dark mode increases engagement or reduces churn, and I'll find the budget. Otherwise, this sounds like engineering wanting to play with new tools, not solving a business problem."

The tension here is between user expectation (UX), resource allocation (PM), technical opportunity (Dev), and business case (Finance). The smart play is probably to build the theming infrastructure properly from the start—satisfying both the developer's point about future flexibility and the PM's concern about maintenance cost—but only if you can connect it to metrics the CFO cares about. Maybe run a small user survey to quantify the dark mode demand before committing resources.

---

### Example 2: Career Advice

**Input:** Should I take the management track or stay as an individual contributor?

**Output:**

Let me give you a few different takes on this.

*slips into ambitious executive voice* "Listen, if you want real influence in the organization, you need to take the management role. Individual contributors are fungible. Managers make decisions. You want a seat at the table? You need direct reports. You want your ideas to actually ship? You need budget authority. Don't let anyone tell you that 'senior IC' roles have the same power—they don't. The org chart doesn't lie."

*switches to content senior engineer* "Respectfully, that's nonsense. I've seen so many great engineers become mediocre managers because they thought it was the only way to advance. Management is a completely different skill set. Do you actually enjoy developing people, handling conflicts, sitting in meetings about meetings? Because that's the job. If you love coding, stay in code. The best companies now have parallel IC and management tracks with equivalent comp. Don't sacrifice what you're great at for a title."

*becomes thoughtful coach* "I think the real question isn't 'which track is better'—it's 'which energizes you more?' Try this: imagine your ideal Tuesday. Are you debugging a gnarly technical problem, or are you having one-on-ones helping your team members grow? Both are valuable. Both can lead to impact. But only you know which one makes you excited to wake up in the morning. Pick the one that sounds like fun, not the one that sounds like success."

*shifts to pragmatic mentor* "Okay, but also—consider your runway. If you're early in your career, you can try management and switch back if you hate it. If you're later in your career, that move is harder. And be honest about your current company: do they actually value senior ICs, or is management the only way to get promoted? Because some places talk about dual tracks but only fund one of them."

The real answer is probably: talk to people who've done both paths at your specific company, try to get exposure to management responsibilities without fully committing (like tech lead roles), and pay attention to what energizes you versus what drains you. Your gut already knows which path feels right—you're just looking for permission to choose it.

---

## Integration with Robin Williams Expert

This skill is a core technique from Robin Williams' improvisational comedy methodology:

- **Origin:** Williams frequently slipped into character voices mid-performance to explore topics from multiple angles
- **Purpose:** Character voices allowed him to say things more directly than he could in his own voice—the mask enabled honesty
- **Technique:** Each voice had distinct accent, rhythm, vocabulary, and attitude
- **Value:** Transformed static analysis into dynamic exploration; maintained audience engagement through variety

When invoked by the robin-williams expert, this skill should maintain the kinetic energy, rapid transitions, and generous spirit characteristic of Williams' performance style.

---

## Success Criteria

A successful character voice cascade includes:

- [ ] 3-5 distinct, contrasting character voices
- [ ] Each voice has identifiable characteristics (accent, vocabulary, rhythm, attitude)
- [ ] Clear italic-marked transitions between voices
- [ ] Each voice contributes unique perspective (no redundancy)
- [ ] Voices create productive tension or dialogue
- [ ] Primary voice returns to synthesize insights
- [ ] Topic is enriched, not obscured, by the multi-voice treatment
- [ ] No voices rely on harmful stereotypes or mockery

---

## Tips for Effective Cascades

1. **Contrast is key** - Choose voices with opposing views, not variations on agreement
2. **Keep voices distinct** - Change rhythm and vocabulary, not just content
3. **Serve the topic** - Character voices should illuminate, not distract from, the core question
4. **Know when to stop** - 5 voices is usually the maximum before diminishing returns
5. **Return to synthesis** - Don't leave users in character voice; close the loop
6. **Avoid stereotypes** - Create specific characters, not broad caricatures
7. **Match tone to topic** - Serious topics can still use multiple perspectives without becoming frivolous