from odoo import http
from odoo.http import request
import json

class GpsController(http.Controller):

    @http.route('/gps/track', type='json', auth='public', methods=['POST'], csrf=False)
    def track(self, **kw):
        latitude = kw.get('latitude')
        longitude = kw.get('longitude')
        if latitude and longitude:
            request.env['gps.data'].sudo().create({
                'latitude': latitude,
                'longitude': longitude
            })
            return json.dumps({'status': 'success'})
        return json.dumps({'status': 'failure'})
