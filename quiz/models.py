import enum

from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from .validators import JsonFieldValidator


class QuestionType(enum.StrEnum):
    SINGLE = 'single'
    MULTI = 'multi'
    TRUEORFALSE = 'tof'
    TEXT = 'text'


class DiseaseType(models.TextChoices):
    INFECTIOUS = 'infectious', "传染病"
    PARASITIC = 'parasitic', "寄生虫病"
    INTERNAL = 'internal', "内科"
    OBSTETRIC = 'obstetric', "外产科疾病"
    SURGERY = 'surgery', "常用手术"
    IMMUNOLOGY = 'immunology', "免疫"


class AnswerChoice(models.IntegerChoices):
    A = 1, 'A'
    B = 2, 'B'
    C = 3, 'C'
    D = 4, 'D'


class TrueOrFalseAnswerChoice(models.IntegerChoices):
    true = 1, "对"
    false = 0, "错"


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)
    duration = models.IntegerField(validators=[
        validators.MaxValueValidator(120),
        validators.MinValueValidator(10)
    ])
    students = models.JSONField(validators=[
        JsonFieldValidator(['list'])
    ])
    questions = models.JSONField(validators=[
        JsonFieldValidator([type for type in QuestionType])
    ])


class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    score = models.IntegerField()


class SingleChoiceQuestion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    optionA = models.CharField(max_length=100, verbose_name="Option A")
    optionB = models.CharField(max_length=100, verbose_name="Option B")
    optionC = models.CharField(max_length=100, verbose_name="Option C")
    optionD = models.CharField(max_length=100, verbose_name="Option D")
    answer = models.CharField(max_length=10, choices=AnswerChoice.choices, default=AnswerChoice.A)
    disease_type = models.CharField(
        max_length=20,
        choices=DiseaseType.choices,
        default=DiseaseType.INTERNAL
    )
    score = models.IntegerField(default=5, validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(10)
    ])


class MultiChoiceQuestion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answerA = models.BooleanField(default=False)
    answerB = models.BooleanField(default=False)
    answerC = models.BooleanField(default=False)
    answerD = models.BooleanField(default=False)
    disease_type = models.CharField(
        max_length=20,
        choices=DiseaseType.choices,
        default=DiseaseType.INTERNAL
    )
    score = models.IntegerField(default=5, validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(10)
    ])


class TrueOrFalseQuestion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    answer = models.CharField(
        max_length=20,
        choices=TrueOrFalseAnswerChoice.choices,
        default=TrueOrFalseAnswerChoice.false
    )
    disease_type = models.CharField(
        max_length=20,
        choices=DiseaseType.choices,
        default=DiseaseType.INTERNAL
    )
    score = models.IntegerField(default=5, validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(5)
    ])


class TextQuestion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    answer = models.TextField(max_length=1000)
    disease_type = models.CharField(
        max_length=20,
        choices=DiseaseType.choices,
        default=DiseaseType.INTERNAL
    )
    score = models.IntegerField(default=5, validators=[
        validators.MinValueValidator(10),
        validators.MaxValueValidator(20)
    ])