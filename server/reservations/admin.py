from django.contrib import admin

from .models import (
    Customer, CustomerDetails, MasterTable, TableAttributes, TableAvailability, ReservationQueue, CustomerAnalytics)
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerDetails)
admin.site.register(ReservationQueue)
admin.site.register(MasterTable)
admin.site.register(TableAttributes)
admin.site.register(TableAvailability)
admin.site.register(CustomerAnalytics)
