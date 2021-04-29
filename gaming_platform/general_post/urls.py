from django.urls import path
from . import views


urlpatterns = [
    path('post/teste/', views.hello, name='hello'),
    path('', views.PostListView.as_view() ,name='home'),
]