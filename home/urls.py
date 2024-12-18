from django.urls import path
from . import views

app_name ='home'
urlpatterns = [
    path('', views.pag_inicial, name='pag_inicial'),
    path('perfil/', views.perfil,name='perfil'),
    path('upload_post',views.upload_post, name='upload_post'),
    path('logout/', views.logout_sessao, name='logout')

]