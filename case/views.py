from rest_framework.decorators import api_view
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_false, json_response_true
from . import models, serializers
from PetClinicBackend import settings


# Create your views here.

class CaseView(APIView):
    def get(self, request):
        cases = models.Case.objects.all()
        serializer = serializers.CaseSerializer(cases, many=True)
        for record in serializer.data:
            for key in record.keys():
                if "pic" in key or "video" in key:
                    record[key] = settings.WEB_HOST_MEDIA_URL + record[key]
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
    serializer = serializers.CaseSerializer(case, many=True)
    for record in serializer.data:
        for key in record.keys():
            if "pic" in key or "video" in key:
                record[key] = settings.WEB_HOST_MEDIA_URL + record[key]
    return json_response_true(msg, {
        "case": serializer.data[0]
    })


@api_view(['GET'])
def get_cases_by_name(request, disease_name):
    cases = models.Case.objects.filter(disease_name=disease_name)
    if not cases.exists():
        return json_response_false("No case with this disease name!")
    msg = "Find cases with this disease_name successfully!"
    serializer = serializers.CaseSerializer(cases, many=True)
    for record in serializer.data:
        for key in record.keys():
            if "pic" in key or "video" in key:
                record[key] = settings.WEB_HOST_MEDIA_URL + record[key]
    return json_response_true(msg, {
        "cases": serializer.data
    })


@api_view(['GET'])
def get_checkups_by_number(request, case_number):
    checkups = models.Checkup.objects.filter(case_number=case_number)
    if not checkups.exists():
        return json_response_false("No checkup with this case number!")
    msg = "Find checkups with this case number successfully!"
    serializer = serializers.CheckupSerializer(checkups, many=True)
    for record in serializer.data:
        for key in record.keys():
            if "pic" in key or "video" in key:
                record[key] = settings.WEB_HOST_MEDIA_URL + record[key]
    return json_response_true(msg, {
        "checkups": serializer.data
    })


@api_view(['POST'])
def test_upload(request):
    case_number = request.POST.get("case_number", "")
    checkup_item = request.POST.get("checkup_item", "")

    checkup_pic = request.FILES.get("checkup_pic", "")
    checkup_video = request.FILES.get("checkup_video", "")
    pic_extend_name = checkup_pic.name[checkup_pic.name.rindex(".") + 1:]
    allow_ends = ["png", "jpg"]
    if pic_extend_name not in allow_ends:
        return json_response_false("Pic format not supported.")
    video_extend_name = checkup_video.name[checkup_video.name.rindex(".") + 1:]
    allow_ends2 = ["mp4"]
    if video_extend_name not in allow_ends2:
        return json_response_false("Video format not supported.")

    models.Checkup.objects.create(case_number=case_number,
                                  checkup_item=checkup_item,
                                  checkup_pic=checkup_pic,
                                  checkup_video=checkup_video)
    return json_response_true("Insert a checkup with picture and video successfully.")
