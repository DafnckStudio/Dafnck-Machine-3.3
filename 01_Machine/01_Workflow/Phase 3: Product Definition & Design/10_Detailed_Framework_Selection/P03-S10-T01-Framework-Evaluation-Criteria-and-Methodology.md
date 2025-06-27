---
phase: P03
step: S10
task: T01
task_id: P03-S10-T01
title: Framework Evaluation Criteria and Methodology
agent: ["@technology-advisor-agent", "@system-architect-agent", "@development-orchestrator-agent", "@security-auditor-agent"]
next_task: P03-S10-T02
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@technology-advisor-agent (lead), with support from @system-architect-agent, @development-orchestrator-agent, and @security-auditor-agent: Define and document the criteria and methodology for evaluating and selecting technology frameworks for DafnckMachine v3.1. Ensure the process is systematic, justified, and aligned with all technical and business requirements. Output all criteria and methodology to the required files. Communicate any blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather architecture requirements and relevant technical/business needs from previous steps and team input.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Framework_Selection_Criteria.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Evaluation_Methodology.json (JSON, schema: {"criteria": [string], "weights": [number], "methodology": string})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Are the selection criteria comprehensive, weighted, and justified?
   - [ ] Is the evaluation methodology systematic and repeatable?
   - [ ] Have all requirements and blockers been communicated and addressed? 
