from odoo import models, fields

class Room(models.Model):
    _name = 'hospital.room'
    _description = 'Hospital Room'

    name = fields.Char(string='Name', required=True)
    departement_id = fields.Many2one('hospital.departement', string='Departement')
    equipment_ids = fields.Many2many('hospital.equipement', string='Equipments')
    patient_ids = fields.One2many('hospital.patient', 'room_id', string='Patients')
    is_available = fields.Boolean(string='Is Available', default=True)
    price_per_day = fields.Float(string='Price per Day')
