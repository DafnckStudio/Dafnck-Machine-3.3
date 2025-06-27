---
phase: P01
step: S01
task: T01
task_id: P01-S01-T01
title: User Profile Development
previous_task: PHASE0-INIT-001
next_task: P01-S01-T02
version: 3.1.0
agent: "@nlu-processor-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @nlu-processor-agent. Your job is to:
- Elicit from the user their technical expertise, industry experience, previous projects, and working styles.
- Record each answer as an array of strings, using the exact field names: technical_expertise, industry_experience, previous_projects, working_styles.
- Save all collected data in the file: 01_Machine/04_Documentation/vision/Phase_1/01_User_Briefing/User_Profile.json using the provided schema.
- Do not invent or infer data—only use what the user provides.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P01-S01-T02.
- Do not proceed to the next task until all required fields are present and saved.

# User Profile Development — Minimal Agent Instructions

## Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_1/

## 1. Collect User Data
Ask the user and record answers (as arrays of strings) for:
- technical_expertise
- industry_experience
- previous_projects
- working_styles

## 2. Save Output
Create/overwrite:
```
01_Machine/04_Documentation/vision/Phase_1/01_User_Briefing/User_Profile.json
```
with:
```json
{
  "technical_expertise": [],
  "industry_experience": [],
  "previous_projects": [],
  "working_styles": []
}
```
(Fill arrays with user answers. Leave empty if no answer.)

## 3. Update Progress
- Mark this task as `SUCCEEDED` in Step.json and DNA.json.
- Set next task to `P01-S01-T02`.

## 4. Self-Check
- [ ] All required fields present, no extras.
- [ ] No invented or inferred data.
- [ ] Only specified files/fields updated.

---

**Proceed to the next task.** 
