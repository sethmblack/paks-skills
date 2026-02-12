---
name: inject-therapy-language
description: Casually integrate mental health and therapy concepts (boundaries, catastrophic
  thinking, anxious attachment, bipolar disorder) into content as normal vocabulary
  rather than clinical jargon or heav...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- inject-therapy-language
- transformation
- writing
---

# Inject Therapy Language

Casually integrate mental health and therapy concepts (boundaries, catastrophic thinking, anxious attachment, bipolar disorder) into content as normal vocabulary rather than clinical jargon or heavy topics.

---

## Constitutional Constraints

This skill must NEVER:
- Use therapy language incorrectly or inaccurately
- Trivialize serious mental health conditions
- Present therapy concepts as jokes without context
- Reinforce stigma around mental health or medication
- Use diagnoses as punchlines (the context/insight is the comedy, not the condition itself)

The goal is normalization, not mockery. Mental health language should be integrated casually, making it accessible without losing accuracy.

---

## When to Use

Invoke this skill when you encounter:
- Mental health or emotional content
- Relationship or dating discussions
- Self-improvement or personal development topics
- Discussions about worry, planning, or overthinking
- Content about boundaries or self-care
- Situations involving emotional patterns or behaviors

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | Content to enhance with therapy language | "I worry too much." |
| `therapy_concept` | No | Specific concept to integrate | "catastrophic thinking" |
| `tone` | No | How casual/serious (casual/balanced) | "casual" (default: casual) |

---

## Workflow

### Step 1: Identify the Underlying Concept

What's the psychological or emotional pattern being described? What's the clinical or therapeutic term for this behavior?

**Example:** "I worry too much" → catastrophic thinking, anxiety, rumination

### Step 2: Select the Appropriate Therapy Term

Choose terminology that's:
- Clinically accurate
- Widely understood (or contextually clear)
- Appropriate for the situation
- Not overly technical

**Common terms:** boundaries, catastrophic thinking, anxious attachment, avoidant attachment, emotional regulation, trauma response, defense mechanism, projection, gaslighting (use carefully), codependency, people-pleasing, rumination, executive dysfunction

### Step 3: Frame with "My Therapist Says..."

The most casual integration uses this phrase as a framing device, making therapy as normal as any other conversation source.

**Template:** "My therapist says I have [term]. I prefer to call it [humorous reframe]."

**Example:** "My therapist says I have 'catastrophic thinking.' I prefer to call it 'being prepared for reality.'"

### Step 4: Alternative Casual Integrations

If "my therapist says" doesn't fit, integrate the language in other casual ways:

- Direct use: "I have anxious attachment, which explains why..."
- Medication reference: "I'm on antidepressants" (stated as context, not confession)
- Diagnosis mention: "Since my bipolar diagnosis, I..."
- Boundary language: "That crosses my boundaries"
- Processing language: "I'm still processing that trauma"

### Step 5: Ensure Normalization, Not Dramatization

The tone should be matter-of-fact, like discussing the weather. Not heavy, confessional, or attention-seeking.

**Pass:** "I'm on antidepressants" (context)
**Fail:** "I have to take antidepressants because I'm broken" (dramatization)

---

## Outputs

Returns the transformed content with:
- Therapy terminology integrated casually
- Clinical accuracy maintained
- Normalization achieved (not heavy or dramatic)
- Humor coming from context/insight, not diagnosis itself

---



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


## Error Handling

| Situation | Response |
|-----------|----------|
| No clear therapy concept applies | Decline transformation |
| Term would be inaccurate | Choose different term or skip |
| Content already uses therapy language | Enhance existing usage or skip |
| Concept requires more explanation | Add brief context without over-explaining |

---

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Examples

### Example 1: Worrying

**Input:** "I worry about everything going wrong."

**Output:** "My therapist says I have 'catastrophic thinking.' I prefer to call it 'being prepared for reality.' She disagrees. We're working on it. By which I mean I'm catastrophizing about therapy."

### Example 2: Relationship Patterns

**Input:** "I always date people who are emotionally unavailable."

**Output:** "I have anxious attachment, which means I'm drawn to avoidant people like a moth to an emotionally distant flame. My therapist calls it 'recreating familiar patterns.' I call it 'having a type.' We're both right, unfortunately."

### Example 3: Boundaries

**Input:** "I have trouble saying no to people."

**Output:** "I'm working on boundaries. Which is therapist-speak for 'learning to say no without writing a 500-word apology email afterward.' So far I've made it to 300 words. Progress."

### Example 4: Medication

**Input:** "I take medication for my mental health."

**Output:** "I'm on antidepressants and a mood stabilizer. When I Googled my medication combo, it turns out everything I'm taking is for bipolar disorder. Went back to my psychiatrist and asked, 'Do we think...' and she was like, 'Oh yeah.' So that was a fun discovery."

### Example 5: Decision-Making

**Input:** "I struggle to make decisions."

**Output:** "My therapist says I have executive dysfunction, which is a fancy way of saying I can research seventeen options for dish soap but can't actually choose one. The clinical term makes it sound more legitimate than 'I'm standing in Target having a crisis about scent profiles.'"

### Example 6: People-Pleasing

**Input:** "I always try to make everyone happy."

**Output:** "I'm a people-pleaser, which my therapist says is a trauma response. I say it's Midwestern upbringing. She says those might be the same thing. Now I'm people-pleasing my therapist by agreeing with her, which she pointed out, which is very rude but also accurate."

---

## Common Therapy Terms to Use

### Anxiety & Worry
- Catastrophic thinking
- Rumination
- Anticipatory anxiety
- Generalized anxiety

### Attachment & Relationships
- Anxious attachment
- Avoidant attachment
- Secure attachment (rarely, usually ironically)
- Codependency
- Enmeshment

### Boundaries & Behavior
- Boundaries (setting, maintaining, crossing)
- People-pleasing
- Emotional regulation
- Defense mechanism

### Diagnoses & Conditions
- Bipolar disorder (I or II)
- Depression
- ADHD
- Executive dysfunction
- Panic disorder

### Medication (stated casually)
- Antidepressants
- Mood stabilizers
- Anti-anxiety medication
- Klonopin, SSRIs (specific names)

### Processing & Growth
- Trauma response
- Processing
- Coping mechanism
- Maladaptive behavior

---

## Integration with Taylor Tomlinson Expert

This skill is central to Taylor Tomlinson's comedy approach. It exemplifies her:
- Casual normalization of mental health treatment
- Therapy as ordinary conversation topic
- Medication mentioned as context, not confession
- Clinical terms deployed with humor and accuracy

When used by the Taylor Tomlinson expert, combine with:
- Anxious precision for deeper exploration of thought patterns
- Generational contradiction (therapy-literate but emotionally avoidant)
- Dark turn pivots for added impact

---

## Constraints

- Must maintain clinical accuracy—don't misuse terms
- Keep it casual—not heavy, confessional, or dramatic
- Don't explain unless necessary—assume therapy literacy
- Humor comes from context, not diagnosis itself
- Avoid reinforcing stigma or making light of serious conditions
- Never present mental health as "quirky" rather than real

---

## Success Criteria

A successful therapy language injection:
- ✓ Uses clinically accurate terminology
- ✓ Integrates casually (matter-of-fact tone)
- ✓ Normalizes rather than dramatizes
- ✓ Humor comes from insight/context, not condition
- ✓ Feels natural, not forced or preachy
- ✓ Reduces stigma through casual integration
- ✓ Maintains accessibility without over-explaining