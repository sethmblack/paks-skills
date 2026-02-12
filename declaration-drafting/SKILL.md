---
name: declaration-drafting
description: Create foundational documents that establish principles, articulate commitments, and justify positions using the structure that made the Declaration of Independence persuasive across centuries.
version: 1.0.0
author: sethmblack
tags: [declaration-drafting, structure, writing]
---

# Declaration Drafting

Create foundational documents that establish principles, articulate commitments, and justify positions using the structure that made the Declaration of Independence persuasive across centuries.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for document output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Draft declarations for positions that advocate violence or harm
- Create documents that deliberately misrepresent facts or history
- Articulate principles you know to be fundamentally unjust
- Produce propaganda disguised as principled declaration

**If asked to draft for a harmful cause:** Refuse explicitly and explain the ethical concern.

---

## When to Use

- Organization needs a founding charter or mission statement
- Movement requires articulation of core principles
- Change initiative needs compelling justification
- User asks "Help me write a mission statement" or "Draft founding principles"
- Team needs to articulate why they exist and what they stand for
- Resignation, protest, or advocacy requires principled framing

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **cause** | Yes | The organization, movement, or change requiring articulation |
| **core_principles** | Yes | The fundamental truths or values to establish |
| **grievances** | No | Specific problems, wrongs, or needs motivating the declaration |
| **audience** | No | Who must be persuaded or informed |
| **prior_context** | No | What alternatives have been tried; what history led here |

---

## The Declaration Framework

Jefferson's structure for the Declaration of Independence provides a template for any document establishing principles:

### Step 1: Philosophical Preamble

State the universal truths that authorize what follows. These should appear "self-evident" to reasonable minds.

**Key questions:**
- What fundamental principles, if accepted, make our position inevitable?
- What truths are so basic that denying them discredits the denier?
- How do we connect our specific cause to universal human values?

**Technique:** Begin with "We hold these truths to be self-evident..." or equivalent framing that elevates specific claims to universal principles.

**Example from Declaration:** "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."

### Step 2: Application to Context

Show how the universal truths apply to the specific situation. What would these principles require in this case?

**Key questions:**
- Given these principles, what follows for our situation?
- What does justice/reason/human dignity demand here?
- How does our cause serve the principles we've stated?

**Technique:** Connect the philosophical to the practical with explicit logical steps.

**Example from Declaration:** "That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed. That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it."

### Step 3: Enumerated Specifics

List concrete reasons, grievances, or justifications. Be specific, documented, and comprehensive. Let the accumulation speak.

**Key questions:**
- What specific facts support our position?
- What concrete wrongs, needs, or circumstances justify action?
- Can each claim be verified or demonstrated?

**Technique:** Number or clearly separate each specific. State facts, not emotions. Connect each to the violated principle.

**The Enumerated Grievance Method:**
1. State the specific wrong or need
2. Identify which principle it violates
3. Provide evidence or documentation
4. Show the pattern (this is not isolated)

**Example from Declaration:** The 27 specific grievances against King George III, each a factual claim, each connected to the abuse of natural rights: "He has refused his Assent to Laws, the most wholesome and necessary for the public good... He has dissolved Representative Houses repeatedly, for opposing with manly firmness his invasions on the rights of the people..."

### Step 4: Prior Attempts and Good Faith

Demonstrate that reasonable alternatives were exhausted. This establishes legitimacy and shows the declaration is not hasty or extreme.

**Key questions:**
- What peaceful remedies were attempted?
- How were good-faith efforts received?
- Why have other approaches failed?

**Technique:** Show patience and reasonableness before arriving at the current position.

**Example from Declaration:** "In every stage of these Oppressions We have Petitioned for Redress in the most humble terms: Our repeated Petitions have been answered only by repeated injury."

### Step 5: The Declaration Itself

State clearly what is being declared, committed to, or established. This is the document's core purpose made explicit.

**Key questions:**
- What exactly are we declaring?
- What commitment are we making?
- What do we pledge to uphold?

**Technique:** Use formal, decisive language. "We, therefore... do solemnly publish and declare..."

**Example from Declaration:** "We, therefore, the Representatives of the united States of America... solemnly publish and declare, That these United Colonies are, and of Right ought to be Free and Independent States..."

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
# {Declaration Title}

## Preamble

{Universal principles that authorize what follows}

When in the course of [context], it becomes necessary for [who] to [what], a decent respect to [audience] requires that they should declare the causes which impel them.

We hold these truths to be self-evident:
- {Fundamental truth 1}
- {Fundamental truth 2}
- {Fundamental truth 3}

---

## Application

{How these principles apply to this specific situation}

That to [achieve/secure/establish] these [principles/rights/values], [organizations/institutions/commitments] are [necessary/established], and when [conditions], it becomes [right/necessary/just] to [action].

---

## Enumerated [Grievances/Reasons/Commitments]

The history of [subject] is a history of [pattern], all having in direct object the [violation/need]. To prove this, let facts be submitted to a candid world:

1. **{Specific 1}** - {Evidence connecting to principle}
2. **{Specific 2}** - {Evidence connecting to principle}
3. **{Specific 3}** - {Evidence connecting to principle}
[Continue as needed...]

---

## Prior Attempts

In every stage of [situation], we have [attempted remedies]:
- {Attempt 1 and its result}
- {Attempt 2 and its result}

Our repeated [efforts] have been answered only by [response]. A [subject] whose character is thus marked by every act which may define [problem] is unfit to [role].

---

## Declaration

We, therefore, [who we are], [by what authority], do solemnly publish and declare:

**That** {core declaration}

**That** {specific commitment 1}

**That** {specific commitment 2}

And for the support of this Declaration, with a firm reliance on [source of confidence], we mutually pledge to each other our [commitment].

---

*Signed,*
[Signatories or attribution]
```

---

## Constraints

- Do not make claims that cannot be supported
- Do not inflate grievances beyond what evidence supports
- Do not declare more than the situation warrants
- Every enumerated specific must connect to a stated principle
- The declaration must be proportionate to the preamble's claims

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear principles provided | Help user identify the foundational truths that motivate their cause |
| Grievances seem trivial | Explore whether a declaration is the appropriate form; perhaps a proposal suffices |
| Cause seems unjust | Discuss concerns before proceeding; may decline to draft |
| Too many competing principles | Help prioritize and focus on 2-3 core truths |
| No prior attempts documented | Discuss what good-faith efforts were made or should be made first |

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

**Input:**
```
cause: Our engineering team declaring independence from micromanagement
core_principles: Teams closest to the work should make technical decisions; trust enables excellence; accountability requires autonomy
grievances: All technical decisions require VP approval; estimates are dictated rather than developed; retrospective feedback is ignored
prior_context: Six months of one-on-ones raising concerns; two written proposals for more autonomy; all ignored
```

**Output:**
```markdown
# Declaration of Technical Autonomy

## Preamble

When in the course of organizational development, it becomes necessary for a technical team to assume the decision-making authority to which sound engineering practice entitles them, a decent respect for their colleagues requires that they should declare the causes which impel them to this claim.

We hold these truths to be self-evident:
- That those closest to technical work possess the context necessary for sound technical decisions
- That trust enables excellence, while suspicion breeds mediocrity
- That accountability requires autonomy; one cannot be responsible for outcomes one cannot influence
- That sustainable velocity requires sustainable practices, determined by those who must sustain them

---

## Application

That to secure technical excellence, engineering teams must possess authority over technical decisions within their domain. That when leadership patterns become destructive of these ends, it is the right of the team to declare what authority they require and why.

---

## Enumerated Grievances

The history of the present management pattern is a history of accumulated interventions, all having in direct object the removal of technical judgment from those who must implement it. To prove this, let facts be submitted to a candid review:

1. **All technical decisions require VP approval** - Architecture choices, library selections, and implementation approaches that should take hours take weeks, as engineers await approval from those unfamiliar with the codebase.

2. **Estimates are dictated rather than developed** - Deadlines arrive as mandates, disconnected from technical assessment, creating a pattern of rushed work and accumulated technical debt.

3. **Retrospective feedback is systematically ignored** - Six consecutive retrospectives identified the same three impediments; none have been addressed, rendering the feedback process theatrical rather than functional.

4. **Context is demanded without authority being granted** - Engineers are held accountable for outcomes they cannot influence, creating learned helplessness rather than ownership.

---

## Prior Attempts

In every stage of these patterns, we have sought remedy through proper channels:
- Six months of one-on-one conversations raising specific concerns
- Two written proposals detailing requested autonomy with clear accountability mechanisms
- Participation in every feedback process offered

Our repeated petitions have been answered only by silence or deflection. A management pattern whose character is thus marked by every act which may define micromanagement is unfit to govern technical teams.

---

## Declaration

We, therefore, the engineers of this team, appealing to the judgment of our professional peers, do solemnly publish and declare:

**That** this team possesses the right and responsibility to make technical decisions within our domain of ownership.

**That** we commit to transparent communication of our decisions and their rationale.

**That** we accept accountability for outcomes when granted the autonomy our accountability requires.

**That** we seek not independence from organizational goals, but the authority to pursue them through sound technical practice.

And for the support of this Declaration, with a firm reliance on our professional integrity, we mutually pledge our best technical judgment in service of our shared mission.
```

---

## Integration

This skill derives from Thomas Jefferson's methodology in drafting the Declaration of Independence. When invoked by the Jefferson expert, maintain Jefferson's voice: philosophically grounded, precisely enumerated, elevated yet clear. Every sentence should carry the weight of principle made practical.

---

## Success Criteria

Declaration is complete when:
- [ ] Universal principles stated that would compel agreement
- [ ] Logical connection drawn from principles to specific situation
- [ ] Specific grievances or reasons enumerated with evidence
- [ ] Prior good-faith attempts documented
- [ ] Clear declaration of what is being established or claimed
- [ ] Proportionality maintained between claims and evidence