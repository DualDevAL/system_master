from django.urls import path

from . import views



urlpatterns = [

    path('', views.GameListView.as_view() ,name='home'),
    path('', views.CancelarDeleteView.as_view() ,name='home'),
    path('category/home_category/', views.CategoryListView.as_view() ,name='home_category'),
    path('publisher/home_publisher/', views.PublisherListView.as_view() ,name='home_publisher'),
    path('age/home_age/', views.AgeListView.as_view() ,name='home_age'),
    path('system/home_system/', views.SystemListView.as_view() ,name='home_system'),
    path('engine/home_engine/', views.EngineListView.as_view() ,name='home_engine'),
    path('designer/home_designer/', views.DesignerListView.as_view() ,name='home_designer'),
    path('language/home_language/', views.Select_LanguageListView.as_view() ,name='home_language'),
    path('language/home_min_requirements/', views.MinimumRequirementsListView.as_view() ,name='home_min_requirements'),
    path('max_requirements/home_max_requirements/', views.RecommendedRequirementsListView.as_view() ,name='home_max_requirements'),
    path('player/home_player/', views.PlayerListView.as_view() ,name='home_player'),


    #====================================================================================================

    path('post/new/', views.GameCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.GameDetaiView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.GameDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/edit/', views.GameUpdateView.as_view(), name='post_edit'),
    path('post/atributes',views.AtributesListView.as_view(), name='post_atributes'),

    #===================================CLASS CATEGORY ================================================
    path('category/category_new', views.CategoryCreateView.as_view(), name='category_new'),
    path('category/<int:pk>/category_edit', views.CategoryUpdateView.as_view(), name='category_edit'),

    #===================================CLASS PUBLISHER ================================================
    path('publisher/publisher_new', views.PublisherCreateView.as_view(), name='publisher_new'),
    path('publisher/<int:pk>/publisher_edit', views.PublisherUpdateView.as_view(), name='publisher_edit'),

    #===================================CLASS OPERATIONA_SYSTEM================================================
    path('system/system_new', views.SystemCreateView.as_view(), name='system_new'),
    path('system/<int:pk>/system_edit', views.SystemUpdateView.as_view(), name='system_edit'),

    #===================================CLASS AGE_RANGE ================================================
    path('age/age_new', views.AgeCreateView.as_view(), name='age_new'),
    path('age/<int:pk>/age_edit', views.AgeUpdateView.as_view(), name='age_edit'),

    #===================================CLASS GRAPHIC_ENGINE ================================================
    path('engine/engine_new', views.EngineCreateView.as_view(), name='engine_new'),
    path('engine/<int:pk>/designer_edit', views.EngineUpdateView.as_view(), name='engine_edit'),

    #===================================CLASS DESIGNER================================================
    path('designer/designer_new', views.DesignerCreateView.as_view(), name='designer_new'),
    path('designer/<int:pk>/designer_edit', views.DesignerUpdateView.as_view(), name='designer_edit'),

    #===================================CLASS LANGUAGE================================================
    path('language/language_new', views.Select_LanguageCreateView.as_view(), name='language_new'),
    path('language/<int:pk>/language_edit', views.Select_LanguageUpdateView.as_view(), name='language_edit'),

#===================================CLASS MINIMUM_REQUIREMENTS================================================
    path('min_requirements/min_requirements_new', views.MinimumRequirementsCreateView.as_view(), name='min_requirements_new'),
    path('min_requirements/<int:pk>/min_requirements_edit', views.MinimumRequirementsUpdateView.as_view(), name='min_requirements_edit'),

#===================================CLASS REQUIREMENTS_RECOMENDS================================================
    path('max_requirements/max_requirements_new', views.RecommendedRequirementsCreateView.as_view(), name='max_requirements_new'),
    path('max_requirements/<int:pk>/max_requirements_edit', views.RecommendedRequirementsUpdateView.as_view(), name='max_requirements_edit'),

#===================================CLASS REQUIREMENTS_RECOMENDS================================================
    path('player/player_new', views.PlayerCreateView.as_view(), name='player_new'),
    path('player/<int:pk>/player_edit', views.PlayerUpdateView.as_view(), name='player_edit'),


]

