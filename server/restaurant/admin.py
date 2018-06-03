from django.contrib import admin

from .models import (
    MasterClient, MasterRestaurant, MasterPremise, PremiseSections, MasterDevice, ClientConfiguration,
    ClientRoles, MasterClientInvoice, ClientPayments, ClientAccount, TransactionLog)

# Register your models here.

admin.site.register(MasterClient)
admin.site.register(MasterRestaurant)
admin.site.register(MasterPremise)
admin.site.register(PremiseSections)
admin.site.register(MasterDevice)
admin.site.register(ClientConfiguration)
admin.site.register(ClientRoles)
admin.site.register(MasterClientInvoice)
admin.site.register(ClientPayments)
admin.site.register(ClientAccount)
admin.site.register(TransactionLog)