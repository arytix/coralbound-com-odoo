# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import werkzeug


class DatabaseBlockController(http.Controller):

    @http.route('/web/database/manager', type='http', auth='none', methods=['GET', 'POST'])
    def database_manager_block(self, **kwargs):
        """Block access to database manager"""
        return werkzeug.exceptions.NotFound()

    @http.route('/web/database', type='http', auth='none', methods=['GET', 'POST'])
    def database_block(self, **kwargs):
        """Block access to database routes"""
        return werkzeug.exceptions.NotFound()

    @http.route('/web/database/<path:subpath>', type='http', auth='none', methods=['GET', 'POST'])
    def database_subpath_block(self, subpath=None, **kwargs):
        """Block access to all database sub-routes"""
        return werkzeug.exceptions.NotFound()
