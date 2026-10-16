# DemoBank QA audit report

- **Target URL:** `http://localhost:5173`
- **API URL:** `http://localhost:8000`
- **PRD reference:** `..\test-website\PRD.md`
- **Started:** 2026-10-16T01:31:17.877442+00:00
- **Finished:** 2026-10-16T01:32:08.709988+00:00

## Summary

| Passed | Failed | Unverified |
|---:|---:|---:|
| 12 | 4 | 126 |

## Cost estimate

| Label | Model | Input tokens | Output tokens | Est. USD | Notes |
|---|---|---:|---:|---:|---|
| Automated browser checks | n/a (deterministic Playwright) | 0 | 0 | 0.0000 | No LLM calls in the default suite. |
| PRD Extraction | gemini-2.5-flash | 1263 | 5257 | 0.0068 | Dynamically extracted requirements using the Gemini API. |

**Total estimated USD:** 0.0068

## Requirement results

### 1 — Purpose

**PRD:** A user should be able to enter a demo session.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 2 — Purpose

**PRD:** A user should be able to inspect their accounts.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 3 — Purpose

**PRD:** A user should be able to inspect their transaction history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 4 — Purpose

**PRD:** A user should be able to transfer funds between their own accounts.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 5 — Purpose

**PRD:** A user should be able to view basic profile information.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 6 — Purpose

**PRD:** The application must use only synthetic records.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 7 — Purpose

**PRD:** The application must never initiate real payments.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 8 — Purpose

**PRD:** The application must never connect to an external bank.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 9 — Users and access

**PRD:** The target has one seeded demo customer.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 10 — Users and access

**PRD:** The landing page provides a clearly labeled 'Enter Demo' action.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 11 — Users and access

**PRD:** The 'Enter Demo' action opens the demo dashboard without requiring a password.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 12 — Users and access

**PRD:** The 'Enter Demo' action opens the demo dashboard without requiring real identity information.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 13 — Users and access

**PRD:** The header identifies the active demo customer.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 14 — Users and access

**PRD:** The header provides a 'Log out' action.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 15 — Users and access

**PRD:** Logging out returns the user to the landing page.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 16 — Users and access

**PRD:** Protected dashboard views should not remain usable after logout.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 17 — Users and access

**PRD:** Direct navigation to protected dashboard views after logout should return the user to the landing page or an access-required state.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 18 — Users and access

**PRD:** Refreshing while in a valid demo session should preserve that session.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 19 — Users and access

**PRD:** A logged-out user must not regain access merely by refreshing a protected page.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 20 — Dashboard and accounts

**PRD:** The dashboard shows the customer's checking account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 21 — Dashboard and accounts

**PRD:** The dashboard shows the customer's savings account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 22 — Dashboard and accounts

**PRD:** Each account displays a readable account name.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 23 — Dashboard and accounts

**PRD:** Each account displays a masked account identifier.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 24 — Dashboard and accounts

**PRD:** Each account displays account type.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 25 — Dashboard and accounts

**PRD:** Each account displays current available balance in USD.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 26 — Dashboard and accounts

**PRD:** Balances are displayed to two decimal places.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 27 — Dashboard and accounts

**PRD:** The UI must not expose a full account identifier.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 28 — Dashboard and accounts

**PRD:** Selecting an account opens an account detail view.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 29 — Dashboard and accounts

**PRD:** The account detail view shows the account's current balance.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 30 — Dashboard and accounts

**PRD:** The account detail view shows the account's related transaction history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 31 — Dashboard and accounts

**PRD:** Account balances shown on the dashboard and detail view must agree with the latest successful transactions.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 32 — Transfers between owned accounts

**PRD:** The user can transfer funds between the checking and savings accounts owned by the demo customer.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 33 — Transfers between owned accounts

**PRD:** The transfer form includes a source account field.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 34 — Transfers between owned accounts

**PRD:** The transfer form includes a destination account field.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 35 — Transfers between owned accounts

**PRD:** The transfer form includes an amount field.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 36 — Transfers between owned accounts

**PRD:** The transfer form includes an optional memo field.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 37 — Transfers between owned accounts

**PRD:** The source and destination accounts for a transfer must be different.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 38 — Transfers between owned accounts

**PRD:** Same-account transfers must be rejected with a clear explanation.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 39 — Transfers between owned accounts

**PRD:** Same-account transfers must not alter balances.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 40 — Transfers between owned accounts

**PRD:** Same-account transfers must not create a transaction.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 41 — Transfers between owned accounts

**PRD:** The transfer amount must be a positive number greater than zero.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 42 — Transfers between owned accounts

**PRD:** The transfer amount must have no more than two digits after the decimal point.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 43 — Transfers between owned accounts

**PRD:** Blank transfer amount values must be rejected with a clear validation message.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 44 — Transfers between owned accounts

**PRD:** Zero transfer amount values must be rejected with a clear validation message.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 45 — Transfers between owned accounts

**PRD:** Negative transfer amount values must be rejected with a clear validation message.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 46 — Transfers between owned accounts

**PRD:** Non-numeric transfer amount values must be rejected with a clear validation message.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 47 — Transfers between owned accounts

**PRD:** Over-precision transfer amount values (more than two decimal places) must be rejected with a clear validation message.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 48 — Transfers between owned accounts

**PRD:** Rejected input for transfer amount must not create a transaction.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 49 — Transfers between owned accounts

**PRD:** Rejected input for transfer amount must not change balances.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 50 — Transfers between owned accounts

**PRD:** The transfer amount must not exceed the source account's available balance.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 51 — Transfers between owned accounts

**PRD:** If funds are insufficient, the transfer must be rejected.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 52 — Transfers between owned accounts

**PRD:** If funds are insufficient, both balances must remain unchanged.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 53 — Transfers between owned accounts

**PRD:** If funds are insufficient, no completed transfer must appear in history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 54 — Transfers between owned accounts

**PRD:** A valid transfer is atomic: the source balance decreases by the amount.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 55 — Transfers between owned accounts

**PRD:** A valid transfer is atomic: the destination balance increases by the same amount.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 56 — Transfers between owned accounts

**PRD:** No partial transfer is allowed.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 57 — Transfers between owned accounts

**PRD:** A successful transfer creates one completed transfer record.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 58 — Transfers between owned accounts

**PRD:** A successful transfer record can be found in both relevant account histories.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 59 — Transfers between owned accounts

**PRD:** The transfer record shows the amount.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 60 — Transfers between owned accounts

**PRD:** The transfer record shows the date and time.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 61 — Transfers between owned accounts

**PRD:** The transfer record shows the source account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 62 — Transfers between owned accounts

**PRD:** The transfer record shows the destination account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 63 — Transfers between owned accounts

**PRD:** The transfer record shows the status.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 64 — Transfers between owned accounts

**PRD:** The transfer record shows the memo if supplied.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 65 — Transfers between owned accounts

**PRD:** The UI reports success only after the transfer has been committed.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 66 — Transfers between owned accounts

**PRD:** If a transfer is rejected or fails, the UI must explain that it did not complete.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 67 — Transfers between owned accounts

**PRD:** If a transfer is rejected or fails, the UI must not show a success state.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 68 — Transfers between owned accounts

**PRD:** Refreshing after a successful transfer must preserve the updated balances.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 69 — Transfers between owned accounts

**PRD:** Refreshing after a successful transfer must preserve the transaction record.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 70 — Transaction history

**PRD:** The user can view a combined transaction history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 71 — Transaction history

**PRD:** The user can view account-specific history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 72 — Transaction history

**PRD:** Each transaction history row shows date and time.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 73 — Transaction history

**PRD:** Each transaction history row shows description or memo.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 74 — Transaction history

**PRD:** Each transaction history row shows transaction type.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 75 — Transaction history

**PRD:** Each transaction history row shows amount.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 76 — Transaction history

**PRD:** Each transaction history row shows status.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 77 — Transaction history

**PRD:** Each transaction history row shows relevant account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 78 — Transaction history

**PRD:** Amount direction should be clear for deposits.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 79 — Transaction history

**PRD:** Amount direction should be clear for withdrawals.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 80 — Transaction history

**PRD:** Amount direction should be clear for transfers.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 81 — Transaction history

**PRD:** The user can filter history by account.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 82 — Transaction history

**PRD:** The user can filter history by transaction type.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 83 — Transaction history

**PRD:** The user can filter history by status.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 84 — Transaction history

**PRD:** The user can filter history by date range.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 85 — Transaction history

**PRD:** When filters are applied, every displayed row must satisfy all selected filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 86 — Transaction history

**PRD:** The start and end dates for history filters are inclusive.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 87 — Transaction history

**PRD:** A transaction occurring on either boundary date must be included when it matches the other filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 88 — Transaction history

**PRD:** An empty result set must show a clear empty state.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 89 — Transaction history

**PRD:** An empty result set must not show an error.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 90 — Transaction history

**PRD:** An empty result set must not show unrelated transactions.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 91 — Transaction history

**PRD:** Clearing filters restores the unfiltered history.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 92 — Profile

**PRD:** A profile view displays only synthetic demo-customer details.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 93 — Profile

**PRD:** The profile view displays the demo-customer's display name.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 94 — Profile

**PRD:** The profile view displays the demo-customer's masked email address.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 95 — Profile

**PRD:** The profile view must not reveal passwords.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 96 — Profile

**PRD:** The profile view must not reveal authentication tokens.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 97 — Profile

**PRD:** The profile view must not reveal full account identifiers.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 98 — Profile

**PRD:** The profile view must not reveal data belonging to another user.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 99 — General interface behavior

**PRD:** The target works in a current desktop browser.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 100 — General interface behavior

**PRD:** The target works at a 1280 × 800 viewport.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 101 — General interface behavior

**PRD:** The target remains usable at narrower widths than 1280x800.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 102 — General interface behavior

**PRD:** Interactive controls have readable labels.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 103 — General interface behavior

**PRD:** Interactive controls communicate loading states.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 104 — General interface behavior

**PRD:** Interactive controls communicate success states.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 105 — General interface behavior

**PRD:** Interactive controls communicate validation states.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 106 — General interface behavior

**PRD:** Interactive controls communicate failure states.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 107 — General interface behavior

**PRD:** A submitted action should not silently disappear.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 108 — General interface behavior

**PRD:** While waiting for a submitted action, the UI should show a loading state.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 109 — General interface behavior

**PRD:** While waiting for a submitted action, the UI should prevent accidental duplicate submission.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 110 — General interface behavior

**PRD:** Navigation links and buttons lead to the labeled destination.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 111 — General interface behavior

**PRD:** Navigation links and buttons perform the labeled action.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 112 — General interface behavior

**PRD:** A recoverable error must leave the user able to retry.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 113 — General interface behavior

**PRD:** A recoverable error must leave the user able to return to the dashboard.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 114 — Seed data expectations

**PRD:** The demo begins with enough historical transactions to exercise account filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 115 — Seed data expectations

**PRD:** The demo begins with enough historical transactions to exercise type filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 116 — Seed data expectations

**PRD:** The demo begins with enough historical transactions to exercise status filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 117 — Seed data expectations

**PRD:** The demo begins with enough historical transactions to exercise date filters.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 118 — Seed data expectations

**PRD:** Seed records should include multiple dates.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 119 — Seed data expectations

**PRD:** Seed records should include at least one transfer between the two accounts.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 120 — Seed data expectations

**PRD:** The demo has no signup features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 121 — Seed data expectations

**PRD:** The demo has no external payment features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 122 — Seed data expectations

**PRD:** The demo has no bill-pay features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 123 — Seed data expectations

**PRD:** The demo has no loan features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 124 — Seed data expectations

**PRD:** The demo has no card features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

### 125 — Seed data expectations

**PRD:** The demo has no multi-user features.

**Verdict:** `unverified` — Not covered by automated suite

- **Expected:** See PRD.
- **Observed:** No automated check mapped.

