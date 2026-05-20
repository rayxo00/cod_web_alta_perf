"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suporte/', views.pagina_suporte, name='pagina_suporte'),
    path('favoritos/', views.pagina_favoritos, name='pagina_favoritos'),
    path('temas/fantasia/', views.pagina_fantasia, name='pagina_fantasia'),
    path('temas/ficção/', views.pagina_ficção, name='pagina_ficção'),
    path('temas/romance/', views.pagina_romance, name='pagina_romance'),
    path('temas/suspense/', views.pagina_suspense, name='pagina_suspense'),
    path('temas/terror/', views.pagina_terror, name='pagina_terror'),
    path('comentarios/comentDistopia/', views.pagina_comentarios_distopia, name='pagina_comentarios_distopia'),   
    path('comentarios/comentFantasia/', views.pagina_comentarios_fantasia, name='pagina_comentarios_fantasia'),
    path('comentarios/comentFicção/', views.pagina_comentarios_ficção, name='pagina_comentarios_ficção'),
    path('comentarios/comentRomance/', views.pagina_comentarios_romance, name='pagina_comentarios_romance'),
    path('comentarios/comentSuspense/', views.pagina_comentarios_suspense, name='pagina_comentarios_suspense'),
    path('comentarios/comentTerror/', views.pagina_comentarios_terror, name='pagina_comentarios_terror'),
    path('admin/', admin.site.urls),
    path('temas/distopia/', views.pagina_distopia, name='pagina_distopia'),
    path('favoritar/<int:livro_id>/', views.favoritar_livro, name='favoritar_livro'),
    path('login/', views.login_cadastro_usuario, name='login_usuario'),
    path('favoritos/', views.pagina_favoritos, name='pagina_favoritos'),
    path('conta/', views.pagina_conta, name='pagina_conta'),
    path('logout/', views.logout_usuario, name='logout_usuario'),

    path('favoritar-js/', views.favoritar_livro_js, name='favoritar_livro_js'),

]
