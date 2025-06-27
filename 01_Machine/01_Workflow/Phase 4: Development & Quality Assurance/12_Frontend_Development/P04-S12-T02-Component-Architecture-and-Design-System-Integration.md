---
phase: P04
step: S12
task: T02
task_id: P04-S12-T02
title: Component Architecture and Design System Integration
agent: ["@coding-agent", "@ui-designer-agent", "@design-system-agent"]
previous_task: P04-S12-T01
next_task: P04-S12-T03
version: 3.1.0
source: Step.json
---

# Super Prompt
@coding-agent (lead), with support from @ui-designer-agent and @design-system-agent: Design and implement scalable component architecture and integrate the design system for DafnckMachine v3.1. Document all architecture, integration, and configuration steps with clear rationale and evidence. Output all component and design system files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Gather requirements for component architecture, design system, and styling from previous steps and team input.
   - Collect preferences and constraints regarding UI structure, composition, and theming.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4/12_Frontend_Development/Component_Architecture_Design.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4/12_Frontend_Development/Component_Structure_Specs.json (JSON, schema: {"components": [string], "structure": object, "patterns": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4/12_Frontend_Development/Design_System_Integration.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4/12_Frontend_Development/Styling_Configuration.json (JSON, schema: {"tokens": object, "themes": object, "breakpoints": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the component architecture and design system rationale clearly documented?
   - [ ] Are architecture, integration, and configuration steps justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
