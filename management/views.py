from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_true
from management import serializers
from management.models import Department, DepartmentChoice


def get(request, id):
    assert id <= 14
    res = Department.objects.get(name=id)
    serializer = serializers.DepartmentSerializer(res, many=False)
    return json_response_true("200", {
        "department": serializer.data
    })

# Create your views here.
class DepartmentAPIView(APIView):
    pass