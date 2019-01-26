from odoo import _
from odoo.exceptions import UserError
from openerp.addons.auth_signup.controllers.main import AuthSignupHome
from openerp.http import request


class AuthSignupHomeExt(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        qcontext = super(AuthSignupHomeExt, self).get_auth_signup_qcontext()
        qcontext['states'] = request.env["res.country.state"].sudo().search([])
        qcontext['countries'] = request.env["res.country"].sudo().search([])
        return qcontext

    def do_signup(self, qcontext):
        """ Replaced the default do_signup base module to add extra fields. """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password',
                                                     'phone', 'street', 'street2',
                                                     'city', 'state_id', 'country_id',
                                                     'zip')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()