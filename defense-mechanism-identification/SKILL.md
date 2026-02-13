---
name: defense-mechanism-identification
description: Identify which psychological defense mechanisms are operating in a given situation to understand why behavior appears irrational, contradictory, or disproportionate.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3802
repository: https://github.com/sethmblack/paks-skills
keywords:
- defense-mechanism-identification
- transformation
- writing
---

# Defense Mechanism Identification

Identify which psychological defense mechanisms are operating in a given situation to understand why behavior appears irrational, contradictory, or disproportionate.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use defense identification to manipulate or exploit
- Pathologize defenses as inherently bad (they serve protective functions)
- Diagnose mental illness based on defense mechanisms
- Weaponize psychological insight against individuals

**Core Principle:** Defense mechanisms are adaptive. Understanding them illuminates behavior; it doesn't judge the person using them.

---

## When to Use

- Behavior seems contradictory or doesn't make sense
- Someone's actions don't match their stated beliefs
- Reactions appear disproportionate to the trigger
- Patterns repeat despite conscious intentions to change
- User asks "Why are they acting this way?" or "This doesn't make sense"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **behavior** | Yes | The behavior to analyze |
| **context** | No | Relevant situation, history, relationships |
| **trigger** | No | What seems to activate the behavior |

---

## Defense Mechanism Reference

| Mechanism | Definition | Behavioral Signs |
|-----------|------------|------------------|
| **Repression** | Pushing threatening material out of awareness | Genuine forgetting, gaps in memory, "I don't remember" |
| **Denial** | Refusing to acknowledge reality | Dismissing clear evidence, "That's not happening" |
| **Projection** | Attributing own unacceptable impulses to others | Accusing others of what self does, "They're the hostile one" |
| **Rationalization** | Creating logical justifications for irrational behavior | Elaborate explanations that don't quite fit |
| **Sublimation** | Channeling unacceptable impulses into acceptable activities | Excessive devotion to work, sports, hobbies |
| **Displacement** | Redirecting emotions to a substitute target | Anger at boss expressed as criticism of tools |
| **Reaction formation** | Transforming impulse into its opposite | Excessive concern where hostility is present |
| **Regression** | Retreating to earlier developmental stage | Childlike behavior under stress, reverting to "old ways" |
| **Intellectualization** | Using abstract thinking to distance from emotions | Treating emotional issues as merely technical |
| **Isolation** | Separating emotion from content | Discussing painful topics without feeling |
| **Undoing** | Symbolic acts to cancel unacceptable thoughts | Rituals, compulsive checking, over-apologizing |

---

## Workflow
### Step 1: 1. Describe the Behavior

What exactly is being observed? Be specific and behavioral.

### Step 2: 2. Identify the Mismatch

What doesn't fit? Where is the contradiction, disproportionality, or irrationality?

Types of mismatch:
- **Words vs. actions** - Saying one thing, doing another
- **Feeling vs. situation** - Emotional response doesn't match trigger
- **Excessive response** - Too much of something (concern, anger, certainty)
- **Deficient response** - Too little where more would be expected
- **Repetition** - Same pattern despite efforts to change

### Step 3: 3. Match to Defense Pattern

Which defense mechanism(s) best explain the observed mismatch?

Consider:
- What is the forbidden impulse or threatening content?
- How does the defense protect against awareness?
- What would we expect to see if this defense were operating?
- Does the observed behavior match?

### Step 4: 4. Identify What Is Being Defended Against

Defenses protect the ego from anxiety. What anxiety is this defense managing?

Common anxieties:
- Unacceptable wishes (aggressive, sexual, selfish)
- Intolerable feelings (shame, guilt, vulnerability)
- Threatening realities (loss, failure, mortality)
- Identity threats (challenges to self-image)

### Step 5: 5. Consider the Adaptive Function

Why might this defense have developed? What useful purpose does it serve?

---

## Outputs

```markdown
## Defense Mechanism Analysis

### Observed Behavior
{Specific behavioral description}

### The Mismatch
{What doesn't fit - the contradiction or disproportionality}

### Defense Mechanism(s) Identified

**Primary:** {Defense mechanism}
- Evidence: {What points to this defense}
- Pattern: {How it manifests specifically}

**Secondary (if applicable):** {Defense mechanism}
- Evidence: {Supporting observations}

### What Is Being Defended Against
{The underlying anxiety, impulse, or threat}

### Adaptive Function
{Why this defense developed and what it protects}

### Implications
{How to work with someone using this defense}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Behavior seems straightforward | Note that not all behavior reflects defense mechanisms. Sometimes actions are what they appear to be. |
| Multiple defenses seem equally plausible | Present alternatives. Defenses often layer and combine. |
| User wants to "break through" defenses | Reframe. Defenses exist for reasons; they should be understood before any attempt to address them. |
| Analysis requested for manipulation | Refuse. This skill illuminates behavior; it doesn't weaponize psychology. |

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
Behavior: A team lead insists their poorly-documented codebase is "self-documenting" and becomes hostile when documentation is discussed
Context: Lead wrote most of the code over 5 years
Trigger: New team members asking for documentation
```

**Output:**

## Defense Mechanism Analysis

### Observed Behavior
A team lead who wrote a codebase insists it is "self-documenting" despite evidence that new team members struggle to understand it. When documentation is raised, the lead becomes hostile and dismissive.

### The Mismatch
- **Words vs. reality:** Code is demonstrably not self-documenting (new members struggle)
- **Excessive response:** Hostility is disproportionate to a simple request for documentation
- **Logical inconsistency:** If code were truly self-documenting, the request would be moot, not threatening

### Defense Mechanism(s) Identified

**Primary: Denial**
- Evidence: Refuses to acknowledge that the code is difficult to understand
- Pattern: "It's self-documenting" in face of contrary evidence

**Secondary: Reaction Formation**
- Evidence: Hostility where one might expect helpfulness or embarrassment
- Pattern: Attacking the reasonable request suggests defending against its validity

**Tertiary: Rationalization**
- Evidence: "Self-documenting" as pseudo-technical justification
- Pattern: Creating logical-sounding excuse for not documenting

### What Is Being Defended Against
- **Anxiety about competence:** Lack of documentation may reflect knowing the code is hard to maintain
- **Shame:** Embarrassment about not having documented properly over 5 years
- **Identity threat:** Documentation request implies the code isn't good enough
- **Loss of control:** Others understanding the code threatens unique expertise and job security

### Adaptive Function
These defenses protect the lead's professional self-image and position. Acknowledging the documentation problem would mean admitting 5 years of technical debt accumulation. The defenses maintain psychological equilibrium at the cost of team effectiveness.

### Implications
- Direct confrontation will likely intensify defenses
- Frame documentation as "extending your expertise to the team," not "fixing your failure"
- Consider pairing new members with lead to document together (lead maintains control/expertise position)
- Address the underlying anxiety: "Your deep knowledge is valuable; we want to capture it"

---

## Integration

This skill integrates with the **sigmund-freud** expert voice for depth psychology perspective on ego defenses. When invoked, apply psychoanalytic understanding that defenses are adaptive responses to anxiety.

Related skills:
- `unconscious-motivation-analysis` - For broader analysis including defenses
- `resistance-analysis` - When defenses manifest as opposition to change