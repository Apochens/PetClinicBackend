from pprint import pprint

from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from PetClinicBackend.utils import json_response_false, json_response_true
from . import models
from . import serializers


@require_http_methods(['GET'])
def role_init(request):
    from yaml import load, FullLoader
    from pathlib import Path

    def load_role():
        roles = load(Path('./data/role.yml').open('r', encoding='utf-8'), Loader=FullLoader)
        return [{
            'name': role,
            'description': roles[role]['description'],
            'jobs': ';'.join(roles[role]['jobs']),
        } for role in roles]

    def load_workflow():
        workflows = load(Path('./data/workflow.yml').open('r', encoding='utf-8'), Loader=FullLoader)
        return [{
            'name': workflow,
            'process': workflows[workflow],
        } for workflow in workflows]

    sers = [
        serializers.RoleSerializer(data=load_role(), many=True),
        serializers.WorkflowSerializer(data=load_workflow(), many=True)
    ]

    try:
        for ser in sers:
            ser.is_valid(raise_exception=True)
    except Exception as e:
        pprint(e)
        return json_response_false("Init failed")

    for ser in sers:
        ser.save()

    return json_response_true("success")


# Create your views here.
class RoleAPIView(APIView):

    def get(self, request):
        pass


@api_view(['GET'])
def get_role_by_id(request, role_id):

    role: models.Role = models.Role.objects.get(id=role_id)
    workflows = models.Workflow.objects.filter(name__in=role.jobs.split(';'))

    return json_response_true("Return information about reception", {
        'role': role.name,
        'description': role.description,
        'jobs': {workflow.name: workflow.process for workflow in workflows},
    })