# Wealthnow MCP server

**Institutional financial data for AI agents: corporate bond prints and CDS spreads, a 10.6M-company private-markets graph, replayable options-chain history, 13F and insider flows, transcripts, and point-in-time fundamentals. 276 read-only tools, one sign-in.**

Wealthnow is a hosted [Model Context Protocol](https://modelcontextprotocol.io) server. Add one URL to your AI app, sign in to Wealthnow, and your agent can call financial data tools directly.

| | |
|---|---|
| **Endpoint** | `https://mcp.wealthnow.io/mcp` |
| **Transport** | Streamable HTTP |
| **Sign-in** | OAuth 2.1. Your AI app opens Wealthnow's sign-in page and returns you connected, with no key to copy. |
| **API key** | Optional, for scripts and apps without OAuth: send it in the `X-API-Key` header. |
| **Registry** | [`io.wealthnow/mcp`](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.wealthnow/mcp) in the official MCP Registry |
| **Free plan** | 1,000 credits a month, no card needed. Connecting from an AI app starts it for you. |

Every tool is read-only.
- **Default list:** your agent first sees `account_status` and up to 12 starter tools.
- **Full catalogue:** connect to `https://mcp.wealthnow.io/mcp?catalog=full` to list every public tool. The same list is in the [server card](https://mcp.wealthnow.io/.well-known/mcp/server-card.json).
- **Plans:** your agent can call any tool your plan includes, whether or not it is listed. The Free plan covers market data, fundamentals and SEC filings.

*Data and structured signals, not investment advice.*

## What your agent can reach

Most finance MCP servers stop at quotes and statements. Wealthnow exposes data that desks usually get through a terminal contract:

- **Corporate credit:** FINRA TRACE bond prints, 21.8M daily single-name CDS observations back to 2005, 15.8M credit-rating actions, and syndicated loans with pricing and covenants, keyed off the equity ticker.
- **Private markets:** 10.6M companies, 3M deals, 4.9M people, 645k investors and funds with IRR, DPI and TVPI, and 100k+ limited partners, with round-by-round syndicates, comparables and a valuation mark.
- **Options chain history and tape:** the entire chain with greeks, implied vol and open interest for every trading day captured since May 2026, replayable exactly as it stood, plus per-print options and futures trades and minute bars for about 10.5k tickers.
- **Transcripts and events:** 1.75M earnings-call transcript versions and 41.9M dated corporate events back to 1990.
- **Institutional and insider flows:** 13F holdings with quarter-over-quarter changes, a 308M-row mutual-fund holdings archive, Form 4, Rule 10b5-1 plans, Form 144 notices, insider buying clusters and congressional trades.
- **Fundamentals done right:** point-in-time vintages, as-reported XBRL, business segments and survivorship-bias-free prices, so backtests do not see the future.
- **And more:** options flow and gamma exposure, short interest and borrow cost, alternative data (WARN layoffs, supply-chain dependence, forensic accounting flags, lobbying, contracts, patents), news sentiment back to 2000, macro and rates, crypto, and a point-in-time ticker, CUSIP, ISIN and CIK crosswalk.

Try asking your agent:
- "Using Wealthnow, is the bond market more worried about Boeing than the stock market is?"
- "Using Wealthnow, who led each funding round for this startup, and what are its closest private peers?"
- "Using Wealthnow, what did NVDA's options chain look like the day before its last earnings?"

The Free plan (1,000 credits a month) covers prices, fundamentals and SEC filings. Credit, private markets and options history are on the Pro plan. Failed calls are never charged. [Pricing](https://app.wealthnow.io/docs/pricing-and-credits) · [Get a free key](https://wealthnow.io/register?next=api&utm_source=github&utm_medium=readme&utm_campaign=api_launch_202609)


---

## Connect

### Claude (claude.ai, Claude Desktop, Claude mobile)

**[Add Wealthnow to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Wealthnow&connectorUrl=https%3A%2F%2Fmcp.wealthnow.io%2Fmcp)**

To add it by hand instead:
1. In Claude, open **Settings → Connectors → Add custom connector**.
2. Enter the name `Wealthnow` and the URL `https://mcp.wealthnow.io/mcp`.
3. Click **Connect**, sign in to Wealthnow, then click **Connect** on the Wealthnow page.

A connector you add on the web also appears in Claude Desktop and on mobile.

### Claude Code

```bash
claude mcp add --transport http wealthnow https://mcp.wealthnow.io/mcp
```

Then run `/mcp` inside Claude Code, choose **wealthnow**, and sign in.

Or install it as a plugin from this repository:

```bash
/plugin marketplace add Hlobo-dev/wealthnow-mcp
/plugin install wealthnow@wealthnow
```

### ChatGPT

1. Open ChatGPT on the web and go to **Settings → Apps**. Some accounts label this **Apps & Connectors** or **Connectors**.
2. Open **Advanced settings** and turn on **Developer mode**.
3. Back on **Apps**, click **Create**.
4. Enter the URL `https://mcp.wealthnow.io/mcp` and choose **OAuth**.
5. Sign in to Wealthnow when ChatGPT sends you there.

### Cursor

**[Add Wealthnow to Cursor](https://cursor.com/en/install-mcp?name=wealthnow&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWFsdGhub3cuaW8vbWNwIn0%3D)**

Or add this to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "wealthnow": { "url": "https://mcp.wealthnow.io/mcp" }
  }
}
```

The first time you use it, Cursor asks you to sign in to Wealthnow.

### Codex

```bash
codex mcp add wealthnow --url https://mcp.wealthnow.io/mcp
codex mcp login wealthnow
```

`codex mcp login` opens the Wealthnow sign-in in your browser. To use an API key instead, set `bearer_token_env_var = "WEALTHNOW_API_KEY"` under `[mcp_servers.wealthnow]` in `~/.codex/config.toml`.

### Other MCP apps

In most apps that support remote MCP servers with OAuth, you add `https://mcp.wealthnow.io/mcp` as a remote (Streamable HTTP) server, and the app registers itself and runs the sign-in.
- **Full sign-in tested end to end** (sign in, back in the app, tools listed): Claude, ChatGPT, Grok, Cursor and Perplexity.
- **Checked to reach the Wealthnow sign-in page (2026-09-28, 70 of 72 client variants):** VS Code, Zed, GitHub Copilot CLI and the Copilot desktop app, Codex, Goose, Devin Desktop (formerly Windsurf), Warp, Continue, Cline, Raycast, the Code tab in Claude Desktop, Devin, Cline, Kiro, Amp, LM Studio, Postman, Slack and Figma. The steps after sign-in are the same as for the apps above.
- **Gemini CLI 0.60 and later** requires an `iss` parameter on the sign-in response; Wealthnow sends it. We have not yet run a Gemini CLI sign-in end to end.
- **OpenCode** cannot finish sign-in yet because of a bug in OpenCode ([opencode#50510](https://github.com/anomalyco/opencode/issues/50510)). Connect it with an API key (below).
- **Devin Desktop** (formerly Windsurf) and **Warp** refused the sign-in until 2026-09-28: their clients drop the `iss` parameter and report it missing ([devin-cli#5](https://github.com/CognitionAI/devin-cli/issues/5)). The server no longer asks clients to require it (it still sends it), so their sign-in is no longer refused for that reason. A key (below) also works.

**If sign-in fails in your app**, connect it with an API key instead:

Keep the key in your user-level settings, never in a project file that may be committed to a repository.

**VS Code** (`.vscode/mcp.json`): VS Code prompts for the key once and stores it securely.

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "wealthnow-key",
      "description": "Wealthnow API key",
      "password": true
    }
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

**Gemini CLI** (`-s user` saves it in `~/.gemini/settings.json`; without it the key is written into the current project's `.gemini/settings.json`):

```bash
gemini mcp add -s user --transport http wealthnow https://mcp.wealthnow.io/mcp -H "X-API-Key: YOUR_WEALTHNOW_API_KEY"
```

**Goose** (`~/.config/goose/config.yaml`):

```yaml
extensions:
  wealthnow:
    type: streamable_http
    name: wealthnow
    enabled: true
    uri: https://mcp.wealthnow.io/mcp
    headers:
      X-API-Key: YOUR_WEALTHNOW_API_KEY
    timeout: 300
```

**OpenCode** (your global config, `~/.config/opencode/opencode.json`; the key comes from an environment variable):

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

Devin Desktop and Warp sign in on their own; a key also works, for example on a machine without a browser.

**Devin Desktop** (formerly Windsurf; `~/.config/devin/mcp_config.json` on macOS and Linux, `%APPDATA%\devin\mcp_config.json` on Windows; the key comes from an environment variable):

```json
{
  "mcpServers": {
    "wealthnow": {
      "serverUrl": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "${env:WEALTHNOW_API_KEY}" }
    }
  }
}
```

**Warp** (Settings → Agents → MCP servers, then add a server):

```json
{
  "wealthnow": {
    "url": "https://mcp.wealthnow.io/mcp",
    "headers": { "X-API-Key": "YOUR_WEALTHNOW_API_KEY" }
  }
}
```

VS Code and Zed sign in on their own; a key also works, for example on a machine without a browser.

**Zed** (your user settings, `~/.config/zed/settings.json`): Zed skips sign-in when an `Authorization` header is set, and the server accepts the key as a bearer token.

```json
{
  "context_servers": {
    "wealthnow": {
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_WEALTHNOW_API_KEY" }
    }
  }
}
```

### With an API key

Get a key from the [Wealthnow dashboard](https://app.wealthnow.io/auth/sign-up) and send it in the `X-API-Key` header. This works in any client that lets you set headers:

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

## What it covers

- Real-time and historical prices for stocks and crypto
- Fundamentals: income statement, balance sheet, cash flow, metrics, screener and peers
- SEC filings: 10-K, 10-Q, 8-K and structured extracts
- Insider trades (Form 4), institutional holdings (13F) and congressional trades
- News and sentiment, macro, rates, FX and commodities
- Options flow, alternative data and private markets (companies, deals, investors)

## Discovery

- MCP server card: https://mcp.wealthnow.io/.well-known/mcp/server-card.json
- OAuth protected resource metadata: https://mcp.wealthnow.io/.well-known/oauth-protected-resource
- REST API (OpenAPI 3.1): https://firm.wealthnow.io/api/openapi.json

## Links

- Product: https://wealthnow.io/api
- Docs: https://app.wealthnow.io/docs/mcp-and-sdks
- Sign up: https://app.wealthnow.io/auth/sign-up
- Pricing: https://app.wealthnow.io/docs/pricing-and-credits
- Privacy: https://wealthnow.io/privacy
- Terms: https://wealthnow.io/terms
- Support: hello@wealthnow.io

## License

The examples and listing files in this repository are MIT licensed; see [LICENSE](./LICENSE). The Wealthnow service is covered by its [terms](https://wealthnow.io/terms). "Wealthnow" is a mark of Tengu LLC.
