from django.contrib import admin
from .models import Post, GameCategory
# Register yo


@admin.register(GameCategory)# usa esse se não funcionar as alteração
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'servant', 'published')
    list_filter = ('name', 'servant', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Post)
class PostgAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'value')
    list_filter = ('status', 'value', 'author')
    #readonly_fields = ('visualizar_imagem',)
    #date_hierarchy = 'disponivel'
    raw_id_fields = ('author',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

    '''def visualizar_imagem(self, obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada"'''

#admin.site.register(GameCategory)



