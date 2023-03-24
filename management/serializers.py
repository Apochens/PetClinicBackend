from rest_framework import serializers
from management import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicine
        fields = "__all__"

class InstrumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrumentation
        fields = "__all__"

class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checkup
        fields = "__all__"

# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Role
#         fields = "__all__"