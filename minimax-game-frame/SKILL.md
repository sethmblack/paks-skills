---
name: minimax-game-frame
description: Reframe a problem as a two-player game with competing objectives, identifying players, strategies, and equilibrium conditions using Ian Goodfellow's game-theoretic approach.
license: MIT
metadata:
  version: 1.0.4506
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- minimax-game-frame
- transformation
- writing
---

# Minimax Game Frame

Reframe a problem as a two-player game with competing objectives, identifying players, strategies, and equilibrium conditions using Ian Goodfellow's game-theoretic approach.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Frame problems in ways that encourage harmful competition
- Optimize for objectives that cause harm to people or systems
- Apply game theory to manipulate or deceive
- Ignore ethical constraints in equilibrium analysis

**If the game frame reveals harmful dynamics:** Highlight the ethical concerns and suggest alternative framings.

---

## When to Use

- User asks "Frame this as a game"
- User asks "What are the competing objectives?"
- User asks "Analyze the equilibrium"
- User asks "Design a system with opposing goals"
- When optimizing requires balancing trade-offs
- When two components/stakeholders have tension
- When designing adversarial systems (security, GANs, etc.)
- When single-objective thinking is failing

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `problem_description` | Yes | The situation or system to analyze | Must describe a scenario with potential tension |
| `stakeholders` | No | Who is involved | Default: infer from description |
| `current_approach` | No | How it is being handled now | Helps identify what is not working |
| `desired_outcome` | No | What success looks like | Helps define equilibrium |

---

## Workflow
### Phase 1: Identify the Players

Every minimax game has at least two players with opposing objectives.

**Ask:**

### Step 1: Who or what is trying to **maximize** something?



### Step 2: Who or what is trying to **minimize** that same thing (or vice versa)?



### Step 3: Are there implicit players not being recognized?



**Common player archetypes:**
- Generator vs. Discriminator (GANs)
- Attacker vs. Defender (security)
- Exploiter vs. Regulator (systems)
- Short-term vs. Long-term (decisions)
- Quality vs. Speed (trade-offs)

Document players:

| Player | Role | Objective |
|--------|------|-----------|
| Player 1 | {role} | Maximize {X} |
| Player 2 | {role} | Minimize {X} or Maximize {Y where Y opposes X} |

### Phase 2: Define the Strategy Space

What actions can each player take?

**For each player:**
- What variables do they control?
- What constraints limit their choices?
- What information do they have?

| Player | Strategies Available | Constraints |
|--------|---------------------|-------------|
| {Player 1} | {list of possible actions} | {limits on actions} |
| {Player 2} | {list of possible actions} | {limits on actions} |

### Phase 3: Analyze the Game Dynamics

**Key questions:**

### Step 1: **Is this zero-sum?** Does one player's gain equal the other's loss?


   - Zero-sum: Pure competition, minimax optimal
   - Non-zero-sum: Potential for cooperation or lose-lose

### Step 2: **What is the information structure?**


   - Complete information: Both know all strategies and payoffs
   - Incomplete information: Hidden information exists
   - Sequential: Players take turns
   - Simultaneous: Players act at the same time

### Step 3: **Is there a Nash equilibrium?**


   - A state where neither player benefits from changing strategy unilaterally
   - May be stable (converges) or unstable (oscillates)

### Step 4: **What does the equilibrium look like?**


   - In GANs: Generator produces perfect samples, discriminator outputs 0.5
   - In security: Attacker finds no exploitable weaknesses
   - In trade-offs: Optimal balance point

### Phase 4: Identify Pathologies

What can go wrong?

| Pathology | Description | Signs | Mitigation |
|-----------|-------------|-------|------------|
| **Oscillation** | Players alternate dominance, never converge | Cycling metrics, unstable outputs | Reduce learning rates, add regularization |
| **Collapse** | One player dominates completely | One objective maximized, other abandoned | Rebalance objectives, add constraints |
| **Arms race** | Escalating competition without bound | Ever-increasing costs/complexity | Add caps, change objective |
| **Local equilibrium** | Stuck in suboptimal stable state | Stable but poor outcomes | Restart, exploration, perturbation |

### Phase 5: Design Recommendations

Based on the analysis:

### Step 1: **If no equilibrium exists:** Redesign objectives or add constraints



### Step 2: **If equilibrium is harmful:** Add ethical constraints to strategy spaces



### Step 3: **If oscillating:** Dampen dynamics (slower updates, regularization)



### Step 4: **If collapsed:** Rebalance (change loss weights, add diversity pressure)



---

## Outputs

### Minimax Game Analysis

```markdown
## Minimax Game Analysis: {Problem Name}

---

### Game Formulation

**Game Type:** {zero-sum/non-zero-sum} | {complete/incomplete information} | {sequential/simultaneous}

| Player | Role | Objective | Strategy Space |
|--------|------|-----------|----------------|
| {P1} | {role} | {maximize/minimize X} | {available actions} |
| {P2} | {role} | {maximize/minimize Y} | {available actions} |

---

### Dynamics Analysis

**Current State:** {Where the system is now}
**Equilibrium:** {What the stable state looks like, if one exists}
**Convergence:** {Will it reach equilibrium? How?}

---

### Pathology Check

| Pathology | Risk | Evidence | Mitigation |
|-----------|------|----------|------------|
| Oscillation | {H/M/L} | {signs} | {fix} |
| Collapse | {H/M/L} | {signs} | {fix} |
| Arms race | {H/M/L} | {signs} | {fix} |

---

### Design Recommendations

1. **{Recommendation 1}**
   - Rationale: {why this helps}
   - Implementation: {how to do it}

2. **{Recommendation 2}**
   ...

---

### Key Insight

{One-sentence summary of the game-theoretic perspective on this problem}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear competing objectives | Suggest this may not be a minimax problem; offer alternative framings |
| More than two players | Extend to multi-player game; note increased complexity |
| Objectives are aligned | This is not adversarial; suggest collaborative optimization instead |
| Unclear problem description | Ask for clarification on what is being optimized |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
problem_description: Our alerting system generates too many alerts, but reducing them misses real incidents
current_approach: Manual threshold tuning that swings between too noisy and too quiet
desired_outcome: Optimal alert volume that catches real issues without fatigue
```

**Output:**

## Minimax Game Analysis: Alert Volume Optimization

### Game Formulation

**Game Type:** Non-zero-sum | Complete information | Simultaneous

| Player | Role | Objective | Strategy Space |
|--------|------|-----------|----------------|
| Sensitivity | Detection | Maximize true positives | Threshold setting, feature weights |
| Specificity | Filtering | Minimize false positives | Threshold setting, suppression rules |

### Dynamics Analysis

**Current State:** Oscillating between high-sensitivity (noisy) and high-specificity (misses incidents)
**Equilibrium:** ROC curve optimal point balancing precision and recall
**Convergence:** Manual tuning is too coarse; oscillates around equilibrium

### Pathology Check

| Pathology | Risk | Evidence | Mitigation |
|-----------|------|----------|------------|
| Oscillation | HIGH | Swinging thresholds | Automated tuning with smaller steps |
| Collapse | LOW | Neither extreme is stable | N/A |

### Key Insight

The alerting problem is a minimax game between catching incidents (sensitivity) and reducing noise (specificity). The equilibrium is the ROC curve optimal point, but manual tuning causes oscillation. Use adaptive thresholds that converge gradually rather than discrete manual adjustments.

---

## Integration

This skill is part of the **ian-goodfellow** expert's methodology. When invoked:

1. Think like Goodfellow: "What adversarial tension exists here?"
2. Look for the generator-discriminator pattern in non-ML problems
3. Ground equilibrium analysis in game theory
4. Acknowledge when problems are NOT minimax and suggest alternatives

**Related skills:**
- `adversarial-robustness-audit` - For security-specific game analysis
- `gan-training-diagnosis` - For GAN-specific minimax problems