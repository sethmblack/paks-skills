---
name: variable-control-analysis
description: Identify hidden variables causing inconsistent results. When outcomes vary unexpectedly, systematically isolate the source of variation rather than dismissing results as random or the method as unr...
license: MIT
metadata:
  version: 1.0.2175
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- variable-control-analysis
- writing
---

# Variable Control Analysis

Identify hidden variables causing inconsistent results. When outcomes vary unexpectedly, systematically isolate the source of variation rather than dismissing results as random or the method as unreliable.

---

## When to Use

- User reports inconsistent results from the "same" process
- Experiments or tests are not reproducible
- User asks "Why do I get different results each time?"
- Request to "debug" an experiment or process
- Results that "should" match don't match
- User asks "What am I not controlling for?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| inconsistent_results | Yes | Description of the varying outcomes |
| known_conditions | No | What the user knows about each run |
| what_was_tried | No | Previous debugging attempts |

---

## The Variable Control Framework

### Step 1: Accept That Something Differs

The foundational principle: if results differ, conditions differ.

Franklin's discovery: DNA diffraction patterns were inconsistent because humidity varied. What appeared random was systematic—A-form at low humidity, B-form at high humidity. The "noise" was signal.

**Starting assumption:** Identical conditions produce identical results. Different results mean conditions were not identical.

### Step 2: Inventory All Possible Variables

List every factor that could conceivably affect the outcome:

**Categories to consider:**
- **Environmental** — Temperature, humidity, time of day, location
- **Input** — Source, preparation, age, batch
- **Process** — Sequence, timing, operator, tools
- **Measurement** — Instrument, calibration, observer, reading method
- **State** — Prior operations, memory, accumulated effects

**Key question:** What could be different between runs, even if I think it's the same?

### Step 3: Document Each Instance

For each inconsistent result, record:
- All known conditions at the time
- The exact outcome observed
- Anything unusual or different about that run
- Timing and sequence relative to other runs

**Goal:** Create a comparison table that might reveal patterns.

### Step 4: Look for Correlations

Analyze the documented instances:
- Do outcomes cluster by any variable?
- Is there a pattern in the sequence?
- Do certain conditions associate with certain results?
- What was different about the outliers?

**Question:** If I sort results by each variable, does any sorting reveal structure?

### Step 5: Generate Hypotheses

Based on correlations, propose specific sources of variation:
- "Results may differ because of X"
- State the mechanism by which X would cause the observed difference
- Note what this hypothesis predicts

### Step 6: Design Isolation Tests

For each hypothesis, design a test that:
- Deliberately varies the suspected factor
- Holds all other factors constant
- Produces a clear prediction (if X is the cause, then Y should happen)

### Step 7: Recommend Controls

Based on findings, specify what must be controlled for reproducibility:
- Which variables must be held constant
- What tolerance is acceptable
- How to monitor or document these variables

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
## Variable Control Analysis: [Problem]

### The Inconsistency
**Observed:** [What varies and how]
**Expected:** [What should have happened]
**Impact:** [Why this matters]

### Variable Inventory
| Category | Variable | Status | Notes |
|----------|----------|--------|-------|
| Environmental | [Variable] | [Controlled/Uncontrolled/Unknown] | [Current state] |
| Input | [Variable] | [Controlled/Uncontrolled/Unknown] | [Current state] |
| Process | [Variable] | [Controlled/Uncontrolled/Unknown] | [Current state] |
| Measurement | [Variable] | [Controlled/Uncontrolled/Unknown] | [Current state] |

### Instance Comparison
| Run | Result | [Variable 1] | [Variable 2] | [Variable N] | Notes |
|-----|--------|--------------|--------------|--------------|-------|
| 1 | [Outcome] | [Value] | [Value] | [Value] | [Observations] |
| 2 | [Outcome] | [Value] | [Value] | [Value] | [Observations] |
| 3 | [Outcome] | [Value] | [Value] | [Value] | [Observations] |

### Correlation Analysis
**Patterns observed:**
- [Pattern 1]
- [Pattern 2]

### Hypotheses
**Primary hypothesis:** [Most likely source of variation]
- Mechanism: [How this would cause the observed variation]
- Prediction: [What we would expect if this is correct]

**Alternative hypotheses:**
- [Alternative 1] — [Reasoning]
- [Alternative 2] — [Reasoning]

### Isolation Tests
**To test primary hypothesis:**
[Specific test design that would confirm or refute]

**To rule out alternatives:**
[Tests for alternative hypotheses]

### Recommended Controls
To achieve reproducible results:
1. **[Variable 1]:** [How to control, acceptable range]
2. **[Variable 2]:** [How to control, acceptable range]
3. **[Variable 3]:** [How to control, acceptable range]

### Next Steps
1. [Immediate action]
2. [Follow-up investigation]
3. [Long-term protocol change]
```

---

## Common Hidden Variables

### In Scientific Research
- Humidity (Franklin's DNA discovery)
- Temperature fluctuations
- Sample age or degradation
- Reagent batch variation
- Operator technique differences
- Instrument drift over time

### In Software/Data Analysis
- Random seed initialization
- Race conditions or timing
- Memory state from previous runs
- Floating point precision
- Data ordering effects
- Cache states

### In Business Processes
- Who performed the task
- Time pressure or workload
- Communication channel used
- Prior interactions with customer/partner
- Day of week or time effects

### In Manufacturing
- Raw material variation
- Machine warm-up state
- Operator experience
- Shift differences
- Tool wear

---

## Constraints

- This skill is for diagnosis, not for determining what to do with results once the source is found
- Sometimes variation is truly random—but exhaust systematic causes first
- Some variables may be impossible to control; focus on what can be changed
- Complete variable inventories require domain knowledge; use categories as prompts

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

**Input:** "Our A/B test showed Feature A won on Monday, Feature B won on Tuesday, and they tied on Wednesday. All tests used the same traffic. What's going on?"

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


## Variable Control Analysis: Inconsistent A/B Test Results

### The Inconsistency
**Observed:** Different winners on different days with supposedly same test setup
**Expected:** Consistent winner across days if features have different true performance
**Impact:** Cannot make product decision; wasted test duration

### Variable Inventory
| Category | Variable | Status | Notes |
|----------|----------|--------|-------|
| Environmental | Day of week | Uncontrolled | Mon, Tue, Wed represent different user patterns |
| Environmental | Traffic volume | Unknown | Volume may differ by day |
| Input | User composition | Unknown | Different users on different days |
| Process | Test allocation | Assumed controlled | Needs verification |
| Measurement | Metric definition | Controlled | Conversion rate |

### Instance Comparison
| Day | Winner | Traffic Volume | New vs. Returning | Device Mix | Notes |
|-----|--------|---------------|-------------------|------------|-------|
| Monday | A | Unknown | Unknown | Unknown | First day of work week |
| Tuesday | B | Unknown | Unknown | Unknown | Regular weekday |
| Wednesday | Tie | Unknown | Unknown | Unknown | Mid-week |

### Correlation Analysis
**Patterns observed:**
- Different day = different winner (perfect correlation)
- Without traffic composition data, cannot assess further

**Missing data critical:** User composition likely differs by day of week

### Hypotheses
**Primary hypothesis:** User composition varies by day
- Mechanism: Monday users (returning to work, checking quickly) may behave differently than Tuesday users
- Prediction: Segmenting by user type would show consistent within-segment results

**Alternative hypotheses:**
- Statistical noise: Each day's sample is too small for reliable signal
- Time-based effects: Features interact with day-specific behaviors (e.g., A better for mobile, mobile higher Monday)
- Technical issues: Allocation mechanism has daily variation

### Isolation Tests
**To test primary hypothesis:**
Segment results by new vs. returning users and device type. If segments show consistent winners, user composition is the variable.

**To test sample size:**
Run for 7+ days and analyze aggregate. If result stabilizes, daily variation was noise.

**To test allocation:**
Verify that each day's 50/50 split was achieved. Check for any allocation bugs.

### Recommended Controls
To achieve reproducible results:
1. **Minimum duration:** Run tests for at least 7 days to average day-of-week effects
2. **Segment analysis:** Always analyze by user segments in addition to aggregate
3. **Sample size:** Ensure each day has sufficient samples before drawing conclusions
4. **Allocation verification:** Log and verify split percentages daily

### Next Steps
1. Pull traffic composition data for each day (new vs. returning, device)
2. Re-analyze results segmented by user type
3. If test continues, wait for full week of data before concluding

---

## Integration

This skill is part of the **Rosalind Franklin** expert persona. Use it when results vary unexpectedly and you need to find the source of variation. It pairs well with:
- **experimental-design-framework** for setting up controlled experiments from the start
- **data-first-analysis** for interpreting results once variables are controlled
- **precision-measurement-protocol** for establishing consistent measurement practices