import { OPERATIONS, SPEC_VERSION } from "./operations.js";
import type { Operation, OperationIndex } from "./types.js";

export type { Operation, OperationIndex };
export { OPERATIONS, SPEC_VERSION };

export const VERSION = "0.1.0";
export const DEFAULT_BASE_URL = "https://firm.wealthnow.io";
const RETRYABLE = new Set([429, 502, 503]);
const MAX_RETRY_AFTER_S = 120;

export type Params = Record<string, string | number | boolean | Array<string | number> | null | undefined>;

export interface WealthnowOptions {
  /** Defaults to process.env.WEALTHNOW_API_KEY. */
  apiKey?: string;
  /** Defaults to process.env.WEALTHNOW_BASE_URL or https://firm.wealthnow.io. */
  baseUrl?: string;
  /** Milliseconds. Default 30000. */
  timeoutMs?: number;
  /** Retries for 429, 502 and retryable 503. Default 2. */
  maxRetries?: number;
  /** Custom fetch, e.g. for testing. Defaults to globalThis.fetch (Node 18+). */
  fetch?: typeof fetch;
}

export class WealthnowError extends Error {
  constructor(
    public readonly status: number,
    public readonly code: string,
    message: string,
    public readonly requestId?: string,
    public readonly body?: unknown,
  ) {
    super(`${status} ${code}: ${message}`);
    this.name = "WealthnowError";
  }
}

function env(name: string): string | undefined {
  const p = (globalThis as { process?: { env?: Record<string, string | undefined> } }).process;
  return p?.env?.[name];
}

export class Wealthnow {
  readonly apiKey?: string;
  readonly baseUrl: string;
  readonly timeoutMs: number;
  readonly maxRetries: number;
  readonly operations: OperationIndex = OPERATIONS;
  readonly specVersion = SPEC_VERSION;
  /** Credit headers from the last successful call. */
  lastCredits: { cost?: string | null; remaining?: string | null } = {};
  /** X-Request-ID of the last call, for support requests. */
  lastRequestId?: string | null;
  private readonly fetchImpl: typeof fetch;

  constructor(opts: WealthnowOptions = {}) {
    this.apiKey = opts.apiKey ?? env("WEALTHNOW_API_KEY");
    this.baseUrl = (opts.baseUrl ?? env("WEALTHNOW_BASE_URL") ?? DEFAULT_BASE_URL).replace(/\/+$/, "");
    this.timeoutMs = opts.timeoutMs ?? 30_000;
    this.maxRetries = opts.maxRetries ?? 2;
    const f = opts.fetch ?? globalThis.fetch;
    if (!f) throw new Error("wealthnow: no fetch available; use Node 18+ or pass options.fetch");
    this.fetchImpl = f.bind(globalThis);
  }

  /** Send one request and return the decoded JSON body. */
  async request<T = any>(method: string, path: string, params: Params = {}, body?: unknown, auth = true): Promise<T> {
    const qs = new URLSearchParams();
    for (const [k, v] of Object.entries(params)) {
      if (v === undefined || v === null) continue;
      qs.set(k, Array.isArray(v) ? v.join(",") : String(v));
    }
    const url = this.baseUrl + path + (qs.toString() ? `?${qs}` : "");
    const headers: Record<string, string> = { Accept: "application/json" };
    if (!(globalThis as { window?: unknown }).window) headers["User-Agent"] = `wealthnow-js/${VERSION}`;
    if (auth) {
      if (!this.apiKey) {
        throw new WealthnowError(401, "missing_api_key",
          "Set WEALTHNOW_API_KEY or pass { apiKey }. Get a free key at https://wealthnow.io/register?next=api");
      }
      headers.Authorization = `Bearer ${this.apiKey}`;
    }
    let payload: string | undefined;
    if (body !== undefined) {
      payload = JSON.stringify(body);
      headers["Content-Type"] = "application/json";
    }

    for (let attempt = 0; ; attempt++) {
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), this.timeoutMs);
      let res: Response;
      try {
        res = await this.fetchImpl(url, { method, headers, body: payload, signal: ctrl.signal });
      } catch (e) {
        throw new WealthnowError(0, "network_error", (e as Error).message);
      } finally {
        clearTimeout(timer);
      }
      this.lastRequestId = res.headers.get("x-request-id");
      const text = await res.text();
      let data: any = undefined;
      try { data = text ? JSON.parse(text) : undefined; } catch { data = { detail: text.slice(0, 500) }; }
      if (res.ok) {
        this.lastCredits = { cost: res.headers.get("x-credits-cost"), remaining: res.headers.get("x-credits-remaining") };
        return data as T;
      }
      const wait = this.retryWait(res.status, res.headers.get("retry-after"), data, attempt);
      if (wait !== null) {
        await new Promise((r) => setTimeout(r, wait * 1000));
        continue;
      }
      const d = (data && typeof data === "object") ? data : {};
      throw new WealthnowError(
        res.status,
        String(d.error ?? d.code ?? "http_error"),
        String(d.detail ?? d.error_description ?? d.message ?? res.statusText),
        d.request_id ?? this.lastRequestId ?? undefined,
        data,
      );
    }
  }

  private retryWait(status: number, retryAfter: string | null, data: any, attempt: number): number | null {
    if (!RETRYABLE.has(status) || attempt >= this.maxRetries) return null;
    if (data && data.retryable === false) return null;
    if (status === 503 && retryAfter === null && !(data && data.retryable)) return null;
    const n = retryAfter !== null ? Number(retryAfter) : 2 ** attempt;
    const wait = Number.isFinite(n) ? n : 2 ** attempt;
    return wait <= MAX_RETRY_AFTER_S ? wait : null;
  }

  /** GET any path, e.g. get("/api/v3/fundamentals/price_snapshot", { ticker: "AAPL" }). */
  get<T = any>(path: string, params: Params = {}): Promise<T> {
    return this.request<T>("GET", path, params);
  }

  /** Call an endpoint by its operationId (the same name the MCP server uses). */
  call<T = any>(operationId: string, params: Params = {}, body?: unknown): Promise<T> {
    const op = this.operations[operationId];
    if (!op) return Promise.reject(new WealthnowError(0, "unknown_operation", `No operation named ${operationId}`));
    const rest: Params = { ...params };
    let path = op.path;
    for (const name of op.path_params) {
      const v = rest[name];
      if (v === undefined || v === null) {
        return Promise.reject(new TypeError(`${operationId}: missing path parameter ${name}`));
      }
      path = path.replace(`{${name}}`, encodeURIComponent(String(v)));
      delete rest[name];
    }
    return this.request<T>(op.method, path, rest, body);
  }

  /** Operation names whose name or summary contains text (case-insensitive). */
  searchOperations(text: string): string[] {
    const t = text.toLowerCase();
    return Object.entries(this.operations)
      .filter(([k, v]) => k.toLowerCase().includes(t) || v.summary.toLowerCase().includes(t))
      .map(([k]) => k);
  }

  /** The live capability manifest. No API key needed. */
  capabilities<T = any>(): Promise<T> { return this.request<T>("GET", "/api/capabilities", {}, undefined, false); }
  /** The public OpenAPI 3.1 spec. No API key needed. */
  openapi<T = any>(): Promise<T> { return this.request<T>("GET", "/api/openapi.json", {}, undefined, false); }

  /** Latest price for a stock or crypto ticker, with the time of its last trade. */
  priceSnapshot<T = any>(ticker: string, params: Params = {}): Promise<T> {
    return this.call<T>("fundamentals_price_snapshot", { ticker, ...params });
  }
  /** Level 1 quote: last print, bid and ask when the session has a book, volume. */
  quote<T = any>(ticker: string): Promise<T> { return this.call<T>("market_quote", { ticker }); }
  /** Crypto quote: last trade, 24 hour change and volume. */
  cryptoQuote<T = any>(ticker: string, params: Params = {}): Promise<T> {
    return this.call<T>("crypto_quote", { ticker, ...params });
  }
  /** Income statement, balance sheet, cash flow and key metrics. */
  fundamentals<T = any>(ticker: string): Promise<T> { return this.call<T>("fundamentals_full", { ticker }); }
  /** Tickers where two or more insiders bought in the last 30 days. */
  insiderClusters<T = any>(limit?: number): Promise<T> { return this.call<T>("insider_clusters", { limit }); }
}

export default Wealthnow;
