{
    'name': 'Custom Account View',
    'author': 'RED Y TEC',
    'version': '1.0',
    'summary': 'Changes views on account module',
    'description': """Cambia la vista de formulario y la vista de árbol para mostrar referencias en el módulo de facturación""",
    'category': 'Extra Tools',
    'website': 'http://www.redytec.com',
    'depends': [
        'account',
        'sale'
    ],
    'data': [
        'views/account_view.xml',
        'views/sale_report_inherit.xml'
        'views/goat.jpg'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto:install': False,
}