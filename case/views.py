from rest_framework.decorators import api_view
from rest_framework.views import APIView

from PetClinicBackend import settings
from PetClinicBackend.utils import json_response_false, json_response_true, json_response_unaccepted
from . import models, serializers, util


# Create your views here.


class CaseView(APIView):
    def init(request):
        try:
            models.Category.objects.all().delete()
            models.Case.objects.all().delete()
            models.Checkup.objects.all().delete()
            util.init_cases()
            util.init_checkups()
            util.init_category()
            return json_response_true("init case data successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            cases = models.Case.objects.all()
            serializer = serializers.CaseSerializer(cases, many=True)
            util.process_urls(serializer.data)
            msg = "Get All Cases successfully!"
            return json_response_true(msg, {
                "cases": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.CaseSerializer(data=request.data)
            # check if case_number already used
            case_number = request.data.get('case_number', None)
            check_case = models.Case.objects.filter(case_number=case_number.strip())
            if len(check_case) != 0:
                return json_response_unaccepted("Case number already used, change to another one and try again.")
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                return json_response_false("Failed to create a new case", e.args[0])
            serializer.save()
            return json_response_true("Create a new case successfully!")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            target_case = models.Case.objects.get(case_number=data['case_number'])
            target_case.disease_type = data.get('disease_type', '')
            target_case.disease_name = data.get('disease_name', '')
            target_case.pet_name = data.get('pet_name', '')
            target_case.pet_species = data.get('pet_species', '')
            target_case.pet_age = data.get('pet_age', -1)
            target_case.owner_name = data.get('owner_name', '')
            target_case.owner_phone = data.get('owner_phone', '')
            target_case.symptom_text = data.get('symptom_text', '')
            target_case.diagnosis_text = data.get('diagnosis_text', '')
            target_case.treatment_text = data.get('treatment_text', '')
            target_case.symptom_pic1 = data.get('symptom_pic1', '')
            target_case.symptom_pic2 = data.get('symptom_pic2', '')
            target_case.symptom_pic3 = data.get('symptom_pic3', '')
            target_case.diagnosis_pic1 = data.get('diagnosis_pic1', '')
            target_case.diagnosis_pic2 = data.get('diagnosis_pic2', '')
            target_case.diagnosis_pic3 = data.get('diagnosis_pic3', '')
            target_case.treatment_pic1 = data.get('treatment_pic1', '')
            target_case.treatment_pic2 = data.get('treatment_pic2', '')
            target_case.treatment_pic3 = data.get('treatment_pic3', '')
            target_case.symptom_video = data.get('symptom_video', '')
            target_case.diagnosis_video = data.get('diagnosis_video', '')
            target_case.treatment_video = data.get('treatment_video', '')
            target_case.save()
            return json_response_true("Modify a case successfully.")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request):
        try:
            # delete cases based on case_number list
            case_number_list = request.data.get('case_number_list', None)
            if case_number_list is None:
                return json_response_false("Empty case number list, please enter a proper one.")
            models.Case.objects.filter(case_number__in=case_number_list).delete()
            # delete all the checkups related with this case at the same time
            models.Checkup.objects.filter(case_number__in=case_number_list).delete()
            return json_response_true("Delete cases successfully.")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))


class CheckView(APIView):
    def get(self, request):
        try:
            checks = models.Checkup.objects.all()
            serializer = serializers.CheckupSerializer(checks, many=True)
            util.process_urls(serializer.data)
            msg = "Get All Checkups successfully!"
            return json_response_true(msg, {
                "checkups": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.CheckupSerializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                return json_response_false("Failed to create a checkup", e.args[0])
            serializer.save()
            return json_response_true("Create a new checkup successfully!")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            target_check = models.Checkup.objects.get(id=data['checkup_id'])
            target_check.case_number = data['case_number']
            target_check.checkup_item = data['checkup_item']
            target_check.checkup_text = data['checkup_text']
            target_check.checkup_video = data['checkup_video']
            target_check.checkup_pic1 = data['checkup_pic1']
            target_check.checkup_pic2 = data['checkup_pic2']
            target_check.checkup_pic3 = data['checkup_pic3']
            target_check.save()
            return json_response_true("Modify a checkup successfully.")
        except Exception as e:
            return json_response_false("Failed to modify a checkup." + str(e))

    def delete(self, request):
        try:
            checkup_id_list = request.data.get("checkup_id_list", None)
            if checkup_id_list is None:
                return json_response_false("Empty checkup_id list, please check again.")
            models.Checkup.objects.filter(id__in=checkup_id_list).delete()
            return json_response_true("Delete checkups successfully.")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))


class CategoryView(APIView):
    def get(self, request):
        try:
            categories = models.Category.objects.all()
            serializer = serializers.CategorySerializer(categories, many=True)
            msg = "Get all categories successfully!"
            return json_response_true(msg, {
                "case_categories": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))


@api_view(['GET'])
def get_single_case_by_number(request, case_number):
    try:
        case = models.Case.objects.filter(case_number=case_number)
        if not case.exists():
            return json_response_false("No case with this case number!")
        msg = "Find case with this case number successfully!"
        serializer = serializers.CaseSerializer(case, many=True)
        util.process_urls(serializer.data)
        return json_response_true(msg, {
            "case": serializer.data[0]
        })
    except (Exception, BaseException) as e:
        return json_response_false("invalid request, reason: " + str(e))


@api_view(['GET'])
def get_cases_by_name(request, disease_name):
    try:
        cases = models.Case.objects.filter(disease_name=disease_name)
        if not cases.exists():
            cases = models.Case.objects.filter(disease_type=disease_name)
            if not cases.exists():
                return json_response_false("No case!")
        msg = "Find cases with this disease_name successfully!"
        serializer = serializers.CaseSerializer(cases, many=True)
        util.process_urls(serializer.data)
        return json_response_true(msg, {
            "cases": serializer.data
        })
    except (Exception, BaseException) as e:
        return json_response_false("invalid request, reason: " + str(e))


@api_view(['GET'])
def get_cases_by_type(request, disease_type):
    try:
        cases = models.Case.objects.filter(disease_type=disease_type)
        if not cases.exists():
            return json_response_false("No case with this disease type!")
        msg = "Find cases with this disease type successfully!"
        serializer = serializers.CaseSerializer(cases, many=True)
        util.process_urls(serializer.data)
        return json_response_true(msg, {
            "cases": serializer.data
        })
    except (Exception, BaseException) as e:
        return json_response_false("invalid request, reason: " + str(e))


@api_view(['GET'])
def get_checkups_by_number(request, case_number):
    try:
        checkups = models.Checkup.objects.filter(case_number=case_number)
        if not checkups.exists():
            return json_response_true("No checkup with this case number.", {
                "checkups": []
            })
        msg = "Find checkups with this case number successfully!"
        serializer = serializers.CheckupSerializer(checkups, many=True)
        util.process_urls(serializer.data)
        return json_response_true(msg, {
            "checkups": serializer.data
        })
    except (Exception, BaseException) as e:
        return json_response_false("invalid request, reason: " + str(e))


@api_view(['POST'])
def post_picture(request):
    pic = request.FILES.get("pic", None)
    if pic is None:
        return json_response_false("Field 'pic' missing, please check again!")
    try:
        models.Pictures.objects.create(pic=pic)
    except Exception as e:
        return json_response_true("Fail to upload a pic", {
            "url": "none",
            "name": str(e),
            "status": "fail",
            "thumbUrl": "none"
        })
    serializer = serializers.PicturesSerializer(models.Pictures.objects.all().last())
    msg = "Upload a pic successfully!"
    pic_name = util.get_pic_name(serializer.data['pic'])
    return json_response_true(msg, {
        "url": settings.WEB_HOST_MEDIA_URL + serializer.data['pic'],
        "name": pic_name,
        "status": "done",
        "thumbUrl": settings.WEB_HOST_MEDIA_URL + serializer.data['pic']
    })


@api_view(['POST'])
def post_video(request):
    video = request.FILES.get("video", None)
    if video is None:
        return json_response_false("Field 'video' missing, please check again!")
    video_type = video.name[video.name.rindex(".") + 1:]
    if video_type is not "mp4":
        video_name = video.name
        new_filename = video_name[:video_name.rindex(".") + 1] + "mp4"
        video2 = video
        video2.name = new_filename
    try:
        if video_type is not "mp4":
            models.Videos.objects.create(video=video)
        else:
            models.Videos.objects.create(video=video2)
    except Exception as e:
        return json_response_true("Fail to upload a video", {
            "url": "none",
            "name": str(e),
            "status": "fail",
            "thumbUrl": "none"
        })
    serializer = serializers.VideosSerializer(models.Videos.objects.all().last())
    msg = "Upload a video successfully!"
    video_name = util.get_video_name(serializer.data['video'])
    return json_response_true(msg, {
        "url": settings.WEB_HOST_MEDIA_URL + serializer.data['video'],
        "name": video_name,
        "status": "done",
        "thumbUrl": settings.WEB_HOST_MEDIA_URL + serializer.data['video']
    })
