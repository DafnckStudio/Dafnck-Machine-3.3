---
phase: P04
step: S15
task: T06
task_id: P04-S15-T06
title: Security Testing Implementation
<<<<<<< HEAD
agent:
  - "@security-penetration-tester-agent"
  - "@test-orchestrator-agent"
=======
>>>>>>> 8f6410b869c68e2dec6a6798282a4437e78b5f85
previous_task: P04-S15-T05
next_task: P04-S15-T07
version: 3.1.0
source: Step.json
<<<<<<< HEAD
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
=======
agent: "@security-penetration-tester-agent"
orchestrator: "@uber-orchestrator-agent"
---
## Output Artifacts Checklist
- [ ] 01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Security_Testing_Implementation.md — Security_Testing_Implementation.md (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Vulnerability_Scanning_Setup.json — Vulnerability_Scanning_Setup.json (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Authentication_Testing_Framework.md — Authentication_Testing_Framework.md (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Access_Control_Validation.json — Access_Control_Validation.json (missing)

# Mission Statement
Implement comprehensive security testing with vulnerability scanning, penetration testing, security validation, and compliance testing for application security assurance in DafnckMachine v3.1.

# Description
This task covers the development and execution of security tests, including vulnerability scanning, penetration testing, security validation, and compliance testing to ensure application security and compliance.

# Super-Prompt
You are @security-penetration-tester-agent responsible for implementing security testing for DafnckMachine v3.1. Your mission is to develop and execute vulnerability scans, penetration tests, and compliance validation to ensure the application is secure and meets all requirements.

# MCP Tools Required
- edit_file
- run_terminal_cmd

# Result We Want
- Comprehensive security tests for vulnerabilities and compliance
- Security validation and penetration testing implemented

# Add to Brain
- Security testing implementation and validation

# Documentation & Templates
- [Security_Testing_Implementation.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Security_Testing_Implementation.md)
- [Vulnerability_Scanning_Setup.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Vulnerability_Scanning_Setup.json)
- [Authentication_Testing_Framework.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Authentication_Testing_Framework.md)
- [Access_Control_Validation.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Access_Control_Validation.json)

# Supporting Agents
- @test-orchestrator-agent

# Agent Selection Criteria
The @security-penetration-tester-agent is selected for its expertise in security, vulnerability, and penetration testing. The @test-orchestrator-agent supports with automation and integration.

# Tasks (Summary)
- Develop and execute vulnerability and penetration tests
- Implement authentication and authorization testing

# Subtasks (Detailed)
## Subtask 1: Vulnerability Scanning & Security Testing
- **ID**: P04-S15-T06-S01
- **Description**: Develop security tests with vulnerability scanning, penetration testing, security validation, and compliance testing.
- **Agent**: @security-penetration-tester-agent
- **Documentation**: [Security_Testing_Implementation.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Security_Testing_Implementation.md), [Vulnerability_Scanning_Setup.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Vulnerability_Scanning_Setup.json)
- **Steps**:
    1. Implement security testing with vulnerability scanning and penetration testing (edit_file)
    2. Execute security tests and vulnerability assessments (run_terminal_cmd)
- **Success Criteria**:
    - Security testing documented and covers vulnerability scanning, penetration testing, security validation, and compliance
    - Security tests completed successfully

## Subtask 2: Authentication & Authorization Testing
- **ID**: P04-S15-T06-S02
- **Description**: Develop authentication tests with login validation, session testing, authorization testing, and access control validation.
- **Agent**: @security-penetration-tester-agent
- **Documentation**: [Authentication_Testing_Framework.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Authentication_Testing_Framework.md), [Access_Control_Validation.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Access_Control_Validation.json)
- **Steps**:
    1. Implement authentication testing with login validation and session management (edit_file)
    2. Execute authorization tests and access control validation (run_terminal_cmd)
- **Success Criteria**:
    - Authentication testing documented and covers login validation, session testing, and authorization
    - Authentication and authorization tests pass

# Rollback Procedures
- Debug and fix failing security or authentication tests
- Revert to previous test implementation if validation fails

# Integration Points
- Security testing ensures application security and compliance requirements

# Quality Gates
- All security and authentication tests pass

# Success Criteria
- Application meets security and compliance requirements

# Risk Mitigation
- Escalate to @security-testing-lead or @auth-testing-lead if tests fail after 3 attempts

# Output Artifacts
- [Security_Testing_Implementation.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Security_Testing_Implementation.md)
- [Vulnerability_Scanning_Setup.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Vulnerability_Scanning_Setup.json)
- [Authentication_Testing_Framework.md](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Authentication_Testing_Framework.md)
- [Access_Control_Validation.json](mdc:01_Machine/04_Documentation/vision/Phase_4/15_Automated_Testing/Access_Control_Validation.json)

# Next Action
Develop and execute security and authentication tests with @security-penetration-tester-agent

# Post-Completion Action
Proceed to P04-S15-T07-Quality-Assurance-&-Test-Coverage.md 
>>>>>>> 8f6410b869c68e2dec6a6798282a4437e78b5f85
