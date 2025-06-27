---
phase: P04
step: S14
task: T05
task_id: P04-S14-T05
title: User Manual and Tutorial Creation
agent:
  - "@documentation-agent"
  - "@ui-designer-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S14-T04
next_task: P04-S14-T06
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @ui-designer-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively create comprehensive user manuals and tutorials for DafnckMachine v3.1. Ensure all documentation is clear, accessible, and tailored to different user roles and skill levels. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference user documentation requirements and onboarding needs
   - Review previous user manuals and tutorials if available
   - Gather standards for clarity, accessibility, and user experience

3. **Save Output**
   - Save user manual: `User_Manual.md`
   - Save tutorials: `Tutorials.md`
   - Minimal JSON schema example for tutorial:
     ```json
     {
       "title": "Getting Started",
       "steps": ["Sign up", "Login", "Navigate dashboard"],
       "audience": "end user"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T06

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] User manuals and tutorials are clear and user-friendly
   - [ ] Documentation is accessible to all user roles
   - [ ] Task status updated in workflow tracking files 
