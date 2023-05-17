# -*- coding: utf-8 -*-
{
    'name': "Employee",

    'summary': """
        Centralize employee information""",

    'description': """
        Centralize employee information
    """,

    'author': "HabibMhamadi",
    'website': "https://www.github.com/habibmhamadi",
    'category': 'Employees',
    'version': '0.1',

    'depends': ['base', 'mail', 'resource', 'hm_master'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employee_document.xml',
        'views/department.xml',
        'views/job.xml',
        'views/employee.xml',
    ],
    'application': True
}
