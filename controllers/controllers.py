# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPartner(http.Controller):
#     @http.route('/custom_partner/custom_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_partner/custom_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_partner.listing', {
#             'root': '/custom_partner/custom_partner',
#             'objects': http.request.env['custom_partner.custom_partner'].search([]),
#         })

#     @http.route('/custom_partner/custom_partner/objects/<model("custom_partner.custom_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_partner.object', {
#             'object': obj
#         })
