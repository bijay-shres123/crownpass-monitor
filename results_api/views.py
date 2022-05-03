from django.shortcuts import render
from rest_framework.response import Response
from results_api import models
from rest_framework import viewsets, views
from rest_framework import status
from results_api import serializers
from rest_framework.authentication import TokenAuthentication
from staff_api import permissions
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
import platform

class ResultsViewSet(viewsets.ModelViewSet):

    # def get_serializer_class(self,*args,**kwargs):
    #     if self.action in ['list','retrieve']:
    #         return serializers.ResultsReadSerializer
    #     else:
    #         return serializers.ResultsWriteSerializer
    """Handle creating, creating and updating Results"""
    serializer_class = serializers.ResultsSerializer
    queryset = models.Result.objects.all()

 
    permission_classes = [IsAuthenticatedOrReadOnly,]

    filter_backends = (filters.SearchFilter,)

    
    # search_fields = ('', 'email',)

# class UserLoginApiView(ObtainAuthToken):
#    """Handle creating  authentication tokens"""
#    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class CompView(views.APIView):
    def get(self, request):
        return Response(platform.node())