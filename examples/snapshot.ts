/**
 * Call a Tengu FIRM tool over MCP (JSON-RPC tools/call).
 * Run: TENGU_API_KEY=... bun run snapshot.ts  (or: npx tsx snapshot.ts)
 */
const MCP = "https://firm.tengu.co/mcp";

async function rpc(method: string, params: unknown = {}, apiKey?: string) {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    Accept: "application/json, text/event-stream",
  };
  if (apiKey) headers["X-API-Key"] = apiKey;
  const res = await fetch(MCP, {
    method: "POST",
    headers,
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }),
  });
  return res.json();
}

const key = process.env.TENGU_API_KEY;
const list: any = await rpc("tools/list");
console.log(`Tengu FIRM exposes ${list.result.tools.length} tools.`);

if (!key) {
  console.log("Set TENGU_API_KEY (free at https://tengu.co/api) to call a tool.");
} else {
  const out: any = await rpc(
    "tools/call",
    { name: "tengu_snapshot", arguments: { ticker: "AAPL" } },
    key,
  );
  console.log("tengu_snapshot(AAPL) ->", JSON.stringify(out.result ?? out).slice(0, 600));
}
