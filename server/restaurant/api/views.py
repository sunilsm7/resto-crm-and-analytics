import json
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from accounts.api.permissions import IsOwnerOrReadOnly
from restaurant.models import (
    MasterClient, MasterRestaurant, MasterPremise, PremiseSections, MasterDevice, ClientConfiguration,
    ClientRoles, MasterClientInvoice, ClientPayments, ClientAccount, TransactionLog)

from .serializers import (
    MasterClientSerializer, MasterRestaurantSerializer, MasterPremiseSerializer, PremiseSectionsSerializer,
    MasterDeviceSerializer, ClientConfigurationSerializer, ClientRolesSerializer, MasterClientInvoiceSerializer,
    ClientPaymentsSerializer, ClientAccountSerializer, TransactionLogSerializer)


class MasterClientViewSet(viewsets.ModelViewSet):
    serializer_class = MasterClientSerializer
    queryset = MasterClient.objects.all()


class MasterRestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = MasterRestaurantSerializer
    queryset = MasterRestaurant.objects.all()


class MasterPremiseViewSet(viewsets.ModelViewSet):
    serializer_class = MasterPremiseSerializer
    queryset = MasterPremise.objects.all()


class PremiseSectionsViewSet(viewsets.ModelViewSet):
    serializer_class = PremiseSectionsSerializer
    queryset = PremiseSections.objects.all()


class MasterDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = MasterDeviceSerializer
    queryset = MasterDevice.objects.all()


class ClientConfigurationViewSet(viewsets.ModelViewSet):
    serializer_class = ClientConfigurationSerializer
    queryset = ClientConfiguration.objects.all()


class ClientRolesViewSet(viewsets.ModelViewSet):
    serializer_class = ClientRolesSerializer
    queryset = ClientRoles.objects.all()


class MasterClientInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = MasterClientInvoiceSerializer
    queryset = MasterClientInvoice.objects.all()


class ClientPaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = ClientPaymentsSerializer
    queryset = ClientPayments.objects.all()


class ClientAccountViewSet(viewsets.ModelViewSet):
    serializer_class = ClientAccountSerializer
    queryset = ClientAccount.objects.all()


class TransactionLogViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionLogSerializer
    queryset = TransactionLog.objects.all()
