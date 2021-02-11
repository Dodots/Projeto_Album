from django.contrib import admin
from .models import Postagem

class ListandoPostagem(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'foto_postagem', 'usuario', 'publicada')
    list_display_links = ('titulo', 'usuario')
    search_fields = ('titulo', )
    list_filter = ('publicada', )
    list_per_page = 20  

admin.site.register(Postagem, ListandoPostagem)