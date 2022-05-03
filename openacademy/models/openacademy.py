from odoo import models, fields, api


class OpenacademyCourse(models.Model):

    _name = 'openacademy.course'
    name = fields.Char()
    _description = "Openacademy"
    description = fields.Char()
    myuser = fields.Many2one("res.users",string="Res. user",default=lambda self: self.env.user)
    session_ids = fields.One2many("session.model","course_id",string="Sessions")

    _sql_constraints = [('name_desc','check(name!=description)','description double name'),
                        ('name_unique','unique(name)','Please enter unique name !'),]

    def copy(self, default={}):
        default['name'] = "Copy ["+self.name+"]"
        rtn = super(OpenacademyCourse,self).copy(default=default)
        return rtn