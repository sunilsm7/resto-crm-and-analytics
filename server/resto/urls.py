"""resto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token

from restaurant.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    re_path(r'^api/restaurant/', include('restaurant.api.urls', namespace='restaurant')),
    re_path(r'^api/reservations/', include('reservations.api.urls', namespace='reservations')),
    re_path(r'^api/menus/', include('menus.api.urls', namespace='menus')),
    re_path(r'^api/orders/', include('orders.api.urls', namespace='orders')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
