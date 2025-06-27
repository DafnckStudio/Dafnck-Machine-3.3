---
phase: P04
step: S15
task: T06
task_id: P04-S15-T06
title: Security Testing Implementation
agent:
  - "@security-penetration-tester-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S15-T05
next_task: P04-S15-T07
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @security-penetration-tester-agent and @test-orchestrator-agent. Your mission is to collaboratively implement comprehensive security testing for DafnckMachine v3.1, including vulnerability scanning, penetration testing, security validation, authentication, and compliance testing. Ensure the application meets all security and compliance requirements. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference security testing and compliance requirements
   - Review previous security and vulnerability documentation if available
   - Gather standards for penetration testing, authentication, and access control

3. **Save Output**
   - Save security testing implementation: `Security_Testing_Implementation.md`
   - Save vulnerability scanning setup: `Vulnerability_Scanning_Setup.json`
   - Save authentication testing framework: `Authentication_Testing_Framework.md`
   - Save access control validation: `Access_Control_Validation.json`
   - Minimal JSON schema example for vulnerability scanning setup:
     ```json
     {
       "tool": "OWASP ZAP",
       "targets": ["/api", "/login"],
       "scanTypes": ["active", "passive"],
       "compliance": ["OWASP Top 10"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T07

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Security and authentication tests are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
