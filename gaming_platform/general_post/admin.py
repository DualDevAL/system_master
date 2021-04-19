from django.contrib import admin
from .models import Post
# Register yo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
#admin.site.register(Post)

