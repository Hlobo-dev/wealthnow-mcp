# Quickstart: call Wealthnow in 60 seconds

AI apps such as Claude, ChatGPT and Cursor sign in with OAuth and need no key; see the [README](../README.md#connect). For scripts, create a free API key in the [Wealthnow dashboard](https://app.wealthnow.io/auth/sign-up) (no card needed), then:

```bash
export TENGU_API_KEY=...
```

## 1. Browse the tool catalogue (no key needed)

```bash
curl -s https://mcp.wealthnow.io/.well-known/mcp/server-card.json | jq '.tools | length'
```

## 2. List the tools your plan can call

```bash
curl -s -X POST https://mcp.wealthnow.io/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H "X-API-Key: $TENGU_API_KEY" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq '.result.tools[].name'
```

## 3. Call a tool

```bash
curl -s -X POST https://mcp.wealthnow.io/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H "X-API-Key: $TENGU_API_KEY" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call",
       "params":{"name":"fundamentals_price_snapshot","arguments":{"ticker":"AAPL"}}}' | jq .
```

## 4. Or call the REST API directly (same key, same credits)

```bash
curl -s https://firm.wealthnow.io/api/market/quote/AAPL -H "X-API-Key: $TENGU_API_KEY" | jq .
```

Language examples: [`list_tools.py`](./list_tools.py) and [`snapshot.ts`](./snapshot.ts).
