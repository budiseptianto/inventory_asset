from odoo import models, fields

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    asset_id = fields.Many2one('asset.master', string='Related Asset')
