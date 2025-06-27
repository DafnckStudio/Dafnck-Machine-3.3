---
phase: P04
step: S12
task: T06
task_id: P04-S12-T06
title: Responsive Design and Accessibility
agent:
  - "@coding-agent"
  - "@design-system-agent"
  - "@ux-researcher-agent"
  - "@usability-heuristic-agent"
previous_task: P04-S12-T05
next_task: P04-S12-T07
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @design-system-agent, @ux-researcher-agent, and @usability-heuristic-agent. Your mission is to collaboratively implement fully responsive design and accessibility for DafnckMachine v3.1. Ensure the frontend adapts to all devices and meets accessibility standards (WCAG, ARIA, keyboard navigation). Document all specifications and implementation details. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference design system and accessibility requirements
   - Review previous responsive and accessibility documentation if available
   - Gather standards for breakpoints, ARIA, and WCAG compliance

3. **Save Output**
   - Save responsive design guide: `Responsive_Design_Guide.md`
   - Save breakpoint specs: `Breakpoint_Specifications.json`
   - Save accessibility implementation guide: `Accessibility_Implementation_Guide.md`
   - Save WCAG compliance checklist: `WCAG_Compliance_Checklist.json`
   - Minimal JSON schema example for breakpoints:
     ```json
     {
       "breakpoint": "md",
       "minWidth": 768,
       "maxWidth": 1023,
       "appliesTo": ["tablet", "desktop"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S12-T07

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Responsive and accessibility features meet standards and compliance
   - [ ] Documentation and specs are clear and complete
   - [ ] Task status updated in workflow tracking files 
