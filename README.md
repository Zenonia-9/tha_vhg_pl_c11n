# THA VHG Partner Ledger Customization

![Odoo 19](https://img.shields.io/badge/Odoo-19.0-875A7B?style=flat-square)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Category](https://img.shields.io/badge/Category-Accounting-4ECDC4?style=flat-square)

Extend the native Partner Ledger report with Anzer and reference columns for Odoo 19.

This addon customizes the original `account_reports` Partner Ledger in place. It adds **Anzer ID** and **Anzer Reference** columns to move-line rows while keeping the standard report action, menu, filters, unfold behavior, PDF export, and XLSX export intact.

## Highlights

- Adds **Anzer ID**, **Anzer Reference**, and **Reference** columns to the native Partner Ledger.
- Reuses the original `account.partner.ledger.report.handler`.
- Reads values from `account.move.anzer_id` and `account.move.vendor_ref`.
- Keeps partner summary and total lines unchanged.
- Avoids cloning the full report definition.

## Technical Notes

- `data/partner_ledger.xml`
  Declares the new `account.report.column` records on the existing Partner Ledger report.
- `models/account_partner_ledger.py`
  Extends the native Partner Ledger query hook to include Anzer fields from the related journal entry.

## Module Layout

```text
tha_vhg_pl_c11n/
|-- data/
|-- models/
`-- __manifest__.py
```

## Dependencies

- `account_reports`
- `anzer_odoo_integration`

## Installation

1. Place the module in your custom addons path.
2. Update the Apps list in Odoo.
3. Install **THA VHG Partner Ledger Customization**.

## License

This module is licensed under `LGPL-3`.
