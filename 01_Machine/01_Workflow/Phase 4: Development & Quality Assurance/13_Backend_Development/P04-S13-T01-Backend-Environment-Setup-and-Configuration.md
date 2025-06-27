---
phase: P04
step: S13
task: T01
task_id: P04-S13-T01
title: Backend Environment Setup and Configuration
agent:
  - "@coding-agent"
  - "@system-architect-agent"
  - "@security-auditor-agent"
  - "@development-orchestrator-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S12-T01
next_task: P04-S13-T02
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @system-architect-agent, @security-auditor-agent, @development-orchestrator-agent, and @test-orchestrator-agent. Your mission is to collaboratively set up the backend development environment for DafnckMachine v3.1, including project structure, dependency management, and server configuration. Ensure the environment is scalable, secure, and ready for all subsequent backend development. Document all setup steps and configurations. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference backend architecture and environment requirements
   - Review previous environment setup documentation if available
   - Gather standards for dependency management, server configuration, and security

3. **Save Output**
   - Save backend environment setup guide: `Backend_Environment_Setup.md`
   - Save server configuration: `Server_Configuration.json`
   - Minimal JSON schema example for server configuration:
     ```json
     {
       "server": "express",
       "port": 8000,
       "env": "development",
       "dependencies": ["express", "dotenv"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T02

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Backend environment is functional and secure
   - [ ] Documentation and configuration are clear and complete
   - [ ] Task status updated in workflow tracking files 
