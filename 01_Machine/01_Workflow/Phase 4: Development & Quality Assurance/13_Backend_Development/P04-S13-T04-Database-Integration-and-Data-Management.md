---
phase: P04
step: S13
task: T04
task_id: P04-S13-T04
title: Database Integration and Data Management
agent:
  - "@coding-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T03
next_task: P04-S13-T05
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively implement database integration, ORM setup, data models, migration system, and data seeding for DafnckMachine v3.1 backend. Ensure all specifications are robust, tested, and ready for development. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference database and ORM requirements
   - Review previous integration and migration documentation if available
   - Gather standards for schema design, migrations, and seeding

3. **Save Output**
   - Save database integration guide: `Database_Integration_Guide.md`
   - Save ORM configuration: `ORM_Configuration.json`
   - Save migration system guide: `Migration_System_Guide.md`
   - Save data seeding scripts: `Data_Seeding_Scripts.json`
   - Minimal JSON schema example for ORM config:
     ```json
     {
       "orm": "prisma",
       "database": "postgresql",
       "models": ["User", "Session", "Role"],
       "migrations": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T05

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Database integration and migration system are functional and tested
   - [ ] Documentation and configuration are clear and complete
   - [ ] Task status updated in workflow tracking files 
