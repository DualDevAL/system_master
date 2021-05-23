from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view() ,name='home'),
    path('', views.CancelarDeleteView.as_view() ,name='home'),
    path('post/new/', views.GameCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.GameDetaiView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.GameDeleteView.as_view(), name='post_delete'),
]
