# -*- coding: utf-8 -*-
# from odoo import http


# class ImOdLivestockAdvanced(http.Controller):
#     @http.route('/im_od_livestock_advanced/im_od_livestock_advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/im_od_livestock_advanced/im_od_livestock_advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('im_od_livestock_advanced.listing', {
#             'root': '/im_od_livestock_advanced/im_od_livestock_advanced',
#             'objects': http.request.env['im_od_livestock_advanced.im_od_livestock_advanced'].search([]),
#         })

#     @http.route('/im_od_livestock_advanced/im_od_livestock_advanced/objects/<model("im_od_livestock_advanced.im_od_livestock_advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('im_od_livestock_advanced.object', {
#             'object': obj
#         })
