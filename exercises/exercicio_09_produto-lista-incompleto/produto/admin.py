from django.contrib import admin
from produto.models import Categoria, Produto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Categoria, CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria']
    search_fields = ['nome']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nome',)}
    list_editable = ['slug', 'categoria']

admin.site.register(Produto, ProdutoAdmin)
