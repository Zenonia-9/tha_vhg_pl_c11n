# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools import SQL


class AccountPartnerLedgerReportHandler(models.AbstractModel):
    _inherit = "account.partner.ledger.report.handler"

    def _get_additional_column_aml_values(self):
        return SQL(
            """
            %(super_columns)s
            account_move.anzer_id AS anzer_id,
            account_move.vendor_ref AS vendor_ref,
            """,
            super_columns=super()._get_additional_column_aml_values(),
        )
