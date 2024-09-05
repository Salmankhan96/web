from odoo import fields, models, _,api

class SKTech(models.Model):
    _name = 'sk.tech'

    sequence = fields.Char(string="Sequence" ,index=True,copy=False,default=lambda self: _('New'))
    name = fields.Char(string="Name")
    dob = fields.Date(string="Date Of Birth")
    partner = fields.Many2one('res.partner',string="Partner")


    @api.model
    def create(self, vals_list):
        if vals_list.get('sequence','New') =='New':
            vals_list['sequence'] = self.env['ir.sequence'].next_by_code('sk.tech') or 'New'
            result = super(SKTech,self).create(vals_list)
            return result