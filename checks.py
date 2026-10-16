from __future__ import annotations

import re
from decimal import Decimal
from pathlib import Path

from playwright.sync_api import BrowserContext, Page, expect

from .browser_helpers import (
    UUID_RE,
    enter_demo,
    list_accounts,
    parse_money,
    screenshot,
)
from .models import CheckResult, Verdict


class CheckContext:
    def __init__(
        self,
        page: Page,
        context: BrowserContext,
        base_url: str,
        api_url: str,
        report_dir: Path,
    ) -> None:
        self.page = page
        self.context = context
        self.base_url = base_url
        self.api_url = api_url
        self.report_dir = report_dir
        self._accounts: list[dict] | None = None

    def shot(self, slug: str) -> str:
        path = screenshot(self.page, self.report_dir, slug)
        return path if path else ""

    def accounts(self) -> list[dict]:
        if self._accounts is None:
            self._accounts = list_accounts(self.context, self.api_url)
        return self._accounts

    def refresh_accounts(self) -> list[dict]:
        self._accounts = list_accounts(self.context, self.api_url)
        return self._accounts

    def goto_transfer(self) -> None:
        self.page.get_by_role("link", name="Transfer", exact=True).click()
        self.page.wait_for_url("**/transfer**")
        expect(self.page.get_by_role("heading", name="Transfer between your accounts")).to_be_visible()

    def submit_transfer(self, amount: str, same_account: bool = False) -> None:
        accounts = self.accounts()
        if len(accounts) < 2:
            raise RuntimeError("Need at least two accounts for transfer tests")
        source_id = accounts[0]["id"]
        dest_id = accounts[0]["id"] if same_account else accounts[1]["id"]
        self.page.locator("#source").select_option(source_id)
        self.page.locator("#destination").select_option(dest_id)
        self.page.locator("#amount").fill(amount)
        self.page.get_by_role("button", name="Transfer funds").click()


def run_all_checks(ctx: CheckContext) -> list[CheckResult]:
    results: list[CheckResult] = []
    results.append(check_enter_demo(ctx))
    results.append(check_header_customer(ctx))
    results.append(check_dashboard_accounts(ctx))
    results.append(check_balance_two_decimals(ctx))
    results.append(check_masked_identifiers(ctx))
    results.append(check_valid_transfer(ctx))
    results.append(check_transfer_success_messaging(ctx))
    results.append(check_same_account_transfer(ctx))
    results.append(check_invalid_amounts(ctx))
    results.append(check_insufficient_funds(ctx))
    results.append(check_transactions_list(ctx))
    results.append(check_transaction_filter(ctx))
    results.append(check_empty_filter_state(ctx))
    results.append(check_profile(ctx))
    results.append(check_logout_and_guard(ctx))
    results.append(check_ui_validation_feedback(ctx))
    results.append(check_loading_on_submit(ctx))
    return results


def check_enter_demo(ctx: CheckContext) -> CheckResult:
    rid = "REQ-ACCESS-01"
    steps = ["Open landing page", "Click Enter Demo"]
    try:
        enter_demo(ctx.page, ctx.base_url)
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED,
            title="Enter Demo reaches dashboard",
            steps=steps,
            expected="Dashboard loads without password.",
            observed=f"URL is {ctx.page.url}",
            evidence=[ctx.shot("access-enter-demo")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Enter Demo failed",
            steps=steps,
            expected="Dashboard loads without password.",
            observed=str(exc),
            evidence=[ctx.shot("access-enter-demo-fail")],
            error=str(exc),
        )


def check_header_customer(ctx: CheckContext) -> CheckResult:
    rid = "REQ-ACCESS-02"
    steps = ["After Enter Demo, inspect header session area"]
    try:
        el = ctx.page.get_by_test_id("active-customer")
        expect(el).to_be_visible()
        name = el.inner_text().strip()
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED,
            title="Header shows demo customer",
            steps=steps,
            expected="Display name visible in header.",
            observed=f"Header text: {name}",
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Header customer missing",
            steps=steps,
            expected="Display name visible in header.",
            observed=str(exc),
            evidence=[ctx.shot("access-header")],
            error=str(exc),
        )


def check_dashboard_accounts(ctx: CheckContext) -> CheckResult:
    rid = "REQ-DASH-01"
    steps = ["On dashboard, count account cards and balance format"]
    try:
        ctx.page.goto(ctx.base_url + "/dashboard")
        cards = ctx.page.get_by_test_id("account-card")
        expect(cards).to_have_count(2, timeout=15_000)
        balances = [c.inner_text() for c in ctx.page.get_by_test_id("account-balance").all()]
        bad = [b for b in balances if parse_money(b) is None]
        verdict = Verdict.FAILED if bad else Verdict.PASSED
        return CheckResult(
            requirement_id=rid,
            verdict=verdict,
            title="Dashboard shows two accounts with formatted balances",
            steps=steps,
            expected="Checking and savings with $X,XXX.XX balances.",
            observed=f"Balances: {balances}",
            evidence=[ctx.shot("dashboard-accounts")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Dashboard account layout failed",
            steps=steps,
            expected="Two accounts on dashboard.",
            observed=str(exc),
            evidence=[ctx.shot("dashboard-fail")],
            error=str(exc),
        )


def check_balance_two_decimals(ctx: CheckContext) -> CheckResult:
    rid = "REQ-DASH-02"
    steps = ["Read balance text on dashboard cards"]
    try:
        ctx.page.goto(ctx.base_url + "/dashboard")
        texts = [t.inner_text() for t in ctx.page.get_by_test_id("account-balance").all()]
        ok = all(re.search(r"\$\d{1,3}(,\d{3})*\.\d{2}", text) for text in texts)
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if ok else Verdict.FAILED,
            title="Balances use two decimal places",
            steps=steps,
            expected="USD amounts like $2,500.00.",
            observed=str(texts),
            evidence=[ctx.shot("dashboard-decimals")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.UNVERIFIED,
            title="Could not verify balance formatting",
            steps=steps,
            expected="Two decimal places.",
            observed=str(exc),
            error=str(exc),
        )


def check_masked_identifiers(ctx: CheckContext) -> CheckResult:
    rid = "REQ-DASH-03"
    steps = ["Inspect dashboard account card numbers for full UUIDs"]
    try:
        ctx.page.goto(ctx.base_url + "/dashboard")
        html = ctx.page.locator(".account-card").first.inner_text()
        has_uuid = bool(UUID_RE.search(html))
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED if has_uuid else Verdict.PASSED,
            title="Account identifiers are masked on dashboard",
            steps=steps,
            expected="No full UUID in account card UI.",
            observed="Full UUID pattern found in card text." if has_uuid else "Only masked number shown.",
            evidence=[ctx.shot("dashboard-masked")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.UNVERIFIED,
            title="Could not verify masked identifiers",
            steps=steps,
            expected="No full UUID in UI.",
            observed=str(exc),
            error=str(exc),
        )


def check_valid_transfer(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TRANSFER-01"
    steps = [
        "Record balances via API",
        "Transfer $1.00 between accounts",
        "Compare balances after success",
    ]
    try:
        before = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        ctx.goto_transfer()
        ctx.submit_transfer("1.00")
        expect(ctx.page.get_by_text("Transfer complete")).to_be_visible(timeout=20_000)
        after = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        ids = list(before.keys())
        if len(ids) < 2:
            raise RuntimeError("Need two accounts")
        src, dst = ids[0], ids[1]
        delta_src = after[src] - before[src]
        delta_dst = after[dst] - before[dst]
        ok = delta_src == Decimal("-1.00") and delta_dst == Decimal("1.00")
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if ok else Verdict.FAILED,
            title="Valid transfer updates both balances atomically",
            steps=steps,
            expected="Source -1.00, destination +1.00.",
            observed=f"Source delta {delta_src}, destination delta {delta_dst}",
            evidence=[ctx.shot("transfer-success")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Valid transfer check failed",
            steps=steps,
            expected="Balances change by transfer amount in opposite directions.",
            observed=str(exc),
            evidence=[ctx.shot("transfer-success-fail")],
            error=str(exc),
        )


def check_transfer_success_messaging(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TRANSFER-05"
    steps = ["After successful transfer, confirm success alert (not failure copy)"]
    try:
        has_success = ctx.page.get_by_text("Transfer complete").is_visible()
        has_failure = ctx.page.get_by_text("Transfer not completed").is_visible()
        if has_success and not has_failure:
            verdict = Verdict.PASSED
            observed = "Success alert visible; no failure alert."
        elif has_failure:
            verdict = Verdict.FAILED
            observed = "Failure alert visible after prior successful transfer step."
        else:
            verdict = Verdict.UNVERIFIED
            observed = "No transfer feedback on page (run valid transfer check first)."
        return CheckResult(
            requirement_id=rid,
            verdict=verdict,
            title="UI success messaging matches committed transfer",
            steps=steps,
            expected="Success only after commit; failures show non-success copy.",
            observed=observed,
            evidence=[ctx.shot("transfer-messaging")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.UNVERIFIED,
            title="Transfer messaging not verified",
            steps=steps,
            expected="Distinct success vs failure UI.",
            observed=str(exc),
            error=str(exc),
        )


def check_same_account_transfer(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TRANSFER-02"
    steps = ["Attempt transfer with same source and destination", "Verify error and unchanged balances"]
    try:
        before = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        ctx.goto_transfer()
        ctx.submit_transfer("1.00", same_account=True)
        expect(ctx.page.get_by_text("Transfer not completed")).to_be_visible(timeout=15_000)
        after = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        unchanged = before == after
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if unchanged else Verdict.FAILED,
            title="Same-account transfer rejected without balance change",
            steps=steps,
            expected="Clear failure; balances unchanged.",
            observed="Balances unchanged." if unchanged else f"Before {before}, after {after}",
            evidence=[ctx.shot("transfer-same-account")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Same-account transfer behavior unexpected",
            steps=steps,
            expected="Rejection without balance change.",
            observed=str(exc),
            evidence=[ctx.shot("transfer-same-account-fail")],
            error=str(exc),
        )


def check_invalid_amounts(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TRANSFER-03"
    steps = ["Try amount 0", "Try negative amount", "Try 1.234 over-precision"]
    try:
        before = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        ctx.goto_transfer()
        for amount in ("0", "-5", "1.234"):
            ctx.submit_transfer(amount)
            expect(ctx.page.get_by_text(re.compile("Transfer not completed|Enter an amount", re.I))).to_be_visible(
                timeout=15_000
            )
        after = {a["id"]: Decimal(a["balance"]) for a in ctx.refresh_accounts()}
        ok = before == after
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if ok else Verdict.FAILED,
            title="Invalid amounts rejected without balance change",
            steps=steps,
            expected="Validation or API rejection; balances unchanged.",
            observed="Balances unchanged." if ok else f"Before {before}, after {after}",
            evidence=[ctx.shot("transfer-invalid-amounts")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Invalid amount handling failed",
            steps=steps,
            expected="Reject invalid amounts.",
            observed=str(exc),
            evidence=[ctx.shot("transfer-invalid-fail")],
            error=str(exc),
        )


def check_insufficient_funds(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TRANSFER-04"
    steps = ["Attempt transfer far above available balance"]
    try:
        accounts = ctx.refresh_accounts()
        src = accounts[0]
        before = Decimal(src["balance"])
        huge = str(before + Decimal("1000000.00"))
        ctx.goto_transfer()
        ctx.page.locator("#source").select_option(src["id"])
        other = next(a for a in accounts if a["id"] != src["id"])
        ctx.page.locator("#destination").select_option(other["id"])
        ctx.page.locator("#amount").fill(huge)
        ctx.page.get_by_role("button", name="Transfer funds").click()
        expect(ctx.page.get_by_text("Transfer not completed")).to_be_visible(timeout=15_000)
        after_bal = Decimal(ctx.refresh_accounts()[0]["balance"])
        ok = before == after_bal
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if ok else Verdict.FAILED,
            title="Insufficient funds rejected",
            steps=steps,
            expected="Failure message; source balance unchanged.",
            observed=f"Balance before {before}, after {after_bal}",
            evidence=[ctx.shot("transfer-insufficient")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Insufficient funds check failed",
            steps=steps,
            expected="Reject over-balance transfer.",
            observed=str(exc),
            evidence=[ctx.shot("transfer-insufficient-fail")],
            error=str(exc),
        )


def check_transactions_list(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TXN-01"
    steps = ["Open Transactions page", "Verify table rows present"]
    try:
        ctx.page.get_by_role("link", name="Transactions", exact=True).click()
        expect(ctx.page.get_by_role("heading", name="Transactions")).to_be_visible()
        expect(ctx.page.get_by_test_id("result-count")).to_be_visible(timeout=15_000)
        count_text = ctx.page.get_by_test_id("result-count").inner_text()
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED,
            title="Combined transaction history loads",
            steps=steps,
            expected="Transaction list with metadata visible.",
            observed=count_text,
            evidence=[ctx.shot("transactions-list")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Transaction history failed to load",
            steps=steps,
            expected="Rows visible.",
            observed=str(exc),
            evidence=[ctx.shot("transactions-list-fail")],
            error=str(exc),
        )


def check_transaction_filter(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TXN-02"
    steps = ["Filter type=transfer", "Apply filters", "Verify rows are transfers only"]
    try:
        ctx.page.get_by_role("link", name="Transactions", exact=True).click()
        ctx.page.locator("#filter-type").select_option("transfer")
        ctx.page.get_by_role("button", name="Apply filters").click()
        expect(ctx.page.get_by_test_id("result-count")).to_be_visible(timeout=15_000)
        rows = ctx.page.locator("table tbody tr")
        if rows.count() == 0:
            return CheckResult(
                requirement_id=rid,
                verdict=Verdict.UNVERIFIED,
                title="No transfer rows to validate filter",
                steps=steps,
                expected="All visible rows type transfer.",
                observed="Zero rows after filter.",
                evidence=[ctx.shot("transactions-filter-empty")],
            )
        types = [
            rows.nth(i).locator("td").nth(2).inner_text()
            for i in range(min(rows.count(), 10))
        ]
        bad = [t for t in types if "transfer" not in t.lower()]
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if not bad else Verdict.FAILED,
            title="Transfer filter matches displayed rows",
            steps=steps,
            expected="Every row is a transfer.",
            observed=f"Sample types: {types[:5]}",
            evidence=[ctx.shot("transactions-filter")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Transaction filter check failed",
            steps=steps,
            expected="Filtered rows match type.",
            observed=str(exc),
            evidence=[ctx.shot("transactions-filter-fail")],
            error=str(exc),
        )


def check_empty_filter_state(ctx: CheckContext) -> CheckResult:
    rid = "REQ-TXN-03"
    steps = ["Apply impossible date range", "Expect empty state message"]
    try:
        ctx.page.get_by_role("link", name="Transactions", exact=True).click()
        ctx.page.locator("#filter-start").fill("2099-01-01")
        ctx.page.locator("#filter-end").fill("2099-01-02")
        ctx.page.get_by_role("button", name="Apply filters").click()
        empty = ctx.page.get_by_text("No transactions match these filters")
        expect(empty).to_be_visible(timeout=15_000)
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED,
            title="Empty filter result shows empty state",
            steps=steps,
            expected="Clear empty state, not an error page.",
            observed="Empty state visible.",
            evidence=[ctx.shot("transactions-empty")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Empty filter state missing or error shown",
            steps=steps,
            expected="Empty state copy.",
            observed=str(exc),
            evidence=[ctx.shot("transactions-empty-fail")],
            error=str(exc),
        )


def check_profile(ctx: CheckContext) -> CheckResult:
    rid = "REQ-PROFILE-01"
    steps = ["Open Profile", "Verify masked email and no secrets"]
    try:
        ctx.page.get_by_role("link", name="Profile").click()
        email = ctx.page.get_by_test_id("profile-email").inner_text()
        name = ctx.page.get_by_test_id("profile-name").inner_text()
        masked = "*" in email or "•" in email
        leaked = "password" in ctx.page.content().lower()
        ok = masked and not leaked and bool(name.strip())
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if ok else Verdict.FAILED,
            title="Profile shows synthetic masked details",
            steps=steps,
            expected="Display name and masked email only.",
            observed=f"name={name}, email={email}",
            evidence=[ctx.shot("profile")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Profile check failed",
            steps=steps,
            expected="Masked email on profile.",
            observed=str(exc),
            evidence=[ctx.shot("profile-fail")],
            error=str(exc),
        )


def check_logout_and_guard(ctx: CheckContext) -> CheckResult:
    rid = "REQ-ACCESS-03"
    steps = ["Log out from header", "Navigate to /dashboard directly"]
    try:
        ctx.page.get_by_role("button", name="Log out").click()
        ctx.page.wait_for_url("**/")
        expect(ctx.page.get_by_role("button", name="Enter Demo")).to_be_visible()
        ctx.page.goto(ctx.base_url + "/dashboard")
        ctx.page.wait_for_load_state("domcontentloaded")
        on_landing = "Enter Demo" in ctx.page.content()
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if on_landing else Verdict.FAILED,
            title="Logout clears session and blocks dashboard",
            steps=steps,
            expected="Landing page after logout; /dashboard requires demo entry.",
            observed=f"URL {ctx.page.url}, landing={on_landing}",
            evidence=[ctx.shot("logout-guard")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Logout/session guard failed",
            steps=steps,
            expected="Protected routes blocked after logout.",
            observed=str(exc),
            evidence=[ctx.shot("logout-guard-fail")],
            error=str(exc),
        )


def check_ui_validation_feedback(ctx: CheckContext) -> CheckResult:
    rid = "REQ-UI-01"
    steps = ["Re-enter demo", "Submit transfer with empty amount", "Look for field error"]
    try:
        enter_demo(ctx.page, ctx.base_url)
        ctx.goto_transfer()
        ctx.page.locator("#amount").fill("")
        ctx.page.get_by_role("button", name="Transfer funds").click()
        expect(ctx.page.locator("#amount-error")).to_be_visible(timeout=10_000)
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED,
            title="Validation errors shown for invalid input",
            steps=steps,
            expected="Clear validation message near amount field.",
            observed="amount-error visible.",
            evidence=[ctx.shot("ui-validation")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.FAILED,
            title="Validation feedback missing",
            steps=steps,
            expected="Field-level validation message.",
            observed=str(exc),
            evidence=[ctx.shot("ui-validation-fail")],
            error=str(exc),
        )


def check_loading_on_submit(ctx: CheckContext) -> CheckResult:
    rid = "REQ-UI-02"
    steps = ["Observe submit button disabled or loading label during transfer submit"]
    try:
        ctx.goto_transfer()
        ctx.page.locator("#amount").fill("0.01")
        btn = ctx.page.get_by_role("button", name="Transfer funds")
        btn.click()
        saw_busy = False
        for _ in range(20):
            label = btn.inner_text()
            disabled = btn.is_disabled()
            if disabled or "Submitting" in label:
                saw_busy = True
                break
            ctx.page.wait_for_timeout(50)
        expect(ctx.page.get_by_text(re.compile("Transfer complete|Transfer not completed"))).to_be_visible(
            timeout=20_000
        )
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.PASSED if saw_busy else Verdict.UNVERIFIED,
            title="Transfer submit shows in-flight state",
            steps=steps,
            expected="Loading/disabled submit while request in flight.",
            observed="Saw in-flight UI." if saw_busy else "Could not observe loading state (too fast).",
            evidence=[ctx.shot("ui-loading")],
        )
    except Exception as exc:
        return CheckResult(
            requirement_id=rid,
            verdict=Verdict.UNVERIFIED,
            title="Loading state not observed",
            steps=steps,
            expected="Loading or disabled submit.",
            observed=str(exc),
            error=str(exc),
        )


def mark_unverified_requirements(requirement_ids: set[str], results: list[CheckResult]) -> list[CheckResult]:
    covered = {r.requirement_id for r in results}
    missing = requirement_ids - covered
    for rid in sorted(missing):
        results.append(
            CheckResult(
                requirement_id=rid,
                verdict=Verdict.UNVERIFIED,
                title="Not covered by automated suite",
                steps=[],
                expected="See PRD.",
                observed="No automated check mapped.",
            )
        )
    return results
