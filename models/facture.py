from odoo import models, fields, api
from datetime import datetime

class Facture(models.Model):
    _name = 'hospital.facture'
    _description = 'Hospital Invoice'

    name = fields.Char(string='Invoice Number', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('hospital.facture'))
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    amount = fields.Float(string='Amount', compute='_compute_amount', store=True)

    @api.depends('patient_id')
    def _compute_amount(self):
        for record in self:
            total = 0.0
            patient = record.patient_id

            if patient.admission_date and patient.discharge_date:
                stay_duration_days = (patient.discharge_date - patient.admission_date).days
                if patient.room_id:
                    total += stay_duration_days * patient.room_id.price_per_day

            operations = self.env['hospital.operation'].search([('patient_id', '=', patient.id)])
            for operation in operations:
                total += operation.price

            record.amount = total
