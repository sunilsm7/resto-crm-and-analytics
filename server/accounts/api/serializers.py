from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
