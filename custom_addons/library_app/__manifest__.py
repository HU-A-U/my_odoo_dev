# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # 'category': 'Uncategorized',
    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/book_list_template.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'reports/library_book_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    # 'application' ：布尔型标记，代表模块是在应用列表中以APP展现；
	# 'installable' ：默认为True，但可以通过设置为False来禁用模块；
	# 'auto_install' ：若设置为True，在其依赖已安装时会自动安装，主要用于同一个实例两个模块安装后功能的链接。
    'application':True,
}