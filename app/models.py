from django.db import models
from django.contrib.auth.models import User

# Modelo para "Pessoa"
class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.user.username

# Modelo para "Livros"
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()
    sinopse = models.TextField()
    capa = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.titulo

# Modelo para "Estante Virtual"
class EstanteVirtual(models.Model):
    nome = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro)

    def __str__(self):
        return self.nome

# Modelo para "Comentário"
class Comentario(models.Model):
    texto = models.TextField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentário de {self.pessoa.user.username} sobre {self.livro.titulo}'

# Modelo para "Fórum"
class Forum(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Modelo para "Postagem do Fórum"
class Postagem(models.Model):
    mensagem = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return f'Postagem de {self.pessoa.user.username} no fórum {self.forum.titulo}'

# Modelo para "Desafios de Leitura"
class DesafioLeitura(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome
