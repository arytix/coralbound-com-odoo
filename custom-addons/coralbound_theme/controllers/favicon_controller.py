from odoo import http
from odoo.http import request, Response

class FaviconController(http.Controller):
    @http.route('/favicon.ico', type='http', auth='public', cors='*')
    def serve_custom_favicon(self, **kwargs):
        """Serve the custom favicon."""
        return request.redirect('/coralbound_theme/static/src/img/logo.png')
