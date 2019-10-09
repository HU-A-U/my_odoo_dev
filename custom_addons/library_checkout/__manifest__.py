# -*- coding: utf-8 -*-
{
    'name': 'Library Book Borrowing',
    'description': 'Members can borrow books from the library.',
    'author': 'HU',
    'depends': ['library_member','mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/checkout_views.xml',
        'data/library_checkout_stage.xml',
        'views/checkout_kanban_view.xml',
    ],
}