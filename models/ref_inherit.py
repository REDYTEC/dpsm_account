from odoo import api, fields, models, _, tools


# calling all modules that just need inheritance but do not need extra fields

class SaleOrder(models.Model):
    _inherit = "account.move"


class CalendarInherit(models.Model):
    _inherit = "calendar.event"


class CrmInherit(models.Model):
    _inherit = "purchase.order"


class StockInherit(models.Model):
    _inherit = "stock.picking"
