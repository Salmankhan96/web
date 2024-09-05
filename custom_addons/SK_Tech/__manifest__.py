# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SK Tech',
    'version' : '1.2',
    'summary': 'SK Technology',
    'sequence': 10,
    'description': """For Testing purpose....""",
    'category': 'Tech',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/tech_view.xml',
        'views/website_slider_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
