---
phase: P04
step: S11
task: T03
task_id: P04-S11-T03
title: Task Complexity Analysis & Assessment
agent: ["@task-planning-agent"]
previous_task: P04-S11-T02
next_task: P04-S11-T04
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@task-planning-agent: Analyze the complexity of all tasks, generate a complexity report, and develop a strategy for expanding and breaking down complex tasks for DafnckMachine v3.1. Document all analysis, assessment, and expansion strategy with clear rationale and evidence. Output all reports and guides to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all tasks from tasks.json and supporting documentation.
   - Collect team input and constraints regarding task complexity and breakdown priorities.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Task_Complexity_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Complexity_Assessment_Report.json (JSON, schema: {"tasks": [string], "complexity_scores": [number], "recommendations": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Task_Expansion_Strategy.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Breakdown_Planning_Guide.json (JSON, schema: {"strategy": string, "steps": [string], "criteria": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the complexity analysis and expansion strategy rationale clearly documented?
   - [ ] Are assessment and planning guides justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
