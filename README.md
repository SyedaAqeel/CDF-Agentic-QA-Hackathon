# DemoBank QA Agent 

Autonomous, specification-driven QA runner built for the Agentic QA Hackathon. This agent reads a raw Product Requirements Document (PRD), dynamically extracts testable behavioral requirements using Gemini 2.5 Flash, executes Playwright browser scenarios against a DemoBank URL, and generates a comprehensive QA audit report complete with real-time API cost tracking.

## Architecture

```text
PRD.md (Raw Text) ───────> Gemini 2.5 Flash API
                                │
                                v (Dynamic JSON array)
CLI (--url, --prd)  →  prd_loader & runner  →  Playwright checks  →  audit.md / audit.json
                                            ↘  API balance asserts
```

| Component | Role |
|-----------|------|
| `Agent/prd_loader.py` | Validates `--prd` path; intercepts document and dynamically generates testable requirements via LLM. |
| `Agent/checks.py` | PRD-mapped Playwright scenarios (session, transfers, filters, profile). |
| `Agent/browser_helpers.py` | Navigation helpers, screenshots, API calls with session cookies. |
| `Agent/reporter.py` | Markdown + JSON audit export logic. |
| `Agent/runner.py` | Orchestrates the audit, compares results, and calculates dynamic token costs. |


## Requirements

- Python 3.11+
- Chromium via Playwright
- `google-genai` Python SDK
- A valid Google Gemini API Key (free tier available via Google AI Studio)

##  Setup & Installation

### 1. Initialize the environment

```bash
cd agent
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -e .
pip install google-genai
playwright install chromium
```

### Set your API key

Configure your Gemini API key as an environment variable before running the agent.

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# macOS/Linux
export GEMINI_API_KEY="your_api_key_here"
```

## Run Commands

**Hosted hackathon URL** (frontend and API on the same origin):

```bash
demobank-qa --url https://YOUR-HOSTED-DEMOBANK --prd ../test-website/PRD.md --output reports
```

**Local DemoBank:**

```bash
demobank-qa --url http://localhost:5173 --api-url http://localhost:8000 --prd ../test-website/PRD.md --output reports
```

> **Note:** Use `http://localhost` instead of `127.0.0.1` so session cookies match CORS.

## Outputs & Artifacts

After a successful run, the `Report/` directory will contain:

- `audit.md` — A human-readable audit for judges, detailing passed/failed metrics and exact LLM token cost calculations.
- `audit.json` — Machine-readable test results.
- `*.png` — Visual screenshot evidence automatically captured at the point of failure/success for each check.

## Cost Breakdown

The agent estimates LLM cost from the token counts reported by the Gemini API, using the published Gemini 2.5 Flash paid-tier rates:

| Item | Rate (per 1M tokens) |
|------|------|
| Input | $0.30 |
| Output | $2.50 |

For the demonstrated PRD extraction run:

| Metric |	Value |
|--------|------|
| Input tokens |	1,263 |
| Output tokens |	5,257 |
| Estimated cost |	$0.0135 |

## License / Scope

Synthetic demo data only. Do not run denial-of-service tests or probe infrastructure outside the supplied application.
