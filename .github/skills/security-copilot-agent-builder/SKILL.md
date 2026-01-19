---
name: security-copilot-agent-builder
description: Helps build Microsoft Security Copilot agents using YAML manifests. Use when creating, editing, or troubleshooting Security Copilot agent definitions, skills, triggers, or authentication configurations. Covers the complete manifest schema including Descriptor, SkillGroups, and AgentDefinitions.
license: Complete terms in LICENSE.txt
---

# Security Copilot Agent Builder

Build Microsoft Security Copilot agents using YAML manifests.

## Overview

Security Copilot agents are defined using a YAML manifest with three top-level keys:

1. **Descriptor** - Metadata about the skill set (plugin)
2. **SkillGroups** - The tools/skills the agent can use
3. **AgentDefinitions** - Agent behavior and triggers

## Quick Start

```yaml
Descriptor:
  Name: YourCompany.YourProduct.YourPurpose-YYMMDD
  DisplayName: Your Agent Display Name
  Description: What your agent does

SkillGroups:
  - Format: AGENT
    Skills:
      - Name: YourSkillName-v1
        DisplayName: Your Skill Display Name
        Description: What this skill does
        Interfaces:
          - Agent
        Inputs:
          - Name: InputName
            Description: What this input is for
            Required: true
        Settings:
          Model: gpt-4.1
          Instructions: |
            Your agent instructions here...
        ChildSkills:
          - OtherSkillName

AgentDefinitions:
  - Name: YourAgentName-v1
    DisplayName: Your Agent Display Name
    Description: What your agent does
    Publisher: YourCompany
    Product: YourProduct
    RequiredSkillsets:
      - YourCompany.YourProduct.YourPurpose-YYMMDD
    AgentSingleInstanceConstraint: None
    Triggers:
      - Name: DefaultTrigger
        DefaultPeriodSeconds: 0
        ProcessSkill: YourCompany.YourProduct.YourPurpose-YYMMDD.YourSkillName-v1
```

## Format Types

### AGENT Format
Orchestrates multiple child skills for complex tasks.

```yaml
- Format: AGENT
  Skills:
    - Name: MyAgent-v1
      Interfaces: [Agent]
      Inputs:
        - Name: URL
          Description: URL to analyze
          Required: true
      Settings:
        Model: gpt-4.1
        Instructions: |
          You are an AI agent that helps analyze URLs...
      ChildSkills:
        - ExtractHostname-v1
        - LookupGeolocation
```

### GPT Format
LLM-based text processing.

```yaml
- Format: GPT
  Skills:
    - Name: ExtractHostname-v1
      Inputs:
        - Name: URL
          Required: true
      Settings:
        ModelName: gpt-4.1
        Template: |-
          <|im_start|>system
          Return the hostname from the URL.
          <|im_end|>
          <|im_start|>user
          {{URL}}
          <|im_end|>
```

### KQL Format
Kusto queries for Defender, Sentinel, or Kusto.

```yaml
- Format: KQL
  Skills:
    - Name: RecentAlerts-v1
      Settings:
        Target: Defender  # or Sentinel, Kusto
        Template: |
          SecurityAlert
          | where TimeGenerated > ago(24h)
          | top 10 by TimeGenerated desc
```

### API Format
External API via OpenAPI spec.

```yaml
- Format: API
  Skills:
    - Name: ThreatLookup-v1
      Settings:
        OpenApiSpecUrl: https://api.example.com/openapi.json
        EndpointUrl: https://api.example.com
```

### MCP Format
Connect to MCP servers including Microsoft Sentinel.

```yaml
- Format: MCP
  Settings:
    Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
    TokenScope: 4500ebfb-89b6-4b14-a480-7f749797bfcd/.default
    UseStreamableHttp: true
    UsePluginAuth: false
    AllowedTools: query_lake,search_tables,analyze_user_entity
    TimeoutInSeconds: 300
```

> For comprehensive Sentinel MCP guidance, see [sentinel-mcp-tools](../sentinel-mcp-tools/SKILL.md).

### LogicApp Format
Azure Logic Apps integration.

```yaml
- Format: LogicApp
  Skills:
    - Name: AutoResponse-v1
      Settings:
        SubscriptionId: your-subscription-id
        ResourceGroup: your-resource-group
        WorkflowName: IncidentResponseWorkflow
        TriggerName: manual
```

## Common Patterns

### Multi-Step Investigation Agent
1. **FetchSkill**: Query items to investigate (alerts, incidents)
2. **ProcessSkill**: Agent orchestrating analysis via ChildSkills
3. **ChildSkills**: Individual tools for enrichment and lookup

### Interactive Agent
Add `Interfaces: [InteractiveAgent]` and `SuggestedPrompts` for chat experience.

### Sentinel MCP Integration
Combine AGENT format with MCP format:
```yaml
SkillGroups:
  - Format: AGENT
    Skills:
      - Name: InvestigationAgent
        ChildSkills: [query_lake, analyze_user]
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
      AllowedTools: query_lake,analyze_user
```

## Validation Checklist

- [ ] Descriptor.Name is unique with no special characters
- [ ] All skill Names have no whitespace or periods
- [ ] AGENT format skills have ChildSkills defined
- [ ] GPT/AGENT format: Model/ModelName is `gpt-4.1`
- [ ] KQL format has Target specified
- [ ] MCP format has Endpoint and AllowedTools
- [ ] Triggers have Name and ProcessSkill

## Reference Documentation

- **[Schema Reference](references/schema-reference.md)** - Complete field definitions for all manifest components
- **[sentinel-mcp-tools](../sentinel-mcp-tools/SKILL.md)** - Sentinel MCP integration guide

## Templates

Ready-to-use starter templates:

| Template | Description |
|----------|-------------|
| [starter-template.yaml](templates/starter-template.yaml) | Minimal working agent |
| [complete-example.yaml](templates/complete-example.yaml) | Full-featured agent with multiple formats |
| [interactive-agent.yaml](templates/interactive-agent.yaml) | Interactive chat agent |
| [kql-alert-investigator.yaml](templates/kql-alert-investigator.yaml) | KQL-based alert investigation |

## Complete Working Examples

Production-ready agents in this project:

| Agent | Description | Location |
|-------|-------------|----------|
| **Phish URL Blast Radius** | Multi-skill agent with SafeLinks decoding, MCP tools | [blast_test.yaml](../../../blast_test.yaml) |
| **Unauthorized Access Agent** | UEBA-based investigation with child skills | [agent 4.yaml](../../../agent%204.yaml) |

### Key Patterns Demonstrated

**blast_test.yaml:** SafeLinks URL decoding, MCP integration, feature flags, multi-agent orchestration

**agent 4.yaml:** Child skill pattern, dynamic MCP tool selection, hidden helper skills, SOP-driven instructions

## Additional Resources

- [Official Documentation](https://learn.microsoft.com/en-us/copilot/security/developer/agent-manifest)
- [Build Agent API Sample](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-api-sample)
- [Interactive Agents](https://learn.microsoft.com/en-us/copilot/security/developer/build-interactive-agents)
