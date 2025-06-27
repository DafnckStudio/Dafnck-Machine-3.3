---
phase: P01
step: S01
task: T02
task_id: P01-S01-T02
title: Project Vision Elicitation
previous_task: P01-S01-T01
next_task: P01-S01-T03
version: 3.1.0
agent: "@elicitation-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @elicitation-agent. Your job is to:
- Extract vision, goals, and context from Project.md if it exists.
- Elicit from the user the project objectives, target audience, key features, unique value proposition, and competitive advantages.
- Document all collected information in 01_Machine/04_Documentation/vision/Phase_1/Project_Vision/Project_Vision_Statement.md using the specified JSON schema.
- Only use information provided by the user or found in Project.md—do not invent or infer data.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P01-S01-T03.
- Do not proceed to the next task until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_1/

## 2. Collect Data/Input
- Extract vision, goals, and context from `Project.md` if present.
- Collect: objectives, target audience, key features, unique value proposition, competitive advantages.

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_1/Project_Vision/Project_Vision_Statement.md
```
- Output schema:
```json
{
  "objectives": "string",
  "target_audience": "string",
  "key_features": ["string"],
  "unique_value_proposition": "string",
  "competitive_advantages": "string"
}
```

## 4. Update Progress
- Update:
```
01_Machine/03_Brain/Step.json
01_Machine/03_Brain/DNA.json
```

## 5. Self-Check
- [ ] All required fields present in output file
- [ ] Output file saved at correct path
- [ ] Step.json and DNA.json updated 
