from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

from .browser_helpers import normalize_url
from .checks import CheckContext, mark_unverified_requirements, run_all_checks
from .models import AuditRun, CostEntry, utc_now
from .prd_loader import load_requirements, llm_usage


def run_audit(
    target_url: str,
    prd_path: Path | None,
    api_url: str | None,
    output_dir: Path,
    *,
    headed: bool = False,
) -> AuditRun:
    base_url = normalize_url(target_url)
    resolved_api = normalize_url(api_url or target_url)
    requirements = load_requirements(prd_path)
    run = AuditRun(
        target_url=base_url,
        api_url=resolved_api,
        prd_path=str(prd_path) if prd_path else "",
        started_at=utc_now(),
        requirements=requirements,
        costs=_default_costs(),
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        ctx = CheckContext(page, context, base_url, resolved_api, output_dir)
        try:
            results = run_all_checks(ctx)
            req_ids = {r.id for r in requirements}
            run.results = mark_unverified_requirements(req_ids, results)
        finally:
            context.close()
            browser.close()

    run.finished_at = utc_now()
    return run


def _default_costs() -> list[CostEntry]:
    """Scripted Playwright run; extended with Gemini LLM orchestration."""
    
    # Calculate exact API costs based on Gemini 2.5 Flash pricing
    in_tokens = llm_usage.get("input_tokens", 0)
    out_tokens = llm_usage.get("output_tokens", 0)
    gemini_cost = (in_tokens / 1_000_000 * 0.15) + (out_tokens / 1_000_000 * 1.25)
    
    return [
        CostEntry(
            label="Automated browser checks",
            model="n/a (deterministic Playwright)",
            input_tokens=0,
            output_tokens=0,
            estimated_usd=0.0,
            notes="No LLM calls in the default suite.",
        ),
        CostEntry(
            label="PRD Extraction",
            model="gemini-2.5-flash",
            input_tokens=in_tokens,
            output_tokens=out_tokens,
            estimated_usd=round(gemini_cost, 4),
            notes="Dynamically extracted requirements using the Gemini API.",
        )
    ]