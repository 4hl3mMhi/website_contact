# -*- coding: utf-8 -*-

{
    'name': 'Website Contacts',
    'summary': """ Web Controllers in Odoo. """,
    'description': """
How To Write Controllers And Render WebPage Using Controllers in Odoo.
From a webinar of Cybrosys Technologies youtube channel.

Add a pagination to the list of customer menu.
""",
    'author': 'Ahlem Mehri',
    'website': "http://www.mehriahlem-dz.com",
    'category': 'Developpement - Version Odoo 14',
    'version': '0.1',
    'sequence': '1',
    'depends': ['website_sale', 'contacts'],
    'data': [
        # demo : data for demonstration
        'demo/customer_demo.xml',
        # data : files to load at module install
        'data/customer_template.xml',
        'data/supplier_template.xml',
        'data/website_contact_data.xml',
        # Security : always load groups first
        #          : load access rights after groups
        'security/website_contact_security.xml',
        # templates
        # workflow
        # views
        # menus
        'views/website_contact_menuitem.xml',
        # reports
        # wizard
    ],
    # 'qweb': [
    # ],
    # 'images': [
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
