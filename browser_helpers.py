from __future__ import annotations

import json
import re
from decimal import Decimal
from pathlib import Path
from typing import Any

from playwright.sync_api import BrowserContext, Page, expect

MONEY_RE = re.compile(r"\$[\d,]+\.\d{2}")
UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    re.IGNORECASE,
)


def normalize_url(url: str) -> str:
    return url.rstrip("/")


def enter_demo(page: Page, base_url: str) -> None:
    page.goto(base_url + "/", wait_until="domcontentloaded")
    page.get_by_role("button", name="Enter Demo").click()
    page.wait_for_url("**/dashboard**", timeout=30_000)
    expect(page.get_by_role("heading", name=re.compile(r"Welcome,"))).to_be_visible(timeout=15_000)


def parse_money(text: str) -> Decimal | None:
    match = MONEY_RE.search(text.replace("−", "-"))
    if not match:
        return None
    raw = match.group(0).replace("$", "").replace(",", "")
    try:
        return Decimal(raw)
    except Exception:
        return None


def screenshot(page: Page, report_dir: Path, slug: str) -> str:
    report_dir.mkdir(parents=True, exist_ok=True)
    path = report_dir / f"{slug}.png"
    try:
        page.screenshot(path=str(path), full_page=True)
    except Exception:
        return ""
    return str(path)


def api_json(context: BrowserContext, api_url: str, method: str, path: str, body: Any | None = None) -> tuple[int, Any]:
    url = api_url + path
    if method.upper() == "GET":
        response = context.request.get(url)
    elif method.upper() == "POST":
        response = context.request.post(
            url,
            data=json.dumps(body) if body is not None else None,
            headers={"Content-Type": "application/json"} if body is not None else None,
        )
    else:
        response = context.request.fetch(url, method=method)
    try:
        payload = response.json()
    except Exception:
        payload = response.text()
    return response.status, payload


def list_accounts(context: BrowserContext, api_url: str) -> list[dict[str, Any]]:
    status, payload = api_json(context, api_url, "GET", "/api/accounts")
    if status != 200 or not isinstance(payload, dict):
        raise RuntimeError(f"GET /api/accounts failed ({status}): {payload}")
    accounts = payload.get("accounts")
    if not isinstance(accounts, list):
        raise RuntimeError("Unexpected /api/accounts response shape")
    return accounts
