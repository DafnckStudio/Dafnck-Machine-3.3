---
phase: P03
step: S09
task: T08
task_id: P03-S09-T08
title: Development Standards and Guidelines
previous_task: P03-S09-T07
next_task: P03-S09-T09
version: 3.1.0
agent: "@system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @system-architect-agent. Your mission is to establish development standards and guidelines for DafnckMachine v3.1. Ensure consistent code quality, readability, maintainability, and reliable testing practices across the development team and codebase. Document all specifications and rationale. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather all requirements for coding standards, best practices, and testing frameworks.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Coding_Standards_Guidelines.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Development_Best_Practices.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Testing_Framework_Design.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/QA_Standards_Specifications.json (JSON)
   - Output JSON schemas must include: { "standards": { ... }, "practices": [ ... ], "testing": { ... }, "qa": { ... } }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json
