# wealthnow (Python)

Python client for the [Wealthnow API](https://wealthnow.io/api): real-time (where licensed) and historical stock and crypto prices, fundamentals, SEC filings, insider and 13F data, congress trades, news and macro. One API key, plain JSON, no dependencies.

```bash
pip install wealthnow
```

Get a free key (1,000 credits a month, no card): https://wealthnow.io/register?next=api

```python
from wealthnow import Wealthnow

wn = Wealthnow()  # reads WEALTHNOW_API_KEY, or Wealthnow(api_key="wn_...")

snap = wn.price_snapshot("AAPL")["snapshot"]
print(snap["price"], snap["as_of"])

print(wn.fundamentals("MSFT"))       # statements and key metrics
print(wn.crypto_quote("BTC"))
print(wn.last_credits)               # {"cost": ..., "remaining": ...}
```

## Every endpoint by name

Each operation in the [OpenAPI spec](https://firm.wealthnow.io/api/openapi.json) is callable by its operationId, the same name the Wealthnow MCP server uses for the tool:

```python
wn.call("fundamentals_full", ticker="NVDA")
wn.op.insider_clusters(limit=20)               # same thing, attribute style
wn.search_operations("13f")                    # find operation names
wn.operations["fundamentals_full"]["min_plan"] # cheapest plan that can call it
wn.get("/api/v3/fundamentals/price_snapshot", ticker="AAPL")  # any path
```

Discovery endpoints need no key: `wn.capabilities()`, `wn.openapi()`.

## Errors and retries

Failed calls raise `WealthnowError` with `status`, `code`, `message` and `request_id`. The client retries 429, 502 and retryable 503 responses up to `max_retries` times (default 2), honouring `Retry-After` up to 120 seconds. Failed calls are never charged.

## Configuration

| Option | Default |
|---|---|
| `api_key` | `WEALTHNOW_API_KEY` env var |
| `base_url` | `https://firm.wealthnow.io` (or `WEALTHNOW_BASE_URL`) |
| `timeout` | 30 seconds |
| `max_retries` | 2 |

## Plans

Free covers market data, fundamentals and SEC filings. Starter ($99), Pro ($499) and Expert ($999) add more data products. See [pricing and credits](https://app.wealthnow.io/docs/pricing-and-credits).

## Using an AI agent instead?

Point any MCP client at `https://mcp.wealthnow.io/mcp` and every endpoint becomes a tool. Setup: https://wealthnow.io/mcp

Data and structured signals, not investment advice.
