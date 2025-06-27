---
phase: P03
step: S10
task: T03
task_id: P03-S10-T03
title: Backend Framework Analysis and Selection
agent: ["@technology-advisor-agent", "@system-architect-agent", "@development-orchestrator-agent", "@security-auditor-agent"]
next_task: P03-S10-T04
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@technology-advisor-agent (lead), with support from @system-architect-agent, @development-orchestrator-agent, and @security-auditor-agent: Evaluate and select backend frameworks, API frameworks, and middleware for DafnckMachine v3.1. Document all findings, comparisons, and selection decisions with clear rationale and evidence. Output all results to the required files. Communicate any blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather requirements and technical needs for backend, API, and middleware from previous steps and team input.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Backend_Framework_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Backend_Comparison_Matrix.json (JSON, schema: {"frameworks": [string], "criteria": [string], "scores": [[number]]})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/API_Framework_Selection.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Middleware_Specifications.json (JSON, schema: {"middleware": [string], "features": [string], "compatibility": object})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Are the framework and middleware selections justified and documented?
   - [ ] Is the comparison matrix comprehensive and evidence-based?
   - [ ] Have all requirements and blockers been communicated and addressed? 
