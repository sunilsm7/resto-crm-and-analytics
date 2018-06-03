from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from orders.models import (
    MasterOrder, OrderDetails, MasterInvoice, InvoiceDetails, CustomerPayments, CustomerFeedback
)


class MasterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterOrder
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class MasterInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterInvoice
        fields = '__all__'


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = '__all__'


class CustomerPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayments
        fields = '__all__'


class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = '__all__'
