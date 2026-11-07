# Asset Disposal Checklist — Starter Template

A starter learning template for retiring IT assets safely: laptops,
desktops, drives, phones, and printers. It is a checklist plus a small
tracking CSV, so an IT team can record each asset from "identified for
disposal" through data wipe, approval, and final disposal — with nothing
lost and no data left on a device that leaves the building. Sample content
only — no real company data, no invented metrics, and no claim of
production use.

## What it is

- `docs/disposal-guide.md` — the disposal workflow and the checklist:
  identify, assess, approve, wipe, dispose, record.
- `asset-disposal-checklist.csv` — the tracking sheet in CSV form, so you
  can copy it, filter it, and add your own assets.
- `scripts/disposal-summary.py` — a starter Python script that summarises
  the CSV by status and disposal method, and flags items still waiting for
  a data wipe. Labelled a starter learning template; it is not a
  production tool.

## How to use

1. Add each retiring asset to `asset-disposal-checklist.csv` with its
   asset tag, type, condition, and planned disposal method.
2. Work the checklist in `docs/disposal-guide.md` in order — no asset
   moves to the next stage until the current stage is signed off.
3. Data-bearing devices (laptops, drives, phones) must be wiped or
   destroyed before they leave the building; record the wipe method and
   who verified it.
4. Summarise the sheet from the command line:

```bash
python3 scripts/disposal-summary.py asset-disposal-checklist.csv
python3 scripts/disposal-summary.py asset-disposal-checklist.csv --status pending-wipe
python3 scripts/disposal-summary.py asset-disposal-checklist.csv --method recycle
```

## Disposal stages (starter guide)

| Stage | What happens | Sign-off |
|-------|--------------|----------|
| Identify | Asset tagged for disposal, reason recorded | Requester |
| Assess | Condition checked, data-bearing or not | IT technician |
| Approve | Disposal approved, method chosen | IT manager |
| Wipe | Data wiped or media destroyed, verified | IT technician |
| Dispose | Recycled, resold, donated, or destroyed | IT manager |
| Record | Certificate / receipt filed, asset closed | IT admin |

Stages above are starter suggestions for a learning template, not a
standard for any real organisation.

## Sample / Demo notice

All assets, people, and examples in this repo are fictional samples for
learning. The diagram in `docs/diagram.png` is a locally generated
illustration labelled "Sample / Demo" — it is not a screenshot of a real
system, and this template does not claim any production use.

## License

MIT — see `LICENSE`.
