from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import logout

@login_required(login_url='usuario:login')
def pag_inicial(request):
    user = request.user
    posts = Post.objects.order_by('-postado') 
    contexto = {'user':user, 'posts':posts}
    

    return render(request,'pag_inicial.html',contexto)


@login_required(login_url='usuario:login')
def perfil(request):
    return render(request,'perfil.html')

@login_required(login_url='usuario:login')
def logout_sessao(request):
    logout(request)  
    return redirect('usuario:login') 


@login_required(login_url='usuario:login')
def upload_post (request):
    if request.method == 'POST':
        txt_post = request.POST.get('txt_post')
        autor = request.user
        post= Post.objects.create(autor=autor, conteudo = txt_post)
        return redirect('home:pag_inicial')
    else:
        return redirect('home:perfil')