#!/usr/bin/env python3
"""Compare two regional price-observation arrays and flag changes for confirmation."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

CONTEXT_FIELDS = ("availability", "seller", "shipping_context", "tax_context", "member_or_promo_context")


def key(row: dict) -> tuple:
    return row.get("product_id"), row.get("variant_id"), row.get("observed_location")


def comparable(row: dict) -> bool:
    return str(row.get("validation_status", "confirmed") or "").lower() in {"confirmed", "ok", "valid"}


def compare(previous: list[dict], current: list[dict], threshold_pct: Decimal) -> list[dict]:
    old = {key(row): row for row in previous if comparable(row)}
    changes: list[dict] = []
    for row in current:
        if not comparable(row):
            continue
        observation_key = key(row)
        prior = old.get(observation_key)
        if not prior:
            continue

        change = {
            "key": observation_key,
            "currency": row.get("currency"),
            "changed_fields": {},
            "requires_confirmation": True,
        }

        if row.get("currency") == prior.get("currency"):
            try:
                before = Decimal(str(prior["normalized_price"]))
                after = Decimal(str(row["normalized_price"]))
                if before != 0:
                    pct = ((after - before) / before) * 100
                    if abs(pct) >= threshold_pct:
                        change["changed_fields"]["normalized_price"] = {
                            "before": str(before),
                            "after": str(after),
                            "change_pct": str(pct.quantize(Decimal("0.01"))),
                        }
            except (KeyError, InvalidOperation):
                pass

        for field in CONTEXT_FIELDS:
            if row.get(field) != prior.get(field):
                change["changed_fields"][field] = {
                    "before": prior.get(field),
                    "after": row.get(field),
                }

        if change["changed_fields"]:
            changes.append(change)
    return changes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous", type=Path)
    parser.add_argument("current", type=Path)
    parser.add_argument("--threshold-pct", type=Decimal, default=Decimal("5"))
    args = parser.parse_args()
    previous = json.loads(args.previous.read_text(encoding="utf-8"))
    current = json.loads(args.current.read_text(encoding="utf-8"))
    print(json.dumps(compare(previous, current, args.threshold_pct), indent=2))


if __name__ == "__main__":
    main()
