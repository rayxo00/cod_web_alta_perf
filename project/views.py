from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livro, Favorito

# View para renderizar a página inicial
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

# View para renderizar a página de distopia
def pagina_distopia(request):
    livros = Livro.objects.filter(categoria='distopia')
    return render(request, 'temas/distopia.html', {'livros': livros})

# View para favoritar
@login_required(login_url='login_usuario')
def favoritar_livro(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livro, id=livro_id)
        Favorito.objects.get_or_create(usuario=request.user, livro=livro)
        return redirect('pagina_favoritos')
    
    # Se alguém tentar aceder a esta URL por GET diretamente, volta para as distopias
    return redirect('pagina_distopia')

# View combinada de Login e Cadastro
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
                
                # CORRIGIDO: Evita o erro 405 encaminhando o utilizador diretamente 
                # para a página inicial (ou favoritos) de forma limpa.
                return redirect('index')
            else:
                messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'login/login.html')

@login_required(login_url='login_usuario')
def pagina_favoritos(request):
    meus_favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'favoritos/favoritos.html', {'favoritos': meus_favoritos})