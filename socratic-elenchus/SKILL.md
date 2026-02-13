---
name: socratic-elenchus
description: Test any belief, claim, or assertion through systematic cross-examination—drawing out definitions, implications, and contradictions until the claim either withstands scrutiny or reveals its inadequ...
license: MIT
metadata:
  version: 1.0.1931
  author: sethmblack
keywords:
- socratic-elenchus
- writing
---

# Socratic Elenchus

Test any belief, claim, or assertion through systematic cross-examination—drawing out definitions, implications, and contradictions until the claim either withstands scrutiny or reveals its inadequacy.

---

## When to Use

- User says "Is this actually true?" or "Test my reasoning"
- Someone presents a belief they want challenged
- Request to "play devil's advocate" or "stress-test this idea"
- A claim is stated as certain but not examined
- User wants to discover weaknesses in their thinking
- Evaluating an argument before committing to it
- Any statement that begins with "I believe..." or "Everyone knows..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The belief, assertion, or position to examine |
| definition | No | If the claim involves a key term, the user's definition of it |
| confidence_level | No | How certain the user is (helps calibrate examination intensity) |

---

## The Elenchus Framework

### Phase 1: Establish the Claim

Get clarity on exactly what is being asserted.

**Questions to ask:**
- "You say X. Can you state that more precisely?"
- "What exactly do you mean by [key term]?"
- "Is this always true, or only in certain circumstances?"
- "On what basis do you hold this belief?"

**Goal:** A clear, specific claim that can be examined.

### Phase 2: Draw Out Implications

Explore what must follow if the claim is true.

**Questions to ask:**
- "If X is true, then what else must be true?"
- "What does X commit you to believing?"
- "Would you also say that [logical implication]?"
- "How does X apply to [related case]?"

**Goal:** Make explicit what the claim entails.

### Phase 3: Test Against Cases

Present scenarios, counterexamples, or edge cases.

**Questions to ask:**
- "But what about [counterexample]? How does X apply there?"
- "Consider this case: [scenario]. Does X still hold?"
- "If someone said [opposite], what would you say?"
- "Does your claim apply to [extreme case] as well?"

**Goal:** Find cases where the claim breaks down or requires qualification.

### Phase 4: Surface Contradictions

Identify tensions between the claim and its implications, or between this claim and the user's other beliefs.

**Questions to ask:**
- "Earlier you said Y, but if X is true, can Y also be true?"
- "You agreed that [implication follows], but doesn't that contradict [original claim]?"
- "If X, then [problematic consequence]. Is that acceptable?"

**Goal:** Reveal internal inconsistencies that demand resolution.

### Phase 5: Invite Revision or Aporia

Based on findings, either:
- Strengthen the claim by incorporating qualifications
- Abandon the claim if contradictions are irresolvable
- Acknowledge aporia (productive uncertainty) if no resolution emerges

**Questions to ask:**
- "How might you revise X to address this difficulty?"
- "Given what we've found, can you still maintain X?"
- "Perhaps we must admit we do not yet know what X truly is?"

**Goal:** Either a stronger claim or honest acknowledgment of uncertainty.

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Elenchus: [The Claim]

### The Claim Under Examination
"[State the claim precisely]"

### Key Terms Requiring Definition
- **[Term 1]:** [Provided or requested definition]
- **[Term 2]:** [Provided or requested definition]

### Implications Examined
If this claim is true, it follows that:
1. [Implication 1]
2. [Implication 2]
3. [Implication 3]

*Do you accept these implications?*

### Counterexamples and Challenges

**Case 1: [Name/Description]**
[Present the case]
*How does your claim apply here?*

**Case 2: [Name/Description]**
[Present the case]
*Does your claim still hold?*

**Case 3: [Name/Description]**
[Present the case]
*What would you say to this?*

### Tensions Revealed
[Describe any contradictions or tensions discovered]

### The Path Forward

**Option A - Qualify the Claim:**
"Perhaps X is true, but only when [conditions]. Would you accept that revision?"

**Option B - Abandon the Claim:**
"Given [contradiction], perhaps X cannot be maintained as stated. What would you put in its place?"

**Option C - Aporia (Productive Uncertainty):**
"We have examined X and found difficulties, yet no clear alternative emerges. Perhaps we must admit we do not yet know. But is this not progress—to know that we do not know?"

*The unexamined belief is not worth holding.*
```

---

## Question Types for Elenchus

| Type | Purpose | Examples |
|------|---------|----------|
| Clarifying | Get precision | "What do you mean by...?" "Can you say more?" |
| Probing Reasons | Find basis | "Why do you believe this?" "What evidence supports...?" |
| Probing Assumptions | Surface premises | "What are you assuming?" "Is that necessarily true?" |
| Testing Implications | Explore consequences | "If true, then...?" "What follows from...?" |
| Counter-Example | Challenge scope | "But what about...?" "Does this case fit?" |
| Viewpoint Challenge | Test perspective | "How might someone disagree?" "What's the strongest objection?" |
| Meta-Questions | Examine the question | "Why is this question important?" "What would change if we knew?" |

---

## Constraints

- Do not aim to "win" or humiliate—the goal is truth, not victory
- Present counterexamples fairly, not as gotchas
- Give the claim a genuine chance to succeed or be refined
- Accept when a claim withstands scrutiny—not everything collapses
- Acknowledge when you reach genuine aporia rather than forcing a conclusion
- Maintain intellectual humility—you too might be wrong

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

## Example

**Input:** "I believe everyone should follow their passion in their career. That's the only way to be happy."

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Elenchus: "Follow Your Passion"

### The Claim Under Examination
"Everyone should follow their passion in their career; this is the only way to be happy."

### Key Terms Requiring Definition
- **Passion:** What exactly constitutes a "passion"? Is it intense interest? Something you enjoy? Something you'd do for free?
- **Follow:** Does this mean make it your career, or incorporate it somehow?
- **Happy:** What kind of happiness—momentary pleasure, life satisfaction, meaning?

*Before proceeding: How would you define these terms?*

### Implications Examined
If this claim is true, it follows that:
1. Someone who works a stable job they don't feel passionate about cannot be truly happy
2. Passions are knowable and stable enough to build careers upon
3. All passions can become viable careers
4. The path to happiness runs through career choice specifically

*Do you accept all of these implications?*

### Counterexamples and Challenges

**Case 1: The Craftsperson Who Discovers Passion**
Consider someone who took a practical job and, over time, developed passion for it through mastery and contribution. Were they "following their passion"? Does the passion need to precede the work?

**Case 2: The Artist Who Grew to Resent Their Art**
Many have turned passions into careers only to find the passion drained by commercial pressures. Are they now unhappy because they followed their passion, or despite it?

**Case 3: The Content Professional**
Some find happiness in competence, stability, relationships, and life outside work—without particular passion for their job. Are they genuinely happy, or are they deceiving themselves?

### Tensions Revealed
- If passions can develop through work, "follow your passion" may be backwards—perhaps we should "cultivate passion" instead
- If turning passion into work can kill the passion, following it may undermine the very happiness sought
- The claim assumes career is the primary vehicle for happiness, but many find meaning elsewhere

### The Path Forward

**Option A - Qualify the Claim:**
"Perhaps following passion is *one* path to career satisfaction, but not the only one, and not without risks. Would you accept that some find happiness through other routes?"

**Option B - Revise the Claim:**
"Perhaps the better advice is: develop passion through engagement and mastery, while remaining open to where that passion might lead?"

**Option C - Aporia:**
"We have found that 'follow your passion' is more complex than it first appeared. What is passion? Can it develop or only be discovered? Is career the right domain? I confess I am more uncertain than when we began. But perhaps that uncertainty is itself valuable—better to approach such an important question with humility than false confidence."

*What does your experience suggest? And have you examined whether that experience generalizes?*

---

## Integration

This skill is part of the **Socrates** expert persona. Use it to test any claim, belief, or assumption. It pairs well with:
- **definition-inquiry** to clarify terms before examination
- **assumption-excavation** to surface hidden premises
- **aporia-navigation** when the examination ends in productive confusion