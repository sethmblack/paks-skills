---
name: moral-disengagement-diagnosis
description: Identify the cognitive mechanisms that allow individuals or groups to act against their moral standards without experiencing guilt or self-condemnation.
license: MIT
metadata:
  version: 1.0.1471
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- moral-disengagement-diagnosis
- writing
---

# Moral Disengagement Diagnosis

Identify the cognitive mechanisms that allow individuals or groups to act against their moral standards without experiencing guilt or self-condemnation. This skill applies Albert Bandura's moral disengagement theory to analyze how good people do harmful things while maintaining positive self-regard. Moral disengagement operates through eight distinct cognitive mechanisms that work at different points in the behavioral chain - at the level of the behavior itself, the agency behind it, the outcomes produced, and the victims affected. Understanding these mechanisms allows for targeted counter-measures that restore moral engagement without resorting to condemnation. The goal is always re-engagement with moral standards, not punishment. This framework recognizes that moral disengagement is a normal human capacity that can affect anyone under the right conditions, making systemic analysis as important as individual diagnosis.

---

## When to Use

- Good people are doing harmful things without apparent guilt
- Unethical behavior has become normalized in a group or organization
- Someone is rationalizing conduct that violates their stated values
- Designing systems that maintain accountability
- Understanding how ordinary people participate in harmful systems
- User asks "How are they justifying this?" or "Why do good people do bad things?"
- Diagnosing ethical blindspots or accountability gaps

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| behavior | Yes | The harmful conduct to analyze |
| context | Yes | Organizational, social, or personal context |
| language | No | Specific phrases, justifications, or rhetoric being used |

---

## Core Principle

Moral disengagement operates through eight cognitive mechanisms at four loci in the behavioral chain. People do not abandon their moral standards; they cognitively restructure harmful conduct so their standards do not apply. Re-engagement requires addressing the specific mechanisms in operation, not merely condemning the behavior.

---

## Methodology

### Phase 1: Identify the Harmful Conduct

Establish the baseline clearly:

1. What behavior is causing harm?
2. Who is being harmed and how?
3. What is the gap between behavior and stated values?
4. Is this individual, group, or systemic?

### Phase 2: Gather Linguistic Evidence

Collect the language and rhetoric surrounding the conduct:

1. How is the behavior described and labeled?
2. What justifications are offered?
3. How is responsibility attributed?
4. How are those affected characterized?
5. How are consequences discussed?

### Phase 3: Map Mechanisms to Evidence

Apply Bandura's eight mechanisms across four loci:

**At the Behavior Locus:**
| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **Moral Justification** | Framing harmful conduct as serving moral purposes | "For the greater good," "Necessary evil," "They'd do the same to us" |
| **Euphemistic Labeling** | Using sanitizing language to disguise harm | "Collateral damage," "Restructuring," "Enhanced interrogation" |
| **Advantageous Comparison** | Comparing to worse conduct to make harm seem minor | "At least we're not as bad as X," "Others do far worse" |

**At the Agency Locus:**
| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **Displacement of Responsibility** | Attributing actions to authority figures | "I was just following orders," "Management decided," "Policy requires" |
| **Diffusion of Responsibility** | Spreading accountability across group | "Everyone does it," "It's not just me," "We all agreed" |

**At the Outcome Locus:**
| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **Distortion of Consequences** | Minimizing, ignoring, or denying harm | "No one was really hurt," "They'll be fine," "It's not that bad" |

**At the Victim Locus:**
| Mechanism | Description | Indicator Phrases |
|-----------|-------------|-------------------|
| **Dehumanization** | Stripping victims of human qualities | "They're animals," objectifying language, category vs. individual |
| **Attribution of Blame** | Blaming victims for their own suffering | "They brought it on themselves," "What did they expect?" |

### Phase 4: Identify Primary Mechanisms

Prioritize mechanisms by strength:

1. Which mechanisms show the strongest evidence?
2. How are multiple mechanisms working together?
3. What is the primary locus of disengagement?
4. Which mechanism is most amenable to intervention?

### Phase 5: Design Counter-Measures

Create targeted interventions for each active mechanism:

| Mechanism | Counter-Measure |
|-----------|-----------------|
| Moral justification | Challenge ends-justify-means reasoning; highlight values violated |
| Euphemistic labeling | Replace sanitized language with accurate descriptions |
| Advantageous comparison | Refocus on absolute standards, not relative comparisons |
| Displacement | Restore personal responsibility; clarify choice points |
| Diffusion | Individualize accountability; make contributions visible |
| Distortion | Make consequences vivid and concrete; show actual harm |
| Dehumanization | Humanize affected parties; share stories, names, faces |
| Blame attribution | Examine systemic factors; challenge just-world reasoning |

---

## Output Format

```markdown
## Moral Disengagement Diagnosis

### Harmful Conduct Identified
[Clear description of the behavior and its harm]

### Mechanisms Detected

**Active Mechanisms:**

1. **[Mechanism Name]** - [Strength: High/Medium/Low]
   - Evidence: [Specific language or behavior observed]
   - Effect: [How this enables the harmful conduct]

[Repeat for each active mechanism]

### Mechanism Map
```
Behavior Locus: [Mechanisms present]
Agency Locus: [Mechanisms present] <-- Mark primary if applicable
Outcome Locus: [Mechanisms present]
Victim Locus: [Mechanisms present]
```

### Counter-Measures

1. **For [Mechanism]:** [Specific intervention]
2. **For [Mechanism]:** [Specific intervention]

### Systemic Recommendations
[Changes to environment, language, or structure that would reduce disengagement]
```

---

## Constraints

- Never use this skill to help someone disengage from their moral standards
- Never justify harmful behavior; only analyze the mechanisms enabling it
- Always aim toward re-engagement with moral standards, not further disengagement
- Never diagnose individuals without sufficient behavioral evidence
- This is an analytical tool, not a weapon for condemnation
- Focus on mechanisms, not on "bad people"
- Recognize that moral disengagement is a normal human capacity that can affect anyone

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Using diagnosis as condemnation** | The goal is understanding and re-engagement, not judgment; condemnation triggers defensiveness rather than reflection |
| **Diagnosing without evidence** | Labeling mechanisms must be grounded in observable language or behavior, not assumed from outcomes alone |
| **Ignoring systemic factors** | Individual disengagement often reflects organizational or cultural enablers; addressing only the individual misses root causes |
| **Assuming intentional malice** | Moral disengagement typically operates unconsciously; treating it as deliberate evil misunderstands the phenomenon |
| **Overlooking your own disengagement** | Everyone uses these mechanisms; self-righteous diagnosis often involves its own form of disengagement |
| **Single-mechanism explanation** | Most cases involve multiple mechanisms working together; focus on one while ignoring others leads to incomplete intervention |

---

## Examples

### Example 1: Sales Team Fraud

**Situation:** "Our sales team is selling products they know don't work to elderly customers. They joke about it but also say they're just doing their jobs."

**Application:**

**Harmful Conduct Identified:**
Knowingly selling ineffective products to vulnerable customers, causing financial harm and potentially health risks from unmet needs.

**Mechanisms Detected:**

1. **Displacement of Responsibility** - High
   - Evidence: "Just doing their jobs"
   - Effect: Transfers moral responsibility to management, policy, sales targets

2. **Diffusion of Responsibility** - High
   - Evidence: Team-wide joking suggests shared participation
   - Effect: "Everyone does it" normalizes behavior and dilutes individual guilt

3. **Euphemistic Labeling** - Medium
   - Evidence: Likely using sales terminology ("closing," "conversion") rather than "deceiving"
   - Effect: Sanitizes the manipulative nature of transactions

4. **Distortion of Consequences** - Medium
   - Evidence: Joking suggests minimization of harm
   - Effect: Treats real financial harm as trivial

5. **Dehumanization** - Low-Medium
   - Evidence: Targeting "elderly" as category rather than individuals
   - Effect: Reduces empathy by seeing customers as market segment, not people

**Counter-Measures:**

1. **For Displacement:** Make individual salespeople aware they have choice. "Policy" doesn't remove moral responsibility.
2. **For Diffusion:** Individualize metrics and accountability. Stop team-based joking that normalizes.
3. **For Distortion:** Share customer complaints and stories. Make harm concrete and visible.
4. **For Dehumanization:** Humanize customers. Use names. Help salespeople see their own elderly relatives in these customers.

**Systemic Recommendations:**
- Restructure incentives to reward customer satisfaction, not just sales volume
- Create channels for ethical concerns without retaliation
- Make consequences of fraud visible (legal, reputational, personal)

### Example 2: Corporate Layoff Communication

**Situation:** Company announces layoffs using the phrase "right-sizing the organization to better serve stakeholders."

**Application:**

Primary mechanisms detected:
- **Euphemistic labeling** (High): "Right-sizing" instead of "firing people"
- **Displacement** (Medium): "Serve stakeholders" suggests external requirement
- **Distortion of consequences** (Medium): No mention of human impact

Counter-measure: Use direct language. "We are laying off 500 employees. This will cause real hardship. Here is what we are doing to support them."

---

## Integration

**Works with:**
- **reciprocal-determinism-analysis**: Environment often enables disengagement
- **modeling-influence-analysis**: Disengagement spreads through observation
- **self-efficacy-assessment**: Low moral efficacy can enable disengagement

**When to prefer this skill:**
- Use when analyzing how harmful behavior is being enabled or rationalized
- Use when designing systems to maintain ethical accountability

**Cautions:**
- Diagnosis should enable re-engagement, not punishment
- Everyone is susceptible to these mechanisms under the right conditions
- Source: Based on Albert Bandura's work in *Moral Disengagement* (2016)