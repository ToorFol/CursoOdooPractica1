from odoo import models, fields

class Veterinary_pet(models.Model):
   _name = "veteranary.pet"
   _description = "Veterinari Pat"

   name = fields.Char(string="Name")
   weight = fields.Integer(string="Weight")
   pet_id = fields.Char(string="Pet id"
