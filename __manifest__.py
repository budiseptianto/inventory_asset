{
    'name': 'Inventory Asset Management',
    'version': '1.0',
    'summary': 'Manage company assets with history, QR code, and integration features',
    'description': 'Comprehensive asset tracking and management with integration to Purchase, Maintenance, and Accounting modules.',
    'author': 'Budi Septianto',
    'category': 'Inventory',
    'depends': ['base', 'purchase', 'maintenance', 'account'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/asset_sequence.xml',
        'views/asset_views.xml',
        'views/asset_history_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {},
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
