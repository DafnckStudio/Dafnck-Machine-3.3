---
phase: P02
step: S02
task: T03
task_id: P02-S02-T03
title: User Validation Research
previous_task: P02-S02-T02
next_task: P02-S02-T04
version: 3.1.0
agent: "@market-research-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent. Your job is to:
- Design a user research plan, including target segments, participant criteria, interview and survey questions, validation metrics, and data collection methods.
- Create an interview guide and survey questionnaire.
- Execute user interviews and surveys, collect pain point data, and validate problem significance and frequency with target users.
- Analyze research data and document findings in the required output files.
- Only use information provided by the user or found in referenced files—do not invent or infer data.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S02-T04.
- Do not proceed to the next task until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/02_Problem_Validation/`

## 2. Collect Data/Input
- Target segments, participant criteria, sample size
- Interview questions, survey questions, validation metrics, success criteria, data collection methods
- Interview responses, pain points, user insights, survey responses, quantitative data, statistical analysis, hypothesis validation, evidence summary, key findings

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/User_Research_Plan.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Interview_Guide.json
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/User_Validation_Report.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Interview_Transcripts.md
```
- Output schemas:
```json
// Interview_Guide.json
{
  "target_segments": ["string"],
  "participant_criteria": ["string"],
  "sample_size": "string",
  "interview_questions": ["string"],
  "survey_questions": ["string"],
  "validation_metrics": ["string"],
  "success_criteria": ["string"],
  "data_collection_methods": ["string"]
}
// User_Validation_Report.md
{
  "interview_responses": ["string"],
  "pain_points": ["string"],
  "user_insights": ["string"],
  "survey_responses": ["string"],
  "quantitative_data": ["string"],
  "statistical_analysis": ["string"],
  "hypothesis_validation": ["string"],
  "evidence_summary": ["string"],
  "key_findings": ["string"]
}
```

## 4. Update Progress
- Update:
```
01_Machine/03_Brain/Step.json
01_Machine/03_Brain/DNA.json
```

## 5. Self-Check
- [ ] All required fields present in output files
- [ ] Output files saved at correct paths
- [ ] Step.json and DNA.json updated 
