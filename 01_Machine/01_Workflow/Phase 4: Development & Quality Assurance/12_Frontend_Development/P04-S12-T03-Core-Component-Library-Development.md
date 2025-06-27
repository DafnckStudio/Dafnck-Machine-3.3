---
phase: P04
step: S12
task: T03
task_id: P04-S12-T03
title: Core Component Library Development
agent:
  - "@coding-agent"
  - "@ui-designer-agent"
previous_task: P04-S12-T02
next_task: P04-S12-T04
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent and @ui-designer-agent. Your mission is to collaboratively design and implement a robust, reusable core component library for DafnckMachine v3.1. Ensure all UI components are accessible, responsive, well-documented, and easily testable. Align with the design system and enable rapid, consistent frontend development. Document all specifications and implementation details. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference design system guidelines and UI requirements
   - Review previous component documentation if available
   - Gather accessibility and responsive design standards

3. **Save Output**
   - Save base component documentation: `Base_Components_Library.md`
   - Save base component specs: `Component_Specifications.json`
   - Save complex component documentation: `Complex_Components_Library.md`
   - Save advanced component specs: `Advanced_Component_Specs.json`
   - Minimal JSON schema example for specs:
     ```json
     {
       "component": "Button",
       "props": ["variant", "size", "onClick"],
       "accessibility": true,
       "responsive": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S12-T04

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Components meet accessibility and responsive design standards
   - [ ] Documentation and specs are clear and complete
   - [ ] Task status updated in workflow tracking files
