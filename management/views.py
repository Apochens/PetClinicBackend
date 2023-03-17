from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_true, json_response_false
from management import serializers
from management.models import Department, Medicine
from management.util import init_department, init_medicine

# Create your views here.
class DepartmentAPIView(APIView):
    def init(request):
        try:
            init_department()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            res = Department.objects.all()
            serializer = serializers.DepartmentSerializer(res, many=True)
            return json_response_true("get successfully", {
                "departmentlist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.DepartmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response_true("create new department successfully", {
                "department": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            id = data["id"]
            assert id is not None
            res = Department.objects.get(id=id)
            if data["name"]:
                res.name = data["name"]
            if data["description"]:
                res.description = data["description"]
            res.save()
            serializer = serializers.DepartmentSerializer(res, many=False)
            return json_response_true("update department successfully", {
                "department": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class DepartmentAPISingleView(APIView):
    def get(self, request, id):
        try:
            res = Department.objects.get(id=id)
            serializer = serializers.DepartmentSerializer(res, many=False)
            return json_response_true("get successfully", {
                "department": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request, id):
        try:
            res = Department.objects.get(id=id)
            serializer = serializers.DepartmentSerializer(res, many=False)
            Department.objects.get(id=id).delete()
            return json_response_true("delete successfully", {
                "department": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class MedicineAPIView(APIView):
    def init(request):
        try:
            init_medicine()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            res = Medicine.objects.all()
            serializer = serializers.MedicineSerializer(res, many=True)
            return json_response_true("get successfully", {
                "medicinelist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.MedicineSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response_true("create new medicine successfully", {
                "medicine": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            id = data["id"]
            assert id is not None
            res = Medicine.objects.get(id=id)
            if data["name"]:
                res.name = data["name"]
            if data["type"]:
                res.type = data["type"]
            if data["tag"]:
                res.tag = data["tag"]
            if data["price"]:
                res.price = data["price"]
            if data["description"]:
                res.description = data["description"]
            res.save()
            serializer = serializers.MedicineSerializer(res, many=False)
            return json_response_true("update medicine successfully", {
                "medicine": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class MedicineAPISingleView(APIView):
    def get(self, request, id):
        try:
            res = Medicine.objects.get(id=id)
            serializer = serializers.MedicineSerializer(res, many=False)
            return json_response_true("get successfully", {
                "medicine": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request, id):
        try:
            res = Medicine.objects.get(id=id)
            serializer = serializers.MedicineSerializer(res, many=False)
            Medicine.objects.get(id=id).delete()
            return json_response_true("delete successfully", {
                "medicine": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))