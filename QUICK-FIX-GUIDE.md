# Quick Fix Guide for Skill Quality

This guide shows how to fix the most common issues found in the 1,445 skills analyzed.

---

## The Three Critical Fixes

These three fixes alone will raise most skills from "Needs Work" to "Acceptable" or "Good":

1. **Add "Outputs" section** (missing in 69.2% of skills)
2. **Add numbered workflow steps** (missing in 69.5% of skills)
3. **Add "Constraints" section** (missing in 55.0% of skills)

---

## Fix #1: Add Missing "Outputs" Section

### The Problem
Many skills have an "Output Format" section but the analysis looks for "Outputs". Also, many output sections are too vague.

### The Solution

**If you have "Output Format" - rename and enhance:**

```markdown
## Output Format

```markdown
[template]
```
```

**Change to:**

```markdown
## Outputs

**Primary Output:** [Clear statement of what this skill produces]

**Format:**
```markdown
[template with clear structure]
```

**Example output:**
[Brief example showing the format in use]
```

### Example Fix

**Before:**
```markdown
## Output Format

The skill produces analysis in markdown.
```

**After:**
```markdown
## Outputs

**Primary Output:** A structured analysis document identifying key patterns,
insights, and recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]

### Patterns Identified
- [Pattern 1]: [Description]
- [Pattern 2]: [Description]

### Recommendations
1. [Action 1]
2. [Action 2]
```

**Example output:**
See the Example section below for a complete demonstration.
```

---

## Fix #2: Add Numbered Workflow Steps

### The Problem
Many skills describe the process in paragraphs or vague sections. The analysis looks for "Step 1", "Step 2", etc.

### The Solution

**Convert narrative to numbered steps:**

**Before:**
```markdown
## The Framework

First, you need to understand the context. Look at what's happening and
analyze the situation. Then you should identify the key factors. After
that, you develop recommendations based on what you found.
```

**After:**
```markdown
## Workflow

### Step 1: Analyze the Context

Review the situation and gather relevant information:
- What is the current state?
- What are the constraints?
- What is the desired outcome?

### Step 2: Identify Key Factors

Look for the most important elements:
- What variables have the most impact?
- What patterns emerge?
- What is causing the current situation?

### Step 3: Develop Recommendations

Based on the analysis, create actionable recommendations:
- What specific actions should be taken?
- What is the priority order?
- What are the expected outcomes?
```

### Quick Template

```markdown
## Workflow

### Step 1: [Action Verb] [What]
[Specific instructions on how to do this step]

**Questions to ask:**
- [Question 1]
- [Question 2]

### Step 2: [Action Verb] [What]
[Specific instructions]

**Look for:**
- [Thing 1]
- [Thing 2]

### Step 3: [Action Verb] [What]
[Specific instructions]

**Output at this step:**
[What you should have]
```

### Good Action Verbs for Steps
- Analyze, Identify, Evaluate, Assess, Review
- Extract, Gather, Collect, Compile, Organize
- Generate, Create, Develop, Formulate, Design
- Compare, Contrast, Measure, Quantify, Calculate
- Recommend, Propose, Suggest, Prioritize, Decide

---

## Fix #3: Add Missing "Constraints" Section

### The Problem
55% of skills don't have explicit constraints. This section is critical for defining boundaries and preventing misuse.

### The Solution

Add a Constraints section with clear "Do not" statements and boundary definitions.

**Template:**
```markdown
## Constraints

- Do not [misuse case 1]
- Do not [misuse case 2]
- Do not [misuse case 3]
- Acknowledge [limitation 1]
- Honor [limitation 2]
- [Boundary condition]
```

### Examples by Skill Type

**For analytical skills:**
```markdown
## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
```

**For creative skills:**
```markdown
## Constraints

- Do not sacrifice meaning for style
- Do not lose the core message in pursuit of cleverness
- Acknowledge when simplification distorts important nuance
- Honor the audience's intelligence—avoid condescension
- Stay true to the source material's intent
```

**For technical skills:**
```markdown
## Constraints

- Do not recommend approaches beyond the stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Test recommendations before implementation where possible
```

**For communication skills:**
```markdown
## Constraints

- Do not manipulate or deceive the audience
- Do not oversimplify to the point of misrepresentation
- Acknowledge cultural and contextual sensitivities
- Honor different communication preferences and styles
- Maintain authenticity while adapting delivery
```

---

## Fix #4: Expand Brief Examples

### The Problem
36% of skills have examples that are too short or lack input/output structure.

### The Solution

**Minimum example structure:**
```markdown
## Example

**Input:**
- [parameter 1]: [value]
- [parameter 2]: [value]
- [parameter 3]: [value]

**Output:**

[Full demonstration of the skill in action - at least 200 words]

[Show the technique working]

[Include commentary if helpful]

**Why this works:**
[Brief explanation of what makes this effective]
```

### Example Fix

**Before:**
```markdown
## Example

Input: "Analyze this marketing campaign"
Output: Campaign analysis with strengths and weaknesses.
```

**After:**
```markdown
## Example

**Input:**
- campaign: New product launch using influencer partnerships
- target_audience: Millennials interested in sustainable products
- budget: $50,000
- duration: 3 months

**Output:**

## Campaign Analysis: Sustainable Product Launch

### Strengths

**Audience-Channel Alignment:** Using influencer partnerships to reach
millennials shows strong channel selection. This demographic trusts peer
recommendations over traditional advertising.

**Authentic Messaging Potential:** Sustainability focus aligns with influencer
credibility if partners are genuine advocates (not just paid promoters).

**Budget Appropriateness:** $50K for 3 months with influencer focus is realistic
for micro/mid-tier influencers, allowing for multiple partnerships.

### Weaknesses

**Measurement Ambiguity:** Campaign lacks clear KPIs. How will success be
measured? Sales? Awareness? Engagement?

**Influencer Vetting Risk:** Not all sustainability influencers have authentic
credentials. Partner selection is critical to avoid greenwashing accusations.

**Limited Channel Diversity:** Relying solely on influencers creates platform
dependency and makes the campaign vulnerable to algorithm changes.

### Recommendations

1. Define 3-5 specific KPIs before launch (e.g., 100K impressions, 5% engagement
   rate, 500 qualified leads)
2. Vet influencers for authentic sustainability practices, not just follower count
3. Allocate 20% of budget to owned content as insurance against platform changes
4. Build in A/B testing to optimize messaging in first 30 days

**Why this works:**

This example shows the complete analytical process: it doesn't just list
strengths and weaknesses, it explains WHY they matter and provides SPECIFIC,
ACTIONABLE recommendations with clear metrics.
```

---

## Fix #5: Improve Section Ordering

### The Problem
35% of skills have poor section flow. The ideal order is logical progression from "what" to "how" to "examples" to "boundaries".

### The Ideal Order

```markdown
# Skill Name
[Opening description]

## When to Use
[Trigger conditions]

## Inputs
[What you need]

## The Framework / Workflow
[How to do it - steps]

## Outputs
[What you get]

## Constraints
[Boundaries and limitations]

## Example
[Demonstration]

## Integration
[How this connects to the expert]
```

### Quick Reordering

If your sections are out of order, just cut and paste to match this sequence. Most markdown editors make this easy.

**Watch for these common mistakes:**
- Example before Workflow (reader doesn't understand what they're seeing)
- Constraints at the very end after Example (feels like an afterthought)
- Outputs before Workflow (tells what you get before how to get it)

---

## Fix #6: Add Missing "When to Use" Bullets

### The Problem
Some skills have "When to Use" but with too few trigger conditions (need 3-5).

### The Solution

Add specific, concrete trigger conditions:

**Template:**
```markdown
## When to Use

- [Situation 1 where this skill applies]
- [Situation 2 where this skill applies]
- [Situation 3 where this skill applies]
- [User request pattern: "specific phrase"]
- [Problem type this solves]
```

**Example:**
```markdown
## When to Use

- Project timeline is slipping and you need to identify critical path
- Multiple stakeholders disagree on priorities
- Resources are constrained and you must choose what to cut
- User asks "What should we focus on first?"
- Decision paralysis due to too many competing options
```

---

## Fix #7: Add Input Table Structure

### The Problem
Some skills list inputs in paragraphs instead of a structured table.

### The Solution

**Always use this table format:**

```markdown
## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_name | Yes | Clear description of what this is and how it's used |
| optional_input | No | Description with default value if applicable |
| context | No | Additional context (default: none) |
```

**Good descriptions:**
- "The text to analyze for tone and sentiment"
- "Target audience demographic (age, interests, location)"
- "Desired outcome or goal for the communication"
- "Budget constraint in USD (default: no limit)"

**Bad descriptions:**
- "The input"
- "Text"
- "Details"

---

## Batch Fix Strategy

If you're fixing multiple skills:

### 1. Group by Issue Type

Run this to find all skills missing a specific section:

```bash
cd paks-ready
grep -L "## Constraints" */SKILL.md | wc -l
```

### 2. Create Templates

Save these templates:
- `template-outputs.md`
- `template-constraints.md`
- `template-workflow.md`

### 3. Use Find & Replace

For consistent issues (like "Output Format" → "Outputs"), use editor find/replace across files.

### 4. Validate

After fixes, re-run the analysis:
```bash
python3 scripts/analyze-skill-quality.py
```

---

## Quality Checklist

After making fixes, verify each skill has:

- [ ] Clear name (3+ words, hyphenated)
- [ ] Description 100+ characters
- [ ] "When to Use" with 3+ bullets
- [ ] "Inputs" table (properly formatted)
- [ ] "Workflow" or "Framework" with 3+ numbered steps
- [ ] "Outputs" section with format and example
- [ ] "Constraints" section with 3+ items
- [ ] "Example" with input/output (200+ words)
- [ ] Proper section ordering
- [ ] No spelling/grammar errors

---

## Time Estimates

| Fix Type | Estimated Time | Priority |
|----------|---------------|----------|
| Add "Outputs" section | 5 minutes | High |
| Add numbered steps to workflow | 10 minutes | High |
| Add "Constraints" section | 5 minutes | High |
| Expand brief example | 15 minutes | Medium |
| Fix section ordering | 2 minutes | Medium |
| Add "When to Use" bullets | 5 minutes | Low |
| Standardize input table | 5 minutes | Low |

**Total for complete fix:** 30-45 minutes per skill

**Quick pass (top 3 fixes only):** 15-20 minutes per skill

---

## Skill-Specific Examples

### Comedy/Creative Skills

**Common Issue:** Missing constraints around harmful content

**Fix:**
```markdown
## Constraints

- Do not punch down—humor should comfort the afflicted, not afflict the comfortable
- Do not sacrifice truth for cleverness
- Acknowledge cultural context and sensitivities
- Honor the subject matter—some things shouldn't be joked about
- Stay within the voice and style of the source material
```

### Technical/Analysis Skills

**Common Issue:** Vague workflows

**Fix:**
```markdown
## Workflow

### Step 1: Gather Input Data

Collect all relevant information:
- System specifications and requirements
- Current performance metrics
- Known issues and constraints
- Stakeholder expectations

### Step 2: Analyze Current State

Perform systematic analysis:
- Benchmark against standards
- Identify bottlenecks and inefficiencies
- Map dependencies
- Calculate key metrics

### Step 3: Generate Recommendations

Create actionable recommendations:
- Prioritize by impact and effort
- Estimate resource requirements
- Define success metrics
- Identify risks and mitigations
```

### Strategic/Business Skills

**Common Issue:** Missing concrete outputs

**Fix:**
```markdown
## Outputs

**Primary Output:** A strategic decision framework with clear recommendations

**Format:**
```markdown
## Strategic Analysis: [Topic]

### Current Situation
[2-3 sentence summary]

### Options Evaluated
1. [Option A]: [Pros/Cons]
2. [Option B]: [Pros/Cons]
3. [Option C]: [Pros/Cons]

### Recommendation
[Specific recommended action]

**Rationale:** [Why this option]
**Expected Outcome:** [What success looks like]
**Timeline:** [Implementation schedule]
**Resources Required:** [What's needed]
```

**Example output:** See Example section below.
```

---

## Getting Help

If you're stuck on a particular skill:

1. **Look at similar top-scoring skills** in TOP-SKILLS.md
2. **Check the template** at the end of QUALITY-ANALYSIS-SUMMARY.md
3. **Review the example** in the skill's own text
4. **Compare to the "Excellent" tier** skills for structure

---

## Quick Wins

Start with these for fastest impact:

1. **Fix all Good-tier skills first** (392 skills)
   - They need the least work
   - Gets you to 30% published quickly

2. **Batch fix by missing section:**
   - Day 1: Add "Outputs" to all missing
   - Day 2: Add "Constraints" to all missing
   - Day 3: Add numbered steps to all missing

3. **Use templates consistently:**
   - Copy from top skills
   - Adapt to specific context
   - Validate against checklist

---

## Before/After Example

### Before (Score: 63)

```markdown
---
name: campaign-analyzer
description: Analyzes marketing campaigns
---

# Campaign Analyzer

This skill helps you analyze marketing campaigns.

## The Process

Look at the campaign and identify what works and what doesn't. Think
about the audience and whether the messaging fits. Consider the budget
and timing.

## Example

Input: Marketing campaign
Output: Analysis showing good and bad parts.
```

### After (Score: 85)

```markdown
---
name: campaign-analyzer
description: Systematically evaluate marketing campaigns against strategic goals, audience alignment, and budget efficiency to identify strengths, weaknesses, and actionable improvements.
---

# Campaign Analyzer

This skill provides a structured framework for analyzing marketing campaigns
across multiple dimensions: audience-channel fit, messaging effectiveness,
budget allocation, and measurement strategy.

---

## When to Use

- Evaluating campaign performance mid-flight or post-launch
- Deciding whether to continue, modify, or kill an underperforming campaign
- Conducting competitive analysis of rival campaigns
- User asks "Is this campaign working?" or "How can we improve this?"
- Need objective assessment before scaling investment

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| campaign_description | Yes | Overview of campaign strategy, channels, and creative approach |
| target_audience | Yes | Demographic and psychographic profile of intended audience |
| budget | Yes | Total budget and allocation across channels |
| duration | Yes | Campaign timeline (start date, end date, or ongoing) |
| goals | No | Stated objectives and KPIs (if not provided, will infer) |
| performance_data | No | Available metrics (impressions, clicks, conversions, etc.) |

---

## Workflow

### Step 1: Map Campaign Fundamentals

Document the campaign structure:
- What is the core value proposition?
- What channels are being used?
- What is the creative approach?
- What is the call-to-action?

### Step 2: Evaluate Audience-Channel Alignment

Assess strategic fit:
- Does the channel reach the target audience?
- Is the messaging appropriate for the channel format?
- Does the creative resonate with audience preferences?
- Are there channel-audience mismatches?

### Step 3: Analyze Budget Efficiency

Review resource allocation:
- Is budget distributed according to channel effectiveness?
- Are there over/under-invested channels?
- What is the cost per desired action?
- Are there budget optimization opportunities?

### Step 4: Assess Measurement Strategy

Evaluate tracking and KPIs:
- Are success metrics clearly defined?
- Is performance trackable and being tracked?
- Do metrics align with campaign goals?
- Are there attribution or measurement gaps?

### Step 5: Generate Recommendations

Create actionable improvements:
- What's working and should be amplified?
- What's not working and should be modified or cut?
- What's missing from the current approach?
- What are the priority fixes by impact and effort?

---

## Outputs

**Primary Output:** A structured campaign analysis document with strengths,
weaknesses, and prioritized recommendations.

**Format:**
```markdown
## Campaign Analysis: [Campaign Name]

### Campaign Overview
- Objective: [Goal]
- Audience: [Target]
- Channels: [List]
- Budget: [Amount]
- Duration: [Timeline]

### Strengths
- [Strength 1]: [Why this works]
- [Strength 2]: [Why this works]

### Weaknesses
- [Weakness 1]: [Why this fails]
- [Weakness 2]: [Why this fails]

### Recommendations
1. [Priority 1]: [Specific action]
   - Impact: [High/Medium/Low]
   - Effort: [High/Medium/Low]
   - Expected outcome: [Result]

2. [Priority 2]: [Specific action]
   [...]
```

---

## Constraints

- Do not evaluate creative quality based on personal taste—focus on audience fit
- Do not recommend changes outside stated budget constraints
- Acknowledge data limitations when performance metrics are incomplete
- Honor campaign objectives even if you would have chosen different goals
- Present recommendations as options, not mandates

---

## Example

**Input:**
- campaign_description: Influencer partnerships for sustainable product launch
- target_audience: Millennials (25-40) interested in eco-friendly living
- budget: $50,000
- duration: 3 months
- goals: Build awareness and generate 500 qualified leads

**Output:**

## Campaign Analysis: Sustainable Product Launch

### Campaign Overview
- Objective: Launch new eco-friendly product with awareness and lead generation
- Audience: Millennials (25-40), sustainability-focused
- Channels: Instagram/TikTok influencer partnerships
- Budget: $50,000 over 3 months
- Duration: Q2 2026

### Strengths

**Audience-Channel Alignment:** Instagram and TikTok influencers are strong
channels for reaching sustainability-minded millennials. This demographic
trusts peer recommendations over brand advertising.

**Budget Appropriateness:** $50K allows for 8-10 micro-influencers (10K-100K
followers) or 3-4 mid-tier influencers (100K-500K), providing good reach
without overextending.

**Authentic Messaging Potential:** Sustainability focus can leverage influencer
credibility if partners are genuine advocates, not just paid promoters.

### Weaknesses

**Measurement Gap:** Campaign goals mention "awareness" and "leads" but lacks
specific KPIs. How is awareness measured? What defines a "qualified" lead?

**Platform Risk:** Full dependency on social platforms creates vulnerability
to algorithm changes and makes the campaign unverifiable independently.

**Influencer Vetting Unclear:** No indication of how influencers will be
selected and vetted for authentic sustainability credentials. Risk of
greenwashing backlash.

**No Owned Media Component:** Campaign relies entirely on rented attention
(influencer audiences). No strategy for building owned audience.

### Recommendations

1. **Define Measurable KPIs** (High Impact, Low Effort)
   - Awareness: 100K impressions, 5% engagement rate
   - Leads: 500 email sign-ups via unique tracking links
   - Expected outcome: Clear success/failure criteria, ability to optimize

2. **Implement Influencer Vetting Process** (High Impact, Medium Effort)
   - Audit influencer sustainability practices, not just follower count
   - Require disclosure of brand partnerships to assess authenticity
   - Expected outcome: Reduce greenwashing risk, increase campaign credibility

3. **Add Owned Media Component** (Medium Impact, Medium Effort)
   - Allocate $10K (20%) to content marketing and email list building
   - Repurpose influencer content for owned channels
   - Expected outcome: Build asset that survives beyond 3-month campaign

4. **Build in A/B Testing** (Medium Impact, Low Effort)
   - Test 2-3 different messaging approaches in first 30 days
   - Reallocate budget to top performers for remaining 60 days
   - Expected outcome: 15-25% improvement in conversion rate

**Overall Assessment:** Solid foundation with good audience-channel fit, but
needs clearer measurement strategy and risk mitigation. With recommended
improvements, strong potential for success.

---

## Integration

This skill is part of the **Marketing Strategy** expert persona. Use it when
campaigns need objective evaluation or improvement.
```

---

*This guide covers the most common fixes needed across 1,445 skills. Apply systematically for best results.*
