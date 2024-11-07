from django.contrib import admin
from .models import *

admin.site.register(Pessoa)
admin.site.register(Livro)
admin.site.register(EstanteVirtual)
admin.site.register(Comentario)
admin.site.register(Forum)
admin.site.register(Postagem)
admin.site.register(DesafioLeitura)