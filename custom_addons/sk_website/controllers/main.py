# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.portal.controllers.web import Home
from odoo import http
import json
from odoo.http import request

class Website(Home):


    @http.route(['/','/home'], auth="public", website=True, sitemap=True)
    def home(self, **kw):
        values = {}
        slider = request.env['website.slider'].search([])
        services = request.env['website.services'].search([])
        values['services'] = services
        values['slider'] = slider
        return request.render("sk_website.custom_homepage", values)

    @http.route('/odoo-implementation', auth="public", website=True, sitemap=True)
    def OdooImplementation(self, **kw):
        return request.render("sk_website.odoo_implementation")

    @http.route('/odoo-integration', auth="public", website=True, sitemap=True)
    def OdooIntegration(self, **kw):
        return request.render("sk_website.odoo_integration")

    @http.route(['/odoo-maintenance','/odoo-support'], auth="public", website=True, sitemap=True)
    def OdooMaintenance(self, **kw):
        return request.render("sk_website.odoo_maintenance")

    @http.route('/odoo-development', auth="public", website=True, sitemap=True)
    def OdooDevelopment(self, **kw):
        return request.render("sk_website.odoo_development")

    @http.route('/odoo-migration', auth="public", website=True, sitemap=True)
    def OdooMigration(self, **kw):
        return request.render("sk_website.odoo_migration")

    @http.route('/odoo-consultancy', auth="public", website=True, sitemap=True)
    def OdooConsultancy(self, **kw):
        return request.render("sk_website.odoo_consultancy")

    @http.route('/odoo-training', auth="public", website=True, sitemap=True)
    def OdooTraining(self, **kw):
        return request.render("sk_website.odoo_training")

    @http.route('/aboutus', auth="public", website=True, sitemap=True)
    def AboutUs(self, **kw):
        return request.render("sk_website.about_us")

    @http.route('/demo-request', auth="public", website=True, sitemap=True)
    def DemoRequest(self, **kw):
        return request.render("sk_website.demo_request")

    @http.route('/website/demo-request/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        print("dfghjk")
        with request.env.cr.savepoint():
            data_dict = {
                "name": kwargs.get('user_name', ''),
                "email": kwargs.get('email_id', ''),
                "app_name": kwargs.get('module_name', ''),
                "version": kwargs.get('version', ''),
                "skype_id": kwargs.get('skype_id', ''),
                "whatsapp_number": kwargs.get('number', '')
            }
            data = request.env['demo.request'].sudo().create(data_dict)
            return json.dumps({'id': data.id})




