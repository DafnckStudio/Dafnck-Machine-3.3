---
phase: P04
step: S14
task: T03
task_id: P04-S14-T03
title: Code Documentation and Comments
agent:
  - "@documentation-agent"
  - "@coding-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S14-T02
next_task: P04-S14-T04
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @coding-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively ensure all code for DafnckMachine v3.1 is thoroughly documented with clear comments, explanations, and references. Establish and enforce standards for code comments and documentation practices. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference code documentation requirements and standards
   - Review previous commenting standards and examples if available
   - Gather best practices for code comments and documentation

3. **Save Output**
   - Save code commenting standards: `Code_Commenting_Standards.md`
   - Save code documentation examples: `Code_Documentation_Examples.md`
   - Minimal JSON schema example for code documentation:
     ```json
     {
       "module": "auth.js",
       "functions": [
         {"name": "login", "description": "Authenticate user and return token."},
         {"name": "logout", "description": "Invalidate user session."}
       ],
       "comments": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T04

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Code documentation and comments are clear and complete
   - [ ] Standards are defined and shared with the team
   - [ ] Task status updated in workflow tracking files 
