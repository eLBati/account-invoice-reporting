# -*- coding: utf-8 -*-
# Copyright 2013-2017 Lorenzo Battistini - Agile Business Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.one
    def _get_prod_lots(self):
        if not self.move_line_ids and not self.order_lines:
            return
        if self.move_line_ids:
            self.prod_lot_ids = self.mapped(
                'move_line_ids.lot_ids')
        else:
            self.prod_lot_ids = self.mapped(
                'order_lines.procurement_ids.move_ids.lot_ids')

    order_lines = fields.Many2many(
        'sale.order.line', 'sale_order_line_invoice_rel', 'invoice_id',
        'order_line_id', 'Order Lines', readonly=True)

    prod_lot_ids = fields.Many2many(
        'stock.production.lot',  'stock_prod_lot_invoice_rel', 'invoice_id',
        compute='_get_prod_lots', string="Production Lots")

    lot_formatted_note = fields.Html(
        'Formatted Note', compute='load_line_lots')

    @api.one
    def load_line_lots(self):
        if self.prod_lot_ids:
            note = u'<ul>'
            note += u' '.join([
                u'<li>S/N {0}</li>'.format(lot.name)
                for lot in self.prod_lot_ids
            ])
            note += u'</ul>'
            self.lot_formatted_note = note
