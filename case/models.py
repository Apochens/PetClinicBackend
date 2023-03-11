from django.db import models


# Create your models here.
class Case(models.Model):
    case_id = models.BigAutoField
    case_number = models.CharField(max_length=100, unique=True, default="")
    disease_type = models.CharField(max_length=100, default="")
    disease_name = models.CharField(max_length=100, default="")
    pet_name = models.CharField(max_length=100, default="")
    pet_species = models.CharField(max_length=100, default="")
    pet_age = models.IntegerField(default=-1)
    owner_name = models.CharField(max_length=100, default="")
    owner_phone = models.CharField(max_length=100, default="")
    expense = models.FloatField(default=0.0)
    symptom = models.JSONField(default=dict)
    diagnosis_result = models.JSONField(default=dict)
    treatment = models.JSONField(default=dict)


class Checkup(models.Model):
    checkup_id = models.BigAutoField
    case_number = models.CharField(max_length=100, unique=True, default="")
    checkup_item = models.CharField(max_length=100, default="")
    checkup_result = models.JSONField(default=dict)
