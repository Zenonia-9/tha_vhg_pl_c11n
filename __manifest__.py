# -*- coding: utf-8 -*-
{
    "name": "VHG Partner Ledger Customization",
    "summary": "Adds Anzer columns to the original Partner Ledger report.",
    "version": "19.0.1.0.0",
    "category": "Accounting/Accounting",
    "author": "Thein Htoo Aung",
    "license": "LGPL-3",
    "depends": [
        "account_reports",
    ],
    "data": [
        "data/partner_ledger.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "tha_vhg_pl_c11n/static/src/components/account_report/filters/filter_vhg_pl_account.xml",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
