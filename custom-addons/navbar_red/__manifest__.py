{
    'name': 'Red Navbar',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Changes the Odoo top bar color to red',
    'description': """
        This module changes the Odoo top navigation bar color to red.
    """,
    'author': 'Coralbound',
    'website': 'https://coralbound.com',
    'license': 'LGPL-3',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'navbar_red/static/src/css/navbar.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
