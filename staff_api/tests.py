import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


from .serializers import UserProfileSerializer
from .models import UserProfile, UserProfileManager

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "email":"test@crownpass.com",
            "name":"test user",
            "password":"some_strong_password123",
            "contact":"321312",
            "address":"Ox",
            "position":"Staff",
            "is_staff":"True",
        }
        response = self.client.post("/api/profile/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AuthenticationTestCase(APITestCase):
    def authenticate(self):
        data = {
            "email":"test@crownpass.com",
            "name":"test user",
            "password":"some_strong_password123",
            "contact":"321312",
            "address":"Ox",
            "position":"Staff",
            "is_staff":"True",
        }
        self.client.post("/api/profile/",data)

        response =  self.client.post('/api/login/',{
            "email":"test@crownpass.com",
            "password":"some_strong_password123"
        })

        self.client.credentials(HTTP_AUTHORIZTION=f"Bearer {response.data['token']}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)