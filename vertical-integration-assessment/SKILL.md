---
name: vertical-integration-assessment
description: Analyze dependencies in a system or business and recommend integration
  strategies to reduce vulnerability, cost, and loss of control.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- vertical-integration-assessment
- writing
---

# Vertical Integration Assessment

Analyze dependencies in a system or business and recommend integration strategies to reduce vulnerability, cost, and loss of control.

**Token Budget:** ~600 tokens
**Origin:** John D. Rockefeller methodology (Standard Oil vertical integration strategy)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend integration that creates harmful monopolies
- Suggest acquiring or controlling suppliers unethically
- Ignore antitrust or regulatory considerations
- Prioritize control over customer or stakeholder welfare

**If asked to apply this skill harmfully:** Refuse explicitly. Integration serves efficiency, not domination.

---

## When to Use

- User asks "What should we build vs. buy?"
- Vendor dependency review needed
- Supply chain vulnerability analysis
- Platform strategy decisions
- User asks "Where are we vulnerable to third parties?"
- Strategic sourcing decisions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system, business, or process to assess |
| dependencies | No | Known external dependencies (will identify if not provided) |
| strategic_goals | No | What outcomes integration should serve |
| constraints | No | Limits on integration (budget, capability, regulatory) |

---

## Workflow

### Step 1: Map the Value Chain

Document all stages from input to customer:

```
[Source] → [Processing] → [Distribution] → [Customer]
```

For each stage, identify:
- Who controls it? (Internal/External)
- What is the cost?
- What is the risk of disruption?
- What is the strategic importance?

### Step 2: Assess Each Dependency

For each external dependency, evaluate:

| Dimension | Questions |
|-----------|-----------|
| **Substitutability** | Can you switch providers easily? Are there alternatives? |
| **Cost Impact** | What margin does the vendor capture? What would self-provision cost? |
| **Risk Exposure** | What happens if this provider fails or changes terms? |
| **Strategic Value** | Is this core to your differentiation or commodity? |
| **Capability Gap** | Do you have or could you build the capability internally? |

### Step 3: Classify Integration Options

Place each dependency in the matrix:

|  | High Strategic Value | Low Strategic Value |
|--|---------------------|---------------------|
| **High Vulnerability** | INTEGRATE (Priority 1) | DIVERSIFY (reduce risk) |
| **Low Vulnerability** | EVALUATE (potential future) | MAINTAIN (status quo acceptable) |

### Step 4: Analyze Integration Paths

For each INTEGRATE candidate:

1. **Build** - Develop capability internally
   - Pros: Full control, customization, no margin to vendor
   - Cons: Time, expertise required, maintenance burden

2. **Acquire** - Purchase the provider or capability
   - Pros: Immediate capability, existing expertise
   - Cons: Cost, integration complexity, culture

3. **Partner** - Deep strategic relationship short of ownership
   - Pros: Shared risk, maintained flexibility
   - Cons: Incomplete control, aligned incentives required

### Step 5: Recommend with Rationale

For each recommendation:
- State the dependency clearly
- Quantify the vulnerability/cost
- Recommend integration path
- Project benefits and costs
- Note implementation requirements

---

## Outputs

Format the assessment as:

```markdown
## Vertical Integration Assessment: [System/Business]

### Value Chain Map

```
[Visual representation of stages and control points]
```

### Dependency Inventory

| Dependency | Controller | Annual Cost | Risk Level | Strategic Value |
|------------|------------|-------------|------------|-----------------|
| [Name] | [Who] | [$X] | [H/M/L] | [H/M/L] |

### Integration Matrix

#### INTEGRATE (Priority)
| Dependency | Path | Rationale | Projected Benefit |
|------------|------|-----------|-------------------|
| [Name] | Build/Acquire/Partner | [Why] | [$X or capability] |

#### DIVERSIFY (Risk Reduction)
| Dependency | Action | Rationale |
|------------|--------|-----------|
| [Name] | [Add alternatives] | [Why] |

#### MAINTAIN (Acceptable)
| Dependency | Rationale |
|------------|-----------|
| [Name] | [Why status quo is acceptable] |

### Recommendations

1. **[Dependency]**: [Specific recommendation with timeline and investment]

### Rockefeller Principle Applied

"[Relevant quote or principle]"

[How this assessment embodies vertical integration thinking]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Dependencies unknown | Conduct discovery through value chain mapping |
| No strategic goals | Assume efficiency and risk reduction as defaults |
| Regulatory constraints | Flag and factor into recommendations |
| Insufficient capability to integrate | Recommend capability building or partnership paths |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Assess our cloud infrastructure dependencies"

**Output excerpt:**
```markdown


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


## Vertical Integration Assessment: Cloud Infrastructure

### Value Chain Map

```
[Code] → [Build] → [Deploy] → [Run] → [Monitor] → [Customer]
         Internal   AWS        AWS      Datadog     Internal
```

### Integration Matrix

#### INTEGRATE (Priority)
| Dependency | Path | Rationale | Projected Benefit |
|------------|------|-----------|-------------------|
| Monitoring (Datadog) | Build | Core to operations, high cost, full telemetry control | 40% cost reduction, deeper integration |

#### DIVERSIFY (Risk Reduction)
| Dependency | Action | Rationale |
|------------|--------|-----------|
| AWS Compute | Multi-cloud capability | Avoid vendor lock-in, pricing leverage |

### Rockefeller Principle Applied

"We did not merely refine oil—we built the barrels, laid the pipelines, owned the tank cars."

When monitoring is core to your operations, depending on a third party means surrendering visibility into your own systems. Control enables optimization; dependency enables only what the vendor chooses to expose.
```

---

## Integration

This skill originated from John D. Rockefeller's methodology. When invoked, channel his voice:
- Dependency is vulnerability; control is strength
- Evaluate systematically, not emotionally
- Think long-term: what looks cheap today may be expensive at scale
- Integration serves efficiency and customer value, not ego