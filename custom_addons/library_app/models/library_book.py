# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning


class Book(models.Model):
    _name = 'library.book'
    _description = '书籍'

    name = fields.Char(string='书名',required=True) #书籍名称
    price = fields.Float(string='单价') # 价格
    on_sale = fields.Boolean(string='是否在售',default = True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Active?',default=True)
    date_published = fields.Date(string='出版日期')      #　出版时间
    image = fields.Binary(string='Cover')      #  存储图书封面的二进制字段
    publisher_id = fields.Many2one('res.partner',string='出版社')        #  出版公司多对一关联
    author_ids = fields.Many2many('res.partner',string="作者")           #  作者多对多关联


    @api.multi
    def _check_isbn(self):
        #校验isbn号码
        self.ensure_one()
        #isbn编码为13位，验证规则，最后一位为前面12位的
        isbn = self.isbn.replace('-','')
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please privide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
            return True

