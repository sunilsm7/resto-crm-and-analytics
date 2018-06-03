from django.contrib import admin
from .models import (
    MasterOrder, OrderDetails, MasterInvoice, InvoiceDetails, CustomerPayments, CustomerFeedback
)
# Register your models here.

admin.site.register(MasterOrder)
admin.site.register(OrderDetails)
admin.site.register(MasterInvoice)
admin.site.register(InvoiceDetails)
admin.site.register(CustomerPayments)
admin.site.register(CustomerFeedback)
