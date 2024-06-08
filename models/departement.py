from odoo import models, fields

class Departement(models.Model):
    _name = 'hospital.departement'
    _description = 'Hospital Departement'

    name = fields.Char(string='Name', required=True)
    doctor_ids = fields.One2many('hospital.doctor', 'departement_id', string='Doctors')
    room_ids = fields.One2many('hospital.room', 'departement_id', string='Rooms')
