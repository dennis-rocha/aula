from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"portfolio/home.html")

def home_dois(request):
    return render(request,"portfolio/home2.html")
