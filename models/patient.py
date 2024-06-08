from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    room_id = fields.Many2one('hospital.room', string='Room', domain=[('is_available', '=', True)])
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    admission_date = fields.Datetime(string='Admission Date', default=fields.Datetime.now)
    discharge_date = fields.Datetime(string='Discharge Date')
