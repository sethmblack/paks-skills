---
name: variation-mapping
description: Systematically identify and catalog the variations within any population, system, or category. Variation is the raw material on which selection acts—without understanding what varies, you cannot pr...
license: MIT
metadata:
  version: 1.0.2176
  author: sethmblack
keywords:
- escalation
- variation-mapping
- writing
---

# Variation Mapping

Systematically identify and catalog the variations within any population, system, or category. Variation is the raw material on which selection acts—without understanding what varies, you cannot predict what will be selected.

---

## When to Use

- Starting analysis of any competitive system (market, organization, ideas)
- Before optimization—need to know what can be improved
- Understanding why some instances succeed and others fail
- User asks "What varies here?" or "What are the differences?"
- Seeking opportunities for differentiation or selection
- Mapping the landscape before making strategic decisions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| population | Yes | The group, system, or category to analyze |
| criteria | No | Specific dimensions of variation to examine |
| purpose | No | Why variation matters (informs which dimensions to emphasize) |

---

## Darwin's Insight on Variation

"These individual differences are highly important for us, as they afford materials for natural selection to accumulate."

Darwin saw what others missed: no two individuals are exactly alike. Where others saw uniform species, Darwin saw countless slight differences. This attention to variation—rather than averages or ideals—was the foundation of his revolutionary insight.

The same principle applies broadly: before you can understand selection, competition, or optimization in any system, you must first map what varies.

---

## The Variation Mapping Framework

### Step 1: Define the Population Boundaries

Clearly specify what you're examining:
- What entities are included?
- What defines membership in this population?
- What timeframe are you examining?
- At what level of analysis (individuals, groups, components)?

**Darwin example:** Not "birds" but "finches of the Galapagos Islands"—specific, bounded, observable.

### Step 2: Identify Dimensions of Variation

List the ways in which members of the population can differ:

**Physical/Structural dimensions:**
- Size, shape, composition
- Components and their arrangements
- Resources and capabilities

**Behavioral dimensions:**
- Actions and strategies
- Responses to conditions
- Patterns of interaction

**Relational dimensions:**
- Position relative to others
- Connections and dependencies
- Environmental fit

**Temporal dimensions:**
- Age, stage, history
- Rate of change
- Timing of actions

### Step 3: Catalog the Actual Variations

For each significant dimension, document:
- The range of variation (minimum to maximum)
- The distribution (are variations clustered or spread?)
- Notable outliers or extreme variants
- Common patterns vs. rare variants

**Key discipline:** Observe what IS, not what you expect. Darwin's genius was seeing variations others dismissed.

### Step 4: Assess Heritability/Transmissibility

Determine whether variations can be passed on:
- Which variations are inherited (genetic, cultural, structural)?
- Which arise anew in each generation (environmental, random)?
- What mechanisms transmit variations?

Variations that cannot be inherited are evolutionarily irrelevant—they can't accumulate.

### Step 5: Identify Variation Implications

Connect variations to outcomes:
- Which variations correlate with success/failure?
- Which variations are independent vs. linked?
- What does the variation landscape suggest about selection pressures?

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
## Variation Map: [Population]

### Population Definition
[Clear boundaries of what's being analyzed]

### Dimension Inventory

| Dimension | Type | Range | Distribution | Notes |
|-----------|------|-------|--------------|-------|
| [Dimension 1] | [Structural/Behavioral/etc.] | [Min-Max] | [Clustered/Spread/Bimodal] | [Key observations] |
| [Dimension 2] | ... | ... | ... | ... |

### Key Variations Identified

**High-impact variations:**
1. [Variation that appears consequential]
2. [Another significant variation]

**Overlooked variations:**
1. [Variation others miss that may matter]
2. [Subtle difference worth noting]

### Variation Distribution
[Describe the overall shape—are most variants clustered around an average, or widely spread? Are there distinct types?]

### Heritability Assessment
| Variation | Heritable? | Mechanism |
|-----------|-----------|-----------|
| [Variation 1] | Yes/No/Partial | [How it's transmitted] |

### Implications for Selection
[What does this variation map suggest about:
- What selection pressures might favor
- Where optimization opportunity exists
- What the population might evolve toward]

### Variation Gaps
[What variations are absent that might be possible? What "empty niches" exist in the variation space?]
```

---

## Types of Variation to Look For

### Continuous Variation
- Varies along a spectrum (size, speed, price)
- Measurable in degrees
- Selection can shift the mean gradually

### Discrete Variation
- Distinct categories (type A vs. type B)
- Selection favors one type over another
- Can lead to rapid population shifts

### Linked Variation
- Variations that co-occur
- Changing one changes another
- Constrains what selection can produce

### Cryptic Variation
- Not expressed under current conditions
- May become visible under changed circumstances
- Hidden potential for adaptation

---

## Constraints

- Variation mapping requires access to multiple instances—can't map variation from a single case
- Some variations are visible only under specific conditions
- Observer bias can cause you to miss unexpected variations
- The dimensions you choose to examine shape what you find
- Not all variation matters—focus on variations that could affect outcomes

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

**Input:** "I'm analyzing our customer support team to understand performance differences."

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


## Variation Map: Customer Support Team (Q4 Performance)

### Population Definition
15 customer support representatives, all handling tier-1 tickets, same product line, Q4 2025. Bounded by: role (CS rep), tier (1), timeframe (Oct-Dec 2025).

### Dimension Inventory

| Dimension | Type | Range | Distribution | Notes |
|-----------|------|-------|--------------|-------|
| Tickets resolved/day | Behavioral | 18-47 | Bimodal (peaks at 22 and 42) | Two distinct performance groups |
| Customer satisfaction | Relational | 3.2-4.9 | Right-skewed | Most above 4.0, few outliers |
| First-contact resolution | Behavioral | 45%-89% | Normal | Centered around 70% |
| Tenure (months) | Temporal | 2-48 | Spread | Mix of new and experienced |
| Handle time (avg min) | Behavioral | 4.2-12.8 | Bimodal | Fast vs. thorough approaches |
| Escalation rate | Behavioral | 3%-28% | Right-skewed | Most escalate rarely |
| Training hours completed | Structural | 0-40 | Left-skewed | Most minimal, few extensive |

### Key Variations Identified

**High-impact variations:**
1. Bimodal ticket resolution (22 vs. 42/day) suggests two distinct work styles
2. Handle time inversely correlates with volume but not with satisfaction
3. First-contact resolution varies 2x between best and worst performers

**Overlooked variations:**
1. Response language patterns (not currently measured)
2. Ticket type preferences (reps may be selecting easier tickets)
3. Time-of-day performance differences

### Variation Distribution
Team shows bimodal distribution on key metrics—not a normal curve around average, but two distinct clusters. This suggests different strategies/approaches rather than skill differences along a single dimension.

### Heritability Assessment
| Variation | Heritable? | Mechanism |
|-----------|-----------|-----------|
| Work style (fast vs. thorough) | Partial | Training, mentorship, culture |
| First-contact resolution | Yes | Training and knowledge base |
| Customer rapport | Partial | Some trainable, some temperament |

### Implications for Selection

The bimodal distribution suggests:
- Two viable strategies exist (high-volume/fast vs. lower-volume/thorough)
- Selection pressure (current metrics) may favor one over the other
- High performers in one style should not be pushed to adopt the other
- New hires might be sorted into styles based on aptitude

The volume/satisfaction independence is crucial—reps achieving 40+ tickets/day maintain high satisfaction. This variant represents an adaptive optimum.

### Variation Gaps
- No reps combining highest volume (47) with highest satisfaction (4.9)
- No testing of hybrid approaches (fast for simple tickets, thorough for complex)
- Night shift performance data absent—may reveal different variation patterns

*"I have been struck with how much the variations which I have found affect the reproductive success of individuals."*—The goal is not just to catalog but to identify variations that matter.

---

## Integration

This skill is part of the **Charles Darwin** expert persona. Use it as the foundation for any analysis involving competition, optimization, or selection. It pairs naturally with:
- **selection-pressure-analysis** to understand what forces act on these variations
- **severe-test-protocol** to test hypotheses about which variations matter
- **patient-accumulation-method** to gather comprehensive variation data