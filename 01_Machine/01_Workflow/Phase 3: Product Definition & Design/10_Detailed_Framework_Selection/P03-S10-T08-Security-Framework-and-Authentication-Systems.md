---
phase: P03
step: S10
task: T08
task_id: P03-S10-T08
title: Security Framework and Authentication Systems
agent: ["@security-auditor-agent", "@system-architect-agent", "@performance-optimization-agent", "@development-orchestrator-agent", "@technology-advisor-agent"]
previous_task: P03-S10-T07
next_task: P03-S10-T09
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@security-auditor-agent (lead), with support from @system-architect-agent, @performance-optimization-agent, @development-orchestrator-agent, and @technology-advisor-agent: Evaluate and select security frameworks, authentication systems, and compliance tools for DafnckMachine v3.1. Document all findings, comparisons, and selection decisions with clear rationale and evidence. Output all analysis, comparison matrices, and specifications to the required files. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather data protection, access control, and compliance requirements from previous steps and team input.
   - Collect preferences and constraints regarding security, authentication, and compliance tools.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Security_Framework_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Authentication_System_Comparison.json (JSON, schema: {"systems": [string], "criteria": [string], "scores": [[number]], "rationale": string})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Compliance_Framework_Selection.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Audit_Tools_Specifications.json (JSON, schema: {"tool": string, "config": object, "compliance": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the security and compliance rationale clearly documented?
   - [ ] Are comparison matrices and specifications justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
