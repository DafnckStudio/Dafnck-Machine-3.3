---
phase: P05
step: S17
task: T03
task_id: P05-S17-T03
title: User Analytics and Behavior Tracking
agent:
  - "@analytics-setup-agent"
  - "@health-monitor-agent"
  - "@data-analyst-agent"
  - "@devops-agent"
previous_task: P05-S17-T02
next_task: P05-S17-T04
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @analytics-setup-agent, collaborating with @health-monitor-agent, @data-analyst-agent, and @devops-agent. Your mission is to implement user analytics and behavior tracking for DafnckMachine v3.1, ensuring comprehensive event collection, session analysis, conversion tracking, and actionable engagement insights. Document all analytics setup and tracking procedures with clear guidelines and best practices. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - All outputs must be saved in: `01_Machine/04_Documentation/vision/Phase_5/17_Monitoring_Analytics/`

2. **Collect Data/Input**
   - Reference user analytics and behavior tracking requirements
   - Review previous analytics, tracking, and engagement documentation if available
   - Gather standards for event collection, session analysis, and A/B testing

3. **Save Output**
   - Save user analytics implementation: `User_Analytics_Implementation.md`
   - Save behavior tracking setup: `Behavior_Tracking_Setup.json`
   - Save engagement analytics framework: `Engagement_Analytics_Framework.md`
   - Save optimization insights: `Optimization_Insights.json`
   - Minimal JSON schema example for behavior tracking setup:
     ```json
     {
       "trackingImplementation": true,
       "eventCollection": ["click", "pageView", "conversion"],
       "sessionAnalysis": true,
       "conversionTracking": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P05-S17-T04

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] User analytics and engagement tracking are implemented and operational
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
