from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from PetClinicBackend.utils import json_response_false, json_response_true
from . import models


# Create your views here.
class RoleAPIView(APIView):

    def get(self, request):
        pass


@api_view(['GET'])
def get_role_by_id(request, role_id):

    # reception
    if role_id == 0:
        role: models.Role = models.Role.objects.get(id=role_id)
        workflows = models.Workflow.objects.filter(name__in=role.jobs.split(';'))

        return json_response_true("Return information about reception")

    # assistant
    if role_id == 1:
        return json_response_true("Return information about assistant")

    # doctor
    if role_id == 2:
        return json_response_true("Return information about doctor")
