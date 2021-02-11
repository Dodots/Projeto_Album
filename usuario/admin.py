from django.contrib import admin
from .models import Perfil


class ListandoPerfil(admin.ModelAdmin):
    list_display = ('nome_completo', 'telefone', 'usuario')
    list_display_links = ('nome_completo', 'usuario')
    search_fields = ('nome_completo', )
    list_per_page = 20  


admin.site.register(Perfil, ListandoPerfil)