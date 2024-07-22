from odoo import models, api
from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def test_code_v17(self):
        # Print to server logs
        _logger = models.logging.getLogger(__name__)
        _logger.info("OK")

        # Raise a UserError to display a message in the UI
        raise UserError("OK")
