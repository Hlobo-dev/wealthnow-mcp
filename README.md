# Tengu FIRM — MCP Server

**One API key. 336 market & quant data tools. Built for AI agents.**

Tengu FIRM is a **hosted [Model Context Protocol](https://modelcontextprotocol.io) server**
that exposes real-time and historical market data, SEC filings, insider/institutional/
congressional trades, fundamentals, quant signals, cited verdicts, private markets, and
macro data — as native agent tools over **MCP Streamable HTTP**.

- **Endpoint:** `https://firm.tengu.co/mcp`
- **Transport:** MCP Streamable HTTP (JSON-RPC 2.0) — `initialize`, `tools/list`, `tools/call`
- **Auth:** send your key as the `X-API-Key` header (or `Authorization: Bearer <key>`)
- **Server:** `tengu-firm` · manifest `2.114`
- **Get a key (free, no card):** https://tengu.co/api

Every `tools/call` proxies to a `firm.tengu.co` REST endpoint, so tier gating and credit
metering apply exactly as on REST. *Data and structured signals — not investment advice.*

---

## Connect

### claude.ai (recommended for a hosted server)
Settings → **Connectors** → **Add custom connector** → URL `https://firm.tengu.co/mcp`,
and set the **`X-API-Key`** header to your key.

### Claude Desktop / Cursor (via `mcp-remote`)
Desktop clients launch MCP servers as local processes, so bridge to the remote endpoint
with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```json
{
  "mcpServers": {
    "tengu-firm": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://firm.tengu.co/mcp",
               "--header", "X-API-Key:YOUR_TENGU_API_KEY"]
    }
  }
}
```

### Any remote-capable MCP client
```json
{
  "mcpServers": {
    "tengu-firm": {
      "url": "https://firm.tengu.co/mcp",
      "headers": { "X-API-Key": "YOUR_TENGU_API_KEY" }
    }
  }
}
```

### Verify it's reachable
```bash
curl -s -X POST https://firm.tengu.co/mcp \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: YOUR_TENGU_API_KEY' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq '.result.tools | length'
```

---

## Tool catalogue

Live discovery (no auth required):
- Capabilities: `https://firm.tengu.co/api/capabilities`
- OpenAPI 3.1: `https://firm.tengu.co/api/openapi.json`

| Group | Prefix | Count | Surface |
|------|--------|------:|---------|
| legacy | `tengu_*` | 10 | EC2-compat core data |
| v2 | `tengu_v2_*` | 15 | FIRM upgrades |
| v3 | `tengu_v3_*` | 301 | Expert: agents, decision, execution, strategies, memory, lab |
| copilot | `tengu_copilot_*` | 20 | Chat-copilot aggregations |
| ml | `tengu_ml_*` | 5 | Direct ML model surface |

**Example tools**
- `tengu_snapshot` — live price snapshot for a ticker
- `tengu_crypto` — real-time crypto quote (439 pairs)
- `tengu_insider_clusters` — companies where multiple insiders bought around the same time
- `tengu_v3_fundamentals_full` — full fundamentals (income, balance sheet, cash flow, 100+ metrics)

**Data surfaces:** real-time + 30yr OHLCV (stocks & crypto) · 100+ fundamentals · SEC
filings (10-K/10-Q/8-K) · insider trades (Form 4) · institutional holdings (13F) ·
congressional trades (STOCK Act) · news sentiment (57 sources) · quant factor scores ·
cited verdicts · private markets (10.5M companies / 3M deals / 646K investors) · macro
(CPI, rates, employment).

---

## Pricing

| Tier | Price | Credits / mo | Rate limit |
|------|------:|-------------:|-----------:|
| Free | $0 | 1,000 | 30 req/min |
| Starter | $99 | 250,000 | 120 req/min |
| Pro | $499 | 2,000,000 | 600 req/min |
| Expert | $999 | 5,000,000 | 1,200 req/min |

Start free (no card): **https://tengu.co/api**

## Links
- Homepage: https://tengu.co/api
- Capabilities: https://firm.tengu.co/api/capabilities
- OpenAPI: https://firm.tengu.co/api/openapi.json

## License
MIT — see [LICENSE](./LICENSE). "Tengu" and "FIRM" are marks of Tengu, Inc.
