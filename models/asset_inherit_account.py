from odoo import models, fields

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    asset_ref_id = fields.Many2one('asset.master', string='Linked Inventory Asset')
