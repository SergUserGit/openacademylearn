# -*- coding: utf-8 -*-

{
    'name': 'openacademy',
    'summary': 'openacademy',
    'description': """openacademy""",
    #  'author': "My Company",
    'website': 'http://www.yourcompany.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',
    'sequence': 1,
    # any module necessary for this one to work correctly
    'depends': ['base','board'],
    # always loaded
    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'wizard/cancel_openacademy_view.xml',
        'views/views.xml',
        'views/session_views.xml',
        'views/menues.xml',
        'views/templates.xml',
        'views/openacademy_lost_reason_views.xml',
        'views/openacademy_session_lost_reason_views.xml',
        'views/openacademy_dashboard.xml',
        'reports/session_card.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
