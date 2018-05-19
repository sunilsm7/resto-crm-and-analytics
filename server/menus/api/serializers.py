from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from menus.models import MenuCategory, MenuItem


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
