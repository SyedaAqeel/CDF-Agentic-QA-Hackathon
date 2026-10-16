from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class Verdict(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    UNVERIFIED = "unverified"


@dataclass
class Requirement:
    id: str
    section: str
    text: str


@dataclass
class CheckResult:
    requirement_id: str
    verdict: Verdict
    title: str
    steps: list[str] = field(default_factory=list)
    expected: str = ""
    observed: str = ""
    evidence: list[str] = field(default_factory=list)
    error: str | None = None


@dataclass
class CostEntry:
    label: str
    model: str
    input_tokens: int
    output_tokens: int
    estimated_usd: float
    notes: str = ""


@dataclass
class AuditRun:
    target_url: str
    api_url: str
    prd_path: str
    started_at: datetime
    finished_at: datetime | None = None
    requirements: list[Requirement] = field(default_factory=list)
    results: list[CheckResult] = field(default_factory=list)
    costs: list[CostEntry] = field(default_factory=list)

    def summary(self) -> dict[str, int]:
        counts = {v.value: 0 for v in Verdict}
        for result in self.results:
            counts[result.verdict.value] += 1
        return counts

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_url": self.target_url,
            "api_url": self.api_url,
            "prd_path": self.prd_path,
            "started_at": self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
            "summary": self.summary(),
            "requirements": [
                {"id": r.id, "section": r.section, "text": r.text} for r in self.requirements
            ],
            "results": [
                {
                    "requirement_id": r.requirement_id,
                    "verdict": r.verdict.value,
                    "title": r.title,
                    "steps": r.steps,
                    "expected": r.expected,
                    "observed": r.observed,
                    "evidence": r.evidence,
                    "error": r.error,
                }
                for r in self.results
            ],
            "costs": [
                {
                    "label": c.label,
                    "model": c.model,
                    "input_tokens": c.input_tokens,
                    "output_tokens": c.output_tokens,
                    "estimated_usd": c.estimated_usd,
                    "notes": c.notes,
                }
                for c in self.costs
            ],
            "total_estimated_usd": round(sum(c.estimated_usd for c in self.costs), 4),
        }


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
