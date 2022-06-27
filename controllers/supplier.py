# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class WebsiteContact(http.Controller):

    @http.route(['/website_contact/suppliers', '/website_contact/suppliers/page/<int:page>'],
                type='http', auth="public", website=True)
    def display_supplier(self, page=0):
        """
           params auth="public" means that a public user have no access to a some database records.
           to make him/her able to access to some database records in some circumstances, it should
           precede the orm methods with .sudo() like:
              request.env['res.partner'].sudo().search(...)
        """
        domain = [('supplier_rank', '=', 1)]
        Supplier = request.env['res.partner'].sudo()
        total_count = len(Supplier.search(domain))
        per_page = 12
        # total : Total count of records
        # page : current page
        # step : count of records need to display in one page
        # scope: count of pages needs to display in a pager at a time
        pager = request.website.pager(url='/website_contact/suppliers', total=total_count, page=page, step=per_page,
                                      scope=3, url_args=None)
        # offset : count to exclude (first n)
        suppliers = Supplier.search(domain, limit=per_page, offset=pager['offset'], order="id asc")
        values = {'suppliers': suppliers, 'page': pager}
        return request.render("website_contact.supplier_template", values)

    @http.route(['/website_contact/suppliers/details/<model("res.partner"):partner>'],
                type='http', auth="public", website=True)
    def supplier_details(self, partner):
        simple_template = """
            <div style="display:flex; position:absolute; top:0; bottom:0; right:0; left:0;">
                <h2 style="margin:auto;">
                    Same as template of customer details.
                    <br/><br/>
                    You can try to write it yourself.
                </h2>
            </div>
        """
        return simple_template
