from __future__ import unicode_literals
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL


CLIENT_STATUS = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)


# change MasterCustomer to MasterClient and all references
class MasterClient(models.Model):
    client_id           = models.AutoField(primary_key=True)
    client_name         = models.CharField(max_length=50)
    client_email        = models.CharField(max_length=50,blank=True, null=True)
    client_mobile       = models.CharField(max_length=15, blank=True, null=True)
    client_status       = models.CharField(max_length=10, choices=CLIENT_STATUS)
    registration_datetime = models.DateTimeField(blank=True, null=True)
    registered_by       = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'Client Name : {self.client_name}'  # use f '' string or format string

    class Meta:
        verbose_name_plural = "01 Master Client"


class MasterRestaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    client_id = models.ForeignKey(MasterClient)

    def __str__(self):
        return '%s ' % (self.restaurant_name)

    class Meta:
        verbose_name_plural = "02 Master Restaurant"


class MasterPremise(models.Model):
    premise_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient)
    restaurant_id = models.ForeignKey(MasterRestaurant)
    premise_name = models.CharField(max_length=200, blank=True, null=True)
    premise_city = models.CharField(max_length=50, blank=True, null=True)
    premise_pincode = models.CharField(max_length=15, blank=True, null=True)
    premise_address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.premise_name)

    class Meta:
        verbose_name_plural = "03 Master Premise"


class PremiseSections(models.Model):
    section_id = models.AutoField(primary_key=True)
    premise_id = models.ForeignKey(MasterPremise)
    section_name = models.CharField(max_length=100, blank=True, null=True)
    section_details = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.section_name)

    class Meta:
        verbose_name_plural = "04 Master Premise Sections"


class MasterDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    premise_id = models.ForeignKey(MasterPremise)
    device_type = models.CharField(max_length=50)
    device_assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  blank=True, null=True, related_name="waiter")

    def __str__(self):
        return '%s ' % (self.device_name)

    class Meta:
        verbose_name_plural = "05 Master Device"


#  change it ClientConfiguration
class ClientConfiguration(models.Model):
    configuration_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient)
    premise_id = models.ForeignKey(MasterPremise)
    configuration_type = models.CharField(max_length=20)
    configuration_attribute = models.CharField(max_length=50)
    configuration_value = models.CharField(max_length=50)
    configuration_status = models.CharField(max_length=15)
    configuration_start_datetime = models.DateTimeField()
    configuration_end_datetime = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.configuration_attribute,self.configuration_value)

    class Meta:
        verbose_name_plural = "06 Client Configurations"


# change it ClientRoles
class ClientRoles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_description = models.CharField(max_length=100)
    client_id = models.ForeignKey(MasterClient)
    premise_id = models.ForeignKey(MasterPremise)

    def __str__(self):
        return '%s ' % (self.role_description)

    class Meta:
        verbose_name_plural = "07 Client Roles"


# change it to MasterClientInvoice
class MasterClientInvoice(models.Model):
    client_invoice_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient)
    premise_id = models.ForeignKey(MasterPremise)
    invoice_datetime = models.DateTimeField()
    invoice_amount = models.FloatField()
    invoice_tax_id = models.IntegerField()

    def __str__(self):
        return '%s ' % (self.customer_invoice_id)
    
    class Meta:
        verbose_name_plural = "08 Client Invoices"


# ClientPayments
class ClientPayments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient)
    customer_invoice_id = models.ForeignKey(MasterCustomerInvoice)
    payment_type = models.CharField(max_length=15)
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    payment_currency = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s' % (self.payment_id,self.customer_invoice_id)

    class Meta:
        verbose_name_plural = "09 Client Payments"


# ClientAccount
class ClientAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(MasterClient)
    premise_id = models.ForeignKey(MasterPremise)
    account_type = models.CharField(max_length=15)
    account_status = models.CharField(max_length=15)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return '%s ' % (self.account_id)

    class Meta:
        verbose_name_plural = "10 Client Account"


# make it MenuCategory
class MenuCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent 	= models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='sub_category')
    category_image = models.CharField(max_length=100, blank=True, null=True)
    premise_id = models.ForeignKey(MasterPremise)

    def __str__(self):
        return '%s ' % (self.product_name)

    class Meta:
        verbose_name_plural = "11 Master Category"


# make it MenuItem
class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_value = models.CharField(max_length=50)
    product_id = models.ForeignKey(MenuItem)
    premise_id = models.ForeignKey(MasterPremise)
    ref_start_date = models.DateTimeField()
    ref_end_date = models.DateTimeField()

    def __str__(self):
        return '%s ' % (self.item_name)

    class Meta:
        verbose_name_plural = "12 Menu Item"


# make it MasterTable
class MasterTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    table_type = models.CharField(max_length=100)
    premise_id = models.ForeignKey(MasterPremise)
    section_id = models.ForeignKey(PremiseSections)

    def __str__(self):
        return '%s ' % (self.table_name)

    class Meta:
        verbose_name_plural = "13 Master Tables "
        

# TableAttributes
class TableAttributes(models.Model):
    table_attribute_id = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(MasterTable)
    table_attribute_value = models.CharField(max_length=100)
    table_status = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s %s' % (self.table_attribute_id,self.table.attribute_value)

    class Meta:
        verbose_name_plural = "14 Table Attributes"


# change it Customer
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    premise_id = models.ForeignKey(MasterPremise)

    def __str__(self):
        return '%s ' % (self.customer_name)

    class Meta:
        verbose_name_plural = "15 Customer"


# change it CustomerDetails 
class CustomerDetails(models.Model):
    customer_details_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    customer_attribute = models.CharField(max_length=50, blank=True, null=True)
    attribute_value = models.CharField(max_length=50, blank=True, null=True)
    attribute_status = models.CharField(max_length=10, blank=True, null=True)
    last_update_date = models.DateTimeField()
    
    def __str__(self):
        return '%s %s' % (self.customer_attribute,self.attribute_value)

    class Meta:
        verbose_name_plural = "16 Customer Details"
        

class ReservationQueue(models.Model):
    # add choice field for reservation_status
    reservation_queue_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    reservation_status = models.CharField(max_length=10)
    reservation_for_date = models.DateField()
    reservation_start_time = models.TimeField()
    pax = models.IntegerField(blank=True, null=True)
    seating_preference = models.CharField(max_length=20, blank=True, null=True)
    reserved_by = models.BigIntegerField(blank=True, null=True)  # user references
    reservation_date = models.DateTimeField(blank=True, null=True)
    reservation_type = models.CharField(max_length=10, blank=True, null=True)
    premise_id = models.BigIntegerField()
    
    def __str__(self):
        return '%s %s %s' % (self.reservation_queue_id,self.customer_id,self.reservation_status)

    class Meta:
        verbose_name_plural = "17 Reservations"


# Table Availability
class TableAvailability(models.Model):
    tbl_availability_id = models.AutoField(primary_key=True)
    table_id = models.OneToOneField(MasterTable, null=True, blank=True)
    tbl_availability_date = models.DateField()
    tbl_availability_status = models.CharField(max_length=15)
    tbl_availability_start_time = models.TimeField()
    tbl_availability_end_time = models.TimeField()

    def __str__(self):
        return '%s %s' % (self.table_id,self.tbl_availability_status)

    class Meta:
        verbose_name_plural = "18 Table Availability"
        

class MasterOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    table_id = models.ForeignKey(MasterTable)
    device_id = models.ForeignKey(MasterDevice)
    served_by = models.BigIntegerField()
    order_manager = models.BigIntegerField()
    order_status = models.CharField(max_length=15)
    order_date = models.DateTimeField()
    premise_id = models.ForeignKey(MasterPremise)

    def __str__(self):
        return '%s ' % (self.order_id)

    class Meta:
        verbose_name_plural = "19 Master Order"
        

class OrderDetails(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(MasterOrder)
    product_id = models.ForeignKey(MenuItem)
    product_quantity = models.FloatField()
    order_time = models.DateTimeField()
    product_delivery_status = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.order_id,self.product_id)

    class Meta:
        verbose_name_plural = "20 Order Details"


# Refactor Invoices according to GST and service charges if any.
class MasterInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(MasterOrder)
    customer_id = models.ForeignKey(Customer)
    invoice_datetime = models.DateTimeField()
    invoice_amount = models.FloatField()
    invoice_discount = models.FloatField()
    invoice_tax_id = models.IntegerField()
    premise_id = models.ForeignKey(MasterPremise)

    def __str__(self):
        return '%s ' % (self.invoice_id)

    class Meta:
        verbose_name_plural = "21 Client Invoice"


class InvoiceDetails(models.Model):
    invoice_details_id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(MasterInvoice)
    product_id = models.ForeignKey(MenuItem)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "22 Client Invoice Details"


# CustomerPayments
class CustomerPayments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    order_id = models.ForeignKey(MasterOrder)
    order_amount = models.FloatField()
    payment_type = models.CharField(max_length=10)
    amount_paid = models.FloatField()
    received_by = models.BigIntegerField()
    receipt_datetime = models.DateTimeField()
    premise_id = models.ForeignKey(MasterPremise)
   
    def __str__(self):
        return '%s ' % (self.payment_id)

    class Meta:
       verbose_name_plural = "23 Customer Payments"


# Customer Feedback
class CustomerFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    order_id = models.ForeignKey(MasterOrder)
    product_id = models.ForeignKey(MenuItem)
    feedback_scale = models.IntegerField(blank=True, null=True)
    feedback_text = models.CharField(max_length=100, blank=True, null=True)
    feedback_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (self.customer_id,self.feedback_text)

    class Meta:
       verbose_name_plural = "24 Customer Feedback"
        

# change customer to client
class TransactionLog(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_description = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=30)
    transaction_source = models.CharField(max_length=50)
    customer_id = models.ForeignKey(MasterCustomer)
    premise_id = models.ForeignKey(MasterPremise)
    transaction_identifier = models.CharField(max_length=50)
    transaction_create_date = models.DateTimeField()
    transaction_created_by = models.CharField(max_length=100)
    transaction_modified_date = models.DateTimeField()
    transaction_modified_by = models.CharField(max_length=100)
    def __str__(self):
        return '%s ' % (self.transaction_id)

    class Meta:
       verbose_name_plural = "25 Transaction Log"


# change to CustomerAnalytics
class CustomerAnalytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    premise_id = models.ForeignKey(MasterPremise)
    analytics_attribute = models.CharField(max_length=50, blank=True, null=True)
    attribute_value = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_modified_date = models.DateTimeField()
    
    def __str__(self):
        return '%s %s' % (self.analytics_attribute,self.attribute_value)

    class Meta:
        verbose_name_plural = "26 Customer Analytics"
