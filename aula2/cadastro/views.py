from django.shortcuts import render
from cadastro.models import Cadastro

# Create your views here.
def cadastro(request):
    count = None
    palavra = None

    if request.method=='POST':
        palavra = request.POST['palavra']
        count = len(palavra)

 
    return render(request, 'home.html', context={'count': count, 'palavra': palavra})
