from django.conf import settings

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from restaurant.api import views 

router = DefaultRouter()
router.register(r'client', views.MasterClientViewSet)
router.register(r'restaurant', views.MasterRestaurantViewSet)
router.register(r'premise', views.MasterPremiseViewSet)
router.register(r'premise-section', views.PremiseSectionsViewSet)
router.register(r'device', views.MasterDeviceViewSet)
router.register(r'client-configuration', views.ClientConfigurationViewSet)
router.register(r'client-role', views.ClientRolesViewSet)
router.register(r'client-invoice', views.MasterClientInvoiceViewSet)
router.register(r'client-payment', views.ClientPaymentsViewSet)
router.register(r'client-account', views.ClientAccountViewSet)
router.register(r'transcation-log', views.TransactionLogViewSet)


app_name = 'restaurant'

urlpatterns = [
    path('', include(router.urls)),
]