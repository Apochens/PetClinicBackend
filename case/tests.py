from django.test import TestCase
import requests
from django.contrib.auth.models import User


# Create your tests here.

class CaseTest(TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/"

    def test_create_user(self):
        data1 = {
            'username': 'test',
            'password': 'test111',
            'superuser': False
        }
        requests.post(url=self.base_url + '/authentication/user/register',
                      data=data1)
        data2 = {
            'username': 'test',
            'password': 'test111'
        }
        token = requests.post(url=self.base_url + 'authentication/token/',
                              data=data2)
        headers = {
            'Authorization': token.json().get("access")
        }
        r = requests.get(url=self.base_url + 'authentication/user/',
                         headers=headers)
        result = r.json()
        self.assertEqual(result.get("message"), "Fetch all users successfully")
