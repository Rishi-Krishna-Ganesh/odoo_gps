from odoo import models, fields

class GpsData(models.Model):
    _name = 'gps.data'
    _description = 'GPS Data'

    latitude = fields.Float(string='Latitude', required=True)
    longitude = fields.Float(string='Longitude', required=True)
    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now)
