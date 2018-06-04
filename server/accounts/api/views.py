import json
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from accounts.models import UserProfile


from .serializers import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
