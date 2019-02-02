# -*- coding: utf-8 -*-
{
    'name': 'Signup with Address, Phone, Date of Birth and Captcha',
    'summary': 'Signup page with Address, Phone, Date of Birth and Captcha Fields.',
    'description': '''Signup page with Address 
            - New Customer can give complete address with phone number while signup.
            - List of all States and Countries will be shown selected field in Signup page.
            - Add Date of Birth field.
            - You can choose whether Phone/Address/Date of Birth need to shown in Signup page in Configuration. 
            Default will be enabled.
            - Upload profile picture while sign up(Upcoming feature)
            - Enable/Disable Captcha in both Signup and Login page.
    ''',
    'author': 'Tintumon .M',
    'website': 'http://www.tintumon.co.in',
    'license': 'Other proprietary',
    'price': 20.00,
    'currency': 'EUR',
    'category': 'Website',
    'version': '0.1',
    'images': ['static/description/banner.jpg'],
    'depends': [
        'base',
        'auth_signup',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'views/auth_signup_views.xml',
        'views/auth_signup_login_templates.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',

    ],
}
