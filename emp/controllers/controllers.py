# -*- coding: utf-8 -*-
# from odoo import http


# class Emp(http.Controller):
#     @http.route('/emp/emp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emp/emp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('emp.listing', {
#             'root': '/emp/emp',
#             'objects': http.request.env['emp.emp'].search([]),
#         })

#     @http.route('/emp/emp/objects/<model("emp.emp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emp.object', {
#             'object': obj
#         })
