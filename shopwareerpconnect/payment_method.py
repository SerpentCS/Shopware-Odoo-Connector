# -*- coding: utf-8 -*-
from openerp import models, fields


class PaymentMethod(models.Model):
    """This corresponds to the object payment.mode of v8 with some
    important changes. It also replaces the object payment.method
    of the module sale_payment_method of OCA/sale-workflow"""
    _inherit = "account.payment.mode"

    create_invoice_on = fields.Selection(
        selection=[('open', 'Validate'),
                   ('paid', 'Paid')],
        string='Create invoice on action',
        help="Should the invoice be created in Shopware "
             "when it is validated or when it is paid in OpenERP?\n"
             "If nothing is set, the option falls back to the same option "
             "on the Shopware shop related to the sales order.",
    )
