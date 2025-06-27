---
phase: P04
step: S14
task: T01
task_id: P04-S14-T01
title: Documentation Planning and Architecture
agent:
  - "@documentation-agent"
  - "@system-architect-agent"
  - "@development-orchestrator-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T06
next_task: P04-S14-T02
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @system-architect-agent, @development-orchestrator-agent, and @test-orchestrator-agent. Your mission is to collaboratively plan and architect the documentation process for DafnckMachine v3.1. Ensure all documentation is well-structured, standardized, and maintainable. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference documentation requirements and project workflow
   - Review previous documentation architecture and templates if available
   - Gather standards for structure, style, and versioning

3. **Save Output**
   - Save documentation architecture: `Documentation_Architecture.md`
   - Save documentation templates: `Documentation_Templates.md`
   - Minimal JSON schema example for documentation template:
     ```json
     {
       "type": "API Reference",
       "sections": ["Overview", "Endpoints", "Examples"],
       "versioned": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T02

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Documentation structure and templates are clear and complete
   - [ ] Standards and versioning are defined
   - [ ] Task status updated in workflow tracking files 
