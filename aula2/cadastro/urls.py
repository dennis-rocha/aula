from django.urls import path
from cadastro.views import cadastro


urlpatterns = [
    path('cadastro/', cadastro),
]