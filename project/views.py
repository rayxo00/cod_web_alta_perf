from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livro, Favorito, Comentario
from django.contrib.auth import logout
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def pagina_suporte(request):
    return render(request, 'suporte/suporte.html')

def pagina_favoritos(request):
    return render(request, 'favoritos/favoritos.html')

def pagina_distopia(request):
    return render(request, 'temas/distopia.html')

def pagina_fantasia(request):
    return render(request, 'temas/fantasia.html')

def pagina_ficção(request):
    return render(request, 'temas/ficção.html')

def pagina_romance(request):
    return render(request, 'temas/romance.html')

def pagina_suspense(request):
    return render(request, 'temas/suspense.html')

def pagina_terror(request):
    return render(request, 'temas/terror.html')

def pagina_comentarios_distopia(request):
    return render(request, 'comentarios/comentDistopia.html') 

def pagina_comentarios_fantasia(request):
    return render(request, 'comentarios/comentFantasia.html')

def pagina_comentarios_ficção(request):
    return render(request, 'comentarios/comentFicção.html')

def pagina_comentarios_romance(request):
    return render(request, 'comentarios/comentRomance.html')

def pagina_comentarios_suspense(request):
    return render(request, 'comentarios/comentSuspense.html')

def pagina_comentarios_terror(request):
    return render(request, 'comentarios/comentTerror.html')

def pagina_distopia(request):
    livros = Livro.objects.filter(categoria='distopia')
    return render(request, 'temas/distopia.html', {'livros': livros})

@login_required(login_url='login_usuario')
def favoritar_livro(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livro, id=livro_id)
        Favorito.objects.get_or_create(usuario=request.user, livro=livro)
        return redirect('pagina_favoritos')
    
    return redirect('pagina_distopia')

def login_cadastro_usuario(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'cadastro':
            nome = request.POST.get('nome').strip()
            email = request.POST.get('email').strip()
            senha = request.POST.get('senha')
            confirma = request.POST.get('confirma_senha')

            if not nome or not email or not senha:
                messages.error(request, 'Preencha todos os campos.')
            elif senha != confirma:
                messages.error(request, 'As senhas não coincidem.')
            elif User.objects.filter(username=email).exists():
                messages.error(request, 'Este e-mail já está cadastrado.')
            else:
                usuario = User.objects.create_user(username=email, email=email, password=senha)
                usuario.first_name = nome
                usuario.save()
                messages.success(request, 'Conta criada com sucesso! Faça o login.')
                
                return redirect('pagina_favoritos')

        elif action == 'login':
            email = request.POST.get('email').strip()
            senha = request.POST.get('senha')

            usuario = authenticate(request, username=email, password=senha)
            if usuario is not None:
                login(request, usuario)
                
                return redirect('index')
            else:
                messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'login/login.html')

@login_required(login_url='login_usuario')
def pagina_favoritos(request):
    meus_favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'favoritos/favoritos.html', {'favoritos': meus_favoritos})

@login_required(login_url='login_usuario') 
def pagina_conta(request):
    return render(request, 'login/conta.html', {'usuario': request.user})

def logout_usuario(request):
    logout(request)
    return redirect(reverse('login_usuario') + '?aba=cadastro')


from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required(login_url='login_usuario')
@require_POST
def favoritar_livro_js(request):
    import json
    data = json.loads(request.body)
    titulo = data.get('titulo')
    autor = data.get('autor')
    
    livro, _ = Livro.objects.get_or_create(titulo=titulo, defaults={'autor': autor, 'categoria': 'distopia'})
    
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, livro=livro)
    if not created:
        favorito.delete()
        favoritado = False
    else:
        favoritado = True
        
    return JsonResponse({'favoritado': favoritado})

def pagina_distopia(request):
    livros = Livro.objects.filter(categoria='distopia')

    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/distopia.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })

def pagina_fantasia(request):
    livros = Livro.objects.filter(categoria='fantasia')
    
    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/fantasia.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })

def pagina_ficção(request):
    livros = Livro.objects.filter(categoria='ficção')
    
    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/ficção.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })

def pagina_romance(request):
    livros = Livro.objects.filter(categoria='romance')
    
    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/romance.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })

def pagina_suspense(request):
    livros = Livro.objects.filter(categoria='suspense')
    
    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/suspense.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })

def pagina_terror(request):
    livros = Livro.objects.filter(categoria='terror')
    
    titulos_favoritados = []
    
    if request.user.is_authenticated:
        titulos_favoritados = Favorito.objects.filter(usuario=request.user).values_list('livro__titulo', flat=True)
    
    return render(request, 'temas/terror.html', {
        'livros': livros, 
        'titulos_favoritados': titulos_favoritados
    })
    


def pagina_comentarios_distopia(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_distopia')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_jogos': todos_comentarios.filter(livro_slug='jogos-vorazes'),
        'comentarios_estilhaca': todos_comentarios.filter(livro_slug='estilhaca-me'),
        'comentarios_divergente': todos_comentarios.filter(livro_slug='divergente'),
    }

    return render(request, 'comentarios/comentDistopia.html', contexto)

def pagina_comentarios_fantasia(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_fantasia')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_rainha': todos_comentarios.filter(livro_slug='a-rainha-vermelha'),
        'comentarios_sangue': todos_comentarios.filter(livro_slug='de-sangue-e-cinzas'),
        'comentarios_principe': todos_comentarios.filter(livro_slug='o-principe-cruel'),
    }

    return render(request, 'comentarios/comentFantasia.html', contexto)


def pagina_comentarios_ficção(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_ficção')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_duna': todos_comentarios.filter(livro_slug='duna'),
        'comentarios_2001': todos_comentarios.filter(livro_slug='2001-uma-odisseia-no-espaco'),
        'comentarios_robo': todos_comentarios.filter(livro_slug='eu-robo'),
    }

    return render(request, 'comentarios/comentFicção.html', contexto)


def pagina_comentarios_romance(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_romance')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_teoricamente': todos_comentarios.filter(livro_slug='amor-teoricamente'),
        'comentarios_hipotese': todos_comentarios.filter(livro_slug='hipotese-do-amor'),
        'comentarios_acordo': todos_comentarios.filter(livro_slug='o-acordo'),
    }

    return render(request, 'comentarios/comentRomance.html', contexto)


def pagina_comentarios_suspense(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_suspense')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_verity': todos_comentarios.filter(livro_slug='verity'),
        'comentarios_misery': todos_comentarios.filter(livro_slug='misery'),
        'comentarios_sobrou_nenhum': todos_comentarios.filter(livro_slug='e-nao-sobrou-nenhum'),
    }

    return render(request, 'comentarios/comentSuspense.html', contexto)


def pagina_comentarios_terror(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('mensagem')
            livro_nome = request.POST.get('livro_nome') 

            if texto and livro_nome:
                Comentario.objects.create(
                    livro_slug=livro_nome,
                    usuario=request.user,
                    texto=texto
                )
        return redirect('pagina_comentarios_terror')

    todos_comentarios = Comentario.objects.all().order_by('-data_criacao')

    contexto = {
        'comentarios_it': todos_comentarios.filter(livro_slug='it-acoisa'),
        'comentarios_dracula': todos_comentarios.filter(livro_slug='dracula'),
        'comentarios_exorcista': todos_comentarios.filter(livro_slug='o-exorcista'),
    }

    return render(request, 'comentarios/comentTerror.html', contexto)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    