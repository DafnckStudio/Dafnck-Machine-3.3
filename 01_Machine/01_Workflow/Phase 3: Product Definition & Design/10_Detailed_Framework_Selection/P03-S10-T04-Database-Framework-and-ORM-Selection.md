---
phase: P03
step: S10
task: T04
task_id: P03-S10-T04
title: Database Framework and ORM Selection
agent: ["@technology-advisor-agent", "@system-architect-agent", "@development-orchestrator-agent", "@security-auditor-agent"]
previous_task: P03-S10-T03
next_task: P03-S10-T05
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@technology-advisor-agent (lead), with support from @system-architect-agent, @development-orchestrator-agent, and @security-auditor-agent: Evaluate and select database technologies (SQL/NoSQL) and ORM frameworks for DafnckMachine v3.1. Document all findings, comparisons, and selection decisions with clear rationale and evidence. Output all analysis, comparison matrices, and specifications to the required files. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather system requirements, scalability needs, and data access patterns from previous architecture and business analysis steps.
   - Collect team preferences and constraints regarding database and ORM technologies.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Database_Technology_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Database_Comparison_Matrix.json (JSON, schema: {"databases": [string], "criteria": [string], "scores": [[number]], "rationale": string})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/ORM_Framework_Selection.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Data_Access_Specifications.json (JSON, schema: {"orm": string, "config": object, "patterns": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the database and ORM selection rationale clearly documented?
   - [ ] Are comparison matrices and specifications justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
