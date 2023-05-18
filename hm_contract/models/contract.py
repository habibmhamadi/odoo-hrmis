# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons.hm_master.helpers import data
from datetime import date, datetime
from odoo.exceptions import ValidationError


class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contract'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(tracking=True)
    employee_id = fields.Many2one('employee.employee', string="Employee", required=True, tracking=True)
    father_name = fields.Char(related='employee_id.father_name')
    department_id = fields.Many2one(related='employee_id.department_id', store=True)
    job_id = fields.Many2one(related='employee_id.job_id')
    image = fields.Binary(related='employee_id.image')
    company_id = fields.Many2one(related='employee_id.company_id', store=True)
    resource_calendar_id = fields.Many2one(related='employee_id.resource_calendar_id')
    previous_contract_id = fields.Many2one('contract.contract', readonly=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(data.CONTRACT_STATES, required=True, default="draft", tracking=True)
    start_date = fields.Date(tracking=True)
    end_date = fields.Date(tracking=True)
    renewal_type = fields.Selection(data.RENEWAL_TYPES, required=True, default="new", tracking=True)
    hr_approver_id = fields.Many2one('res.users', string="HR Approver", domain=lambda self: [("groups_id", "=", self.env.ref("hm_contract.group_contract_officer").id)])
    director_approver_id = fields.Many2one('res.users', string="Director Approver", domain=lambda self: [("groups_id", "=", self.env.ref("hm_contract.group_contract_admin").id)])
    currency_id = fields.Many2one('res.currency', string="Currency", required=True, tracking=True)
    wage = fields.Monetary(currency_field="currency_id", required=True, tracking=True)


    # ------------------------------------------------------- ACTIONS ---------------------------------------------------------
    def action_hr_approval(self):
        for rec in self:
            rec.write({'state': 'hr_approval'})

    def action_director_approval(self):
        for rec in self:
            rec.write({'state': 'director_approval'})
    
    def action_running(self):
        for rec in self:
            rec.write({'state': 'running'})

    def action_draft(self):
        for rec in self:
            rec.write({'state': 'draft'})


    def write(self, vals):
        if vals.get('state') in ['running', 'draft']:
            emp = self.env['employee.employee'].sudo().search([('id', '=', self.employee_id.id)])
            
        if vals.get('state') == 'running':
            emp.write({'current_contract_id': self.id})
        elif vals.get('state') == 'draft':
            emp.write({'current_contract_id': None})

        return super(Contract, self).write(vals)