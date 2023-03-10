from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from PetClinicBackend.utils import json_response_true, json_response_false


class UserView(APIView):

    def get(self, request, *args, **kwargs):
        """Get the user list"""
        fetch_data = lambda user: {"id": user.id, "username": user.username}
        return json_response_true("Fetch all users successfully", {
            "list": list(map(fetch_data, User.objects.all()))
        })

    def post(self, request, *args, **kwargs):
        """Create a new User"""
        username = request.data.get('username', None)
        if username is None:
            return json_response_false('No username!')

        password = request.data.get('password', None)
        if password is None:
            return json_response_false('No password!')

        if User.objects.filter(username=username).exists():
            return json_response_false("This user exists already!")

        User.objects.create_user(username, password=password)
        return json_response_true("Create successfully!")

    def put(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if id is None:
            return json_response_false("No id provided!")

        if not User.objects.filter(id=id).exists():
            return json_response_false("No such user!")

        user = User.objects.get(id=id)

        username = request.data.get('username', None)
        if username is not None:
            if User.objects.filter(username=username).exists():
                return json_response_false("This username exists already!")
            user.username = username

        password = request.data.get('password', None)
        if password is not None:
            user.set_password(password)

        user.save()
        return json_response_true("Modified successfully!")

    def delete(self, request, *args, **kwargs):
        uid = request.data.get('id', None)
        if uid is None:
            return json_response_false("No id provided!")

        if User.objects.filter(id=uid).exists():
            User.objects.get(id=uid).delete()

        return json_response_true("Deleted successfully!")

