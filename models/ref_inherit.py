from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = "account.move"


class CalendarInherit(models.Model):
    _inherit = "calendar.event"
