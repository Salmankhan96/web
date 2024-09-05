from odoo import fields, models, _,api

class WebsiteSlider(models.Model):
    _name = "website.slider"
    _description = "Website Slider"

    name = fields.Char(translate=True)
    summary = fields.Char(translate=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id)
    slider_image = fields.Binary(attachment=True, help="This field holds the image used as image for the slider.")
    slider_video = fields.Binary(attachment=True, help="This field holds the video used as video for the slider.")
    active = fields.Boolean(default=True, help="Set active to false to hide the Slider without removing it.")
    partner_logo = fields.Binary(attachment=True, help="This field holds the image used as image for the logo.")


class WebsiteServices(models.Model):
    _name = "website.services"
    _description = "Website Service"

    name = fields.Char(translate=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id)
    service_logo = fields.Binary(attachment=True, help="This field holds the image used as image for the slider.")
    url = fields.Char(string="Service URL")
    active = fields.Boolean(default=True, help="Set active to false to hide the Slider without removing it.")

class DemoRequest(models.Model):
    _name = 'demo.request'
    _description = 'Demo Request'

    name = fields.Char(string="Full Name")
    email = fields.Char(string="Email")
    app_name = fields.Char(string="App/Module Name")
    odoo_platform = fields.Selection([('odoo.sh', 'Odoo.sh'), ('on_premise', 'On Premise')], string="Odoo Platform")
    version = fields.Selection([('17.0', '17.0'), ('16.0', '16.0'), ('15.0', '15.0')], string="Version")
    skype_id = fields.Char(string="Skype ID")
    whatsapp_number = fields.Char(string="WhatsApp Number")
