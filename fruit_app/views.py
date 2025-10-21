from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import json

from .fruits_data import fruits


def send_fruits_view(request):
    return HttpResponse(json.dumps(fruits), content_type="application/json")


def single_fruit_view(request, fruit_id):
    try:
        fruit = fruits[fruit_id]
        return JsonResponse(fruit)
    except IndexError:
        return JsonResponse({'error': 'Fruit not found'})
