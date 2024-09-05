# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SK Website',
    'version' : '1.2',
    'summary': 'SK Technology',
    'sequence': 10,
    'description': """For Testing purpose....""",
    'category': 'Tech',
    'depends': ['base','website'],
    'data': [
            'views/website_slider_views.xml',
            'views/website_template.xml',
            'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            'sk_website/static/src/scss/website.scss',
            'sk_website/static/src/js/website.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
