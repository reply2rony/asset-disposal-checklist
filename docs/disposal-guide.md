# Asset Disposal Checklist — Guide

A starter guide for retiring IT assets safely. This is a learning
template — adapt the stages to your own organisation's policy. All
assets, people, and examples below are fictional.

## The six stages

### 1. Identify

Record the asset tag, type, location, and reason for disposal
(end of life, broken beyond repair, replaced). One row per asset in
`asset-disposal-checklist.csv`. Keep the asset in a secure holding
area until the process finishes — never leave retiring kit in a
public corridor or an unlocked cupboard.

### 2. Assess

Check the condition and whether the asset holds data. A laptop, a
hard drive, a phone, and a USB stick are data-bearing even if they
no longer switch on — a dead drive can still be read. Note the
storage type (HDD, SSD, flash) because the wipe method depends on
it. Note anything hazardous (swollen battery, cracked screen) so
the disposal vendor handles it safely.

### 3. Approve

An IT manager approves the disposal and picks the method: recycle,
resell, donate, or destroy. Resale and donation are only for
working, wiped devices. Approval is recorded with a name and a date
— an unsigned disposal is not a disposal.

### 4. Wipe

Data-bearing devices are wiped or destroyed **before** they leave
the building:

- **HDD:** overwrite with a certified wipe tool, or physical
  destruction (degauss / shred) for sensitive drives.
- **SSD / flash:** use the manufacturer's secure-erase command;
  overwriting alone is not reliable on flash.
- **Phone / tablet:** factory reset, then remove the account lock
  and check the device is no longer tied to an account.

Record the wipe method, the tool used, and who verified it. If a
wipe fails or cannot be verified, the device is destroyed instead.

### 5. Dispose

Hand the asset to the chosen route and get proof: a recycling
certificate, a resale receipt, a donation letter, or a destruction
certificate. File the proof against the asset row. Never put IT
kit in general waste — batteries and screens are hazardous waste
in most places.

### 6. Record

Close the asset row: final status, disposal date, proof filed.
Update the asset register so the item no longer shows as live.
Keep the records for as long as your organisation's policy
requires — the audit trail is the point of the whole process.

## Common mistakes (starter notes)

- Skipping the wipe because a device "won't turn on".
- Reselling a drive that was only quick-formatted.
- No approval recorded, so nobody can prove the disposal was
  authorised.
- Proof of disposal filed nowhere, so the asset still looks live
  in the register a year later.

## Adding your own assets

Add a row to `asset-disposal-checklist.csv` with: asset_tag, type,
location, condition, data_bearing, status, disposal_method,
wipe_method, approved_by, and notes. Keep asset tags fictional in
samples — never commit real serial numbers or real user names.

## Sample / Demo notice

All assets and examples here are fictional samples for learning,
labelled "Sample / Demo" in the diagram. This template does not
claim any production use.
