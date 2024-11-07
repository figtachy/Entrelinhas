from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # Página do admin
    path("", IndexView.as_view(), name="index"),  # Página inicial
    path("pessoa/", PessoaView.as_view(template_name='pessoa.html'), name="pessoa"),  # Página para exibir Pessoa
    path("livro/", LivroView.as_view(template_name='livro.html'), name="livro"),  # Página para exibir Livros
    path("estante/", EstanteView.as_view(template_name='estante.html'), name="estante"),  # Página para exibir Estante Virtual
    path("comentario/", ComentarioView.as_view(template_name='comentario.html'), name="comentario"),  # Página para exibir Comentários
    path("forum/", ForumView.as_view(template_name='forum.html'), name="forum"),  # Página para exibir Fórum
    path("desafio/", DesafioLeituraView.as_view(template_name='desafio.html'), name="desafio"),  # Página para exibir Desafios de Leitura
    path('forum/<int:id>/', ForumDetalhesView.as_view(), name='forum_detalhes'),  # Detalhes do fórum
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
