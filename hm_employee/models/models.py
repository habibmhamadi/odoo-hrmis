# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.hm_master.helpers import data

# Document
class EmployeeDocument(models.Model):
    _name = 'employee.document'
    _description = 'Employee Document'

    name = fields.Char(required=True)
    doc_type = fields.Selection(data.EMP_DOC_TYPES, required=True)
    doc_file = fields.Binary(required=True)
    employee_id = fields.Many2one('employee.employee')



# Reference
class EmployeeReference(models.Model):
    _name = 'employee.reference'
    _description = 'Employee Reference'

    name = fields.Char(required=True)
    job_title = fields.Char(required=True)
    organization = fields.Char(required=True)
    phone_no = fields.Char(string="Phone No.", required=True)
    employee_id = fields.Many2one('employee.employee')



# Emergency Contact
class EmergencyContact(models.Model):
    _name = 'emergency.contact'
    _description = 'Emergency Contact'

    name = fields.Char(required=True)
    relationship = fields.Selection(data.RELATIONSHIPS, required=True)
    phone_no = fields.Char(string="Phone No.", required=True)
    employee_id = fields.Many2one('employee.employee')



# Department
class Department(models.Model):
    _name = 'department.department'
    _description = 'Department'

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique (name, company_id)', 'The department name must be unique for a specific company.')
    ]


# Job
class Department(models.Model):
    _name = 'job.job'
    _description = 'Job'

    name = fields.Char(required=True)