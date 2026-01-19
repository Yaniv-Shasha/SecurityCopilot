---
name: sentinel-mcp-tools
description: Helps integrate Microsoft Sentinel MCP (Model Context Protocol) tools into Security Copilot agents. Use when adding Sentinel data exploration, triage, or custom KQL-based MCP tools to security agents. Covers built-in tool collections, custom tool creation, and MCP plugin YAML configuration.
license: Complete terms in LICENSE.txt
---

# Microsoft Sentinel MCP Tools Integration

Integrate Microsoft Sentinel MCP tools into Security Copilot agents.

## Overview

Microsoft Sentinel MCP Server provides security-focused tools that enable AI agents to:
- Search tables and query the data lake
- Analyze entities (users, IPs, URLs)
- Triage incidents and hunt for threats

## Built-in Collections

| Collection | Endpoint | Use Case |
|------------|----------|----------|
| **Data Exploration** | `https://sentinel.microsoft.com/mcp/data-exploration` | Search tables, query lake, analyze entities |
| **Triage** | `https://sentinel.microsoft.com/mcp/triage` | Incident triage, threat hunting |
| **Agent Creation** | `https://sentinel.microsoft.com/mcp/security-copilot-agent-creation` | Create Security Copilot agents |

## Quick Start

### Add MCP Tools to Agent YAML

```yaml
Descriptor:
  Name: MySentinelMCPTools
  DisplayName: My Sentinel MCP Tools
  Description: Sentinel MCP tools for security analysis

SkillGroups:
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
      TokenScope: 4500ebfb-89b6-4b14-a480-7f749797bfcd/.default
      UseStreamableHttp: true
      UsePluginAuth: false
      AllowedTools: query_lake,search_tables,analyze_user_entity
      TimeoutInSeconds: 300
```

### MCP Settings Reference

| Setting | Required | Description |
|---------|----------|-------------|
| Endpoint | Yes | MCP server URL |
| UseStreamableHttp | Yes | `true` (SSE will be deprecated) |
| UsePluginAuth | Yes | `false` to use user credential |
| TokenScope | Yes* | Required when `UsePluginAuth: false` |
| AllowedTools | Yes | Comma-separated tool names |
| TimeoutInSeconds | No | Timeout for execution |

> **Sentinel Token Scope:** `4500ebfb-89b6-4b14-a480-7f749797bfcd/.default`

## Integration Patterns

### Pattern 1: MCP-Only Agent

```yaml
SkillGroups:
  - Format: AGENT
    Skills:
      - Name: DataExplorer
        ChildSkills: [query_lake, search_tables]
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
      AllowedTools: query_lake,search_tables
```

### Pattern 2: Hybrid (MCP + KQL)

```yaml
SkillGroups:
  - Format: AGENT
    Skills:
      - Name: HybridInvestigator
        ChildSkills: [analyze_user_entity, CustomAlertQuery]
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
      AllowedTools: analyze_user_entity
  - Format: KQL
    Skills:
      - Name: CustomAlertQuery
        Settings:
          Target: Sentinel
          Template: SecurityAlert | take 10
```

### Pattern 3: Multi-Collection

```yaml
SkillGroups:
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/data-exploration
      AllowedTools: query_lake,search_tables
  - Format: MCP
    Settings:
      Endpoint: https://sentinel.microsoft.com/mcp/triage
      AllowedTools: get_incidents,prioritize_alerts
```

## Creating Custom MCP Tools

Create tools from saved KQL queries in Advanced Hunting:

1. Go to **Advanced Hunting** in Microsoft Defender portal
2. Write your KQL query
3. Select **Save as tool**
4. Configure: Name, Description, Collection, Parameters

### Example: Parameterized Tool

```kql
SecurityEvent
| where TimeGenerated > ago({LookbackHours}h)
| where Account contains "{UserName}"
| summarize EventCount = count() by Activity
| top 10 by EventCount desc
```

### Tool Description Best Practices

| Do | Don't |
|----|-------|
| Keep short (1-2 sentences) | Write lengthy explanations |
| Start with a verb | Use jargon |
| Focus on purpose | Describe all parameters |

**Good:** "Retrieves audit log data for a specific user within a configurable time window."

**Poor:** "Helps with logs."

## Sample Prompts

| Use Case | Prompt |
|----------|--------|
| User Risk | "Find the top three users at risk and explain why" |
| Sign-ins | "Find sign-in failures in the last 24 hours" |
| Network | "Identify devices with outstanding outgoing connections" |
| Compromise Check | "Is user `<objectId>` compromised?" |

## Known Limitations

- Only MCP **tools** supported (not resources, prompts, utilities)
- Tool updates require re-uploading YAML
- `destructiveHint: true` tools not imported
- Only primitive input types supported

## Templates

Ready-to-use templates:

| Template | Description |
|----------|-------------|
| [data-exploration-plugin.yaml](templates/data-exploration-plugin.yaml) | Data exploration tools |
| [triage-plugin.yaml](templates/triage-plugin.yaml) | Incident triage tools |
| [custom-tools-plugin-template.yaml](templates/custom-tools-plugin-template.yaml) | Custom tool collection |
| [complete-sentinel-mcp-agent.yaml](templates/complete-sentinel-mcp-agent.yaml) | Full agent with MCP |

## Additional Resources

- [Get started with Sentinel MCP](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started)
- [Tool collections overview](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview)
- [Create custom MCP tools](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)
- [MCP plugins in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp)
