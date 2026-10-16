# DemoBank QA Agent

Autonomous, specification-driven QA runner built for the Agentic QA Hackathon. This agent reads a raw Product Requirements Document (PRD), dynamically extracts testable behavioral requirements using Gemini 2.5 Flash, executes Playwright browser scenarios against a DemoBank URL, and generates a comprehensive QA audit report complete with real-time API cost tracking.

## Architecture

PRD.md (Raw Text) ───────> Gemini 2.5 Flash API
                                │
                                v (Dynamic JSON array)
CLI (--url, --prd)  →  prd_loader & runner  →  Playwright checks  →  audit.md / audit.json
                                            ↘  API balance asserts

## Cost Breakdown
The agent dynamically calculates costs based on Gemini 2.5 Flash pricing ($0.15 / 1M input tokens, $1.25 / 1M output tokens). 
For the demonstrated PRD extraction run:
- Input Tokens: 1,263
- Output Tokens: 5,257
- Total Estimated Cost: $0.0068 USD
