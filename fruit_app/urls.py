from django.urls import path
from .views import send_fruits_view, single_fruit_view

urlpatterns = [
    path('', send_fruits_view, name='fruit-list'),
    path('<int:fruit_id>/', single_fruit_view, name='single-fruit'),
]
