---
name: decision-noise-audit
description: Evaluate a decision-making process for "noise" - the unwanted variability in judgments that should be consistent. Identify sources of noise and recommend decision hygiene practices.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3786
repository: https://github.com/sethmblack/paks-skills
keywords:
- decision-noise-audit
- writing
---

# Decision Noise Audit

Evaluate a decision-making process for "noise" - the unwanted variability in judgments that should be consistent. Identify sources of noise and recommend decision hygiene practices.

---

## When to Use

- Evaluating consistency of repeated judgments (hiring, pricing, grading, sentencing)
- Diagnosing why similar cases get different outcomes
- Designing decision processes for organizations
- Improving accuracy by reducing variability
- User asks "Is there noise in this process?" or "Audit for consistency"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| process | Yes | The decision-making process to audit |
| examples | No | Specific cases showing potential inconsistency |
| context | No | Organizational and stakes context |

---

## Kahneman's Framework

### The Noise Problem

Most organizations focus on bias - systematic error in one direction. But **noise** - random scatter in judgments - is often just as harmful and far more overlooked.

"Wherever there is judgment, there is noise - and more of it than you think."

**The Thought Experiment:**
Imagine the same professional evaluating the same case twice, without remembering the first evaluation. Would they give the same answer? For most judgments, the answer is "no" - and the gap is often startling.

### Types of Noise

1. **Level Noise (Between-Judge)**
   - Some judges are consistently lenient, others harsh
   - Some underwriters always price high, others low
   - Creates systematic differences between decision-makers

2. **Pattern Noise (Within-Judge)**
   - Different judges respond differently to specific features
   - One hiring manager loves initiative; another values caution
   - Creates unpredictable variation based on who evaluates

3. **Occasion Noise**
   - Same judge, same case, different times = different decisions
   - Affected by mood, fatigue, recent cases, random factors
   - The "noise in your head"

### Why Noise Matters

| Scenario | Average Bias | Average Noise | Outcome |
|----------|--------------|---------------|---------|
| Loan decisions | 0% | 40% variance | Unfair - identical applicants get different outcomes |
| Medical diagnoses | 0% | 30% variance | Dangerous - treatment depends on which doctor |
| Performance reviews | 0% | 55% variance | Demoralizing - evaluation depends on evaluator |

Even with zero bias, high noise means the process is essentially a lottery.

---

## The Audit Process

### Step 1: Identify the Judgment

What decision is being made? What is the intended output?

**Key Questions:**
- Is this a repeated judgment (same type of decision made many times)?
- Who makes these judgments?
- What information do they use?
- How much discretion do they have?

### Step 2: Estimate Noise Levels

**Methods:**
- **Noise audit:** Have multiple judges evaluate the same cases independently
- **Retest study:** Have same judge evaluate same case at different times
- **Historical analysis:** Look at variance in outcomes for similar cases

**Typical Findings:**
- Insurance underwriting: 55% variance between underwriters
- Criminal sentencing: 50%+ variance between judges
- Job interviews: 63% of variance is interviewer, not candidate
- Performance ratings: >55% variance between raters

### Step 3: Identify Noise Sources

**Environmental Factors:**
- Time of day, day of week
- Order effects (what came before this case)
- Physical environment (noise, temperature)
- Cognitive load

**Case Presentation Factors:**
- Irrelevant information influencing judgment
- Order of information presentation
- Framing and anchoring

**Judge Factors:**
- Mood and fatigue
- Personal preferences and values
- Idiosyncratic weighting of features

**Process Factors:**
- Ambiguous criteria
- Lack of structure
- Premature holistic judgment
- No calibration mechanisms

### Step 4: Recommend Decision Hygiene

Decision hygiene practices reduce noise without targeting specific biases:

**Structural Hygiene:**
- Use structured evaluation with defined dimensions
- Delay holistic judgment until components assessed
- Provide clear, operational definitions for scales

**Aggregation Hygiene:**
- Use multiple independent judges
- Aggregate judgments (don't let one judge dominate)
- Maintain independence - don't share initial impressions

**Process Hygiene:**
- Train on calibration cases
- Use reference points and examples
- Reduce irrelevant variation in how cases are presented

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
## Decision Noise Audit

### The Process Under Review
[Description of the judgment/decision process]

### Judgment Characteristics
- **Type:** [One-time / Repeated]
- **Judges:** [Who makes these decisions]
- **Stakes:** [Consequences of variance]
- **Current structure:** [Structured / Semi-structured / Unstructured]

### Estimated Noise Level
**Assessment:** [High / Moderate / Low / Unknown]
**Evidence:** [How this was determined or estimated]

### Noise Sources Identified

#### Level Noise (Between-Judge)
- [Source]: [Evidence and impact]
- [Source]: [Evidence and impact]

#### Pattern Noise (Within-Judge)
- [Source]: [Evidence and impact]
- [Source]: [Evidence and impact]

#### Occasion Noise
- [Source]: [Evidence and impact]
- [Source]: [Evidence and impact]

### Decision Hygiene Recommendations

#### High Priority
1. **[Recommendation]**
   - Addresses: [Which noise type]
   - Implementation: [How to do it]
   - Expected impact: [What improvement]

2. **[Recommendation]**
   [Same structure]

#### Medium Priority
[Additional recommendations]

### The Mediating Assessments Protocol (MAP)

For this process, a MAP approach would involve:
1. **Dimensions:** [What independent aspects to assess]
2. **Anchors:** [Reference points for each dimension]
3. **Sequence:** [Order of assessment, holistic judgment last]
4. **Aggregation:** [How to combine dimension scores]

### Measurement Recommendations
[How to track noise reduction]

### Kahneman's Warning
"Organizations are noise factories. But unlike bias, noise is invisible - you can't see it by looking at averages. You only see it when you look at the variance."
```

---

## Constraints

- Reducing noise may conflict with "respecting professional judgment"
- Some discretion may be intentional and valuable
- Perfect consistency is not the goal - accurate consistency is
- Structure can reduce noise but may introduce rigidity
- Noise reduction is organizational, not just individual

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

**Input:** "Our company's annual performance reviews. Different managers seem to rate very differently. Same person transferring teams might go from 'exceeds expectations' to 'meets expectations.'"

**Output:**

## Decision Noise Audit

### The Process Under Review
Annual performance reviews conducted by managers for their direct reports, using a 5-point scale (Does Not Meet, Partially Meets, Meets, Exceeds, Significantly Exceeds).

### Judgment Characteristics
- **Type:** Repeated (100s of reviews annually)
- **Judges:** ~40 managers across the organization
- **Stakes:** High - affects compensation, promotion, retention, morale
- **Current structure:** Semi-structured (general criteria, manager discretion)

### Estimated Noise Level
**Assessment:** HIGH
**Evidence:**
- Same employee receiving different ratings after team transfer
- Anecdotal reports of "harsh" vs. "generous" managers
- Similar roles in similar teams showing different rating distributions
- No calibration process between managers

Industry benchmarks suggest 55%+ of variance in performance ratings is attributable to the rater, not the ratee.

### Noise Sources Identified

#### Level Noise (Between-Judge)
- **Manager calibration differences:** Some managers rarely give "Exceeds"; others give it freely. No organizational calibration enforces consistency.
- **Team norm differences:** High-performing teams may have "grade inflation" relative to average teams.
- **Manager personality:** Conflict-averse managers avoid low ratings; critical managers avoid high ratings.

#### Pattern Noise (Within-Judge)
- **Dimension weighting:** Some managers weight output heavily; others weight collaboration. Same employee may score differently depending on manager's priorities.
- **Recency bias patterns:** How recently good/bad work occurred affects rating differently by manager.
- **Halo effect variance:** Some managers let one dimension dominate; others evaluate dimensions independently.

#### Occasion Noise
- **Recent interactions:** Rating affected by last few weeks, not full year
- **Manager's mood/stress:** Reviews done during busy periods may be cursory
- **Order effects:** Employees reviewed early vs. late in the cycle get different treatment
- **Contrast effects:** Rating affected by who was reviewed just before

### Decision Hygiene Recommendations

#### High Priority

1. **Implement Calibration Sessions**
   - Addresses: Level noise
   - Implementation: Managers in groups review 5-10 "borderline" cases together, discuss ratings, align on standards
   - Expected impact: Research shows 20-30% reduction in between-rater variance

2. **Structured Dimension Assessment**
   - Addresses: Pattern noise, halo effect
   - Implementation: Rate each dimension separately (quality, collaboration, initiative, etc.) before holistic rating; holistic rating should be derived from dimensions
   - Expected impact: Forces consideration of all factors, reduces single-factor domination

3. **Behavioral Anchors for Each Rating Level**
   - Addresses: Level noise, occasion noise
   - Implementation: For each role level, provide specific examples: "Exceeds looks like X, Y, Z"
   - Expected impact: Reduces subjective interpretation of rating labels

4. **Independent Review of Rating Distributions**
   - Addresses: Level noise
   - Implementation: HR reviews each manager's distribution; outliers require justification
   - Expected impact: Identifies systematically harsh/lenient managers

#### Medium Priority

5. **Time-spaced evidence collection**
   - Addresses: Recency bias, occasion noise
   - Implementation: Quarterly notes on performance, reviewed at annual review
   - Expected impact: Reduces reliance on recent memory

6. **Blind initial ratings**
   - Addresses: Social pressure, anchoring
   - Implementation: Managers submit preliminary ratings before calibration
   - Expected impact: Prevents social influence on initial judgment

### The Mediating Assessments Protocol (MAP)

For performance reviews, a MAP approach would involve:

1. **Dimensions:**
   - Quality of work output (1-5)
   - Collaboration and teamwork (1-5)
   - Initiative and ownership (1-5)
   - Growth and development (1-5)
   - Role-specific criteria (1-5)

2. **Anchors:**
   - Each dimension has 5 behavioral descriptions
   - "3" is clearly defined as "meets expectations for role level"
   - Examples from previous reviews for reference

3. **Sequence:**
   - Rate each dimension independently
   - No holistic judgment until all dimensions scored
   - Holistic rating = weighted average with defined weights
   - Manager can adjust by 0.5 with written justification

4. **Aggregation:**
   - Initial ratings reviewed in calibration session
   - Final ratings approved by skip-level manager
   - Distribution targets serve as guidelines, not quotas

### Measurement Recommendations

1. **Noise audit:** Have 10 managers independently rate 5 hypothetical cases; measure variance
2. **Transfer analysis:** Track rating changes for employees who change teams
3. **Distribution monitoring:** Flag managers >1 SD from organizational mean
4. **Outcome correlation:** Do ratings predict subsequent performance (promotion, attrition)?

### Kahneman's Warning
"Your employees are not being evaluated by 'the company.' They're being evaluated by one person who happens to be their manager. And that person's judgment contains as much noise as signal. Until you measure the noise, you can't reduce it. Until you reduce it, you're running a lottery and calling it a meritocracy."

---

## Integration

This skill is part of the **Daniel Kahneman** expert persona. It applies the research from *Noise: A Flaw in Human Judgment* to practical organizational decision-making.

Related skills:
- **Cognitive Bias Detection** - Bias and noise are both errors, addressed differently
- **Premortem Analysis** - Process flaws surface in premortems
- **Reference Class Forecasting** - Provides calibration benchmarks