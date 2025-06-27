---
phase: P04
step: S13
task: T03
task_id: P04-S13-T03
title: Authentication and User Management APIs
agent:
  - "@coding-agent"
  - "@security-auditor-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T02
next_task: P04-S13-T04
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @security-auditor-agent, and @test-orchestrator-agent. Your mission is to collaboratively implement secure authentication and user management APIs for DafnckMachine v3.1, including JWT, password hashing, session management, and RBAC. Ensure all specifications are secure, tested, and ready for integration. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference authentication and user management requirements
   - Review previous authentication and RBAC documentation if available
   - Gather standards for JWT, password hashing, and access control

3. **Save Output**
   - Save authentication implementation guide: `Authentication_Implementation.md`
   - Save JWT configuration: `JWT_Configuration.json`
   - Save user management API docs: `User_Management_APIs.md`
   - Save RBAC configuration: `RBAC_Configuration.json`
   - Minimal JSON schema example for JWT config:
     ```json
     {
       "algorithm": "HS256",
       "expiresIn": "1h",
       "issuer": "dafnckmachine"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T04

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Authentication and user management APIs are secure and tested
   - [ ] Documentation and configuration are clear and complete
   - [ ] Task status updated in workflow tracking files 
