from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from home.models import Perfil

def cadastro (request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif  request.method =='POST':
        usuario = request.POST.get('usuario')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=usuario, first_name=nome, email=email, password=senha)
        perfil = Perfil.objects.create(Usuario=user)


        return render(request,'login.html')

def login (request):
    if request.method =='GET':
        return render(request,'login.html') 
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario,password=senha)
        if user :
            login_django (request,user)
            return redirect('home:pag_inicial')
        else:
            contexto ={'erro':1}
            return render(request, 'login.html',contexto)

