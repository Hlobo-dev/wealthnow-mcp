# Wealthnow MCP server

**Market data, fundamentals, SEC filings, insider, 13F and congressional trades, and private markets for AI agents.**

Wealthnow is a hosted [Model Context Protocol](https://modelcontextprotocol.io) server. Add one URL to your AI app, sign in to Wealthnow, and your agent can call financial data tools directly.

| | |
|---|---|
| **Endpoint** | `https://mcp.wealthnow.io/mcp` |
| **Transport** | Streamable HTTP |
| **Sign-in** | OAuth 2.1. Your AI app opens Wealthnow's sign-in page and returns you connected, with no key to copy. |
| **API key** | Optional, for scripts and apps without OAuth: send it in the `X-API-Key` header. |
| **Registry** | [`io.wealthnow/mcp`](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.wealthnow/mcp) in the official MCP Registry |
| **Free plan** | 1,000 credits a month, no card needed. Connecting from an AI app starts it for you. |

Every tool is read-only. Which tools you see depends on your plan:
- **Free:** market data, fundamentals and SEC filings.
- **Paid plans:** the full catalogue, which is listed in the [server card](https://mcp.wealthnow.io/.well-known/mcp/server-card.json).

*Data and structured signals, not investment advice.*

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

### Other MCP apps

In most apps that support remote MCP servers with OAuth, you add `https://mcp.wealthnow.io/mcp` as a remote (Streamable HTTP) server, and the app registers itself and runs the sign-in. We have checked this with:
- Grok, Perplexity and Devin
- Cline, Kiro, Amp and LM Studio
- Warp's terminal, Postman, Slack and Figma

**Not working yet.** Sign-in from these apps is still being enabled on our side. Until then, connect them with an API key:
- **VS Code, Zed, GitHub Copilot CLI and Goose:** they identify themselves with a client metadata document.
- **Gemini CLI 0.60 and later:** it requires an `iss` parameter on the sign-in response.

Zed skips sign-in when you set the `Authorization: Bearer YOUR_TENGU_API_KEY` header; the server accepts the key there as well as in `X-API-Key`.

### With an API key

Get a key from the [Wealthnow dashboard](https://app.wealthnow.io/auth/sign-up) and send it in the `X-API-Key` header. This works in any client that lets you set headers:

```json
{
  "mcpServers": {
    "wealthnow": {
      "url": "https://mcp.wealthnow.io/mcp",
      "headers": { "X-API-Key": "YOUR_TENGU_API_KEY" }
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
               "--header", "X-API-Key:${TENGU_API_KEY}"],
      "env": { "TENGU_API_KEY": "YOUR_TENGU_API_KEY" }
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
  -H "X-API-Key: $TENGU_API_KEY" \
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
- Pricing: https://wealthnow.io/pricing
- Privacy: https://wealthnow.io/privacy
- Terms: https://wealthnow.io/terms
- Support: hello@wealthnow.io

## License

The examples and listing files in this repository are MIT licensed; see [LICENSE](./LICENSE). The Wealthnow service is covered by its [terms](https://wealthnow.io/terms). "Wealthnow" is a mark of Tengu LLC.
