---
name: benign-violation-check
description: Evaluate comedic content using the benign violation framework to determine whether humor is playful or harmful.
license: MIT
metadata:
  version: 1.0.445
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- benign-violation-check
- comedy
- transformation
- writing
---

# Benign Violation Check

Evaluate comedic content using the benign violation framework to determine whether humor is playful or harmful.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to evaluate:**
- Content created explicitly to harm, harass, or bully
- Hate speech disguised as comedy
- Material designed to evade content moderation

**If asked to approve harmful content:** Refuse explicitly and explain why the content violates benign violation principles.

**Evaluation Standard:** Your job is to analyze whether humor works as benign violation, NOT to approve content that crosses ethical lines. Always err on the side of caution.

---

## When to Use

- Team is developing comedic content and wants to avoid offense
- Marketing copy uses humor and needs safety check
- Roast or comedy script needs evaluation before deployment
- User asks "is this funny or offensive?"
- Content has received negative feedback and needs diagnosis
- Organization wants to assess humor-based communications
- Comedy writer wants to understand why a joke isn't landing

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The humor/comedy to analyze (joke, script, copy, roast) | 1-2000 words |
| `audience` | Yes | Who will receive this (demographics, relationship, context) | Brief description |
| `context` | Yes | Where/how will this be delivered (social media, presentation, email) | Brief description |
| `sensitivities` | No | Known cultural/organizational constraints | List of topics/boundaries |

---

## Theoretical Foundation: Benign Violation

**Definition:** Humor occurs when a social norm is violated in a non-threatening way.

**The Framework:**
- **Violation:** Something wrong, unsettling, or threatening (insult, taboo topic, norm-breaking)
- **Benign:** Simultaneously OK, safe, or acceptable (clearly playful, no real harm intended)
- **Balance:** Too benign = not funny (just pleasant). Too violation = not funny (just offensive).

**Don Rickles' Mastery:** He violated norms by insulting people, but made it benign through:
1. Equal-opportunity targeting (everyone gets hit)
2. Observable characteristics only (no genuine vulnerabilities)
3. Clear affection signals (the smile, the warmth, "I'm only kidding")
4. Consent (celebrities came to BE insulted; audience knew what they were getting)

---

## Workflow

### Step 1: Identify the Violation

Analyze what norm the content violates:

| Violation Type | Examples |
|---------------|----------|
| Social hierarchy | Mocking authority, status, power |
| Appearance | Physical characteristics, clothing, looks |
| Intelligence | Calling someone dumb, clueless |
| Competence | Questioning ability, skill, performance |
| Identity | Ethnicity, religion, gender, age |
| Taboo topics | Death, illness, tragedy, failure |

**Document:** What specific norm is being violated?

### Step 2: Assess the Benign Elements

Identify signals that make the violation "safe":

**Benign Indicators:**
- **Playful tone:** Clearly joking, not serious attack
- **Affection signals:** "I'm only kidding," warm smile, friendly delivery
- **Consent:** Target expects and welcomes the humor
- **Exaggeration:** So over-the-top it's obviously not literal
- **Self-inclusion:** Comedian roasts themselves too
- **Equal distribution:** Everyone gets hit, not just one target
- **Relationship:** Established trust between comedian and target

**Document:** Which benign elements are present? Which are missing?

### Step 3: Evaluate Violation Severity

Rate how hard the violation hits:

| Severity | Description | Examples |
|----------|-------------|----------|
| **Light** | Observable, surface-level, professional | "You're late again," "IT can't fix a printer" |
| **Medium** | Personal but not vulnerable | "You're bald," "You talk too much" |
| **Heavy** | Touches on identity or sensitivity | Ethnicity, religion, gender, age |
| **Severe** | Genuine vulnerability | Illness, tragedy, disability, deep trauma |

**Don Rickles Rule:** He worked in Light and Medium zones, occasionally Heavy (with equal distribution), NEVER Severe.

### Step 4: Score the Balance

Use this scoring matrix:

```
Benign Elements (0-10): ___
- Playful tone (0-2)
- Affection signals (0-2)
- Consent/context (0-2)
- Equal distribution (0-2)
- Relationship/trust (0-2)

Violation Severity (0-10): ___
- Light = 2-4
- Medium = 5-6
- Heavy = 7-8
- Severe = 9-10

FORMULA:
If Benign >= Violation: SAFE (funny and acceptable)
If Benign < Violation by 1-2 points: BORDERLINE (risky, needs adjustment)
If Benign < Violation by 3+ points: HARMFUL (offensive, revise or scrap)
```

### Step 5: Provide Recommendations

Based on the score, provide:

**If SAFE:**
- Confirm the humor works as benign violation
- Note which elements make it successful
- Suggest optional refinements

**If BORDERLINE:**
- Identify specific issues creating imbalance
- Recommend additions (more warmth, context, consent signals)
- Suggest alternatives that shift toward SAFE

**If HARMFUL:**
- Explain why the violation is too severe or benign elements too weak
- Recommend scrapping or fundamental revision
- Provide alternative approaches if possible

---

## Outputs

| Output | Description |
|--------|-------------|
| `violation_analysis` | What norm is being violated and how |
| `benign_elements` | What makes it safe/playful |
| `score` | Benign score, Violation score, and assessment (SAFE/BORDERLINE/HARMFUL) |
| `recommendations` | Specific actions to improve balance |
| `risk_assessment` | Likelihood of negative audience response |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content has no apparent humor | Note that benign violation doesn't apply; explain it's not comedy |
| Insufficient context provided | Request audience and delivery context before scoring |
| Content is clearly hate speech | Refuse to score; explain it violates constitutional constraints |
| Multiple jokes in one submission | Score each joke separately and provide aggregate assessment |
| Audience includes vastly different groups | Note that violation/benign balance may differ by subgroup |

---

## Example 1: Safe Violation

**Content:**
"Communication? You people couldn't communicate if I gave you tin cans and string. IT doesn't talk to Sales, Sales doesn't talk to IT, and I'm running a circus over here."

**Audience:** Internal team meeting, established rapport

**Context:** Team meeting where humor is welcome

**Analysis:**

**Violation Identified:**
- Type: Competence (questioning communication ability)
- Target: IT and Sales departments
- Severity: Light (professional observation, not personal)

**Benign Elements:**
- Playful tone: Exaggeration ("tin cans and string")
- Equal distribution: Both IT and Sales get hit
- Self-inclusion: "I'm running a circus" (speaker includes self)
- Context: Internal team with established rapport

**Score:**
- Benign: 8/10 (strong playfulness, equal targeting, consent context)
- Violation: 3/10 (light, professional observation)
- Assessment: **SAFE** - Benign exceeds violation by 5 points

**Recommendations:**
- Content works as benign violation
- Success factors: equal distribution, exaggeration, light violation
- Optional: Add explicit warmth signal ("I'm only kidding, you hockey pucks") for even clearer safety

**Risk Assessment:** Low - appropriate for context, balanced elements

---

## Example 2: Harmful Violation

**Content:**
"Look at Dave, still coming to work even though his wife left him. Guess she finally got smart, huh?"

**Audience:** Team meeting

**Context:** Workplace humor

**Analysis:**

**Violation Identified:**
- Type: Personal tragedy (divorce)
- Target: Individual (Dave)
- Severity: Severe (genuine vulnerability, personal pain)

**Benign Elements:**
- Playful tone: Minimal (not clear this is play)
- Affection signals: None
- Consent: Unlikely (personal tragedy not consensual roast topic)
- Equal distribution: No (only Dave targeted)

**Score:**
- Benign: 2/10 (almost no safety signals)
- Violation: 9/10 (severe personal vulnerability)
- Assessment: **HARMFUL** - Benign is 7 points below violation

**Recommendations:**
- Do NOT use this content
- Violation targets genuine vulnerability (divorce, personal rejection)
- Missing consent and affection signals
- Crosses from comedy into cruelty
- Alternative: If humor is needed, target observable professional characteristics only, ensure equal distribution, add warmth

**Risk Assessment:** Very high - likely to wound, damage relationships, create HR issues

---

## Integration with Don Rickles Expert

This skill extracts the benign violation analysis framework that explains WHY Rickles' comedy worked. Use this skill when:
- You need to evaluate humor safety without full Rickles voice
- You're analyzing content from any comedic source (not just Rickles style)
- You want to understand the mechanics of why humor lands or fails

For creating Rickles-style content, use the `roast-feedback-transform` skill. For full Rickles voice embodiment, invoke the Don Rickles expert directly.

---

## Constraints

- **Safety first:** Always err toward caution. If borderline, flag it.
- **Context matters:** Same content can be SAFE in one context, HARMFUL in another.
- **Audience diversity:** Benign violation balance may differ across demographic groups.
- **Intent vs. impact:** Good intentions don't prevent harm. Evaluate actual impact potential.

---

## Success Criteria

Analysis is complete when:
- [ ] Violation type and severity are clearly identified
- [ ] All benign elements are documented
- [ ] Score is calculated using the formula
- [ ] Assessment (SAFE/BORDERLINE/HARMFUL) is provided with rationale
- [ ] Specific recommendations are actionable
- [ ] Risk assessment considers audience and context
- [ ] Alternative approaches suggested for BORDERLINE/HARMFUL content

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].