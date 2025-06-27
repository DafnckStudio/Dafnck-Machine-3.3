---
phase: P04
step: S12
task: T04
task_id: P04-S12-T04
title: Page Implementation and Routing
agent:
  - "@coding-agent"
  - "@ui-designer-agent"
  - "@development-orchestrator-agent"
previous_task: P04-S12-T03
next_task: P04-S12-T05
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @ui-designer-agent, and @development-orchestrator-agent. Your mission is to collaboratively implement all core application pages and configure robust routing for DafnckMachine v3.1. Ensure seamless navigation, modular page structure, and alignment with the frontend architecture. Document all specifications and implementation details. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference design system and navigation requirements
   - Review previous page and routing documentation if available
   - Gather accessibility and responsive layout standards

3. **Save Output**
   - Save page implementation guide: `Page_Implementation_Guide.md`
   - Save layout specs: `Layout_Specifications.json`
   - Save routing implementation guide: `Routing_Implementation_Guide.md`
   - Save navigation config: `Navigation_Configuration.json`
   - Minimal JSON schema example for layout/navigation:
     ```json
     {
       "page": "Dashboard",
       "route": "/dashboard",
       "layout": "MainLayout",
       "protected": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S12-T05

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Pages and routing meet accessibility and responsive design standards
   - [ ] Documentation and specs are clear and complete
   - [ ] Task status updated in workflow tracking files
