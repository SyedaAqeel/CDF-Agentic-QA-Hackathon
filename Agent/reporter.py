from __future__ import annotations

import json
from pathlib import Path

from .models import AuditRun, CheckResult, Requirement, Verdict


def write_reports(run: AuditRun, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "audit.json"
    md_path = output_dir / "audit.md"
    json_path.write_text(json.dumps(run.to_dict(), indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(run), encoding="utf-8")
    return json_path, md_path


def render_markdown(run: AuditRun) -> str:
    summary = run.summary()
    req_by_id = {r.id: r for r in run.requirements}
    lines = [
        "# DemoBank QA audit report",
        "",
        f"- **Target URL:** `{run.target_url}`",
        f"- **API URL:** `{run.api_url}`",
        f"- **PRD reference:** `{run.prd_path or '(bundled checklist only)'}`",
        f"- **Started:** {run.started_at.isoformat()}",
        f"- **Finished:** {run.finished_at.isoformat() if run.finished_at else '—'}",
        "",
        "## Summary",
        "",
        f"| Passed | Failed | Unverified |",
        f"|---:|---:|---:|",
        f"| {summary['passed']} | {summary['failed']} | {summary['unverified']} |",
        "",
        "## Cost estimate",
        "",
        "| Label | Model | Input tokens | Output tokens | Est. USD | Notes |",
        "|---|---|---:|---:|---:|---|",
    ]
    for cost in run.costs:
        lines.append(
            f"| {cost.label} | {cost.model} | {cost.input_tokens} | {cost.output_tokens} | "
            f"{cost.estimated_usd:.4f} | {cost.notes} |"
        )
    lines.append(f"\n**Total estimated USD:** {sum(c.estimated_usd for c in run.costs):.4f}")
    lines.extend(["", "## Requirement results", ""])

    by_req: dict[str, list[CheckResult]] = {}
    for result in run.results:
        by_req.setdefault(result.requirement_id, []).append(result)

    for req in run.requirements:
        lines.extend(_render_requirement_block(req, by_req.get(req.id, [])))

    return "\n".join(lines) + "\n"


def _render_requirement_block(req: Requirement, checks: list[CheckResult]) -> list[str]:
    if not checks:
        checks = [
            CheckResult(
                requirement_id=req.id,
                verdict=Verdict.UNVERIFIED,
                title="No check executed",
                observed="",
            )
        ]
    primary = checks[0]
    lines = [
        f"### {req.id} — {req.section}",
        "",
        f"**PRD:** {req.text}",
        "",
        f"**Verdict:** `{primary.verdict.value}` — {primary.title}",
        "",
    ]
    if primary.expected:
        lines.append(f"- **Expected:** {primary.expected}")
    if primary.observed:
        lines.append(f"- **Observed:** {primary.observed}")
    if primary.steps:
        lines.append("- **Steps:**")
        for step in primary.steps:
            lines.append(f"  1. {step}")
    evidence = [path for path in primary.evidence if path]
    if evidence:
        lines.append("- **Evidence:**")
        for path in evidence:
            lines.append(f"  - `{path}`")
    if primary.error:
        lines.append(f"- **Error:** {primary.error}")
    lines.append("")
    return lines
