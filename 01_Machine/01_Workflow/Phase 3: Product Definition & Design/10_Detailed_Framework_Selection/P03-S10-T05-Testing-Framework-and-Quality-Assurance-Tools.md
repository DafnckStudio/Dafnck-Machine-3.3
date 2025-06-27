---
phase: P03
step: S10
task: T05
task_id: P03-S10-T05
title: Testing Framework and Quality Assurance Tools
agent: ["@technology-advisor-agent", "@system-architect-agent", "@performance-optimization-agent", "@development-orchestrator-agent", "@security-auditor-agent"]
previous_task: P03-S10-T04
next_task: P03-S10-T06
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@technology-advisor-agent (lead), with support from @system-architect-agent, @performance-optimization-agent, @development-orchestrator-agent, and @security-auditor-agent: Evaluate and select testing frameworks (unit, integration, e2e, performance) and quality assurance tools (linting, static analysis, code quality, security) for DafnckMachine v3.1. Document all findings, comparisons, and selection decisions with clear rationale and evidence. Output all analysis, comparison matrices, and specifications to the required files. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather system requirements, codebase characteristics, and QA needs from previous architecture and business analysis steps.
   - Collect team preferences and constraints regarding testing and QA tools.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Testing_Framework_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/QA_Tools_Comparison.json (JSON, schema: {"tools": [string], "criteria": [string], "scores": [[number]], "rationale": string})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Code_Quality_Tools_Selection.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Analysis_Tools_Specifications.json (JSON, schema: {"tool": string, "config": object, "patterns": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the testing and QA tool selection rationale clearly documented?
   - [ ] Are comparison matrices and specifications justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
