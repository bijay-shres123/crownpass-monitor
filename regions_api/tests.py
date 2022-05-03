from http.client import FORBIDDEN
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Region
from .serializers import RegionSerializer
from django.urls import reverse

class RegionRegistrationTestCase(APITestCase):

    """RETURN FORBIDDEN IF USER NOT LOGGED IN"""
    def test_registration(self):
        self.authenticate()
        data = {
           'region_name':'ENGLAND',
           'county_name':'Essex',
           'city_town':'Test City',
           'status':'RED',
        }
        response = self.client.post("/api/regions/",data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN