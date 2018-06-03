from django.conf import settings

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from menus.api import views as menus_views

router = DefaultRouter()
router.register(r'category', menus_views.MenuCategoryViewSet)
router.register(r'item', menus_views.MenuItemViewSet)

app_name = 'menus'

urlpatterns = [
    path('', include(router.urls)),
]