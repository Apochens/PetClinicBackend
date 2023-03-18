from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_false, json_response_true
from . import models, serializers


# Create your views here.

class CaseView(APIView):
    def get(self, request):
        cases = models.Case.objects.all()
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

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CheckView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        serializer = serializers.CheckupSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create a checkup", e.args[0])
        serializer.save()
        msg = "Create a new checkup successfully!"
        return json_response_true(msg)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CategoryView(APIView):
    def get(self, request):
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        print(serializer.data)
        msg = "Get all categories successfully!"
        return json_response_true(msg, {
            "case_categories": serializer.data
        })

    def post(self, request):
        serializer = serializers.CategorySerializer(data=request.data, many=True)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to insert categories", e.args[0])
        serializer.save()
        msg = "Insert categories successfully!"
        return json_response_true(msg)
