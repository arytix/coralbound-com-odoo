{
    'name': 'Coralbound Theme',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom theme for Coralbound Odoo instance',
    'description': """
        This module customizes the Odoo interface with Coralbound branding:
        - Custom logo
        - Primary and secondary colors
        - Custom styling
    """,
    'author': 'Coralbound',
    'website': 'https://coralbound.com',
    'license': 'LGPL-3',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'coralbound_theme/static/src/css/theme.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
