from odoo import models, fields, api


class CancelOpenacademyWizard(models.TransientModel):

    _name = 'cancel.openacademy.wizard'
    _description = "Cancel Openacademy Wizard"

    def _default_session(self):
        return self.env['session.model'].browse(self._context.get('active_ids'))

    #session_id = fields.Many2one('session.model',string="Session",default=_default_session)
    session_id = fields.Many2many('session.model',string="Sessions")
    #partner_id = fields.Many2one('res.partner',string="Partner")
    partner_id = fields.Many2many('res.partner',string="Partner")

    def add_user(self):
        for session in self.session_id:
            for partner in self.partner_id:
                session.part_ids |= partner
        return {}


