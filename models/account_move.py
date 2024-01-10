from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def button_draft(self):
        self.zatca_status_code = 400
        return super(AccountMove, self).button_draft()