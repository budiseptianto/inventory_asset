from odoo import models, fields

class AssetHistory(models.Model):
    _name = 'asset.history'
    _description = 'Asset Movement History'
    _order = 'date desc'

    asset_id = fields.Many2one('asset.master', string='Asset', ondelete='cascade')
    from_location = fields.Char(string='From Location')
    to_location = fields.Char(string='To Location')
    moved_by = fields.Char(string='Moved By')
    date = fields.Datetime(string='Move Date', default=fields.Datetime.now)
    note = fields.Text(string='Note')
