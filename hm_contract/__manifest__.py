# -*- coding: utf-8 -*-
{
    'name': "Contract",

    'summary': """
        Manage employee contract""",

    'description': """
        Manage employee contract
    """,

    'author': "HabibMhamadi",
    'website': "https://www.github.com/habibmhamadi",
    'category': 'Employees',
    'version': '0.1',

    'depends': ['base', 'mail', 'resource', 'hm_employee'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/contract.xml'
    ],
    'application': True
}
