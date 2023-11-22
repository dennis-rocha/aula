from django.urls import path
from app_aula.views import home

urlpatterns = [
    path('', home),
]