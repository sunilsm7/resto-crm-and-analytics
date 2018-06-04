from django.conf import settings

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from accounts.api import views

router = DefaultRouter()
router.register(r'user-profile', views.UserProfileViewSet)


app_name = 'accounts'

urlpatterns = [
    path('', include(router.urls)),
]