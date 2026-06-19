# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools import SQL


class AccountPartnerLedgerReportHandler(models.AbstractModel):
    _inherit = "account.partner.ledger.report.handler"

    def _custom_options_initializer(self, report, options, previous_options):
        super()._custom_options_initializer(report, options, previous_options=previous_options)

        previous_options = previous_options or {}
        previous_account_ids = previous_options.get("account_ids") or []
        selected_account_ids = [int(account_id) for account_id in previous_account_ids]
        selected_accounts = selected_account_ids and self.env["account.account"].with_context(active_test=False).search([
            ("id", "in", selected_account_ids),
            ("account_type", "in", ("asset_receivable", "liability_payable")),
            *self.env["account.account"]._check_company_domain(report.get_report_company_ids(options)),
        ]) or self.env["account.account"]

        options["vhg_pl_account_filter"] = True
        options["account_ids"] = selected_accounts.ids
        options["selected_account_ids"] = selected_accounts.mapped("display_name")

        if selected_accounts:
            options["forced_domain"] = options.get("forced_domain", []) + [("account_id", "in", selected_accounts.ids)]

    def _get_additional_column_aml_values(self):
        return SQL(
            """
            %(super_columns)s
            COALESCE(account_move.anzer_id, '') AS anzer_id,
            COALESCE(account_move.vendor_ref, '') AS vendor_ref,
            COALESCE(account_move.name, '') AS invoice_no,
            """,
            super_columns=super()._get_additional_column_aml_values(),
        )
