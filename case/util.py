from . import models
import json
from PetClinicBackend import settings


def init_category():
    with open('data/category.json', encoding='utf-8') as fr:
        datas = json.loads(fr.read())
        for data in datas:
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
