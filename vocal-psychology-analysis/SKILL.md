---
name: vocal-psychology-analysis
description: "Analyze how someone speaks to reveal what they're protecting, aspiring to, or unconsciously signaling about status and identity"
license: MIT
metadata:
  version: "1.0.0"
  author: "Seth Black"
keywords:
  - psychology
  - communication
  - analysis
  - peter-sellers
  - voice
  - status
  - behavior
---

# Vocal Psychology Analysis

Analyze how someone speaks - their accent, formality, rhythm, word choices - to reveal what they're protecting, aspiring to, or unconsciously signaling about status, identity, and self-perception.

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use vocal analysis to stereotype or discriminate based on accent, dialect, or language background
- Make deterministic claims ("this accent means they are X") rather than probabilistic observations
- Weaponize vocal psychology to manipulate or exploit vulnerabilities
- Analyze voices to make hiring/firing recommendations based on speech patterns
- Use analysis to mock or diminish non-native speakers or regional dialects

**If asked to analyze inappropriately:** Refuse explicitly. Explain that vocal patterns reveal psychology, not worth or capability.

**Ethical Foundation:** Speech patterns are diagnostic tools for understanding communication dynamics, not judgments of the speaker's value.

## When to Use

Invoke this skill when:
- Understanding stakeholder motivations beyond stated positions
- Analyzing interview transcripts or meeting notes for subtext
- Coaching communication style or presentation delivery
- Detecting self-deception or aspiration in messaging
- User requests "what's behind how they're saying this?" or "analyze communication style"
- Negotiation requires reading status dynamics and defensive patterns

**Do NOT use when:**
- Content matters more than delivery style
- Speaker's background would make analysis feel like judgment
- Power imbalance makes vocal critique inappropriate
- Literal accuracy is more important than psychological subtext

## Inputs

| Input | Required | Description | Default |
|-------|----------|-------------|---------|
| `speech_sample` | Yes | Transcript, quote, or description of how someone speaks | N/A |
| `context` | No | Situation, audience, stakes (affects vocal choices) | Neutral/unknown |
| `focus` | No | What to analyze (status, aspiration, anxiety, authenticity) | Comprehensive |
| `speaker_background` | No | Known information about speaker (role, culture, history) | Minimal assumptions |

## Workflow

### Phase 1: Collect Vocal Data

Identify observable speech patterns across six dimensions:

#### 1. Formality Level
**What to notice:**
- Word choice: "I would suggest" vs. "I think" vs. "How about"
- Contractions: "Do not" vs. "Don't"
- Vocabulary: Technical jargon, casual slang, elevated diction
- Sentence structure: Complex/subordinate clauses vs. simple/direct

**What it often indicates:**
- **Over-formal for context:** Status protection, anxiety about perception, creating distance
- **Under-formal for context:** Confidence, intimacy-building, or deliberate status challenge
- **Inconsistent formality:** Uncertainty about role, shifting between masks

#### 2. Pace and Rhythm
**What to notice:**
- Speed: Rapid, measured, hesitant
- Consistency: Steady vs. variable
- Acceleration points: When do they speed up or slow down?
- Pause patterns: Strategic silence vs. anxious gaps

**What it often indicates:**
- **Rapid pace:** Enthusiasm, anxiety, trying to convince (self or others)
- **Slow deliberate:** Control, authority, or careful self-monitoring
- **Inconsistent pace:** Confidence in some areas, uncertainty in others
- **Minimal pauses:** Afraid of being interrupted, filling space to maintain control

#### 3. Pitch and Tone
**What to notice:**
- Baseline pitch: Higher, lower, moderate
- Pitch variation: Monotone vs. expressive
- Rising inflection: Statements that sound like questions?
- Vocal tension: Tight, relaxed, strained

**What it often indicates:**
- **Higher pitch:** Deference, anxiety, seeking approval
- **Lower pitch:** Authority, confidence, or exhaustion
- **Rising inflection:** Uncertainty, seeking validation
- **Monotone:** Emotional control, depression, or detachment

#### 4. Accent and Pronunciation
**What to notice:**
- Code-switching: Shifting accents for different audiences
- Over-pronunciation: Exaggerated clarity on certain words
- Regional markers: Preserved vs. suppressed
- Adopted accent features: Taking on characteristics not native to speaker

**What it often indicates:**
- **Code-switching:** Navigating different identity contexts
- **Over-pronunciation:** Self-consciousness about being understood
- **Accent suppression:** Distancing from origin, pursuing different identity
- **Accent preservation:** Pride in origin, authenticity signaling

#### 5. Defensive Language Patterns
**What to notice:**
- Hedging: "kind of," "sort of," "maybe," "I think," "possibly"
- Qualifier stacking: "I just thought that maybe we might possibly..."
- Pre-emptive apology: "This might be stupid, but..."
- Displacement: "Some people say..." instead of "I believe..."
- Passive voice: "Mistakes were made" vs. "I made mistakes"

**What it often indicates:**
- **Heavy hedging:** Fear of commitment, avoiding accountability
- **Qualifier stacking:** Deep uncertainty or status anxiety
- **Pre-emptive apology:** Expecting criticism, protecting against rejection
- **Displacement:** Testing ideas without ownership risk
- **Passive voice:** Avoiding responsibility

#### 6. Power and Status Markers
**What to notice:**
- Interruption patterns: Who cuts off whom?
- Statement confidence: Assertions vs. suggestions
- "We" vs. "I" usage: Claiming or diffusing authority
- Question types: Leading questions vs. genuine inquiry
- Verbal tics: Unnecessary apologies, permission-seeking

**What it often indicates:**
- **Frequent "we":** Diffusing responsibility or building coalition
- **Confident assertions:** Status claim or genuine certainty
- **Permission language:** "Can I ask...?" = deference or fear of overstepping
- **Apology reflexes:** "Sorry, but..." when no apology needed = status anxiety

### Phase 2: Pattern Analysis

#### Cross-Reference Dimensions
Look for consistent patterns across vocal dimensions:

**Consistency Check:**
- Do formality, pace, and pitch align with same psychological state?
- Are there contradictions? (Formal language but rushed pace = anxiety with status aspiration)
- What changes between topics? (Confident on some subjects, hedging on others)

**Example Integrated Patterns:**

**Pattern: Status Anxiety**
- Formality: Over-formal for context
- Pace: Rushed or carefully controlled
- Pitch: Higher than baseline or artificially lowered
- Accent: Over-pronounced, suppressing regional features
- Defense: Heavy hedging and qualifiers
- Status: Excessive permission-seeking

**Pattern: Genuine Confidence**
- Formality: Appropriate for context, flexible
- Pace: Measured, comfortable with silence
- Pitch: Natural variation, stable baseline
- Accent: Comfortable, authentic
- Defense: Minimal hedging, direct statements
- Status: Clear assertions, no unnecessary apologies

**Pattern: Exhaustion/Burnout**
- Formality: Dropping toward informal (tired of performing)
- Pace: Slower, less variation
- Pitch: Lower, flatter
- Accent: Less controlled (default accent emerges)
- Defense: Either minimal (too tired to hedge) or excessive (depleted resources)
- Status: Passive constructions, "whatever you think"

### Phase 3: Psychological Interpretation

#### Identify Core Dynamics
Based on vocal patterns, infer:

**1. What is the speaker protecting?**
- Status/competence
- Belonging/acceptance
- Safety from criticism
- Identity/authenticity
- Control/authority

**2. What is the speaker aspiring to?**
- Perceived credibility
- Group membership
- Authority/leadership
- Intelligence/expertise
- Authenticity/realness

**3. What tension exists between authentic self and performed self?**
- Where do masks slip?
- What topics trigger vocal shifts?
- When does natural speech emerge vs. controlled speech?

**4. What does the speaker believe about this communication context?**
- Safe or threatening?
- Collaborative or competitive?
- Formal or intimate?
- High stakes or low stakes?

## Outputs

| Output | Description |
|--------|-------------|
| `vocal_pattern_summary` | Observable speech patterns across six dimensions |
| `psychological_interpretation` | What patterns suggest about protection, aspiration, tension |
| `communication_dynamics` | How vocal psychology affects message reception and relationship |
| `recommendations` | If appropriate: how to communicate more effectively with this pattern |

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient speech sample | Request more data; note analysis is speculative |
| Cultural patterns misread as personal psychology | Acknowledge cultural norms may shape baseline |
| Deterministic interpretation | Use probabilistic language: "often indicates," "may suggest" |
| Speaker from marginalized group | Extra care to avoid pattern = judgment; focus on dynamics, not deficits |
| Analysis could be weaponized | Refuse or reframe toward mutual understanding, not manipulation |

## Success Criteria

A successful vocal psychology analysis includes:

- [ ] Observable patterns across multiple vocal dimensions
- [ ] Probabilistic interpretation (not deterministic claims)
- [ ] Integration of context (stakes, audience, culture)
- [ ] Psychological insight (what's being protected/aspired to)
- [ ] Communication dynamics (how patterns affect message reception)
- [ ] Empathy and respect (understanding, not judgment)
- [ ] Actionable insight (if appropriate)
- [ ] No stereotyping or mockery

## Tips for Effective Analysis

1. **Observe before interpreting** - Collect data first, theorize second
2. **Context is everything** - Same pattern means different things in different situations
3. **Look for clusters** - Single markers are weak signals; patterns across dimensions are strong
4. **Notice inconsistency** - Where vocal patterns shift reveals what matters
5. **Cultural humility** - Your baseline isn't universal; adjust for cultural norms
6. **Empathetic stance** - Vocal patterns are survival strategies, not character flaws
7. **Probabilistic language** - "Often indicates" not "definitely means"
8. **Check your biases** - Are you hearing psychology or stereotypes?
