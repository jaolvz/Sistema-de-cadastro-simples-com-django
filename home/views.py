from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Perfil
import os
from django.contrib.auth import logout

@login_required(login_url='usuario:login')
def pag_inicial(request):
    user = request.user
    posts = Post.objects.order_by('-postado') 
    posts_com_urls = []
    for post in posts:
        foto_perfil = Perfil.url_foto_perfil(post.autor)
        foto_capa = Perfil.url_foto_capa(post.autor)
        posts_com_urls.append({
            'post': post,
            'foto_perfil': foto_perfil,
            'foto_capa': foto_capa
        })
    contexto = {'user':user, 'posts':posts_com_urls}
    return render(request,'pag_inicial.html',contexto)


@login_required(login_url='usuario:login')
def perfil(request,usuario):
    Usuario_perfil = get_object_or_404(User, username=usuario)
    if Usuario_perfil:
        posts_usuario = Post.retornar_posts_por_usuario(Usuario_perfil)
        foto_perfil_url = Perfil.url_foto_perfil(Usuario_perfil)
        foto_capa_url = Perfil.url_foto_capa(Usuario_perfil)
        contexto = {'usuario':Usuario_perfil,'posts_usuario':posts_usuario, 'perfil_url':foto_perfil_url, 'capa_url':foto_capa_url }
        return render(request,'perfil.html',contexto)
    else:
        return HttpResponse('algo de errado')
    
@login_required(login_url='usuario:login')
def logout_sessao(request):
    logout(request)  
    return redirect('usuario:login') 


def handler404(request, exception):
    return render(request, '404.html')

@login_required(login_url='usuario:login')
def upload_post (request):
    if request.method == 'POST':
        txt_post = request.POST.get('txt_post')
        autor = request.user
        post= Post.objects.create(autor=autor, conteudo = txt_post)
        return redirect('home:pag_inicial')
    else:
        return redirect('home:perfil')
    
@login_required(login_url='usuario:login')
def upload_img_perfil(request):
    if request.method == "POST":
        arq = request.FILES.get('img_perfil')
        if arq:
            try:
                perfil = Perfil.objects.get(Usuario=request.user)
            
                if perfil.foto_perfil:
                    caminho_antigo =  os.path.join('media/', perfil.foto_perfil.name)
                    if os.path.isfile(caminho_antigo):
                        os.remove(caminho_antigo)
                nome_base, ext =os.path.splitext(arq.name)
                novo_nome = f"{request.user.username}{ext}"
                arq.name = novo_nome
                
                perfil.foto_perfil = arq
                perfil.save()
                return redirect('home:perfil', usuario=request.user.username)

            except Perfil.DoesNotExist:
                return redirect('home:pag_inicial')

        else:
            return redirect('home:pag_inicial')
    else:
        return redirect('home:pag_inicial')

    

@login_required(login_url='usuario:login')
def upload_img_capa(request):
    if request.method == "POST":
        arq = request.FILES.get('img_capa')
        if arq:
            try:
                perfil = Perfil.objects.get(Usuario=request.user)

                # Remover a capa antiga, se existir
                if perfil.foto_capa:
                    caminho_antigo = os.path.join('media/', perfil.foto_capa.name)
                    if os.path.isfile(caminho_antigo):
                        os.remove(caminho_antigo)

                # Renomear o arquivo enviado
                nome_base, ext = os.path.splitext(arq.name)
                novo_nome = f"{request.user.username}_capa{ext}"
                arq.name = novo_nome

                # Atualizar o campo de foto_capa no perfil
                perfil.foto_capa = arq
                perfil.save()

                return redirect('home:perfil', usuario=request.user.username)

            except Perfil.DoesNotExist:
                return redirect('home:pag_inicial')

        else:
            # Quando nenhum arquivo é enviado
            return redirect('home:perfil', usuario=request.user.username)

    # Caso o método não seja POST
    return redirect('home:perfil', usuario=request.user.username)