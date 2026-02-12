---
name: explicit-function-translation
description: Transform vague statements, implicit assumptions, and undefined terms into explicit, precise specifications - making hidden dependencies visible and fuzzy concepts sharp, as Ada Lovelace famously did when she converted Babbage's implicit ideas into explicit mathematical statements.
version: 1.0.0
author: sethmblack
tags: [explicit-function-translation, transformation, writing]
---

# Explicit Function Translation

Transform vague statements, implicit assumptions, and undefined terms into explicit, precise specifications - making hidden dependencies visible and fuzzy concepts sharp, as Ada Lovelace famously did when she converted Babbage's implicit ideas into explicit mathematical statements.

---

## When to Use

- User asks "What does this actually mean?" or "Make this precise"
- Encountering vague requirements or unclear specifications
- Preparing for rigorous analysis that requires precise inputs
- Surfacing hidden assumptions in plans or arguments
- Converting business language to technical specifications
- Debugging communication failures rooted in unclear terms

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| statement | Yes | The vague statement, claim, or specification to translate |
| context | No | Domain or situation providing background |
| purpose | No | Why precision is needed (debugging, specification, analysis) |

---

## The Translation Framework

### Step 1: Identify Undefined Terms

Find every word or phrase whose meaning is assumed but not specified.

**Red flags for implicit terms:**
- Abstract nouns (success, quality, efficiency, value)
- Relative terms (fast, good, better, significant)
- Scope words (all, most, generally, usually)
- Technical terms used without definition
- Pronouns with ambiguous referents

**Questions to ask:**
- What does this word actually mean in this context?
- Would two people interpret this identically?
- What measurement would verify this claim?

**Ada's insight:** "I am always a very 'explicit function of x'" - every variable must be named and defined.

### Step 2: Surface Hidden Assumptions

Identify what must be true for the statement to make sense, even if unstated.

**Common hidden assumptions:**
- Existence assumptions (that something exists or is possible)
- Scope assumptions (what's included/excluded)
- Temporal assumptions (when, how long, in what order)
- Causal assumptions (what causes what)
- Value assumptions (what matters, what's prioritized)

**Questions to ask:**
- What must be true for this to work?
- What conditions are taken for granted?
- What's the implied "if" before this "then"?

**Ada's insight:** Babbage was often "implicit" in what he said. Making the implicit explicit was half the analytical work.

### Step 3: Specify Quantitative Bounds

Convert qualitative statements to quantitative where possible.

**Translation patterns:**
- "Fast" -> "Completes in under X seconds"
- "Most users" -> "Greater than Y% of users"
- "Significant impact" -> "Change of at least Z in metric M"
- "Reliable" -> "Fails no more than N times per period P"

**Questions to ask:**
- What number would make this true/false?
- How would we measure this?
- What's the threshold between success and failure?

### Step 4: Eliminate Ambiguous Scope

Clarify exactly what's included and excluded.

**Scope clarifications:**
- Which entities are covered? (all users? some users? which ones?)
- What time period applies?
- What conditions must hold?
- What exceptions exist?

**Questions to ask:**
- Does this apply to X? (test boundary cases)
- What's the smallest case this covers?
- What's the largest case this covers?
- What's explicitly outside scope?

### Step 5: State Dependencies and Preconditions

Make explicit what must be true before the statement applies.

**Dependency types:**
- Inputs required
- States that must hold
- Resources that must be available
- Preceding steps that must complete

**Questions to ask:**
- What must happen first?
- What resources are assumed available?
- Under what conditions does this apply?

### Step 6: Reformulate as Explicit Specification

Rewrite the original statement with all ambiguity resolved.

**Explicit statement structure:**
```
Given [preconditions],
When [trigger/context],
Then [precise outcome],
Where [term] means [definition],
Assuming [explicit assumptions],
Excluding [what's not covered].
```

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
## Explicit Function Translation

### Original Statement
"[The vague statement being translated]"

### Undefined Terms Identified
| Term | Problem | Clarification Needed |
|------|---------|---------------------|
| [term] | [why it's vague] | [question to resolve] |

### Hidden Assumptions Surfaced
1. **[Assumption]:** [What's taken for granted]
   - *If false:* [How this changes the statement]

### Quantitative Translation
| Original | Explicit Version |
|----------|-----------------|
| [qualitative] | [quantitative] |

### Scope Clarification
- **Includes:** [What's covered]
- **Excludes:** [What's not covered]
- **Boundary cases:** [Edge situations and their treatment]

### Dependencies and Preconditions
- [Precondition 1]
- [Precondition 2]

### Explicit Reformulation
"[Complete, precise restatement of the original]"

### Remaining Ambiguities
[Any aspects that still require clarification from the source]
```

---

## Constraints

- Don't over-specify where flexibility is intended
- Distinguish precision from false precision
- Maintain the intent of the original while adding clarity
- Flag genuine ambiguities rather than resolving them arbitrarily
- Some statements may be intentionally vague - note this if so

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

**Input:** "The system should be fast and user-friendly."

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


## Explicit Function Translation

### Original Statement
"The system should be fast and user-friendly."

### Undefined Terms Identified
| Term | Problem | Clarification Needed |
|------|---------|---------------------|
| system | What system? Which components? | Which specific system or subsystem? |
| fast | Relative to what? What operations? | What response times? For what operations? |
| user-friendly | Subjective; for which users? | What specific UX criteria? Measured how? |
| should | Requirement? Aspiration? | Is this mandatory or nice-to-have? |

### Hidden Assumptions Surfaced
1. **Users exist and are defined:** Who are the users? Technical? General public?
   - *If false:* "User-friendly" has no referent
2. **Speed and friendliness are independent:** We can optimize both
   - *If false:* May need to trade off between them
3. **Current system is slow/unfriendly:** This is an improvement
   - *If false:* Requirement may already be met
4. **Standard hardware/network:** Performance assumes typical conditions
   - *If false:* Requirements need environment specification

### Quantitative Translation
| Original | Explicit Version |
|----------|-----------------|
| "fast" | Page load under 2 seconds on 4G connection; API responses under 200ms |
| "user-friendly" | Task completion rate >90% for new users; SUS score >80; error recovery <30 seconds |

### Scope Clarification
- **Includes:** Web application front-end, primary user workflows
- **Excludes:** Admin interfaces, batch processing, edge case workflows
- **Boundary cases:**
  - Mobile vs. desktop: Both must meet criteria
  - Peak load: Must maintain performance at 10x average load
  - Accessibility: Must meet WCAG 2.1 AA standards

### Dependencies and Preconditions
- Users have modern browsers (last 2 versions of Chrome, Firefox, Safari, Edge)
- Network connectivity of at least 4G/broadband
- Backend services are available and performing to SLA

### Explicit Reformulation
"The customer-facing web application shall:
1. Load initial page content in under 2 seconds on a 4G mobile connection
2. Respond to user interactions within 200ms under normal load
3. Maintain these performance levels at up to 10x average concurrent users
4. Enable new users to complete primary workflows (account creation, purchase, support request) with >90% success rate without assistance
5. Achieve a System Usability Scale score of 80 or higher in user testing
6. Allow users to recover from errors within 30 seconds on average
7. Meet WCAG 2.1 AA accessibility standards

These requirements apply to Chrome, Firefox, Safari, and Edge (last 2 versions) on both desktop and mobile platforms, assuming backend services are meeting their SLAs."

### Remaining Ambiguities
- "Primary workflows" needs enumeration from product team
- Performance under degraded backend conditions not specified
- Target user population for usability testing not defined

---

## Integration

This skill is part of the **Ada Lovelace** expert persona. Use it when vagueness threatens precision - the very work Ada performed in translating Babbage's implicit vision into the explicit operations of the first computer program.