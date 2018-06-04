import json
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from orders.models import (
    MasterOrder, OrderDetails, MasterInvoice, InvoiceDetails, CustomerPayments, CustomerFeedback
)


from .serializers import (
    MasterOrderSerializer, OrderDetailsSerializer, MasterInvoiceSerializer, InvoiceDetailsSerializer,
    CustomerPaymentsSerializer, CustomerFeedbackSerializer
)


class MasterOrderViewSet(viewsets.ModelViewSet):
    serializer_class = MasterOrderSerializer
    queryset = MasterOrder.objects.all()


class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class MasterInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = MasterInvoiceSerializer
    queryset = MasterInvoice.objects.all()


class InvoiceDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceDetailsSerializer
    queryset = InvoiceDetails.objects.all()


class CustomerPaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerPaymentsSerializer
    queryset = CustomerPayments.objects.all()


class CustomerFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerFeedbackSerializer
    queryset = CustomerFeedback.objects.all()
