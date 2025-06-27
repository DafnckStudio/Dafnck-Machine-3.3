---
phase: P03
step: S09
task: T04
task_id: P03-S09-T04
title: API Architecture and Integration Design
previous_task: P03-S09-T03
next_task: P03-S09-T05
version: 3.1.0
agent: "@system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @system-architect-agent. Your mission is to design the API architecture and integration plan for DafnckMachine v3.1. Ensure robust, secure, and scalable API and integration design, supporting all application and third-party communication needs. Document all specifications and rationale. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather all requirements for endpoints, authentication, service communication, and integration needs.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/API_Design_Specifications.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Endpoint_Documentation.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Integration_Architecture_Plan.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Service_Communication_Specs.json (JSON)
   - Output JSON schemas must include: { "endpoints": [ ... ], "integration": { ... }, "communication": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json 
