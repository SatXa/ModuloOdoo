#-*- coding: utf-8 -*-
from openerp import models, fields

class Game(models.Model):
    _name = 'app01.game'
    name = fields.Char('Description', required=True)
	year = fields.Date()
	developers = fields.Char()
	developers = fields.Char()
	platforms = fields.Char()
	synopsis = fields.Text()
	urlLogo = fields.Char()
	
	@api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
	
	@api.multi
	def do_clear_done(self):
		done_recs = self.search([('is_done', '=', True)])
		done_recs.write({'active': False})
		return True