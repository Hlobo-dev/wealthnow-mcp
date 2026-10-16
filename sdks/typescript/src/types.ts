export interface Operation {
  method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  path: string;
  path_params: string[];
  query_params: string[];
  body: boolean;
  min_plan: string | null;
  summary: string;
}

export type OperationIndex = Record<string, Operation>;
