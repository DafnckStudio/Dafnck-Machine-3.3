---
phase: P04
step: S12
task: T05
task_id: P04-S12-T05
title: State Management and API Integration
agent:
  - "@coding-agent"
  - "@system-architect-agent"
  - "@development-orchestrator-agent"
previous_task: P04-S12-T04
next_task: P04-S12-T06
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @system-architect-agent, and @development-orchestrator-agent. Your mission is to collaboratively implement robust state management and API integration for DafnckMachine v3.1. Ensure scalable, efficient state handling, backend communication, and real-time data synchronization. Document all specifications and implementation details. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference architecture and API requirements
   - Review previous state management and API documentation if available
   - Gather standards for data flow, caching, and synchronization

3. **Save Output**
   - Save state management guide: `State_Management_Guide.md`
   - Save data flow architecture: `Data_Flow_Architecture.json`
   - Save API integration guide: `API_Integration_Guide.md`
   - Save data synchronization specs: `Data_Synchronization_Specs.json`
   - Minimal JSON schema example for data flow:
     ```json
     {
       "slice": "user",
       "actions": ["login", "logout", "updateProfile"],
       "api": "/api/user",
       "sync": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S12-T06

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] State management and API logic meet efficiency and reliability standards
   - [ ] Documentation and specs are clear and complete
   - [ ] Task status updated in workflow tracking files
