# -*- coding: utf-8 -*-
{
    'name': "bi_sale",

    'summary': "",

    'description': "",

    'author': "Bassam Infotech LLP",
    'website': "http://www.bassaminfotech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/paperformat.xml',
        'reports/report.xml',
        'reports/report_template.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
