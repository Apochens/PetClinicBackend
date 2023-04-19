from django.test import TestCase
import requests
from django.contrib.auth.models import User


# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        self.base_auth_url = "http://127.0.0.1:8000/authentication/"

    def test_get_users(self):
        data1 = {
            'username': 'root',
            'password': '123456'
        }
        token = requests.post(url=self.base_auth_url + 'token/', data=data1)
        headers = {
            'Authorization': 'Token ' + token.json().get('access')
        }
        r = requests.get(url=self.base_auth_url + 'user/', headers=headers)
        result = r.json()
        self.assertEqual(result.get("message"), "Fetch all users successfully")


class FunctionTest(TestCase):
    pass
