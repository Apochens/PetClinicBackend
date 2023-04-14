import json

from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_true, json_response_false


@require_http_methods(['GET'])
def authentication_init(request):
    User.objects.create_superuser('root', 'root@123.com', '123456')
    User.objects.create_user('user1', 'user1@123.com', 'user1')
    User.objects.create_user('user2', 'user2@123.com', 'user2')
    User.objects.create_user('user3', 'user3@123.com', 'user3')


@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body)
    username = data.get('username', None)
    if username is None:
        return json_response_false('No username!')

    if User.objects.filter(username=username).exists():
        return json_response_false("This user exists already!")

    password = data.get('password', None)
    if password is None:
        return json_response_false('No password!')

    superuser = data.get('superuser', None)
    if superuser is None or not superuser:
        User.objects.create_user(username, password=password)
    else:
        User.objects.create_superuser(username, password=password)

    return json_response_true("Create successfully!")


class UserView(APIView):

    def get(self, request, *args, **kwargs):
        """Get the user list"""
        return json_response_true("Fetch all users successfully", {
            "users": list(map(lambda user: {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "superuser": True if user.is_superuser else False
            }, User.objects.all()))
        })

    # def post(self, request, *args, **kwargs):
    #     """Create a new User"""
    #     username = request.data.get('username', None)
    #     if username is None:
    #         return json_response_false('No username!')
    #
    #     if User.objects.filter(username=username).exists():
    #         return json_response_false("This user exists already!")
    #
    #     password = request.data.get('password', None)
    #     if password is None:
    #         return json_response_false('No password!')
    #
    #     superuser = request.data.get('superuser', None)
    #     if superuser is None or not superuser:
    #         User.objects.create_user(username, password=password)
    #     else:
    #         User.objects.create_superuser(username, password=password)
    #
    #     return json_response_true("Create successfully!")

    def put(self, request, *args, **kwargs):
        """Modify the user information"""
        username = request.data.get('username', None)
        if username is None:
            return json_response_false("No username given!")
        # if username is not None:
        #     if User.objects.filter(username=username).exists():
        #         return json_response_false("This username exists already!")

        if not User.objects.filter(username=username).exists():
            return json_response_false("No such user!")

        user = User.objects.get(username=username)

        password = request.data.get('password', None)
        if password is not None:
            user.set_password(password)

        superuser = request.data.get('superuser', None)
        if superuser:
            user.is_superuser = 1 if superuser else 0
            user.is_staff = 1 if superuser else 0

        user.save()
        return json_response_true("Modified successfully!")

    def delete(self, request, *args, **kwargs):
        """Delete one user or a collection of users"""
        users = request.data.get('users', None)
        if users is not None:
            User.objects.filter(id__in=users).delete()
        return json_response_true("Deleted successfully!")

