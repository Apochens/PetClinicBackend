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
    symptom_text = models.TextField(max_length=1000, default="")
    diagnosis_text = models.TextField(max_length=1000, default="")
    treatment_text = models.TextField(max_length=1000, default="")
    symptom_pic1 = models.CharField(max_length=1000, default="")
    symptom_pic2 = models.CharField(max_length=1000, default="")
    symptom_pic3 = models.CharField(max_length=1000, default="")
    diagnosis_pic1 = models.CharField(max_length=1000, default="")
    diagnosis_pic2 = models.CharField(max_length=1000, default="")
    diagnosis_pic3 = models.CharField(max_length=1000, default="")
    treatment_pic1 = models.CharField(max_length=1000, default="")
    treatment_pic2 = models.CharField(max_length=1000, default="")
    treatment_pic3 = models.CharField(max_length=1000, default="")
    symptom_video = models.CharField(max_length=1000, default="")
    diagnosis_video = models.CharField(max_length=1000, default="")
    treatment_video = models.CharField(max_length=1000, default="")


class Checkup(models.Model):
    checkup_id = models.BigAutoField
    case_number = models.CharField(max_length=100, default="")
    checkup_item = models.CharField(max_length=100, default="")
    checkup_text = models.TextField(max_length=1000, default="")
    checkup_pic1 = models.CharField(max_length=1000, default="")
    checkup_pic2 = models.CharField(max_length=1000, default="")
    checkup_pic3 = models.CharField(max_length=1000, default="")
    checkup_video = models.CharField(max_length=1000, default="")


class Category(models.Model):
    category_id = models.BigAutoField
    # Chinese type
    title = models.CharField(max_length=1000, default="")
    # English type
    key = models.CharField(max_length=1000, default="")
    # name list
    children = models.JSONField(default=dict)


class Pictures(models.Model):
    pictures_id = models.BigAutoField
    pic = models.ImageField(upload_to='images/')


class Videos(models.Model):
    videos_id = models.BigAutoField
    video = models.FileField(upload_to='videos/')
