from django.conf import settings

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from reservations.api import views

router = DefaultRouter()
router.register(r'reservations', views.ReservationQueueViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'customers-details-list', views.CustomerDetailsViewSet)
router.register(r'tables-list', views.MasterTableViewSet)
router.register(r'table-attributes', views.TableAtrributesViewSet)
router.register(r'table-available-status', views.TableAvailabilityViewSet)
router.register(r'customer-analytics', views.CustomerAnalyticsViewSet)

app_name = 'reservations'

urlpatterns = [
    path('', include(router.urls)),
]