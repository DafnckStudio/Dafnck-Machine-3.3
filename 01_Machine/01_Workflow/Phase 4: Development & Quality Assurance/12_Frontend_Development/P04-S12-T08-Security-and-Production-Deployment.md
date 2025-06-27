---
phase: P04
step: S12
task: T08
task_id: P04-S12-T08
title: Security and Production Deployment
agent:
  - "@security-auditor-agent"
  - "@devops-agent"
  - "@security-penetration-tester-agent"
  - "@adaptive-deployment-strategist-agent"
previous_task: P04-S12-T07
next_task: P04-S13-T01
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @security-auditor-agent, @devops-agent, @security-penetration-tester-agent, and @adaptive-deployment-strategist-agent. Your mission is to collaboratively implement frontend security best practices and deploy DafnckMachine v3.1 to production. Ensure the application is secure, optimized, and reliably deployed, with monitoring and audit compliance. Document all security and deployment strategies, configurations, and results. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference security and deployment requirements
   - Review previous security and deployment documentation if available
   - Gather standards for audit, monitoring, and production readiness

3. **Save Output**
   - Save security implementation guide: `Security_Implementation_Guide.md`
   - Save security audit checklist: `Security_Audit_Checklist.json`
   - Save deployment configuration guide: `Deployment_Configuration_Guide.md`
   - Save production deployment specs: `Production_Deployment_Specs.json`
   - Minimal JSON schema example for audit checklist:
     ```json
     {
       "check": "XSS Protection Enabled",
       "status": "passed",
       "details": "Content-Security-Policy header set"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T01

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Security and deployment meet compliance and operational standards
   - [ ] Documentation and audit results are clear and complete
   - [ ] Task status updated in workflow tracking files 
