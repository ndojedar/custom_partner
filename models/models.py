# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    metodo_pago = fields.Many2one('payment.acquirer', 'Método de pago')


