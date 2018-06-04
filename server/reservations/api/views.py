import json
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from reservations.models import (
    Customer, CustomerDetails, MasterTable, TableAttributes, TableAvailability, ReservationQueue, CustomerAnalytics)

from .serializers import (
    CustomerSerializer, CustomerDetailsSerializer, MasterTableSerializer, TableAttributesSerializer,
    TableAvailabilitySerializer, ReservationQueueSerializer, CustomerAnalyticsSerializer)    


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDetailsSerializer
    queryset = CustomerDetails.objects.all()


class MasterTableViewSet(viewsets.ModelViewSet):
    serializer_class = MasterTableSerializer
    queryset = MasterTable.objects.all()


class TableAtrributesViewSet(viewsets.ModelViewSet):
    serializer_class = TableAttributesSerializer
    queryset = TableAttributes.objects.all()


class TableAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = TableAvailabilitySerializer
    queryset = TableAvailability.objects.all()


class ReservationQueueViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationQueueSerializer
    queryset = ReservationQueue.objects.all()


class CustomerAnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAnalyticsSerializer
    queryset = CustomerAnalytics.objects.all()
