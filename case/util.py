import os

from . import models
import json
from PetClinicBackend import settings


def init_category():
    with open('data/category.json', encoding='utf-8') as fr:
        categorys = json.loads(fr.read())
        for data in categorys:
            c = models.Category()
            c.title = data['title']
            c.key = data['key']
            c.children = data['children']
            c.save()


def process_urls(serializer_data):
    for record in serializer_data:
        for key in record.keys():
            if "pic" in key or "video" in key:
                if record[key] is not None:
                    record[key] = settings.WEB_HOST_MEDIA_URL + record[key]
                else:
                    record[key] = ""


def init_cases():
    with open('data/cases.json', encoding='utf-8') as fr:
        cases = json.loads(fr.read())
        for data in cases:
            c = models.Case()
            c.disease_type = data['disease_type']
            c.disease_name = data['disease_name']
            c.case_number = data['case_number']
            c.pet_name = data['pet_name']
            c.pet_species = data['pet_species']
            c.pet_age = data['pet_age']
            c.owner_name = data['owner_name']
            c.owner_phone = data['owner_phone']
            c.symptom_text = data['symptom_text']
            c.diagnosis_text = data['diagnosis_text']
            c.treatment_text = data['treatment_text']
            c.symptom_pic1 = data['symptom_pic1']
            c.symptom_pic2 = data['symptom_pic2']
            c.symptom_pic3 = data['symptom_pic3']
            c.diagnosis_pic1 = data['diagnosis_pic1']
            c.diagnosis_pic2 = data['diagnosis_pic2']
            c.diagnosis_pic3 = data['diagnosis_pic3']
            c.treatment_pic1 = data['treatment_pic1']
            c.treatment_pic2 = data['treatment_pic2']
            c.treatment_pic3 = data['treatment_pic3']
            c.symptom_video = data['symptom_video']
            c.diagnosis_video = data['diagnosis_video']
            c.treatment_video = data['treatment_video']
            c.save()


def init_checkups():
    with open('data/cases_checkup.json', encoding='utf-8') as fr:
        checkups = json.loads(fr.read())
        for data in checkups:
            c = models.Checkup()
            c.case_number = data['case_number']
            c.checkup_item = data['checkup_item']
            c.checkup_text = data['checkup_text']
            c.checkup_pic1 = data['checkup_pic1']
            c.checkup_pic2 = data['checkup_pic2']
            c.checkup_pic3 = data['checkup_pic3']
            c.checkup_video = data['checkup_video']
            c.save()
