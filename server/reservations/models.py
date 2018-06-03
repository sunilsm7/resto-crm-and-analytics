from django.db import models
from django.conf import settings
from restaurant.models import MasterPremise, PremiseSections
User = settings.AUTH_USER_MODEL
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='customer_premise')

    def __str__(self):
        return f'Customer Name : {self.customer_name}'

    class Meta:
        verbose_name_plural = "Customer"


class CustomerDetails(models.Model):
    customer_details_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_details')
    customer_attribute = models.CharField(max_length=50, blank=True, null=True)
    attribute_value = models.CharField(max_length=50, blank=True, null=True)
    attribute_status = models.CharField(max_length=10, blank=True, null=True)
    last_update_date = models.DateTimeField()

    def __str__(self):
        return f'Customer Attribute : {self.customer_attribute} Attribute Value : {self.attribute_value}'

    class Meta:
        verbose_name_plural = "Customer Details"


class MasterTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    table_type = models.CharField(max_length=100)
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='table_premise')
    section_id = models.ForeignKey(PremiseSections, on_delete=models.CASCADE, related_name='table_section')

    def __str__(self):
        return f'Table Name : {self.table_name}'

    class Meta:
        verbose_name_plural = "Master Tables "


class TableAttributes(models.Model):
    table_attribute_id = models.AutoField(primary_key=True)
    table = models.ForeignKey(MasterTable, on_delete=models.CASCADE, related_name='table_attributes')
    table_attribute_value = models.CharField(max_length=100)
    table_status = models.CharField(max_length=50)

    def __str__(self):
        return f'Table Attribute ID : {self.table_attribute_id} Table Attribute Value : {self.table_attribute_value}'

    class Meta:
        verbose_name_plural = "Table Attributes"


class TableAvailability(models.Model):
    tbl_availability_id = models.AutoField(primary_key=True)
    table_id = models.OneToOneField(
        MasterTable, null=True, blank=True, on_delete=models.CASCADE, related_name="available_table")
    tbl_availability_date = models.DateField()
    tbl_availability_status = models.CharField(max_length=15)
    tbl_availability_start_time = models.TimeField()
    tbl_availability_end_time = models.TimeField()

    def __str__(self):
        return f'Table ID : {self.table_id} Availability Status : {self.tbl_availability_status}'

    class Meta:
        verbose_name_plural = "Table Availability"


class ReservationQueue(models.Model):
    RESERVATION_STATUS = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Waiting', 'Waiting'),
        ('Canceled', 'Canceled'),
        ('Cleaning', 'Cleaning'),
    )

    reservation_queue_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_in_queue')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='reservation_premise')
    seating_preference = models.ForeignKey(PremiseSections, on_delete=models.CASCADE, related_name='pref_section')
    table_id = models.ForeignKey(
        MasterTable, on_delete=models.CASCADE, default=None, blank=False, related_name='reserved_table')
    reservation_status = models.CharField(max_length=10, choices=RESERVATION_STATUS, default='Available')
    reservation_for_date = models.DateField()
    reservation_start_time = models.TimeField()
    pax = models.IntegerField(blank=True, null=True)
    reserved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='reserved_by')
    reservation_date = models.DateTimeField(blank=True, null=True)
    reservation_type = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'Reservation ID : {self.reservation_queue_id} Customer ID :\
            {self.customer_id} Status : {self.reservation_status}'

    class Meta:
        verbose_name_plural = "Reservations"


class CustomerAnalytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_analytics')
    premise = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_analytics')
    analytics_attribute = models.CharField(max_length=50, blank=True, null=True)
    attribute_value = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'Analytics Attribute : {self.analytics_attribute} Attribute Value :{self.attribute_value}'

    class Meta:
        verbose_name_plural = "Customer Analytics"
