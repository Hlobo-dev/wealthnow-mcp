# Quickstart — call Tengu FIRM in 60 seconds

Get a free key (no card): https://tengu.co/api → then `export TENGU_API_KEY=...`

## 1. List the tool catalogue (no key needed — public discovery)
```bash
curl -s -X POST https://firm.tengu.co/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq '.result.tools | length'
```

## 2. Call a tool over MCP (JSON-RPC `tools/call`)
```bash
curl -s -X POST https://firm.tengu.co/mcp \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: $TENGU_API_KEY" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call",
       "params":{"name":"tengu_snapshot","arguments":{"ticker":"AAPL"}}}' | jq .
```

## 3. Or hit the REST endpoint directly (same auth, same metering)
```bash
curl -s https://firm.tengu.co/api/snapshot/AAPL -H "X-API-Key: $TENGU_API_KEY" | jq .
```

Language examples: [`list_tools.py`](./list_tools.py) · [`snapshot.ts`](./snapshot.ts)
