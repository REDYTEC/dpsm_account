# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SaleInherit(models.Model):
    _inherit = "sale.order"

    psm = fields.Boolean(string='Cuentas PSM', tracking=True)
    zk = fields.Boolean(string='Cuentas ZK', tracking=True)

