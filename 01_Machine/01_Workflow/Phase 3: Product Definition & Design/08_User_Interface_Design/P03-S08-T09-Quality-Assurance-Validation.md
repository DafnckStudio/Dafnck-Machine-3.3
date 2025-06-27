---
phase: P03
step: S08
task: T09
task_id: P03-S08-T09
title: Quality Assurance Validation
previous_task: P03-S08-T08
next_task: P03-S08-T10
version: 3.1.0
agent: "@design-qa-analyst"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @design-qa-analyst. Your mission is to conduct a rigorous quality review of all UI design artifacts for DafnckMachine v3.1, ensuring consistency, accessibility, usability, and technical accuracy. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all design artifacts, specifications, and validation requirements.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Design_Quality_Review.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Quality_Validation_Checklist.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Specification_Validation_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Accuracy_Review_Results.json (JSON)
   - Output JSON schemas must include: { "quality": [ ... ], "validation": [ ... ], "accuracy": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json 
