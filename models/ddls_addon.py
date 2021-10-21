from odoo import models, fields, api
from odoo.osv import expression


class DdlsInherit(models.Model):
    _inherit = 'hr.employee'

#   ===================== EASY =====================
    i_love_field = fields.Boolean(string='i_love_ddls')

#   ==================== MEDIUM ====================
    salary_field = fields.Integer(string='Salary')
    tax_field = fields.Integer(string='Tax')
    total_salary_field = fields.Integer(
        string='Total salary', readonly=True, compute='_compute_total_salary')

    @api.depends('salary_field', 'tax_field')
    def _compute_total_salary(self):
        salary = 0
        if self.salary_field:
            salary = max(self.salary_field, 0)

        tax = 0
        if self.tax_field:
            tax = max(self.tax_field, 0)

        self.total_salary_field = salary + tax


#   =================== ADVANCED ===================
    PHONE = '0911111'
    special_phone = fields.Char(string='Special phone')

    @api.model
    def create(self, values):
        if not values.get('special_phone'):
            values['special_phone'] = self.PHONE
        return super(DdlsInherit, self).create(values)

    def write(self, values):
        res = super(DdlsInherit, self).write(values)
        if not self.special_phone:
            self.special_phone = self.PHONE
        return res
