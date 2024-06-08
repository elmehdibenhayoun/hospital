from odoo import models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    date = fields.Datetime(string='Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

