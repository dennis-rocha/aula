from django.contrib import admin
from django.urls import path
from sobre.views import home

urlpatterns = [
    path('home/', home),
]