from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from restaurant.models import (
    MasterClient, MasterRestaurant, MasterPremise, PremiseSections, MasterDevice, ClientConfiguration,
    ClientRoles, MasterClientInvoice, ClientPayments, ClientAccount, TransactionLog)



class MasterClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClient
        fields = '__all__'


class MasterRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterRestaurant
        fields = '__all__'


class MasterPremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterPremise
        fields = '__all__'


class PremiseSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiseSections
        fields = '__all__'


class MasterDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDevice
        fields = '__all__'


class ClientConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientConfiguration
        fields = '__all__'


class ClientRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientRoles
        fields = '__all__'


class MasterClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClientInvoice
        fields = '__all__'


class ClientPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPayments
        fields = '__all__'


class ClientAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAccount
        fields = '__all__'


class TransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = '__all__'
