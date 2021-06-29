# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = "account.move"


class SaleInherit(models.Model):
    _inherit = "sale.order"

    pay_rate = fields.Many2one('product.pricelist')
    nombre = fields.Char()
    banco = fields.Char()
    cuenta = fields.Char()
    cable = fields.Char()
    rfc = fields.Char()

    def table_condition(self):
        if self.pay_rate == 'Tarifa de Distribuidores (MXN)' or self.pay_rate.name == 'Tarifa de Distribuidores (USD)':
            self.nombre = 'ZKTECO LATAM S.A. DE C.V.'
        else:
            self.nombre = ''

    # psm = fields.Boolean(string='Cuentas PSM')
    # zk = fields.Boolean(string='Cuentas ZK')
