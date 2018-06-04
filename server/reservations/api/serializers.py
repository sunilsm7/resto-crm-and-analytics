from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from reservations.models import (
    Customer, CustomerDetails, MasterTable, TableAttributes, TableAvailability, ReservationQueue, CustomerAnalytics)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'


class MasterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTable
        fields = '__all__'


class TableAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAttributes
        fields = '__all__'


class TableAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAvailability
        fields = '__all__'


class ReservationQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationQueue
        fields = '__all__'


class CustomerAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnalytics
        fields = '__all__'
