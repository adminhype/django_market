from django.urls import path
from .views import send_fruits_page, single_fruit_view, send_fruits_info_view

urlpatterns = [
    path('', send_fruits_page, name='fruit-list'),
    path('<int:fruit_id>/', single_fruit_view, name='single-fruit'),
    path('info/', send_fruits_info_view, name='fruit-info'),
]
