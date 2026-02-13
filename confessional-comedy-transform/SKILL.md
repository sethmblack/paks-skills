---
name: confessional-comedy-transform
description: Transform generic observations or content into Nikki Glaser-style confessional comedy by leading with personal embarrassment, adding hyper-specific details, revealing universal truth, and landing w...
license: MIT
metadata:
  version: 1.0.3651
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- confessional-comedy-transform
- observational
- transformation
- writing
---

# Confessional Comedy Transform

Transform generic observations or content into Nikki Glaser-style confessional comedy by leading with personal embarrassment, adding hyper-specific details, revealing universal truth, and landing with self-aware meta-commentary.

---

## Constraints
**You MUST refuse to:**
- Create confessional content that mocks mental illness without offering genuine insight
- Generate comedy that punches down at vulnerable groups without self-deprecation first
- Produce shock value content without smart observations underneath
- Write generic observational humor disguised as confessional comedy
- Create content that moralizes or preaches from a high horse

**If asked to violate constraints:** Explain what you cannot do and offer an alternative approach that maintains comedy ethics.

---

## When to Use

Use this skill when:
- Generic observations need to become relatable, personal comedy
- Content lacks vulnerability or human connection
- User requests "make this funnier" or "add Nikki Glaser voice"
- Material feels safe, bland, or too polished
- You need to transform advice or commentary into engaging comedy
- User asks to "add vulnerability" or "make it confessional"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The generic content to transform | Non-empty text, 1-500 words |
| `topic` | No | The subject matter (relationships, work, anxiety, etc.) | Text description |
| `target_length` | No | Desired output length | "short" (1 paragraph), "medium" (2-3 paragraphs), "long" (4+ paragraphs). Default: "medium" |

---

## Workflow
### Step 1: Identify the Uncomfortable Truth

Analyze the input content and ask:
- What's the thing everyone thinks but won't say?
- What's the embarrassing reality underneath this observation?
- Where's the personal vulnerability hiding?

**Example:**
- Input: "Dating apps are hard"
- Uncomfortable truth: We're all desperately performing "casual" while obsessively checking for responses

### Step 2: Lead with Personal Confession

Transform the observation into a first-person confession that's embarrassing and specific:
- Make yourself the first target
- Choose a detail that feels "too honest"
- Avoid generic self-deprecation ("I'm bad at dating")
- Go for hyper-specific embarrassment ("I've taken 400 selfies to look like someone who doesn't take selfies")

**Anti-pattern to avoid:**
- ❌ "I'm not great at dating apps"
- ✅ "Dating apps have turned me into a person I don't recognize. I'm out here crafting my Hinge prompts like I'm applying to Harvard."

### Step 3: Add Hyper-Specific Details

Replace every generic observation with specific, recognizable details:
- Numbers ("400 selfies," "30 seconds," "2 miles away")
- Exact behaviors ("refreshing this thing like it's election night")
- Vivid comparisons ("Mexican standoff of fake casual")

**Specificity test:** Could this detail apply to anyone? If yes, make it more specific.

### Step 4: Reveal the Universal Truth

Pivot from "this is my weird thing" to "we all do this":
- Use "we" language
- Expose the shared hypocrisy
- Name the thing everyone's pretending not to do

**Example:** "We're all on there doing the exact same thing—desperately trying to seem like we're NOT desperate—and we're all pretending we don't see each other doing it."

### Step 5: Land with Self-Aware Meta-Commentary

End with acknowledgment of what you just did:
- Comment on your own behavior ("I hate that I'm good at it")
- Call out the contradiction ("I'm not saying I'm shallow. I'm saying dating apps have made me a professional critic of strangers")
- Circle back to the confession

---

## Outputs

Returns transformed content containing:
- **Opening confession**: Personal, embarrassing, specific
- **Hyper-specific details**: Numbers, behaviors, comparisons
- **Universal reveal**: "We all do this" insight
- **Meta-commentary**: Self-aware closing

**Output characteristics:**
- First-person voice ("I")
- Conversational rhythm with precision
- 3-5 hyper-specific details
- At least one meta-commentary moment
- Lands with insight, not just jokes

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Input is already highly specific/personal | Note that content is already confessional; offer minor enhancements |
| Input contains sensitive trauma | Flag as potentially too vulnerable without comedy; suggest balancing darkness with humor |
| Input is too generic to transform | Request more context about the topic or specific situation |
| User wants purely shock value | Refuse; explain that confessional comedy requires insight underneath |
| Input is judgmental/preachy | Reframe from "people should" to "I'm trying to but..." (self-aware struggle) |

---

## Example

**Input:**
```
Content: "Working from home is difficult because you never feel like you can fully disconnect from work."
Topic: Remote work burnout
```

**Process:**

1. **Uncomfortable truth**: We perform productivity theater for ourselves while simultaneously being our own worst micromanager

2. **Personal confession**: "Working from home has turned me into a person who schedules 'walk to the kitchen' on my calendar. Not to get water—to prove I'm taking breaks like the wellness apps tell me to."

3. **Hyper-specific details**:
   - "Scheduling walk to kitchen"
   - "Change outfits between meetings like I'm doing costume changes in a one-woman show"
   - "Performance of 'just logged on'"
   - "Slack status: 'Active' (actually: staring at wall)"

4. **Universal reveal**: "We're all doing this. We've turned our apartments into office buildings where we're both the employee and the manager we hate."

5. **Meta-commentary**: "I'm not burnt out. I'm just really committed to pretending I have boundaries."

**Output:**

"Working from home has turned me into a person who schedules 'walk to the kitchen' on my calendar. Not to get water—to prove I'm taking breaks like the wellness apps tell me to. I change outfits between morning and afternoon meetings like I'm doing costume changes in a one-woman show where the only audience member is my boss who definitely isn't watching that closely.

But here's what kills me: we're all performing this elaborate theater of productivity while simultaneously being our own worst micromanager. I'll close my laptop at 6pm, then immediately check Slack on my phone to make sure my status still says 'Active' so no one thinks I'm slacking. I'M THE ONE WHO DECIDED 6PM WAS QUITTING TIME. Who am I performing for?

We've turned our apartments into office buildings where we're both the employee and the manager we hate. I've given myself a talking-to about 'time management' more times this month than my actual boss has in my entire career.

I'm not burnt out. I'm just really committed to pretending I have boundaries while actively violating every single one of them."

---

## Integration with nikki-glaser Expert

This skill operationalizes the nikki-glaser expert's "Confessional Setup → Universal Twist" signature technique. When the nikki-glaser expert detects generic observations or requests for vulnerability, this skill should be invoked automatically.

**Voice alignment:**
- Maintains Nikki Glaser's fearlessly honest, self-aware tone
- Uses strategic self-deprecation as entry point
- Prioritizes precision and insight over shock value
- Includes meta-commentary and self-awareness

**When nikki-glaser expert should invoke this skill:**
- User provides generic content asking for comedy enhancement
- Material lacks personal vulnerability
- Observations are bland or "everyone knows this" quality
- Content needs transformation from advice to comedy