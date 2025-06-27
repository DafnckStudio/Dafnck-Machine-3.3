---
phase: P04
step: S15
task: T04
task_id: P04-S15-T04
title: End-to-End Testing Implementation
agent:
  - "@functional-tester-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S15-T03
next_task: P04-S15-T05
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @functional-tester-agent and @test-orchestrator-agent. Your mission is to collaboratively implement comprehensive end-to-end (E2E) testing for DafnckMachine v3.1, including user journey automation, workflow validation, cross-browser testing, and visual regression testing using Playwright. Ensure robust user experience validation across browsers and devices. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference E2E and visual regression testing requirements
   - Review previous E2E and UI validation documentation if available
   - Gather standards for Playwright, user journey automation, and accessibility testing

3. **Save Output**
   - Save E2E testing implementation: `E2E_Testing_Implementation.md`
   - Save user journey automation specs: `User_Journey_Automation.json`
   - Save visual regression testing guide: `Visual_Regression_Testing.md`
   - Save UI validation framework: `UI_Validation_Framework.json`
   - Minimal JSON schema example for user journey automation:
     ```json
     {
       "journey": "Login and Dashboard",
       "steps": ["visit /login", "enter credentials", "submit", "verify dashboard"],
       "browsers": ["chromium", "firefox", "webkit"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T05

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] E2E and visual regression tests are comprehensive and pass across browsers
   - [ ] Documentation and specs are clear and complete
   - [ ] Task status updated in workflow tracking files 
