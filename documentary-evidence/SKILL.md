---
name: documentary-evidence
description: A skill for building arguments through systematic citation of primary sources - letting documents speak louder than claims.
version: 1.0.0
author: sethmblack
tags: [documentary-evidence, writing]
---

# Documentary Evidence

A skill for building arguments through systematic citation of primary sources - letting documents speak louder than claims.

## When to Use

- When making claims that will be contested
- When authority of the argument should rest on evidence, not the arguer
- When permanent record matters more than persuasive style
- When opponents can be refuted by their own documents

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Identify What Needs Proving

Break your claim into components:
- What specific facts must be established?
- What causal connections must be demonstrated?
- What objections must be preempted?
- What standards of proof does your audience expect?

Each component needs its own documentary support.

### Step 2: Phase 2: Locate Primary Sources

Find original documents:
- Official records (government, corporate, organizational)
- Internal communications (memos, emails, meeting notes)
- Public statements (speeches, press releases, testimony)
- Legal documents (filings, contracts, court records)
- Academic sources (peer-reviewed studies, data)
- Contemporaneous accounts (journalism, reports)

Primary sources are harder to dismiss than secondary interpretation.

### Step 3: Phase 3: Evaluate Source Quality

Assess each source:
- Is it authentic? (Could it be forged or misattributed?)
- Is it complete? (Has it been selectively quoted or redacted?)
- Is it contemporaneous? (Was it created at the time of events?)
- Is it authoritative? (Who created it and why?)
- Is it accessible? (Can others verify it?)

Weak sources undermine even strong arguments.

### Step 4: Phase 4: Build the Chain

Connect sources to claims:
- Each factual claim should have explicit source citation
- Complex claims need multiple supporting sources
- Anticipate objections and address with additional sources
- Show your work - readers should be able to follow the chain

The argument should be traceable from claim to source.

### Step 5: Phase 5: Present Systematically

Structure for maximum clarity:
- State claim, then provide supporting evidence
- Use consistent citation format
- Quote directly when possible rather than paraphrasing
- Acknowledge limitations and gaps
- Distinguish certain from probable from speculative

### Step 6: Phase 6: Preserve the Record

Ensure sources remain available:
- Archive sources locally (documents disappear)
- Use persistent links where possible
- Note access dates for online sources
- Consider how adversaries might challenge sources

The argument is only as permanent as its sources.

## Output Format

A documentary evidence compilation including:
1. Claims stated precisely
2. Sources for each claim with quality assessment
3. Citation chain showing claim-to-source connection
4. Acknowledgment of gaps and limitations
5. Preservation notes
6. Anticipated objections addressed through documentation

## Constraints

- Documents can be misinterpreted - context matters
- Some claims can't be documented (classified, destroyed, never written)
- Over-documentation can obscure the argument
- Adversaries may challenge source authenticity
- Documentary style can be less engaging - balance with accessibility

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

**Input**: Document the claim that Company X knew about product danger before public disclosure

**Output**:
"Claim: Company X had internal evidence of danger by [date], [years] before public acknowledgment. Source 1: Internal memo dated [date] (obtained through [litigation/FOIA]) showing test results indicating danger. Quality: Authenticated in court proceedings, complete document, contemporaneous. Source 2: Email thread from [date] showing executive awareness of memo. Quality: Produced in discovery, partial (some redactions), direct evidence of knowledge. Source 3: Public statement from [later date] claiming no evidence of danger. Quality: Publicly available, establishes contradiction. Source 4: Expert testimony that test results memo would have been understood as indicating danger. Quality: Qualified expert, but interpretation rather than fact. Chain: Memo proves knowledge of data → Email proves executive awareness → Statement proves public denial → Timeline proves gap. Limitations: Cannot document every executive's awareness, only those in email chain. Preserved: All documents archived locally, court filings available through [database]."

## Integration

Works with:
- **documentation-as-resistance**: Documentary evidence is a form of documentation
- **evidence-authentication**: Assessing source credibility
- **disclosure-calculus**: Documents may come from whistleblowers