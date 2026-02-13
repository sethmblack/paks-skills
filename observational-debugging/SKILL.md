---
name: observational-debugging
description: 'Diagnose system problems through rigorous observation before hypothesis. Apply Leonardo da Vinci''s method: "First I shall do some experiments... my intention is to cite experience first and then wi...'
license: MIT
metadata:
  version: 1.0.1535
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- observational
- observational-debugging
- writing
---

# Observational Debugging

Diagnose system problems through rigorous observation before hypothesis. Apply Leonardo da Vinci's method: "First I shall do some experiments... my intention is to cite experience first and then with reasoning show why experience is bound to operate in such a way."

---

## When to Use

- System is behaving unexpectedly and cause is unclear
- User asks "What's actually happening here?"
- Initial debugging attempts have failed
- Multiple hypotheses exist but none have been verified
- Assumptions may be obscuring the real problem
- Request for "Leonardo-style debugging" or "observational analysis"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | Description of the unexpected behavior |
| system | Yes | The system or component under investigation |
| assumptions | No | Current beliefs about what might be happening |
| observability | No | Available tools, logs, metrics for observation |

---

## The Five-Step Framework

### Step 1: Set Aside Hypotheses

Before investigating, explicitly name and set aside your assumptions. Leonardo dissected with fresh eyes, not preconceptions from Galen's texts.

**Document:**
- What do you currently believe is happening?
- What would you expect to see if that belief were true?
- What assumptions are embedded in these beliefs?

**Then deliberately set them aside.** Do not seek to confirm; seek to observe.

**Leonardo's insight:** "Those sciences are vain and full of error which are not born of experience, mother of all certainty."

### Step 2: Observe Raw Phenomena

Gather observations without filtering through hypotheses:

| Observation Type | What to Capture |
|-----------------|-----------------|
| **Logs** | Raw entries, not pre-filtered searches |
| **Metrics** | Actual values, not just anomalies |
| **State** | Current configuration, actual vs. expected |
| **Timeline** | When did behavior change? What else changed then? |
| **Scope** | What is affected? What is NOT affected? |
| **Reproduction** | Under what conditions does it occur? |

**Key discipline:** Capture what IS happening, not what you think is relevant. Leonardo drew what he saw in corpses, not what anatomy texts told him should be there.

### Step 3: Compare Observations to Assumptions

Now bring back your assumptions and compare:

```
Assumption: [What you believed]
Expected observation: [What you would see if true]
Actual observation: [What you actually saw]
Discrepancy: [How they differ]
```

**Questions to ask:**
- Where do observations contradict assumptions?
- Where are assumptions simply unverified (neither confirmed nor contradicted)?
- What observations were surprising or unexplained?
- What observations were you NOT looking for but noticed anyway?

**Leonardo's insight:** "The painter who has no doubts will achieve little. When the work surpasses the judgment of the worker, that worker achieves little."

### Step 4: Generate Hypotheses from Discrepancies

Now, and only now, form hypotheses based on what you observed:

For each discrepancy or surprising observation:
1. What would explain this observation?
2. What else would have to be true if this explanation is correct?
3. How could you verify or falsify this?

**Prioritize hypotheses by:**
- Explanatory power (how much does it explain?)
- Testability (can you verify it quickly?)
- Likelihood (given what else you know)

### Step 5: Design Verification Experiments

For each hypothesis, design a minimal experiment:

```
Hypothesis: [What you believe might be true]
Test: [What you will do or observe]
Expected result if true: [What should happen]
Expected result if false: [What should happen instead]
```

Execute experiments in order of priority. Each experiment either confirms, refutes, or refines the hypothesis.

**Iterate:** New observations may require returning to Step 2.

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
## Observational Debugging Report

### Problem Statement
[Clear description of unexpected behavior]

### System Under Investigation
[Component/service/system being analyzed]

### Initial Assumptions (Set Aside)
| Assumption | Expected if True |
|------------|------------------|
| [Belief 1] | [What we'd see] |

### Raw Observations
| Observation | Source | Timestamp |
|-------------|--------|-----------|
| [What was seen] | [Log/metric/state] | [When] |

### Discrepancy Analysis
| Assumption | Expected | Actual | Discrepancy |
|------------|----------|--------|-------------|
| [Belief] | [Expected] | [Observed] | [Difference] |

### Hypotheses Generated
| Hypothesis | Explains | Testable Via | Priority |
|------------|----------|--------------|----------|
| [Theory] | [Observations] | [Method] | High/Med/Low |

### Verification Plan
1. **Experiment:** [Test]
   - **Hypothesis tested:** [Which one]
   - **If true:** [Expected result]
   - **If false:** [Expected result]

### Findings
[Results of verification, root cause if found]

### Remaining Unknowns
[What is still unclear; next steps]
```

---

## Constraints

- Do not skip observation to jump to hypothesis
- Do not filter observations through your expectations
- Do not declare "root cause found" until verified
- Acknowledge when the system is too opaque to observe properly
- Document what you cannot observe, not just what you can
- Iterate; debugging is rarely linear

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

**Input:**
```
problem: API response times have increased 3x in the last hour
system: User authentication service
assumptions: Probably database slowdown or increased load
observability: APM traces, database metrics, CloudWatch logs
```

**Output:**

## Observational Debugging Report

### Problem Statement
API response times for the authentication service have increased from ~100ms to ~300ms average over the last hour. No deployments during this period.

### System Under Investigation
User authentication service (auth-svc), including downstream dependencies: PostgreSQL, Redis cache, identity provider

### Initial Assumptions (Set Aside)
| Assumption | Expected if True |
|------------|------------------|
| Database slowdown | High DB query times in traces |
| Increased load | Higher request rate |
| Cache misses | Higher Redis miss rate |

### Raw Observations
| Observation | Source | Timestamp |
|-------------|--------|-----------|
| Request rate: stable at 500 rps | CloudWatch | Last 2 hours |
| DB query p99: 15ms (unchanged) | APM | Last 2 hours |
| Redis hit rate: 94% (unchanged) | Redis metrics | Last 2 hours |
| auth-svc CPU: 45% (up from 30%) | CloudWatch | Last hour |
| External IdP call p99: 180ms (was 50ms) | APM traces | Last hour |
| IdP timeout errors: 12 (was 0) | Application logs | Last hour |
| New IdP certificate deployed upstream | IdP status page | 47 minutes ago |

### Discrepancy Analysis
| Assumption | Expected | Actual | Discrepancy |
|------------|----------|--------|-------------|
| Database slowdown | High DB latency | DB latency unchanged | Not supported |
| Increased load | Higher request rate | Request rate stable | Not supported |
| Cache misses | Higher miss rate | Miss rate unchanged | Not supported |
| (No assumption) | - | IdP latency 3.5x higher | Unexpected |

### Hypotheses Generated
| Hypothesis | Explains | Testable Via | Priority |
|------------|----------|--------------|----------|
| IdP certificate change causing TLS renegotiation overhead | IdP latency spike, timing correlation | Compare TLS handshake times before/after | High |
| IdP capacity issue after cert rotation | Latency spike, timeout errors | Check IdP status, contact IdP | High |
| Our TLS cache invalidated by new cert | CPU increase, latency increase | Check TLS session reuse rate | Medium |

### Verification Plan
1. **Experiment:** Check TLS handshake times in APM traces
   - **Hypothesis tested:** TLS renegotiation overhead
   - **If true:** Handshake times increased from ~5ms to ~50ms+
   - **If false:** Handshake times unchanged

2. **Experiment:** Contact IdP support or check status page
   - **Hypothesis tested:** IdP capacity issue
   - **If true:** Known issue or degradation reported
   - **If false:** IdP reports nominal

### Findings
TLS handshake times increased from 5ms to 85ms after the certificate rotation. The new certificate chain has one additional intermediate certificate, and our TLS session cache was invalidated by the new cert, causing full handshakes for every request. Session reuse rate dropped from 92% to 0% at the time of the cert change.

**Root cause:** IdP certificate rotation invalidated our TLS session cache, forcing expensive full handshakes on every request.

**Resolution:** Restart service to warm TLS cache; consider implementing TLS session resumption with tickets.

### Remaining Unknowns
Why did the extra intermediate certificate add 80ms? May indicate suboptimal certificate chain ordering. Worth investigating with IdP.

---

## Integration

This skill is part of the **Leonardo da Vinci** expert persona. Use it when debugging requires disciplined observation rather than hypothesis-driven investigation.

Leonardo approached anatomy by observing what was actually there, not what authorities said should be there. He discovered the heart has four chambers because he looked, while others trusted Galen's texts. This skill applies that same rigor to system debugging.