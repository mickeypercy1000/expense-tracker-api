from django.test import TestCase
from rest_framework import status
import requests

class TestAddExpenditure(TestCase):

    def test_add_expenditure_successful(self):
        url = "http://127.0.0.1:8000/user/expenditure/"
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTg3MTI3LCJpYXQiOjE2NzkxODY4MjcsImp0aSI6IjUwNzhiNGRjOWNiZDQxZTViMmM4MzA4YjJiYmUxNTk3IiwidXNlcl9pZCI6IjA0MTAzMjQ4LWE3ZGQtNGExNy04NTQ0LWE5ZDJiMWU2ODg2MiJ9.CPSYxK-MB8ULijIA71YHjByal6LHdLqd7xo6eEE1d9U"
        }
        payload = {
            "category":"fuel",
            "nameOfItem":"fuel to town",
            "estimatedAmount":11
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_expenditure_fail(self):

        url = "http://127.0.0.1:8000/user/expenditure/"
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTg3MTI3LCJpYXQiOjE2NzkxODY4MjcsImp0aSI6IjUwNzhiNGRjOWNiZDQxZTViMmM4MzA4YjJiYmUxNTk3IiwidXNlcl9pZCI6IjA0MTAzMjQ4LWE3ZGQtNGExNy04NTQ0LWE5ZDJiMWU2ODg2MiJ9.CPSYxK-MB8ULijIA71YHjByal6LHdLqd7xo6eEE1d9U"
        }
        payload = {
            "category":"",
            "nameOfItem":"fuel to town",
            "estimatedAmount":1.1
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


