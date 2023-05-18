# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = 'employee.employee'

    current_contract_id = fields.Many2one('contract.contract', readonly=True)