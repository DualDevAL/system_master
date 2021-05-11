from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view() ,name='home'),
    path('post/new/', views.AddGameView.as_view(), name='post_new'),
    #path('add_game', views.PostAddGame.as_view(), name='addgame'),
]
