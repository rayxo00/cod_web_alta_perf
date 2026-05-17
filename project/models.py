from django.db import models
from django.contrib.auth.models import User

# Tabela que vai guardar as informações de cada livro
class Livro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    descricao = models.TextField(verbose_name="Descrição")
    imagem_url = models.CharField(max_length=500, verbose_name="Caminho da Imagem (Ex: img/capa.png)")
    link_compra = models.URLField(verbose_name="Link de Compra (Amazon)")
    categoria = models.CharField(max_length=100, verbose_name="Categoria (Ex: fantasia, distopia)")

    def __str__(self):
        return self.titulo

# Tabela que vai associar qual Usuário favoritou qual Livro
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Impede que o mesmo usuário favorite o mesmo livro mais de uma vez
        unique_together = ('usuario', 'livro') 

    def __str__(self):
        return f"{self.usuario.username} favoritou {self.livro.titulo}"