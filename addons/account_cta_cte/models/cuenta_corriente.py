from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CuentaCorriente(models.Model):
    _name = 'account.cta.cte'

    name = fields.Char(required=True, string='Nombre')
    description = fields.Text(string='Descripcion')
    balance = fields.Float(default=0, copy=False, string='Saldo')
    create_date = fields.Date(
        default=fields.Date.today, string='Fecha de creacion')

    @api.constrains('balance')
    def _check_balance_not_negative(self):
        for record in self:
            if record.balance < 0:
                raise ValidationError('El saldo no puede ser negativo.')
