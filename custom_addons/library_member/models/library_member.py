# -*- coding: utf-8 -*-

from odoo import models,fields

class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    # _inherit = ['mail.thread','mail.activity.mixin']

    card_number = fields.Char(string='会员卡号')
    partner_id = fields.Many2one(
        'res.partner',  #继承partner，使用地址联系的字段
        delegate=True,  #指定为代理继承
        ondelete='cascade',
        required=True
    )
