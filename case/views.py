from django.shortcuts import render
from rest_framework.views import APIView

from .models import Case
from . import models, serializers
from PetClinicBackend.utils import json_response_false, json_response_true


# Create your views here.

class CaseView(APIView):
    def get(self, request):
        cases = models.Case.objects.all()
        # for case_main in case_mains:
        #     print(case_main.case_number)
        serializer = serializers.CaseSerializer(cases, many=True)
        msg = "Get All Cases successfully!"
        return json_response_true(msg, {"Cases": serializer.data})

    def post(self, request):
        serializer = serializers.CaseSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create a new case", e.args[0])
        serializer.save()
        msg = "Create a new case successfully!"
        return json_response_true(msg)


class CheckView(APIView):
    def get(self, request):
        checkups = models.Checkup.objects.all()
        serializer = serializers.CheckupSerializer(checkups, many=True)
        msg = "Get All Checkups successfully!"
        return json_response_true(msg, {"Checkups": serializer.data})

    def post(self, request):
        serializer = serializers.CheckupSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create a checkup", e.args[0])
        serializer.save()
        msg = "Create a new checkup successfully!"
        return json_response_true(msg)
