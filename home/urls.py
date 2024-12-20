from django.urls import path
from . import views

app_name ='home'
urlpatterns = [
    path('', views.pag_inicial, name='pag_inicial'),
    path('perfil/<str:usuario>', views.perfil,name='perfil'),
    path('upload_post',views.upload_post, name='upload_post'),
    path('upload_img_perfil',views.upload_img_perfil, name='upload_img_perfil'),
    path('upload_img_capa',views.upload_img_capa, name='upload_img_capa'),
    path('logout/', views.logout_sessao, name='logout')

]