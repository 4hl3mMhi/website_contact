# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug

""" slug method:
Transform a string to a slug that can be used in a url path.
This method will first try to do the job with python-slugify if present.
Otherwise it will process string by stripping leading and ending spaces,
converting unicode chars to ascii, lowering all chars and replacing spaces
and underscore with hyphen "-".
"""


class WebsiteContact(http.Controller):

    @http.route([
        '''/website_contact/customers''',
        '''/website_contact/customers/page/<int:page>''',
        '''/website_contact/customers/category/<model("res.partner.category"):category>''',
        '''/website_contact/customers/category/<model("res.partner.category"):category>/page/<int:page>'''
    ],type='http', auth="user", website=True)
    def display_customer(self, page=0, search='', category=None):
        """
           params auth="user" means that a only logged user have access to database records.
        """
        url = "/website_contact/customers"
        domain = [('customer_rank', '=', 1)]
        # for search option in template search box
        if search:
            domain += [('name', 'ilike', search)]

        if category:
            domain += [('category_id', '=', category.id)]
            url += "/category/%s" % slug(category)
        else:
            category = request.env['res.partner.category']
        categories = request.env['res.partner.category'].search([])

        Partner = request.env['res.partner']
        total_count = len(Partner.search(domain))
        per_page = 12
        # total : Total count of records
        # page : current page
        # step : count of records need to display in one page
        # scope: count of pages needs to display in a pager at a time
        pager = request.website.pager(url=url, total=total_count, page=page, step=per_page, scope=3, url_args=None)

        # offset : count to exclude (first n)
        partners =  Partner.search(domain, limit=per_page, offset=pager['offset'], order="id asc")

        ### This 5 lines are from the video but they do not achieve the intended result,
        ### so I replaced them with previous lines.
        # categories = request.env['res.partner.category'].search([])
        # if category:
        #     partners = partners.filtered(lambda record: category.id in record.category_id.ids)
        # if not category:
        #     category = request.env['res.partner.category']

        values = {
            'customers': partners,
            'pager': pager,
            'categories': categories,
            'category': category,
        }
        return request.render("website_contact.customer_template", values)

    @http.route(['/website_contact/customers/details/<model("res.partner"):partner>'],
                type='http', auth="user", website=True)
    def customer_details(self, partner):
        values = {'customer': partner}
        return request.render("website_contact.customer_details", values)
