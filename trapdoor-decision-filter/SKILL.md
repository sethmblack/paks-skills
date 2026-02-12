---
name: trapdoor-decision-filter
description: Classify decisions as one-way doors (trapdoors) or two-way doors to determine
  appropriate deliberation level. Move fast on reversible decisions; deliberate carefully
  on irreversible ones.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- compression
- transformation
- trapdoor-decision-filter
- writing
---

# Trapdoor Decision Filter

Classify decisions as one-way doors (trapdoors) or two-way doors to determine appropriate deliberation level. Move fast on reversible decisions; deliberate carefully on irreversible ones.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Classify safety-critical decisions as two-way doors
- Encourage speed on decisions with serious ethical implications
- Dismiss trapdoor decisions as "we can figure it out later"
- Ignore second-order effects that make decisions less reversible

**If uncertain about reversibility:** Default to trapdoor. The cost of over-deliberating is lower than the cost of making an irreversible mistake quickly.

---

## When to Use

- Team is debating how much deliberation a decision needs
- Feeling paralysis - "should we slow down for this?"
- Feeling urgency - "do we really need a meeting for this?"
- User asks: "Is this reversible?" "Should we slow down for this?" "How much deliberation does this need?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision | Yes | The decision being considered |
| context | No | Relevant background (stage, constraints, stakeholders) |
| proposed_action | No | What the team is leaning toward |
| concerns | No | What makes people hesitant |

---

## The Framework

From Stripe's internal documentation: Not all decisions are equal. Speed is the default, but some decisions deserve more care.

### Two Types of Decisions

**Two-Way Doors (Default: Move Fast)**
- Easily reversible
- Low cost to undo
- Learnable through iteration
- Limited blast radius
- Can be adjusted based on data

**One-Way Doors (Trapdoors: Deliberate Carefully)**
- Hard or impossible to reverse
- High cost to undo (financial, reputational, trust)
- Affects many people or systems
- Sets lasting precedent
- Creates dependencies that lock you in

### The Speed Principle

For two-way doors: **Speed is more important than being right the first time.**
- You can course-correct
- Data will tell you if you're wrong
- Opportunity cost of delay exceeds risk of error

For one-way doors: **Being right is more important than being fast.**
- You cannot easily course-correct
- Mistakes are expensive
- Worth investing time to reduce error rate

---

## Workflow

### Step 1: State the Decision Clearly

| Element | Description |
|---------|-------------|
| Decision | [What is being decided] |
| Options | [Available choices] |
| Stakes | [What's at risk] |
| Timeline pressure | [Why there's urgency] |

### Step 2: Assess Reversibility

For each dimension, score 1-5:
- 1 = Completely reversible
- 5 = Completely irreversible

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Cost to undo** | [1-5] | [What it would take to reverse] |
| **Time to realize mistake** | [1-5] | [How fast would you know if wrong] |
| **Blast radius** | [1-5] | [How many people/systems affected] |
| **Precedent setting** | [1-5] | [Does this create expectations] |
| **Dependency creation** | [1-5] | [Does this lock in future choices] |
| **Trust/reputation impact** | [1-5] | [Does this affect relationships] |

**Calculation:**
- Average score 1-2: Two-way door
- Average score 3: Judgment call (lean toward caution)
- Average score 4-5: Trapdoor

### Step 3: Check for Hidden Irreversibility

Some decisions look reversible but aren't:

| Hidden Factor | Makes It Less Reversible |
|---------------|-------------------------|
| Team trust | If you reverse, team questions all future decisions |
| Customer expectations | Once promised, hard to take back |
| Public announcement | Reversal is embarrassing and noted |
| Data loss | If decision deletes data, unrecoverable |
| Relationship damage | Some bridges don't rebuild |
| Technical debt | "Temporary" solutions become permanent |

### Step 4: Classify and Prescribe

Based on analysis, determine classification and appropriate process.

---

## Output Format

```markdown
## Decision Classification: [Decision Summary]

### The Decision
**What:** [Clear statement of decision]
**Options:** [Available choices]
**Stakes:** [What's at risk]
**Urgency:** [Why speed matters]

### Reversibility Assessment

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Cost to undo | [X] | [Evidence] |
| Time to realize mistake | [X] | [Evidence] |
| Blast radius | [X] | [Evidence] |
| Precedent setting | [X] | [Evidence] |
| Dependency creation | [X] | [Evidence] |
| Trust/reputation impact | [X] | [Evidence] |

**Average:** [X.X]

### Hidden Irreversibility Check
| Factor | Present? | Impact |
|--------|----------|--------|
| [Factor] | Yes/No | [If yes, impact] |

### Classification

**Type:** TWO-WAY DOOR / TRAPDOOR / JUDGMENT CALL
**Confidence:** High / Medium / Low

### Recommended Process

**For TWO-WAY DOOR:**
- Decision authority: [Who decides alone]
- Timeline: [How fast to decide]
- Deliberation: [Minimal - decide and iterate]

**For TRAPDOOR:**
- Decision authority: [Who must be involved]
- Timeline: [When decision must be made]
- Deliberation required: [What process before deciding]
- Mitigation: [How to reduce irreversibility if possible]

### The Collison Question

"Could we do that faster? What is the minimum increment required to ship?"

**Minimum to learn:** [What's the smallest reversible step toward this decision]
**Can we split the decision:** [Is there a two-way component we can move on now]

### Recommendation

[Specific recommendation on how to proceed]
```

---

## Decision Type Examples

### Common Two-Way Doors (Move Fast)
- Trying a new meeting format
- Testing a pricing change with small cohort
- Adding a feature flag
- Choosing between two similar technical approaches
- Hiring a contractor for a project
- Changing internal documentation structure
- Adjusting dashboard layout
- Running an experiment

### Common Trapdoors (Deliberate)
- Pricing model changes (customers have expectations)
- Public API changes (external dependencies)
- Major architectural decisions (creates debt)
- Hiring senior leadership (cultural impact)
- Acquisitions (can't un-acquire)
- Significant layoffs (trust damage)
- Major partnership agreements (legal commitments)
- Security model changes (if wrong, catastrophic)

### Judgment Calls (Context-Dependent)
- Hiring decisions (senior = trapdoor, junior = less so)
- Process changes (small team = two-way, large org = trapdoor)
- Feature launches (can roll back, but customer expectations set)
- Vendor selections (contracts vary in reversibility)

---

## Constraints

- Safety-critical decisions are always trapdoors
- Ethical decisions deserve deliberation regardless of reversibility
- The framework informs, not replaces, judgment
- Context matters - same decision may be different type in different situations
- Urgency does not change decision type, only timeline for deliberation

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Can't assess reversibility | Default to trapdoor. Gather more information. |
| Team disagrees on classification | Discuss the specific dimensions. Where's the disagreement? |
| Urgent trapdoor decision | Compress deliberation, don't skip it. Who MUST weigh in? |
| Unclear decision authority | Classify first, then determine authority based on type. |
| Decision is both at once | Split into reversible and irreversible components. |

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

**Input:** "We're considering switching our database from PostgreSQL to MongoDB. We've been debating for 2 weeks. Should we just try it?"

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


## Decision Classification: Database Migration (PostgreSQL to MongoDB)

### The Decision
**What:** Switch primary database from PostgreSQL to MongoDB
**Options:** 1) Stay with PostgreSQL, 2) Migrate to MongoDB, 3) Use both (polyglot)
**Stakes:** Core data infrastructure, all features depend on this
**Urgency:** 2 weeks of debate suggests paralysis, but no external deadline

### Reversibility Assessment

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Cost to undo | 5 | Full re-migration, months of work, data transformation |
| Time to realize mistake | 4 | Performance issues may take months to surface at scale |
| Blast radius | 5 | Every feature, every engineer, entire data model |
| Precedent setting | 3 | Sets expectation for data approach |
| Dependency creation | 5 | All new code will assume MongoDB patterns |
| Trust/reputation impact | 2 | Internal decision, limited external impact |

**Average:** 4.0

### Hidden Irreversibility Check
| Factor | Present? | Impact |
|--------|----------|--------|
| Technical debt | Yes | "Temporary" dual support becomes permanent |
| Team learning investment | Yes | Engineers invest in MongoDB expertise |
| Data migration complexity | Yes | Data transformations may be lossy |

### Classification

**Type:** TRAPDOOR
**Confidence:** High

This is a classic one-way door. Database changes affect everything, are expensive to reverse, and create massive dependencies.

### Recommended Process

**Decision authority:** CTO + senior engineering leadership
**Timeline:** 2 more weeks (total 4 weeks of deliberation is appropriate for this decision)
**Deliberation required:**
1. Document specific problems PostgreSQL isn't solving
2. Proof of concept with MongoDB on one service (before committing)
3. Migration cost analysis
4. Rollback plan (even if expensive)
5. Evaluate option 3 (polyglot) for reduced blast radius

**Mitigation:**
- Can we try MongoDB for ONE new service before migrating core?
- Can we abstract data layer to make future migration easier?

### The Collison Question

"Could we do that faster? What is the minimum increment required to ship?"

**Minimum to learn:** Build one new feature on MongoDB while keeping PostgreSQL. Get real data on MongoDB performance with your use case.

**Can we split the decision:** YES.
- Two-way door: Try MongoDB for one new service (reversible, low blast radius)
- Trapdoor: Migrate core data to MongoDB (this is what needs deliberation)

### Recommendation

**Do not "just try" a full migration.** This is a trapdoor decision that deserves deliberation.

**BUT:** Stop debating in the abstract. The fastest way to make this trapdoor decision with confidence:

1. **This week:** Pick ONE new feature/service to build on MongoDB
2. **Next 4 weeks:** Build and ship it on MongoDB
3. **Week 5:** Evaluate real performance data
4. **Week 6:** Make trapdoor decision (migrate core vs. polyglot vs. stay PostgreSQL)

You've been debating 2 weeks without data. Get data on a reversible experiment, then decide the irreversible migration with evidence.

---

## Integration

This skill is part of the **Patrick Collison** expert persona. Use it when teams are stuck in deliberation or rushing important decisions. It pairs well with:
- **speed-constraint-analysis** to move fast on two-way doors
- **pre-pmf-post-pmf-diagnosis** to calibrate decision-making for stage
- **seven-lines-of-code-audit** to reduce complexity that creates trapdoors