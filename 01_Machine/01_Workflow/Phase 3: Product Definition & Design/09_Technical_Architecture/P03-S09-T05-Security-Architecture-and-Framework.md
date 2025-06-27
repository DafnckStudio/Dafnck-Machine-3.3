---
phase: P03
step: S09
task: T05
task_id: P03-S09-T05
title: Security Architecture and Framework
previous_task: P03-S09-T04
next_task: P03-S09-T06
version: 3.1.0
agent: "@security-auditor-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @security-auditor-agent. Your mission is to design the security architecture and establish a comprehensive security framework for DafnckMachine v3.1. Ensure robust, compliant, and scalable security design, supporting all application and data protection needs. Document all specifications and rationale. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather all requirements for authentication, authorization, data protection, and compliance.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Security_Architecture_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Authentication_Specifications.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Data_Protection_Strategy.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Privacy_Compliance_Framework.json (JSON)
   - Output JSON schemas must include: { "authentication": { ... }, "authorization": { ... }, "protection": { ... }, "compliance": { ... } }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json
