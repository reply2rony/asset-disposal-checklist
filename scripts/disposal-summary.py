#!/usr/bin/env python3
"""Starter learning template: summarise the asset disposal checklist.

Usage:
    python3 scripts/disposal-summary.py asset-disposal-checklist.csv
    python3 scripts/disposal-summary.py asset-disposal-checklist.csv --status pending-wipe
    python3 scripts/disposal-summary.py asset-disposal-checklist.csv --method recycle

Summarises the CSV by status and disposal method, and flags data-bearing
items still waiting for a wipe. Sample data only; no real company data.
"""
import argparse
import csv
import sys
from collections import Counter


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description="Summarise the disposal checklist.")
    ap.add_argument("csv_file", help="path to asset-disposal-checklist.csv")
    ap.add_argument("--status", help="filter by status (e.g. pending-wipe)")
    ap.add_argument("--method", help="filter by disposal method (e.g. recycle)")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.status:
        rows = [r for r in rows if r.get("status", "").lower() == args.status.lower()]
    if args.method:
        rows = [r for r in rows if r.get("disposal_method", "").lower() == args.method.lower()]

    if not rows:
        print("No matching assets.")
        sys.exit(0)

    print(f"Assets: {len(rows)}")
    print()
    print("By status:")
    for status, n in Counter(r.get("status", "") for r in rows).most_common():
        print(f"  {status}: {n}")
    print()
    print("By disposal method:")
    for method, n in Counter(r.get("disposal_method", "") for r in rows).most_common():
        print(f"  {method}: {n}")
    print()
    pending = [r for r in rows
               if r.get("data_bearing", "").lower() == "yes"
               and r.get("status", "").lower() in ("pending-wipe", "identified", "assessed")]
    if pending:
        print("Data-bearing items still waiting for a wipe:")
        for r in pending:
            print(f"  {r['asset_tag']} ({r['type']}, {r['location']}) — {r['status']}")
    else:
        print("No data-bearing items waiting for a wipe.")


if __name__ == "__main__":
    main()
