{
    'name': 'Coralbound Theme',
    'version': '17.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Custom theme for Coralbound with primary blue colors and custom navbar',
    'description': """
        Custom Odoo theme for Coralbound featuring:
        - Custom primary blue color scheme
        - Custom navbar styling
        - Modern UI improvements
        - Remove "Powered by Odoo" footer
    """,
    'author': 'Coralbound',
    'website': 'https://coralbound.com',
    'license': 'LGPL-3',
    'depends': ['web', 'base'],
    'assets': {
        'web.assets_backend': [
            'coralbound_theme/static/src/css/theme.css',
            'coralbound_theme/static/src/css/remove_footer.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
