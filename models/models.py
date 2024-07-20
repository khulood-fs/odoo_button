from odoo import api, fields, models

class MyModel(models.Model):
    _name = 'my_module.my_model'
    _description = 'My Module Model'

    name = fields.Char(string='Name')

    @api.model
    def test_code_v17(self):
        # Your custom logic here
        return True
