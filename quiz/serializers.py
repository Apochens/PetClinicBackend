from rest_framework import serializers
from . import models


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = "__all__"


class SingleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SingleChoiceQuestion
        fields = "__all__"


class MultiChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MultiChoiceQuestion
        fields = "__all__"


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextQuestion
        fields = "__all__"


class TrueOrFalseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrueOrFalseQuestion
        fields = "__all__"

