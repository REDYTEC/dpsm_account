# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = "account.move"


class SaleInherit(models.Model):
    _inherit = "sale.order"

    client = fields.Boolean(string='Cliente')
    supplier = fields.Boolean(string='Proveedor')

