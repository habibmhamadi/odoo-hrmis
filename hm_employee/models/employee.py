# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons.hm_master.helpers import data
from datetime import date, datetime
from odoo.exceptions import ValidationError
from validate_email import validate_email


class Employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    father_name = fields.Char(required=True, tracking=True)
    gender = fields.Selection(data.GENDERS, required=True, tracking=True)
    dob = fields.Date(string="Date of Birth", required=True, tracking=True)
    age = fields.Integer(compute="_compute_age")
    marital_status = fields.Selection(data.MARITAL_STATUS, required=True, tracking=True)
    no_of_children = fields.Integer(string="No. of Children", tracking=True)
    place_of_birth = fields.Char(tracking=True)
    private_phone = fields.Char(tracking=True)
    private_email = fields.Char(tracking=True)
    work_phone = fields.Char(tracking=True)
    work_email = fields.Char(tracking=True)
    current_address = fields.Char(tracking=True)
    tin_no = fields.Char(string="TIN No.", tracking=True)
    nid_no = fields.Char(string="NID No.", help="National Identification No.", tracking=True)
    passport_no = fields.Char(string="Passport No.", tracking=True)
    badge_no = fields.Char(tracking=True)
    blood_group = fields.Selection(data.BLOOD_GROUPS, tracking=True)
    image = fields.Binary()
    active = fields.Boolean(default=True)
    
    nationality_id = fields.Many2one('res.country', string="Nationality", tracking=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    parent_id = fields.Many2one('employee.employee', string="Manager", tracking=True)
    department_id = fields.Many2one('department.department', string="Department", tracking=True)
    job_id = fields.Many2one('job.job', string="Job", tracking=True)
    emergency_contact_ids = fields.One2many('emergency.contact', 'employee_id', string="Emergency Contacts", tracking=True)
    reference_ids = fields.One2many('employee.reference', 'employee_id', string="References", tracking=True)
    doc_ids = fields.One2many('employee.document', 'employee_id', string="Documents", tracking=True)
    user_id = fields.Many2one('res.users', string="Related User", domain="[('company_id', '=', company_id)]", tracking=True)
    resource_calendar_id = fields.Many2one('resource.calendar', string="Working Time", required=True, default=lambda self: self.company_id.resource_calendar_id, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=True)
    
    # -------------------------------------------- Computed Methods --------------------------------------------------------------------
    def _compute_age(self):
        for rec in self:
            rec.age = ((date.today() - rec.dob).days // 365) if rec.dob else 0



    # --------------------------------------------- Constrains --------------------------------------------------------------------------
    @api.constrains('dob')
    def check_dob(self):
        for rec in self:
            if rec.dob and date.today() < rec.dob:
                raise ValidationError(_('Date of birth cannot be greater than current date.'))
            
            
    @api.constrains('work_email', 'private_email')
    def check_emails(self):
        for rec in self:
            if rec.work_email and not validate_email(rec.work_email):
                raise ValidationError(_('Invalid work email.'))
            if rec.private_email and not validate_email(rec.private_email):
                raise ValidationError(_('Invalid private email.'))



    # ---------------------------------------------- Actions ----------------------------------------------------------------------------
    def action_open_employee_document(self):
        for rec in self:
            return {
                'name': _('Employee Documents'),
                'type': 'ir.actions.act_window',
                'res_model': 'employee.document',
                'view_mode': 'tree,form',
                'domain': [('employee_id', '=', rec.id)],
                'context': {
                    'default_employee_id': rec.id,
                },
            }