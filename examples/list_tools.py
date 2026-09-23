#!/usr/bin/env python3
"""Browse the Wealthnow MCP tool catalogue (public, no key needed), then list
and call tools with TENGU_API_KEY if it is set. Stdlib only.

    python3 list_tools.py
"""
import json
import os
import urllib.request

MCP = "https://mcp.wealthnow.io/mcp"
SERVER_CARD = "https://mcp.wealthnow.io/.well-known/mcp/server-card.json"


def get_json(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read())


def rpc(method, params, api_key):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                       "params": params}).encode()
    headers = {"Content-Type": "application/json",
               "Accept": "application/json, text/event-stream",
               "X-API-Key": api_key}
    req = urllib.request.Request(MCP, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode()
    # The server may answer as JSON or as a single server-sent event.
    for line in raw.splitlines():
        if line.startswith("data: "):
            return json.loads(line[len("data: "):])
    return json.loads(raw)


def main():
    card = get_json(SERVER_CARD)
    print(f"Wealthnow catalogue: {len(card['tools'])} tools across all plans.")

    key = os.environ.get("TENGU_API_KEY")
    if not key:
        print("\nSet TENGU_API_KEY (free at https://app.wealthnow.io/auth/sign-up) "
              "to list and call the tools your plan includes.")
        return

    tools = rpc("tools/list", {}, key)["result"]["tools"]
    print(f"\nYour plan can call {len(tools)} tools. First 10:")
    for t in tools[:10]:
        print(f"  - {t['name']}: {t.get('description', '')[:70]}")

    out = rpc("tools/call", {"name": "fundamentals_price_snapshot",
                             "arguments": {"ticker": "AAPL"}}, key)
    print("\nfundamentals_price_snapshot(AAPL) ->")
    print(json.dumps(out.get("result", out), indent=2)[:600])


if __name__ == "__main__":
    main()
