---
name: modular-integration-assessment
description: Determine whether a market or product category favors integrated or modular architectures, and predict architectural evolution for build-vs-buy and platform strategy decisions.
license: MIT
metadata:
  version: 1.0.1464
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- modular-integration-assessment
- structure
- writing
---

# Modular-Integration Assessment

Determine whether a market or product category favors integrated or modular architectures, and predict architectural evolution for build-vs-buy and platform strategy decisions.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Make definitive architectural predictions without acknowledging uncertainty
- Ignore the "good enough" question that determines architecture evolution
- Apply this framework to decisions where it does not fit

**If misapplied:** Explain that modular-integration dynamics depend on whether products are "good enough" for customer needs.

---

## When to Use

- User asks "Should we build or buy?"
- User asks "Is this market commoditizing?"
- User asks "Will this platform become modular?"
- User asks "What's the future architecture?"
- Making platform vs component strategy decisions
- Evaluating vendor lock-in vs flexibility tradeoffs
- Predicting industry structure evolution

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **product_category** | Yes | The product, technology, or industry being analyzed |
| **customer_needs** | Yes | What customers require from this product |
| **current_performance** | Yes | How well current offerings meet customer needs |
| **interface_stability** | No | How standardized are the interfaces between components |

---

## Workflow

### Step 1: Assess "Good Enough" Status

Determine where the product is on the trajectory:
- **Not good enough:** Products do not fully meet customer needs on the dimensions that matter most
- **More than good enough:** Products exceed what customers need on traditional dimensions; overshoot

### Step 2: Map Current Architecture

Identify the dominant architecture:
- **Integrated/Interdependent:** Proprietary interfaces, components optimized together, tight coupling
- **Modular:** Standardized interfaces, components from different vendors, loose coupling

### Step 3: Predict Evolutionary Direction

Apply the theory:
- **Not good enough + Integrated = Stable:** Integration wins because it allows cross-component optimization
- **Not good enough + Modular = Shifting to integrated:** Expect integration/consolidation
- **More than good enough + Integrated = Shifting to modular:** Expect commoditization, standardization
- **More than good enough + Modular = Stable:** Modularity wins because components are interchangeable

### Step 4: Assess Interface Stability

Examine the interfaces:
- Are interfaces well-defined and standardized?
- Is innovation happening at interfaces or within components?
- Who controls interface definitions?

### Step 5: Recommend Strategy

Based on position and direction:
- Build vs buy decisions
- Integration vs flexibility tradeoffs
- Where to invest and where to buy commodity

---

## Outputs

### Modular-Integration Assessment Report

```markdown
## Modular-Integration Assessment: [Product/Industry Name]

### "Good Enough" Assessment

**Current status:** [Not Good Enough | Good Enough | More Than Good Enough]

**Evidence:**
- Customer satisfaction on core dimensions: [assessment]
- Performance improvements that customers ignore: [evidence of overshoot]
- Unmet needs driving purchases: [what customers still want]

### Current Architecture

**Dominant pattern:** [Integrated | Modular | Mixed]

**Architecture map:**
| Component | Integration Status | Interface Type |
|-----------|-------------------|----------------|
| [Component 1] | [Integrated/Modular] | [Proprietary/Standard] |
| [Component 2] | [Integrated/Modular] | [Proprietary/Standard] |
| [Component 3] | [Integrated/Modular] | [Proprietary/Standard] |

### Evolutionary Direction

**Current position:** [Quadrant description]
**Predicted direction:** [Toward integration | Toward modularization | Stable]
**Confidence:** [High | Medium | Low]

**Driving forces:**
- [What is pushing toward current direction]
- [What could change the trajectory]

### Timeline Estimate

| Phase | Architecture State | Timeframe |
|-------|-------------------|-----------|
| Current | [description] | Now |
| Near-term | [description] | [1-3 years] |
| Long-term | [description] | [3-10 years] |

### Strategic Implications

**For build vs buy:**
- Components to build (where integration matters): [list]
- Components to buy (where modular is sufficient): [list]

**For platform strategy:**
- Where to control interfaces: [where and why]
- Where to adopt standards: [where and why]

**For investment prioritization:**
- Where integration creates value: [areas]
- Where commodity purchase is appropriate: [areas]

### Historical Parallel

[Reference relevant example: PC industry, cloud, mobile, etc.]

### Oscillation Warning

This analysis reflects current position. Architecture is cyclical:
- Modularization leads to commoditization
- Commoditization shifts competition to new dimensions
- New dimensions require integration
- Integration leads to "good enough"
- Cycle continues

### Recommendations

1. [Specific recommendation for the analyzed category]
2. [Specific recommendation]
3. [Specific recommendation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Multiple components at different stages | Assess each component separately; provide composite view |
| "Good enough" is subjective | Identify which customer segments and for which dimensions |
| Architecture is mixed | Common situation; identify where integration and modularization matter most |
| Rapid technology change | Note that trajectories can shift; identify trigger events |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Should we build our own ML infrastructure or use cloud services?"

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


## Modular-Integration Assessment: ML Infrastructure

### "Good Enough" Assessment

**Current status:** Mixed - Depends on use case

| Use Case | Status | Rationale |
|----------|--------|-----------|
| Standard ML training | Good Enough | Cloud offerings meet most needs |
| Large-scale training (LLMs) | Not Good Enough | Performance, cost, customization still matter |
| Inference at scale | Good Enough | Commodity services work well |
| Edge/specialized inference | Not Good Enough | Custom optimization still valuable |

### Current Architecture

**Dominant pattern:** Shifting from modular to re-integration at scale

**Architecture map:**
| Component | Integration Status | Interface Type |
|-----------|-------------------|----------------|
| Compute (GPUs) | Modular | Standardized APIs |
| Training frameworks | Modular | Open source standards |
| ML platforms | Mixed | Cloud proprietary + OSS |
| Large-scale orchestration | Integrating | Custom at hyperscaler level |
| Serving infrastructure | Modular | Container/Kubernetes standard |

### Evolutionary Direction

**Current position:** Modular for most use cases, integrating at frontier
**Predicted direction:** Continued modularization for standard use cases; integration at the frontier
**Confidence:** Medium

**Driving forces:**
- Commoditization of standard ML workflows (toward modular)
- Massive scale requirements for frontier models (toward integration at top end)
- Open source tooling maturing (toward modular)
- Hyperscaler investment in proprietary systems (toward integration for their platforms)

### Timeline Estimate

| Phase | Architecture State | Timeframe |
|-------|-------------------|-----------|
| Current | Modular for 80%, integrated for frontier 20% | Now |
| Near-term | Modular for 90%, integrated for frontier | 2-3 years |
| Long-term | Highly modular for standard ML, integrated for next frontier | 5+ years |

### Strategic Implications

**For build vs buy:**
- Components to build (where integration matters):
  - Large-scale training orchestration (if you're at frontier scale)
  - Specialized inference for your specific use case
  - Data pipelines unique to your domain
- Components to buy (where modular is sufficient):
  - Standard ML training compute
  - General inference infrastructure
  - ML frameworks and libraries
  - Monitoring and observability

**For platform strategy:**
- Where to control interfaces: Your data pipelines, model deployment integration with your product
- Where to adopt standards: Training frameworks, container orchestration, general compute

**For investment prioritization:**
- Where integration creates value: Your specific ML application, not general infrastructure
- Where commodity purchase is appropriate: Everything that is not your core differentiation

### Historical Parallel

PC industry: When PCs were "not good enough," integrated players (Apple, early IBM) had advantages. As PCs became "good enough," modular architecture won (Dell, commodity parts). Cloud is similar: early cloud was integrated; as it becomes "good enough," some modularization occurs (multi-cloud, cloud-agnostic tooling).

### Oscillation Warning

ML infrastructure is not uniformly modular or integrated. The frontier is always integrated (because it's not good enough), but yesterday's frontier becomes today's commodity. GPUs were the frontier; now they are commodity. Large-scale training is the frontier now.

### Recommendations

1. **Use cloud ML services for standard workloads** - These are "good enough" and modular; building your own creates cost without differentiation
2. **Invest in integration at your application layer** - Where ML meets your specific product is where integration creates value
3. **Monitor the "good enough" threshold** - If your needs move to frontier, integration may become necessary
4. **Avoid lock-in on commodity layers** - Use open standards and multi-cloud where services are "good enough"

---

## Integration

This skill applies Clayton Christensen's modular-interdependent theory from The Innovator's Solution. Key insight: architecture is not static. Products oscillate between integration and modularization based on whether they are "good enough." Position your strategy for where the market is heading, not just where it is today.