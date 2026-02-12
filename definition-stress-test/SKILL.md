---
name: definition-stress-test
description: Test whether definitions, categories, or criteria are robust by finding
  absurd edge cases that technically satisfy the definition but violate its intent—exposing
  weaknesses before they cause problems.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- definition-stress-test
- writing
---

# Definition Stress Test

Test whether definitions, categories, or criteria are robust by finding absurd edge cases that technically satisfy the definition but violate its intent—exposing weaknesses before they cause problems.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use edge cases to dismiss legitimate concepts through sophistry
- Generate edge cases for harmful categories (e.g., testing definitions that could enable discrimination)
- Present gotchas as wisdom when the definition is actually functional

**Integrity Requirements:**
1. Apply the test fairly to the definition as actually used
2. Acknowledge when definitions are robust enough for their purpose
3. Offer constructive refinements, not just critique

---

## When to Use

- Evaluating definitions in policies, criteria, or specifications
- Testing hiring criteria before use
- Reviewing legal or contractual language
- Auditing taxonomies and classification systems
- Checking if categories will hold up in practice
- Preventing "letter of the law" violations of intent

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **definition** | Yes | The definition, category, or criteria to test |
| **purpose** | No | What the definition is trying to accomplish |

---

## Workflow
### Step 1: 1. State the Definition Clearly

Capture the exact definition being tested:

**Template:** "[Term] is defined as [criteria/conditions]"

Identify:
- Necessary conditions (must have)
- Sufficient conditions (enough to qualify)
- Boundary markers (what's excluded)

### Step 2: 2. Find the Plucked Chicken

Generate edge cases that:
- Technically satisfy all stated criteria
- Are clearly absurd or unintended
- Expose what the definition failed to capture

**The Diogenes Method:** When Plato defined "man" as a "featherless biped," Diogenes plucked a chicken and presented it: "Behold, Plato's man!"

**Edge Case Categories:**
| Type | Method |
|------|--------|
| Literal compliance | Follow letter while violating spirit |
| Boundary straddling | Find cases exactly at the edge |
| Unexpected satisfiers | What else technically qualifies? |
| Missing exclusions | What should be out but isn't? |
| Context collapse | Would this work in a different context? |

### Step 3: 3. Expose the Weakness

For each edge case, articulate:
- Why it technically satisfies the definition
- Why it violates the apparent intent
- What the definition failed to specify

### Step 4: 4. Suggest Refinements

Propose how to strengthen the definition:
- Additional necessary conditions
- Explicit exclusions
- Intent clauses
- Context boundaries

---

## Outputs

Format the output as:

```markdown
## Definition Stress Test: [Term]

**Definition Under Test:**
"[exact definition]"

**Apparent Intent:**
[what the definition seems to be trying to accomplish]

### Edge Cases Found

#### 1. [Edge Case Name]
**The Case:** [description]
**Why It Technically Qualifies:** [how it meets stated criteria]
**Why It's Absurd:** [how it violates intent]
**Weakness Exposed:** [what the definition failed to capture]

#### 2. [Edge Case Name]
[repeat structure]

### Robustness Assessment
- [ ] Definition is robust for its purpose
- [ ] Minor refinements needed
- [ ] Significant gaps exist
- [ ] Definition is fundamentally flawed

### Suggested Refinements
| Current Gap | Proposed Addition |
|-------------|-------------------|
| [weakness] | [fix] |

### Refined Definition
"[improved definition incorporating fixes]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Definition withstands all tests | Report it as robust; this is success |
| Edge cases are unrealistic | Note unreality but still document the gap |
| Definition is purpose-built for specific context | Test within that context |
| Definition is intentionally broad | Test whether breadth is feature or bug |

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

**Input:** "Test this hiring criterion: 'Candidates must have 5+ years of relevant experience'"

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


## Definition Stress Test: "5+ Years Relevant Experience"

**Definition Under Test:**
"Candidates must have 5+ years of relevant experience"

**Apparent Intent:**
Ensure candidates have sufficient depth of practice to perform at senior level

### Edge Cases Found

#### 1. The Plucked Chicken: Repeated Year One
**The Case:** Candidate with 5 years at same job doing same tasks, never growing
**Why It Technically Qualifies:** 5 years have elapsed; work was in the field
**Why It's Absurd:** 1 year of experience repeated 5 times ≠ 5 years of growth
**Weakness Exposed:** "Years" measures time, not learning or capability

#### 2. The Adjacent Dabbler
**The Case:** 5 years in adjacent field with occasional overlap
**Why It Technically Qualifies:** "Relevant" is undefined; they can argue relevance
**Why It's Absurd:** Tangential experience may not transfer
**Weakness Exposed:** "Relevant" needs definition

#### 3. The Credential Without Practice
**The Case:** 5 years employed in role but minimal actual practice (management, leave, etc.)
**Why It Technically Qualifies:** 5 years on the payroll in the title
**Why It's Absurd:** Title ≠ practice
**Weakness Exposed:** Employment duration ≠ practice hours

#### 4. The Prodigy Exclusion
**The Case:** Exceptional candidate with 3 years who outperforms 10-year veterans
**Why They Don't Qualify:** Fails the 5-year threshold
**Why It's Absurd:** Capability exists; arbitrary cutoff excludes it
**Weakness Exposed:** Time proxy may exclude best candidates

### Robustness Assessment
- [ ] Definition is robust for its purpose
- [ ] Minor refinements needed
- [x] Significant gaps exist
- [ ] Definition is fundamentally flawed

### Suggested Refinements
| Current Gap | Proposed Addition |
|-------------|-------------------|
| Time ≠ learning | Add "progressive responsibility" or "demonstrated growth" |
| "Relevant" undefined | Specify which domains/skills count |
| Title ≠ practice | Add "hands-on" or specify practice hours |
| Excludes prodigies | Add "or equivalent demonstrated capability" |

### Refined Definition
"Candidates must demonstrate 5+ years of progressive, hands-on experience in [specific domains], OR equivalent capability demonstrated through [portfolio/test/references]"

---

## Integration with Diogenes Expert

This skill should be invoked when the Diogenes expert encounters:
- Definitions that seem too neat
- Categories being used to include/exclude
- Policies or criteria under development
- Arguments that depend on precise definitions

May combine with:
- **lantern-audit**: Test if the definition is even followed in practice
- **barrel-reduction**: Eliminate unnecessary definitional complexity

---

## Success Criteria

The skill is successfully applied when:

1. The definition is accurately stated
2. Multiple edge cases are generated
3. Each edge case's absurdity is clearly articulated
4. Weaknesses are precisely identified
5. Constructive refinements are offered