from odoo import models, fields,api
from odoo.exceptions import ValidationError

class SessionModel(models.Model):



    _name = 'session.model'
    name = fields.Char()
    datestart = fields.Date(string="Start date",default=fields.datetime.today())
    duration = fields.Integer('Duration')
    numberseats = fields.Integer('Number seats')
    instructor_id = fields.Many2one("res.partner",string="Instructor",domain=['|',('instructor', '=', True),'|',('level_one', '=', True),('level_two', '=', True)])
    course_id = fields.Many2one("openacademy.course",string="Course",required=True)
    part_ids = fields.Many2many("res.partner",string="Participants")
    active = fields.Boolean(string="Active",default=True)
    dateend = fields.Date(string="End date")

    perc_empl_places = fields.Integer(compute="_compute_place_percent",string="Percent employed place")
    @api.depends("numberseats","part_ids")
    def _compute_place_percent(self):
        for record in self:
            record.perc_empl_places = int((len(record.part_ids)/record.numberseats) * 100) if record.numberseats!=0 else 0

    @api.onchange('numberseats','part_ids')
    def _onchange_seats(self):
        if self.numberseats<0:
            return {'warning': {'title':"Warning",'message':"Count of seats is negative !",}}
        elif self.numberseats==0:
            return {'warning': {'title': "Warning", 'message': "Count of seats is zero !", }}
        elif len(self.part_ids) > self.numberseats:
            return {'warning': {'title': "Warning", 'message': "Count of participants is greater than count of seats !", }}
        else:
            self.perc_empl_places = int((len(self.part_ids) / self.numberseats) * 100) if self.numberseats != 0 else 0


    #@api.constrains('instructor_id','part_ids')

    @api.constrains('instructor_id','part_ids')
    def _instructor_not_listen(self):
        for rec in self:
            if rec.instructor_id in rec.part_ids:
                raise ValidationError("Instructor: "+str(rec.instructor_id.name) + " is in list visitor !")

