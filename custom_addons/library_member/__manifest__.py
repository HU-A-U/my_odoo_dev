# -*- coding: utf-8 -*-
{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Alan Hou',
    # 'depends': ['library_app','mail'],
    'depends': ['library_app'],
    'data':[
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
    ],
    'application': False,
}