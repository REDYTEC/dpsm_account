# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SaleInherit(models.Model):
    # _inherit = "sale.order"
    _inherit = "sale.order.line"

    psm = fields.Boolean(string='Cuentas PSM')
    zk = fields.Boolean(string='Cuentas ZK')

