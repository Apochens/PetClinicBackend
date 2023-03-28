from django.db import models
from PetClinicBackend import settings


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
    symptom_text = models.TextField(max_length=1000, default="")
    diagnosis_text = models.TextField(max_length=1000, default="")
    treatment_text = models.TextField(max_length=1000, default="")
    symptom_pic1 = models.ImageField(upload_to='images/symptom/', null=True)
    symptom_pic2 = models.ImageField(upload_to='images/symptom/', null=True)
    symptom_pic3 = models.ImageField(upload_to='images/symptom/', null=True)
    diagnosis_pic1 = models.ImageField(upload_to='images/diagnosis/', null=True)
    diagnosis_pic2 = models.ImageField(upload_to='images/diagnosis/', null=True)
    diagnosis_pic3 = models.ImageField(upload_to='images/diagnosis/', null=True)
    treatment_pic1 = models.ImageField(upload_to='images/treatment/', null=True)
    treatment_pic2 = models.ImageField(upload_to='images/treatment/', null=True)
    treatment_pic3 = models.ImageField(upload_to='images/treatment/', null=True)
    symptom_video = models.FileField(upload_to='videos/', null=True)
    diagnosis_video = models.FileField(upload_to='videos/', null=True)
    treatment_video = models.FileField(upload_to='videos/', null=True)


class Checkup(models.Model):
    checkup_id = models.BigAutoField
    case_number = models.CharField(max_length=100, default="")
    checkup_item = models.CharField(max_length=100, default="")
    checkup_text = models.TextField(max_length=1000, default="")
    checkup_pic1 = models.ImageField(upload_to='images/checkup/', null=True)
    checkup_pic2 = models.ImageField(upload_to='images/checkup/', null=True)
    checkup_pic3 = models.ImageField(upload_to='images/checkup/', null=True)
    checkup_video = models.FileField(upload_to='videos/', null=True)


class Category(models.Model):
    category_id = models.BigAutoField
    # Chinese type
    title = models.CharField(max_length=1000, default="")
    # English type
    key = models.CharField(max_length=1000, default="")
    # name list
    children = models.JSONField(default=dict)
