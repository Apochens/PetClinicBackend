from django.http import JsonResponse
from rest_framework import status


def json_response_false(msg: str, additional_data=None):
    if additional_data is None:
        additional_data = {}
    return JsonResponse({"success": False, "message": msg, **additional_data}, status=status.HTTP_400_BAD_REQUEST)


def json_response_true(msg: str, additional_data=None):
    if additional_data is None:
        additional_data = {}
    return JsonResponse({"success": True, "message": msg, **additional_data}, status=status.HTTP_200_OK)