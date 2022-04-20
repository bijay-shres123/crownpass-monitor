from django.shortcuts import render
from results_api import models
from rest_framework import viewsets
from rest_framework import status
from results_api import serializers
from rest_framework.authentication import TokenAuthentication
from staff_api import permissions
from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class ResultsViewSet(viewsets.ModelViewSet):

    # def get_serializer_class(self,*args,**kwargs):
    #     if self.action in ['list','retrieve']:
    #         return serializers.ResultsReadSerializer
    #     else:
    #         return serializers.ResultsWriteSerializer
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.ResultsSerializer
    queryset = models.Results.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    # search_fields = ('', 'email',)

# class UserLoginApiView(ObtainAuthToken):
#    """Handle creating  authentication tokens"""
#    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES