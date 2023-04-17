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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ["id"]


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pictures
        fields = "__all__"


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Videos
        fields = "__all__"
