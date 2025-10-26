from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if 'Asset' in (rec.product_id.categ_id.name or ''):
                self.env['asset.master'].create({
                    'hostname': rec.name,
                    'vendor_name': rec.order_id.partner_id.name,
                    'purchase_date': fields.Date.today(),
                    'price': rec.price_subtotal,
                })
        return records
