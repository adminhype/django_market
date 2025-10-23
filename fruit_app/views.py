from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import json

from .fruits_data import fruits

fruits = [
    {"name": "Apfel", "weight": 100, "color": "red"},
    {"name": "Banane", "weight": 120, "color": "yellow"},
    {"name": "Orange", "weight": 150, "color": "orange"},
    {"name": "Birne", "weight": 130, "color": "green"},
    {"name": "Kirsche", "weight": 10, "color": "red"}
]


def send_fruits_page(request):
    return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})


def send_fruits_view(request):
    return HttpResponse(json.dumps(fruits), content_type="application/json")


def single_fruit_view(request, fruit_id):
    try:
        fruit = fruits[fruit_id]
        return JsonResponse(fruit)
    except IndexError:
        return JsonResponse({'error': 'Fruit not found'})
