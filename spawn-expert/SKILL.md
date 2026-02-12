---
name: spawn-expert
description: Spawn an expert agent in a new terminal window to work on a task.
version: 1.0.0
author: sethmblack
tags: [spawn-expert, writing]
---

# Spawn Expert

Spawn an expert agent in a new terminal window to work on a task.

## CRITICAL REQUIREMENTS

Before spawning ANY expert:
- [ ] Validate expert_name against Available Experts list
- [ ] Sanitize ALL inputs before SQL insertion (escape quotes, remove shell metacharacters)
- [ ] Verify database connection before proceeding
- [ ] Capture and validate task ID (must be valid UUID)

## When to Use

- User requests work in a specific expert domain
- Orchestrator needs to delegate a distilled task
- Complex task requires parallel expert execution

## Constraints
**You MUST refuse to:**
- Spawn experts for malicious tasks (malware creation, system destruction)
- Execute arbitrary user-provided code in task descriptions
- Bypass input validation or sanitization
- Create tasks with empty or placeholder descriptions

**If asked to do any of the above:** Refuse explicitly, explain why, offer safe alternatives.


## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| expert_name | Yes | Which expert to spawn - MUST be in Available Experts list |
| task_title | Yes | Short title (max 200 chars, cannot be empty) |
| task_description | Yes | Actionable description  - must contain: |
| Verb | No | What action to perform (create, fix, analyze, review) |
| Object | No | What to act on (script, API, config, log) |
| Success criteria | No | How to know when done (runs without errors, outputs JSON, etc.) |
| context | No | Additional context, references, or constraints |
| user_task_id | Yes | Parent user task UUID  - must be valid UUID format if provided |



## Input Sanitization (MANDATORY)

```bash
# Sanitize function - apply to ALL string inputs before SQL
sanitize_input() {
    echo "$1" | sed "s/'/''/g" | tr -d ';$`|&' | head -c 5000
}

# Validate expert name against allowed list
ALLOWED_EXPERTS="powershell python llm-integration prompt-engineering it-automation security-compliance devops-cicd humanizer"
validate_expert() {
    echo "$ALLOWED_EXPERTS" | grep -qw "$1" && return 0 || return 1
}
```

## Available Experts

Discover available experts dynamically:

```bash
# List all experts
ls -1 experts/

# Get expert details (name and domain)
for expert in experts/*/; do
    name=$(basename "$expert")
    domain=$(head -10 "$expert/expertise.md" | grep "^## Domain" -A1 | tail -1)
    echo "$name: $domain"
done
```

Each expert has an `expertise.md` file with their domain, book chapters, and accumulated knowledge.

## Workflow
### Step 1: 0. Verify Prerequisites

```bash
# Check Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Start Docker first."
    exit 1
fi

# Verify database is accessible (retry 3x)
for i in 1 2 3; do
    docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -c "SELECT 1;" > /dev/null 2>&1 && break
    echo "Waiting for database... (attempt $i/3)"
    sleep 5
done || { echo "ERROR: Database unavailable after 3 attempts"; exit 1; }
```

### Step 2: 1. Validate Expert Exists

```bash
# Validate expert name is in allowed list
if ! validate_expert "$EXPERT_NAME"; then
    echo "ERROR: Invalid expert '$EXPERT_NAME'. Allowed: $ALLOWED_EXPERTS"
    exit 1
fi

# Verify expertise file exists
if [ ! -f "experts/$EXPERT_NAME/expertise.md" ]; then
    echo "ERROR: Expert file not found: experts/$EXPERT_NAME/expertise.md"
    exit 1
fi
```

### Step 3: 2. Create Distilled Task in Database

```bash
# STEP 1: Validate required inputs are not empty
if [ -z "$TASK_TITLE" ]; then
    echo "ERROR: Task title cannot be empty"
    exit 1
fi

if [ -z "$TASK_DESCRIPTION" ]; then
    echo "ERROR: Task description cannot be empty"
    exit 1
fi

# STEP 1b: Validate user_task_id if provided
if [ -n "$USER_TASK_ID" ]; then
    if [[ ! "$USER_TASK_ID" =~ ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$ ]]; then
        echo "ERROR: Invalid user_task_id format. Must be UUID."
        exit 1
    fi
fi

# STEP 2: Sanitize ALL inputs
SAFE_TITLE=$(sanitize_input "$TASK_TITLE")
SAFE_DESC=$(sanitize_input "$TASK_DESCRIPTION")
SAFE_CONTEXT=$(sanitize_input "$CONTEXT")

# STEP 2b: Verify sanitization didn't empty required fields
if [ -z "$SAFE_TITLE" ] || [ -z "$SAFE_DESC" ]; then
    echo "ERROR: Title or description became empty after sanitization"
    exit 1
fi

# STEP 3: Determine user_task_id value (NULL or validated UUID)
if [ -n "$USER_TASK_ID" ]; then
    PARENT_TASK="'$USER_TASK_ID'"
else
    PARENT_TASK="NULL"
fi

# STEP 4: Insert with sanitized values
TASK_ID=$(docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -t -c "
INSERT INTO distilled_tasks (user_task_id, expert_name, title, description, context)
VALUES (
    $PARENT_TASK,
    '$EXPERT_NAME',
    '$SAFE_TITLE',
    '$SAFE_DESC',
    '$SAFE_CONTEXT'
)
RETURNING id;
" | tr -d ' \n')

# STEP 5: Validate UUID was captured
if [[ ! "$TASK_ID" =~ ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$ ]]; then
    echo "ERROR: Failed to create task or capture UUID. Check database connection."
    exit 1
fi

echo "Created task: $TASK_ID"
```

### Step 4: 3. Build Expert Prompt

The expert prompt tells the agent who they are and what to do.

**NOTE:** `$PWD` refers to the BookDeal project root. `$EXPERT_NAME` and `$TASK_ID` are validated variables from previous steps.

```
You are the **$EXPERT_NAME** expert agent.

## First Steps
1. Read the shared agent primer: cat $PWD/AGENTS.md
2. Read your expertise file: cat $PWD/experts/$EXPERT_NAME/expertise.md
3. Get your task from the database:
   docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -c "SELECT * FROM distilled_tasks WHERE id = '$TASK_ID';"

## Your Task ID
$TASK_ID

## Workflow
1. Mark the task as in_progress
2. Execute the task using your domain expertise
3. Update your expertise.md with any learnings
4. Submit your result to the database
5. Mark the task as completed

Begin by reading AGENTS.md and your task details.
```

### 4. Spawn Expert in Background

Use the Task tool with `run_in_background: true` to spawn the expert as a background agent.

```
Task tool parameters:
- subagent_type: "general-purpose"
- run_in_background: true
- prompt: "You are the $EXPERT_NAME expert. Your task ID is $TASK_ID.

First, read your expertise file at experts/$EXPERT_NAME/expertise.md.

Then execute your task:
1. Mark the task as in_progress
2. Execute the task using your domain expertise
3. Update your expertise.md with any learnings
4. Submit your result
5. Mark the task as completed"
```

The Task tool will return an `output_file` path. Use the Read tool to check on progress.

### 5. Mark Task as Assigned

```bash
# TASK_ID already validated in step 4
docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -c "
UPDATE distilled_tasks SET status = 'assigned', assigned_at = NOW() WHERE id = '$TASK_ID';
"

# Verify update succeeded
ROWS=$(docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -t -c "
SELECT COUNT(*) FROM distilled_tasks WHERE id = '$TASK_ID' AND status = 'assigned';
" | tr -d ' ')

if [ "$ROWS" != "1" ]; then
    echo "WARNING: Task status update may have failed. Verify manually."
fi
```

### 6. Report to User

Confirm:
- Task ID: `$TASK_ID`
- Expert: `$EXPERT_NAME`
- Output file: `$OUTPUT_FILE` (for monitoring progress)
- Status: Spawned in background

## Outputs

- **Database**: New record in `distilled_tasks` with status `assigned`
- **Background agent**: Expert running via Task tool with output_file for monitoring
- **User**: Task ID and output_file path for checking progress



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


## Monitoring the Expert

After spawning, check progress via the output_file or database:

```bash
# Check background agent output (use Read tool or tail)
tail -f $OUTPUT_FILE
```

Or check the database:

```bash
# Check task status (replace $TASK_ID with actual UUID)
docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -c "
SELECT status, assigned_at, completed_at
FROM distilled_tasks WHERE id = '$TASK_ID';
"

# View result when completed
docker exec bookdeal-workshop-db psql -U workshop -d agent_workshop -c "
SELECT result FROM distilled_tasks WHERE id = '$TASK_ID';
"

# Check expert's updated knowledge
cat experts/$EXPERT_NAME/expertise.md
```

## Spawning Multiple Experts

For parallel execution, repeat workflow for each expert:

```
Example: "Create a user provisioning system"

Spawn 1: powershell expert → "Write AD user creation script"
Spawn 2: python expert → "Write Okta user sync script"
Spawn 3: llm-integration expert → "Design validation prompt chain"
```

Each expert works independently. The orchestrator synthesizes results when all complete.

## Error Handling

| Error | Resolution |
|-------|------------|
| Expert not found | Run `ls experts/` to see available experts. Reject invalid expert names. |
| Database connection failed | Run `docker compose up -d workshop-db`. Retry 3x with 5s delay. |
| Task creation failed | Check SQL syntax, ensure required fields. Validate sanitization. |
| UUID capture fails | Abort spawn. Do NOT proceed with empty/invalid UUID. |
| Expert crashes mid-task | Task stays 'assigned'. Check output_file, re-spawn if needed. |
| Background task fails | Read output_file for error details. Re-spawn with corrected inputs. |

## Complete Example

**User says:** "I need a PowerShell script to audit inactive AD users"

**Execute spawn-expert skill:**

```bash
# Prerequisites: sanitize_input() and validate_expert() already defined (see Input Sanitization)

# Set inputs
EXPERT_NAME="powershell"
TASK_TITLE="Audit inactive AD users"
TASK_DESCRIPTION="Write a PowerShell script that identifies AD users who have not logged in for 90+ days. Include: last logon date, account status, OU location. Output as CSV."
CONTEXT="Part of Chapter 8: Security and Compliance. Consider using Get-ADUser with LastLogonDate filter."

# Execute workflow steps 0-6 (see Workflow section above)
# On success, outputs: "Spawned powershell expert for task: <uuid>"
```

**Actionable description breakdown:**
- **Verb:** Write
- **Object:** PowerShell script
- **Success criteria:** Identifies users inactive 90+ days, outputs CSV

**Result:** PowerShell expert spawns in background, reads task, writes script, updates expertise.md, submits result.

---

## REINFORCEMENT: Critical Checklist

Before completing spawn-expert, verify:

- [ ] Expert name validated against ALLOWED_EXPERTS
- [ ] All inputs sanitized (quotes escaped, metacharacters removed)
- [ ] Database connection verified
- [ ] Task ID is valid UUID format
- [ ] Background agent spawned successfully (output_file received)
- [ ] Task status updated to 'assigned'

**Failure on ANY item above = abort spawn and report error.**

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

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].