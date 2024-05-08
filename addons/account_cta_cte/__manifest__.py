# -*- coding: utf-8 -*-
{
    'name': 'Cuentas Bancarias',
    'summary': 'Administra las cuentas del banco',
    'version': '1.0',
    'description': 'Puedes generar reportes y ver en tiempo real los saldos de las cuentas bancarias',
    'author': 'Renato Monroy',
    'licence': 'GPL-2',
    'category': 'Services',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'report/acc_template.xml',
        'report/acc_views.xml',
        'views/acc_menus.xml',
        'views/acc_views.xml',
    ],
    'installable': True,
    'application': True
}
