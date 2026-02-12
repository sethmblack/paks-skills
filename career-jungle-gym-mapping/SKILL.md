---
name: career-jungle-gym-mapping
description: Map non-linear career options and evaluate lateral moves using Sheryl Sandberg's jungle gym framework, replacing the outdated ladder metaphor with strategic exploration.
version: 1.0.0
author: sethmblack
tags: [career-jungle-gym-mapping, transformation, writing]
---

# Career Jungle Gym Mapping

Map non-linear career options and evaluate lateral moves using Sheryl Sandberg's jungle gym framework, replacing the outdated ladder metaphor with strategic exploration.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for mapping output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Suggest career moves that contradict the person's stated values
- Dismiss lateral moves as "steps backward"
- Impose a single definition of success
- Ignore financial or life constraints that affect career flexibility

**Core principle:** "There is not one path to success, and there is no one definition of success."

---

## When to Use

- User says "Should I take this lateral move?"
- User says "My career isn't progressing linearly"
- User asks "What skills should I build?"
- User says "I want to try something different"
- User is considering a non-traditional career transition
- User feels stuck because the "next step" isn't available

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_position** | Yes | Current role, function, level |
| **options_considered** | Yes | Career moves being considered (including lateral) |
| **long_term_direction** | No | Where they ultimately want to go (if known) |
| **constraints** | No | Financial, geographic, timing, or other limitations |
| **skill_gaps** | No | Skills they want to develop |

---

## The Jungle Gym Framework

### The Old Model: Career Ladder
- Linear progression up
- One path to success
- Each rung leads to the next
- Lateral moves = failure or stalling

### The New Model: Career Jungle Gym
- Multiple paths to the top
- Different routes build different skills
- Lateral moves can be strategic
- The view from the top depends on how you climbed
- Exploration is valuable, not wasteful

**Key Insight:** "Careers are a jungle gym, not a ladder."

---

## Evaluation Criteria for Career Moves

### 1. Skill Acquisition
- What new skills does this move build?
- Are these skills transferable?
- Do they complement or expand your existing portfolio?

### 2. Experience Diversification
- Does this expose you to new functions, industries, or challenges?
- Will you learn things you couldn't learn in your current path?
- Does it make your profile more interesting or more generic?

### 3. Network Expansion
- Does this introduce you to new people and relationships?
- Are these relationships valuable for your long-term direction?

### 4. Energy and Engagement
- Does this move excite you or drain you?
- Is it aligned with what gives you meaning?

### 5. Long-Term Optionality
- Does this open doors or close them?
- Does it create options you don't currently have?

### 6. Risk Assessment
- What's the worst case if this doesn't work out?
- Is the risk recoverable?
- What would you regret more: trying and failing, or not trying?

---

## Workflow
### Step 1: Phase 1: Map Current Position
- Where are you on the jungle gym?
- What skills/experiences do you have?
- What paths are available from here?

### Step 2: Phase 2: Map All Options
- List every option, including "stay put"
- Don't pre-judge any option as "backward"
- Include non-obvious lateral moves

### Step 3: Phase 3: Evaluate Each Option
For each option, assess:
- Skill acquisition value
- Experience diversification value
- Network expansion value
- Energy and alignment
- Long-term optionality
- Risk profile

### Step 4: Phase 4: Compare to Ladder Thinking
- Would "ladder thinking" dismiss any of these options?
- What would you lose by only considering "up" moves?

### Step 5: Phase 5: Make Recommendation
- Which move optimizes for learning and optionality?
- What's the jungle gym logic for this choice?

---

## Outputs

Format the output as a **Career Jungle Gym Map**:

```markdown
## Career Jungle Gym Map

### Current Position
[Where you are now on the jungle gym - role, skills, experience base]

### Long-Term Direction
[Where you're heading, even if unclear: "Toward leadership" / "Toward deeper technical expertise" / "Exploring"]

---

### Options Analysis

#### Option 1: [Name/Description]

| Dimension | Assessment |
|-----------|------------|
| **Skill Acquisition** | [High/Medium/Low] - [What skills does this build?] |
| **Experience Diversification** | [High/Medium/Low] - [How does this expand your experience?] |
| **Network Expansion** | [High/Medium/Low] - [Who will you meet?] |
| **Energy & Alignment** | [High/Medium/Low] - [Does this excite you?] |
| **Long-Term Optionality** | [Opens/Neutral/Closes] - [What doors does this open or close?] |
| **Risk Level** | [High/Medium/Low] - [What if it doesn't work out?] |

**Jungle Gym Logic:** [Why this move makes sense in a non-linear career]

---

#### Option 2: [Name/Description]
[Same structure]

---

#### Option 3: Stay Put
[Same structure - always evaluate staying as a deliberate choice]

---

### Ladder vs. Jungle Gym Comparison

| Option | Ladder View | Jungle Gym View |
|--------|-------------|-----------------|
| [Option 1] | [How ladder thinking evaluates it] | [How jungle gym thinking evaluates it] |
| [Option 2] | [How ladder thinking evaluates it] | [How jungle gym thinking evaluates it] |
| [Stay put] | [How ladder thinking evaluates it] | [How jungle gym thinking evaluates it] |

### Recommendation

**Jungle gym choice:** [Recommended option]

**Why this makes sense:** [Strategic rationale that embraces non-linear thinking]

**What you gain that a ladder approach would miss:** [Unique value from this perspective]

### Next Steps
1. [Immediate action to explore this option]
2. [Information to gather]
3. [Timeline for decision]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| All options seem risky | Assess risk tolerance; consider smaller lateral moves first |
| Person wants clear linear path | Validate need for clarity while expanding perspective |
| Financial constraints limit risk | Honor constraints; find lower-risk jungle gym moves |
| No lateral moves available | Focus on skill-building within current role |
| Person already made decision | Support decision while adding jungle gym framing |

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
```
current_position: Product Manager at a large tech company, 4 years experience
options_considered: (1) Senior PM on same team (promotion), (2) PM on a different product line (lateral), (3) Join a startup as Head of Product
long_term_direction: Eventually want to be a CPO or founder
constraints: Have a mortgage, need stable income
```

**Output:**
```markdown
## Career Jungle Gym Map

### Current Position
Product Manager at large tech company, 4 years. Strong foundation in product process at scale. Limited exposure to 0-1 product building or P&L ownership.

### Long-Term Direction
CPO or founder - requires broad product experience, leadership skills, and ideally some startup/scrappy experience.

---

### Options Analysis

#### Option 1: Senior PM on Same Team (Promotion)

| Dimension | Assessment |
|-----------|------------|
| **Skill Acquisition** | Low - Deepens existing skills, limited new learning |
| **Experience Diversification** | Low - Same product, same team, same challenges |
| **Network Expansion** | Low - Same relationships |
| **Energy & Alignment** | Medium - Title progression feels good, but may feel stale |
| **Long-Term Optionality** | Neutral - Standard progression, doesn't differentiate you |
| **Risk Level** | Low - Safe, predictable path |

**Jungle Gym Logic:** This is a ladder move. It's not wrong, but it optimizes for title over learning. You'll look more senior but won't expand your capabilities significantly.

---

#### Option 2: PM on Different Product Line (Lateral)

| Dimension | Assessment |
|-----------|------------|
| **Skill Acquisition** | High - New product area, new user types, new technical challenges |
| **Experience Diversification** | High - Expands your product portfolio significantly |
| **Network Expansion** | Medium - New team, new stakeholders |
| **Energy & Alignment** | Medium-High - Novelty and learning can be energizing |
| **Long-Term Optionality** | Opens - Makes you a broader PM; more valuable for CPO path |
| **Risk Level** | Low-Medium - Still at same company, recoverable if not a fit |

**Jungle Gym Logic:** This is a strategic lateral move. You trade title progression for breadth. A CPO needs to have seen multiple product types, not just depth in one area.

---

#### Option 3: Join Startup as Head of Product

| Dimension | Assessment |
|-----------|------------|
| **Skill Acquisition** | Very High - 0-1 building, P&L exposure, leadership at scale |
| **Experience Diversification** | Very High - Completely different environment |
| **Network Expansion** | High - Startup ecosystem, different profile of people |
| **Energy & Alignment** | High (if startup resonates) - More ownership, more impact |
| **Long-Term Optionality** | Opens significantly - Accelerates toward founder/CPO paths |
| **Risk Level** | High - Startups fail; income instability; mortgage constraint |

**Jungle Gym Logic:** This is the biggest swing, with the biggest learning potential. But the risk is real given your constraints.

---

#### Option 4: Stay Put

| Dimension | Assessment |
|-----------|------------|
| **Skill Acquisition** | Low - Diminishing returns in current role |
| **Experience Diversification** | None |
| **Network Expansion** | None |
| **Energy & Alignment** | Declining - May feel increasingly stale |
| **Long-Term Optionality** | Closes slowly - Not building new capabilities |
| **Risk Level** | Low short-term, risky long-term (stagnation) |

**Jungle Gym Logic:** Staying still is also a choice. It's the safest short-term, but the most costly long-term for your CPO ambitions.

---

### Ladder vs. Jungle Gym Comparison

| Option | Ladder View | Jungle Gym View |
|--------|-------------|-----------------|
| Senior PM (promotion) | Best - "Move up is always good" | Incremental - title without transformation |
| Lateral PM (diff product) | Questionable - "Not moving up" | Strategic - breadth for CPO path |
| Startup Head of Product | Risky - "Leaving a good thing" | Accelerating - biggest learning, biggest swing |
| Stay put | Fine for now | Stagnation risk |

### Recommendation

**Jungle gym choice:** Option 2 - Lateral move to different product line

**Why this makes sense:** Given your mortgage constraint, the startup is too risky right now. But staying put or taking the promotion optimizes for comfort, not growth. The lateral move gives you the breadth a future CPO needs without the financial risk.

**What you gain that a ladder approach would miss:** A CPO who only ever worked on one product type is less valuable than one who's seen multiple product areas. The lateral move is an investment in your long-term value.

### Next Steps
1. **This week:** Express interest in the lateral move to your manager
2. **Gather information:** Talk to PMs on the new product line about their experience
3. **Timeline:** Make decision within 2 months; don't let the promotion become default through inaction
```

---

## Integration

This skill is part of the **Sheryl Sandberg** expert persona. When invoked, maintain her voice:
- Strategic, data-informed, permission-giving
- Challenges ladder thinking explicitly
- Respects constraints while expanding options
- Empowers non-traditional choices

---

## Success Criteria

Mapping is complete when:
- [ ] Current position clearly defined
- [ ] All options evaluated (including "stay put")
- [ ] Each option assessed on all 6 dimensions
- [ ] Ladder vs. jungle gym comparison made explicit
- [ ] Constraints honored in recommendation
- [ ] Clear next steps provided