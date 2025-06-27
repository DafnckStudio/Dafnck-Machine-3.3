---
phase: P04
step: S11
task: T02
task_id: P04-S11-T02
title: PRD Analysis & Task Generation
agent: ["@prd-architect-agent", "@task-planning-agent"]
previous_task: P04-S11-T01
next_task: P04-S11-T03
version: 3.1.0
source: Step.json
---

# Super Prompt
@prd-architect-agent (lead), with support from @task-planning-agent: Synthesize all relevant documentation into a comprehensive PRD, then use TaskMaster to generate an actionable, prioritized task list for DafnckMachine v3.1. Document all analysis, extraction, and task structure with clear rationale and evidence. Output all reports, PRD, and task structure files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all requirements, features, and priorities from PRD and supporting documentation (especially Phase 0-3 folders).
   - Collect team input and constraints regarding task breakdown and prioritization.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/PRD_Analysis_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Requirements_Extraction.json (JSON, schema: {"requirements": [string], "features": [string], "priorities": [string]})
   - 01_Machine/04_Documentation/vision/Phase_3_Product_Definition_Design/DafnckMachine_PRD.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Initial_Task_Structure.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Task_Hierarchy_Design.json (JSON, schema: {"tasks": [string], "hierarchy": object, "dependencies": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the PRD analysis and task structure rationale clearly documented?
   - [ ] Are requirements, extraction, and hierarchy justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
