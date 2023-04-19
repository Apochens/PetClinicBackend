from django.http import JsonResponse
from rest_framework import status
import csv


def json_response_false(msg: str, additional_data=None):
    if additional_data is None:
        additional_data = {}
    return JsonResponse({"success": False, "message": msg, **additional_data}, status=status.HTTP_400_BAD_REQUEST)


def json_response_true(msg: str, additional_data=None):
    if additional_data is None:
        additional_data = {}
    return JsonResponse({"success": True, "message": msg, **additional_data}, status=status.HTTP_200_OK)


def json_response_unaccepted(msg: str, additional_data=None):
    if additional_data is None:
        additional_data = {}
    return JsonResponse({"success": False, "message": msg, **additional_data}, status=status.HTTP_406_NOT_ACCEPTABLE)


def read_csv_data(file):
    with open('data/' + file, encoding='utf-8-sig') as f:
        l = []
        rows = csv.reader(f)
        for row in rows:
            l.append(row)
        return l
