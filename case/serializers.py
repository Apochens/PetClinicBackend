from rest_framework import serializers
from . import models


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = "__all__"


class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checkup
        fields = "__all__"
