from django.urls import path
from portfolio.views import home, home_dois

urlpatterns = [
    path('', home),
    path('home/', home_dois),
]