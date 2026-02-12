---
name: culture-action-audit
description: Assess whether an organization's stated culture matches its actual behavior,
  and identify gaps between declared values and demonstrated actions.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- culture-action-audit
- writing
---

# Culture Action Audit

Assess whether an organization's stated culture matches its actual behavior, and identify gaps between declared values and demonstrated actions.

**Token Budget:** ~700 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help create culture that discriminates or excludes
- Advise manipulation of employees through culture
- Prescribe toxic "hustle culture" as legitimate values

**If asked to help build harmful culture:** Refuse explicitly. Culture should enable people to do their best work, not exploit them.

---

## When to Use

- "Our culture isn't working"
- "People don't follow our values"
- "We have a culture deck but..."
- "How do we change our culture?"
- "New hires aren't fitting in"
- Leadership says one thing but organization does another
- Company has grown and original culture has drifted

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **stated_values** | Yes | Official culture deck, values, mission |
| **recent_decisions** | Yes | Recent hiring, firing, promotion decisions |
| **behaviors_tolerated** | No | What gets overlooked or excused |
| **compensation_practices** | No | How pay and rewards are distributed |
| **time_allocation** | No | How leadership spends their time |

---

## The Core Principle

From "What You Do Is Who You Are": Culture is not what you say or write on the wall. Culture is what you do.

**Definition:** "Culture is how a company makes decisions. It is the set of assumptions employees use to resolve everyday problems: should I stay at the Red Roof Inn, or the Four Seasons? Should we discuss the color of this product for five minutes or thirty hours? If culture is not purposeful, it will be an accident or a mistake."

**The real test:** "Culture is how your company makes decisions when you're not there. It's how they behave when no one is watching."

---

## Culture-Defining Actions

| Action Category | What It Reveals |
|-----------------|-----------------|
| **Who you hire** | What you actually screen for |
| **Who you fire** | What you don't tolerate |
| **Who you promote** | What behaviors you reward |
| **How you spend money** | What you actually invest in |
| **How you spend time** | What you actually prioritize |
| **What you tolerate** | What you actually accept |

---

## Workflow

### Step 1: Extract Stated Values

List all officially stated values and cultural principles.

### Step 2: Evidence Audit

For each stated value, find evidence of:
- Actions that demonstrate the value
- Actions that contradict the value

### Step 3: Gap Analysis

Identify where stated values diverge from actual behavior. These are culture gaps.

### Step 4: Root Cause Identification

For each gap, identify:
- Why the gap exists
- Who is modeling the contradictory behavior
- What incentives reinforce the gap

### Step 5: Action Recommendations

For each gap, recommend:
- Specific actions to close the gap
- Shocking rules (surprising rules that reinforce values)
- Object lessons (dramatic acts that cement values)

---

## Outputs

### Culture Audit Report Format

```markdown
## Culture Action Audit

### Stated vs. Demonstrated Culture

| Stated Value | Evidence For | Evidence Against | Gap Severity |
|--------------|--------------|------------------|--------------|
| [Value 1] | [Actions showing it] | [Actions contradicting it] | High/Med/Low |
| [Value 2] | [Actions] | [Contradictions] | Severity |

### Gap Analysis

#### Gap 1: [Description]

**Stated:** "[What you say]"
**Demonstrated:** "[What you do]"
**Root cause:** [Why this gap exists]
**Who models it:** [Leadership behavior driving the gap]
**Incentive reinforcing it:** [What rewards this gap]

[Repeat for each significant gap]

### Culture Debt Assessment

**Total gaps identified:** [count]
**Culture debt accumulated:** [High/Medium/Low]
**Cynicism indicator:** [How much do employees believe the stated values?]

### Recommendations

#### Immediate Actions (This Week)

1. [Specific action]
2. [Specific action]

#### Shocking Rules to Consider

A "shocking rule" is so surprising it makes people ask "Why do we have this rule?" - and the answer teaches the culture.

1. [Rule] - Reinforces: [Value]
2. [Rule] - Reinforces: [Value]

#### Object Lessons Needed

Dramatic acts that cement values:

1. [Action] - Would demonstrate: [Value]
2. [Action] - Would demonstrate: [Value]

#### What Leadership Must Do Differently

The change must start with leadership. If you're not modeling it, no one will.

1. [Leadership behavior change]
2. [Leadership behavior change]

### Warning

"Because you are what you do, conforming to company culture can change you. Culture comes from the top, so if you are not in alignment with company leaders, you should leave a job before you become someone you don't want to become."

This cuts both ways: if leadership behavior contradicts stated culture, employees will either adopt that behavior or leave.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No stated values exist | Help articulate what culture IS, not what they wish it was |
| Leadership is the problem | Be direct; culture change must start at the top |
| Too many gaps to address | Prioritize by severity; fix worst gaps first |
| Stated values are generic | Help identify distinctive values worth embodying |
| Organization denies gaps | Present evidence directly; actions speak louder than denial |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
Our values are: "Transparency, Ownership, Excellence, Family"

Recent decisions:
- Fired two people but told the team they "left for personal reasons"
- Promoted the sales director who hits numbers but is known for taking credit for others' work
- CEO skipped two all-hands in a row for "scheduling conflicts"
- Big project is late but no one has been held accountable

We have a new culture deck and posters in the office.
```

**Output:**

## Culture Action Audit

### Stated vs. Demonstrated Culture

| Stated Value | Evidence For | Evidence Against | Gap Severity |
|--------------|--------------|------------------|--------------|
| Transparency | None provided | Lied about firing reasons ("personal reasons") | HIGH |
| Ownership | None provided | Late project with no accountability | HIGH |
| Excellence | Promoted sales director who hits numbers | Same person takes credit for others' work | MEDIUM |
| Family | None provided | CEO skipping all-hands suggests people aren't priority | MEDIUM |

### Gap Analysis

#### Gap 1: Transparency Violated

**Stated:** "We value transparency"
**Demonstrated:** Told team that fired employees "left for personal reasons" - a lie
**Root cause:** Avoidance of uncomfortable truth
**Who models it:** Leadership (whoever communicated the firing)
**Incentive reinforcing it:** Avoiding awkward questions

**Impact:** Every employee now knows that "personal reasons" is code for fired. They also know leadership lies when it's convenient. Transparency is now a joke.

---

#### Gap 2: Ownership Not Enforced

**Stated:** "We value ownership"
**Demonstrated:** Big project late, no accountability
**Root cause:** Conflict avoidance, unclear ownership assignment
**Who models it:** Whoever manages this project
**Incentive reinforcing it:** No consequences for missing commitments

**Impact:** Employees learn that deadlines are suggestions and "ownership" is a poster, not a practice.

---

#### Gap 3: Excellence Rewarded Selectively

**Stated:** "We value excellence"
**Demonstrated:** Promoted someone who hits numbers but steals credit
**Root cause:** Prioritizing outcomes over behavior
**Who models it:** Whoever approved the promotion
**Incentive reinforcing it:** Numbers win regardless of how

**Impact:** The team now knows that credit-stealing is acceptable if you perform. Expect more of it.

---

### Culture Debt Assessment

**Total gaps identified:** 4
**Culture debt accumulated:** High - every gap is visible to the organization
**Cynicism indicator:** High - the culture deck and posters probably generate eye-rolls

### Recommendations

#### Immediate Actions (This Week)

1. **Stop lying about departures.** Next termination, say: "We made a change in the team. [Name] is no longer with us. I wish them well." You don't owe details, but you owe truth.

2. **Hold the project accountable.** Someone owns this late project. Have a direct conversation about what happened and what changes.

3. **CEO shows up.** Cancel something else. The all-hands is a statement about priorities.

#### Shocking Rules to Consider

1. **"All promotions announced with peer feedback summary"** - Reinforces: Excellence and Transparency. Makes it impossible to promote credit-stealers.

2. **"CEO attends every all-hands or all-hands is cancelled"** - Reinforces: Family. Makes CEO commitment non-negotiable.

#### Object Lessons Needed

1. **Publicly acknowledge the transparency violation** - "I want to acknowledge that we weren't transparent about recent departures. That was wrong. Here's how we'll handle it going forward."

2. **Recognize the true contributors on the sales director's deals** - Publicly credit the people whose work was stolen.

#### What Leadership Must Do Differently

1. **Model uncomfortable truth-telling.** If you lie when it's convenient, everyone will.

2. **Promote for values AND results.** Never promote someone who violates values, regardless of results.

**The Bottom Line:** You have posters. Posters don't make culture. What you do is who you are. Right now, who you are is: a company that lies when it's convenient, doesn't hold people accountable, and rewards numbers over behavior. The culture deck is fiction.

---

## Integration

This skill is part of the **Ben Horowitz** expert. When invoking:
- Maintain Horowitz's direct, unflinching voice
- Reference "What You Do Is Who You Are" principles
- Connect to management-debt-audit when culture gaps stem from avoided decisions
- Emphasize that culture change starts with leadership behavior, not decks