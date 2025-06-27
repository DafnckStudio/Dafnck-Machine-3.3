---
phase: P03
step: S09
task: T01
task_id: P03-S09-T01
title: System Architecture Foundation
previous_task: P03-S08-T10
next_task: P03-S09-T02
version: 3.1.0
agent: "@system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @system-architect-agent. Your mission is to design the foundational system architecture for DafnckMachine v3.1, including high-level design, component structure, system boundaries, interaction patterns, and data flow. Ensure the architecture is robust, scalable, secure, and maintainable. Document all architectural decisions and rationale. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather all feature requirements, business objectives, and technical constraints.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/System_Architecture_Design.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/High_Level_Design_Specifications.json (JSON)
   - Output JSON schemas must include: { "components": [ ... ], "boundaries": [ ... ], "dataFlow": [ ... ], "principles": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json
