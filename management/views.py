import json
from datetime import datetime

from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_true, json_response_false
from management import serializers
from management.models import Department, Medicine, Instrumentation, Checkup, Hospitalization
from management.util import init_department, init_medicine, init_instrumentation, init_checkup, init_hospitalization


# Create your views here.
class DepartmentAPIView(APIView):
    def init(request):
        try:
            init_department()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def instrumentation(request, id):
        try:
            dept = Department.objects.get(id=id)
            ins = Instrumentation.objects.filter(dept_id=dept)
            serializer = serializers.InstrumentationSerializer(ins, many=True)
            return json_response_true("get successfully", {
                "instrumentationlist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def checkup(request, id):
        try:
            dept = Department.objects.get(id=id)
            ups = Checkup.objects.filter(dept_id=dept)
            serializer = serializers.CheckupSerializer(ups, many=True)
            return json_response_true("get successfully", {
                "checkuplist": serializer.data
            })
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

    def delete(self, request):
        try:
            id_list = request.data
            assert id_list is not None
            for i in id_list:
                assert Department.objects.get(id=i) is not None
            for i in id_list:
                Department.objects.get(id=i).delete()
            return json_response_true("delete all departments successfully")
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
            if data["manager"]:
                res.manager = data["manager"]
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

    def delete(self, request):
        try:
            id_list = request.data
            assert id_list is not None
            for i in id_list:
                assert Medicine.objects.get(id=i) is not None
            for i in id_list:
                Medicine.objects.get(id=i).delete()
            return json_response_true("delete all medicine successfully")
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

class InstrumentationAPIView(APIView):
    def init(request):
        try:
            init_instrumentation()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            res = Instrumentation.objects.all()
            serializer = serializers.InstrumentationSerializer(res, many=True)
            return json_response_true("get successfully", {
                "instrumentationlist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request):
        try:
            id_list = request.data
            assert id_list is not None
            for i in id_list:
                assert Instrumentation.objects.get(id=i) is not None
            for i in id_list:
                Instrumentation.objects.get(id=i).delete()
            return json_response_true("delete all instrumentation successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.InstrumentationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response_true("create new instrumentation successfully", {
                "instrumentation": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            id = data["id"]
            assert id is not None
            res = Instrumentation.objects.get(id=id)
            if data["name"]:
                res.name = data["name"]
            if data["dept_id"]:
                res.dept_id = Department.objects.get(id=data["dept_id"])
            if data["description"]:
                res.description = data["description"]
            if data["method"]:
                res.method = data["method"]
            res.save()
            serializer = serializers.InstrumentationSerializer(res, many=False)
            return json_response_true("update instrumentation successfully", {
                "instrumentation": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class InstrumentationAPISingleView(APIView):
    def get(self, request, id):
        try:
            res = Instrumentation.objects.get(id=id)
            serializer = serializers.InstrumentationSerializer(res, many=False)
            return json_response_true("get successfully", {
                "instrumentation": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request, id):
        try:
            res = Instrumentation.objects.get(id=id)
            serializer = serializers.InstrumentationSerializer(res, many=False)
            Instrumentation.objects.get(id=id).delete()
            return json_response_true("delete successfully", {
                "instrumentation": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class CheckupAPIView(APIView):
    def init(request):
        try:
            init_checkup()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            res = Checkup.objects.all()
            serializer = serializers.CheckupSerializer(res, many=True)
            return json_response_true("get successfully", {
                "checkuplist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request):
        try:
            id_list = request.data
            assert id_list is not None
            for i in id_list:
                assert Checkup.objects.get(id=i) is not None
            for i in id_list:
                Checkup.objects.get(id=i).delete()
            return json_response_true("delete all checkups successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.CheckupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response_true("create new checkup successfully", {
                "checkup": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            id = data["id"]
            assert id is not None
            res = Checkup.objects.get(id=id)
            if data["name"]:
                res.name = data["name"]
            if data["dept_id"]:
                res.dept_id = Department.objects.get(id=data["dept_id"])
            if data["price"]:
                res.price = data["price"]
            if data["description"]:
                res.description = data["description"]
            res.save()
            serializer = serializers.CheckupSerializer(res, many=False)
            return json_response_true("update checkup successfully", {
                "checkup": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class CheckupAPISingleView(APIView):
    def get(self, request, id):
        try:
            res = Checkup.objects.get(id=id)
            serializer = serializers.CheckupSerializer(res, many=False)
            return json_response_true("get successfully", {
                "checkup": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request, id):
        try:
            res = Checkup.objects.get(id=id)
            serializer = serializers.CheckupSerializer(res, many=False)
            Checkup.objects.get(id=id).delete()
            return json_response_true("delete successfully", {
                "checkup": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class HospitalizationAPIView(APIView):
    def init(request):
        try:
            init_hospitalization()
            return json_response_true("init successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def get(self, request):
        try:
            res = Hospitalization.objects.all()
            serializer = serializers.HospitalizationSerializer(res, many=True)
            return json_response_true("get successfully", {
                "hospitalizationlist": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request):
        try:
            id_list = request.data
            assert id_list is not None
            for i in id_list:
                assert Hospitalization.objects.get(id=i) is not None
            for i in id_list:
                Hospitalization.objects.get(id=i).delete()
            return json_response_true("delete all hospitalization successfully")
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def post(self, request):
        try:
            serializer = serializers.HospitalizationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response_true("create new hospitalization successfully", {
                "hospitalization": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def put(self, request):
        try:
            data = request.data
            id = data["id"]
            assert id is not None
            res = Hospitalization.objects.get(id=id)
            if data["case_id"]:
                res.case_id = data["case_id"]
                # assert Case.objects.get(id=d.case_id) is not None
            if data["price"]:
                res.price = data["price"]
            if data["bg_time"]:
                res.bg_time = datetime.strptime(data["bg_time"], '%Y-%m-%d')
            if data["ed_time"]:
                res.ed_time = datetime.strptime(data["ed_time"], '%Y-%m-%d')
            assert res.ed_time >= res.bg_time
            res.save()
            serializer = serializers.HospitalizationSerializer(res, many=False)
            return json_response_true("update hospitalization successfully", {
                "hospitalization": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

class HospitalizationAPISingleView(APIView):
    def get(self, request, id):
        try:
            res = Hospitalization.objects.get(id=id)
            serializer = serializers.HospitalizationSerializer(res, many=False)
            return json_response_true("get successfully", {
                "hospitalization": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))

    def delete(self, request, id):
        try:
            res = Hospitalization.objects.get(id=id)
            serializer = serializers.HospitalizationSerializer(res, many=False)
            Hospitalization.objects.get(id=id).delete()
            return json_response_true("delete successfully", {
                "hospitalization": serializer.data
            })
        except (Exception, BaseException) as e:
            return json_response_false("invalid request, reason: " + str(e))