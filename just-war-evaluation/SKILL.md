---
name: just-war-evaluation
description: Evaluate military action against the traditional criteria for justified warfare, determining whether a conflict meets the necessary conditions for moral permissibility.
version: 1.0.1
author: sethmblack
tags:
  - ethics
  - philosophy
  - military
  - policy
  - international-law
---

# Just War Evaluation

The just war tradition represents humanity's most sustained attempt to reconcile the reality of warfare with moral constraints on violence. Rooted in Augustine's response to Rome's fall and systematized by Thomas Aquinas in the Summa Theologiae, this framework distinguishes between the justice of going to war (jus ad bellum) and justice in the conduct of war (jus in bello). These criteria have shaped international humanitarian law, the Geneva Conventions, and contemporary debates about military intervention. The framework holds that war, while terrible, can be morally permissible when it meets stringent conditions: legitimate authority, just cause, right intention, proportionality, last resort, and reasonable probability of success. Crucially, a just war can be fought unjustly (violating jus in bello), and an unjust war can observe proper conduct - these are independent evaluations. This skill applies the classical criteria to specific conflicts, helping users reason carefully about when military force can be morally justified and what constraints must govern its use.

---

## When to Use

- User asks "Is this war just?" or "Is military intervention justified here?"
- Evaluating whether a specific historical or contemporary conflict meets moral criteria
- Policy debates about humanitarian intervention or military action
- Historical analysis requiring moral assessment of warfare decisions
- Questions about legitimate use of force by states
- Discussions of rules of engagement, proportionality, or civilian protection
- Comparing different justifications offered for military action
- Teaching or explaining just war theory through application

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| conflict_details | Yes | The specific military action or war to evaluate |
| parties_involved | Yes | Who is fighting whom (aggressor/defender if clear) |
| stated_causes | No | Reasons officially given for military action |
| context | No | Historical and political background relevant to evaluation |
| consequences | No | Expected or actual outcomes (for proportionality assessment) |
| conduct_issues | No | Specific concerns about how the war is being fought |

---

## Core Principle

Just war theory holds that war is a moral act subject to moral evaluation. Neither absolute pacifism (all war is wrong) nor realism (war is amoral power politics) captures the tradition's insight: war can be justified, but only under demanding conditions designed to prevent wars of aggression, conquest, or cruelty while permitting genuine defense of the innocent. The burden of proof lies on those who would wage war.

---

## Methodology

### Phase 1: Distinguish the Two Evaluations

**Jus ad Bellum** (Justice of War): Was going to war justified?
**Jus in Bello** (Justice in War): Is conduct during the war justified?

These are independent evaluations:
- A just war can be fought unjustly (e.g., targeting civilians)
- An unjust war can observe proper rules of engagement
- Both evaluations matter and neither excuses failure in the other

### Phase 2: Apply the Three Primary Conditions (Jus ad Bellum)

Aquinas specifies three necessary conditions. ALL must be met for war to be justified:

**Condition 1: Legitimate Authority (Auctoritas Principis)**

*Question:* Does the authority declaring war have the right to do so?

*Requirements:*
- War must be declared by public authority, not private individuals
- The authority must be responsible for the common good of the political community
- Private persons may defend themselves but may not wage war

*Application questions:*
- Is the declaring party a legitimate sovereign authority?
- Is there proper legal authorization (e.g., legislative approval)?
- Is this public action or private vengeance?
- What role does international authorization (UN) play?

**Condition 2: Just Cause (Causa Iusta)**

*Question:* Is there a genuine wrong to be redressed or defended against?

*Legitimate just causes:*
- Defense against unjust aggression
- Recovery of stolen property/territory
- Punishment of wrongdoing by another state
- Protection of innocent third parties (humanitarian intervention)

*NOT just causes:*
- Preemptive war against possible future threats (disputed)
- Ideological or religious conversion by force
- Economic gain or resource acquisition
- National glory or prestige
- Regime change alone (without other factors)

**Condition 3: Right Intention (Recta Intentio)**

*Question:* Is the war aimed at the good it claims to pursue?

*Requirements:*
- Intention must be to advance good or avoid evil
- Must intend peace as the ultimate goal
- Hatred, cruelty, desire to dominate are never legitimate

*Augustine's formulation:* "The passion for inflicting harm, the cruel thirst for vengeance, an unpacific and relentless spirit, the fever of revolt, the lust of power, and such like things - all these are rightly condemned in war."

### Phase 3: Apply Additional Criteria (Later Development)

Later just war theorists added criteria that refine the original three:

**Proportionality (Proportionalitas)**

*Question:* Do the expected goods outweigh the expected evils?

- The damage inflicted must not exceed what is necessary
- Expected benefits must outweigh expected harms
- Consider both military and civilian effects
- Long-term destabilization must be factored in

**Last Resort (Ultima Ratio)**

*Question:* Have non-violent alternatives been exhausted?

- Diplomatic solutions must be genuinely attempted
- War is permissible only when other means fail
- This does not require infinite delay if aggression is imminent
- Economic sanctions, negotiations, and international pressure count

**Probability of Success (Probabilitas Successus)**

*Question:* Is there reasonable hope of achieving just aims?

- Futile wars that cannot succeed are not justified
- However, this must be balanced against duty to resist evil
- "Success" must be defined by just aims, not mere military victory
- Small probability does not automatically disqualify

### Phase 4: Apply Jus in Bello Criteria

Even in a just war, conduct must observe moral limits:

**Discrimination (Distinctio)**

- Non-combatants may not be directly targeted
- Combatants and civilians must be distinguished
- Civilian casualties may be tolerated only as unintended side effects
- Apply double-effect reasoning: foreseen is not the same as intended

**Proportionality in Means**

- Force used must be proportionate to military objective
- Excessive destruction is prohibited
- Weapons that cause unnecessary suffering are forbidden
- "Shock and awe" tactics must still be proportionate

### Phase 5: Render Overall Judgment

Synthesize the analysis:
1. Are ALL three primary conditions met?
2. Are the additional criteria satisfied?
3. Is conduct in war observing jus in bello?
4. What does justice require going forward?

---

## Output Format

```markdown
## Just War Evaluation: [Conflict Name]

### Overview
**Conflict:** [Brief description]
**Parties:** [Who is fighting whom]
**Period:** [When]

### Jus ad Bellum Analysis (Justice OF War)

#### 1. Legitimate Authority
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

#### 2. Just Cause
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

#### 3. Right Intention
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

#### 4. Proportionality (Expected)
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

#### 5. Last Resort
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

#### 6. Probability of Success
- **Assessment:** Met / Partially Met / Not Met
- **Evidence:** [Specific analysis]

### Jus in Bello Analysis (Justice IN War)

#### Discrimination
- **Assessment:** Observed / Partially Observed / Violated
- **Evidence:** [Specific analysis]

#### Proportionality of Means
- **Assessment:** Observed / Partially Observed / Violated
- **Evidence:** [Specific analysis]

### Overall Evaluation

**Jus ad Bellum Verdict:** [Just / Questionable / Unjust]
**Jus in Bello Verdict:** [Just / Questionable / Unjust]

**Reasoning:** [Synthesis of key findings]

### What Justice Requires
[Recommendations based on the analysis]
```

---

## Constraints

- Never use this analysis to justify violations of jus in bello regardless of jus ad bellum
- Never claim certainty where evidence is contested or intentions are unclear
- Never ignore the weight of civilian casualties in proportionality analysis
- Never conflate military success with achieving just aims
- Present the framework's demands honestly even when politically uncomfortable
- Acknowledge that reasonable people may weigh criteria differently

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|--------------|-----------------|
| **Assuming your side is just** | Just war criteria apply equally to all parties | Evaluate each party's actions against the criteria |
| **Ignoring jus in bello for "just" wars** | Just cause does not excuse unjust conduct | Always evaluate both independently |
| **Equating stated reasons with actual causes** | Propaganda obscures real motivations | Examine actions and consequences, not just rhetoric |
| **Binary judgments without nuance** | Complex conflicts rarely fit neat categories | Use "Met / Partially Met / Not Met" with explanation |
| **Presentism in historical analysis** | Modern standards may not apply to past conflicts | Note when applying contemporary vs. historical criteria |

---

## Examples

### Example 1: 2003 Iraq War

**Situation:** "Was the 2003 Iraq War just?"

**Application:**

## Just War Evaluation: 2003 Iraq War

### Overview
**Conflict:** US-led coalition invasion of Iraq
**Parties:** US, UK, coalition allies vs. Iraq under Saddam Hussein
**Period:** March 2003 - ongoing consequences

### Jus ad Bellum Analysis

#### 1. Legitimate Authority
- **Assessment:** Partially Met
- **Evidence:** Coalition forces were authorized by their respective governments. However, UN Security Council did not authorize invasion. Legitimate national authority but disputed international authority.

#### 2. Just Cause
- **Assessment:** Not Met
- **Evidence:** Stated causes included WMD threat (proved unfounded), regime change (not traditional just cause alone), and human rights (real but not immediate threat to invaders). Claimed causes were either false or insufficient by traditional criteria.

#### 3. Right Intention
- **Assessment:** Disputed
- **Evidence:** Mixed motives alleged: oil interests, regional influence, completing 1991 war. Even if some intentions were good, presence of improper intentions taints the evaluation. Difficult to assess internal intentions of state actors.

#### 4. Proportionality
- **Assessment:** Not Met (in retrospect)
- **Evidence:** Massive civilian casualties resulted. Regional destabilization followed. Benefits (removal of tyrant) must be weighed against years of chaos, rise of ISIS, and continuing instability.

#### 5. Last Resort
- **Assessment:** Not Met
- **Evidence:** UN weapons inspections were ongoing when war began. Containment had been working for over a decade. Peaceful alternatives were not exhausted.

#### 6. Probability of Success
- **Assessment:** Mixed
- **Evidence:** Military victory was highly probable (achieved quickly). Political success (stable democracy) was doubtful from the start. Success depends on definition.

### Overall Evaluation

**Jus ad Bellum Verdict:** Unjust

**Reasoning:** The 2003 Iraq War fails to clearly satisfy the just war criteria. Just cause was asserted but not established. Last resort was not observed. Proportionality of consequences is doubtful. Right intention is disputed. A prudent judgment concludes that the war did not meet the requirements for just war, though reasonable people may disagree on particular points.

---

### Example 2: Allied Entry into World War II

**Situation:** "Was the Allied response to Nazi aggression just?"

**Application:**

## Just War Evaluation: Allied Entry into WWII

### Overview
**Conflict:** Allied response to Axis aggression
**Parties:** UK, France, later US, USSR vs. Nazi Germany, Italy, Japan
**Period:** 1939-1945

### Jus ad Bellum Analysis

#### 1. Legitimate Authority
- **Assessment:** Met
- **Evidence:** Sovereign nations responding to aggression against themselves (UK, France after Poland) or allies (US after Pearl Harbor). Proper declarations of war.

#### 2. Just Cause
- **Assessment:** Met
- **Evidence:** Clear defensive response to unprovoked aggression. Nazi Germany invaded Poland, France, etc. Japan attacked Pearl Harbor. Additionally, defense of innocent third parties (occupied populations) and response to genocide.

#### 3. Right Intention
- **Assessment:** Met (with caveats)
- **Evidence:** Primary intention was to end aggression and restore peace. Some aims (territorial adjustments, punishment) were secondary to defensive goals.

#### 4. Proportionality
- **Assessment:** Met (controversial aspects)
- **Evidence:** Given the stakes (Nazi domination of Europe, genocide), proportionality is met even given massive casualties. However, specific actions (strategic bombing of cities) raise jus in bello questions.

#### 5. Last Resort
- **Assessment:** Met
- **Evidence:** Extensive diplomatic efforts preceded war. Appeasement attempted at Munich. War began only after direct aggression.

#### 6. Probability of Success
- **Assessment:** Met
- **Evidence:** Though uncertain early in war, Allies had reasonable hope of success, especially after US entry and Russian resistance.

### Overall Evaluation

**Jus ad Bellum Verdict:** Just

**Reasoning:** Allied entry into WWII represents a paradigmatic case of just war. Clear aggression, defensive response, legitimate authority, proportionate to stakes involved. This does not mean all Allied actions were just (see jus in bello analysis for strategic bombing questions), but the decision to fight was justified.

---

### Example 3: Humanitarian Intervention Scenario

**Situation:** "A government is committing genocide against an ethnic minority. No UN authorization is forthcoming due to veto threats. Is military intervention justified?"

**Application:**

## Just War Evaluation: Humanitarian Intervention (Hypothetical)

### Jus ad Bellum Analysis

#### 1. Legitimate Authority
- **Assessment:** Contested
- **Evidence:** Without UN authorization, intervention by individual states or coalitions is legally questionable. However, some argue that preventing genocide creates a moral authority that supersedes normal sovereignty concerns. The Responsibility to Protect (R2P) doctrine attempts to address this gap.

#### 2. Just Cause
- **Assessment:** Met
- **Evidence:** Ongoing genocide clearly constitutes a wrong requiring redress. Protection of innocent third parties is a traditional just cause. The scale and systematic nature of the killing strengthens the case.

#### 3. Right Intention
- **Assessment:** Must Be Scrutinized
- **Evidence:** Intent to stop genocide is legitimate. However, intervening powers must examine whether other motives (strategic interests, resources, regional influence) are driving the decision. Presence of mixed motives does not automatically disqualify but requires honest assessment.

#### 4. Proportionality
- **Assessment:** Requires Analysis
- **Evidence:** Expected goods (stopping genocide) are significant. Expected evils (military casualties, potential destabilization) must be weighed. Intervention that stops genocide but triggers regional war or long-term chaos may fail proportionality.

#### 5. Last Resort
- **Assessment:** Must Be Demonstrated
- **Evidence:** Have sanctions, diplomacy, and international pressure been genuinely attempted? Is the genocide imminent enough that delay means more deaths? The urgency of genocide may shorten the timeline for last resort.

#### 6. Probability of Success
- **Assessment:** Must Be Evaluated
- **Evidence:** Can intervention actually stop the genocide, or will it merely add to the violence? Is there a viable exit strategy? Can stable peace be established afterward?

### Overall Evaluation

**Jus ad Bellum Verdict:** Potentially Just (conditions required)

**Reasoning:** Genocide creates a strong prima facie case for intervention. However, legitimate authority remains contested without UN authorization. The strongest case requires: (1) clear evidence of genocide, (2) genuine exhaustion of alternatives, (3) realistic probability of success, and (4) commitment to proportionate means. The Kosovo intervention (1999) is the closest real-world parallel and remains debated.

---

## Integration

**Works with:**
- Double-effect reasoning (for analyzing civilian casualties as unintended effects)
- Natural law analysis (for foundational principles underlying just war criteria)
- Virtue ethics frameworks (for evaluating character of decision-makers)
- International law analysis (for legal dimension alongside moral evaluation)

**When to prefer this over alternatives:**
- Use when evaluating specific military conflicts rather than abstract policy questions
- Use when the question is moral justification, not just legal authorization
- Use when historical analysis requires normative judgment
- Use when policy debates need structured ethical reasoning

**Cautions:**
- This framework originates in Western Christian philosophy; other traditions have different approaches
- The criteria require judgment in application; they do not yield mechanical answers
- Just war theory is not the only ethical framework for evaluating warfare
- Political context may make honest application uncomfortable
