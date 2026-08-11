#!/usr/bin/env python3
"""List the Tengu FIRM MCP tool catalogue (public discovery, no key needed)
and call one tool if TENGU_API_KEY is set. Stdlib only.

    python3 list_tools.py
"""
import json
import os
import urllib.request

MCP = "https://firm.tengu.co/mcp"


def rpc(method, params=None, api_key=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                       "params": params or {}}).encode()
    headers = {"Content-Type": "application/json",
               "Accept": "application/json, text/event-stream"}
    if api_key:
        headers["X-API-Key"] = api_key
    req = urllib.request.Request(MCP, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def main():
    tools = rpc("tools/list")["result"]["tools"]
    print(f"Tengu FIRM exposes {len(tools)} tools. First 10:")
    for t in tools[:10]:
        print(f"  - {t['name']}: {t.get('description','')[:70]}")

    key = os.environ.get("TENGU_API_KEY")
    if not key:
        print("\nSet TENGU_API_KEY (free at https://tengu.co/api) to call a tool.")
        return
    out = rpc("tools/call",
              {"name": "tengu_snapshot", "arguments": {"ticker": "AAPL"}}, key)
    print("\ntengu_snapshot(AAPL) ->")
    print(json.dumps(out.get("result", out), indent=2)[:600])


if __name__ == "__main__":
    main()
