# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools import SQL


class AccountPartnerLedgerReportHandler(models.AbstractModel):
    _inherit = "account.partner.ledger.report.handler"

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
