# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = "account.move"