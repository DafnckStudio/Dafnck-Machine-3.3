---
phase: P03
step: S05
task: T01
task_id: P03-S05-T01
title: System Overview and Vision Definition
previous_task: P02-S04-T08
next_task: P03-S05-T02
version: 3.1.0
agent: "@prd-architect-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @prd-architect-agent, supported by @system-architect-agent. Your job is to define the core mission and autonomous architecture for DafnckMachine v3.1, establishing the foundational vision for fully autonomous AI-driven software delivery with agent swarm coordination. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure architectural completeness.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/05_PRD_Generator/`

## 2. Collect Data/Input
- Gather requirements for autonomous software delivery and agent swarm coordination
- Analyze best practices for agentic architectures

## 3. Save Output
- Save system overview and vision to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Product_Requirements_Document.md`
- Save agent swarm architecture to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Agent_Swarm_Architecture.json`

### Agent_Swarm_Architecture.json (JSON Schema)
```
{
  "type": "object",
  "properties": {
    "agents": {"type": "array", "items": {"type": "object"}},
    "coordination_protocols": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["agents", "coordination_protocols"]
}
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Is the system vision and agent swarm architecture clearly documented?
- [ ] Are agent coordination protocols explicit and actionable?
- [ ] Have all supporting agents contributed as needed? 
