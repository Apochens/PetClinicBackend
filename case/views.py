from rest_framework.decorators import api_view
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_false, json_response_true
from . import models, serializers


# Create your views here.

class CaseView(APIView):
    def get(self, request):
        cases = models.Case.objects.all()
        serializer = serializers.CaseSerializer(cases, many=True)
        msg = "Get All Cases successfully!"
        return json_response_true(msg, {
            "cases": serializer.data
        })

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


@api_view(['GET'])
def get_single_case_by_number(request, case_number):
    case = models.Case.objects.filter(case_number=case_number)
    if not case.exists():
        return json_response_false("No case with this case number!")
    msg = "Find case with this case number successfully!"
    serializer = serializers.CaseSerializer(case[0])
    return json_response_true(msg, {
        "case": serializer.data
    })


@api_view(['GET'])
def get_cases_by_name(request, disease_name):
    cases = models.Case.objects.filter(disease_name=disease_name)
    if not cases.exists():
        return json_response_false("No case with this disease name!")
    msg = "Find cases with this disease_name successfully!"
    serializer = serializers.CaseSerializer(cases, many=True)
    return json_response_true(msg, {
        "cases": serializer.data
    })


def get_checkups_by_number(request, case_number):
    checkups = models.Checkup.objects.filter(case_number=case_number)
    if not checkups.exists():
        return json_response_false("No checkup with this case number!")
    msg = "Find checkups with this case number successfully!"
    serializer = serializers.CheckupSerializer(checkups, many=True)
    return json_response_true(msg, {
        "checkups": serializer.data
    })
