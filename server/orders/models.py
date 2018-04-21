from django.db import models
from django.conf import settings

from restaurant.models import MasterPremise,MasterDevice
from menus.models import MenuItem
from reservations.models import MasterTable, Customer

User = settings.AUTH_USER_MODEL
# Create your models here.

class MasterOrder(models.Model):
    ORDER_STATUS = (
        ('Delivered','Delivered'),
        ('Cooking','Cooking'),
        ('Pending','Pending'),
        )
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_order')
    table_id = models.ForeignKey(MasterTable, on_delete=models.CASCADE,related_name='order_table')
    device_id = models.ForeignKey(MasterDevice, on_delete=models.CASCADE,related_name='device_order')
    served_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='served_by')
    order_manager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='order_manager')
    order_status = models.CharField(max_length=15,choices=ORDER_STATUS,default='Cooking')
    order_date = models.DateTimeField()
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE,related_name='premise_order')

    def __str__(self):
        return f'Order ID : {self.order_id}'

    class Meta:
        verbose_name_plural = "Master Order"
        

class OrderDetails(models.Model):
    DELIVERY_STATUS = (
        ('Served','Served'),
        ('Ready For Serving','ReadyForServing'),
        )
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(MasterOrder, on_delete=models.CASCADE,related_name='oreder_details')
    item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE,related_name='ordered_item')
    product_quantity = models.IntegerField()
    order_time = models.DateTimeField()
    item_delivery_status = models.CharField(max_length=30, choices=DELIVERY_STATUS,related_name='item_delivery_status')

    def __str__(self):
        return f'Order ID : {self.order_id} Item ID : {self.item_id}'

    class Meta:
        verbose_name_plural = "Order Details"


class MasterInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(MasterOrder, on_delete=models.CASCADE, related_name='order_invoice')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers_invoice')
    invoice_datetime = models.DateTimeField()
    invoice_amount = models.FloatField()
    invoice_discount = models.FloatField()
    invoice_tax_id = models.IntegerField()
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_order_invoice')

    def __str__(self):
        return f'Invoice ID : {self.invoice_id}'

    class Meta:
        verbose_name_plural = "Client Invoice"


class InvoiceDetails(models.Model):
    invoice_details_id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(MasterInvoice, on_delete=models.CASCADE, related_name='invoice_details')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_menuitem')
    menu_item_quantity = models.IntegerField()
    menu_item_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Client Invoice Details"


class CustomerPayments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_payment')
    order_id = models.ForeignKey(MasterOrder, on_delete=models.CASCADE, related_name='order_payment')
    order_amount = models.FloatField()
    payment_type = models.CharField(max_length=10)
    amount_paid = models.FloatField()
    received_by = models.BigIntegerField()
    receipt_datetime = models.DateTimeField()
    premise_id = models.ForeignKey(MasterPremise, on_delete=models.CASCADE, related_name='premise_payment')
   
    def __str__(self):
        return f'Payment ID : {self.payment_id}'

    class Meta:
       verbose_name_plural = "Customer Payments"


class CustomerFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_feedback')
    order_id = models.ForeignKey(MasterOrder, on_delete=models.CASCADE, related_name='order_feedback')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menu_item_feedback')
    feedback_scale = models.IntegerField(blank=True, null=True)
    feedback_text = models.CharField(max_length=100, blank=True, null=True)
    feedback_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f'Customer ID : {self.customer_id} Feedback : {self.feedback_text}'

    class Meta:
       verbose_name_plural = "Customer Feedback"