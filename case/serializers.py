from rest_framework import serializers
from . import models


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        exclude = ["id"]


class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checkup
        exclude = ["id"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ["id"]
