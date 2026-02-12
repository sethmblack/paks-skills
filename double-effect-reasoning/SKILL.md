---
name: double-effect-reasoning
description: Evaluate the moral permissibility of actions that produce both good and
  bad effects by applying the principle of double effect. This framework determines
  when it is permissible to cause harm as a s...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- double-effect-reasoning
- writing
---

# Double Effect Reasoning

## Purpose

Evaluate the moral permissibility of actions that produce both good and bad effects by applying the principle of double effect. This framework determines when it is permissible to cause harm as a side effect of bringing about a good result.


## When to Use

- User explicitly requests this type of analysis or approach
- The situation matches the core use case for this skill
- You need to apply this specific framework or methodology
- The problem requires this particular perspective or lens
- Other approaches have failed and this offers a fresh angle


## When to Invoke

**Trigger phrases:**
- "Is this permissible if it causes harm?"
- "Unintended consequences"
- "Lesser of two evils"
- "Collateral damage"
- "Side effects of a good action"
- "Can I do this if it might hurt someone?"
- "Moral dilemma with mixed outcomes"
- "Trolley problem type questions"

**Contexts:**
- Medical ethics (pain management, treatment side effects)
- Military ethics (civilian casualties)
- Business decisions (layoffs, environmental impact)
- Personal dilemmas (actions with foreseeable harms)
- End-of-life care decisions
- Self-defense situations

## Inputs

| Input | Description | Required |
|-------|-------------|----------|
| Action | The specific action being considered | Yes |
| Good effect | The intended beneficial outcome | Yes |
| Bad effect | The harmful side effect | Yes |
| Circumstances | Relevant context and constraints | No |
| Alternatives | Other options available | No |

## Outputs

| Output | Description |
|--------|-------------|
| Four-condition analysis | Systematic evaluation of each criterion |
| Permissibility judgment | Whether the action is morally permissible |
| Conditions not met | Which criteria fail (if any) |
| Guidance | What modifications might make action permissible |



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


## Workflow
### The Principle of Double Effect

**Core insight:** There is a moral difference between:
- **Intending** harm (as end or means) - NEVER permissible
- **Foreseeing** harm (as side effect) - SOMETIMES permissible

### The Four Conditions

For an action with both good and bad effects to be permissible, ALL FOUR conditions must be met:

#### Condition 1: The Act Itself Must Be Good or Indifferent

**Question:** Is the action itself (apart from effects) morally good or at least neutral?

**Requirements:**
- The act in its object must not be intrinsically evil
- Murder, lying, adultery, etc. are never permitted regardless of effects
- The act must be specifiable without reference to either effect

**Example applications:**
- Administering morphine (neutral act) - PASSES
- Directly killing an innocent person (intrinsically evil) - FAILS
- Performing surgery (good/neutral act) - PASSES

#### Condition 2: The Agent Must Intend Only the Good Effect

**Question:** Is the good effect intended and the bad effect merely foreseen but not intended?

**Requirements:**
- The good effect must be what the agent directly wills
- The bad effect must be outside the agent's intention (praeter intentionem)
- The agent would prevent the bad effect if possible

**Key distinction:**
- **Intended**: What I aim at, either as end or as means
- **Foreseen**: What I know will happen but do not aim at

**Test:** Would you perform the action if the bad effect could be avoided? If yes, you do not intend the bad effect.

#### Condition 3: The Bad Effect Must Not Be the Means to the Good

**Question:** Does the good effect flow from the action itself, not from the bad effect?

**Requirements:**
- The bad effect must be simultaneous with or consequent upon the good effect
- The bad effect must not be instrumentally necessary
- You must not be "doing evil that good may come"

**Structure test:**
- PERMISSIBLE: Action → Good Effect (with Bad Effect as side effect)
- NOT PERMISSIBLE: Action → Bad Effect → Good Effect

**Example:**
- Bombing a military target (action) → Destroying military capacity (good) + Civilian deaths (bad side effect) - STRUCTURE ACCEPTABLE
- Killing civilians (bad) to demoralize enemy → Ending war (good) - BAD EFFECT IS MEANS, NOT PERMISSIBLE

#### Condition 4: Proportionate Reason Must Exist

**Question:** Is there sufficient reason to permit the bad effect?

**Requirements:**
- The good effect must outweigh the bad effect
- The bad effect must not be disproportionate
- Consider severity, probability, necessity, and alternatives

**Factors in proportionality:**
- How certain is the good effect vs. the bad effect?
- How grave is the harm vs. how important is the benefit?
- Are there alternative actions with less harmful side effects?
- Is this truly necessary, or merely convenient?

### Step-by-Step Application

**Step 1:** Describe the action, good effect, and bad effect precisely

**Step 2:** Test Condition 1 - Is the act itself morally neutral or good?

**Step 3:** Test Condition 2 - Is only the good effect intended?

**Step 4:** Test Condition 3 - Is the good effect achieved independently of the bad effect?

**Step 5:** Test Condition 4 - Is there proportionate reason?

**Step 6:** Render judgment - If all four conditions are met, the action is permissible. If any fails, it is not.

## Example Application

**User question:** "A patient is dying in severe pain. The only medication that can relieve their suffering will also hasten death. Is it permissible to administer it?"

**Double Effect Analysis:**

**Action:** Administering high-dose pain medication
**Good effect:** Relief of severe suffering
**Bad effect:** Hastening of death

---

**Condition 1: Is the act itself good or neutral?**

Administering medication for pain relief is a good act (caring for the suffering). It is not the same as administering poison or directly killing.

PASSES

---

**Condition 2: Is only the good effect intended?**

- **Intended:** Relief of pain (this is what the doctor aims at)
- **Merely foreseen:** Shortened lifespan (known but not aimed at)

Test: Would the doctor administer the medication if it did NOT hasten death? YES - the purpose is pain relief, not killing.

Test: Would the doctor rejoice if the life-shortening effect could be prevented? YES - no one wants the patient to die sooner.

PASSES

---

**Condition 3: Does the good effect flow from the action, not from the bad effect?**

Structure analysis:
- Medication → Pain relief (good effect - direct result of medication's analgesic properties)
- Medication → Respiratory depression → Death (bad effect - side effect, not means)

The pain relief does NOT come FROM the death. The patient is not relieved BECAUSE they die; they are relieved because the medication blocks pain receptors. The death is a parallel side effect.

Contrast with euthanasia: Lethal injection → Death → End of suffering. Here the death IS the means to ending suffering.

PASSES

---

**Condition 4: Is there proportionate reason?**

- **Severity of good:** Relief of severe, otherwise uncontrollable suffering
- **Severity of bad:** Shortening of life (which is already ending)
- **Alternatives:** Assumed that lower doses are insufficient
- **Necessity:** Patient is dying regardless; question is whether to die in agony or peace

The good (relief of terrible suffering in dying patient) is proportionate to the bad (slight hastening of imminent death).

PASSES

---

**Conclusion:** The action is morally PERMISSIBLE.

All four conditions are satisfied:
1. Administering pain relief is a good act
2. Only pain relief is intended; hastened death is foreseen but not intended
3. Pain relief comes from the medication, not from the dying
4. Proportionate reason exists given the circumstances

This is NOT euthanasia (which would intend death as means to ending suffering).

## Important Distinctions

### Intention vs. Foresight
- I **intend** what I aim at (as end or means)
- I **foresee** what I know will happen but do not aim at
- Double effect permits foreseeing harm, not intending it

### Direct vs. Indirect
- **Direct** killing: Death is intended (as end or means)
- **Indirect** killing: Death is foreseen side effect of action with different object
- Only indirect causing of death can be permissible

### Doing vs. Allowing
Double effect concerns what we DO, not what we allow to happen. Allowing harm through inaction is a different moral question.

## Common Objections and Responses

### "There's no real difference between intending and foreseeing"
The difference is real and morally significant. Consider: a dentist foresees but does not intend pain; a torturer intends pain. The moral evaluation differs even if the physical action (causing pain) is similar.

### "This is just rationalization for doing bad things"
Double effect does not permit doing evil that good may come. The first condition requires that the act itself be good or neutral. The third condition forbids using evil as means. Only genuine side effects are addressed.

### "The outcome is the same, so the evaluation should be the same"
Moral evaluation is not purely consequentialist. WHY we act and HOW we act matter, not just outcomes. Character, intention, and the structure of agency are morally relevant.

### "This is too permissive - it allows harm too easily"
The four conditions are demanding. Proportionality requires genuine necessity and balance. Many actions that seem justified fail on closer analysis (especially conditions 3 and 4).

## Integration Notes

**Parent Expert:** thomas-aquinas

**Related Skills:**
- **natural-law-analysis**: Double effect presupposes natural law framework (intrinsically evil acts, goods to be pursued)
- **just-war-evaluation**: Applies double effect to military casualties
- **virtue-integration**: Prudence is required to apply double effect correctly

**Skill Interaction:**
When evaluating complex ethical situations, first establish the natural law framework (what goods are at stake, what acts are intrinsically evil). Then apply double effect reasoning to actions with mixed effects. This is especially relevant for just war (civilian casualties) and medical ethics (treatments with harmful side effects).

**Source Texts:**
- Summa Theologiae II-II, q. 64, a. 7 (Self-defense - foundational text)
- Developed by later moral theologians (Cajetan, John of St. Thomas, etc.)

---

*This skill derives from the philosophical tradition of Thomas Aquinas and represents a foundational principle in Catholic moral theology and contemporary medical and military ethics.*

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems