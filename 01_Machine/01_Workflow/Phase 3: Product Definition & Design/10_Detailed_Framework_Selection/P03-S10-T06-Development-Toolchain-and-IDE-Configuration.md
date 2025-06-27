---
phase: P03
step: S10
task: T06
task_id: P03-S10-T06
title: Development Toolchain and IDE Configuration
agent: ["@development-orchestrator-agent", "@system-architect-agent", "@performance-optimization-agent", "@technology-advisor-agent", "@security-auditor-agent"]
previous_task: P03-S10-T05
next_task: P03-S10-T07
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@development-orchestrator-agent (lead), with support from @system-architect-agent, @performance-optimization-agent, @technology-advisor-agent, and @security-auditor-agent: Select and configure the development toolchain, IDEs, build tools, and package management for DafnckMachine v3.1. Document all findings, configurations, and selection decisions with clear rationale and evidence. Output all specifications, configuration guides, and strategies to the required files. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/10_Detailed_Framework_Selection/`

2. **Collect Data/Input**
   - Gather team requirements, workflow needs, and environment constraints from previous steps and team input.
   - Collect preferences and constraints regarding IDEs, build tools, and package management.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Development_Toolchain_Specifications.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/IDE_Configuration_Guide.json (JSON, schema: {"ide": string, "extensions": [string], "settings": object, "shortcuts": [string]})
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Build_Tools_Selection.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/10_Detailed_Framework_Selection/Package_Management_Strategy.json (JSON, schema: {"manager": string, "strategy": string, "config": object})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the toolchain and configuration rationale clearly documented?
   - [ ] Are configuration guides and strategies justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
