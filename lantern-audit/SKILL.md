---
name: lantern-audit
description: Expose gaps between stated values and actual behavior by designing and performing literal tests that reveal hypocrisy, forcing confrontation between what is claimed and what is practiced.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4357
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- lantern-audit
- writing
---

# Lantern Audit

Expose gaps between stated values and actual behavior by designing and performing literal tests that reveal hypocrisy, forcing confrontation between what is claimed and what is practiced.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for audit output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design tests that violate laws or safety
- Use results to publicly humiliate individuals without their consent
- Apply the method to strawman or misrepresent stated values

**Integrity Requirements:**
1. Test the value as actually stated, not a distorted version
2. Acknowledge when values ARE being practiced
3. Distinguish between hypocrisy and honest struggle

---

## When to Use

- Organizational values seem performative ("We value X" but...)
- Culture doesn't match marketing
- Personal values feel hollow
- Evaluating whether an institution practices what it preaches
- Testing your own integrity
- Due diligence on organizations claiming certain values

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **stated_value** | Yes | The value, principle, or claim to test |
| **context** | No | The organization, person, or situation making the claim |

---

## Workflow
### Step 1: 1. Identify the Stated Value

Capture the exact claim being made:

**Examples:**
- "We value innovation"
- "I'm committed to work-life balance"
- "This company puts customers first"
- "We believe in transparency"

Document where and how the value is stated (mission statement, speech, policy, personal claim).

### Step 2: 2. Design the Literal Test

Create a test that takes the value at its word:

**The Diogenes Method:** If this value were literally true, what would I be able to observe?

| Value Claimed | Literal Test |
|---------------|--------------|
| "We value innovation" | Walk through asking "where do the innovators sit?" |
| "Open door policy" | Walk through every open door |
| "Customer obsession" | Ask any employee to name three recent customer complaints |
| "We value diversity" | Count who speaks in meetings, who gets promoted |

**Test Design Principles:**
- Make it observable, not theoretical
- Make it simple enough to actually perform
- Make the gap undeniable if it exists

### Step 3: 3. Perform the Test

Actually do it, not as a thought experiment:

**Documentation:**
- What happened when you tried?
- Who responded how?
- What obstacles appeared?
- What excuses were offered?

### Step 4: 4. Let the Absurdity Speak

Present findings without editorializing—the gap exposes itself:

**Template:** "You stated [value]. I tested by [method]. I found [result]. The distance between the two is [observable gap]."

---

## Outputs

Format the output as:

```markdown
## Lantern Audit: [Value]

**Value Claimed:** "[exact statement]"
**Source:** [where/when stated]

**Test Designed:**
[Description of literal test]

**Test Performed:**
[What actually happened]

**Gap Analysis:**
| Claimed | Observed | Distance |
|---------|----------|----------|
| [what was promised] | [what was found] | [the gap] |

**Diagnosis:**
- [ ] Value practiced consistently
- [ ] Value practiced inconsistently
- [ ] Value stated but not practiced
- [ ] Value contradicted by practice

**Evidence:**
[Specific observations that support the diagnosis]

**The Lantern Verdict:**
[One-sentence statement of what the test revealed]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Value IS being practiced | Acknowledge it—this is a finding, not a failure |
| Test cannot be safely performed | Design alternative observable test |
| Value is too vague to test | Ask for clarification on what it would look like in practice |
| Partial practice | Document the boundaries—where does practice stop? |

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

**Input:** "Test whether my company actually values 'psychological safety' as stated in our handbook"

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


## Lantern Audit: Psychological Safety

**Value Claimed:** "We maintain a culture of psychological safety where every voice matters"
**Source:** Employee handbook, page 3; CEO all-hands speech Q1

**Test Designed:**
In the next three meetings, observe:
1. Who speaks first and most
2. What happens when junior people disagree with senior people
3. Whether "bad news" is welcomed or punished

**Test Performed:**
- Meeting 1 (team sync): Same 3 people spoke 80% of the time. When intern raised concern, was told "let's take that offline"
- Meeting 2 (project review): Developer mentioned timeline risk, was asked "why didn't you flag this sooner?" in sharp tone
- Meeting 3 (brainstorm): Silence when asked for "wild ideas"; only safe suggestions offered

**Gap Analysis:**
| Claimed | Observed | Distance |
|---------|----------|----------|
| Every voice matters | 3 voices dominate | 27 employees silent |
| Safe to disagree | Disagreement redirected | "Offline" = buried |
| Welcome bad news | Bad news blamed | Shoot messenger |

**Diagnosis:**
- [ ] Value practiced consistently
- [ ] Value practiced inconsistently
- [x] Value stated but not practiced
- [ ] Value contradicted by practice

**Evidence:**
- Junior voices systematically silenced or redirected
- Risk-raising punished with blame
- "Wild ideas" request met with protective silence

**The Lantern Verdict:**
Psychological safety exists in the handbook but not in the room. The company has written a value it does not practice.

---

## Integration with Diogenes Expert

This skill should be invoked when the Diogenes expert encounters:
- Claims about values that seem hollow
- Requests to evaluate organizational culture
- Personal integrity checks
- Situations where words and actions diverge

May combine with:
- **barrel-reduction**: After exposing gaps, eliminate the pretense
- **definition-stress-test**: Test whether the value is even coherently defined

---

## Success Criteria

The skill is successfully applied when:

1. The stated value is accurately captured
2. A literal, observable test is designed
3. The test is actually performed (or clearly could be)
4. Findings are documented without editorializing
5. The gap (or lack thereof) speaks for itself