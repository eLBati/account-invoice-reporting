# -*- coding: utf-8 -*-
# Copyright 2013-2017 Lorenzo Battistini - Agile Business Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


{
    "name": "Invoice Production Lots",
    "version": "10.0.0.1.0",
    'category': 'Generic Modules/Accounting',
    "depends": [
        "account_accountant",
        "sale_stock",
        "stock_picking_invoice_link",
        ],
    "author": "Agile Business Group,Odoo Community Association (OCA)",
    "summary": "Display delivered serial numbers in invoice",
    'website': 'http://www.agilebg.com',
    'license': 'LGPL-3',
    'data': [
        'views/invoice_view.xml',
        'views/report_invoice.xml',
        ],
    'demo': [
        'demo/sale.yml',
        ],
    'installable': False,
    'active': False,
}
