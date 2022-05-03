import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from results_api.views import ResultsViewSet

from .serializers import ResultsSerializer
from .models import Result

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "number_of_positive"  :"2131232",
            "number_of_recoverd":"312312",
            "number_of_negative" :"23213",
            "date" : "2010-10-12",
           
        }
        response = self.client.post("/api/results/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

