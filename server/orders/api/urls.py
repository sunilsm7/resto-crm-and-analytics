from django.conf import settings

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from orders.api import views

router = DefaultRouter()
router.register(r'order', views.MasterOrderViewSet)
router.register(r'order-details', views.OrderDetailsViewSet)
router.register(r'invoice', views.MasterInvoiceViewSet)
router.register(r'invoice-details', views.InvoiceDetailsViewSet)
router.register(r'order-payments', views.CustomerPaymentsViewSet)
router.register(r'order-feedback', views.CustomerFeedbackViewSet)

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls)),
]