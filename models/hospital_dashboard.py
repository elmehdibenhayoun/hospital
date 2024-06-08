from odoo import fields, models, api

class HospitalReport(models.Model):
    _name = 'hospital.report'
    _description = 'Hospital Report'
    name = fields.Char(string='Report Name')




    total_patients = fields.Integer(string='Total Patients', compute='_compute_total_patients')
    total_doctors = fields.Integer(string='Total Doctors', compute='_compute_total_doctors')
    total_appointments = fields.Integer(string='Total Appointments', compute='_compute_total_appointments')
    total_rooms = fields.Integer(string='Total Rooms', compute='_compute_total_rooms')
    total_operations = fields.Integer(string='Total Operations', compute='_compute_total_operations')


    @api.depends()
    def _compute_total_patients(self):
        for record in self:
            record.total_patients = self.env['hospital.patient'].search_count([])

    @api.depends()
    def _compute_total_doctors(self):
        for record in self:
            record.total_doctors = self.env['hospital.doctor'].search_count([])

    @api.depends()
    def _compute_total_appointments(self):
        for record in self:
            record.total_appointments = self.env['hospital.appointment'].search_count([])

    @api.depends()
    def _compute_total_rooms(self):
        for record in self:
            record.total_rooms = self.env['hospital.room'].search_count([])

    @api.depends()
    def _compute_total_operations(self):
        for record in self:
            record.total_operations = self.env['hospital.operation'].search_count([])







