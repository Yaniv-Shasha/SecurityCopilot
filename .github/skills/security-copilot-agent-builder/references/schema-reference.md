# Security Copilot Agent Schema Reference

Complete field reference for all manifest components.

## Descriptor Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | string | Yes | Internal unique name. No `/`, `\`, `?`, `#`, `@`, or whitespace |
| DisplayName | string | Recommended | Human-readable name |
| Description | string | Yes | Human-readable description (cannot be null/empty) |
| Authorization | object | Conditional | Required for API tools when SupportedAuthTypes != None |
| SupportedAuthTypes | array | Conditional | Required for API tools |

### Naming Conventions
- Use format: `CompanyName.Product.Purpose-YYMMDD`
- Example: `Contoso.SecurityOperations.URLAnalyzer-090925`

## SkillGroups Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Format | string | Yes | `API`, `GPT`, `AGENT`, `KQL`, `LogicApp`, or `MCP` |
| Skills | object | Yes | List of skills in this group (not used for MCP format) |
| Settings | object | Yes | Format-specific settings |

### Skills Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | string | Yes | Internal name (no whitespace or periods) |
| DisplayName | string | Recommended | Human-readable name |
| Description | string | Recommended | Human-readable description |
| Inputs | array | No | List of input parameters |
| Settings | object | Yes | Format-specific settings |
| ChildSkills | array | Conditional | Required for `Format: AGENT` |
| Interfaces | object | Conditional | Set to `Agent` or `InteractiveAgent` |
| SuggestedPrompts | object | Conditional | For Interactive agents only |

## AgentDefinitions Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | string | Yes | Installation name (no whitespace or periods) |
| DisplayName | string | Yes | User-friendly UI name |
| Description | string | Yes | Summary of agent purpose |
| Publisher | string | Yes | Name of the publisher |
| Product | string | Yes | Source product for filtering |
| RequiredSkillsets | array | Yes | Skillsets the agent needs |
| AgentSingleInstanceConstraint | string | No | `None`, `Workspace`, or `Tenant` |
| Settings | object | No | Applied to FetchSkill invocation |
| Triggers | object | Yes | How/when agent is triggered |
| PromptSkill | object | Conditional | For Interactive agents only |

### Triggers Configuration

| Field | Required | Description |
|-------|----------|-------------|
| Name | Yes | Descriptive name (no whitespace) |
| DefaultPeriodSeconds | No | Interval for scheduled execution (0 = disabled) |
| FetchSkill | No | Skill to invoke first (returns array of objects) |
| ProcessSkill | Yes | Skill called for each object from FetchSkill |

## Format-Specific Settings

### AGENT Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| Model | Yes | Must be `gpt-4.1` |
| Instructions | Yes | Natural language guidance for agent behavior |

### GPT Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| ModelName | Yes | Must be `gpt-4.1` |
| Template | Yes | GPT prompt template (up to 80,000 chars) |

### KQL Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| Target | Yes | `Defender`, `Sentinel`, or `Kusto` |
| Template | Yes | KQL query template (up to 80,000 chars) |

**Sentinel-specific:**
- TenantId, SubscriptionId, ResourceGroupName, WorkspaceName

**Kusto-specific:**
- Cluster, Database

### API Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| OpenApiSpecUrl | Yes | URL to OpenAPI specification |
| EndpointUrl | No | Override API server URL |
| EndpointUrlSettingName | No | Make endpoint configurable |
| EnableSkillContextApi | No | Enable SkillContext API access |

### LogicApp Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| SubscriptionId | Yes | Azure subscription ID |
| ResourceGroup | Yes | Azure resource group |
| WorkflowName | Yes | Logic App name |
| TriggerName | Yes | Trigger name in Logic Apps |

### MCP Format Settings

| Field | Required | Description |
|-------|----------|-------------|
| Endpoint | Yes | URL of the MCP Server |
| UseStreamableHttp | Yes | Use StreamableHttp (true) or SSE (false) |
| UsePluginAuth | Yes | `true` for OAuth2/AADDelegated, `false` for user credential |
| TokenScope | Conditional | Required if `UsePluginAuth: false` |
| AllowedTools | Yes | Comma-separated list of allowed tool names |
| TimeoutInSeconds | No | Timeout for tool execution |

## Authentication Types

| Type | Description | Workspace Upload | User Upload |
|------|-------------|------------------|-------------|
| None | No authentication | Yes | Yes |
| Basic | Username/Password | Yes | No |
| ApiKey | Key in header/query | Yes | Yes |
| ServiceHttp | Token-based | Yes | Yes |
| OAuthAuthorizationCodeFlow | OAuth 2.0 code flow | Yes | Yes |
| OAuthClientCredentialsFlow | Server-to-server OAuth | Yes | No |
| OAuthPasswordGrantFlow | Legacy (not recommended) | Yes | No |
| AAD | Microsoft Entra App only | Yes | Yes |
| AADDelegated | User + Microsoft Entra | Yes | Yes |

### Authentication Configuration Examples

**API Key:**
```yaml
Descriptor:
  SupportedAuthTypes:
    - ApiKey
  Authorization:
    ApiKey:
      Key: X-Api-Key
      Location: Header
      Value: your-api-key
```

**OAuth Client Credentials:**
```yaml
Descriptor:
  SupportedAuthTypes:
    - OAuthClientCredentialsFlow
  Authorization:
    OAuthClientCredentialsFlow:
      TokenEndpoint: https://login.microsoftonline.com/tenant/oauth2/v2.0/token
      ClientId: your-client-id
      ClientSecret: your-client-secret
      Scopes: https://api.example.com/.default
```

**Microsoft Entra (AAD):**
```yaml
Descriptor:
  SupportedAuthTypes:
    - AAD
  Authorization:
    AAD:
      EntraScopes: https://graph.microsoft.com/.default
```
