from django.conf import settings
from django.utils.translation import ugettext as _

ugettext = lambda s: s

BILLING_INVOICE_ID_PREFIX = getattr(settings, 'BILLING_INVOICE_ID_PREFIX', 'I')
BILLING_AMENDMENTINVOICE_ID_PREFIX = getattr(settings, 'BILLING_AMENDMENT_INVOICE_ID_PREFIX', 'AI')
BILLING_FEE_ID_PREFIX = getattr(settings, 'BILLING_FEE_ID_PREFIX', 'F')
BILLING_AMENDMENTFEE_ID_PREFIX = getattr(settings, 'BILLING_AMENDMENT_FEE_ID_PREFIX', 'AF')
BILLING_BUDGET_ID_PREFIX = getattr(settings, 'BILLING_BUDGET_ID_PREFIX', 'B')

BILLING_INVOICE_ID_LENGTH = getattr(settings, 'BILLING_INVOICE_ID_LENGTH', 4)
BILLING_AMENDMENTINVOICE_ID_LENGTH = getattr(settings, 'BILLING_AMENDMENT_INVOICE_ID_LENGTH', 4)
BILLING_FEE_ID_LENGTH = getattr(settings, 'BILLING_FEE_ID_LENGTH', 4)
BILLING_AMENDMENTFEE_ID_LENGTH = getattr(settings, 'BILLING_AMENDMENT_FEE_ID_LENGTH', 4)
BILLING_BUDGET_ID_LENGTH = getattr(settings, 'BILLING_BUDGET_ID_LENGTH', '4')

BILLING_INVOICE_TEMPLATE = getattr(settings, 'BILLING_INVOICE_TEMPLATE', './invoice.html')
BILLING_AMENDMENTINVOICE_TEMPLATE = getattr(settings, 'BILLING_AMENDMENTINVOICE_TEMPLATE', './invoice.html')
BILLING_FEE_TEMPLATE = getattr(settings, 'BILLING_FEE_TEMPLATE', './invoice.html')
BILLING_AMENDMENTFEE_TEMPLATE = getattr(settings, 'BILLING_AMENDMENTFEE_TEMPLATE', './invoice.html')
BILLING_BUDGET_TEMPLATE = getattr(settings, 'BILLING_BUDGET_TEMPLATE', './invoice.html')

BILLING_BILLS_DIRECTORY = getattr(settings, 'BILLING_BILLS_DIRECTORY', '/tmp/')

BILLING_DUE_DATE_DAYS = getattr(settings, 'BILLING_DUE_DATE_DAYS', 30)

#Billing options
BILLING_DEFAULT_FIXED_POINT = getattr(settings, 'BILLING_DEFAULT_FIXED_POINT', False)
BILLING_DEFAULT_FORCE_NEXT = getattr(settings, 'BILLING_DEFAULT_FORCE_NEXT', True)
BILLING_DEFAULT_CREATE_NEW_OPEN = getattr(settings, 'BILLING_DEFAULT_CREATE_NEW_OPEN', True)
BILLING_DEFAULT_EFFECT = getattr(settings, 'BILLING_DEFAULT_EFFECT', 'B')

IGNORE_DEPENDENCIES = 'I'
BILL_DEPENDENCIES = 'B'
PRICING_DEPENDENCIES = 'P'

BILLING_DEFAULT_DEPENDENCIES_EFFECT = getattr(settings, 'BILLING_DEFAULT_EFFECT', BILL_DEPENDENCIES)

BILLING_FEE_PER_FEE_LINE = getattr(settings, 'BILLING_FEE_PER_FEE_LINE', True)

# FEES and INVOICES AMENDMENT Behaviour
CREATE_AMENDMENT_FOR_REFOUND = 'A'
CREATE_AMENDMENT_FOR_RECHARGE = 'C'
PUT_REFOUND_ON_OPEN_INVOICE = 'D'
PUT_REFOUND_ON_OPEN_INVOICE_IF_EQ_TAX = 'E'
PUT_RECHARGE_ON_OPEN_INVOICE = 'F'
#GROUP_REFOUND_AND_RECHARGE = 'G'

BILLING_INVOICES_AMENDMENT_BEHAVIOUR = getattr(settings, 'BILLING_INVOICES_AMENDMENT_BEHAVIOUR', [PUT_RECHARGE_ON_OPEN_INVOICE, 
            CREATE_AMENDMENT_FOR_REFOUND, PUT_REFOUND_ON_OPEN_INVOICE_IF_EQ_TAX])
BILLING_FEES_AMENDMENT_BEHAVIOUR = getattr(settings, 'BILLING_FEES_AMENDMENT_BEHAVIOUR', [CREATE_AMENDMENT_FOR_REFOUND, 
            CREATE_AMENDMENT_FOR_RECHARGE])


OPEN = 'OPEN'
CLOSED = 'CLOSED'
SEND = 'SEND'
RETURNED = 'RETURNED'
PAYD = 'PAYD'
IRRECOVRABLE = 'IRRECOVRABLE'

BILLING_STATUS_CHOICES = getattr(settings, 'BILLING_STATUS_CHOICES', ((OPEN, _('Open')),
                                                      (CLOSED, _('Closed')),
                                                      (SEND, _('Sent')),
                                                      (RETURNED, _('Returned')),
                                                      (PAYD, _('Payd')),
                                                      (IRRECOVRABLE, _('Irrecovrable debt')),))