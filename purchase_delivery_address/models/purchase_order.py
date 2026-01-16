from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_address_id = fields.Many2one(
        'res.partner',
        string='Teslimat Adresi',
        help="Custom address to override the default warehouse delivery address."
    )
