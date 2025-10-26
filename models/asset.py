from odoo import models, fields, api
import base64, qrcode
from io import BytesIO

class AssetMaster(models.Model):
    _name = 'asset.master'
    _description = 'Inventory Asset Management'
    _rec_name = 'hostname'
    _order = 'purchase_date desc'

    hostname = fields.Char(string='Hostname', required=True)
    brand = fields.Char(string='Brand')
    type = fields.Char(string='Type')
    serial_number = fields.Char(string='Serial Number')
    mac_address = fields.Char(string='MAC Address')
    os = fields.Char(string='Operating System')
    processor = fields.Char(string='Processor')
    hdd = fields.Integer(string='HDD (GB)')
    ram = fields.Integer(string='RAM (GB)')
    location = fields.Char(string='Location')
    current_user = fields.Char(string='Current User')
    subsidiary = fields.Char(string='Subsidiary')
    position = fields.Char(string='Position')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
        ('disposed', 'Disposed')
    ], string='Status', default='active')
    vendor_name = fields.Char(string='Vendor Name')
    purchase_date = fields.Date(string='Purchase Date')
    price = fields.Integer(string='Price')
    keterangan = fields.Text(string='Keterangan')
    remark = fields.Text(string='Remark')
    placement = fields.Char(string='Placement')
    history_ids = fields.One2many('asset.history', 'asset_id', string='History')
    qr_code = fields.Binary("QR Code", compute='_generate_qr_code', store=True)

    @api.depends('hostname', 'serial_number')
    def _generate_qr_code(self):
        for rec in self:
            qr = qrcode.make(f"Asset: {rec.hostname}\nSN: {rec.serial_number}")
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            rec.qr_code = base64.b64encode(buffer.getvalue())

    @api.onchange('status')
    def _auto_maintenance_request(self):
        if self.status == 'maintenance':
            self.env['maintenance.request'].create({
                'name': f'Maintenance for {self.hostname}',
                'asset_id': self.id,
                'request_date': fields.Datetime.now(),
            })
