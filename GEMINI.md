# Wealthnow

Wealthnow tools return institutional financial data. Every tool only reads data; none places orders or moves money.

- Sign in with your Wealthnow account when Gemini CLI opens the OAuth window, or set an API key header in settings.json if you script it.
- Start with search_tools when you are not sure which tool fits; it searches the whole catalogue.
- Good first calls: credit_snapshot (credit risk for a ticker), private_markets_search (resolve a private company), transcripts_search (earnings calls), intel_sec13f (fund holdings), tape_options_chain (historical options chains).
- Answers carry as-of dates. Say when data is stale or unavailable instead of guessing. Data only, not investment advice.
