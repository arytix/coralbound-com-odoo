{
    'name': 'Remove Powered by Odoo',
    'version': '17.0.1.0.0',
    'summary': 'Remove "Powered by Odoo" footer from web interface',
    'description': """
        This module removes the "Powered by Odoo" footer from the web interface
        by overriding the web template.
    """,
    'author': 'Coralbound',
    'website': 'https://coralbound.com',
    'category': 'Web',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {},
    'installable': True,
    'auto_install': False,
    'application': False,
}
