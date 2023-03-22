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
    symptom_pic = models.ImageField(upload_to='images/', default=None)
    symptom_video = models.FileField(upload_to='videos/', default=settings.STATIC_VID_ROOT)
    diagnosis_pic = models.ImageField(upload_to='images/', default=settings.STATIC_PIC_ROOT)
    diagnosis_video = models.FileField(upload_to='videos/', default=settings.STATIC_VID_ROOT)
    treatment_pic = models.ImageField(upload_to='images/', default=settings.STATIC_PIC_ROOT)
    treatment_video = models.FileField(upload_to='videos/', default=settings.STATIC_VID_ROOT)


class Checkup(models.Model):
    checkup_id = models.BigAutoField
    case_number = models.CharField(max_length=100, default="")
    checkup_item = models.CharField(max_length=100, default="")
    checkup_text = models.TextField(max_length=1000, default="")
    checkup_pic = models.ImageField(upload_to='images/', default=settings.STATIC_PIC_ROOT)
    checkup_video = models.FileField(upload_to='videos/', default=settings.STATIC_VID_ROOT)


class Category(models.Model):
    category_id = models.BigAutoField
    # Chinese type
    title = models.CharField(max_length=1000, default="")
    # English type
    key = models.CharField(max_length=1000, default="")
    # name list
    children = models.JSONField(default=dict)
