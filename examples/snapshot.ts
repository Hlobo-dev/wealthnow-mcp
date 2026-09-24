/**
 * Call a Wealthnow tool over MCP (JSON-RPC tools/call).
 * Run: WEALTHNOW_API_KEY=... bun run snapshot.ts  (or: npx tsx snapshot.ts)
 */
const MCP = "https://mcp.wealthnow.io/mcp";

type RpcResponse = { result?: any; error?: { code: number; message: string } };

async function rpc(method: string, params: unknown, apiKey: string): Promise<RpcResponse> {
  const res = await fetch(MCP, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json, text/event-stream",
      "X-API-Key": apiKey,
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }),
  });
  const raw = await res.text();
  // The server may answer as JSON or as a single server-sent event.
  const event = raw.split("\n").find((line) => line.startsWith("data: "));
  return JSON.parse(event ? event.slice("data: ".length) : raw);
}

// Wrapped in main(): with no package.json, tsx compiles this file as CommonJS,
// which has no top-level await.
async function main(): Promise<void> {
  const key = process.env.WEALTHNOW_API_KEY;
  if (!key) {
    console.log("Set WEALTHNOW_API_KEY (free at https://app.wealthnow.io/auth/sign-up) to call a tool.");
  } else {
    const list = await rpc("tools/list", {}, key);
    console.log(`The default list shows ${list.result?.tools?.length ?? 0} Wealthnow tools (add ?catalog=full to the URL for all).`);
    const out = await rpc(
      "tools/call",
      { name: "fundamentals_price_snapshot", arguments: { ticker: "AAPL" } },
      key,
    );
    console.log("fundamentals_price_snapshot(AAPL) ->", JSON.stringify(out.result ?? out).slice(0, 600));
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
