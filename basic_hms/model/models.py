# -*- coding: utf-8 -*-

from odoo import models, fields, api

class basicHms(models.Model)
	_inherit= 'basic_hms'
	
	nombre_medicación = fields.Char('Nombre de medicación')
	toma_medicacion = fields.boolean (string = 'Toma medicación')

