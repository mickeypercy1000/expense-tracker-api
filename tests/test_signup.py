from django.test import TestCase
from rest_framework import status
import requests

class TestUserSignup(TestCase):

    def test_signup_successful(self):
        url = 'http://127.0.0.1:8000/auth/signup/'
        payload = {
            'email': 'user2@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'Tes3ter',
            'password': 'Test.1password'
        }
        response = requests.request("POST", url, data=payload)
        # print("response1", response.text["email"][0])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.text[0][0], "email already exists")

    def test_signup_failed(self):
        url = 'http://127.0.0.1:8000/auth/signup/'
        # missing required "email" field
        payload = {
            'password': 'Test.1password',
            'first_name': 'mike',
            'last_name': 'amoo'
        }
        response = requests.request("POST", url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


