from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .reporter import write_reports
from .runner import run_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run specification-driven QA checks against a DemoBank deployment.",
    )
    parser.add_argument("--url", required=True, help="DemoBank frontend base URL (e.g. https://host or http://localhost:5173)")
    parser.add_argument(
        "--prd",
        type=Path,
        default=None,
        help="Path to PRD.md (validates file exists; checklist uses bundled requirement IDs)",
    )
    parser.add_argument(
        "--api-url",
        default=None,
        help="API base URL if different from --url (local dev: http://localhost:8000)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports"),
        help="Directory for audit.md, audit.json, and screenshots",
    )
    parser.add_argument("--headed", action="store_true", help="Run browser with UI visible")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args(argv)

    try:
        audit = run_audit(
            target_url=args.url,
            prd_path=args.prd,
            api_url=args.api_url,
            output_dir=args.output,
            headed=args.headed,
        )
        json_path, md_path = write_reports(audit, args.output)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Audit failed: {exc}", file=sys.stderr)
        return 1

    summary = audit.summary()
    print(f"Audit complete — passed={summary['passed']} failed={summary['failed']} unverified={summary['unverified']}")
    print(f"Report: {md_path}")
    print(f"JSON:   {json_path}")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
