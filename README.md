<p align="center"><img src="./assets/wealthnow-logo-512.png" alt="Wealthnow" width="112" height="112"></p>

# Wealthnow MCP server

**Market data MCP for AI agents: prices, fundamentals, SEC filings, insider, 13F and congress trades, options flow, credit, macro, private markets.**

[![MCP Registry](https://img.shields.io/badge/MCP_Registry-io.wealthnow%2Fmcp-0b0b14?style=flat-square)](https://registry.modelcontextprotocol.io/v0.1/servers/io.wealthnow%2Fmcp/versions/latest)
[![Add to Claude](https://img.shields.io/badge/Claude-Add_Wealthnow-D97757?style=flat-square&logo=claude&logoColor=white)](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Wealthnow&connectorUrl=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp)
[![Add to Cursor](https://img.shields.io/badge/Cursor-Add_Wealthnow-000000?style=flat-square)](https://cursor.com/install-mcp?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0%3D)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Wealthnow-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Wealthnow-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D&quality=insiders)
[![Add to Kiro](https://img.shields.io/badge/Kiro-Add_Wealthnow-7B42F6?style=flat-square)](https://kiro.dev/launch/mcp/add?name=wealthnow&config=%7B%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D)

Wealthnow is a hosted [Model Context Protocol](https://modelcontextprotocol.io) server. Add one URL to your AI app, sign in to Wealthnow, and your agent can call financial data tools directly. Nothing to install or run.

| | |
|---|---|
| **Endpoint** | `https://mcp.wealthnow.io/mcp` |
| **Transport** | Streamable HTTP |
| **Sign-in** | OAuth 2.1. Your AI app opens Wealthnow's sign-in page and returns you connected, with no key to copy. |
| **API key** | Optional, for scripts and apps without OAuth: send it in the `X-API-Key` header (or as `Authorization: Bearer`). |
| **Registry** | [`io.wealthnow/mcp`](https://registry.modelcontextprotocol.io/v0.1/servers/io.wealthnow%2Fmcp/versions/latest) in the official MCP Registry |
| **Free plan** | 1,000 credits a month, no card needed. Connecting from an AI app starts it for you. |
| **Docs** | [app.wealthnow.io/docs/mcp-and-sdks](https://app.wealthnow.io/docs/mcp-and-sdks) |

*Wealthnow provides data for research. It is not investment advice; see [Disclosure](#disclosure).*

---

## Install

Every app below connects to the same URL, `https://mcp.wealthnow.io/mcp`, and signs you in to Wealthnow in the browser the first time you use it. No key is needed unless noted.

### Quick install

| App | One click or one command |
|---|---|
| **Claude** (web, Desktop, mobile) | [Add Wealthnow to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Wealthnow&connectorUrl=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp) |
| **Cursor** | [Add Wealthnow to Cursor](https://cursor.com/install-mcp?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0%3D) |
| **VS Code** (GitHub Copilot) | [Install in VS Code](https://vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D) · [Install in VS Code Insiders](https://insiders.vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D&quality=insiders) |
| **Kiro** | [Add Wealthnow to Kiro](https://kiro.dev/launch/mcp/add?name=wealthnow&config=%7B%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D) |
| **ChatGPT** | Plugins → **+** → **Add custom MCP server** → `https://mcp.wealthnow.io/mcp` ([steps](#chatgpt)) |
| **Claude Code** | `claude mcp add --transport http --scope user wealthnow https://mcp.wealthnow.io/mcp` |
| **Gemini CLI** | `gemini extensions install https://github.com/Hlobo-dev/wealthnow-mcp` |
| **Codex** (CLI, IDE extension, ChatGPT desktop app) | `codex mcp add wealthnow --url https://mcp.wealthnow.io/mcp` |
| **Windsurf / Devin Desktop** | `devin mcp add -s user wealthnow https://mcp.wealthnow.io/mcp` |
| **Zed** | Settings → AI → MCP Servers → **Add Remote Server** ([config](#zed)) |
| **Goose**, **LM Studio** | Open the app link in [Goose](#goose) or [LM Studio](#lm-studio) |

### Claude (claude.ai, Claude Desktop, Claude mobile)

Use the **[Add Wealthnow to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Wealthnow&connectorUrl=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp)** link, which opens Claude with the name and URL filled in for you to confirm. Or by hand:
1. In Claude, open **Customize → Connectors**, click **Add**, then choose **Custom → Web** (on some plans the button reads **Add custom connector**).
2. Enter the name `Wealthnow` and the URL `https://mcp.wealthnow.io/mcp`, then click **Continue** and **Add**.
3. Click **Connect**, sign in to Wealthnow, and click **Connect** on the Wealthnow page.

A connector you add on the web also appears in Claude Desktop and on mobile. On a Team or Enterprise plan, an Owner adds it under **Organization settings → Connectors** ([or with this link](https://claude.ai/admin-settings/connectors?modal=add-custom-connector&connectorName=Wealthnow&connectorUrl=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp)), then members click **Connect**.

### Claude Code

```bash
claude mcp add --transport http --scope user wealthnow https://mcp.wealthnow.io/mcp
```

Then run `/mcp` inside Claude Code, choose **wealthnow**, and sign in. Or install it as a plugin from this repository:

```bash
/plugin marketplace add Hlobo-dev/wealthnow-mcp
/plugin install wealthnow@wealthnow
```

### ChatGPT

1. Open [chatgpt.com/plugins](https://chatgpt.com/plugins) on the web, click **+**, then **Add custom MCP server**.
2. Enter the name `Wealthnow` and the server URL `https://mcp.wealthnow.io/mcp`, and set authentication to **OAuth**.
3. Accept the risk notice, click **Create as a plugin**, install it, and sign in to Wealthnow when ChatGPT sends you there.
4. In a new chat, type `@` and pick **Wealthnow**.

Custom MCP servers depend on your ChatGPT plan, and workspace admins may control them. If your account does not show **Add custom MCP server**, turn on **Developer mode** in ChatGPT's settings first. In the ChatGPT desktop app, you can also add it under **Settings → MCP servers → Add server** as a **Streamable HTTP** server; that list is shared with Codex (see [Codex](#codex)).

### Cursor

**[Add Wealthnow to Cursor](https://cursor.com/install-mcp?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0%3D)**

The button opens Cursor with the server filled in (the same as the deeplink `cursor://anysphere.cursor-deeplink/mcp/install?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0=`). Or add this to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "wealthnow": { "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

### VS Code

**[Install in VS Code](https://vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D)** · **[Install in VS Code Insiders](https://insiders.vscode.dev/redirect/mcp/install?name=wealthnow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%7D&quality=insiders)**

Or run `code --add-mcp '{"name":"wealthnow","type":"http","url":"https://mcp.wealthnow.io/mcp"}'` (`code-insiders` for Insiders), or add this to `.vscode/mcp.json` (or your user `mcp.json`):

```json
{
  "servers": {
    "wealthnow": { "type": "http", "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

### Windsurf (now Devin Desktop)

Run `devin mcp add -s user wealthnow https://mcp.wealthnow.io/mcp`, or add this to `~/.config/devin/mcp_config.json` (macOS and Linux) or `%APPDATA%\devin\mcp_config.json` (Windows):

```json
{
  "mcpServers": {
    "wealthnow": { "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

On older Windsurf releases the file is `~/.codeium/windsurf/mcp_config.json`, and the same entry works (Windsurf also accepts `"serverUrl"` in place of `"url"`).

### Zed

Open **Settings → AI → MCP Servers → Add Server → Add Remote Server**, or add this to your settings (`~/.config/zed/settings.json`):

```json
{
  "context_servers": {
    "wealthnow": { "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

Zed opens the Wealthnow sign-in the first time it connects.

### Kiro

**[Add Wealthnow to Kiro](https://kiro.dev/launch/mcp/add?name=wealthnow&config=%7B%22url%22%3A%22https%3A%2F%2Fmcp.wealthnow.io%2Fmcp%22%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D)**

Kiro asks you to confirm, then adds the server to your user config. Or open **Kiro: Open user MCP config (JSON)** from the command palette and add:

```json
{
  "mcpServers": {
    "wealthnow": { "url": "https://mcp.wealthnow.io/mcp", "disabled": false, "autoApprove": [] }
  }
}
```

### Cline

Run `cline mcp add wealthnow https://mcp.wealthnow.io/mcp --transport http`, or open **MCP Servers → Configure** and add this to `cline_mcp_settings.json` (the `type` is required; without it Cline uses the older SSE transport):

```json
{
  "mcpServers": {
    "wealthnow": { "type": "streamableHttp", "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

### Goose

Open this link to install it in Goose Desktop (GitHub does not make app links clickable, so paste it into your browser's address bar):

```text
goose://extension?url=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp&type=streamable_http&id=wealthnow&name=Wealthnow&description=Wealthnow%20market%20data
```

Or add this to `~/.config/goose/config.yaml`:

```yaml
extensions:
  wealthnow:
    type: streamable_http
    name: Wealthnow
    enabled: true
    uri: https://mcp.wealthnow.io/mcp
    timeout: 300
```

### LM Studio

LM Studio 0.3.17 or later. Paste this link into your browser's address bar to open LM Studio with the server filled in:

```text
lmstudio://add_mcp?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0%3D
```

Or open the **Program** tab in the right sidebar, click **Install → Edit mcp.json**, and add the entry below. LM Studio's documentation shows remote servers with a header rather than a browser sign-in, so if it does not open the Wealthnow sign-in, use the API key form:

```json
{
  "mcpServers": {
    "wealthnow": {
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "YOUR_WEALTHNOW_API_KEY" }
    }
  }
}
```

### Gemini CLI

Install Wealthnow as a Gemini CLI extension from this repository:

```bash
gemini extensions install https://github.com/Hlobo-dev/wealthnow-mcp
```

Or add just the server:

```bash
gemini mcp add --scope user --transport http wealthnow https://mcp.wealthnow.io/mcp
```

Then run `/mcp auth wealthnow` inside Gemini CLI to sign in. `--scope user` saves it in `~/.gemini/settings.json` rather than the current project. By hand, the entry is `"wealthnow": { "httpUrl": "https://mcp.wealthnow.io/mcp" }` under `mcpServers` (`httpUrl`, not `url`, which means SSE).

### Codex

```bash
codex mcp add wealthnow --url https://mcp.wealthnow.io/mcp
codex mcp login wealthnow
```

Or add this to `~/.codex/config.toml`:

```toml
[mcp_servers.wealthnow]
url = "https://mcp.wealthnow.io/mcp"
```

The Codex CLI, the Codex IDE extension and the ChatGPT desktop app share this configuration, so adding it once makes Wealthnow available in all three. In the IDE extension or desktop app, click **Authenticate** next to **wealthnow** to sign in.

### Other MCP apps

Most apps that support remote MCP servers with OAuth take `https://mcp.wealthnow.io/mcp` as a remote (Streamable HTTP) server, register themselves and run the sign-in. Full sign-in has been tested end to end in Claude, ChatGPT, Grok, Cursor and Perplexity; on 2026-09-28, 70 of 72 client variants reached the Wealthnow sign-in page. OpenCode cannot finish sign-in yet because of a bug in OpenCode ([opencode#50510](https://github.com/anomalyco/opencode/issues/50510)); connect it with an API key.

### With an API key

If your app cannot sign in, or you are calling from a script, get a key from the [Wealthnow dashboard](https://app.wealthnow.io/auth/sign-up) and send it in the `X-API-Key` header. Keys start with `wn_`; older keys keep working. Keep the key in user-level settings, never in a project file that may be committed.

```json
{
  "mcpServers": {
    "wealthnow": {
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "YOUR_WEALTHNOW_API_KEY" }
    }
  }
}
```

The same `headers` object works in VS Code (with `"type": "http"`), Windsurf / Devin Desktop (with `url`), Cline, Goose and Gemini CLI (`-H "X-API-Key: ..."`). Zed skips sign-in when an `Authorization` header is set, so use `"Authorization": "Bearer YOUR_WEALTHNOW_API_KEY"` there. For Codex, set `bearer_token_env_var = "WEALTHNOW_API_KEY"` under `[mcp_servers.wealthnow]` in `~/.codex/config.toml`.

**VS Code** can prompt for the key once and store it securely:

```json
{
  "inputs": [
    { "type": "promptString", "id": "wealthnow-key", "description": "Wealthnow API key", "password": true }
  ],
  "servers": {
    "wealthnow": {
      "type": "http",
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "${input:wealthnow-key}" }
    }
  }
}
```

**OpenCode** (`~/.config/opencode/opencode.json`; the key comes from an environment variable):

```json
{
  "mcp": {
    "wealthnow": {
      "type": "remote",
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "{env:WEALTHNOW_API_KEY}" },
      "oauth": false
    }
  }
}
```

If your app only runs local servers, bridge to the remote one with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```json
{
  "mcpServers": {
    "wealthnow": {
      "command": "npx",
      "args": ["-y", "mcp-remote@0.14.2", "https://mcp.wealthnow.io/mcp",
               "--header", "X-API-Key:${WEALTHNOW_API_KEY}"],
      "env": { "WEALTHNOW_API_KEY": "YOUR_WEALTHNOW_API_KEY" }
    }
  }
}
```

---

## Tools

- **40 default tools on every plan.** Your agent's tool list holds 40 tools, including `account_status`, `search_tools` and `call_tool`; the list is the same size on Free and on paid plans.
- **The full catalog** is one call away: `search_tools` finds any tool by topic, and `call_tool` runs one that is not in the list. Your agent can call any tool your plan includes, listed or not.
- **Every tool, with its schema,** is in the [server card](https://mcp.wealthnow.io/.well-known/mcp/server-card.json). To list them all in your app, connect to `https://mcp.wealthnow.io/mcp?catalog=full`.

Market data tools are read-only; nothing places orders or moves money.

## What your agent can reach

- **Prices and fundamentals:** live prices where licensed (each labeled with its age), historical prices, income statement, balance sheet, cash flow, metrics, screener and peers, with point-in-time vintages and as-reported XBRL so backtests do not see the future.
- **SEC filings:** 10-K, 10-Q, 8-K and structured extracts.
- **Insider, institutional and congressional flows:** Form 4, Rule 10b5-1 plans, Form 144 notices, 13F holdings with quarter-over-quarter changes, and congressional trades.
- **Options:** options flow and gamma exposure, and the full chain with greeks, implied vol and open interest, replayable as it stood on any captured day.
- **Credit:** FINRA TRACE bond prints, single-name CDS, credit-rating actions and syndicated loans, keyed off the equity ticker.
- **Macro:** rates, FX, commodities and economic series.
- **Private markets:** companies, funding rounds, investors and funds, with syndicates and comparables.
- **And more:** news and sentiment, earnings-call transcripts, short interest, alternative data, crypto, and a ticker, CUSIP, ISIN and CIK crosswalk.

Try asking your agent:
- "Using Wealthnow, is the bond market more worried about Boeing than the stock market is?"
- "Using Wealthnow, which members of Congress traded NVDA this year, and what did insiders do?"
- "Using Wealthnow, what did NVDA's options chain look like the day before its last earnings?"

The Free plan covers prices, fundamentals and SEC filings. Credit, private markets and options history are on paid plans. Failed calls are never charged. [Pricing](https://app.wealthnow.io/docs/pricing-and-credits) · [Get a free account](https://wealthnow.io/register?next=api&utm_source=github&utm_medium=readme&utm_campaign=api_launch_202610)


---

## Try it

Once connected, ask your agent:

> Using Wealthnow, what's the latest quote for AAPL?

Or call it directly with an API key:

```bash
curl -s -X POST https://mcp.wealthnow.io/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H "X-API-Key: $WEALTHNOW_API_KEY" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call",
       "params":{"name":"fundamentals_price_snapshot","arguments":{"ticker":"AAPL"}}}'
```

More in [`examples/`](./examples): a [quickstart](./examples/quickstart.md), [Python](./examples/list_tools.py) and [TypeScript](./examples/snapshot.ts).

## SDKs

Clients for the REST API, with every operation callable by the same name the MCP server uses for the tool:

```bash
pip install wealthnow   # Python, see sdks/python
npm i wealthnow         # TypeScript / JavaScript, see sdks/typescript
```

## Discovery

- MCP server card: https://mcp.wealthnow.io/.well-known/mcp/server-card.json
- OAuth protected resource metadata: https://mcp.wealthnow.io/.well-known/oauth-protected-resource
- REST API (OpenAPI 3.1): https://firm.wealthnow.io/api/openapi.json
- MCP Registry entry: [`io.wealthnow/mcp`](https://registry.modelcontextprotocol.io/v0.1/servers/io.wealthnow%2Fmcp/versions/latest), published from [`server.json`](./server.json) on every release tag

## Links

- Product: https://wealthnow.io/api
- Docs: https://app.wealthnow.io/docs/mcp-and-sdks
- Sign up: https://app.wealthnow.io/auth/sign-up
- Pricing: https://app.wealthnow.io/docs/pricing-and-credits
- Privacy: https://wealthnow.io/privacy
- Terms: https://wealthnow.io/terms
- Support: hello@wealthnow.io
- Security: see [SECURITY.md](./SECURITY.md)

## License

The examples, SDKs and listing files in this repository are MIT licensed; see [LICENSE](./LICENSE). The Wealthnow API and MCP server are a commercial service covered by the [Wealthnow terms](https://wealthnow.io/terms); the MIT license does not grant access to them.

## Disclosure

Wealthnow is not a broker-dealer or a registered investment adviser. Wealthnow provides data for research and education only. Nothing it returns is investment, tax or legal advice, or a recommendation to buy or sell any security. Data can be delayed, incomplete or wrong; verify it before you rely on it.
