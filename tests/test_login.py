from django.test import TestCase
from rest_framework import status
import requests

class TestUserLogin(TestCase):

    def test_login_successful(self):
        url = 'http://127.0.0.1:8000/auth/login/'
        payload = {
            'email': 'user2@example.com',
            'password': 'Test.1password'
        }
        response = requests.request("POST", url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_failed(self):
        url = 'http://127.0.0.1:8000/auth/signup/'
        payload = {
            'email': 'mike@gmial.com',
            'password': 'Test.1password'
        }
        response = requests.request("POST", url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
