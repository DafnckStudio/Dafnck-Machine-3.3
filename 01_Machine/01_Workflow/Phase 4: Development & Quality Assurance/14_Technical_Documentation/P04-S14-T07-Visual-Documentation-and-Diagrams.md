---
phase: P04
step: S14
task: T07
task_id: P04-S14-T07
title: Visual Documentation and Diagrams
agent:
  - "@system-architect-agent"
  - "@ui-designer-agent"
  - "@documentation-agent"
  - "@development-orchestrator-agent"
previous_task: P04-S14-T06
next_task: P04-S14-T08
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @system-architect-agent, @ui-designer-agent, @documentation-agent, and @development-orchestrator-agent. Your mission is to collaboratively create comprehensive visual documentation and diagrams for DafnckMachine v3.1. Ensure all system diagrams, UI documentation, and visual aids are clear, professional, and enhance understanding. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference visual documentation and diagram requirements
   - Review previous system diagrams and UI documentation if available
   - Gather standards for diagram clarity, completeness, and accessibility

3. **Save Output**
   - Save system diagrams collection: `System_Diagrams_Collection.md`
   - Save visual documentation: `Visual_Documentation.json`
   - Save UI documentation: `UI_Documentation_Complete.md`
   - Save interface guides: `Interface_Guides.json`
   - Minimal JSON schema example for visual documentation:
     ```json
     {
       "diagram": "System Architecture",
       "type": "mermaid",
       "description": "High-level system architecture diagram",
       "file": "system-architecture.mmd"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T08

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Visual and UI documentation is clear and complete
   - [ ] Diagrams and guides meet clarity and accessibility standards
   - [ ] Task status updated in workflow tracking files 
