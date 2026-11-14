# IgnitionSense

Python Streamlit educational space-fire dashboard for the NASA Space Apps Challenge "Flame in Freefall".

## Run & Operate

- `python artifacts/ignitionsense/run.py` — launch the Streamlit dashboard; the managed web workflow supplies its assigned port.
- Python dependencies are declared in root `pyproject.toml` and locked in `uv.lock`.
- Dashboard source: `artifacts/ignitionsense/app.py`; educational scoring: `risk_model.py`; case studies and NASA references: `research.py`.
- The dark theme uses native Streamlit configuration; no custom CSS is needed.
- Scores are hand-weighted demonstrations, not probabilities or NASA-validated predictions. No NASA datasets are ingested and no runtime AI service is called.

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

_Populate as you build — short repo map plus pointers to the source-of-truth file for DB schema, API contracts, theme files, etc._

## Architecture decisions

_Populate as you build — non-obvious choices a reader couldn't infer from the code (3-5 bullets)._

## Product

_Describe the high-level user-facing capabilities of this app once they exist._

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
