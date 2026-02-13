---
name: scalability-decision-framework
description: Choose between approaches based on their ability to scale, transform, and transmit effectively—applying Tesla's insight about why AC defeated DC.
license: MIT
metadata:
  version: 1.0.1833
  author: sethmblack
keywords:
- scalability-decision-framework-(ac-vs-dc)
- structure
- transformation
- writing
---

# Scalability Decision Framework (AC vs DC)

Choose between approaches based on their ability to scale, transform, and transmit effectively—applying Tesla's insight about why AC defeated DC.

---

## When to Use

- Deciding between technical approaches or architectures
- Evaluating build vs. buy decisions
- Choosing between solutions that work now vs. solutions that scale
- User asks "Which approach scales better?" or "Will this solution scale?"
- Making foundational decisions that will be hard to reverse

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| options | Yes | The approaches or solutions being compared |
| current_needs | No | What's required now |
| future_needs | No | What might be required as scale increases |

---

## The AC vs DC Lesson

Edison's DC system worked. It powered Pearl Street Station. It lit Manhattan. But it couldn't scale.

DC Limitations:
- Fixed voltage—couldn't be transformed
- Short transmission range—about one mile from the power station
- Required power stations in every neighborhood
- Heavy copper cables for the fixed low voltage

Tesla's AC Advantages:
- Transformable—step up for transmission, step down for use
- Long transmission range—26 miles from Niagara Falls to Buffalo
- Centralized generation—one plant could serve a region
- Efficient—higher voltage means thinner wires

The DC system was simpler and worked immediately. The AC system required more upfront complexity but scaled to power civilization.

**The principle:** Choose the approach that transforms, transmits, and scales—even if it's harder initially.

---

## The Evaluation Framework

### Criterion 1: Transformability
Can the solution adapt to different contexts without rebuilding?

**AC characteristics:**
- Configurable for different use cases
- Abstraction layers that allow change
- Modular components that can be recombined

**DC characteristics:**
- Hard-coded for current use case
- Tightly coupled implementation
- Changes require rewrites

### Criterion 2: Transmission Distance
How far can the solution "reach" from its origin?

**AC characteristics:**
- Works across teams, departments, organizations
- Documentation and interfaces enable handoff
- Others can extend without understanding internals

**DC characteristics:**
- Only works for original creators
- Requires deep knowledge to use or modify
- Doesn't survive personnel changes

### Criterion 3: Efficiency at Scale
Does marginal cost decrease as usage increases?

**AC characteristics:**
- Fixed costs amortize over growing usage
- Performance improves or stays constant with scale
- Network effects benefit all users

**DC characteristics:**
- Linear or worse scaling—costs grow with usage
- Performance degrades under load
- Each new user adds overhead

### Criterion 4: Generation Centralization
Can you solve once and distribute, or must you solve repeatedly?

**AC characteristics:**
- Single source of truth
- Updates propagate automatically
- Consistency maintained centrally

**DC characteristics:**
- Duplicated solutions
- Updates require touching each instance
- Drift and inconsistency over time

### Criterion 5: Initial Complexity Trade-off
What's the upfront investment vs. long-term benefit?

**AC characteristics:**
- Higher initial complexity
- Requires more planning and design
- Pays off at scale

**DC characteristics:**
- Simple to start
- Fast initial delivery
- Becomes burden at scale

---

## Decision Matrix

For each option, score 1-5 on each criterion:

| Criterion | Option A | Option B | Notes |
|-----------|----------|----------|-------|
| Transformability | | | Can it adapt? |
| Transmission | | | Can others use it? |
| Scale Efficiency | | | Does marginal cost decrease? |
| Centralization | | | Solve once, benefit many? |
| Complexity Trade-off | | | Upfront cost vs. long-term gain |

**Scoring Guide:**
- 1: Strongly DC characteristics
- 3: Mixed characteristics
- 5: Strongly AC characteristics

**Threshold:** Total score above 15 suggests "AC" approach; below 15 suggests current needs may justify "DC" approach.

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
## Scalability Decision Framework

### Decision Context
[What is being decided]

### Options Under Evaluation
- **Option A:** [Description]
- **Option B:** [Description]

### Current vs. Future Needs
| Timeframe | Needs | Scale |
|-----------|-------|-------|
| Now | [Current requirements] | [Current scale] |
| 1 year | [Expected requirements] | [Expected scale] |
| 3+ years | [Projected requirements] | [Projected scale] |

### Evaluation Matrix

| Criterion | Option A | Option B | Analysis |
|-----------|----------|----------|----------|
| Transformability | [1-5] | [1-5] | [Why] |
| Transmission | [1-5] | [1-5] | [Why] |
| Scale Efficiency | [1-5] | [1-5] | [Why] |
| Centralization | [1-5] | [1-5] | [Why] |
| Complexity Trade-off | [1-5] | [1-5] | [Why] |
| **Total** | [Sum] | [Sum] | |

### Deep Analysis

**Transformability:**
[Detailed assessment of how each option adapts to changing needs]

**Transmission:**
[Detailed assessment of how each option travels beyond its creators]

**Scale Efficiency:**
[Detailed assessment of how costs and performance change at scale]

**Centralization:**
[Detailed assessment of solve-once-benefit-many potential]

**Complexity Trade-off:**
[Detailed assessment of upfront investment vs. long-term return]

### Risk Assessment
| Risk | Option A | Option B |
|------|----------|----------|
| Outgrow the solution | [Likelihood] | [Likelihood] |
| Stranded investment | [Likelihood] | [Likelihood] |
| Integration difficulties | [Likelihood] | [Likelihood] |

### The Verdict

**Recommended approach:** [Option]

**Reasoning:** [Why this option wins on scalability grounds]

**When to choose the other option:** [Circumstances where the losing option would be appropriate]

### Tesla's Judgment
[Summary in Tesla's voice—applying the AC/DC lesson to this decision]
```

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "We need to handle user authentication. Should we build our own system or use a third-party auth provider like Auth0?"

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


## Scalability Decision Framework

### Decision Context
Choosing between building custom authentication or adopting third-party auth provider (Auth0/Clerk/similar)

### Options Under Evaluation
- **Option A:** Build custom authentication system
- **Option B:** Adopt third-party auth provider (Auth0)

### Current vs. Future Needs
| Timeframe | Needs | Scale |
|-----------|-------|-------|
| Now | Basic email/password, maybe OAuth | 1,000 users |
| 1 year | SSO, MFA, team management | 50,000 users |
| 3+ years | Enterprise features, compliance, global | 500,000+ users |

### Evaluation Matrix

| Criterion | Option A (Custom) | Option B (Auth0) | Analysis |
|-----------|----------|----------|----------|
| Transformability | 4 | 5 | Custom can adapt but requires engineering; Auth0 has built-in options |
| Transmission | 2 | 5 | Custom knowledge stays with builders; Auth0 documented industry standard |
| Scale Efficiency | 2 | 5 | Custom requires security team growth; Auth0 scales without headcount |
| Centralization | 3 | 5 | Custom can be central but needs building; Auth0 is solve-once |
| Complexity Trade-off | 3 | 4 | Custom is simpler initially but burden grows; Auth0 has learning curve but pays off |
| **Total** | 14 | 24 | |

### Deep Analysis

**Transformability:**
Custom authentication can be modified endlessly, but each modification requires engineering time and security review. Auth0 provides MFA, SSO, social login, enterprise connections, and passwordless options out of the box. The third-party solution is more transformable in practice because the options already exist.

**Transmission:**
Custom auth knowledge lives in your engineers' heads. When they leave, the knowledge leaves. Auth0 has extensive documentation, community support, and is a known skill in the market. New hires can be productive quickly.

**Scale Efficiency:**
Custom auth requires ongoing security maintenance, vulnerability patching, and eventually a dedicated security team. Each 10x growth requires proportional investment. Auth0 costs grow with users but without linear headcount growth—they handle the security team overhead.

**Centralization:**
Auth0 has solved authentication for thousands of companies. Every security improvement they make benefits all customers. Custom auth means solving the same problems others have already solved.

**Complexity Trade-off:**
Custom auth is simpler on day one—just a users table and bcrypt. But compliance (SOC2), features (MFA), and enterprise requirements (SAML) add complexity that compounds. Auth0's initial learning curve is a one-time cost; custom auth's complexity is ongoing.

### Risk Assessment
| Risk | Option A (Custom) | Option B (Auth0) |
|------|----------|----------|
| Outgrow the solution | Medium—will need rebuilds | Low—enterprise scale is their business |
| Stranded investment | High—custom code has no resale value | Low—skills transfer, can migrate |
| Integration difficulties | Medium—depends on design | Low—standard protocols |
| Security breach | High—you own the attack surface | Low—they specialize in security |

### The Verdict

**Recommended approach:** Option B (Auth0)

**Reasoning:** Authentication is infrastructure, not differentiator. It must scale globally, handle security threats, and support enterprise requirements you can't predict today. This is exactly the case where "AC" wins—the upfront complexity of adopting a third-party system pays off in transformability, transmission, and scale efficiency.

**When to choose custom:** If authentication IS your product (you're building an auth provider), if you have extreme custom requirements no provider supports, or if you have a dedicated security team and compliance infrastructure already.

### Tesla's Judgment
You are asking whether to build a power station in every neighborhood or to transmit power from a central plant. The DC approach—custom authentication—works for a small area. But you speak of 500,000 users across enterprises with compliance requirements. You will need MFA, SSO, SAML, SCIM, and security practices you cannot yet name. Build custom, and you hire security engineers for the rest of your existence. Adopt the scalable solution, and authentication becomes like electricity from the wall—reliable, standardized, and someone else's expertise. Do not build your own power plant unless you are in the power business.

---

## Integration

This skill is part of the **Nikola Tesla** expert persona. Use it to choose approaches that scale like AC—transformable, transmittable, and efficient across distance.

"The present is theirs; the future, for which I really worked, is mine."