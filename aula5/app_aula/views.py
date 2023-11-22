from django.shortcuts import render

# Create your views here.
def home (request):
    if request.POST:
        dados = request.POST["texto"]
        print('Olá mundo', dados)
    return render(request,"app_aula/home.html")
