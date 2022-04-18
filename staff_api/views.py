from django.shortcuts import render
from staff_api import models
from rest_framework import viewsets
from rest_framework import status
from staff_api import serializers

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
