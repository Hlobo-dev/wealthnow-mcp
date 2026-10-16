"""A small, dependency-free client for the Wealthnow REST API.

Every endpoint in the public OpenAPI spec (https://firm.wealthnow.io/api/openapi.json)
is reachable by its operationId through ``Wealthnow.call`` or ``client.op.<name>``.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from importlib import resources
from typing import Any, Dict, List, Optional

__version__ = "0.1.0"

DEFAULT_BASE_URL = "https://firm.wealthnow.io"
_RETRYABLE = {429, 502, 503}
_MAX_RETRY_AFTER = 120.0


class WealthnowError(Exception):
    """An API call failed. ``status`` is the HTTP status (0 for network errors)."""

    def __init__(self, status: int, code: str, message: str,
                 request_id: Optional[str] = None, body: Any = None):
        super().__init__(f"{status} {code}: {message}")
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.body = body


def _load_operations() -> Dict[str, Any]:
    raw = resources.files("wealthnow").joinpath("_operations.json").read_text("utf-8")
    return json.loads(raw)


class _Ops:
    """Attribute access to operations: ``client.op.fundamentals_full(ticker="AAPL")``."""

    def __init__(self, client: "Wealthnow"):
        self._client = client

    def __getattr__(self, name: str):
        if name.startswith("_") or name not in self._client.operations:
            raise AttributeError(f"unknown Wealthnow operation: {name}")
        return lambda **params: self._client.call(name, **params)

    def __dir__(self):
        return sorted(self._client.operations)


class Wealthnow:
    """Client for the Wealthnow API.

    >>> from wealthnow import Wealthnow
    >>> wn = Wealthnow()                      # reads WEALTHNOW_API_KEY
    >>> wn.price_snapshot("AAPL")["snapshot"]["price"]
    """

    def __init__(self, api_key: Optional[str] = None, *, base_url: Optional[str] = None,
                 timeout: float = 30.0, max_retries: int = 2):
        self.api_key = api_key if api_key is not None else os.environ.get("WEALTHNOW_API_KEY")
        self.base_url = (base_url or os.environ.get("WEALTHNOW_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        index = _load_operations()
        self.spec_version: str = index["spec_version"]
        self.operations: Dict[str, Dict[str, Any]] = index["operations"]
        self.op = _Ops(self)
        #: Credit headers from the last successful call: {"cost": ..., "remaining": ...}
        self.last_credits: Dict[str, Optional[str]] = {}
        #: X-Request-ID of the last call, for support requests.
        self.last_request_id: Optional[str] = None

    def __repr__(self) -> str:
        return f"Wealthnow(base_url={self.base_url!r}, api_key={'set' if self.api_key else 'unset'})"

    # Low level -----------------------------------------------------------

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None,
                body: Any = None, auth: bool = True) -> Any:
        """Send one request and return the decoded JSON body."""
        query = {k: (",".join(map(str, v)) if isinstance(v, (list, tuple)) else v)
                 for k, v in (params or {}).items() if v is not None}
        url = self.base_url + path + (("?" + urllib.parse.urlencode(query, doseq=True)) if query else "")
        headers = {"Accept": "application/json", "User-Agent": f"wealthnow-python/{__version__}"}
        if auth:
            if not self.api_key:
                raise WealthnowError(401, "missing_api_key",
                                     "Set WEALTHNOW_API_KEY or pass api_key=. Get a free key at https://wealthnow.io/register?next=api")
            headers["Authorization"] = f"Bearer {self.api_key}"
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"

        attempt = 0
        while True:
            req = urllib.request.Request(url, data=data, method=method.upper(), headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    self.last_request_id = resp.headers.get("X-Request-ID")
                    self.last_credits = {"cost": resp.headers.get("X-Credits-Cost"),
                                         "remaining": resp.headers.get("X-Credits-Remaining")}
                    raw = resp.read()
                    return json.loads(raw) if raw else None
            except urllib.error.HTTPError as e:
                raw = e.read()
                try:
                    payload = json.loads(raw) if raw else {}
                except ValueError:
                    payload = {"detail": raw[:500].decode("utf-8", "replace")}
                self.last_request_id = e.headers.get("X-Request-ID")
                wait = self._retry_wait(e.code, e.headers.get("Retry-After"), payload, attempt)
                if wait is not None:
                    time.sleep(wait)
                    attempt += 1
                    continue
                if not isinstance(payload, dict):
                    payload = {"detail": payload}
                raise WealthnowError(
                    e.code,
                    str(payload.get("error") or payload.get("code") or "http_error"),
                    str(payload.get("detail") or payload.get("error_description") or payload.get("message") or e.reason),
                    payload.get("request_id") or self.last_request_id,
                    payload,
                ) from None
            except urllib.error.URLError as e:
                raise WealthnowError(0, "network_error", str(e.reason)) from None

    def _retry_wait(self, status: int, retry_after: Optional[str], payload: Any, attempt: int) -> Optional[float]:
        if status not in _RETRYABLE or attempt >= self.max_retries:
            return None
        if isinstance(payload, dict) and payload.get("retryable") is False:
            return None
        if status == 503 and retry_after is None and not (isinstance(payload, dict) and payload.get("retryable")):
            return None
        try:
            wait = float(retry_after) if retry_after is not None else 2.0 ** attempt
        except ValueError:
            wait = 2.0 ** attempt
        return wait if wait <= _MAX_RETRY_AFTER else None

    def get(self, path: str, **params: Any) -> Any:
        """GET any path, e.g. ``wn.get("/api/v3/fundamentals/price_snapshot", ticker="AAPL")``."""
        return self.request("GET", path, params)

    def call(self, operation_id: str, body: Any = None, **params: Any) -> Any:
        """Call an endpoint by its operationId (the same name the MCP server uses)."""
        try:
            op = self.operations[operation_id]
        except KeyError:
            raise WealthnowError(0, "unknown_operation", f"No operation named {operation_id!r}") from None
        path = op["path"]
        for name in op["path_params"]:
            if name not in params:
                raise TypeError(f"{operation_id}() missing path parameter {name!r}")
            path = path.replace("{" + name + "}", urllib.parse.quote(str(params.pop(name)), safe=""))
        return self.request(op["method"], path, params, body=body)

    def search_operations(self, text: str) -> List[str]:
        """Operation names whose name or summary contains ``text`` (case-insensitive)."""
        t = text.lower()
        return [k for k, v in self.operations.items() if t in k.lower() or t in v["summary"].lower()]

    # Discovery (no key needed) ------------------------------------------

    def capabilities(self) -> Any:
        """The live capability manifest. No API key needed."""
        return self.request("GET", "/api/capabilities", auth=False)

    def openapi(self) -> Any:
        """The public OpenAPI 3.1 spec. No API key needed."""
        return self.request("GET", "/api/openapi.json", auth=False)

    # Convenience wrappers for common calls ------------------------------

    def price_snapshot(self, ticker: str, **params: Any) -> Any:
        """Latest price for a stock or crypto ticker, with the time of its last trade."""
        return self.call("fundamentals_price_snapshot", ticker=ticker, **params)

    def quote(self, ticker: str) -> Any:
        """Level 1 quote: last print, bid and ask when the session has a book, volume."""
        return self.call("market_quote", ticker=ticker)

    def crypto_quote(self, ticker: str, **params: Any) -> Any:
        """Crypto quote: last trade, 24 hour change and volume."""
        return self.call("crypto_quote", ticker=ticker, **params)

    def fundamentals(self, ticker: str) -> Any:
        """Income statement, balance sheet, cash flow and key metrics."""
        return self.call("fundamentals_full", ticker=ticker)

    def insider_clusters(self, limit: Optional[int] = None) -> Any:
        """Tickers where two or more insiders bought in the last 30 days."""
        return self.call("insider_clusters", limit=limit)
