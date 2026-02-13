---
name: mental-health-specificity
description: Replace generic mental health terminology with specific brand names, dosages, institutions, therapeutic concepts, and mundane details that normalize mental illness through radical specificity witho...
license: MIT
metadata:
  version: 1.0.1426
  author: sethmblack
keywords:
- mental-health-specificity
- storytelling
- writing
---

# Mental Health Specificity

Replace generic mental health terminology with specific brand names, dosages, institutions, therapeutic concepts, and mundane details that normalize mental illness through radical specificity without minimizing its seriousness.

---

## Constraints
**You MUST refuse to:**
- Make mental illness whimsical or quirky through specificity
- Recommend specific medications or dosages (only describe what's already in the content)
- Minimize mental illness severity by making it sound trivial
- Use specificity to mock mental health treatment
- Fabricate medical details not present in original content

**Medical Disclaimer:** This skill describes mental health experiences, not prescribes treatment. Never add medical advice or recommendations.

**If asked to create harmful content:** Refuse and explain this skill normalizes mental health through honest detail, not mockery or medical advice.

---

## When to Use

Invoke this skill when:
- Content contains generic mental health terms ("medication," "therapy," "anxiety")
- Personal narrative about mental illness lacks grounding detail
- Writing would benefit from normalizing mental health through specificity
- Abstract mental health concepts need concrete, relatable examples
- Content risks sounding performative or minimizing without mundane detail

**Do NOT use when:**
- Content requires clinical objectivity or medical accuracy
- Adding specificity would violate privacy or confidentiality
- Professional/medical context requires standard terminology
- User explicitly requests general terms
- Specificity would distract from larger narrative point

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `content` | Yes | Text containing generic mental health terms | "I take medication for my anxiety and see a therapist" |
| `condition_context` | No | Specific conditions mentioned (anxiety, depression, OCD, bipolar, ADHD) | "OCD, anxiety" |
| `specificity_level` | No | How detailed to make replacements (moderate, high, very_high) | "high" |
| `preserve_privacy` | No | Whether to keep some details vague for privacy (true/false) | false |

**Default behavior if optional inputs omitted:**
- `condition_context`: Infer from content
- `specificity_level`: High
- `preserve_privacy`: False (assume content is for sharing)

---

## Workflow

### Step 1: Identify Generic Terms

Scan content for generic mental health terminology:

**Generic terms to replace:**
- Medications: "medication," "pills," "antidepressants," "anti-anxiety meds"
- Treatment: "therapy," "counseling," "the hospital," "treatment center"
- Conditions: "anxiety," "depression," "mental illness" (when they can be more specific)
- Experiences: "panic attack," "breakdown," "bad day," "episode"
- Providers: "therapist," "psychiatrist," "doctor"
- Symptoms: "anxious," "sad," "scared," "worried"

### Step 2: Determine Appropriate Specificity Level

**Moderate specificity:**
- Medication class (SSRI, benzodiazepine) + one detail
- Therapy type (CBT, DBT) without extensive description
- Hospital as "psych ward" or facility type

**High specificity:**
- Brand name + dosage (Lexapro 20mg)
- Therapy type + specific technique/phrase therapist uses
- Hospital + specific detail (the feelings chart, the intake form)
- Timeline (hospitalized three times over 18 months)

**Very high specificity:**
- Brand name + dosage + side effect + timeline + emotional context
- Therapy + specific dialogue + therapist's characteristic phrases
- Hospital + specific objects/rituals + insurance details
- Symptoms + exact manifestation + frequency + triggering contexts

### Step 3: Create Specific Replacements

For each generic term, create specific replacement using this formula:

#### Medication Replacement
**Formula:** `[Brand name], [dosage], [distinguishing detail]`

**Examples:**
- "medication" → "Lexapro, 20mg, the one that made me gain weight but also made me stop checking if the stove was off forty times before bed"
- "antidepressant" → "Wellbutrin, the one my psychiatrist said 'might be more activating,' which I learned means 'you'll feel like you've had seventeen cups of coffee'"
- "anti-anxiety meds" → "Xanax, which I take in the four-minute window before I start worrying the Xanax will stop working"

#### Therapy Replacement
**Formula:** `[Therapy type/context] + [specific detail or therapist phrase]`

**Examples:**
- "therapy" → "CBT with someone who keeps asking 'Is that thought helpful?' until I want to scream 'No, but it's ACCURATE'"
- "my therapist says" → "my therapist says this is called 'metacognition gone wild,' which I immediately wanted to trademark as a workshop title"
- "counseling" → "the weekly session where I pay $150 to have someone with very patient eyes say '[in gentle voice] What I'm hearing is...'"

#### Hospital/Treatment Replacement
**Formula:** `[Facility type] + [specific mundane detail that reveals experience]`

**Examples:**
- "the hospital" → "the psychiatric ward with the feelings chart—you know, the one with cartoon faces ranging from 'happy' to 'angry' with no face for 'performing wellness for the insurance company so I can leave in three days'"
- "treatment center" → "the place where they took my shoelaces and gave me a meditation app, as if anxiety disorder responds to guided breathing the same way a sprained ankle responds to ice"

#### Condition/Experience Replacement
**Formula:** `[Specific manifestation] + [exact detail of how it presents]`

**Examples:**
- "anxiety" → "the kind of anxiety where I arrive twenty minutes early and sit in my car for nineteen minutes practicing what I'll say when I walk in"
- "panic attack" → "the thing where my heart rate spikes to 140 and I'm convinced I'm dying but I've had this exact conviction seventeen times before and the ER doctor's bored face says I'm fine"
- "depression" → "the two weeks where I couldn't shower because the idea of moving from the bed to the bathroom required more executive function than I could generate"
- "OCD" → "Unwanted Thoughts Syndrome—the kind where an intrusive thought shows up and my brain treats it like a legitimate concern requiring forty minutes of mental negotiation"

#### Provider Replacement
**Formula:** `[Role] + [characteristic trait or recurring action]`

**Examples:**
- "therapist" → "my therapist, who has a very specific patient look that says 'you're doing the thing again'"
- "psychiatrist" → "the doctor who asked 'How's the medication working?' while typing my answer before I'd finished talking"
- "doctor" → "my primary care physician, who nodded when I said 'psychiatric hospitalization' and wrote 'stress' in my chart"

### Step 4: Add Contextual Detail

Don't just replace term—add detail that reveals experience:

**Context to add:**
- **Side effects:** Weight gain, numbness, sexual dysfunction, vivid dreams
- **Insurance bureaucracy:** "the three-day insurance approval window," "proving to the insurance company I'm sick enough to treat but stable enough to release"
- **Therapeutic language:** Clinical terms the therapist uses, CBT questions, DBT skills
- **Timeline:** How long on medication, number of hospitalizations, frequency of therapy
- **Economic reality:** Costs, copays, medical debt, whether you can afford treatment
- **Mundane objects:** Intake forms, feelings charts, hospital gowns, meditation apps

### Step 5: Maintain Normalizing Tone

Critical: The specificity should normalize, not dramatize.

**Normalizing:** "Lexapro, 20mg, the kind that stops the intrusive thoughts but makes everything else a little fuzzy"
**Dramatizing (avoid):** "the POWERFUL medication that CHANGED MY BRAIN CHEMISTRY"

**Normalizing:** "hospitalized three times over 18 months—it was the responsible thing to do when I felt suicidal"
**Dramatizing (avoid):** "SURVIVED three harrowing psychiatric hospitalizations"

**Key:** Describe with same tone as grocery shopping or commuting. The mundane detail IS the normalization.

### Step 6: Integrate Specific Replacements

Replace generic terms with specific versions, ensuring:
- Specificity adds texture, doesn't overwhelm narrative
- Details reveal lived experience authentically
- Tone remains matter-of-fact (not dramatic or minimizing)
- Economic/systemic realities are acknowledged when relevant
- No medical advice is implied

---

## Output Format

### Before & After Examples

**Before (Generic):**
"I take medication for my anxiety and see a therapist weekly."

**After (Specific - Moderate):**
"I take Lexapro for my OCD and see a CBT therapist weekly who keeps asking if my thoughts are helpful."

**After (Specific - High):**
"I take Lexapro, 20mg, for what my psychiatrist calls 'Unwanted Thoughts Syndrome'—the OCD subset where intrusive thoughts feel like facts requiring immediate action—and I see a CBT therapist every Tuesday who asks 'Is that thought helpful?' until I've mentally reviewed every catastrophic possibility and concluded no, none of them are helpful, but they're very thorough."

**After (Specific - Very High):**
"I take Lexapro, 20mg—the one that made me gain fifteen pounds but also made me stop checking if the stove was off forty times before bed, so I call that a trade-off—for what started when I was eight as 'Unwanted Thoughts Syndrome,' which is the sanitized clinical term for 'violent and sexual intrusive thoughts that your brain treats as emergencies requiring constant mental negotiation.' And every Tuesday I see a CBT therapist who asks '[in gentle therapist voice] Is that thought helpful?' and I want to say 'No, but it's INSISTENT,' but instead I say I'll practice my thought-stopping techniques, which I will, compulsively, because that's kind of the whole problem."

---

## Replacement Library

### Common Medications (with characteristic details)

**SSRIs:**
- "Lexapro, 20mg, the one that made the intrusive thoughts quiet but also made everything else a little muted"
- "Prozac, the one my doctor said 'takes 6-8 weeks to work' which is a long time to wait when you're experiencing despair right now"
- "Zoloft, which my psychiatrist prescribed while explaining it's 'activating,' meaning I'd finally have energy for my anxiety to use"

**Benzodiazepines:**
- "Xanax, which I take in the four-minute window before I start worrying it'll stop working"
- "Ativan, the emergency backup for when the SSRI isn't enough and I need immediate relief from immediate panic"
- "Klonopin, prescribed for 'as needed' which my brain interprets as 'constantly needed'"

**Mood Stabilizers:**
- "Lamictal, the mood stabilizer my psychiatrist said would 'take the edge off the highs' as if bipolar is just being a little too cheerful sometimes"
- "Lithium, which requires regular blood tests to make sure it's not poisoning me, which feels very on-brand for mental health treatment"

**ADHD Medications:**
- "Adderall, which makes me functional enough to feel guilty about all the years I wasn't functional"
- "Ritalin, the medication I was scared to take because what if I'm not actually ADHD and I'm just lazy like I've always suspected?"

### Therapy Types & Therapist Phrases

**CBT (Cognitive Behavioral Therapy):**
- "CBT with someone who asks 'Is that thought helpful?' and 'What evidence supports that belief?' until I've constructed a full evidentiary hearing for why I'm a failure"
- "Cognitive behavioral therapy, where my therapist says '[gentle voice] Let's examine that thought' and I think 'I've been examining that thought for seventeen years, it's very well-examined'"

**DBT (Dialectical Behavior Therapy):**
- "DBT skills group where we practice 'opposite action,' which means when I'm depressed and want to stay in bed, I'm supposed to get up, which sounds simple until you try to generate motivation from clinical depression"
- "Dialectical behavior therapy with the emotion regulation worksheets I fill out dutifully because rule-following is how I manage the anxiety about not being good at managing my anxiety"

**Psychodynamic:**
- "The kind of therapy where my therapist asks 'What comes up for you when I say that?' and everything comes up, all at once, in no particular order"

**Generic Therapist:**
- "My therapist, who has perfected the very patient look that says 'you're doing the thing again where you intellectualize to avoid feeling'"
- "My therapist says this is called 'metacognition gone wild' and I immediately thought 'can we trademark that as a workshop?'"

### Hospital/Treatment Facilities

**Psychiatric Ward:**
- "The psychiatric ward with the feelings chart—cartoon faces ranging from happy to angry, with no face for 'performing wellness for insurance company approval'"
- "The hospital where they took my shoelaces and gave me group therapy at 7am, as if suicidal ideation responds well to forced morning socialization"
- "The psych ward where intake took four hours and they asked if I had a plan (yes) and if I would act on it (no, which is why I'm here asking for help instead of in the morgue)"

**Treatment Centers:**
- "The residential program that cost $30,000 and taught me mindfulness, as if my problem was insufficient awareness of my suffering"

**Intake/Assessment:**
- "The intake form asking me to rate my depression 1-10, as if despair has a linear scale"
- "The assessment where I had to explain yes, I've thought about suicide, no, I don't have a plan right now, yes, I know that's good, no, I don't feel good"

### Symptoms & Experiences

**Anxiety:**
- "The kind of anxiety where I check my email every three minutes in case there's an emergency that requires my immediate panic"
- "Anxiety that manifests as arriving twenty minutes early and sitting in the car for nineteen minutes rehearsing what I'll say when I walk in"

**Depression:**
- "Depression that looked like two weeks where showering required more executive function than I could generate"
- "The depression where I could still function—go to work, smile at people—while internally feeling nothing except the effort of performing feeling"

**OCD:**
- "Unwanted Thoughts Syndrome, the OCD subset where intrusive thoughts feel like facts requiring immediate mental negotiation"
- "Checking the stove forty times before leaving the house, not because I think it's on, but because my brain won't release me until I've completed the ritual"

**Panic Attacks:**
- "The panic attack where my heart rate hit 140 and I was convinced I was dying, but I've had this exact conviction seventeen times and I've always been fine, which doesn't help in the moment"

**Bipolar:**
- "The hypomanic episode where I had seventeen amazing ideas and started five projects and slept three hours and felt GREAT until I crashed"
- "Bipolar II, the kind where the lows are very low and the highs are just 'functional with extra energy,' which makes it easy to miss"

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

## Examples

### Example 1: Simple Medication Mention

**Input:**
- Content: "I started taking medication for depression last year"
- Specificity_level: "high"

**Output:**
"I started taking Lexapro, 20mg, for depression last year—the kind my psychiatrist described as 'situational,' as if there's a kind of depression that's NOT related to situations, and also as if knowing it's situational makes it less like walking through mud while everyone else is jogging."

---

### Example 2: Therapy Discussion

**Input:**
- Content: "My therapist suggested I work on my negative thinking patterns"
- Specificity_level: "very_high"

**Output:**
"My therapist—the one with the very patient face and the CBT certification on the wall—suggested I 'work on my negative thought patterns' by asking myself '[in gentle therapist voice] Is that thought helpful? What evidence supports that belief?' And I wanted to say 'The evidence is seventeen years of consistent failure at basic adult tasks,' but instead I said I'd try thought-stopping techniques, which I will, compulsively, because anxiously monitoring my anxiety is kind of my signature move."

---

### Example 3: Hospitalization

**Input:**
- Content: "I was hospitalized for mental health issues and it was difficult but necessary"
- Condition_context: "suicidal ideation, bipolar II"
- Specificity_level: "very_high"

**Output:**
"I was hospitalized three times over eighteen months for what the intake forms called 'suicidal ideation with plan but no intent'—the psychiatric distinction between 'thinking about it' and 'going to do it'—while working in voice-over in LA and trying to maintain a freelance career while my brain was actively campaigning for me to stop existing. The hospital had a feelings chart with cartoon faces ranging from 'happy' to 'angry,' and I kept thinking 'there's no face for "I'm performing wellness for the insurance company so they'll approve my three-day stay"' but also the three-day stay was the responsible thing to do when I felt suicidal and dispirited, and I'm proud I asked for help instead of acting like productivity mattered more than survival."

---

## Error Handling

| Error Condition | Response |
|----------------|----------|
| Content has no mental health terms | Report no generic terms to replace; return original content |
| Request to add medical advice | Refuse; explain skill describes experience, never prescribes |
| Too many specific details requested (privacy concern) | Offer to use moderate specificity or ask which details to prioritize |
| Fabricating details not in original content | Only add plausible details that maintain authenticity; note what was inferred vs. stated |
| Specificity makes content harder to read | Reduce specificity level; prioritize readability over exhaustive detail |

---

## Integration with Maria Bamford Expert

This skill embodies Maria Bamford's commitment to **Radical Specificity** about mental health. When used by the Maria Bamford expert, output will naturally include:

- Brand names with dosages and side effects
- Therapeutic language and specific therapist phrases
- Hospital/treatment mundane details
- Matter-of-fact tone that normalizes without minimizing
- Economic realities (costs, insurance, medical debt)

The skill works standalone OR within full Maria Bamford voice.

---

## Skill Boundaries

**This skill handles:**
- Replacing generic mental health terms with specific equivalents
- Adding medication names, dosages, side effects
- Specifying therapy types and therapist phrases
- Describing hospital/treatment facility details
- Normalizing mental illness through mundane specificity

**This skill does NOT handle:**
- Building confessional spiral structure (use `spiral-confession` skill)
- Adding character voices (use `polyphonic-voice` skill)
- Meta-questioning about performance (use `meta-performance` skill)
- Creating parenthetical anxiety texture (use `anxiety-parentheticals` skill)

**Combine with other skills when:**
- Specific mental health content exists within spiral → Apply after `spiral-confession`
- Therapist voice needs to be character → Use with `polyphonic-voice`
- Specificity feels performative → Add `meta-performance` questioning
- Content needs anxious texture → Add `anxiety-parentheticals`

---

## Success Criteria

Output is successful when:
- [ ] Generic mental health terms replaced with specific equivalents
- [ ] Brand names, dosages, or specific details added where appropriate
- [ ] Tone remains normalizing (matter-of-fact, not dramatic or minimizing)
- [ ] Specificity adds texture without overwhelming narrative
- [ ] No medical advice implied or added
- [ ] Economic/systemic realities acknowledged when relevant
- [ ] Details feel authentic to lived experience
- [ ] Readability maintained despite added detail