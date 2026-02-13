---
name: monetary-diagnosis
description: Trace macroeconomic phenomena (inflation, recessions, financial crises) back to monetary policy causes using the Friedman-Schwartz analytical framework.
license: MIT
metadata:
  version: 1.0.4522
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- monetary-diagnosis
- writing
---

# Monetary Diagnosis

Trace macroeconomic phenomena (inflation, recessions, financial crises) back to monetary policy causes using the Friedman-Schwartz analytical framework.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Claim certainty about complex macroeconomic causation without acknowledging uncertainty
- Ignore non-monetary factors entirely when they are clearly relevant
- Fabricate historical data or statistics
- Present monetarist interpretation as the only valid framework

**Intellectual honesty:** Monetary policy is often a major factor, but rarely the only factor. Acknowledge complexity while applying the monetary lens.

---

## When to Use

- User asks "What caused this inflation?"
- User asks "Why did this recession happen?"
- User asks "Diagnose the monetary causes of..."
- User asks "Was this a policy failure or market failure?"
- Analyzing any significant macroeconomic event (inflation surge, recession, financial crisis)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **event** | Yes | The macroeconomic event to analyze |
| **timeframe** | Yes | When the event occurred |
| **jurisdiction** | No | Country or region (default: United States) |
| **data** | No | Relevant monetary data if available |

---

## Workflow
### Step 1: 1. Identify the Phenomenon
Characterize what happened:
- Inflation? By how much? Over what period?
- Recession? How deep? How long?
- Financial crisis? What triggered the panic?

### Step 2: 2. Examine Monetary Policy Actions
Before and during the event, what did the central bank do?
- Money supply changes (M1, M2 growth rates)
- Interest rate decisions
- Open market operations
- Reserve requirements
- Liquidity provision or withdrawal

### Step 3: 3. Apply the Friedman Test
Ask the core Friedman questions:
- Did money supply growth significantly exceed output growth? (Inflation)
- Did the central bank allow or cause monetary contraction? (Recession)
- Was there a failure to act as lender of last resort? (Financial crisis)

### Step 4: 4. Trace the Transmission Mechanism
How did monetary policy affect the real economy?
- Interest rates to investment and consumption
- Credit availability to business activity
- Expectations and confidence effects
- Exchange rate effects (for open economies)

### Step 5: 5. Consider Expectations
Apply Friedman's expectations-augmented analysis:
- Were expectations anchored or unanchored?
- Did policy create inflation expectations that became self-fulfilling?
- Was there a lag between policy and effect?

### Step 6: 6. Assess Alternative Explanations
Acknowledge other contributing factors:
- Real shocks (oil prices, technology, war)
- Fiscal policy
- Regulatory failures
- International factors

---

## Output Format

```markdown
## Monetary Diagnosis: {Event Name}

### The Phenomenon
{What happened: inflation rate, recession depth, crisis severity}

### Monetary Policy Timeline
| Date | Action | Money Supply Effect |
|------|--------|---------------------|
| {Date} | {Policy action} | {Expansionary/Contractionary} |

### The Friedman Diagnosis
{Core monetary explanation. Apply "inflation is always and everywhere a monetary phenomenon" or "central bank failure" framework as appropriate.}

### Transmission Mechanism
{How monetary policy affected the real economy}

### Expectations Dynamics
{Role of inflation expectations, adaptive adjustment, policy credibility}

### Contributing Factors
{Non-monetary factors that also mattered}

### Counterfactual
{What different monetary policy could have achieved}

### Friedman Principle
*"{Relevant Friedman quote, e.g., 'The Great Depression was produced by government mismanagement...'}"*
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

## Example

**Input:**
```
event: The Great Inflation
timeframe: 1965-1982
jurisdiction: United States
```

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


## Monetary Diagnosis: The Great Inflation (1965-1982)

### The Phenomenon
Inflation rose from 1.6% in 1965 to 14.8% by 1980. CPI roughly tripled over 15 years. Inflation became embedded in expectations, contracts, and wage negotiations.

### Monetary Policy Timeline
| Date | Action | Money Supply Effect |
|------|--------|---------------------|
| 1965-68 | Fed accommodated Vietnam War + Great Society spending | M2 growth accelerated to 8-9% |
| 1971 | Nixon wage-price controls; dollar delinked from gold | Monetary expansion continued |
| 1972-73 | Burns Fed expanded money supply ahead of election | M2 growth reached 13% |
| 1979-82 | Volcker tightened dramatically | M2 growth slowed to 6% |

### The Friedman Diagnosis
The Great Inflation was caused by excessive money supply growth. From 1965-1979, the Federal Reserve consistently expanded the money supply faster than real output growth. This was classic monetarist causation: too much money chasing too few goods.

Key policy failures:
1. **Accommodation of fiscal deficits** - The Fed monetized Vietnam War and Great Society spending
2. **Political pressure** - Fed Chairman Arthur Burns faced pressure to support Nixon's reelection
3. **Misdiagnosis** - Policymakers blamed "cost-push" factors (oil, unions) rather than monetary excess
4. **Phillips curve thinking** - Belief that inflation was the price of low unemployment

### Transmission Mechanism
- Rapid money growth lowered real interest rates
- Negative real rates encouraged borrowing and speculation
- Easy money bid up asset and commodity prices
- Wage-price spirals developed as expectations adjusted

### Expectations Dynamics
By the mid-1970s, inflation expectations became unanchored. Workers demanded higher wages expecting future inflation; firms raised prices anticipating wage increases. The short-run Phillips curve had shifted up repeatedly. Friedman's prediction (AEA address, 1967) was vindicated: there was no permanent tradeoff.

### Contributing Factors
- Oil shocks (1973, 1979) worsened inflation but did not cause it
- Fiscal deficits created pressure on the Fed to monetize
- Bretton Woods collapse removed gold anchor
- Unionization facilitated wage-price spirals

### Counterfactual
Volcker proved the cure worked. By reducing money supply growth despite short-term recession, he broke the inflation. This demonstrated that inflation was indeed monetary and could be ended by monetary policy.

### Friedman Principle
*"Inflation is always and everywhere a monetary phenomenon in the sense that it is and can be produced only by a more rapid increase in the quantity of money than in output."*

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient monetary data | Note data limitations; use available proxies |
| Strong non-monetary explanation | Acknowledge it; explain why monetary factors still matter |
| Disagreement among economists | Present monetarist view; note alternative interpretations |
| Recent event with uncertain data | Provide preliminary analysis; flag uncertainty |

---

## Integration

This skill integrates with the **Milton Friedman** expert. When analyzing macroeconomic events, the expert should apply this framework to diagnose monetary causes, maintaining Friedman's empirical approach and his core insight that monetary policy is the primary driver of inflation and a major factor in economic fluctuations.

---

## Success Criteria

Analysis is complete when:
- [ ] Phenomenon clearly characterized with data
- [ ] Monetary policy actions documented
- [ ] Friedman diagnostic framework applied
- [ ] Transmission mechanism explained
- [ ] Expectations dynamics considered
- [ ] Alternative factors acknowledged
- [ ] Output follows specified format