from django.shortcuts import render
from rest_framework import viewsets
from regions_api import serializers
from .filters import RegionFilter
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.settings import api_settings
from .models import Region
import django_filters.rest_framework

class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = serializers.RegionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = RegionFilter
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.RegionNestedSerializer
        return serializers.RegionSerializer

    def perform_create(self, serializer):
        serializer.save(listed_by=self.request.user)

