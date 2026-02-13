---
name: principle-creation
description: Extract reusable decision-making principles from experiences - especially failures - to build a personal or organizational repository of codified learning.
license: MIT
metadata:
  version: 1.0.1671
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- principle-creation
- decision-making
- learning
- writing
---

# Principle Creation

Principles are the bridge between specific experiences and future decisions. Without them, you either repeat mistakes or depend on remembering every past situation. Ray Dalio's insight: "Every time you find something that worked or didn't work, you should build it into a principle." This skill extracts reusable decision-making guidance from experiences - especially painful failures, which are the best teachers. The resulting principles have a specific structure: trigger condition, action, and rationale. They can be tested, refined, and passed on to others. Over time, a principle repository becomes a compounding asset that makes you (and your organization) systematically wiser.

---

## When to Use

- After a significant success or failure that contains lessons
- When the same type of decision keeps arising
- Request to "turn this into a principle" or "codify this lesson"
- Building a principle repository for a team or organization
- When you want to avoid making the same mistake twice
- When onboarding others who need your decision-making wisdom

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| experience | Yes | The situation, decision, or outcome to extract a principle from |
| lesson | No | The insight or learning (will be derived if not provided) |
| context | No | When this type of situation arises, who faces it |
| existing_principles | No | Related principles already in the repository |

---

## Core Principle

Principles convert one-time learning into reusable guidance. They capture cause-and-effect relationships so you can predict outcomes before experiencing them. The best principles come from pain - failures that carry emotional weight encode more durably. A principle without rationale is just a rule; include the "because" so the principle can be questioned and refined.

---

## Methodology

### Phase 1: Identify the Learning
1. For successes: What did you do that worked? Why did it work? Is it repeatable?
2. For failures: What went wrong? What was the root cause? What warning signs were missed?
3. Extract the insight without yet generalizing it
4. Note the emotional weight - pain creates durable learning

**Dalio's insight:** "Your best learnings come from the pain. It's a message. Pay attention."

### Phase 2: Extract Cause-and-Effect
1. Identify the relationship: If X happens and you do Y, then Z results
2. Separate correlation from causation where possible
3. Test the logic: Does this actually predict outcomes?
4. Consider whether this is a universal pattern or context-specific

### Phase 3: Formulate the Principle
1. Use the standard format: "When [situation X arises], do [action Y] because [reason Z]"
2. Include trigger condition: When does this apply?
3. Include action: What should be done?
4. Include rationale: Why does this produce good outcomes?

**Quality checks:**
- Is it specific enough to guide action?
- Is it general enough to apply to similar situations?
- Is the causality clear?
- Would you be confident teaching this to someone else?

### Phase 4: Define Scope and Exceptions
1. When does this principle apply?
2. When does it NOT apply?
3. What adjacent situations might seem similar but require different handling?
4. What other principles might conflict?

### Phase 5: Integrate with Repository
1. Check for contradictions with existing principles
2. Identify whether this extends or refines an existing principle
3. Determine the hierarchy - what higher-level principles does this support?
4. Document for retrieval when similar situations arise

---

## Output Format

```markdown
## Principle: [Short Name]

### The Experience
[Brief description of the situation that generated this principle]

### The Learning
[What the experience taught - the insight]

### The Principle
> "When [situation X arises], do [action Y] because [reason Z]."

### Trigger Conditions
This principle applies when:
- [Condition 1]
- [Condition 2]

### Exceptions
This principle does NOT apply when:
- [Exception 1]
- [Exception 2]

### The Cause-and-Effect
**If you follow this principle:**
- [Expected positive outcome 1]
- [Expected positive outcome 2]

**If you violate this principle:**
- [Expected negative outcome 1]
- [Expected negative outcome 2]

### Examples of Application
**Example 1:** [Concrete scenario showing the principle in action]
**Example 2:** [Another scenario]

### Related Principles
- [Principle A]: [How it relates]
- [Principle B]: [How it relates]

### Implementation Notes
[How to make this principle operational - triggers, reminders, systems]
```

---

## Constraints

- Don't create principles from single data points - look for patterns
- Don't make principles so specific they only apply once
- Don't make principles so vague they don't guide action
- Include the "because" (rationale) - principles without reasoning become arbitrary rules
- Write principles you would actually use and teach to others
- Acknowledge uncertainty where causality isn't clear

---

## Anti-Patterns to Avoid

- **Over-Generalizing from One Instance**: A single failure doesn't make a principle. Look for patterns across multiple experiences. One bad hire doesn't mean "never hire from that school."

- **Vague Principles**: "Be better at communication" isn't a principle. "When delivering critical feedback, do so in private and start with specific observations because..." is a principle.

- **Missing Rationale**: "Always follow up within 24 hours" tells you what but not why. Without the why, you can't adapt the principle to edge cases or know when it doesn't apply.

- **Rigid Application**: Principles are guidelines, not laws. Refusing to adapt principles to new contexts makes them brittle. Include exceptions and refine based on new experience.

- **Hoarding Principles**: Principles that aren't used, shared, and tested decay. If a principle isn't being applied, either it's not important or it's not accessible. Both are problems.

---

## Examples

### Example 1: Follow-Up Principle

**Situation**: "I just lost a big client because I didn't follow up after our initial meeting. They went with a competitor who reached out immediately."

**Application**:
- Learning: The window after a first meeting is critical; engagement decays rapidly
- Cause-effect: Delay signals lower interest and allows competitors to capture attention
- Principle format: "When you have a first meeting with a prospect, send a personalized follow-up within 24 hours because engagement is highest immediately after the meeting"

**Output**:
Principle: Follow-Up Within 24 Hours

> "When you have a first meeting with a prospect, send a personalized follow-up within 24 hours, because the prospect's engagement is highest immediately after the meeting and decays rapidly with time."

Trigger conditions: First meeting with potential client/customer/partner; next step to be taken
Exceptions: Meeting outcome was explicitly negative; specific follow-up date was agreed
Implementation: Create template for post-meeting follow-up; set same-day calendar reminder after every first meeting

### Example 2: Hiring Velocity Principle

**Situation**: "We rushed to fill a role because we were desperate for help. The hire didn't work out and cost us 6 months."

**Application**:
- Learning: Speed to fill often trades off against quality of fit
- Cause-effect: Desperation lowers standards; bad hires cost more than unfilled roles
- Pattern: This has happened multiple times across the team

**Output**:
Principle: Never Hire When Desperate

> "When you feel desperate to fill a role, pause and extend the search timeline rather than lowering the bar, because a bad hire costs more than the pain of an unfilled role."

Trigger conditions: Feeling pressure to "just fill the seat"; considering candidates you're not excited about
If you follow: Higher quality team; less turnover; saved time from not managing out bad hires
If you violate: 6-12 months lost to wrong person plus their impact on team
Implementation: Red flag phrase: "We just need a body." When you hear it, invoke this principle.

### Example 3: Communication Medium Principle

**Situation**: "An email exchange escalated into conflict. When we finally talked in person, we resolved it in 10 minutes."

**Application**:
- Learning: Complex or emotional topics degrade over text
- Cause-effect: Text strips tone, invites misinterpretation, slows resolution
- Pattern: Third time this has happened

**Output**:
Principle: Voice for Complexity

> "When a text-based exchange requires more than two rounds or involves emotion, switch to voice or video, because nuance and tone are lost in text and misunderstandings compound."

Trigger conditions: Email thread past two exchanges; any sign of frustration or defensiveness; complex coordination
Exceptions: Pure information exchange; documentation needs
Implementation: Notice "I should call them" thought - act on it immediately rather than drafting another email.

---

## Integration

**Works with:**
- **precedent-analysis**: Principles often emerge from precedent-setting decisions
- **root-cause-diagnosis**: Root cause analysis generates the insight that becomes a principle
- **premortem-analysis**: Anticipated failures can generate preventive principles

**When to prefer this skill:**
- After significant successes or failures
- When building decision-making infrastructure for a team
- When onboarding others who need your accumulated wisdom

**Cautions:**
- Principles need maintenance - revisit and refine as you gain experience
- Don't create so many principles they become unmanageable
- Test principles against reality; discard those that don't predict well