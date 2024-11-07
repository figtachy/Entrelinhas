from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User

class IndexView(View):
    def get(self, request):
        # Recupera todos os livros cadastrados
        livros = Livro.objects.all()  
        return render(request, 'index.html', {'livros': livros})  # Passa os livros para o template

class PessoaView(View):
    template_name = 'pessoa.html'
    
    def get(self, request):
        # Obtém a pessoa relacionada ao usuário logado
        pessoa = Pessoa.objects.filter(user=request.user).first()  
        return render(request, self.template_name, {'pessoa': pessoa})

class LivroView(View):
    template_name = 'livro.html'
    
    def get(self, request):
        livros = Livro.objects.all()  # Recupera todos os livros cadastrados
        return render(request, self.template_name, {'livros': livros})

class EstanteView(View):
    template_name = 'estante.html'
    
    def get(self, request):
        estantes = EstanteVirtual.objects.all()  # Recupera todas as estantes virtuais
        return render(request, self.template_name, {'estantes': estantes})

class ComentarioView(View):
    template_name = 'comentario.html'
    
    def get(self, request):
        comentarios = Comentario.objects.all()  # Recupera todos os comentários
        return render(request, self.template_name, {'comentarios': comentarios})

class ForumView(View):
    template_name = 'forum.html'
    
    def get(self, request):
        forums = Forum.objects.all()  # Recupera todos os fóruns
        return render(request, self.template_name, {'forums': forums})

class ForumDetalhesView(View):
    def get(self, request, id):
        forum = get_object_or_404(Forum, id=id)  # Obtém o fórum pelo ID
        postagens = Postagem.objects.filter(forum=forum)  # Obtém as postagens relacionadas ao fórum
        return render(request, 'forum_detalhes.html', {'forum': forum, 'postagens': postagens})

    def post(self, request, id):
        forum = get_object_or_404(Forum, id=id)  # Obtém o fórum pelo ID
        if request.method == 'POST':
            mensagem = request.POST.get('mensagem')

            # Cria uma nova postagem no fórum
            Postagem.objects.create(
                forum=forum,
                pessoa=request.user.pessoa,  # Assumindo que o usuário tem uma pessoa associada
                mensagem=mensagem,
            )
            return redirect('forum_detalhes', id=id)  # Redireciona para a página de detalhes do fórum

class DesafioLeituraView(View):
    template_name = 'desafio.html'
    
    def get(self, request):
        desafios = DesafioLeitura.objects.all()  # Recupera todos os desafios de leitura
        return render(request, self.template_name, {'desafios': desafios})
    
    

