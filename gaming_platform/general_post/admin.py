from django.contrib import admin
from .models import Post, GameCategory, Publisher, Select_Language, Operational_System, Age_Range, Graphics_Engine, Designer, Player, MinimumRequirements, RecommendedRequirements
# Register yo


@admin.register(GameCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Select_Language)
class SelectLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(RecommendedRequirements)
class RecommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)



@admin.register(MinimumRequirements)
class MinRequirementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Designer)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Age_Range)
class AgeRangeAdmin(admin.ModelAdmin):
    list_display = ('age', 'create', 'published')
    list_filter = ('age', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('age',)

@admin.register(Graphics_Engine)
class GraphicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Operational_System)
class OperationalSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'published')
    list_filter = ('name', 'create', 'published')
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



