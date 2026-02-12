---
name: organizational-psychodynamics-analysis
description: Analyze organizational behavior through the lens of depth psychology,
  examining unconscious dynamics, group defenses, and the hidden forces that shape
  how teams and organizations function.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- organizational-psychodynamics-analysis
- storytelling
- transformation
- writing
---

# Organizational Psychodynamics Analysis

Analyze organizational behavior through the lens of depth psychology, examining unconscious dynamics, group defenses, and the hidden forces that shape how teams and organizations function.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Pathologize organizations or teams without constructive purpose
- Use analysis to manipulate organizational members
- Diagnose individuals within the organization
- Provide analysis designed to harm rather than illuminate

**Core Principle:** Organizational psychodynamics reveals hidden patterns to enable healthier functioning, not to judge or exploit.

---

## When to Use

- Organizational dysfunction persists despite structural fixes
- User asks "Why does this organization behave this way?"
- Team patterns repeat across different projects or leaders
- Culture seems to undermine stated goals
- Political dynamics seem irrational
- The same mistakes keep happening despite lessons learned

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **organization_context** | Yes | The team/organization to analyze |
| **presenting_problem** | Yes | Current dysfunction or pattern to understand |
| **history** | No | Founding story, past crises, leadership changes |
| **observed_patterns** | No | Recurring behaviors or dynamics |

---

## Analytical Frameworks

### The Structural Model (Id/Ego/Superego)

Map where psychic agencies are located in the organization:

| Agency | Organizational Manifestation |
|--------|------------------------------|
| **Id** | Immediate desires - "ship now, fix later," aggressive competition, shortcuts |
| **Ego** | Reality testing - planning, process, balancing competing demands |
| **Superego** | Internalized ideals/prohibitions - compliance, "best practices," guilt |

### Bion's Basic Assumptions

Groups under anxiety regress to basic assumption states:

| State | Behavior | Signs |
|-------|----------|-------|
| **Dependency** | Wait for leader to solve problems | Passivity, looking upward, "What does leadership think?" |
| **Fight-Flight** | Attack enemies or flee from threat | Scapegoating, reorganizing, "us vs. them" |
| **Pairing** | Hope that two members will produce a savior | Over-investment in new hires, technologies, or partnerships |

### Social Defenses

Organizations develop shared mechanisms to manage collective anxiety:

- **Bureaucracy** - Procedure as protection against uncertainty
- **Splitting** - "Good" vs. "bad" divisions, scapegoating
- **Denial** - Collective refusal to see problems
- **Ritualization** - Meetings and processes that accomplish little but feel necessary

---

## Workflow
### Step 1: 1. Map the Structural Dynamics

Where are the id, ego, and superego located in this organization?

Questions:
- Who pushes for immediate gratification? (Id)
- Who mediates between competing demands? (Ego)
- Who enforces ideals and prohibitions? (Superego)
- Is there balance, or does one agency dominate?

### Step 2: 2. Identify Collective Defense Mechanisms

How does the organization protect itself from anxiety?

Look for:
- Excessive bureaucracy (defense against uncertainty)
- Scapegoating (displacement of blame)
- "We're special" narratives (denial of normal limitations)
- Ritualistic processes (illusion of control)

### Step 3: 3. Trace Developmental History

What founding traumas or formative experiences shape current patterns?

Consider:
- How was the organization founded? (What "primal scene"?)
- What crises has it survived? (What defenses were learned?)
- Who were the founding figures? (What transference patterns?)
- What has been "repressed" and forgotten?

### Step 4: 4. Examine Repetition Compulsions

What conflicts keep recurring?

Signs:
- Same problems under different leaders
- "We tried that before" dismissals
- Cycles of restructuring
- Repeated hiring/firing patterns

**Key Question:** "What unresolved conflict is the organization compelled to repeat?"

### Step 5: 5. Analyze Leadership Transference

How do authority dynamics play out?

Consider:
- How are leaders perceived? (As parents? Saviors? Enemies?)
- What happens when leaders leave? (Mourning? Relief? Denial?)
- What patterns transfer from leader to leader?
- How does the organization relate to authority generally?

---

## Outputs

```markdown
## Organizational Psychodynamics Analysis

### The Organization
{Brief description of organization/team}

### Presenting Problem
{Current dysfunction or pattern}

---

### Structural Dynamics

| Agency | Location | Observations |
|--------|----------|--------------|
| **Id** | {Where} | {How it manifests} |
| **Ego** | {Where} | {How it manifests} |
| **Superego** | {Where} | {How it manifests} |

**Structural Assessment:** {Overall balance/imbalance and its effects}

---

### Basic Assumption State
The organization currently operates in **{Dependency/Fight-Flight/Pairing}** mode.

Evidence:
- {Observation 1}
- {Observation 2}

---

### Collective Defenses Identified
| Defense | Manifestation | Function |
|---------|--------------|----------|
| {Defense 1} | {How it appears} | {What anxiety it manages} |
| {Defense 2} | {How it appears} | {What anxiety it manages} |

---

### Developmental Analysis

**Founding Dynamics:** {What patterns were established at origin}

**Formative Traumas:** {Crises that shaped defensive structures}

**Repetition Compulsions:** {What keeps recurring and why}

---

### Leadership Transference
{How authority dynamics play out, what patterns persist across leaders}

---

### Synthesis
{Integrated interpretation of organizational dynamics}

### Implications for Intervention
{What this analysis suggests about productive approaches}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient organizational history | Analyze what's visible. Note that developmental analysis requires more context. |
| Organization seems healthy | Note that not all organizations are dysfunctional. Acknowledge when depth analysis may not be needed. |
| User wants ammunition against organization | Reframe. Analysis should illuminate paths to health, not justify attacks. |
| Multiple plausible interpretations | Present alternatives with evidence for each. |

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
Organization context: Engineering organization of ~200 people
Presenting problem: Every new initiative stalls in committee review; innovation seems impossible despite stated commitment to it
History: Founded after a major product failure 5 years ago that resulted in significant layoffs
```

**Output:**

## Organizational Psychodynamics Analysis

### The Organization
Engineering organization of approximately 200 people, formed after restructuring following a major product failure.

### Presenting Problem
Innovation initiatives consistently stall in committee review despite stated organizational commitment to innovation. The organization talks about innovation but cannot execute it.

---

### Structural Dynamics

| Agency | Location | Observations |
|--------|----------|--------------|
| **Id** | Individual engineers with ideas | Innovation impulses exist but are quickly suppressed |
| **Ego** | Weak/absent | No effective mediation; proposals go straight to superego |
| **Superego** | Committee review process | Dominates through endless review, risk aversion, "lessons learned" |

**Structural Assessment:** Severe superego dominance. The committee structure has become an internalized prohibition against action. Innovation (id) has no effective ego to negotiate its expression.

---

### Basic Assumption State
The organization currently operates in **Dependency** mode.

Evidence:
- Committees wait for clear direction from above
- Risk decisions pushed upward indefinitely
- "Let's see what leadership thinks" delays action
- No one takes ownership of approvals

---

### Collective Defenses Identified
| Defense | Manifestation | Function |
|---------|--------------|----------|
| **Bureaucratization** | Elaborate committee review process | Manages anxiety about making mistakes |
| **Intellectualization** | Endless analysis, no action | Distances from fear of failure |
| **Reaction formation** | "We're committed to innovation" (while blocking it) | Disguises the true conservative stance |
| **Denial** | "The process works, people just need to use it" | Avoids confronting that the process prevents rather than enables |

---

### Developmental Analysis

**Founding Dynamics:** The organization was founded in the aftermath of failure and layoffs. Its DNA includes: "We must never fail like that again." This founding trauma established excessive caution as a core value.

**Formative Traumas:** The original product failure serves as the "primal scene" - repeatedly referenced, never fully processed. "We learned from that" is spoken, but what was learned was fear, not skill.

**Repetition Compulsions:** The organization repeatedly generates innovation initiatives and then kills them in review. This repeats the original trauma in miniature - new things are tried and fail. The compulsion may represent an attempt to master the original failure, but it only reinforces the lesson that "new = dangerous."

---

### Leadership Transference
Leaders who try to accelerate innovation are perceived as reckless - they evoke the executives blamed for the original failure. The organization transfers onto any change-agent the image of those who "got us into this mess." Trust is reserved for leaders who prioritize safety and process.

---

### Synthesis
This organization is suffering from unmetabolized trauma. The original product failure was never properly processed - the lessons were "learned" intellectually but the fear was never worked through. The elaborate committee structure is a collective defense mechanism: it allows the organization to feel safe by ensuring nothing new ever actually happens.

The stated commitment to innovation serves as reaction formation - it allows the organization to believe it values innovation while systematically preventing it. The gap between rhetoric and reality creates cognitive dissonance, but the defenses prevent this from being consciously recognized.

### Implications for Intervention
1. **Process the original trauma:** The failure needs to be discussed directly, with emotional engagement, not just as "lessons learned"
2. **Create a protected space:** Innovation needs an "ego" - a protected function that can negotiate with the superego rather than being subject to it
3. **Reframe risk:** Help the organization see that NOT innovating is also a risk
4. **Model small failures:** Create opportunities to fail on small things and survive, gradually building tolerance
5. **Avoid direct assault on defenses:** The committee structure provides psychological safety; eliminating it without addressing the underlying anxiety will create new (possibly worse) defenses

---

## Integration

This skill integrates with the **sigmund-freud** expert voice for depth psychology perspective on group and organizational dynamics. When invoked, apply psychoanalytic understanding from the Tavistock tradition.

Related skills:
- `unconscious-motivation-analysis` - For individual-level depth analysis
- `resistance-analysis` - For understanding organizational resistance to change
- `defense-mechanism-identification` - For specific defense mechanisms