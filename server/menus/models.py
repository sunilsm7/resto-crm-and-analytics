from django.db import models
from django.conf import settings
from restaurant.models import MasterPremise
User = settings.AUTH_USER_MODEL
# Create your models here.


class MenuCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='sub_category')
    category_image = models.CharField(max_length=100, blank=True, null=True)
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_menu')

    def __str__(self):
        return f'Category Name : {self.category_name}'

    class Meta:
        verbose_name_plural = "Master Category"


class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_value = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='category')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_menu_item')
    ref_start_date = models.DateTimeField()
    ref_end_date = models.DateTimeField()
    slug = models.SlugField(max_length=120)

    def __str__(self):
        return f'Item Name : {self.item_name}'

    class Meta:
        verbose_name_plural = "Menu Item"
