from odoo import models, fields

class Operation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'

    name = fields.Char(string='Name', required=True)
    date = fields.Datetime(string='Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    equipment_ids = fields.Many2many('hospital.equipement', string='Equipments')
    room_id = fields.Many2one('hospital.room', string='Room')
    price = fields.Float(string='Price', required=True)
