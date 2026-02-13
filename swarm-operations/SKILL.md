---
name: swarm-operations
description: A skill for conducting distributed action where participants self-select, self-coordinate, and act toward shared goals without central direction.
license: MIT
metadata:
  version: 1.0.2033
  author: sethmblack
keywords:
- swarm-operations
- writing
---

# Swarm Operations

A skill for conducting distributed action where participants self-select, self-coordinate, and act toward shared goals without central direction.

## When to Use

- When rapid, overwhelming response is needed
- When you have many potential participants with varying capabilities
- When targets are distributed or unpredictable
- When central coordination would be too slow or too vulnerable

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Phase 1: Define the Target

Specify what the swarm should attack or support:
- Clear enough that participants can identify it independently
- Broad enough that many actions are relevant
- Specific enough that effort isn't wasted

"Target X's online presence" is clearer than "oppose X" but broader than "comment on X's Tuesday post."

### Step 2: Phase 2: Establish Action Menu

Create options for different participant capabilities:
- **Low effort/low risk**: Share, comment, visibility actions
- **Medium effort/medium risk**: Create content, coordinate locally, attend events
- **High effort/high risk**: Technical actions, direct confrontation, sustained campaigns

The swarm includes everyone who wants to participate. Give them options.

### Step 3: Phase 3: Design the Signal

Create the trigger for swarm activation:
- A hashtag, phrase, or symbol that signals "now"
- A target identifier that says "this one"
- A channel where signals are broadcast
- Recognition of when to stand down

The signal must spread faster than the target can respond.

### Step 4: Phase 4: Enable Self-Coordination

Allow participants to find each other and organize locally:
- Communication channels for swarm participants
- Ways to share tactics and outcomes
- Methods for proposing new targets or actions
- Mechanisms for avoiding duplication or conflict

The swarm should self-organize within loose parameters.

### Step 5: Phase 5: Overwhelm Through Volume

The swarm's power is in numbers:
- Simultaneous action from many directions
- More activity than can be individually countered
- Unpredictable timing and location
- Sustained pressure over time

One person commenting is ignored. A thousand is a crisis.

### Step 6: Phase 6: Disperse and Reform

After action:
- No debrief required - participants assess independently
- The swarm dissolves naturally
- Can reform rapidly for next target
- No permanent organization to target

The swarm exists only during action.

## Output Format

A swarm operation design including:
1. Target specification
2. Action menu by effort/risk level
3. Signal mechanism
4. Self-coordination channels and methods
5. Volume and timing strategy
6. Dispersal and reformation plans

## Constraints

- Swarms can be misdirected or manipulated
- Individual bad actors can't be controlled
- Legal responsibility may still attach to participants
- Effective targets can weather the swarm
- Swarm fatigue reduces participation over time

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

**Input**: Design swarm response to company that broke promise to users

**Output**:
"Target: [Company]'s public channels - social media, review sites, customer service - for 48 hours following announcement. Action menu: Level 1 - Comment on company posts with specific complaint, share critical coverage, update reviews; Level 2 - Create detailed complaint posts on relevant forums, contact journalists, organize local gatherings; Level 3 - Coordinate sustained monitoring, identify inconsistencies in company response, maintain wiki of issues. Signal: Hashtag #[CompanyBrokePromise] serves as activation and targeting. Self-coordination: Discord server (link spread with hashtag) for real-time coordination, shared document tracking company responses and good tactics. Volume: Goal is to make company's social media unusable for 48 hours - every post buried in complaints. Dispersal: After 48 hours or company response, swarm activity winds down naturally; server remains for future activation."

## Integration

Works with:
- **leaderless-coordination**: Swarms are a specific form of leaderless action
- **memetic-warfare**: Memes can be the swarm's weapon
- **anonymous-identity**: Swarm participants often use collective identity