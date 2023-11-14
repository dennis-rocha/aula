from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request,"home.html", context={
        'name' : 'Dennis',
        'lista_headers' : range(1,7)
    })