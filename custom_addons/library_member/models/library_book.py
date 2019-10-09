# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Book(models.Model):
    '''
    继承library.book模型,添加is_available字段
    '''
    _inherit = 'library.book'
    is_available = fields.Boolean(string='Is Available')
    isbn = fields.Char(help='稍后会支持ISBN-10')
    publisher_id = fields.Many2one(index=True)

    @api.multi
    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-','')
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            total = sum(a * b for a, b in zip(digits[:9], ponderators))
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()