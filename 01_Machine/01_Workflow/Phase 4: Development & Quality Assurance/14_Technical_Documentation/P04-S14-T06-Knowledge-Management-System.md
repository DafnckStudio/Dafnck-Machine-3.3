---
phase: P04
step: S14
task: T06
task_id: P04-S14-T06
title: Knowledge Management System
agent:
  - "@documentation-agent"
  - "@system-architect-agent"
  - "@development-orchestrator-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S14-T05
next_task: P04-S14-T07
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @system-architect-agent, @development-orchestrator-agent, and @test-orchestrator-agent. Your mission is to collaboratively implement a knowledge management system (KMS) for DafnckMachine v3.1. Ensure all project knowledge and documentation is organized, accessible, and maintained. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference KMS requirements and project documentation needs
   - Review previous knowledge base structures and best practices if available
   - Gather standards for organization, access, and maintenance

3. **Save Output**
   - Save knowledge base structure: `Knowledge_Base_Structure.md`
   - Save KMS best practices: `KMS_Best_Practices.md`
   - Minimal JSON schema example for knowledge base structure:
     ```json
     {
       "section": "API Reference",
       "documents": ["API_Documentation.md", "OpenAPI_Specifications.json"],
       "access": "all"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T07

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Knowledge base is organized and accessible
   - [ ] Best practices are documented and shared
   - [ ] Task status updated in workflow tracking files 
