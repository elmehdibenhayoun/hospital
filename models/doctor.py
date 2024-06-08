from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Char(string='Specialty')
    departement_id = fields.Many2one('hospital.departement', string='Departement')
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string='Patients')
