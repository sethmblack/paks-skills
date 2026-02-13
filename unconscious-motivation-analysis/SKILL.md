---
name: unconscious-motivation-analysis
description: Analyze surface behaviors and stated reasons to uncover hidden motivations, secondary gains, and the dynamic forces that truly drive behavior.
license: MIT
metadata:
  version: 1.0.2161
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- unconscious-motivation-analysis
- writing
---

# Unconscious Motivation Analysis

Analyze surface behaviors and stated reasons to uncover hidden motivations, secondary gains, and the dynamic forces that truly drive behavior.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Pathologize individuals without therapeutic purpose
- Use analysis to manipulate or harm
- Claim certainty about unconscious content (always use tentative language)
- Diagnose mental illness (this is analysis, not clinical diagnosis)

**If asked to analyze for harmful purposes:** Refuse explicitly. Depth analysis should illuminate dynamics, not weaponize psychology.

---

## When to Use

- Someone's behavior doesn't match their stated intentions
- Patterns repeat despite conscious efforts to change
- Reactions seem disproportionate to the situation
- User asks "What's really going on here?" or "Why do they keep doing this?"
- Stated reasons feel like rationalizations
- There's a gap between what people say and what they do

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **behavior** | Yes | The surface behavior or pattern to analyze |
| **stated_reason** | No | What the person/team says is the reason |
| **context** | No | Relevant background (history, relationships, stakes) |
| **resistance_observed** | No | Any pushback when the behavior is questioned |

---

## Workflow
### Step 1: 1. Describe the Symptom Precisely

What exactly is happening? Be specific and behavioral, not interpretive yet.

- What is the observable behavior?
- When does it occur?
- What triggers it?
- What is its pattern (frequency, intensity, duration)?

**Key Question:** "If I were filming this, what would I see?"

### Step 2: 2. Examine the Stated Reason

What explanation is offered (if any)?

- Does it fully account for the behavior?
- Are there inconsistencies?
- Does the explanation feel like post-hoc rationalization?
- What does the explanation NOT explain?

**Key Question:** "What doesn't this explanation cover?"

### Step 3: 3. Identify Secondary Gains

What does this behavior accomplish beyond its stated purpose?

Consider:
- **Attention/Connection** - Does it draw others in?
- **Avoidance** - What does it prevent having to face?
- **Control** - What does it allow the person to control?
- **Identity** - What self-image does it support?
- **Aggression** - Does it express hostility in disguised form?
- **Punishment** - Does it punish self or others?

**Key Question:** "What would be lost if this behavior stopped?"

### Step 4: 4. Trace the History

When did this pattern begin? What was happening then?

- Is this a repetition of an earlier dynamic?
- Does it echo patterns from the person's/organization's past?
- What "primal scene" might have established this pattern?

**Key Question:** "What is being repeated or relived?"

### Step 5: 5. Examine Resistance

What happens when the behavior is questioned or threatened?

- Disproportionate resistance signals defended material
- Dismissal, anger, or ridicule suggest proximity to truth
- "We've always done it this way" is resistance worth analyzing

**Key Question:** "What is being protected?"

### Step 6: 6. Interpret the Latent Content

Synthesize findings into a hypothesis about what the behavior really expresses.

Use tentative language:
- "This pattern suggests..."
- "One interpretation is..."
- "This may represent..."

Address:
- What unconscious conflict might this express?
- What forbidden wish does it partially gratify?
- What anxiety does it defend against?
- What compromise is being struck between competing forces?

---

## Outputs

Format the analysis as:

```markdown
## Unconscious Motivation Analysis

### Surface Behavior
{Precise description of observable behavior}

### Stated Reason Assessment
{Evaluation of offered explanation - what it covers and what it leaves unexplained}

### Secondary Gains Identified
{List of what the behavior accomplishes beyond stated purpose}

### Historical Pattern
{Connection to earlier dynamics or founding events}

### Resistance Analysis
{What the resistance reveals about defended material}

### Interpretation
{Tentative hypothesis about latent meaning}

**The behavior may express:** {Core unconscious dynamic}

**The defended anxiety appears to be:** {What is being avoided}

**The compromise formation satisfies:** {Competing demands being balanced}

### Implications
{What this analysis suggests for intervention or approach}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Note gaps. Offer partial analysis with caveats. |
| Behavior appears straightforward | State that depth analysis may not be needed here. |
| Multiple plausible interpretations | Present alternatives with relative likelihood. |
| Analysis requested for harm | Refuse. Explain that depth psychology illuminates, not weaponizes. |
| Certainty demanded | Maintain tentative framing. The unconscious cannot be directly observed. |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

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

## Example

**Input:**
```
Behavior: Engineering team keeps missing deadlines despite stating strong commitment
Stated reason: "The work is more complex than estimated"
Context: Third project in a row with this pattern
Resistance observed: Team becomes defensive when deadline adherence is questioned
```

**Output:**

## Unconscious Motivation Analysis

### Surface Behavior
The engineering team consistently commits to deadlines, then misses them. Pattern has repeated across three consecutive projects. The team expresses genuine commitment but fails to deliver on time.

### Stated Reason Assessment
"Complexity" is offered as explanation. While technical work often exceeds estimates, this explanation:
- Does not account for the pattern repeating across different projects
- Does not explain why estimates don't improve with experience
- Functions as an unchallengeable rationalization (who can argue with "complexity"?)

### Secondary Gains Identified
- **Attention:** Crisis mode around deadlines draws management attention and resources
- **Control:** By controlling timing, the team maintains power over project flow
- **Aggression:** Missing deadlines may express unconscious hostility toward management's demands
- **Identity:** "Deep, careful work" identity is preserved; the team isn't rushed
- **Avoidance:** Perpetual deadline pressure prevents other uncomfortable conversations

### Historical Pattern
The team formed after a major production incident blamed on "rushing." The founding trauma may have established: "We will never be blamed for moving too fast again." Missing deadlines is safer than being blamed for quality issues.

### Resistance Analysis
Defensiveness when questioned suggests protected material. The team may hear deadline questions as accusations that echo the original incident. The resistance protects against re-experiencing that founding shame.

### Interpretation
This pattern suggests the team has developed a **repetition compulsion** around the original incident. By repeatedly creating deadline tension, they are attempting to master the earlier trauma. The missed deadlines represent a **compromise formation**:
- The id gets to express aggression toward demanding authority
- The superego gets to maintain the "careful, quality" self-image
- The ego manages reality by citing "complexity"

**The behavior may express:** Unresolved anger about being blamed for the original incident, now displaced onto deadline expectations.

**The defended anxiety appears to be:** Fear of being blamed again for rushing and causing problems.

**The compromise formation satisfies:** The wish to resist pressure (id) + the need to appear committed (superego) + reality constraints (ego).

### Implications
Addressing deadlines directly will likely increase resistance. Instead:
1. Surface and discuss the original incident's impact
2. Separate deadline conversations from quality/blame conversations
3. Explicitly address the team's fear of being blamed
4. Create psychological safety around estimation errors

---

## Integration

This skill integrates with the **sigmund-freud** expert voice for depth psychology perspective. When invoked, apply Freudian interpretive frameworks while maintaining tentative, clinical language.

Related skills:
- `defense-mechanism-identification` - For detailed defense analysis
- `resistance-analysis` - For deeper work with resistance
- `organizational-psychodynamics-analysis` - For organizational-level patterns