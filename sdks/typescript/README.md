# wealthnow (TypeScript / JavaScript)

Client for the [Wealthnow API](https://wealthnow.io/api): real-time (where licensed) and historical stock and crypto prices, fundamentals, SEC filings, insider and 13F data, congress trades, news and macro. Zero dependencies, ESM and CommonJS, Node 18+ (uses the built-in fetch).

```bash
npm i wealthnow
```

Get a free key (1,000 credits a month, no card): https://wealthnow.io/register?next=api

```ts
import { Wealthnow } from "wealthnow";

const wn = new Wealthnow(); // reads WEALTHNOW_API_KEY, or new Wealthnow({ apiKey: "wn_..." })

const { snapshot } = await wn.priceSnapshot("AAPL");
console.log(snapshot.price, snapshot.as_of);

await wn.fundamentals("MSFT");
await wn.cryptoQuote("BTC");
console.log(wn.lastCredits); // { cost, remaining }
```

## Every endpoint by name

Each operation in the [OpenAPI spec](https://firm.wealthnow.io/api/openapi.json) is callable by its operationId, the same name the Wealthnow MCP server uses for the tool:

```ts
await wn.call("fundamentals_full", { ticker: "NVDA" });
wn.searchOperations("13f");                       // find operation names
wn.operations["fundamentals_full"].min_plan;      // cheapest plan that can call it
await wn.get("/api/v3/fundamentals/price_snapshot", { ticker: "AAPL" }); // any path
```

Discovery endpoints need no key: `wn.capabilities()`, `wn.openapi()`.

## Errors and retries

Failed calls throw `WealthnowError` with `status`, `code`, `message` and `requestId`. The client retries 429, 502 and retryable 503 responses up to `maxRetries` times (default 2), honouring `Retry-After` up to 120 seconds. Failed calls are never charged.

## Options

| Option | Default |
|---|---|
| `apiKey` | `WEALTHNOW_API_KEY` env var |
| `baseUrl` | `https://firm.wealthnow.io` (or `WEALTHNOW_BASE_URL`) |
| `timeoutMs` | 30000 |
| `maxRetries` | 2 |
| `fetch` | `globalThis.fetch` |

Keep your key on the server. Do not ship it in browser code.

## Plans

Free covers market data, fundamentals and SEC filings. Starter ($99), Pro ($499) and Expert ($999) add more data products. See [pricing and credits](https://app.wealthnow.io/docs/pricing-and-credits).

## Using an AI agent instead?

Point any MCP client at `https://mcp.wealthnow.io/mcp` and every endpoint becomes a tool. Setup: https://wealthnow.io/mcp

Data and structured signals, not investment advice.
