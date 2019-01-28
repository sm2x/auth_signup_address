# -*- coding: utf-8 -*-
{
    'name': 'Signup with Address',
    'summary': 'Signup page with Address.',
    'description': '''Signup page with Address 
            - New Customer can give complete address with phone number while signup.
            - List of all States and Countries will be shown selected field in Signup page.
            - You can chooose wheather Phone or Address need to shown in Signup page. Default will be true. 
    ''',
    'author': 'Tintumon .M',
    'website': 'http://www.tintumon.co.in',
    'license': 'AGPL-3',
    'category': 'Website',
    'version': '0.1',
    'depends': [
        'base',
        'auth_signup',
    ],
    'data': [
        'views/auth_signup_views.xml',
        'views/res_config_settings_views.xml',
    ],
}
