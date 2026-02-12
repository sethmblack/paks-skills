---
name: negative-expertise-audit
description: Systematically identify and document what NOT to do in a domain, building the "censor agents" that prevent known failures.
version: 1.0.0
author: sethmblack
tags: [negative-expertise-audit, structure, writing]
---

# Negative Expertise Audit

Systematically identify and document what NOT to do in a domain, building the "censor agents" that prevent known failures.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Document negative expertise for harmful domains (hacking, exploitation, deception)
- Create guides for avoiding detection of malicious activity
- Build anti-pattern catalogs that could enable harm

**If asked to audit negative expertise for harmful purposes:** Refuse explicitly. This skill is for preventing accidents, not evading consequences.

---

## When to Use

- User asks "What should I avoid here?"
- User asks "Build a negative expertise catalog"
- After a post-mortem (capturing what went wrong)
- When designing guardrails or safety constraints
- User asks "What are the anti-patterns?"
- Before a risky operation (pre-mortem)
- When onboarding someone to avoid known pitfalls

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **domain** | Yes | Area to audit (e.g., deployment, monitoring, incident response) |
| **positive_knowledge** | No | Existing runbooks, procedures, best practices |
| **historical_incidents** | No | Past failures, post-mortems, near-misses |
| **scope** | No | How comprehensive (quick audit vs. exhaustive) |

---

## Workflow
### Step 1: 1. Inventory Positive Knowledge

First, understand what the domain's "do this" rules are:
- Existing runbooks and procedures
- Best practices and standards
- Known good patterns

This establishes the baseline against which negative knowledge is defined.

### Step 2: 2. Extract Negative Knowledge

For each piece of positive knowledge, identify the corresponding negative:

| Positive Rule | Corresponding Negative |
|---------------|------------------------|
| "Do X before Y" | "Never do Y without first doing X" |
| "Use pattern A" | "Avoid anti-patterns B, C, D" |
| "Check for Z" | "Never assume Z is true" |

### Step 3: 3. Mine Historical Incidents

From post-mortems and failures:
- What action caused or contributed to the failure?
- Was there a point where intervention could have prevented it?
- What should have been avoided?

**Template for each incident:**
```
Incident: {name}
What went wrong: {description}
Negative lesson: "Never {action that caused harm}"
Censor timing: {early detection} or {last-resort suppression}
```

### Step 4: 4. Classify Censors and Suppressors

Organize negative expertise by when it should activate:

| Type | Function | Example |
|------|----------|---------|
| **Censor** | Stops activity BEFORE it becomes dangerous | "Never start a deployment without checking dependencies" |
| **Suppressor** | Stops action just BEFORE execution | "Never execute DELETE without confirmation" |
| **Early Warning** | Flags risky patterns for review | "Flag any change affecting >10 services" |

### Step 5: 5. Document the Anti-Pattern Catalog

Structure findings for easy reference and integration into tooling.

### Step 6: 6. Recommend Implementation

How can these vetoes be built into systems?
- Automated checks in CI/CD
- Pre-commit hooks
- Runtime guardrails
- Human approval gates
- Monitoring alerts for anti-patterns

---

## Outputs

Format output as:

```markdown
## Negative Expertise Audit: {Domain}

### Scope
{What was audited, how comprehensive}

### Positive-Negative Mapping

| Do This | Never Do This |
|---------|---------------|
| {positive rule} | {corresponding negative} |
| ... | ... |

### Historical Lessons

| Incident | Root Cause | Never Again |
|----------|------------|-------------|
| {name} | {what went wrong} | {anti-pattern to avoid} |
| ... | ... | ... |

### Censor Agents (Early Detection)

| Censor | Trigger | Why Critical |
|--------|---------|--------------|
| {name} | {what it watches for} | {consequence avoided} |
| ... | ... | ... |

### Suppressor Agents (Last-Resort Vetoes)

| Suppressor | Blocks | Escape Hatch |
|------------|--------|--------------|
| {name} | {what action is blocked} | {how to override if truly needed} |
| ... | ... | ... |

### Implementation Recommendations

1. **Automated:** {what can be automated as checks}
2. **Approval Gates:** {what requires human sign-off}
3. **Monitoring:** {what to alert on}
4. **Documentation:** {what to add to runbooks}

### Gaps Identified

{Anti-patterns that lack corresponding censors/suppressors}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No positive knowledge provided | Build audit from historical incidents and common patterns |
| No historical incidents | Use domain-standard anti-patterns; note as theoretical |
| Too many anti-patterns | Prioritize by severity of consequence |
| Conflicting anti-patterns | Note the conflict; different contexts may have different rules |
| Anti-pattern requires complex detection | Flag as needing human judgment; cannot be fully automated |

---

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
- domain: Deployment
- historical_incidents: "Friday evening deploy caused outage", "Rollback failed because no previous version tagged", "Config change broke 5 services"

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


## Negative Expertise Audit: Deployment

### Scope
Deployment practices, focusing on three historical incidents and standard anti-patterns.

### Positive-Negative Mapping

| Do This | Never Do This |
|---------|---------------|
| Deploy during business hours | Never deploy Friday afternoon or before holidays |
| Test in staging first | Never go directly to production |
| Tag releases before deploy | Never deploy without a tagged rollback target |
| Announce deployments | Never deploy silently to shared infrastructure |
| Check downstream dependencies | Never deploy upstream changes without notifying downstream |

### Historical Lessons

| Incident | Root Cause | Never Again |
|----------|------------|-------------|
| Friday Outage | Deployed complex change with no on-call coverage | Never deploy without adequate support window |
| Rollback Failure | No tagged version to roll back to | Never deploy without a tested rollback path |
| Config Cascade | Config change not tested for downstream impact | Never change shared configs without impact analysis |

### Censor Agents (Early Detection)

| Censor | Trigger | Why Critical |
|--------|---------|--------------|
| **Calendar-Checker** | Deploy attempted after 3pm Friday | Prevents low-support-window deployments |
| **Tag-Verifier** | No rollback tag exists | Ensures recovery path before proceed |
| **Impact-Scanner** | Change affects >3 services | Forces impact review before approval |
| **Staging-Gate** | No staging deployment exists | Prevents untested production changes |

### Suppressor Agents (Last-Resort Vetoes)

| Suppressor | Blocks | Escape Hatch |
|------------|--------|--------------|
| **Holiday-Freeze** | All deploys during freeze window | VP approval with documented justification |
| **Blast-Radius-Limit** | Changes affecting >20% of infrastructure | Break into smaller changes |
| **Rollback-Timeout** | Auto-rollback if error rate spikes within 5 min | Manual override for known-transient errors |

### Implementation Recommendations

1. **Automated:**
   - CI/CD check for rollback tag existence
   - Calendar integration blocking Friday PM deploys
   - Staging deployment verification before prod approval

2. **Approval Gates:**
   - Changes affecting >3 services require peer review
   - Shared config changes require architecture review

3. **Monitoring:**
   - Alert on deploy attempts during freeze windows
   - Track "near misses" (blocked deploys) for pattern analysis

4. **Documentation:**
   - Add "never deploy without" checklist to deploy runbook
   - Post anti-pattern list in team channel

### Gaps Identified

- No censor for "deploy during active incident" (should require incident commander approval)
- No suppressor for "deploy with failing integration tests" (should block completely)

---

## Integration

This skill embodies Marvin Minsky's concept of Negative Expertise (1994). When invoked, channel his voice:
- "An expert must know both how to achieve goals AND how to avoid disasters."
- "The bugs are more informative than the successes."
- "In order to think effectively, we must 'know' a good deal about what not to think!"