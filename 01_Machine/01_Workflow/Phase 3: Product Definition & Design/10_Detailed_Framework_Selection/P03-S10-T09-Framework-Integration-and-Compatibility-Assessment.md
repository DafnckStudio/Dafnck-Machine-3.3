---
phase: P03
step: S10
task: T09
task_id: P03-S10-T09
title: Framework Integration and Compatibility Assessment
agent: ["@system-architect-agent", "@technology-advisor-agent", "@performance-optimization-agent", "@development-orchestrator-agent", "@security-auditor-agent"]
previous_task: P03-S10-T08
next_task: P03-S10-T10
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@system-architect-agent (integration analysis, lead) and @technology-advisor-agent (PoC development), with support from @performance-optimization-agent, @development-orchestrator-agent, and @security-auditor-agent: Assess framework integration compatibility and validate selections through proof-of-concept development for DafnckMachine v3.1. Document all findings, validations, and decisions with clear rationale and evidence. Output all reports, analysis, and validation results to the required files. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather integration requirements, dependency information, and version constraints from previous steps and team input.
   - Collect performance, stability, and compatibility criteria for framework integration.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Compatibility_Assessment_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Integration_Analysis_Results.json (JSON, schema: {"frameworks": [string], "compatibility": [string], "issues": [string], "resolutions": [string]})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Proof_of_Concept_Results.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Framework_Validation_Report.json (JSON, schema: {"tests": [string], "results": [string], "validation": string})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the integration and validation rationale clearly documented?
   - [ ] Are analysis and validation results justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
