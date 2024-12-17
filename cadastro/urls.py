from django.urls import path
from . import views

app_name ='usuario'

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]