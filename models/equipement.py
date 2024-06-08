from odoo import models, fields

class Equipement(models.Model):
    _name = 'hospital.equipement'
    _description = 'Hospital Equipement'

    name = fields.Char(string='Name', required=True)
    room_ids = fields.Many2many('hospital.room', string='Rooms')
    operation_ids = fields.Many2many('hospital.operation', string='Operations')
