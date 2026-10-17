# Security policy

## Reporting a vulnerability

Email **hello@wealthnow.io** with "Security" in the subject line. Please include:

- what you found and where (the MCP server at `https://mcp.wealthnow.io/mcp`, the REST API, the dashboard, the SDKs, or this repository);
- steps to reproduce, and the impact you believe it has;
- whether you would like to be credited.

Please do not open a public issue for a security problem, and do not include live API keys or other people's data in your report. We aim to acknowledge reports within three business days and will keep you updated until the issue is resolved.

## Scope

In scope: the hosted Wealthnow MCP server, its OAuth sign-in, the Wealthnow REST API, and the code in this repository (examples, plugin manifests and SDKs).

Out of scope: denial-of-service and volumetric testing, social engineering, and findings in third-party AI apps that connect to Wealthnow (report those to the app's vendor).

## Keys

If you believe a Wealthnow API key has leaked, rotate it in the [dashboard](https://app.wealthnow.io) and tell us at the address above.
