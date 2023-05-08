

from django.test import TestCase
from rest_framework import status
import requests

class TestIncomeDetail(TestCase):

    def test_income_detail_successful(self):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTg3MTI3LCJpYXQiOjE2NzkxODY4MjcsImp0aSI6IjUwNzhiNGRjOWNiZDQxZTViMmM4MzA4YjJiYmUxNTk3IiwidXNlcl9pZCI6IjA0MTAzMjQ4LWE3ZGQtNGExNy04NTQ0LWE5ZDJiMWU2ODg2MiJ9.CPSYxK-MB8ULijIA71YHjByal6LHdLqd7xo6eEE1d9U"
        }
        userID = "26b209f7-0ec7-4d88-bb30-01a0a17d6297"
        url = f"http://127.0.0.1:8000/user/income/{userID}/"

        response = requests.request("GET", url, headers=headers)
        print("rrrrrrrrrr", response.text)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_income_detail_failed(self):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTg3MTI3LCJpYXQiOjE2NzkxODY4MjcsImp0aSI6IjUwNzhiNGRjOWNiZDQxZTViMmM4MzA4YjJiYmUxNTk3IiwidXNlcl9pZCI6IjA0MTAzMjQ4LWE3ZGQtNGExNy04NTQ0LWE5ZDJiMWU2ODg2MiJ9.CPSYxK-MB8ULijIA71YHjByal6LHdLqd7xo6eEE1d9U"
        }
        userID = "26b209f7-0ec7-4d88-bb30-01a0a17d6297"
        url = f"http://127.0.0.1:8000/user/income/{userID}/"

        response = requests.request("GET", url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
