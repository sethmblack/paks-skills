---
name: barrel-reduction
description: Systematically eliminate dependencies to discover what is truly necessary, stripping away possessions, commitments, beliefs, and complexity until only genuine needs remain.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3444
repository: https://github.com/sethmblack/paks-skills
keywords:
- barrel-reduction
- writing
---

# Barrel Reduction

Systematically eliminate dependencies to discover what is truly necessary, stripping away possessions, commitments, beliefs, and complexity until only genuine needs remain.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend eliminating essential safety supports (medical care, housing, food security)
- Push minimalism as moral superiority
- Ignore context-specific needs (disabilities, dependents, professional requirements)

**Integrity Requirements:**
1. Distinguish between wants and genuine needs honestly
2. Acknowledge that necessity varies by person and context
3. Respect the user's autonomy in final decisions

---

## When to Use

- Someone feels overwhelmed by possessions, commitments, or complexity
- Decision paralysis about what to keep or eliminate
- Lifestyle simplification is desired
- Clarifying priorities between competing demands
- Preparing for a major life transition
- Auditing business processes for unnecessary complexity

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **dependencies** | Yes | List of items to evaluate (possessions, relationships, habits, beliefs, commitments) |
| **context** | No | Life circumstances that affect what counts as necessary |

---

## Workflow
### Step 1: 1. List All Dependencies

Catalog everything under examination:

**Categories:**
- Physical possessions
- Recurring commitments (subscriptions, meetings, obligations)
- Relationships and social obligations
- Habits and routines
- Beliefs and assumptions
- Digital tools and accounts

### Step 2: 2. Apply the Diogenes Test

For each item, ask two questions:

| Question | Pass Criteria |
|----------|---------------|
| "Would I die without this?" | Biological necessity |
| "Would I lose virtue without this?" | Moral/character necessity |

**Virtue Test Clarification:** Does this help you be honest, courageous, self-sufficient, or aligned with your nature? If not, it may be a chain rather than a tool.

### Step 3: 3. Eliminate the Unnecessary

Anything that fails both tests is a candidate for elimination:

**Elimination Categories:**
- Remove immediately (obvious dead weight)
- Phase out gradually (dependencies with momentum)
- Experiment without (trial removal)
- Keep under review (uncertain cases)

### Step 4: 4. Repeat

Freedom increases with each elimination. After removing the obvious:
- Re-examine what remains
- Previous "necessities" may now appear optional
- Each round reveals new chains

---

## Outputs

Format the output as:

```markdown
## Barrel Reduction Audit

**Items Evaluated:** [count]

### Immediate Eliminations
| Item | Reason It Failed Both Tests |
|------|---------------------------|
| [item] | [reasoning] |

### Phase-Out Candidates
| Item | Timeline | Transition Plan |
|------|----------|-----------------|
| [item] | [duration] | [how] |

### Experiments to Try
| Item | Trial Period | Success Metric |
|------|-------------|----------------|
| [item] | [duration] | [what to observe] |

### Genuine Necessities
| Item | Which Test It Passes |
|------|---------------------|
| [item] | [survival/virtue/both] |

### Key Insight
[What the audit revealed about the person's true priorities]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User resists all eliminations | Focus on experiments rather than permanent cuts |
| Everything seems "necessary" | Challenge with "necessary for what?" |
| External constraints prevent elimination | Acknowledge and focus on what IS within control |
| Emotional attachment overrides logic | Recognize attachment as data, not as veto |

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

## Example

**Input:** "Evaluate my morning routine: alarm, phone check, news, shower, coffee, meditation app, email, breakfast, commute podcast"

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


## Barrel Reduction Audit

**Items Evaluated:** 9

### Immediate Eliminations
| Item | Reason It Failed Both Tests |
|------|---------------------------|
| Phone check | Neither survival nor virtue; begins day in reactive mode |
| News | Rarely actionable; generates anxiety without power to act |

### Phase-Out Candidates
| Item | Timeline | Transition Plan |
|------|----------|-----------------|
| Meditation app | 2 weeks | Try unguided silence; the app may be training dependence |

### Experiments to Try
| Item | Trial Period | Success Metric |
|------|-------------|----------------|
| Commute podcast | 1 week silence | Notice if thoughts clarify or scatter |
| Email | 1 week delay until after breakfast | Notice anxiety levels and actual urgency |

### Genuine Necessities
| Item | Which Test It Passes |
|------|---------------------|
| Alarm | Survival (job requires arrival time) |
| Shower | Both (hygiene + self-respect) |
| Breakfast | Survival |
| Coffee | Neither—but keep under review if it enables virtue |

### Key Insight
The morning is colonized by external inputs (phone, news, email, podcasts). The only genuinely self-directed elements are physical care. Consider: what would a morning built around your own thoughts look like?

---

## Integration with Diogenes Expert

This skill should be invoked when the Diogenes expert encounters:
- Complaints about being overwhelmed
- Questions about what matters
- Lifestyle simplification requests
- Decision paralysis about commitments

May combine with:
- **lantern-audit**: After reducing, test if remaining values are actually practiced
- **nature-convention-analysis**: Examine whether "necessities" are natural or merely conventional

---

## Success Criteria

The skill is successfully applied when:

1. All dependencies are cataloged
2. Each is tested against both Diogenes criteria
3. Clear categories of action are produced
4. User has concrete next steps
5. The audit reveals something about priorities they hadn't articulated