from django.contrib import admin
from .models import Post, GameCategory, publisher, Select_Language, Operational_System
# Register yo


@admin.register(GameCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'servant', 'published')
    list_filter = ('name', 'servant', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Select_Language)
class Select_Language(admin.ModelAdmin):
    list_display = ('name', 'servant', 'published')
    list_filter = ('name', 'servant', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Operational_System)
class Operational_System(admin.ModelAdmin):
    list_display = ('name', 'servant', 'published')
    list_filter = ('name', 'servant', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(publisher)
class publisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'servant', 'published')
    list_filter = ('name', 'servant', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Post)
class PostgAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'value')
    list_filter = ('publisher', 'value', 'author')
    raw_id_fields = ('author',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


#admin.site.register(GameCategory)



