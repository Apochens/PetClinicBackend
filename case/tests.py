from django.test import TestCase
import requests
from . import util


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
    def test_get_pic_name1(self):
        res = util.get_pic_name("http://127.0.0.1:8000/media/images/dog1_symptom_pic1.png")
        self.assertEqual(res, "dog1_symptom_pic1")

    def test_get_pic_name2(self):
        res = util.get_pic_name("http://127.0.0.1:8000/media/images/ccccc.png")
        self.assertEqual(res, "ccccc")

    def test_get_pic_name3(self):
        res = util.get_pic_name("http://127.0.0.1:8000/media/images/ssssssymptm.png")
        self.assertEqual(res, "ssssssymptm")

    def test_get_video_name1(self):
        res = util.get_video_name("http://127.0.0.1:8000/media/videos/dog1_symptom_video.mp4")
        self.assertEqual(res, "dog1_symptom_video")

    def test_get_video_name2(self):
        res = util.get_video_name("http://127.0.0.1:8000/media/videos/catttttttt_1.mp4")
        self.assertEqual(res, "catttttttt_1")

    def test_get_video_name3(self):
        res = util.get_video_name("http://127.0.0.1:8000/media/videos/ssssssssssss__2.mp4")
        self.assertEqual(res, "ssssssssssss__2")
