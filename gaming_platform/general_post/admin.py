from django.contrib import admin
from .models import Post
# Register yo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
#admin.site.register(Post)

