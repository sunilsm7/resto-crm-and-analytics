from __future__ import unicode_literals
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible # noqa
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL


CLIENT_STATUS = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)


class MasterClient(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    client_email = models.CharField(max_length=50, blank=True, null=True)
    client_mobile = models.CharField(max_length=15, blank=True, null=True)
    client_status = models.CharField(max_length=10, choices=CLIENT_STATUS, default='A')
    registration_datetime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_by')

    def __str__(self):
        return f'Client Name : {self.client_name}'

    class Meta:
        verbose_name_plural = "01 Master Client"


class MasterRestaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_restaurant')

    def __str__(self):
        return f'Restaurant Name : {self.restaurant_name}'

    class Meta:
        verbose_name_plural = "02 Master Restaurant"


class MasterPremise(models.Model):
    premise_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_premise')
    restaurant_id = models.ForeignKey(MasterRestaurant, on_delete=models.CASCADE, related_name='restaurant_premise')
    premise_name = models.CharField(max_length=200, blank=True, null=True)
    premise_city = models.CharField(max_length=50, blank=True, null=True)
    premise_pincode = models.CharField(max_length=15, blank=True, null=True)
    premise_address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'Premise Name : {self.premise_name}'

    class Meta:
        verbose_name_plural = "03 Master Premise"


class PremiseSections(models.Model):
    section_id = models.AutoField(primary_key=True)
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_section')
    section_name = models.CharField(max_length=100, blank=True, null=True)
    section_details = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'Section Name : {self.section_name}'

    class Meta:
        verbose_name_plural = "04 Master Premise Sections"


class MasterDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_device')
    device_type = models.CharField(max_length=50)
    device_assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="device_assigned")

    def __str__(self):
        return f'Device Name : {self.device_name}'

    class Meta:
        verbose_name_plural = "05 Master Device"


class ClientConfiguration(models.Model):
    configuration_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_configuration')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_configuration')
    configuration_type = models.CharField(max_length=20)
    configuration_attribute = models.CharField(max_length=50)
    configuration_value = models.CharField(max_length=50)
    configuration_status = models.CharField(max_length=15)
    configuration_start_datetime = models.DateTimeField()
    configuration_end_datetime = models.DateTimeField()

    def __str__(self):
        return f'Configuration Attribute : {self.configuration_attribute} Value : {self.configuration_value}'

    class Meta:
        verbose_name_plural = "06 Client Configurations"


class ClientRoles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_description = models.CharField(max_length=100)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_role')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_role')

    def __str__(self):
        return f' Role Description : {self.role_description}'

    class Meta:
        verbose_name_plural = "07 Client Roles"


class MasterClientInvoice(models.Model):
    client_invoice_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_invoice')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_invoice')
    invoice_datetime = models.DateTimeField()
    invoice_amount = models.FloatField()
    invoice_tax_id = models.IntegerField()

    def __str__(self):
        return f'Customer Invoice ID : {self.client_id}'

    class Meta:
        verbose_name_plural = "08 Client Invoices"


class ClientPayments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_payment')
    customer_invoice_id = models.ForeignKey(
        MasterClientInvoice, on_delete=models.CASCADE, related_name='client_payment_invoice')
    payment_type = models.CharField(max_length=15)
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    payment_currency = models.CharField(max_length=15)

    def __str__(self):
        return f'Payment ID : {self.payment_id} Customer Invoice ID : {self.customer_invoice_id}'

    class Meta:
        verbose_name_plural = "09 Client Payments"


class ClientAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_account')
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_account')
    account_type = models.CharField(max_length=15)
    account_status = models.CharField(max_length=15)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f'Account ID : {self.account_id} Customer ID : {self.client_id}'

    class Meta:
        verbose_name_plural = "10 Client Account"


class TransactionLog(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_description = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=30)
    transaction_source = models.CharField(max_length=50)
    client = models.ForeignKey(MasterClient, on_delete=models.CASCADE, related_name='client_transcation')
    premise = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_transaction')
    transaction_identifier = models.CharField(max_length=50)
    transaction_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    transaction_created_by = models.CharField(max_length=100)
    transaction_modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    transaction_modified_by = models.CharField(max_length=100)

    def __str__(self):
        return f'Transaction ID : {self.transaction_id}'

    class Meta:
        verbose_name_plural = "11 Transaction Log"
