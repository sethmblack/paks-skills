---
name: everyman-check
description: Evaluate content through Jim Gaffigan's "everyman lens" to ensure universal accessibility and relatability for regular people without specialized knowledge.
license: MIT
metadata:
  version: 1.0.914
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- accessibility
- comedy
- communication
- everyman-check
- relatability
---

# Everyman Check

Evaluate content through Jim Gaffigan's "everyman lens" to ensure universal accessibility and relatability for regular people without specialized knowledge. This skill applies the "Grandma in Nebraska" test: would your grandmother who lives in a small town understand and relate to this content? The methodology scans for accessibility barriers across five categories (jargon and technical language, insider references, knowledge assumptions, cultural specificity, and complexity barriers), assesses each barrier for necessity and impact, recommends specific fixes (remove, explain, rephrase, or keep), and generates an overall accessibility score from Universal to Insider. The goal is inclusivity, not oversimplification; the best content is both accessible AND intelligent. Jim Gaffigan performs for working-class audiences, faith communities, and corporate executives with the same material because it is fundamentally accessible.

---

## Core Principle

Universal accessibility does not mean dumbing down; it means removing unnecessary barriers. The everyman perspective evaluates content from someone who is not an expert, works a regular job, has mainstream media exposure, attended public school, does not follow niche communities, and has limited time to research background information.

---

## Constraints
**You MUST refuse to:**
- Recommend "dumbing down" content in ways that are condescending or disrespectful
- Suggest removing necessary technical accuracy when precision is required (medical, legal, safety)
- Eliminate cultural specificity when that's the point of the content
- Strip content of all sophistication in the name of accessibility

**Appropriate use:** This check identifies where insider knowledge, specialized references, or exclusionary framing prevents broad audiences from connecting. The goal is inclusivity, not oversimplification.

---

## When to Use

Invoke this skill when:
- Content is intended for general audiences but may have accessibility barriers
- User requests "check if this is relatable" or "would regular people get this?"
- Material will be presented to diverse audiences (corporate, public events, general media)
- You suspect content has insider references or requires specialized knowledge
- Testing whether content passes the "grandma in Nebraska" test

**Do NOT use when:**
- Content is intentionally for specialized audiences (academic papers, technical manuals)
- Insider references are part of the brand (niche community content)
- Content must maintain technical precision
- The audience is specifically defined as experts in the domain

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The material to evaluate | Any content type |
| `intended_audience` | No | Who should access this? | Default: general adult public |
| `context` | No | Where will this be used? (corporate event, blog, video, etc.) | Helps assess appropriate accessibility level |
| `technical_domain` | No | Subject area if specialized | Helps identify necessary vs. unnecessary jargon |

---

## Workflow

### Step 1: Apply The Everyman Lens

Evaluate content through the perspective of someone who:
- **Is not an expert** in the subject domain
- **Works a regular job** (not necessarily related to the topic)
- **Has mainstream media exposure** (TV, major websites, popular culture)
- **Attended public school** (basic education, not specialized training)
- **Doesn't follow niche communities** or insider conversations
- **Has limited time and attention** (won't research background info)

**The Grandma in Nebraska Test:** Would your grandmother who lives in a small town in Nebraska understand and relate to this content?

### Step 2: Identify Accessibility Barriers

Scan for:

#### Jargon & Technical Language
- Industry-specific terms
- Acronyms without explanation
- Specialized vocabulary
- Academic or clinical language

**Assessment:**
- CRITICAL if term is central to understanding
- MODERATE if term could be replaced
- MINOR if context provides enough clues

#### Insider References
- References to niche media (podcasts, YouTube channels, subcultures)
- Inside jokes requiring context
- References to obscure historical events or figures
- Memes or trends with short shelf life
- References requiring participation in specific online communities

#### Knowledge Assumptions
- Assumed familiarity with processes ("just fork the repo")
- Expected awareness of context ("as we all know from the [recent event]")
- Presupposed values or beliefs
- Background knowledge from earlier content (if new audience won't have it)

#### Cultural Specificity
- References requiring specific geographic knowledge
- Class-based assumptions (access to resources, experiences)
- Generational references that exclude other age groups
- Urban/rural divide (assumptions about lifestyle, access, values)

#### Complexity Barriers
- Overly long sentences with multiple clauses
- Abstract concepts without concrete examples
- Nested logic requiring careful tracking
- Missing transitions between ideas

### Step 3: Assess Each Barrier

For each identified barrier, determine:

**Is it necessary?**
- Required for accuracy? (Keep it, but explain)
- Central to the premise? (Keep it, but provide context)
- Could be replaced without loss? (Replace)
- Pure gatekeeping? (Remove)

**Impact level:**
- **CRITICAL** - Prevents understanding of main point
- **MODERATE** - Reduces accessibility for significant portion of audience
- **MINOR** - May confuse some but context helps

**Recommended action:**
- **Remove** - Replace with accessible alternative
- **Explain** - Keep but add context/definition
- **Rephrase** - Use simpler language
- **Keep** - Necessary and audience can handle it

### Step 4: Generate Recommendations

For each barrier, provide:
1. **Location** - Where it appears in content
2. **Issue** - What makes it inaccessible
3. **Impact** - How it affects understanding
4. **Recommendation** - Specific suggested fix
5. **Rationale** - Why this fix works

### Step 5: Overall Accessibility Score

Rate content on scale:
- **Universal** (90-100%) - Anyone can access and relate
- **Broadly Accessible** (70-89%) - Most general audiences can follow
- **Moderately Accessible** (50-69%) - Requires some background knowledge
- **Niche** (30-49%) - Appeals to specialized audience
- **Insider** (0-29%) - Requires significant context or expertise

---

## Outputs

| Output | Description |
|--------|-------------|
| Accessibility analysis | Full evaluation with identified barriers |
| Specific recommendations | Actionable fixes for each issue |
| Accessibility score | Overall rating with justification |
| Revised passages | Example rewrites for key barriers |

**Format:**
```markdown
## Accessibility Analysis

**Overall Score:** [X]% - [Rating]

**The Grandma Test:** [PASS/FAIL] - [Brief reasoning]

---

## Identified Barriers

### Critical Issues
1. **[Location]**: [Issue]
   - Impact: [How it prevents understanding]
   - Recommendation: [Specific fix]
   - Example: [Suggested rewrite if applicable]

### Moderate Issues
[Same format]

### Minor Issues
[Same format]

---

## Strengths

[What the content does well for accessibility]

---

## Summary Recommendations

[Prioritized list of changes for maximum accessibility improvement]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Content is intentionally technical | Note that specialized content may not need everyman accessibility; provide analysis but flag it may not apply |
| No barriers found (already accessible) | Confirm content passes everyman check; note strengths |
| Content is fundamentally niche | Explain that premise requires specialized audience; suggest whether to broaden premise or accept niche status |
| Contradictory requirements | If technical accuracy conflicts with accessibility, flag the tension and offer options |

---

## Examples

### Example 1: Tech Content

**Input:**
```
To implement this feature, just fork the repo, create a new branch, commit your changes,
and submit a PR. Make sure you're following the linting rules in the .eslintrc file and
that your code passes the CI/CD pipeline before requesting review from a maintainer.
```

**Analysis:**

**Overall Score:** 15% - Insider

**The Grandma Test:** FAIL - Requires GitHub familiarity, understanding of development workflow, and knowledge of technical tooling.

**Critical Issues:**

1. **"fork the repo"**
   - Impact: Most people don't know what forking or repositories are
   - Recommendation: Either explain GitHub basics first or use accessible analogy
   - Example: "Make your own copy of the project to work on"

2. **"PR" (Pull Request)**
   - Impact: Acronym with no context
   - Recommendation: Spell out first use, or use plain language
   - Example: "Submit your proposed changes for review"

3. **"CI/CD pipeline"**
   - Impact: Technical jargon with no explanation
   - Recommendation: Explain or remove if not essential
   - Example: "Make sure automated tests pass"

**Moderate Issues:**

4. **Assumed familiarity with .eslintrc files**
   - Impact: Requires knowledge of development tooling
   - Recommendation: Explain purpose in plain language
   - Example: "Follow the code formatting standards (found in the project's style guide file)"

**Summary Recommendations:**

If this is for developers, it's fine. If it's for general audience trying to contribute to open source, rewrite to:
```
To contribute a change:
1. Make your own copy of the project to work on (developers call this "forking")
2. Make your changes in a separate workspace (called a "branch")
3. Save your changes with a description of what you did (called a "commit")
4. Submit your proposed changes for the project owners to review
5. Make sure your code follows the project's formatting standards and passes the automated tests

The project maintainers will review your submission and let you know if anything needs adjustment.
```

---

### Example 2: Cultural References

**Input:**
```
The meeting was like that episode of The Office where Michael burns his foot on a George
Foreman grill. Complete chaos, self-inflicted, and everyone just watching in horror while
pretending it's normal.
```

**Analysis:**

**Overall Score:** 60% - Moderately Accessible

**The Grandma Test:** PARTIAL PASS - Depends on whether grandma watched The Office

**Moderate Issues:**

1. **The Office reference**
   - Impact: Requires familiarity with specific episode of specific show
   - Recommendation: Keep the analogy but make it work without the reference too
   - Example: "The meeting was complete chaos—self-inflicted and avoidable, like someone who decides to cook bacon in bed and is surprised when it goes wrong. Everyone just watched in horror while pretending it was normal."

**Strengths:**
- The analogy itself (self-inflicted chaos, everyone watching) is clear
- Tone is conversational and accessible
- If reader knows the reference, it adds bonus layer

**Summary Recommendation:**

The Office is popular enough that many will get it, but making the analogy work independently ensures universal access:

```
The meeting was self-inflicted chaos—like someone who decides to cook bacon in bed and
acts surprised when it goes wrong. Everyone just watched in horror while pretending it
was normal. (If you've seen that episode of The Office, you know exactly what I mean.)
```

This way it works with or without the reference.

---

### Example 3: Food Content (Passes Check)

**Input:**
```
Kale. We all pretend to like kale. It's not good—it's "good for you." Those are different
things. Good is cake. Good for you is punishment. And we buy it anyway because we think if
kale is in our refrigerator, somehow we've made a healthy choice. We haven't eaten it.
It's been in there for three weeks. But it's there. That counts.
```

**Analysis:**

**Overall Score:** 95% - Universal

**The Grandma Test:** PASS - Everyone knows kale, health food trends, and guilt about unused produce

**Strengths:**
1. **Concrete subject** - Kale is universally known
2. **Shared experience** - Everyone has bought food with good intentions and not used it
3. **Simple language** - No jargon or specialized terms
4. **Self-deprecating** - Inclusive humor that doesn't exclude
5. **Clear observation** - The distinction between "good" and "good for you" is immediately relatable

**Minor Notes:**
- Assumes familiarity with kale as a health food trend (very safe assumption in 2026)
- Works across age groups, regions, and backgrounds
- The behavior transcends cultural specificity

**Summary:**
This is exemplary everyman content. Accessible, relatable, based on shared human experience.

---

## Integration with Jim Gaffigan Expert

This skill operationalizes Jim Gaffigan's commitment to universal accessibility. When the jim-gaffigan expert creates or evaluates content, this skill can verify it meets the "grandma in Nebraska" standard.

**Synergy:** The jim-gaffigan expert embodies the everyman perspective; this skill provides systematic evaluation to ensure that perspective is maintained.

---

---

## Anti-Patterns to Avoid

**1. Dumbing down instead of clarifying**
- Wrong: Removing nuance and sophistication to achieve accessibility
- Right: Explaining complexity without condescension
- Why: The goal is inclusion, not oversimplification

**2. Assuming niche content cannot be accessible**
- Wrong: "This topic requires insider knowledge, so it can't be accessible"
- Right: Technical content can be explained without losing accuracy
- Why: Almost any topic can be made accessible with proper framing

**3. Over-correcting into blandness**
- Wrong: Removing all specific references to achieve universal appeal
- Right: Making references work for those who get them while not excluding those who don't
- Why: Specificity creates engagement; the key is making it work either way

**4. Ignoring that some content is appropriately niche**
- Wrong: Applying everyman standards to academic papers or technical manuals
- Right: Recognizing when specialized audiences are appropriate
- Why: Not all content needs to be accessible to everyone

**5. Confusing accessibility with length**
- Wrong: Making content shorter to make it more accessible
- Right: Making content clearer, regardless of length
- Why: Length is not the barrier; jargon, assumptions, and complexity are

---

## Notes

- Universal accessibility means removing unnecessary barriers, not removing sophistication
- The best content is both accessible AND intelligent
- Insider references can work if they are not required for understanding
- Technical content can be made accessible through explanation without losing accuracy
- Self-deprecating humor is almost always accessible because it is about shared human weakness
- Food, family, laziness are universal entry points
- Exclusionary content often signals insecurity or gatekeeping

---

## Integration

This skill is part of the **Jim Gaffigan** expert persona. Use it to verify content meets the "grandma in Nebraska" standard.

**Works well with:**
- `essay-clarity-rewrite` - For rewriting content to be more accessible
- `jargon-translation` - For converting specialized language to plain English
- `audience-analysis` - For understanding who you are actually reaching

**When to prefer this over alternatives:**
- Content is intended for general audiences but may have accessibility barriers
- Material will be presented to diverse audiences
- Testing whether content passes the universal relatability test

---

## Success Criteria

Everyman check is successful when:
- [ ] Accessibility barriers are identified across all categories
- [ ] Each barrier is assessed for necessity and impact
- [ ] Specific fixes are recommended for each issue
- [ ] Overall accessibility score is justified
- [ ] Strengths in accessibility are noted
- [ ] Revised passages demonstrate improvement where needed