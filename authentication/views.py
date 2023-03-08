from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from rest_framework.views import APIView
import json


class UserView(APIView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        """Create a new User"""
        if request.body == b'':
            return HttpResponse('No request body')

        try:
            json_dict = json.loads(request.body)
        except Exception as e:
            return HttpResponse("Incorrect request body format")

        username = json_dict.get('username', None)
        if username is None:
            return HttpResponse('No username')

        password = json_dict.get('password', None)
        if password is None:
            return HttpResponse('No username')

        if User.objects.filter(username=username).exists():
            return HttpResponse('This username is already been used')

        User.objects.create_user(username, password=password)
        return HttpResponse('success')

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, pk, *args, **kwargs):
        user = User.objects.filter(pk=pk)
        if not user.exists():
            return HttpResponse("No such user")

        user.delete()
