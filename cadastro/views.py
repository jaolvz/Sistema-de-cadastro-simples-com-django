from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario 

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request,'cadastro.html')

def cadastrar (request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif  request.method =='POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario (usuario=usuario, email=email, senha=senha)
        usuario.save()
        return render(request,'index.html')