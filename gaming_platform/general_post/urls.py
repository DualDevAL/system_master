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

    #====================================================================================================

    path('post/new/', views.GameCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.GameDetaiView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.GameDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/edit/', views.GameUpdateView.as_view(), name='post_edit'),
    path('post/atributes',views.AtributesListView.as_view(), name='post_atributes'),

    #===================================CLASS CATEGORY ================================================
    path('category/category_new', views.CategoryCreateView.as_view(), name='category_new'),

    #===================================CLASS PUBLISHER ================================================
    path('publisher/publisher_new', views.PublisherCreateView.as_view(), name='publisher_new'),

    #===================================CLASS OPERATIONA_SYSTEM================================================
    path('system/system_new', views.SystemCreateView.as_view(), name='system_new'),

    #===================================CLASS AGE_RANGE ================================================
    path('age/age_new', views.AgeCreateView.as_view(), name='age_new'),

    #===================================CLASS GRAPHIC_ENGINE ================================================
    path('engine/engine_new', views.EngineCreateView.as_view(), name='engine_new'),


    
    
]
